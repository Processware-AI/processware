---
description: 표준 프로세스 제·개정 (차원 4 Act) — act queue 를 받아 RCA → 개정 범위 결정 → PCB 승인 → 차원 1 재트리거. 4차원 PDCA 폐쇄 루프 마지막 단계. 사용 ./act start <queue_id> | --resume <trace> | --approve <trace> | --trigger-rebuild <trace>
argument-hint: "start <queue_id> | --resume <trace_id> | --approve <trace_id> [--approver <이름>] | --reject <trace_id> --reason \"...\" | --trigger-rebuild <trace_id> [--dry-run] | --status <trace_id> | --list [--status pending|running|approved|done] [+ --dry-run | --rca-method 5why|fishbone|both | --auto-approve]"
---

# 표준 프로세스 제·개정 하네스 (차원 4 Act)

대상 입력: **$ARGUMENTS**

본 커맨드는 차원 3 (`/audit`) 의 act-trigger 가 발행한 큐 (`.claude/queues/act/queue-q*.yaml`) 를 받아 **근본 원인 분석 → 개정 범위 결정 → PCB 승인 → 차원 1 재트리거** 의 4단계로 자산 개정을 자동화한다. 4차원 PDCA 의 **Act → Plan 재트리거 폐쇄 루프**.

상위 설계: `표준프로세스_AI관리체계_4차원PDCA.md` §3 차원 4 / §5.4 차원 4 재트리거 조건 / `AI-Driven CMMI Operating Platform.md` Layer 3 자동 최적화 (ML5)

---

## 0. 실행 원칙

- **act queue 가 단일 입력**: 차원 3 의 큐만 처리. 큐 외 임의 개정 트리거 금지 (사후 추적성 위해).
- **기존 자산 우선 (구성원칙 §8)**: As-Is 파일에 기존 PRO/WI 의 인용 포함 → 차원 1 빌드 시 신규 생성보다 기존 확장 채택.
- **신규 자산 절대 생성 안 함**: 본 커맨드는 As-Is 입력 파일 (`vault/02_표준/{표준}/_inputs/04_AsIs/queue-q*.md`) + MAT-001 행만 작성. POL/PRO/WI/TMP/EX 개정은 차원 1 (`/build-standard --from write`) 의 책임.
- **PCB (Process Control Board) 승인 강제**: PCB = 표준 자산 개정의 최종 승인 게이트. ISO/IEC 27001 §9.3 (관리검토) 동형. 자동 승인은 `--auto-approve` 플래그 (PoC 한정).
- **모든 trace 기록**: `.claude/runs/{trace_id}/trace.jsonl` 전수 로그. trace prefix `run-c*` (change/CAPA — audit `run-a*` / kpi `run-k*` 와 분리).
- **As-Is 입력 파일은 차원 1 의 입력**: 차원 1 빌드가 자동으로 읽어 개정에 반영. 본 커맨드는 작성만.

---

## 1. 인자 파싱 — 진입 모드 (배타적, 1개만 적용)

### 1-1. `start` 모드 — `/act start <queue_id|--batch <ids>> [--rca-method ...] [--auto-approve]`
```
/act start queue-qa1b2c3d4
/act start queue-qa1b2c3d4 --rca-method both    # 5-Why + Fishbone
/act start queue-qa1b2c3d4 --auto-approve        # PCB HITL skip (PoC)

# Phase 2 — 다중 큐 일괄 처리 (의존성 그래프 + 통합 As-Is)
/act start --batch queue-qe5f6a7b8,queue-q9d8c7b6a            # 명시적 list
/act start --batch-related queue-qa1b2c3d4                    # queue.related_to 자동 펼침
/act start --batch queue-qe5f6a7b8,queue-q9d8c7b6a --auto-approve
```

#### Phase 2 — `--batch` / `--batch-related` 동작
- `--batch <id1,id2,...>`: 명시한 큐 list 를 단일 사이클로 처리.
- `--batch-related <id>`: 시드 큐의 `dependencies.related_to[]` 를 펼쳐서 일괄 처리 (또는 revision-planner 의 1차 분석 결과로 통합 후보 자동 식별).
- 일괄 처리의 효과:
   1. **rca-analyzer** 가 큐들의 root cause 통합 분석 (공통 root cause 가 있으면 단일 root_cause.yaml 의 `merged_root_cause`).
   2. **revision-planner** 가 Mermaid 의존성 다이어그램 자동 생성 + 통합 rebuild_plan (단일 `--from write` 명령으로 다수 자산 처리 가능).
   3. **act-coordinator** 가 **통합 As-Is 파일** 작성 (`queue-batch-{first-id-suffix}.md` — frontmatter `linked_queues[]` 에 모든 큐 인용).
   4. PCB 승인 1회 (다수 큐 일괄).
