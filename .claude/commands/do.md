---
description: 표준 프로세스 실행 (차원 2 Do) — WI 이행·REC 작성 + HITL 정지/재개/승인/반려. 사용: /do <WI번호> | --resume <trace> | --approve <trace> | --reject <trace> --reason "..."
argument-hint: "<WI번호 | 자연어> | --resume <trace_id> | --approve <trace_id> | --reject <trace_id> --reason \"...\" | --status <trace_id> | --check-approvals  [+ --dry-run | --executor <이름> | --auto-approve]"
---

# 표준 프로세스 실행 하네스 (차원 2 Do)

대상 입력: **$ARGUMENTS**

본 커맨드는 `/build-standard` 가 만들어 놓은 자산(WI/TMP/EX/PRO/POL)을 **계약서**로 삼아, AI Agent 가 사람과 대화하며 절차를 이행하고 REC(기록본)를 자동 작성한다.

상위 설계: `표준프로세스_AI관리체계_4차원PDCA.md` §3 "차원 2 — DO" / §5.3 "WI 이중 포맷"

---

## 0. 실행 원칙

- **자산은 읽기 전용**: POL/PRO/WI/TMP/EX 는 본 커맨드가 절대 수정하지 않는다 (개정은 차원 4·1의 책임).
- **REC 만 신규 생성**: 산출물은 `vault/08_REC_기록/` 에만 쓴다.
- **MAT-005 만 갱신**: 추적성은 MAT-005 의 `## 실행 기록 (운영 인스턴스)` 섹션에 1행 append.
- **모든 입력·LLM 출력 전수 로그**: `.claude/runs/{trace_id}/trace.jsonl` (심사 증적).
- **환각 방지**: TMP 필드에 직접 매핑 가능한 값만 REC 에 기록한다. 매핑 불가능한 자유 서술이 필요하면 사람에게 추가 질문.
- **HITL 강제 정지·재개**: WI §5.3 "완료 조건" 에 "승인" 표현이 있거나, WI §2 "수행 주체" 의 "승인자" 역할이 있으면 반드시 사람 승인 게이트 발동. Phase 2 부터 진짜 정지 (`pending_approval`) + 외부 채널 drop-out + `/do --approve|--reject` 응답 후 재개.

---

## 1. 인자 파싱 — 진입 모드 (배타적, 1개만 적용)

본 커맨드는 다음 6개 진입 모드 중 하나로 동작한다. 첫 인자에 따라 분기.

### 1-1. `start` 모드 — 신규 실행
```
/do WI-CMMI-04-01-03                 # 직접 doc_id
/do WI-CMMI-04-01-03_작업산출물_평가_v1.0    # 직접 파일명
/do 작업산출물 평가                   # 자연어 (Phase 3) — process-router 위임
/do 공급자 평가                       # 자연어 + 후보 제시 모드 가능
```
→ 인자 파싱:
- 인자가 `WI-` / `PRO-` 접두사 + doc_id 패턴이면 **직접 매칭** → Phase A 진입.
- 그 외(자연어) → **process-router 위임** (Phase 3 정식 동작):
  - `auto_accepted` → 즉시 Phase A 진입.
  - `candidates_presented` → 후보 표 출력 + 사용자 선택 대기.
  - `no_match` → 구체화 요청 메시지 후 종료.

### 1-2. `resume` 모드 — `/do --resume <trace_id>`
```
/do --resume run-a3f9c2b1
```
→ `state.yaml` Read · `status` 확인:
  - `pending_approval` → "승인 대기 중" 안내 + `approval_request.md` 경로 출력 + 종료 (사용자가 응답할 차례).
  - `ready_to_finalize` (승인 응답이 외부에서 들어와 갱신된 상태) → process-executor 재진입 후 rec-writer 위임.
  - `running` (전 세션 비정상 종료) → 마지막 step 부터 재개.
  - `completed` → "이미 완료된 trace" 안내 + REC 경로 출력.

### 1-3. `approve` 모드 — `/do --approve <trace_id> [--approver <이름>]`
```
/do --approve run-a3f9c2b1
/do --approve run-a3f9c2b1 --approver "박팀장"
```
→ `hitl-gatekeeper` `gate_response` 모드 호출 (decision: approved). 응답 처리 후 자동으로 process-executor 재개 → rec-writer 위임.

