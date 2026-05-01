---
description: 표준 프로세스 심사 (차원 3 Check) — REC ↔ PRO/WI 요건 자동 대조 + 부적합 탐지 + 심사 보고서 발행. ISO §9.2 독립성 강제. 사용 ./audit start <PRO|WI|범위> --auditor "이름" | --confirm <trace> | --status <trace>
argument-hint: "start <PRO|WI|범위> --auditor \"이름\" | --resume <trace_id> | --confirm <trace_id> [--auditor \"이름\"] | --reject-finding <ncr_id> --reason \"...\" | --status <trace_id> | --list-ncr [--status open|closed] | --close-ncr <ncr_id> --capa <REC> [+ --dry-run | --override-independence (PoC만) | --period <from..to> | --strictness strict|normal|lenient]"
---

# 표준 프로세스 심사 하네스 (차원 3 Check)

대상 입력: **$ARGUMENTS**

본 커맨드는 차원 2 (`/do`) 가 누적한 **REC + trace.jsonl + MAT-005** 를 입력으로, AI 심사원이 **PRO/WI 요건 ↔ REC 충족 여부**를 자동 대조하여 **심사 보고서·부적합·KPI** 를 산출한다.

상위 설계: `표준프로세스_AI관리체계_4차원PDCA.md` §3 "차원 3 — CHECK" / §5.2 "AI 독립성 보장" / `AI-Driven CMMI Operating Platform.md` Layer 2 회귀 방지

---

## 0. 실행 원칙

- **자산은 읽기 전용**: POL/PRO/WI/TMP/EX/REC/MAT-001~005,007 은 본 커맨드가 절대 수정하지 않는다.
- **신규 산출물만 생성**: 심사 보고서·부적합 → `vault/08_REC_기록/AUDIT/REC-AUDIT-*.md` 와 `vault/08_REC_기록/AUDIT/REC-NCR-*.md` (Phase 2). NCR 관리대장은 `vault/90_MAT_통합매핑/MAT-006_NCR_관리대장.md` (Phase 2).
- **MAT-005 §심사 이력 만 갱신**: 차원 2 가 §실행 기록 을 누적하듯, 차원 3 은 §심사 이력 섹션에 1행 append.
- **독립성 강제 (ISO 9.2)**: `/audit start` 진입 시 `--auditor` 이름과 대상 trace 들의 `executed_by` 가 1건이라도 일치하면 즉시 abort. PoC 한정 `--override-independence` 만 허용 (Phase 1 만, Phase 4 에서 제거).
- **대화는 차원 2 보다 적다**: 차원 3 은 "사후 검토" 라 사람과의 대화는 매트릭스 확정 1회 (HITL gate) + 부적합 등급 조정 (Phase 2) 정도. 차원 2 의 step-by-step 대화 모델과 다르다.
- **모든 입력·LLM 출력 전수 로그**: `.claude/runs/{trace_id}/trace.jsonl` (심사 증적의 증적).
- **환각 방지**: 충족 판정은 REC 본문에 명시된 값·증적 매트릭스의 trace_id 만 근거로 한다. REC 에 없는 값은 임의로 채우지 않는다.

---

## 1. 인자 파싱 — 진입 모드 (배타적, 1개만 적용)

본 커맨드는 다음 7개 진입 모드 중 하나로 동작한다. 첫 인자에 따라 분기.

### 1-1. `start` 모드 — 신규 심사
```
/audit start PRO-CMMI-04-01 --auditor "이감사"            # 단일 PRO 범위
/audit start WI-CMMI-04-01-03 --auditor "이감사"           # 단일 WI 범위 (좁은 심사)
/audit start CMMI-DEV-ML3 --auditor "이감사"               # 표준 전체 범위 (넓은 심사)
/audit start PRO-CMMI-04-01 --auditor "이감사" --period 2026-01-01..2026-04-30
```
→ 인자 파싱:
- 첫 인자가 `PRO-` / `WI-` / 표준 코드 패턴이면 직접 매칭.
- `--auditor` 누락 시 에러 (독립성 강제 위해 필수).
- `--period` 누락 시 기본값: 지난 분기 (오늘 기준 90일).
- trace_id 생성 (예: `run-a` + 8자 hex), `.claude/runs/{trace_id}/state.yaml` 초기화.