- 단점·제약:
   - 의존성 충돌 (큐 간 rebuild_mode 불일치) 시 자동 abort + 사용자에게 분리 권고.
   - 통합 RCA 의 confidence 가 medium 이하면 사용자에게 분리 처리 권고.
   - 통합 As-Is 파일 1건 = 큐 다수 처리 → 차원 1 빌드 시 한 번에 다수 자산 개정 (정합 검증 부담 증가).
→ 인자 파싱:
- queue_id 가 `.claude/queues/act/queue-q*.yaml` 에 존재하고 `status in [pending, in_progress]` 확인.
- queue 가 dispatched_to 채워져 있으면 그 사람의 권한으로 진행 (RBAC).
- trace_id 생성 (`run-c` + 8자 hex).
- state.yaml 초기화.

### 1-2. `resume` 모드 — `/act --resume <trace_id>`
→ state.yaml status 분기:
- `pending_pcb_approval` → "PCB 승인 대기" 안내 + drop-out 경로 출력.
- `pcb_approved` → act-coordinator 재진입 → As-Is 파일 + MAT-001 갱신 + 차원 1 재트리거 명령 출력.
- `running` → 마지막 phase 부터 재개.
- `completed` → 이미 완료, As-Is 파일 + MAT-001 행 경로 출력.
- `rejected` → PCB 반려 마감, 큐 status: pending 복귀.

### 1-3. `approve` 모드 — `/act --approve <trace_id> [--approver <이름>]`
→ pcb-gatekeeper `gate_response` (decision: approved). 응답 후 자동 act-coordinator 위임.

### 1-4. `reject` 모드 — `/act --reject <trace_id> --reason "..." [--approver <이름>]`
→ PCB 반려. 큐 status 는 pending 복귀 (재시도 가능). state.yaml status: rejected.

### 1-5. `trigger-rebuild` 모드 — `/act --trigger-rebuild <trace_id> [--dry-run]`
→ act-coordinator 가 작성한 차원 1 재트리거 명령을 **본 커맨드가 실행 안 함**. 사용자에게 명령을 출력하고, 사용자가 수동으로 `/build-standard {표준코드} --from write --target {scope}` 또는 `/do {WI번호}` 를 실행. dry-run 시 명령만 출력하고 어떤 것도 실행 안 함.
> Phase 4.5 에서 자동 실행 옵션 검토.

### 1-6. `status` 모드 — `/act --status <trace_id>`
→ 현재 phase / RCA 결과 / revision plan 요약 / PCB 승인 상태 출력.

### 1-7. `list` 모드 — `/act --list [--status <상태>]`
→ `.claude/runs/run-c*` 디렉터리 전수 스캔 + state.yaml status 필터. 표 stdout.

### 1-8. 공통 옵션
| 플래그 | 효과 | 적용 모드 |
|---|---|---|
| `--dry-run` | RCA·revision plan 만 작성, As-Is 파일 미작성 + MAT-001 미갱신 + 큐 미수정 | start, resume, approve, trigger-rebuild |
| `--auto-approve` | PCB 게이트 자동 승인 (PoC·테스트 한정 — 실운영 금지) | start, resume |
| `--approver <이름>` | PCB 승인 응답자 신원 명시 | approve, reject |
| `--reason "..."` | PCB 반려 사유 (필수) | reject |
| `--rca-method <id>` | RCA 방법 (5why \| fishbone \| both, 기본 5why) | start |
| `--no-mat001-update` | MAT-001 §개정 이력 자동 갱신 보류 (테스트) | start, approve |

---

## 2. 실행 시퀀스 — 모드별

### 2-A. `start` 모드 (신규 차원 4 사이클)

#### Phase A. 사전 점검

A-1. 큐 yaml Read 성공 + status 검증 (pending 또는 in_progress).
A-2. **RBAC 검증** (Phase 4 차원 3 의 independence-guard 동형):
   - `independence-guard` `rbac_check` 모드 호출 (action: `act.start`, target: queue.target.scope_id).
   - act 의 RBAC 정책: process_owner / qmr / admin 만 허용 (auditor·executor 는 deny).
A-3. 큐의 source / target / rationale / recommendation 추출.
A-4. trace_id 생성 (`run-c` + 8자 hex). `.claude/runs/{trace_id}/state.yaml` 초기화.
A-5. 큐 status: pending → in_progress 전환 + dispatched_at 채움 (이미 dispatched 면 그대로).

