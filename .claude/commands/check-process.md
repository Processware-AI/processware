---
description: 표준 프로세스 심사 (차원 3 Check) — REC ↔ PRO/WI 요건 자동 대조 + 부적합 탐지 + 심사 보고서 발행. ISO §9.2 독립성 강제. 사용 ./check-process start <PRO|WI|범위> --auditor "이름" | --confirm <trace> | --status <trace>
argument-hint: "start <PRO|WI|범위> --auditor \"이름\" | --resume <trace_id> | --confirm <trace_id> [--auditor \"이름\"] | --reject-finding <ncr_id> --reason \"...\" | --status <trace_id> | --list-ncr [--status open|closed] | --close-ncr <ncr_id> --capa <REC> [+ --dry-run | --override-independence (PoC만) | --period <from..to> | --strictness strict|normal|lenient]"
---

# 표준 프로세스 심사 하네스 (차원 3 Check)

대상 입력: **$ARGUMENTS**

본 커맨드는 차원 2 (`/do-process`) 가 누적한 **REC + trace.jsonl + MAT-005** 를 입력으로, AI 심사원이 **PRO/WI 요건 ↔ REC 충족 여부**를 자동 대조하여 **심사 보고서·부적합·KPI** 를 산출한다.

상위 설계: `docs/표준프로세스_AI관리체계_4차원PDCA.md` §3 "차원 3 — CHECK" / §5.2 "AI 독립성 보장" / `docs/AI-Driven CMMI Operating Platform.md` Layer 2 회귀 방지

---

## 0. 실행 원칙

- **자산은 읽기 전용**: POL/PRO/WI/TMP/EX/REC/MAT-001~005,007 은 본 커맨드가 절대 수정하지 않는다.
- **신규 산출물만 생성**: 심사 보고서·부적합 → `vault/08_REC_기록/AUDIT/REC-AUDIT-*.md` 와 `vault/08_REC_기록/AUDIT/REC-NCR-*.md` (Phase 2). NCR 관리대장은 `vault/90_MAT_통합매핑/MAT-009_NCR_관리대장.md` (Phase 2).
- **MAT-005 §심사 이력 만 갱신**: 차원 2 가 §실행 기록 을 누적하듯, 차원 3 은 §심사 이력 섹션에 1행 append.
- **독립성 강제 (ISO 9.2)**: `/check-process start` 진입 시 `--auditor` 이름과 대상 trace 들의 `executed_by` 가 1건이라도 일치하면 즉시 abort. PoC 한정 `--override-independence` 만 허용 (Phase 1 만, Phase 4 에서 제거).
- **대화는 차원 2 보다 적다**: 차원 3 은 "사후 검토" 라 사람과의 대화는 매트릭스 확정 1회 (HITL gate) + 부적합 등급 조정 (Phase 2) 정도. 차원 2 의 step-by-step 대화 모델과 다르다.
- **모든 입력·LLM 출력 전수 로그**: `.claude/runs/{trace_id}/trace.jsonl` (심사 증적의 증적).
- **환각 방지**: 충족 판정은 REC 본문에 명시된 값·증적 매트릭스의 trace_id 만 근거로 한다. REC 에 없는 값은 임의로 채우지 않는다.

---

## 1. 인자 파싱 — 진입 모드 (배타적, 1개만 적용)

본 커맨드는 다음 7개 진입 모드 중 하나로 동작한다. 첫 인자에 따라 분기.

### 1-1. `start` 모드 — 신규 심사
```
/check-process start PRO-CMMI-04-01 --auditor "이감사"            # 단일 PRO 범위
/check-process start WI-CMMI-04-01-03 --auditor "이감사"           # 단일 WI 범위 (좁은 심사)
/check-process start CMMI-DEV-ML3 --auditor "이감사"               # 표준 전체 범위 (넓은 심사)
/check-process start PRO-CMMI-04-01 --auditor "이감사" --period 2026-01-01..2026-04-30
```
→ 인자 파싱:
- 첫 인자가 `PRO-` / `WI-` / 표준 코드 패턴이면 직접 매칭.
- `--auditor` 누락 시 에러 (독립성 강제 위해 필수).
- `--period` 누락 시 기본값: 지난 분기 (오늘 기준 90일).
- trace_id 생성 (예: `run-a` + 8자 hex), `.claude/runs/{trace_id}/state.yaml` 초기화.

### 1-2. `resume` 모드 — `/check-process --resume <trace_id>`
```
/check-process --resume run-a1c2d3e4
```
→ `state.yaml` Read · `status` 분기:
  - `pending_confirmation` → "심사원 확정 대기" 안내 + `confirmation_request.md` 경로 출력 + 종료 (사용자가 응답할 차례).
  - `running` (전 세션 중단) → 마지막 단계부터 재개.
  - `completed` → "이미 발행된 심사 보고서" 안내 + `final_audit_path` 출력 + 종료.