### 1-4. `reject` 모드 — `/do --reject <trace_id> --reason "..." [--approver <이름>]`
```
/do --reject run-a3f9c2b1 --reason "표본 부족 — 재수집 필요"
```
→ `--reason` 누락 시 에러. 반려 처리 후 rec-writer 가 REC `status: rejected` 로 마감 + MAT-005 ❌ 반려 표기.

### 1-5. `status` 모드 — `/do --status <trace_id>`
```
/do --status run-a3f9c2b1
```
→ `hitl-gatekeeper` `gate_query` 모드. 정지된 trace 의 현재 상태·승인자·경과 시간 출력.

### 1-6. `check-approvals` 모드 — `/do --check-approvals`
```
/do --check-approvals
```
→ 모든 `.claude/runs/run-*/approval_request.md` 의 frontmatter 를 스캔. `status: approved/rejected` 인 drop-in 응답이 있으면 자동으로 처리 (외부 채널 사용자가 파일을 직접 편집한 경우의 일괄 회수).

### 1-7. `rebuild-catalog` 모드 — `/do --rebuild-catalog [--scope <영역>]`
```
/do --rebuild-catalog                # 전체 표준 재인덱싱
/do --rebuild-catalog --scope CMMI   # CMMI 만
```
→ `traceability-mapper` 를 **catalog-rebuild 모드** 로 호출. 모든 PRO/WI 의 frontmatter + §1 업무목적 + §2 수행주체 + §5 절차 를 스캔해 MAT-007 의 trigger·alias·event_triggers·hitl_required 를 재추출. 사람이 `manual_override: true` 표시한 행은 보존.

### 1-8. 공통 옵션
| 플래그 | 효과 | 적용 모드 |
|---|---|---|
| `--dry-run` | 대화는 진행하되 REC 파일·MAT-005 갱신 생략, 미리보기만 출력 | start, resume, approve |
| `--executor <이름>` | 실행자(작성자) 명시. 미지정 시 시스템 사용자명 자동 인식 | start |
| `--auto-approve` | HITL 게이트를 자동 승인 (PoC·테스트용 — 실운영 금지) | start, resume |
| `--approver <이름>` | 승인/반려 응답자 신원 명시 (감사 증적). 미지정 시 시스템 사용자명 | approve, reject |
| `--reason "..."` | 반려 사유. `--reject` 모드에서 필수 | reject |
| `--scope <영역>` | 카탈로그 재구축 범위 한정 (예: CMMI / ISO9001) | rebuild-catalog |
| `--auto-threshold <0~1>` | process-router 자동 채택 임계 (기본 0.9) | start (자연어 진입) |

---

## 2. 실행 시퀀스 — 모드별

### 2-A. `start` 모드 (신규 실행)

#### Phase A0. 자연어 라우팅 (Phase 3 — 인자가 doc_id 가 아닐 때)
A0-1. 인자가 `WI-`/`PRO-` 접두사 + 영역코드 패턴이면 본 단계 skip → A-1 로.
A0-2. 그 외 자연어면 `process-router` 에이전트 호출:
   - 입력: `query`, `catalog_path: vault/90_MAT_통합매핑/MAT-007_프로세스_카탈로그.md`, `options.auto_threshold` (기본 0.9), `scope_filter` (선택)
A0-3. process-router 반환 처리:
   - `mode: auto_accepted` → 사용자에게 "자동 매칭: {doc_id} ({title}, confidence {score})" 안내 + Phase A 진입.
   - `mode: candidates_presented` → 후보 표 출력 + "[1/2/3] 또는 doc_id 직접 입력" 대기. 응답 수신 후 Phase A 진입.
   - `mode: no_match` → 구체화 요청 메시지 + 종료.
A0-4. trace.jsonl 의 첫 이벤트로 `routed` 기록 (mode, query, selected.doc_id, confidence).

#### Phase A. 사전 점검
A-1. WI 식별 (Phase A0 또는 직접 인자에서). 매칭 실패 시 후보 목록 출력 후 종료.
A-2. WI 파일 Read 성공 확인. frontmatter 의 다음 필드 추출:
   - `doc_id`, `parent_pro`, `parent_pol`, `related_tmp[]`, `related_ex[]`, `owner`, `reviewer`, `approver`, `standards`, `scope_code`
A-3. **TMP 필수 확인**: `related_tmp[]` 가 비어 있으면 실행 중단 (REC 산출 불가 — TMP 부재).
A-4. trace_id 생성 (예: `run-` + 8자 hex).
A-5. `.claude/runs/{trace_id}/` 디렉터리 생성 + `state.yaml` 초기화.