#### Phase B. rca-analyzer 위임 (근본 원인 분석)

B-1. `rca-analyzer` 호출:
```yaml
[입력]
- queue_id, queue_data (전체 yaml)
- options: { rca_method: 5why|fishbone|both }
- trace_id

[출력]
- .claude/runs/{trace_id}/root_cause.yaml
  └ method, why_chain[] (5why 의 경우 5단계 trace), causes[] (Fishbone 의 6 카테고리), root_cause_summary, evidence_refs[]
- trace.jsonl rca_started ~ rca_done
```

#### Phase C. revision-planner 위임 (개정 범위 결정)

C-1. `revision-planner` 호출:
```yaml
[입력]
- queue_data, root_cause_path, trace_id

[출력]
- .claude/runs/{trace_id}/revision_plan.yaml
  └ revision_scope (POL/PRO/WI/TMP/EX 식별), rebuild_mode (--from design|write|restart),
    estimated_impact (low/medium/high), affected_assets[], recommended_actions[]
```

C-2. revision_plan 의 rebuild_mode 휴리스틱:
- 단일 WI 의 경미한 보완 → `--from write --target {WI}`
- WI 다수 + 신규 절차 가능성 → `--from design --target {PRO}`
- 정책 자체 변경 / 표준 개정판 편입 → `--restart` (전체 재실행)
- REC 보완만 → 차원 1 재실행 불필요, `/do {WI} --reissue` (Phase 2.5 지원 예정)

#### Phase D. pcb-gatekeeper 위임 (HITL)

D-1. `pcb-gatekeeper` 를 `gate_enter` 모드로 호출:
```yaml
[입력]
- trace_id, queue_id
- root_cause_summary, revision_plan_summary
- pcb_role: "PCB"            # Process Control Board
- options: { auto_approve }
```
D-2. `auto_approve == true` → 즉시 승인 처리 + state.status: pcb_approved → Phase E.
D-3. 그렇지 않으면 → state.status: pending_pcb_approval + drop-out (`pcb_request.md`) → 본 커맨드 종료 (PCB 응답 대기).

#### Phase E. act-coordinator 위임 (As-Is 파일 + MAT-001 갱신 + 큐 종결)

E-1. PCB 승인 후 (수동 `/act --approve` 또는 auto_approve):
   - state.status: pcb_approved → Phase E 진입.

E-2. `act-coordinator` 호출:
```yaml
[입력]
- trace_id, queue_id, root_cause_path, revision_plan_path
- pcb_decision: approved
- options: { dry_run, no_mat001_update }

[출력]
- vault/02_표준/{표준}/_inputs/04_AsIs/queue-q{hex}.md (신규 As-Is 입력 파일)
- vault/90_MAT_통합매핑/MAT-001_문서관리대장.md (Edit, §"개정 이력" 또는 신규 섹션 추가)
- .claude/queues/act/queue-q*.yaml (Edit, status: done + done_capa_rec: As-Is 파일 식별)
- state.yaml status: completed + final_asis_path + finalized_at
- trace.jsonl 마지막 라인 act_finalized
```

E-3. 종결 보고 + 차원 1 재트리거 명령 안내 (사용자 실행).

---

### 2-B. `resume` 모드

R-1. state.yaml Read · status 별 분기:

| status | 동작 |
|---|---|
| `running` | 마지막 phase (rca/planner/pcb_request) 부터 재개. |
| `pending_pcb_approval` | "PCB 승인 대기" 안내 + pcb_request.md 경로 출력. |
| `pcb_approved` | act-coordinator 재진입 → Phase E 마무리. |
| `completed` | 이미 완료, As-Is + MAT-001 + 큐 정보 출력. |
| `rejected` | "PCB 반려" 안내 + 사유 출력. |

---

### 2-C. `approve` / `reject` 모드

AR-1. state.yaml Read 후 status == pending_pcb_approval 검증.
AR-2. `pcb-gatekeeper` `gate_response` 호출 (decision: approved/rejected).
AR-3. **승인 시**: state.status: pcb_approved → 자동 act-coordinator 위임 → Phase E.
AR-4. **반려 시**: state.status: rejected + 큐 status: pending 복귀 + queue.dispatched_to 유지 (재시도 가능).
AR-5. trace.jsonl 에 `pcb_responded` 이벤트.

---

### 2-D. `trigger-rebuild` 모드