### 1-3. `confirm` 모드 — `/check-process --confirm <trace_id> [--auditor <이름>] [--adjust-finding <id>=<grade>]`
```
/check-process --confirm run-a1c2d3e4
/check-process --confirm run-a1c2d3e4 --auditor "이감사"
/check-process --confirm run-a1c2d3e4 --adjust-finding F-002=minor
```
→ `pending_confirmation` 인 trace 의 매트릭스를 확정. 등급 조정이 있으면 적용. `audit-reporter` 위임 → REC-AUDIT 발행.

### 1-4. `reject-finding` 모드 — `/check-process --reject-finding <finding_id> --reason "..." [--trace <trace_id>]`
```
/check-process --reject-finding F-002 --reason "AI 오탐 — REC §3 에 시정 권고 이미 기재" --trace run-a1c2d3e4
```
→ AI 가 부적합으로 판정한 항목을 심사원이 인정하지 않음 (오탐 제거). 매트릭스에서 해당 row 의 `human_override: rejected` 로 마크. `--reason` 필수.

### 1-5. `status` 모드 — `/check-process --status <trace_id>`
```
/check-process --status run-a1c2d3e4
```
→ trace 의 진행 단계·발견 부적합 수·소요 시간 출력.

### 1-6. `list-ncr` 모드 — `/check-process --list-ncr [--status open|closed|all] [--standard <코드>] [--severity critical|major|minor] [--overdue]`
```
/check-process --list-ncr                                      # open 인 NCR 모두 (기본)
/check-process --list-ncr --status all                         # open + closed 모두
/check-process --list-ncr --status closed --standard CMMI-DEV-ML3
/check-process --list-ncr --severity critical --overdue        # SLA 기한 경과한 critical NCR
```
→ `vault/90_MAT_통합매핑/MAT-009_NCR_관리대장.md` 의 두 섹션을 Read · 필터 적용 후 표 출력.
- 각 행에 NCR_ID, 등급, 제목, R/A, SLA 기한, 잔여일 (open 만), 상태, 모(母) 심사 wikilink 포함.
- `--overdue` : open 인 NCR 중 `today > sla_due_date` 인 것.
- 출력은 stdout (파일 미생성, 미수정).

### 1-7-K. `kpi` 모드 (Phase 3) — `/check-process --kpi <subcommand> [...]`

KPI 측정·시계열 누적·회귀 탐지를 담당하는 단일 진입점. 4 subcommand.

```
/check-process --kpi start CMMI-DEV-ML3 --period 2026-01-01..2026-04-30
/check-process --kpi start PRO-CMMI-04-01 --period 2026-01-01..2026-04-30 --baseline auto
/check-process --kpi show CMMI-DEV-ML3                                   # MAT-008 표준 섹션 stdout 출력
/check-process --kpi show CMMI-DEV-ML3 --round 2                         # 특정 회차만
/check-process --kpi update CMMI-DEV-ML3                                 # 별칭 — start 와 동일 (period 미지정 시 자동 분기)
/check-process --kpi check-regressions                                   # 모든 표준의 critical+watch 알림 출력 + --overdue 가능
```

**4 subcommand 동작**:

- **`start` / `update`** (신규 측정 회차):
  1. 인자에서 표준 코드 / PRO doc_id / period 추출.
  2. `period` 미지정 시 default = 직전 분기 (오늘 기준 90일 — Q1=1/1~3/31 식).
  3. trace_id 생성 (`run-k` + 8자 hex — audit trace 와 prefix 분리).
  4. `kpi-collector` 위임 (입력: scope, period, include_meta_kpis=true) → kpi_data.yaml.
  5. `kpi-analyzer` 위임 (입력: kpi_data_path, options.baseline) → MAT-008 갱신 + MAT-009 §통계 갱신.
  6. 결과 표 stdout (verdict 분포 + alerts 수).

- **`show`** (조회만, 미수정):
  1. `vault/90_MAT_통합매핑/MAT-008_KPI_대시보드.md` Read.
  2. 해당 표준 섹션의 §회차 시계열 + §회귀 알림 + §결과 요약 출력.
  3. `--round N` 지정 시 그 회차만 (전체는 default).

- **`check-regressions`** (전사 알림 모음):
  1. MAT-008 의 모든 표준 섹션 스캔.
  2. 각 표준의 마지막 회차 §회귀 알림 표를 모음.
  3. `--overdue` : 회귀 알림 중 NCR 이 SLA 경과한 항목만 표기 (MAT-009 cross-ref).
  4. 출력은 stdout (파일 미수정).

### 1-7-AQ. `act-queue` 모드 (Phase 4) — `/check-process --act-queue <subcommand> [...]`

차원 4 인계 큐를 조회·관리하는 단일 진입점. 4 subcommand.

```
/check-process --act-queue list                                          # 모든 큐 (status: pending 이 default)
/check-process --act-queue list --status all                             # 전체
/check-process --act-queue list --priority critical --kind ncr_capa
/check-process --act-queue show queue-q3a8f2c1                           # 단일 큐 상세
/check-process --act-queue dispatch queue-q3a8f2c1 --to "박팀장"          # process_owner 등에게 dispatch
/check-process --act-queue done queue-q3a8f2c1 --capa REC-CMMI-...       # 차원 4 완료 후 종결
```

