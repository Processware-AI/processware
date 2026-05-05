---
description: '외부 표준 부합성 심사 (GAP 분석) — inputs/ 의 표준 요건 ↔ 내부 POL/PRO/WI 커버리지 대조 → GAP 보고서 발행 + MAT-002 갱신. 사용: /process-audit start --against <표준코드> | --confirm <trace> | --status <trace>'
argument-hint: 'start --against <표준코드> [--scope <모듈슬러그>] [--strictness strict|normal|lenient] [--llm-fallback] | --confirm <trace_id> [--not-applicable <조항>="사유"] [--adjust-gap <조항>=minor|major|critical] [--no-act-queue] | --status <trace_id> | --list [--status pending|done]'
---

# 외부 표준 부합성 심사 하네스 (GAP 분석)

대상 입력: **$ARGUMENTS**

본 커맨드는 **"우리가 설계한 프로세스가 외부 표준을 얼마나 커버하는가?"** 를 분석한다.  
`/process-check` 가 *이행 증적* 을 심사한다면, 본 커맨드는 *프로세스 설계* 자체를 외부 표준과 대조한다.

```
외부 표준 조항 (ISO/IEC/KS/법규)
    ↓  inputs/{category}/{표준}/requirements.yaml
적용요건 매핑 (REQ-NNN ↔ 표준 조항)
    ↓  vault/02_적용요건/{슬러그}/적용요건.md
내부 자산 커버리지 (POL/PRO/WI 가 REQ-NNN 을 커버하는가?)
    ↓  vault/01_POL / 03_PRO / 05_WI 의 frontmatter requirements[]
gap-analyzer → coverage_matrix.yaml → gap-reporter → REC-GAP-*.md
```

---

## 0. 실행 원칙

- **자산 읽기 전용**: 본 커맨드는 POL/PRO/WI/TMP 를 수정하지 않는다.
- **신규 산출물만 생성**: `vault/08_REC_기록/AUDIT/REC-GAP-{표준코드}-{YYYY}-{NNN}.md` + MAT-002 갱신.
- **환각 방지**: 커버리지 판정은 반드시 파일 실존 + frontmatter 근거. 없으면 GAP.
- **LLM fallback 명시**: `inputs/` 에 표준 요건 파일이 없을 때만 `--llm-fallback` 허용. 이 경우 보고서에 `source: llm_knowledge` 로 표시 + 낮은 신뢰도 경고.
- **HITL 1회 강제**: coverage_matrix 초안 완성 후 반드시 사람이 검토 확정 (`--confirm`). 확정 전까지 보고서 미발행.
- **트레이스 완전 보관**: `.claude/runs/{trace_id}/` — state.yaml + coverage_matrix.yaml + trace.jsonl.

---

## 1. 인자 파싱 — 진입 모드

### 1-1. `start` 모드 — 신규 GAP 분석

```
/process-audit start --against ISO9001
/process-audit start --against ISO9001 --scope "OOO사_품질경영체계"
/process-audit start --against ISO9001 --strictness strict
/process-audit start --against ISO27001 --llm-fallback    # inputs/ 없을 때
```

인자 파싱:
- `--against` 필수. 표준 코드 (예: ISO9001, ISO27001, CMMI-ML3, 개인정보보호법).
- `--scope` 선택. `vault/02_적용요건/` 하위 특정 슬러그만 대상. 생략 시 전체 스캔.
- `--strictness` 기본 `normal`.
- `--llm-fallback` 생략 시, inputs/ 에 표준 파일 없으면 abort + 안내.
- trace_id 생성: `run-g` + 8자 hex.
- `.claude/runs/{trace_id}/state.yaml` 초기화.

strictness 별 GAP 판정 범위:
| strictness | 보고 대상 |
|---|---|
| `strict` | GAP + PARTIAL + THIN (PRO 있으나 WI 없음) |
| `normal` | GAP + PARTIAL |
| `lenient` | GAP 만 |

### 1-2. `confirm` 모드 — HITL 확정 후 보고서 발행

```
/process-audit --confirm run-g1a2b3c4
/process-audit --confirm run-g1a2b3c4 --not-applicable "8.3"="해당 조직은 외주 개발 미실시"
/process-audit --confirm run-g1a2b3c4 --adjust-gap "7.5.1"=minor
```