#### Phase B. process-executor 위임
B-1. 서브에이전트 `process-executor` 를 다음 컨텍스트로 호출:
```
[입력]
- wi_path / tmp_path / ex_path / pro_path
- trace_id, executor
- options: {dry_run, auto_approve}

[출력]
- step 별 대화 진행
- state.yaml 갱신
- trace.jsonl 1라인/이벤트
- HITL step 도달 시 hitl-gatekeeper 위임 → 정지
- 모든 step 완료 시 .claude/runs/{trace_id}/rec_payload.yaml 생성
```

B-2. process-executor 가 `state.status: ready_to_finalize` 로 만들면 Phase C 로.
B-3. **HITL 게이트 만나면 `state.status: pending_approval` 로 정지 → 종료** (사용자가 응답할 차례).
   - `hitl-gatekeeper` 가 `approval_request.md` 를 drop-out.
   - 사용자에게 응답 명령 (`/do --approve` / `/do --reject`) 안내.
   - 본 커맨드는 종료. 응답 시 `approve`/`reject` 모드로 재진입.

#### Phase C. rec-writer 위임
C-1. 서브에이전트 `rec-writer` 호출 (입력: trace_id, payload_path, options).
C-2. dry-run 인 경우 REC 미리보기만 출력하고 저장하지 않는다.

#### Phase D. 종결 보고

---

### 2-B. `resume` 모드

R-1. `state.yaml` Read.
R-2. `status` 별 분기:

| status | 동작 |
|---|---|
| `pending_approval` | "승인 대기" 안내 + `approval_request.md` 경로 출력 + 종료 (재개 불가, 응답이 먼저). |
| `ready_to_finalize` | process-executor 재진입 (`mode: resume_after_approval`) → derivation 마무리 + payload 생성 → rec-writer 위임. |
| `running` (전 세션 중단) | process-executor 재진입 (`mode: resume_running`, last_step 부터) → 정상 흐름 이어서. |
| `completed` | "이미 완료" 안내 + final_rec_path 출력 + 종료. |
| `rejected` | "이미 반려 마감" 안내 + REC 경로 출력 + 종료. |
| 미존재 trace_id | 에러 |

---

### 2-C. `approve` / `reject` 모드

AR-1. `state.yaml` Read 후 `status == "pending_approval"` 확인. 아니면 에러.
AR-2. `hitl-gatekeeper` `gate_response` 모드 호출:
```
[입력]
- trace_id
- decision: approved | rejected
- approver_name: <--approver 옵션 또는 시스템 사용자>
- reason: <--reason, reject 시 필수>
- input_source: "/do --approve" or "/do --reject"
```
AR-3. gate_response 처리 완료 후 (`status: ready_to_finalize`):
   - `decision == approved`: process-executor 마지막 step 마무리 (derivation) → rec-writer 위임.
   - `decision == rejected`: rec-writer 를 **rejected 모드**로 직접 호출 (REC.status: rejected).
AR-4. 종결 보고.

---

### 2-D. `status` 모드

S-1. `hitl-gatekeeper` `gate_query` 모드 호출. 결과 출력 후 종료.

---

### 2-F. `rebuild-catalog` 모드

RC-1. `traceability-mapper` 를 `catalog-rebuild` 모드로 호출 (scope 옵션 전달).
RC-2. 결과 출력:
```
✅ MAT-007 카탈로그 갱신 완료
   인덱싱: PRO 20 / WI 145 (정밀 26 + 자동 119)
   manual_override 보존: 0 행
   변경: trigger 추출 갱신 12 행 / 신규 5 행
```

### 2-E. `check-approvals` 모드

CA-1. `Glob ".claude/runs/run-*/approval_request.md"` 전수 스캔.
CA-2. 각 파일의 frontmatter `status` 검사:
   - `pending` → 그대로 두기 (대기 중 표시).
   - `approved` / `rejected` → drop-in 응답으로 간주, `hitl-gatekeeper` `gate_response` 자동 호출.
CA-3. 처리된 trace_id 목록 + 그 결과(approved/rejected/no_change) 표 형태로 출력.
CA-4. drop-in 으로 처리된 trace_id 들에 대해 `approve`/`reject` 모드와 동일한 후속 흐름 (rec-writer 위임) 자동 트리거.

---

## 3. trace_id·state·로그 규약