**4 subcommand 동작**:
- `list`: `Glob ".claude/queues/act-process/queue-q*.yaml"` 전수 스캔 + 필터 적용 후 표 stdout.
- `show <queue_id>`: 해당 큐 yaml 본문 stdout.
- `dispatch <queue_id> --to <이름>`: 큐 status: pending → in_progress, dispatched_to / dispatched_at 채움. RBAC 검증: dispatch 는 process_owner 또는 qmr 권한 필요.
- `done <queue_id> --capa <REC>`: 큐 status: in_progress → done, done_at / done_capa_rec 채움. 본 큐가 NCR 연계면 NCR 도 자동 close 권장 (별도 `/check-process --close-ncr` 호출 안내).

### 1-7-RC. `rbac-check` 모드 (Phase 4) — `/check-process --rbac-check --action <id> [--target <id>]`

```
/check-process --rbac-check --action audit.start --target PRO-CMMI-04-01
/check-process --rbac-check --action audit.close-ncr --target REC-NCR-04-01-2026-001
```
→ `independence-guard` 를 `rbac_check` 모드로 호출. 현재 사용자의 권한이 해당 action 을 허용하는지 검증 후 결과 stdout.
사용 시점: 운영 자동화 스크립트가 작업 전에 권한 사전 검증할 때, 또는 사용자가 자기 권한 확인할 때.

### 1-7. `close-ncr` 모드 — `/check-process --close-ncr <ncr_id> --capa <REC> [--closed-by <이름>] [--reason "..."]`
```
/check-process --close-ncr REC-NCR-04-01-2026-001 --capa REC-CMMI-04-01-04-01-2026-003
/check-process --close-ncr REC-NCR-04-01-2026-001 --capa REC-CMMI-04-01-04-01-2026-003 --closed-by "박팀장" --reason "SLA 정의 + 재실행 정상 승인"
```
→ `ncr-drafter` 를 `close` 모드로 호출:
- NCR frontmatter `status: closed` + `capa_rec` / `closed_at` / `closed_by` / `closed_reason` 채움.
- NCR 본문 §7 종결 기록 표 채움.
- MAT-009: §"NCR 발행 현황 (open)" 행 제거 → §"NCR 종결 현황 (closed)" 행 추가 (행 이동).
- `--closed-by` 미지정 시 시스템 사용자명.
- `--reason` 미지정 시 capa_rec 의 frontmatter `title` 을 기본 사유로.
- CAPA REC 가 vault 에 미존재 시 abort + 후보 안내.

### 1-8. 공통 옵션
| 플래그 | 효과 | 적용 모드 |
|---|---|---|
| `--dry-run` | 분석은 진행하되 REC-AUDIT 파일·MAT-005 갱신 생략, 미리보기만 출력 | start, resume, confirm |
| `--auditor <이름>` | 심사원 명시 (필수). 독립성 검증의 기준값 | start, confirm, reject-finding |
| `--override-independence` | 독립성 위반 무시 (PoC·테스트 한정 — 실운영 금지). state.yaml 에 위반 사실 기록됨 | start (PoC만) |
| `--period <from..to>` | 심사 대상 기간 한정 (REC 의 `executed_at` 기준) | start |
| `--strictness <strict\|normal\|lenient>` | 부적합 판정 임계값. 기본 `normal` | start |
| `--reason "..."` | 인정 거부 사유 / NCR 종결 사유 | reject-finding (필수), close-ncr |
| `--no-ncr` | confirm 시 NCR 자동 발행 보류 (Phase 2 default 는 자동 발행). 보고서만 발행하고 finding 은 보고서 §4 에만 남음 | confirm |
| `--capa <REC>` | 시정조치 후속 REC doc_id (close-ncr 필수) | close-ncr |
| `--closed-by <이름>` | 종결 응답자 (close-ncr) | close-ncr |
| `--standard <코드>` | NCR 목록 필터 (예: CMMI-DEV-ML3) | list-ncr |
| `--severity <등급>` | NCR 목록 필터 (critical/major/minor) | list-ncr |
| `--overdue` | SLA 기한 경과한 NCR 만 | list-ncr, kpi check-regressions |
| `--baseline auto\|<round>` | KPI baseline 결정 (auto: 직전 회차) | kpi start/update |
| `--regression-threshold-pp <N>` | 회귀 임계 %포인트 (default 5.0) | kpi start/update |
| `--round <N>` | 특정 회차만 조회 | kpi show |
| `--no-act-queue` | confirm/kpi finalize 시 차원 4 큐 자동 발행 보류 (Phase 4) | confirm, kpi start/update |
| `--to <이름>` | act queue dispatch 대상 (process_owner 등) | act-queue dispatch |
| `--kind <id>` | act queue 필터 (ncr_capa\|kpi_critical\|recommendation) | act-queue list |
| `--priority <등급>` | act queue 필터 | act-queue list |
| `--action <id>` | RBAC 검증할 action 식별자 (필수) | rbac-check |