- `pending_confirmation` 상태 trace 만 처리.
- `--not-applicable` 반복 가능 (조항별 사유 필수).
- `--adjust-gap` 반복 가능. 심각도 override.
- 확정 후 `gap-reporter` 위임 → REC-GAP 발행 + MAT-002 갱신.

### 1-3. `status` 모드

```
/process-audit --status run-g1a2b3c4
```

→ 단계·커버리지 요약·GAP 수 출력.

### 1-4. `list` 모드

```
/process-audit --list
/process-audit --list --status pending
/process-audit --list --against ISO9001
```

→ `.claude/runs/run-g*/state.yaml` Glob → 표로 출력.

---

## 2. Phase 흐름 (start 모드)

### Phase 0 — Preflight

P0-1. 표준 코드 정규화 (대소문자 통일, 구분자 통일: `ISO 9001` → `ISO9001`).

P0-2. 표준 요건 파일 탐색 (우선순위):
```
inputs/01_표준원문/{표준코드}/requirements.yaml    # 1순위
inputs/02_법규/{표준코드}/requirements.yaml        # 2순위 (법규)
inputs/03_해설서/{표준코드}/requirements.yaml      # 3순위 (해설서 기반)
```
- 발견 → `requirements_source: inputs` 로 기록, Phase 1 진행.
- 미발견 + `--llm-fallback` 없음 → **abort**:
  ```
  ⛔ inputs/ 에 {표준코드} 요건 파일이 없습니다.
  
  해결 방법:
    /process-ingest sources/{표준코드}.pdf --standard {표준코드}
    /process-ingest --confirm {표준코드}
  
  또는 LLM 추정 모드로 실행 (낮은 신뢰도):
    /process-audit start --against {표준코드} --llm-fallback
  ```
- 미발견 + `--llm-fallback` → `requirements_source: llm_knowledge` 기록, 경고 출력 후 진행.

P0-3. `vault/02_적용요건/` 하위 적용요건.md 탐색.
- `--scope` 지정 시: `vault/02_적용요건/{슬러그}/적용요건.md` 단일 파일.
- 미지정 시: Glob `vault/02_적용요건/*/적용요건.md` 전체.
- 0건이어도 abort 하지 않음 (직접 frontmatter 매핑으로 fallback).

P0-4. state.yaml 초기화 + trace.jsonl 시작.

---

### Phase 1 — 표준 요건 로드 (`gap-analyzer` 위임)

**위임 입력:**
```yaml
trace_id: run-gXXXXXXXX
standard_code: ISO9001
requirements_source: inputs | llm_knowledge
requirements_path: inputs/01_표준원문/ISO9001/requirements.yaml   # source=inputs 일 때만
applicable_req_paths:
  - vault/02_적용요건/OOO사_품질경영체계/적용요건.md
options:
  strictness: normal
  scope_slug: null | "OOO사_품질경영체계"
```

`gap-analyzer` 가 수행:
- requirements.yaml 에서 조항 목록 추출 (clause, title, obligation, text).
- `llm_knowledge` 모드: LLM 내부 지식으로 표준 조항 목록 생성 (confidence: low 태그).
- 적용요건.md 파싱: REQ-NNN ↔ source_clause 역방향 맵 구성.
- POL/PRO/WI frontmatter Glob → `requirements: [REQ-NNN, ...]` 수집.
- 조항별 커버리지 판정 → `coverage_matrix.yaml` 생성.

산출: `.claude/runs/{trace_id}/coverage_matrix.yaml`

---

### Phase 2 — HITL 확정 게이트

Phase 1 완료 후 **반드시 정지**하고 사용자에게 초안 출력:

```
🔍 GAP 분석 초안 — ISO9001 vs OOO사_품질경영체계
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
전체 조항: 47개
✅ COVERED  : 28개 (59.6%)
🟡 PARTIAL  : 11개 (23.4%)
🔴 GAP      : 6개  (12.8%)
⚪ 분석불가  : 2개  (4.3%)

🔴 GAP 목록 (critical/major):
  4.2  이해관계자 요구사항  [critical] — POL/PRO/WI 없음
  6.1  리스크·기회 조치     [major]   — POL만 있고 PRO·WI 없음
  8.3  제품·서비스 설계     [major]   — 적용요건 매핑 없음
  ...

🟡 PARTIAL 목록 (normal 모드):
  5.1  리더십·의지표명      [minor]   — POL·PRO 있으나 WI 없음
  7.5  문서화 정보          [minor]   — WI 있으나 TMP 없음
  ...

확정: /process-audit --confirm run-gXXXXXXXX
N/A 처리: /process-audit --confirm run-gXXXXXXXX --not-applicable "8.3"="외주 개발 미실시"
심각도 조정: /process-audit --confirm run-gXXXXXXXX --adjust-gap "6.1"=minor
```