### 1-2. `resume` 모드 — `/audit --resume <trace_id>`
```
/audit --resume run-a1c2d3e4
```
→ `state.yaml` Read · `status` 분기:
  - `pending_confirmation` → "심사원 확정 대기" 안내 + `confirmation_request.md` 경로 출력 + 종료 (사용자가 응답할 차례).
  - `running` (전 세션 중단) → 마지막 단계부터 재개.
  - `completed` → "이미 발행된 심사 보고서" 안내 + `final_audit_path` 출력 + 종료.

### 1-3. `confirm` 모드 — `/audit --confirm <trace_id> [--auditor <이름>] [--adjust-finding <id>=<grade>]`
```
/audit --confirm run-a1c2d3e4
/audit --confirm run-a1c2d3e4 --auditor "이감사"
/audit --confirm run-a1c2d3e4 --adjust-finding F-002=minor
```
→ `pending_confirmation` 인 trace 의 매트릭스를 확정. 등급 조정이 있으면 적용. `audit-reporter` 위임 → REC-AUDIT 발행.

### 1-4. `reject-finding` 모드 — `/audit --reject-finding <finding_id> --reason "..." [--trace <trace_id>]`
```
/audit --reject-finding F-002 --reason "AI 오탐 — REC §3 에 시정 권고 이미 기재" --trace run-a1c2d3e4
```
→ AI 가 부적합으로 판정한 항목을 심사원이 인정하지 않음 (오탐 제거). 매트릭스에서 해당 row 의 `human_override: rejected` 로 마크. `--reason` 필수.

### 1-5. `status` 모드 — `/audit --status <trace_id>`
```
/audit --status run-a1c2d3e4
```
→ trace 의 진행 단계·발견 부적합 수·소요 시간 출력.

### 1-6. `list-ncr` 모드 — `/audit --list-ncr [--status open|closed|all] [--standard <코드>] [--severity critical|major|minor] [--overdue]`
```
/audit --list-ncr                                      # open 인 NCR 모두 (기본)
/audit --list-ncr --status all                         # open + closed 모두
/audit --list-ncr --status closed --standard CMMI-DEV-ML3
/audit --list-ncr --severity critical --overdue        # SLA 기한 경과한 critical NCR
```
→ `vault/90_MAT_통합매핑/MAT-006_NCR_관리대장.md` 의 두 섹션을 Read · 필터 적용 후 표 출력.
- 각 행에 NCR_ID, 등급, 제목, R/A, SLA 기한, 잔여일 (open 만), 상태, 모(母) 심사 wikilink 포함.
- `--overdue` : open 인 NCR 중 `today > sla_due_date` 인 것.
- 출력은 stdout (파일 미생성, 미수정).

### 1-7. `close-ncr` 모드 — `/audit --close-ncr <ncr_id> --capa <REC> [--closed-by <이름>] [--reason "..."]`
```
/audit --close-ncr REC-NCR-04-01-2026-001 --capa REC-CMMI-04-01-04-01-2026-003
/audit --close-ncr REC-NCR-04-01-2026-001 --capa REC-CMMI-04-01-04-01-2026-003 --closed-by "박팀장" --reason "SLA 정의 + 재실행 정상 승인"
```
→ `ncr-drafter` 를 `close` 모드로 호출:
- NCR frontmatter `status: closed` + `capa_rec` / `closed_at` / `closed_by` / `closed_reason` 채움.
- NCR 본문 §7 종결 기록 표 채움.
- MAT-006: §"NCR 발행 현황 (open)" 행 제거 → §"NCR 종결 현황 (closed)" 행 추가 (행 이동).
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
| `--overdue` | SLA 기한 경과한 NCR 만 | list-ncr |