---

## 2. 실행 시퀀스 — 모드별

### 2-A. `start` 모드 (신규 심사)

#### Phase A. 사전 점검 + 독립성 가드 (조기 실패)

A-1. 인자에서 대상 범위 추출:
   - `PRO-*` → 해당 PRO + 그 PRO 의 모든 WI 자식.
   - `WI-*` → 단일 WI.
   - 표준 코드 (`CMMI-DEV-ML3` 등) → MAT-005 의 해당 표준 모든 PRO/WI.
A-2. 대상 PRO/WI 가 vault 에 존재하는지 확인. 미존재 시 abort.
A-3. **독립성 가드 (ISO §9.2) — Phase 4 부터 `independence-guard` 정식 위임**:
   - 본 커맨드는 `independence-guard` 를 `independence_check` 모드로 호출:
     ```
     [입력]
     - mode: independence_check
     - auditor: --auditor 인자
     - scope: { pro, wi, period }
     - options: { override: --override-independence }
     ```
   - 반환 verdict 별 분기:
     - `passed` → 정상 진행.
     - `failed` → 즉시 abort + 위반 trace 출력 (independence-guard 의 §C-2 메시지 그대로).
     - `overridden` → 경고 + state.yaml.independence 에 violations[] 기록 후 진행.
   - **추가 RBAC 검증** (Phase 4): independence-guard 를 `rbac_check` 모드로 다시 호출 (action: `audit.start`, target: scope.ids[0]). denied 시 abort.
   - state.yaml 에 `independence: { checked: true, violations: [...], overridden: false, rbac_verdict: allowed }` 기록.
   - trace.jsonl 에 `independence_guard_invoked` + `rbac_check_invoked` 이벤트.
A-4. trace_id 생성 (`run-a` + 8자 hex 권장 — 차원 2 와 충돌 방지). `.claude/runs/{trace_id}/` 디렉터리 생성 + `state.yaml` 초기화.

#### Phase B. audit-planner 위임 (요건 → 체크리스트)

B-1. 서브에이전트 `audit-planner` 호출:
```
[입력]
- scope: { kind: PRO|WI|standard, ids: [...], period: from..to }
- trace_id, auditor
- options: { strictness }

[출력]
- .claude/runs/{trace_id}/audit_plan.yaml
  └ requirement[] : { req_id, source(PRO/WI), source_section, statement, severity_default, expected_evidence_type }
- trace.jsonl 1라인/이벤트
```

B-2. plan 의 `requirement[]` 가 0건이면 abort (대상 PRO/WI 가 요건을 명시하지 않음).

#### Phase C. evidence-collector 위임 (REC 수집·인덱싱)

C-1. 서브에이전트 `evidence-collector` 호출:
```
[입력]
- scope (Phase B 와 동일)
- trace_id

[출력]
- .claude/runs/{trace_id}/evidence.yaml
  └ rec[] : { rec_id, rec_path, parent_wi, parent_pro, executed_by, executed_at, status, fields_summary }
  └ trace_refs[] : { trace_id, executed_by, hitl, started_at, completed_at }
  └ coverage_hint : { wi_with_rec: [...], wi_without_rec: [...] }
```

C-2. `rec[]` 가 0건이면 경고 + 사용자 결정 대기 ("이행 증적이 없는 심사를 진행하시겠습니까? Y/N"). N 이면 abort.

#### Phase D. compliance-checker 위임 (요건 ↔ 증적 대조)

D-1. 서브에이전트 `compliance-checker` 호출:
```
[입력]
- audit_plan_path, evidence_path
- trace_id
- options: { strictness }

[출력]
- .claude/runs/{trace_id}/conformity_matrix.yaml
  └ row[] : { req_id, evidence_refs[], judgement: conformant|partial|nonconformant|not_assessed,
              rationale, finding_id?: F-NNN, severity?: critical|major|minor }
- trace.jsonl 라인 (judgement_made 이벤트)
- state.yaml status: pending_confirmation
```

D-2. 매트릭스 작성 완료 → state.status: `pending_confirmation` + `confirmation_request.md` drop-out (심사원에게 매트릭스 미리보기 + `/check-process --confirm` 안내).

D-3. **본 커맨드는 종료** (사용자가 응답할 차례).

### 2-B. `resume` 모드

R-1. `state.yaml` Read.
R-2. `status` 별 분기:

| status | 동작 |
|---|---|
| `pending_confirmation` | "확정 대기" 안내 + `confirmation_request.md` 경로 출력 + 종료. |
| `running` (B/C/D 중 비정상 종료) | 마지막 완료 단계부터 재개. |
| `completed` | "이미 발행" 안내 + `final_audit_path` 출력 + 종료. |
| `aborted` | "중단됨" 안내 + 사유 출력 + 종료. |
| 미존재 trace_id | 에러 |

