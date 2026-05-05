---
type: session-recap
date: 2026-05-05
title: "아키텍처 개선 (process-ingest·적용요건·inputs/) + /process-audit 신설"
participants: ["dongseok"]
commits:
  - b05c67a  # 아키텍처 개선 — process-ingest 신설 + 폴더 구조 재정의
  - 4eef560  # 사용자 매뉴얼 v1.1 — process-ingest 신설 + 아키텍처 반영
  - d71f44a  # /process-audit 신설 — 외부 표준 부합성 GAP 분석
tags: [session, architecture, process-ingest, process-audit, gap-analysis, refactor]
---

# 세션 회고 — 2026-05-05

## 1. 배경 및 출발점

이전 세션(2026-05-03)에서 사용자 매뉴얼 8종 작성과 커맨드 4종 완성 이후, 이번 세션에서는 두 가지 큰 방향이 도출됐다.

**문제 인식 1 — 입력 구조 이중화**  
`vault/_inputs_common/`과 `vault/02_표준/{코드}/_inputs/` 두 폴더가 중복 존재. "LLM이 다양한 형태의 자료를 바로 적용요건으로 뽑아내는 성능과 완전성에 의심이 간다"는 지적이 출발점.

**문제 인식 2 — 외부 표준 부합성 체크 부재**  
`/process-check`는 내부 이행 심사(PRO/WI vs REC)만 했고, "구축된 프로세스가 ISO 9001을 얼마나 커버하는가?"라는 역방향 질문에 답하는 기능이 없었음.

---

## 2. 아키텍처 개선 (commit b05c67a)

### 2-1. 폴더 구조 재정의

| 변경 전 | 변경 후 | 이유 |
|---|---|---|
| `vault/_inputs_common/` | `inputs/` (vault 바깥) | vault는 생성물만, 입력은 바깥 |
| `vault/02_표준/{코드}/_inputs/` | (삭제) | 위와 통합 |
| `vault/02_표준/` | `vault/02_적용요건/` | 개념 명확화 + 사용자 자유 명명 |
| (없음) | `sources/` | 원본 바이너리 분리 보관 |

**inputs/ 카테고리 5종:**
```
inputs/01_표준원문/  — ISO/IEC/KS 등
inputs/02_법규/     — 국내 법령·규정
inputs/03_해설서/   — 해설서·가이드
inputs/04_AsIs/     — 기존 조직 문서 + act queue
inputs/05_산업가이드/ — 산업별 가이드
```

**핵심 원칙**: `inputs/`는 YAML·MD만. 바이너리 절대 금지. `sources/`는 원본 바이너리 전용, git 제외(README만 추적).

### 2-2. vault/02_적용요건 개념

단순 표준 파일 저장에서 "조직이 해석·채택한 요건 기준선"으로 역할 강화.
- 사용자가 원하는 이름으로 자유 명명 (예: "OOO사 품질경영체계")
- `적용요건.md` 구조: REQ-NNN 형식 요건 + `source_clause` (ISO 조항 매핑) 포함
- 이 파일이 `/process-audit`의 커버리지 분석 기준선이 됨

### 2-3. /process-ingest 신설 (차원 0)

5단계 파이프라인에 차원 0(Ingest)가 추가되어 구조가 확정됐다:
```
차원 0 Ingest  → 차원 1 Plan → 차원 2 Do → 차원 3 Check → 차원 4 Act
/process-ingest   /process-plan   /process-do   /process-check    /process-act
                                                /process-audit
```

**process-ingest 8단계:**
1. Intake (파일 수신·분류)
2. Extraction (텍스트 추출)
3. Parsing (구조 분석)
4. Mining (요건 채굴)
5. Classification (의무/권고/선택 분류)
6. Traceability (조항 간 연결)
7. QA (누락·오류 검사)
8. Handoff (HITL 검토 후 inputs/ 배포)

**핵심 결정:**
- 스캔본 PDF 지원 안 함 → 100자/페이지 미만이면 즉시 abort + 외부 OCR 안내
- HITL 강제: Phase 7 QA 후 반드시 `--confirm`으로 사람 검토 후 확정
- delta 모드: 표준 개정판 처리 (ADD/MODIFIED/DEPRECATED 태깅)
- 출력: `inputs/{카테고리}/{표준코드}/requirements.yaml` 등 YAML/MD 패키지

### 2-4. 에이전트·커맨드 경로 일괄 업데이트

6개 에이전트 파일의 경로 참조 수정:
- `_inputs/04_AsIs/` → `inputs/04_AsIs/`
- `02_표준/` → `02_적용요건/`
- `_inputs_common/` 참조 제거

`.claude/states/` 폴더 신설 → state.yaml을 vault 바깥에 보관.

---

## 3. 사용자 매뉴얼 v1.1 (commit 4eef560)

기존 매뉴얼 6종 업데이트 + MAN-02-0 신규 작성:

| 파일 | 변경 내용 |
|---|---|
| `02-0_표준문서_전처리.md` (신규) | /process-ingest 완전 가이드 |
| `00_시작하기.md` | PDF 유무에 따른 시작 경로 분기 안내 추가 |
| `01_개념이해.md` | "4차원 PDCA" → "5단계 파이프라인" 전면 재작성, 폴더 구조 갱신 |
| `02_프로세스_설계.md` | Phase 0 이진 파일 감지·차단, 적용요건.md 생성 흐름 |
| `06_역할별_가이드.md` | 표준 분석가 역할 신설 |
| `07_FAQ.md` | /process-ingest 섹션 신설, 경로 오류 수정 |

---

## 4. /process-audit 신설 (commit d71f44a)

### 4-1. 기획 배경

현재 `/process-check`의 한계: "내부 기준(PRO/WI)을 이행했는가?" 만 확인 가능.
사용자 질문: "구축된 표준 프로세스가 특정 ISO, IEC에 부합하는지 체크하는 방법이 있나?"

→ 방향이 다른 두 심사를 명확히 분리하기로 결정.

| | `/process-check` | `/process-audit` |
|---|---|---|
| 질문 | 이행 여부 | 설계 커버리지 |
| 기준 | 내부 PRO/WI | 외부 ISO/IEC/KS |
| 입력 | REC 증적 | POL/PRO/WI 자산 |
| 산출 | REC-AUDIT, NCR | REC-GAP |
| MAT | MAT-005 | MAT-002 |

### 4-2. 커버리지 분석 체인

```
외부 표준 조항 (ISO clause)
    ↓ inputs/{표준}/requirements.yaml
적용요건 매핑 (REQ-NNN ↔ ISO clause)
    ↓ vault/02_적용요건/{슬러그}/적용요건.md
내부 자산 커버리지 (POL/PRO/WI frontmatter requirements[])
    ↓
coverage_matrix.yaml → REC-GAP-*.md + MAT-002
```

### 4-3. 신규 파일

**커맨드** (`.claude/commands/process-audit.md`):
- `start --against <표준코드>`: GAP 분석 실행
- `--confirm`: HITL 확정 + 보고서 발행
- `--status`, `--list`: 진행·이력 조회
- `--llm-fallback`: inputs/ 없을 때 LLM 지식 기반
- `--strictness`: strict(THIN까지)/normal(GAP+PARTIAL)/lenient(GAP만)
- `--not-applicable`, `--adjust-gap`: 사람 override

**에이전트** (`.claude/agents/gap-analyzer.md`):
- 표준 요건 로드 (inputs/ 또는 LLM)
- 적용요건 역방향 맵 구성 (ISO clause → REQ-NNN)
- POL/PRO/WI frontmatter 스캔 → 조항별 커버리지 판정
- 산출: `coverage_matrix.yaml`

**에이전트** (`.claude/agents/gap-reporter.md`):
- human_overrides 반영 (N/A 처리, 심각도 조정)
- REC-GAP-{표준}-{YYYY}-{NNN}.md 발행
- MAT-002 §매핑표 갱신

### 4-4. 매뉴얼 갱신

- FAQ: `/process-audit` 섹션 신설 (4문항)
- 역할별 가이드: 심사원 역할에 외부 GAP 분석 항목 추가, 역할표 업데이트
- README: 커맨드 목록에 process-audit 추가

---

## 5. 미결 항목 (deferred)

| 항목 | 상태 | 비고 |
|---|---|---|
| WI 시간적 선후 관계 | 미구현 | preconditions/postconditions 필드 + PRO 시퀀스 그래프 |
| REC 백필 | 미구현 | `/process-do --import` 모드 — 기존 산출물 → REC 변환 |
| process-audit → process-act 자동 트리거 | 미구현 | critical GAP → act queue 자동 등록 |
| 외부 인증기관 포맷 (XLSX/PDF) | 미구현 | REC-GAP 외부 제출용 포맷 |

---

## 6. 핵심 논의·결정 사항

**"외부 표준 GAP 분석을 별도 프로젝트로 빼야 하나?"**  
→ 이 프로젝트 안에 포함. 표준 부합성 체크는 프로세스 관리의 자연스러운 확장이고 컨텍스트 공유가 필요하다.

**"inputs 폴더 중복 어떻게 할까?"**  
→ vault 바깥 단일 `inputs/`로 통합. vault는 생성물(POL/PRO/WI 등)만.

**"적용요건 명칭을 사용자가 자유롭게 지정할 수 있나?"**  
→ 예. 표준 코드와 무관하게 조직이 원하는 이름으로 (예: "OOO사 품질경영체계").

**"스캔본 PDF 지원할까?"**  
→ 지원 안 함. 사전 OCR 변환 필요. 100자/페이지 미만이면 즉시 abort.

---

## 7. 세션 메모리 저장

이번 세션 종료 시 메모리 시스템 초기화:
- `memory/user_profile.md`
- `memory/project_architecture.md`
- `memory/project_commands_agents.md`
- `memory/project_key_decisions.md`
- `memory/project_pending_features.md`
- `memory/feedback_preferences.md`
- `memory/reference_files.md`