---

## 2. 실행 시퀀스 — 모드별

### 2-A. `start` 모드 (신규 심사)

#### Phase A. 사전 점검 + 독립성 가드 (조기 실패)

A-1. 인자에서 대상 범위 추출:
   - `PRO-*` → 해당 PRO + 그 PRO 의 모든 WI 자식.
   - `WI-*` → 단일 WI.
   - 표준 코드 (`CMMI-DEV-ML3` 등) → MAT-005 의 해당 표준 모든 PRO/WI.
A-2. 대상 PRO/WI 가 vault 에 존재하는지 확인. 미존재 시 abort.
A-3. **독립성 가드 (ISO §9.2)** —
   - MAT-005 §"실행 기록" 섹션을 Read · 본 심사 범위 안의 모든 trace_id 추출.
   - 각 trace 의 `executed_by` 와 `--auditor` 비교.
   - 1건이라도 일치하면 즉시 abort + 에러 출력:
     ```
     ❌ 독립성 위반 (ISO §9.2)
     심사원 "이감사" 가 다음 trace 의 이행자와 동일합니다:
       - run-xxxxxxx (WI-..., 2026-04-22)
     본 심사를 진행하려면 다른 심사원을 지정하거나, 이행 trace 를 범위에서 제외하십시오.
     ```
   - `--override-independence` 가 명시되면 abort 대신 경고 + state.yaml 에 `independence: { overridden: true, violations: [...] }` 기록 후 진행.
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

D-2. 매트릭스 작성 완료 → state.status: `pending_confirmation` + `confirmation_request.md` drop-out (심사원에게 매트릭스 미리보기 + `/audit --confirm` 안내).

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
- options: { dry_run, no_ncr }     # no_ncr=true 면 NCR 발행 보류

[출력]
- vault/08_REC_기록/AUDIT/REC-AUDIT-{PRO|STD}-{회차}-{YYYY}-{NNN}_심사보고서.md
- MAT-005 §"심사 이력" 섹션 1행 append
- (no_ncr=false 일 때) ncr-drafter 자동 위임 → REC-NCR-*.md N건 + MAT-006 N행
- (no_ncr=false 일 때) 보고서 frontmatter ncr_refs[] + §4 finding 블록의 NCR 링크 채움
- state.yaml status: completed + final_audit_path + ncr_count
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
   - MAT-006 §"NCR 발행 현황 (open)" 행 제거 → §"NCR 종결 현황 (closed)" 행 append (이동).
CN-5. 종결 보고 (SLA 준수 여부 포함).

### 2-LN. `list-ncr` 모드 (Phase 2)

LN-1. MAT-006 두 섹션 (open / closed) Read · 표 행 파싱.
LN-2. 필터 적용:
   - `--status open|closed|all` (기본 open)
   - `--standard <코드>`, `--severity <등급>`
   - `--overdue` : open 인 행 중 today > sla_due_date.
LN-3. 결과 표를 stdout 출력 (파일 미생성, 미수정).
LN-4. 0건이면 "조건 충족 NCR 없음" 안내.

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
- `mat006_ncr_issued` — MAT-006 NCR 발행 행 추가 (Phase 2)
- `aborted` — 중단 사유 (독립성 위반 / 요건 0건 / 사용자 중단)

---

## 4. Phase 범위 명시 (현 단계)

본 커맨드는 다음 4 Phase 로 점진 구축된다. 현재는 **Phase 2**.