### 2-C. `confirm` 모드

CF-1. `state.yaml` Read 후 `status == "pending_confirmation"` 확인. 아니면 에러.
CF-2. `--auditor` 가 state.yaml `auditor` 와 다르면 경고 (다른 심사원이 확정하는 것은 가능 — 분담 심사 — 하되 trace 에 명시).
CF-3. `--adjust-finding` 옵션이 있으면 `conformity_matrix.yaml` 의 해당 row 의 `severity` 갱신 + `human_override` 메모.
CF-4. **audit-reporter 위임**:
```
[입력]
- trace_id
- audit_plan_path, evidence_path, conformity_matrix_path
- auditor (확정자)
- options: { dry_run, no_ncr, no_act_queue }     # no_ncr / no_act_queue: 발행 보류

[출력]
- vault/08_REC_기록/AUDIT/REC-AUDIT-{PRO|STD}-{회차}-{YYYY}-{NNN}_심사보고서.md
- MAT-005 §"심사 이력" 섹션 1행 append
- (no_ncr=false 일 때) ncr-drafter 자동 위임 → REC-NCR-*.md N건 + MAT-009 N행
- (no_ncr=false 일 때) 보고서 frontmatter ncr_refs[] + §4 finding 블록의 NCR 링크 채움
- (no_act_queue=false 일 때, Phase 4) act-trigger 자동 위임 → .claude/queues/act-process/queue-q*.yaml N건 + MAT-008 §"차원 4 인계" 갱신
- state.yaml status: completed + final_audit_path + ncr_count + act_queue_count
- trace.jsonl 마지막 라인 audit_finalized
```

CF-5. 종결 보고.

### 2-CN. `close-ncr` 모드 (Phase 2)

CN-1. `--ncr_id` 의 NCR 파일 Read · `status in [open, in_progress]` 확인. closed 면 에러.
CN-2. `--capa <REC>` 의 파일이 vault 에 존재하는지 Glob 검증. 미존재 시 abort + 후보 안내.
CN-3. `ncr-drafter` `close` 모드 호출:
```
[입력]
- mode: close
- ncr_id, capa_rec_id, closed_by, closed_reason
- options: { dry_run }
```
CN-4. ncr-drafter 가:
   - NCR frontmatter status: closed + capa_rec / closed_at / closed_by / closed_reason 채움.
   - NCR 본문 §7 종결 기록 표 채움.
   - MAT-009 §"NCR 발행 현황 (open)" 행 제거 → §"NCR 종결 현황 (closed)" 행 append (이동).
CN-5. 종결 보고 (SLA 준수 여부 포함).

### 2-LN. `list-ncr` 모드 (Phase 2)

LN-1. MAT-009 두 섹션 (open / closed) Read · 표 행 파싱.
LN-2. 필터 적용:
   - `--status open|closed|all` (기본 open)
   - `--standard <코드>`, `--severity <등급>`
   - `--overdue` : open 인 행 중 today > sla_due_date.
LN-3. 결과 표를 stdout 출력 (파일 미생성, 미수정).
LN-4. 0건이면 "조건 충족 NCR 없음" 안내.

### 2-K. `kpi` 모드 (Phase 3)

#### 2-K-A. `start` / `update`

KA-1. 인자 파싱: scope (표준코드 또는 PRO/WI doc_id), `--period from..to`, `--baseline auto|<N>`, `--regression-threshold-pp`.
KA-1.5. **RBAC 검증 (Phase 4)**: `independence-guard` `rbac_check` 모드 호출 (action: `audit.kpi.start`). denied 시 abort.
   - KPI 측정은 독립성 검증 불필요 (사후 통계 — 측정자가 이행자와 동일해도 무관).
KA-2. trace_id 생성 (`run-k` + 8자 hex).
KA-3. `.claude/runs/{trace_id}/state.yaml` 초기화 (kind: kpi, scope, options).
KA-4. **kpi-collector 위임**:
```
[입력]
- trace_id, scope (resolved_targets 포함), period, include_meta_kpis=true

[출력]
- .claude/runs/{trace_id}/kpi_data.yaml
- trace.jsonl (kpi_collector_start ... kpi_collector_done)
```
KA-5. **kpi-analyzer 위임**:
```
[입력]
- trace_id, kpi_data_path
- options: { dry_run, baseline, regression_threshold_pp, no_act_queue }

[출력]
- vault/90_MAT_통합매핑/MAT-008_KPI_대시보드.md (신규 또는 Edit append)
- vault/90_MAT_통합매핑/MAT-009_NCR_관리대장.md (Edit, §"NCR 통계" 만)
- state.yaml status: completed
- trace.jsonl 마지막 라인 kpi_analyzer_done
```
KA-6. **act-trigger 자동 위임 (Phase 4, options.no_act_queue == false 일 때)**:
   - kpi-analyzer 의 verdict==critical KPI 들을 `from_kpi` 모드로 act-trigger 에 인계.
   - .claude/queues/act-process/queue-q*.yaml N건 발행 + MAT-008 §"차원 4 인계" 표 갱신.