### 3-1. 디렉터리 구조
```
.claude/runs/{trace_id}/
├── state.yaml          ← 실행 상태 (재개·HITL 대기)
├── trace.jsonl         ← 입력·LLM 출력·승인 전수 로그
└── rec_payload.yaml    ← process-executor → rec-writer 인계용
```

### 3-2. `state.yaml` 스키마
```yaml
trace_id: run-a3f9c2b1
wi_id: WI-CMMI-04-01-03
wi_path: vault/05_WI_업무지침/WI-CMMI-04-01-03_...md
tmp_path: vault/06_TMP_템플릿/TMP-CMMI-04-01-03-01_...md
ex_path:  vault/07_EX_작성예시/EX-CMMI-04-01-03-01_...md
pro_path: vault/04_PRO_절차/PRO-CMMI-04-01_...md
status: running | pending_approval | ready_to_finalize | completed | aborted
started_at: "ISO8601"
executed_by: "{사용자명}"
options:
  dry_run: false
  auto_approve: false
current_step: step-04
steps:
  - id: step-01
    name: 표본 선정
    status: done
    answers:
      sample_items: ["요구사항 등록부", "설계서"]
hitl:
  required: true
  approver_role: "PM"
  approver_name: null         # 응답 후 채워짐
  decision: null              # approved | rejected
  requested_at: null
  responded_at: null
final_rec_path: null
finalized_at: null
```

### 3-3. `trace.jsonl` 이벤트 종류
- `start` — 실행 시작
- `step_enter` — step 진입
- `question` — Agent → 사람 질문 (step / field / prompt)
- `answer` — 사람 → Agent 응답 (값 + 검증 결과)
- `derivation` — 처리 규칙 자동 적용 (예: 점수 합산 → 등급)
- `step_done` — step 종료
- `hitl_request` — 승인 요청 발송
- `hitl_response` — 승인 응답 수신
- `rec_drafted` — REC 초안 작성 완료
- `rec_finalized` — REC 파일 저장 완료
- `mat005_updated` — MAT-005 행 추가
- `aborted` — 중단 사유 기록

---

## 4. Phase 범위 명시 (현 단계)

본 커맨드는 다음 4 Phase 로 점진 구축된다. 현재는 **Phase 2**.

| Phase | 포함 | 제외 |
|---|---|---|
| 1 | 직접 WI 지정 / 단일 step 대화 / TMP 매핑 / REC 1건 생성 / MAT-005 1행 / trace 로그 / HITL `--auto-approve` 모킹 | 자연어 라우팅 / HITL 정식 / 멀티턴 재개 |
| 2 | HITL 정지(`pending_approval`) / 외부 채널 drop-out / `/do --resume\|--approve\|--reject\|--status\|--check-approvals` / 반려 처리 (REC.status: rejected) / 6개 진입 모드 | 자연어 라우팅 / 타임아웃·에스컬레이션 / 외부 IdP 인증 / 다단계 승인 |
| **3 (지금)** | process-router / MAT-007 카탈로그 / 자연어 매칭 (auto_accepted / candidates_presented / no_match) / `--rebuild-catalog` / `--auto-threshold` | 외부 시스템 연동 / 다국어 / RAG |
| 4 | wi-tmp-writer 확장 (steps.yaml 정식 출력) / steps.yaml ↔ MD 동기화 | — |

---

## 5. 안전 가드

- 본 커맨드 실행 중 `vault/03~07_*` (자산 영역) 의 어떤 파일도 **수정하지 않는다**. 검증 위반 즉시 중단.
- `vault/08_REC_기록/` 와 `vault/90_MAT_통합매핑/MAT-005_*.md` 만 쓰기 허용.
- main / feat 브랜치에 직접 push 금지. 커밋은 사용자가 명시 요청 시에만.
- `--dry-run` 외 모드에서 REC 파일을 동일 경로로 덮어쓰는 것은 금지 (일련번호 충돌 시 다음 번호로 진행).

---

## 6. 최종 보고 양식

```
✅ 실행 완료 — WI-CMMI-04-01-03 작업산출물 평가
📁 REC: vault/08_REC_기록/REC-CMMI-04-01-03-01-2026-001_작업산출물_평가서.md
📋 MAT-005 갱신: 실행 기록 섹션 1행 append
🔍 trace_id: run-a3f9c2b1  (.claude/runs/run-a3f9c2b1/)
👤 실행자: {사용자명}
⏸ HITL: required=true / approver=PM / decision=approved (mock)
⏱ 소요 시간: 4분 12초
```