state: `pending_confirmation`.

---

### Phase 3 — 보고서 발행 (`gap-reporter` 위임, confirm 후)

**위임 입력:**
```yaml
trace_id: run-gXXXXXXXX
coverage_matrix_path: .claude/runs/run-gXXXXXXXX/coverage_matrix.yaml
human_overrides:
  not_applicable:
    "8.3": "외주 개발 미실시"
  adjusted_severity:
    "6.1": minor
standard_code: ISO9001
```

`gap-reporter` 가 수행:
- coverage_matrix.yaml 에 human_overrides 반영.
- 일련번호 결정: Glob `vault/08_REC_기록/AUDIT/REC-GAP-ISO9001-{YYYY}-*.md` → max + 1.
- `REC-GAP-{표준코드}-{YYYY}-{NNN}.md` 생성.
- MAT-002 §매핑 표 갱신: GAP/PARTIAL/COVERED 행 반영.
- state.yaml: `status: completed`, `report_path` 기록.

---

### Phase 4 — act-trigger 위임 (GAP → 차원 4 큐 자동 push)

gap-reporter 반환값의 `critical_gaps[]` + `major_gaps[]` 합산 건수 > 0 이고 `--no-act-queue` 미설정 시:

**위임 입력:**
```yaml
mode: from_gap
trace_id: run-gXXXXXXXX
gap_rec_id: REC-GAP-{표준코드}-{YYYY}-{NNN}
standard_code: {standard_code}
critical_gaps: [gap-reporter 반환값 그대로]
major_gaps:    [gap-reporter 반환값 그대로]
options:
  dry_run: {--dry-run 여부}
  no_act_queue: false
```

`act-trigger` (from_gap 모드) 가 수행:
- critical/major GAP 마다 `.claude/queues/process-act/queue-q*.yaml` 1건씩 생성.
- 중복 큐(동일 gap_rec_id + clause) 자동 skip.
- MAT-008 §"차원 4 인계" 표 갱신.

GAP 없거나 (critical + major == 0) `--no-act-queue` 설정 시: 이 Phase 생략.

---

## 3. 산출물

```
.claude/runs/{trace_id}/
├── state.yaml                    # 진행 상태·메타
├── coverage_matrix.yaml          # 조항별 커버리지 판정 (raw)
└── trace.jsonl                   # 분석 로그

vault/08_REC_기록/AUDIT/
└── REC-GAP-{표준코드}-{YYYY}-{NNN}_GAP분석보고서.md

vault/90_MAT_통합매핑/
└── MAT-002_규제요구사항_대조표.md  (Edit — 신규/갱신 행 추가)

.claude/queues/process-act/
└── queue-q{hex}.yaml × N  (critical/major GAP 건수)  ← --no-act-queue 미설정 시
```

### coverage_matrix.yaml 구조

```yaml
standard: ISO9001
version: "2015"
audit_date: "2026-05-05"
trace_id: run-gXXXXXXXX
requirements_source: inputs | llm_knowledge
scope_slug: "OOO사_품질경영체계"
strictness: normal

summary:
  total: 47
  covered: 28
  partial: 11
  gap: 6
  not_applicable: 2
  unknown: 0
  coverage_rate: "59.6%"

clauses:
  - clause: "4.1"
    title: "조직과 조직 상황의 이해"
    obligation: mandatory
    req_mapping: "REQ-001"           # 적용요건.md 에서 추출 (없으면 null)
    process_coverage:
      pol: ["POL-001"]
      pro: ["PRO-PPR-101"]
      wi:  ["WI-PPR-101-01"]
      tmp: ["TMP-PPR-101-01"]
    verdict: COVERED | PARTIAL | GAP | NOT_APPLICABLE | UNKNOWN
    severity: null | observation | minor | major | critical
    gap_note: ""
    recommendation: ""
    human_override: null | "not_applicable" | "severity_adjusted"
    confidence: high | medium | low    # llm_knowledge 시 low
```