KA-7. 종결 보고.

#### 2-K-S. `show`

KS-1. MAT-008 Read · 인자에서 표준 코드 매칭 → 그 §섹션 추출.
KS-2. `--round N` 지정 시 그 회차 행만 필터.
KS-3. 표 stdout 출력 (파일 미수정).

#### 2-K-R. `check-regressions`

KR-1. MAT-008 의 모든 `## {표준코드}` 섹션 스캔.
KR-2. 각 표준의 마지막 회차의 §회귀 알림 표 행 수집.
KR-3. `--overdue` 시 MAT-009 의 open NCR 중 today > sla_due_date 인 항목 cross-ref → 회귀 알림 행에 ⏰ 표기.
KR-4. 통합 표 stdout (표준 / KPI ID / verdict / 측정값/목표 / 권고).

### 2-D. `reject-finding` 모드

RF-1. trace 의 `conformity_matrix.yaml` Read.
RF-2. 해당 finding row 찾고 `human_override.decision: rejected`, `human_override.reason: "..."`, `human_override.by: <auditor>`, `human_override.at: now` 기록.
RF-3. trace.jsonl 에 `finding_overridden` 이벤트.
RF-4. **상태 변경 안 함**. confirm 시점에 final 매트릭스에 반영됨.

### 2-E. `status` 모드

S-1. trace 의 state.yaml + 매트릭스 요약 출력.

---

## 3. trace_id·state·로그 규약

### 3-1. 디렉터리 구조
```
.claude/runs/{trace_id}/
├── state.yaml              ← 심사 상태 (재개·확정 대기)
├── trace.jsonl             ← 입력·LLM 판정·확정 전수 로그
├── audit_plan.yaml         ← audit-planner 산출
├── evidence.yaml           ← evidence-collector 산출
├── conformity_matrix.yaml  ← compliance-checker 산출
└── confirmation_request.md ← 심사원 확정 drop-out (pending_confirmation 시)
```

### 3-2. `state.yaml` 스키마
```yaml
trace_id: run-a1c2d3e4
kind: audit                  # 차원 2 의 do trace 와 구분
scope:
  kind: PRO                  # PRO | WI | standard
  ids: ["PRO-CMMI-04-01"]
  period:
    from: "2026-01-01"
    to:   "2026-04-30"
  resolved_targets:          # planner 가 펼친 결과
    pro: ["PRO-CMMI-04-01"]
    wi:  ["WI-CMMI-04-01-01", "WI-CMMI-04-01-02", ...]
status: running | pending_confirmation | completed | aborted
started_at: "ISO8601"
auditor: "이감사"
options:
  dry_run: false
  strictness: normal
  override_independence: false
independence:
  checked: true
  violations: []             # [{ trace_id, executed_by, wi }] — overridden 시에만 채워짐
  overridden: false
phase:
  planner: done
  evidence: done
  checker: done
  reporter: not_started
counts:
  requirements: 12
  evidence_recs: 3
  conformant: 8
  partial: 2
  nonconformant: 2
  not_assessed: 0
final_audit_path: null
finalized_at: null
```

### 3-3. `trace.jsonl` 이벤트 종류
- `start` — 심사 시작
- `independence_checked` — 독립성 검증 결과
- `planner_done` — audit-planner 완료
- `evidence_done` — evidence-collector 완료
- `judgement_made` — 단일 요건 판정 (req_id + judgement + rationale 요약)
- `checker_done` — compliance-checker 전체 완료
- `confirmation_requested` — 심사원 확정 drop-out
- `finding_overridden` — 부적합 인정 거부 (reject-finding)
- `confirmed` — 심사원 확정 응답
- `audit_drafted` — 보고서 초안
- `ncr_issued` — NCR 발행 (Phase 2; finding 별 1건)
- `ncrs_drafted` — 본 audit 의 NCR 일괄 발행 종합 (Phase 2)
- `audit_finalized` — 보고서 저장 완료
- `mat005_audit_history_updated` — MAT-005 §심사 이력 행 추가
- `mat009_ncr_issued` — MAT-009 NCR 발행 행 추가 (Phase 2)
- `kpi_collector_start` / `kpi_extracted` / `kpi_measured` / `meta_kpi_measured` / `kpi_collector_done` — KPI 수집 (Phase 3)
- `kpi_analyzer_start` / `baseline_resolved` / `kpi_analyzed` / `alerts_raised` / `mat008_updated` / `mat009_stats_updated` / `kpi_analyzer_done` — KPI 분석 (Phase 3)
- `independence_guard_invoked` / `rbac_check_invoked` / `rbac_denied` — 가드 호출 (Phase 4)
- `act_trigger_invoked` / `act_queue_created` / `mat008_act_queue_updated` / `act_trigger_done` — 차원 4 인계 (Phase 4)
- `act_queue_dispatched` / `act_queue_done` — 큐 진행 (Phase 4)
- `aborted` — 중단 사유 (독립성 위반 / 요건 0건 / 사용자 중단 / RBAC denied)