TR-1. state.yaml status == completed 확인 + revision_plan.yaml Read.
TR-2. revision_plan 의 `recommended_actions[]` 명령들을 stdout 출력 (실행은 사용자):
```
▶ 차원 1 재트리거 (사용자 실행 필요):

  /build-standard CMMI-DEV-ML3 --from write --target PRO-CMMI-04-01

  As-Is 입력 파일: vault/02_표준/CMMI-DEV-ML3/_inputs/04_AsIs/queue-qa1b2c3d4.md
  영향 자산: PRO-CMMI-04-01 v1.0 → v1.1 (예상)
  관련 큐: queue-qa1b2c3d4 (NCR-001 / F-001 종결 추적)

  실행 후: /audit --close-ncr REC-NCR-04-01-2026-001 --capa <개정판 PRO 의 후속 REC>
```
TR-3. `--dry-run` 시 명령만 미리보기. 본 모드는 실제 실행하지 않음 — 차원 1 빌드는 별도 사이클 (사용자 권한·자원 검증 단계).

---

### 2-E. `status` 모드

S-1. trace 의 state.yaml + RCA 요약 + revision plan 요약 + PCB 승인 상태 stdout.

---

### 2-F. `list` 모드

L-1. `Glob ".claude/runs/run-c*/state.yaml"` 전수 스캔.
L-2. `--status` 필터 적용 후 표 stdout (trace_id / queue_id / status / 마지막 갱신 / scope_id).

---

## 3. trace_id·state·로그 규약

### 3-1. 디렉터리 구조
```
.claude/runs/{trace_id}/
├── state.yaml           ← 차원 4 사이클 상태 (재개·PCB 대기)
├── trace.jsonl          ← 입력·LLM 분석·PCB 응답 전수 로그
├── root_cause.yaml      ← rca-analyzer 산출
├── revision_plan.yaml   ← revision-planner 산출
└── pcb_request.md       ← PCB 승인 drop-out (pending_pcb_approval 시)
```

### 3-2. `state.yaml` 스키마
```yaml
trace_id: run-cxxxxxxxx
kind: act                                # audit/kpi/act 구분
queue_id: queue-qa1b2c3d4
queue_path: .claude/queues/act/queue-qa1b2c3d4.yaml
queue_kind: ncr_capa                     # 큐의 kind 인용
priority: critical                       # 큐의 priority 인용
status: running | pending_pcb_approval | pcb_approved | completed | rejected | aborted
started_at: "ISO8601"
actor: "{사용자명}"                       # /act 호출자 (process_owner 등)
options:
  rca_method: 5why
  auto_approve: false
  dry_run: false
  no_mat001_update: false
phase:
  rca: done
  planner: done
  pcb: done                              # auto_approve 또는 사용자 응답 후
  coordinator: done
rca_summary: "..."                       # root_cause.yaml 의 root_cause_summary 인용
revision_summary:
  scope_kind: PRO
  scope_id: PRO-CMMI-04-01
  rebuild_mode: "--from write"
  estimated_impact: medium
  affected_assets: ["PRO-CMMI-04-01"]
pcb:
  required: true
  approver_role: "PCB"
  approver_name: null
  decision: null                         # approved | rejected
  requested_at: null
  responded_at: null
  rejection_reason: null
final_asis_path: null
final_mat001_row: null
finalized_at: null
related_audit_trace: "run-a1c2d3e4"      # 큐의 source.trace_id 인용
related_ncr: REC-NCR-04-01-2026-001       # 큐가 NCR 큐일 때
```

### 3-3. `trace.jsonl` 이벤트 종류
- `start` — 차원 4 사이클 시작
- `rbac_check_invoked` / `rbac_denied` — RBAC 검증
- `queue_loaded` — 큐 데이터 로드
- `rca_started` / `rca_method_applied` / `rca_done` — 근본 원인 분석
- `revision_planner_done` — 개정 범위 결정
- `pcb_requested` — PCB 승인 drop-out
- `pcb_responded` — PCB 응답 수신 (approved/rejected)
- `asis_written` — As-Is 입력 파일 작성
- `mat001_revision_history_updated` — MAT-001 §개정 이력 행 추가
- `queue_done` — 큐 status: done 전환
- `act_finalized` — 차원 4 사이클 완료
- `trigger_rebuild_announced` — /build-standard 명령 stdout 출력 (실행은 사용자)
- `aborted` — 중단

---

## 4. Phase 범위 명시 (현 단계)

본 커맨드는 다음 4 Phase 로 점진 구축된다. 현재는 **Phase 1**.