| Phase | 포함 | 제외 |
|---|---|---|
| 1 | start / resume / confirm / reject-finding / status / 4 에이전트 (planner+collector+checker+reporter) / 단일 PRO PoC / 독립성 inline 가드 / `vault/08_REC_기록/AUDIT/` 산출 / MAT-005 §심사이력 자동 누적 | NCR 자동 발행 / KPI 대시보드 / RBAC 정식 / 다국어 / 외부 시스템 |
| **2 (지금)** | **ncr-drafter** / NCR 일련번호 (`REC-NCR-{POL2}-{PRO2}-{YYYY}-{NNN}`) / **MAT-006** NCR 관리대장 / `--list-ncr`·`--close-ncr` / 시정조치 종결 워크플로우 / SLA 휴리스틱 (critical 20영업일 / major 60일 / minor 90일) / R/A 휴리스틱 (카테고리 → 책임자) / `--no-ncr` 옵션 / confirm 시 NCR 자동 발행 | KPI / 외부 시스템 / RBAC 정식 / 책임자 R/A 정식 매핑 |
| 3 | KPI 대시보드 (MAT-008) / 회귀 알림 / PRO/WI §KPI 자동 추출 / NCR 종결율·SLA 준수율 자동 갱신 / 반복 부적합 TOP 자동 분석 | RBAC 정식 / 외부 시스템 |
| 4 | independence-guard 정식 분리 / RBAC enforcement / 차원 4 인계 hook (NCR → 차원 1 재트리거 큐) / 외부 인증기관 보고서 양식 (XLSX/PDF) / 영업일 정식 계산기 (KST 휴일) | — |

---

## 5. 안전 가드

- 본 커맨드 실행 중 `vault/03_POL ~ 07_EX, 08_REC_기록 (AUDIT/ 제외), 90_MAT_통합매핑/MAT-001~005,007` 어떤 파일도 **수정하지 않는다**. 검증 위반 즉시 중단.
- 쓰기 허용:
  - `vault/08_REC_기록/AUDIT/REC-AUDIT-*.md` (신규)
  - `vault/08_REC_기록/AUDIT/REC-NCR-*.md` (Phase 2 — issue 신규 / close Edit)
  - `vault/90_MAT_통합매핑/MAT-005_*.md` (Edit append, §심사 이력 섹션만)
  - `vault/90_MAT_통합매핑/MAT-006_*.md` (Phase 2 — Edit append / 행 이동, 두 섹션 운영)
  - `.claude/runs/{trace_id}/*` (전체)
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

▶ 다음: /audit --confirm run-a1c2d3e4
   또는 부적합 인정 거부: /audit --reject-finding F-002 --reason "..." --trace run-a1c2d3e4
```

### 6-2. confirm 종료 시 (completed)
```
✅ 심사 보고서 발행 — REC-AUDIT-04-01-01-2026-001
📁 vault/08_REC_기록/AUDIT/REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서.md
📋 MAT-005 §"심사 이력" 1행 append
🚨 NCR 자동 발행: 4건 (REC-NCR-04-01-2026-001 ~ 004) → MAT-006 §"NCR 발행 현황" 4행 append
🔍 trace_id: run-a1c2d3e4 (status=completed)
👤 심사원: 이감사
📊 결과: 충족 4 · 부분 2 · 부적합 2 · 미평가 4  (지적 4건 — critical 2 · major 1 · minor 1)
⏰ SLA 기한: critical 2026-05-30 / major 2026-07-01 / minor 2026-07-31
⏱ 소요 시간: 6분 24초

▶ 다음 (시정조치 종결):
  /audit --close-ncr REC-NCR-04-01-2026-001 --capa <시정조치 REC>
  /audit --list-ncr --overdue            # SLA 경과 NCR 점검
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
📋 MAT-006: open 행 제거 → closed 행 추가 (행 이동)
🔍 CAPA: REC-CMMI-04-01-04-01-2026-003
👤 종결자: 박팀장 (PM)
⏱ SLA 준수: ✅ 11일 단축 (기한 2026-05-30 / 종결 2026-05-15)
```