---

## 4. Phase 범위 명시 (현 단계)

본 커맨드는 다음 4 Phase 로 점진 구축된다. 현재는 **Phase 4**.

| Phase | 포함 | 제외 |
|---|---|---|
| 1 | start / resume / confirm / reject-finding / status / 4 에이전트 (planner+collector+checker+reporter) / 단일 PRO PoC / 독립성 inline 가드 / `vault/08_REC_기록/AUDIT/` 산출 / MAT-005 §심사이력 자동 누적 | NCR 자동 발행 / KPI 대시보드 / RBAC 정식 / 다국어 / 외부 시스템 |
| 2 | **ncr-drafter** / NCR 일련번호 (`REC-NCR-{POL2}-{PRO2}-{YYYY}-{NNN}`) / **MAT-009** NCR 관리대장 / `--list-ncr`·`--close-ncr` / 시정조치 종결 워크플로우 / SLA 휴리스틱 (critical 20영업일 / major 60일 / minor 90일) / R/A 휴리스틱 (카테고리 → 책임자) / `--no-ncr` 옵션 / confirm 시 NCR 자동 발행 | KPI / 외부 시스템 / RBAC 정식 / 책임자 R/A 정식 매핑 |
| 3 | **kpi-collector** / **kpi-analyzer** / **MAT-008** KPI 대시보드 / `/check-process --kpi start\|show\|update\|check-regressions` / PRO/WI §KPI 표 자동 추출 / 메타 KPI 5종 (Coverage / Findings density / Independence / NCR 종결율 / NCR SLA) / 4-tier verdict (healthy/watch/recovering/critical/data_gap) / baseline seed + 회귀 임계 (default ±5%p) / MAT-009 §통계 자동 갱신 hook | RBAC 정식 / 외부 시스템 / 차원 4 자동 트리거 / 시계열 시각화 |
| **4 (지금)** | **independence-guard** 정식 분리 (independence_check + rbac_check 2 모드) / **RBAC** policy.yaml 6 역할 / **act-trigger** 에이전트 / 차원 4 인계 큐 (.claude/queues/act-process/queue-q*.yaml) / `--act-queue list\|show\|dispatch\|done` / `--rbac-check` / `--no-act-queue` 옵션 / MAT-008 §"차원 4 인계" 자동 누적 / Mermaid 시계열 시각화 (PoC) / 영업일 계산기 명세 (가이드 부록 B, 휴리스틱 28일 유지) | 외부 인증기관 보고서 (XLSX/PDF) → Phase 4.5 / 외부 IdP 연동 → Phase 4.5 / 큐 dispatch 외부 시스템 알림 → Phase 4.5 |

---

## 5. 안전 가드

- 본 커맨드 실행 중 `vault/03_POL ~ 07_EX, 08_REC_기록 (AUDIT/ 제외), 90_MAT_통합매핑/MAT-001~005,007` 어떤 파일도 **수정하지 않는다**. 검증 위반 즉시 중단.
- 쓰기 허용:
  - `vault/08_REC_기록/AUDIT/REC-AUDIT-*.md` (신규)
  - `vault/08_REC_기록/AUDIT/REC-NCR-*.md` (Phase 2 — issue 신규 / close Edit)
  - `vault/90_MAT_통합매핑/MAT-005_*.md` (Edit append, §심사 이력 섹션만)
  - `vault/90_MAT_통합매핑/MAT-009_*.md` (Phase 2 — Edit append / 행 이동, 두 섹션 운영 / Phase 3 — §"NCR 통계" Edit)
  - `vault/90_MAT_통합매핑/MAT-008_*.md` (Phase 3 — 신규 또는 Edit append, 표준별 §섹션 / §회차 시계열 / §회귀 알림 / Phase 4 — §"차원 4 인계" 추가)
  - `.claude/queues/act-process/queue-q*.yaml` (Phase 4 — 신규 / dispatch / done 시 Edit)
  - `.claude/runs/{trace_id}/*` (전체) — audit trace `run-a*` / kpi trace `run-k*` 분리
- **읽기만**: `.claude/rbac/policy.yaml` — 본 커맨드는 절대 수정 안 함 (admin 권한 사용자가 직접 편집).
- 동일 (scope, 회차, 연도) 조합의 REC-AUDIT 일련번호 충돌 절대 금지 — Glob 재검증 후 Write.

---

## 6. 최종 보고 양식

### 6-1. start 종료 시 (pending_confirmation)
```
🔍 심사 매트릭스 작성 완료 — 심사원 확정 대기
📁 매트릭스: .claude/runs/run-a1c2d3e4/conformity_matrix.yaml
📋 확정 요청서: .claude/runs/run-a1c2d3e4/confirmation_request.md
👤 심사원: 이감사
📊 요건 12 / 충족 4 · 부분 2 · 부적합 2 · 미평가 4

▶ 다음: /check-process --confirm run-a1c2d3e4
   또는 부적합 인정 거부: /check-process --reject-finding F-002 --reason "..." --trace run-a1c2d3e4
```