| Phase | 포함 | 제외 |
|---|---|---|
| 1 | start / resume / approve / reject / trigger-rebuild / status / list 7 모드 / 4 에이전트 (rca-analyzer + revision-planner + pcb-gatekeeper + act-coordinator) / 단일 큐 PoC / RBAC 검증 / As-Is 파일 자동 작성 / MAT-001 §개정 이력 자동 누적 / 차원 1 재트리거 명령 stdout (사용자 실행) | 다중 큐 일괄 처리 / 의존성 그래프 / /build-standard 자동 실행 / 사이클 측정 |
| **2 (지금)** | **`--batch <ids>` / `--batch-related <id>` 모드** / rca-analyzer 통합 root cause 분석 (`merged_root_cause`) / revision-planner Mermaid 의존성 다이어그램 자동 생성 / act-coordinator 통합 As-Is 파일 (`queue-batch-{id}.md` — `linked_queues[]`) / PCB 승인 1회 (다수 큐 일괄) / 의존성 충돌 자동 abort | 자동 재실행 / 사이클 KPI |
| 3 | 차원 1 자동 재실행 (`--auto-rebuild` 옵션, 사용자 명시 승인 후) / 재실행 결과 검증 (qa-reviewer 자동 호출) | 사이클 KPI |
| 4 | 사이클 측정 — NCR 발행 → 차원 4 종결 → KPI 회복까지의 평균 기간 / 재발률 / 회귀 알림 (MAT-008 차원 4 KPI 추가) | — |

---

## 5. 안전 가드

- 본 커맨드 실행 중 다음 외 어떤 파일도 **수정하지 않는다**:
  - `vault/02_표준/{표준}/_inputs/04_AsIs/queue-q*.md` (신규)
  - `vault/90_MAT_통합매핑/MAT-001_문서관리대장.md` (Edit, §개정 이력 만)
  - `.claude/queues/act/queue-q*.yaml` (Edit, status / done_* 만)
  - `.claude/runs/{trace_id}/*` (전체)
- POL/PRO/WI/TMP/EX/REC/MAT-002~008 모두 보호.
- 차원 1 재트리거 (`/build-standard`) 는 **본 커맨드가 직접 실행 안 함** — 명령만 stdout. 사용자가 별도 권한·자원 검증 후 실행.

---

## 6. 최종 보고 양식

### 6-1. start 종료 시 (auto_approve=false → pending_pcb_approval)
```
🔧 차원 4 사이클 시작 — queue-qa1b2c3d4 (NCR-001 critical)
📁 RCA: .claude/runs/run-c{hex}/root_cause.yaml
📁 Revision plan: .claude/runs/run-c{hex}/revision_plan.yaml (PRO-CMMI-04-01, --from write, impact: medium)
📋 PCB 승인 요청서: .claude/runs/run-c{hex}/pcb_request.md
👤 actor: dongseok (role: process_owner)
⏸ PCB 승인 대기

▶ 다음 (PCB 응답):
  /act --approve run-c{hex} [--approver "PCB위원장"]
  /act --reject  run-c{hex} --reason "..."
```

### 6-2. approve 종료 시 (completed)
```
✅ 차원 4 사이클 완료 — queue-qa1b2c3d4
📁 As-Is 입력: vault/02_표준/CMMI-DEV-ML3/_inputs/04_AsIs/queue-qa1b2c3d4.md
📋 MAT-001 §"개정 이력" 1행 append (PRO-CMMI-04-01 v1.0 → v1.1 예정)
🔄 큐 status: in_progress → done (capa: 본 As-Is 파일)
🔍 trace_id: run-c{hex} (status=completed)
👤 PCB 승인: PCB위원장 (2026-05-02 14:30 KST)

▶ 차원 1 재트리거 (사용자 실행 필요):
  /act --trigger-rebuild run-c{hex}
  또는 직접:
  /build-standard CMMI-DEV-ML3 --from write --target PRO-CMMI-04-01

▶ 차원 1 재실행 후:
  /audit --close-ncr REC-NCR-04-01-2026-001 --capa <후속 REC>
```

### 6-3. list 출력 예시
```
🔧 차원 4 사이클 목록 (status: pending_pcb_approval / running / completed / ...)
| trace_id | queue_id | scope | status | 마지막 갱신 |
|---|---|---|---|---|
| run-c4f8a1b2 | queue-qa1b2c3d4 | PRO-CMMI-04-01 | completed | 2026-05-02 14:30 |
| run-cb9d3e4 | queue-qf1e2d3c4 | WI-CMMI-04-01-04 | pending_pcb_approval | 2026-05-02 15:00 |
```