### REC-GAP 보고서 구조

```markdown
---
type: REC
doc_id: REC-GAP-ISO9001-2026-001
title: "ISO 9001:2015 부합성 GAP 분석 보고서"
standard: ISO9001
version: "2015"
scope: "OOO사_품질경영체계"
audit_date: ...
auditor: ...    # --auditor 지정 시, 생략 시 "system"
trace_id: run-gXXXXXXXX
coverage_rate: "59.6%"
gap_count: 6
status: issued
---

# ISO 9001:2015 GAP 분석 보고서

## 요약
## 커버리지 현황 (조항별)
## GAP 상세 (critical → major → minor 순)
## PARTIAL 상세
## 권고사항 (프로세스 개선 우선순위)
## 다음 단계
```

---

## 4. 에이전트 연계

| Phase | 에이전트 | 입력 | 산출 |
|---|---|---|---|
| 1 | `gap-analyzer` | requirements_path + applicable_req_paths + vault Glob | coverage_matrix.yaml |
| 3 | `gap-reporter` | coverage_matrix.yaml + human_overrides | REC-GAP-*.md + MAT-002 Edit |

---

## 5. 옵션 목록

| 옵션 | 설명 | 적용 모드 |
|---|---|---|
| `--against <코드>` | 대상 외부 표준 코드 (필수) | start |
| `--scope <슬러그>` | 특정 적용요건 슬러그만 | start |
| `--strictness` | strict / normal / lenient | start |
| `--llm-fallback` | inputs/ 없을 때 LLM 지식 사용 | start |
| `--auditor "이름"` | 보고서 심사자 명시 | start |
| `--not-applicable <조항>="사유"` | 해당 조항 N/A 처리 | confirm |
| `--adjust-gap <조항>=<등급>` | 심각도 override | confirm |
| `--no-act-queue` | GAP 발견 시에도 act 큐 자동 push 억제 | confirm |
| `--dry-run` | REC·MAT-002 저장 생략, 미리보기만 | start |

---

## 6. 사용 예시

```bash
# 기본: ISO 9001 대비 GAP 분석 (inputs/ 필요)
/process-audit start --against ISO9001

# 특정 모듈만
/process-audit start --against ISO9001 --scope "OOO사_품질경영체계"

# inputs/ 없이 LLM 추정
/process-audit start --against CMMI-ML3 --llm-fallback

# 엄격 모드 (WI 없으면 PARTIAL)
/process-audit start --against ISO27001 --strictness strict

# 검토 후 확정 (일부 조항 N/A 처리)
/process-audit --confirm run-g1a2b3c4 \
  --not-applicable "8.3"="외주 개발 미실시" \
  --adjust-gap "7.5.1"=minor

# 상태 확인
/process-audit --status run-g1a2b3c4

# 과거 분석 목록
/process-audit --list --against ISO9001
```

---

## 7. process-check 와의 차이

| 구분 | `/process-check` | `/process-audit` |
|---|---|---|
| 질문 | "우리가 절차대로 이행했는가?" | "우리 프로세스가 표준을 커버하는가?" |
| 입력 | PRO/WI 요건 vs REC 증적 | 외부 표준 조항 vs POL/PRO/WI 설계 |
| 기준 | 내부 (자체 PRO/WI) | 외부 (ISO/IEC/KS/법규) |
| 산출 | REC-AUDIT, NCR | REC-GAP |
| MAT 갱신 | MAT-005 §심사이력 | MAT-002 §매핑표 |
| HITL | 매트릭스 확정 1회 | 커버리지 초안 확정 1회 |

---

## 8. Scope / Roadmap

| Phase | 현재 구현 | 미구현 |
|---|---|---|
| 1 (지금) | start / confirm / status / list / 2 에이전트 (gap-analyzer + gap-reporter) / coverage_matrix / REC-GAP / MAT-002 갱신 / HITL 게이트 / llm-fallback 모드 / 자동 /process-act 트리거 | 다국어 보고서 / 외부 인증기관 포맷 (XLSX) |