### 6-2. confirm 종료 시 (completed)
```
✅ 심사 보고서 발행 — REC-AUDIT-04-01-01-2026-001
📁 vault/08_REC_기록/AUDIT/REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서.md
📋 MAT-005 §"심사 이력" 1행 append
🚨 NCR 자동 발행: 4건 (REC-NCR-04-01-2026-001 ~ 004) → MAT-009 §"NCR 발행 현황" 4행 append
🔍 trace_id: run-a1c2d3e4 (status=completed)
👤 심사원: 이감사
📊 결과: 충족 4 · 부분 2 · 부적합 2 · 미평가 4  (지적 4건 — critical 2 · major 1 · minor 1)
⏰ SLA 기한: critical 2026-05-30 / major 2026-07-01 / minor 2026-07-31
⏱ 소요 시간: 6분 24초

▶ 다음 (시정조치 종결):
  /check-process --close-ncr REC-NCR-04-01-2026-001 --capa <시정조치 REC>
  /check-process --list-ncr --overdue            # SLA 경과 NCR 점검
```

### 6-3. list-ncr 출력 예시
```
📋 NCR 목록 (status: open, 4건)
| NCR ID                      | 등급     | 제목         | R/A    | SLA 기한    | 잔여 |
|---|---|---|---|---|---|
| REC-NCR-04-01-2026-001      | critical | 종결 추적     | QA/PM  | 2026-05-30  | 28일  |
| REC-NCR-04-01-2026-002      | major    | KPI 종결율    | QA/QMR | 2026-07-01  | 60일  |
| REC-NCR-04-01-2026-003      | minor    | 평가서 95%   | QA/PM  | 2026-07-31  | 90일  |
| REC-NCR-04-01-2026-004      | critical | 다단계 승인   | PM/PO  | 2026-05-30  | 28일  |
```

### 6-4. close-ncr 종료 시
```
✅ NCR 종결 완료 — REC-NCR-04-01-2026-001
📁 vault/08_REC_기록/AUDIT/REC-NCR-04-01-2026-001_*.md (status=closed)
📋 MAT-009: open 행 제거 → closed 행 추가 (행 이동)
🔍 CAPA: REC-CMMI-04-01-04-01-2026-003
👤 종결자: 박팀장 (PM)
⏱ SLA 준수: ✅ 11일 단축 (기한 2026-05-30 / 종결 2026-05-15)
```

### 6-5. kpi start / update 종료 시
```
✅ KPI 1회차 측정 완료 — CMMI-DEV-ML3 (baseline seed)
📁 MAT-008 §"CMMI-DEV-ML3" — 11행 append
📊 verdict 분포: 🟢 healthy 3 · 🟡 watch 0 · 🟠 recovering 0 · 🔴 critical 4 · ⚪ data_gap 4
🚨 회귀 알림 4건 (모두 critical, baseline seed 라 임계 미달 단독)
   - KPI-CMMI-04-01-02 부적합 종결율: 0.0% (목표 ≥95%)
   - META-COVERAGE 심사 Coverage: 40.0% (목표 ≥80%)
   - META-FINDINGS-DENSITY Findings 밀도: 33.3% (목표 ≤20%)
   - META-NCR-CLOSURE NCR 종결율: 0.0% (목표 ≥95%)
📋 MAT-009 §"NCR 통계" 9 항목 자동 갱신
🔍 trace_id: run-k4f8d2a1
⏱ 소요 시간: 4분 18초

▶ 다음:
  /check-process --kpi show CMMI-DEV-ML3              # 결과 확인
  /check-process --kpi check-regressions              # 전사 알림 모음
  /check-process --kpi start CMMI-DEV-ML3 --period 2026-04-01..2026-06-30   # 2회차 (baseline 비교 자동)
```

### 6-6. kpi check-regressions 출력 예시
```
🚨 전사 회귀 알림 (current rounds, 모든 표준)

| 표준 | 회차 | KPI ID | KPI 명 | 측정값/목표 | verdict | NCR 연계 |
|---|---|---|---|---|---|---|
| CMMI-DEV-ML3 | 1 | KPI-CMMI-04-01-02 | 부적합 종결율 | 0.0% / >=95% | 🔴 critical | NCR-001, NCR-002 |
| CMMI-DEV-ML3 | 1 | META-COVERAGE | 심사 Coverage | 40.0% / >=80% | 🔴 critical | — |
| CMMI-DEV-ML3 | 1 | META-FINDINGS-DENSITY | Findings 밀도 | 33.3% / <=20% | 🔴 critical | NCR-001~004 |
| CMMI-DEV-ML3 | 1 | META-NCR-CLOSURE | NCR 종결율 | 0.0% / >=95% | 🔴 critical | NCR-001~004 |

총 4건 (critical 4 / watch 0). --overdue 옵션 사용 시 SLA 경과한 NCR 만 표기.
```
