---
description: '표준 문서 전처리 (차원 0 Ingest) — sources/ 의 PDF·DOCX·PPTX 등을 추출·정규화·요구사항화하여 inputs/ 에 정제된 YAML·MD 패키지로 변환. /process-plan 의 선행 필수 단계. 사용: /process-ingest sources/ISO9001.pdf --standard ISO9001 --version 2015'
argument-hint: "<source_file> --standard <ID> [--version <ver>] [--category <01-05>] [--ocr] [--mode delta --base-version <ver>] | --confirm <standard_id> [--mode delta] | --status <standard_id> | --list [--category <01-05>]"
---

# 표준 문서 전처리 파이프라인 (차원 0 Ingest)

대상 입력: **$ARGUMENTS**

본 커맨드는 `sources/` 에 배치된 원본 문서(PDF·DOCX·PPTX 등)를 **추출 → 정규화 → 요구사항 단위 분할 → 분류 → 추적성 매핑 → QA 검토** 단계로 처리하여, `/process-plan` 이 안정적으로 읽을 수 있는 **정규화된 입력 패키지** 를 `inputs/` 에 생성한다.

---

## 0. 핵심 원칙

- **소스와 산출물 분리**: 원본 파일은 `sources/` 에서만. `inputs/` 는 ingest 출력 전용 — 바이너리 파일 진입 절대 금지.
- **스캔본 처리 정책**: `--ocr` 플래그 없으면 즉시 중단. `--ocr` 지정 시 `ocrmypdf`(Tesseract 백엔드)로 자동 OCR 처리 후 계속 진행. OCR 처리된 파일은 `_state.yaml.ocr_processed: true` 마킹.
- **HITL 강제 게이트**: Phase 7 QA 완료 후 반드시 사람이 검토·확인해야 Phase 8 실행 가능. 자동 통과 없음.
- **입력 불변**: `sources/` 원본은 본 커맨드가 절대 수정하지 않는다. 읽기 전용.
- **멱등성**: 동일 standard_id 재실행 시 기존 outputs 덮어쓰기 전 사용자 확인.

---

## 1. 폴더 구조

```
projectroot/
  sources/                              ← 원본 파일 전용 (바이너리 허용)
    ISO9001_2015.pdf
    개인정보보호법_2024.pdf
    ISO9001_2024_개정사항.pdf           ← delta 문서
    현_품질매뉴얼_v3.docx

  inputs/                               ← ingest 출력 전용 (바이너리 금지)
    01_표준원문/
      ISO9001/
        structure.yaml
        requirements.yaml
        clauses.md
        definitions.yaml
        annexes.yaml
        source_map.yaml
        qa/
          review_request.md
          extraction_quality_report.md
        _state.yaml
    02_법규/
      개인정보보호법/
        ...
    03_해설서/
    04_AsIs/
    05_산업가이드/
    06_목표흐름/
      business_flow.yaml    ← flow-proposer 생성 (사람이 직접 수정 가능)

  vault/                                ← process-plan 산출물
    02_적용요건/
    ...
```

### 카테고리 자동 분류 기준

| 카테고리 | 대상 문서 | 예시 |
|---|---|---|
| `01_표준원문` | 국제표준 (ISO·IEC·KS·ANSI 등) | ISO9001, IEC62304, ASPICE |
| `02_법규` | 국내외 법령·고시·규정 | 개인정보보호법, 산업안전보건법 |
| `03_해설서` | 표준 해설서·인증기관 가이드 | KISA ISMS-P 가이드 |
| `04_AsIs` | 기존 조직 내부 문서 | 현_품질매뉴얼, 기존_절차서 |
| `05_산업가이드` | 업종 프레임워크·체크리스트 | NIST CSF, COBIT, 식약처 GMP |

`--category` 미지정 시 파일명·문서 첫 페이지 메타데이터로 자동 판단. 불명확 시 사용자에게 질문.

---

## 2. 진입 모드

### 2-1. 신규 ingest (기본)
```
/process-ingest sources/ISO9001_2015.pdf --standard ISO9001 --version 2015
/process-ingest sources/개인정보보호법.pdf --standard 개인정보보호법 --version 2024 --category 02
/process-ingest sources/현_품질매뉴얼.docx --standard 현_품질매뉴얼 --category 04
```

### 2-2. delta 모드 (표준 개정)
```
/process-ingest sources/ISO9001_2024_개정사항.pdf --standard ISO9001 --mode delta --base-version 2015
```
→ 기존 `inputs/01_표준원문/ISO9001/requirements.yaml` 와 대조하여 ADD/MODIFIED/DEPRECATED 처리.

### 2-3. confirm 모드 (HITL 승인)
```
/process-ingest --confirm ISO9001
/process-ingest --confirm ISO9001 --mode delta
```
→ `review_request.md` 검토 완료 후 Phase 8 실행.

### 2-4. status 모드
```
/process-ingest --status ISO9001
```
→ 현재 ingest 단계·요건 수·검토 대기 여부 출력.

### 2-5. list 모드
```
/process-ingest --list
/process-ingest --list --category 01
```
→ `inputs/` 내 완료된 ingest 목록 + 상태 출력.

---

## 3. 실행 시퀀스 — 신규 ingest

### Phase 1. Source Intake

1-1. `--standard` 슬러그 생성 (소문자·언더스코어). 예: `ISO9001_2015`  
1-2. `sources/<source_file>` 존재 확인. 없으면 abort.  
1-3. `inputs/<category>/<standard_id>/` 이미 존재 시:
  - `_state.yaml` 의 `overall_status` 확인.
  - `done` 또는 `pending_confirmation` → "이미 처리됨. 재실행하시겠습니까? (Y/N)"
  - N 이면 중단.  
1-4. `_state.yaml` 초기화:
```yaml
standard_id: ISO9001
version: "2015"
source_file: sources/ISO9001_2015.pdf
category: "01_표준원문"
mode: new          # new | delta
overall_status: running
current_phase: intake
started_at: "ISO8601"
phases:
  intake: done
  extraction: pending
  parsing: pending
  mining: pending
  classification: pending
  traceability: pending
  qa: pending
  handoff: not_started
counts:
  clauses: 0
  requirements: 0
  flagged_items: 0
```
1-5. 파일 해시(SHA-256) 생성 → `_state.yaml.source_hash` 저장 (추적성).

---

### Phase 2. Text Extraction

2-1. 파일 유형별 처리:
  - `.pdf` → 텍스트 레이어 추출 시도.
  - `.docx` / `.pptx` / `.xlsx` → XML 구조 파싱.
  - `.md` / `.txt` → 직접 읽기.

2-2. **스캔본 감지** (PDF 한정):
  - 추출 텍스트가 전체 페이지 평균 **100자 미만** 이면 스캔본으로 판단.

  **`--ocr` 플래그 없는 경우** → 즉시 중단:
  ```
  ❌ 스캔본 PDF 감지 — 작업 중단
  이 파일은 이미지 기반 PDF(스캔본)입니다.

  OCR로 자동 처리하려면:
    /process-ingest sources/ISO9001_2015.pdf --standard ISO9001 --ocr

  또는 외부 도구로 텍스트 변환 후 재투입:
    1. Adobe Acrobat / ABBYY FineReader 등으로 텍스트 PDF 변환
    2. 변환 파일을 sources/ 에 배치 후 재실행
  ```
  `_state.yaml.overall_status: aborted` + `abort_reason: scanned_pdf`.

  **`--ocr` 플래그 있는 경우** → OCR 처리 분기 (Phase 2-OCR):

  2-OCR-1. `ocrmypdf` 설치 확인:
  ```bash
  which ocrmypdf
  ```
  미설치 시:
  ```
  ❌ ocrmypdf 미설치 — OCR 처리 불가
  설치 방법: brew install ocrmypdf
  설치 후 재실행하세요.
  ```
  `_state.yaml.overall_status: aborted` + `abort_reason: ocrmypdf_not_found`.

  2-OCR-2. OCR 실행:
  ```bash
  ocrmypdf --force-ocr -l kor+eng \
    sources/ISO9001_2015.pdf \
    .claude/runs/ingest_{standard_slug}/ocr_output.pdf
  ```
  - `-l kor+eng`: 한국어 + 영어 동시 인식 (한글 문서 대응).
  - `--force-ocr`: 기존 텍스트 레이어 무시 후 재인식 (혼합 PDF 대응).
  - 출력 파일은 `.claude/runs/ingest_{standard_slug}/` 임시 디렉터리. `sources/` 와 `inputs/` 에는 쓰지 않는다.

  2-OCR-3. OCR 성공 시 → OCR'd PDF 에서 텍스트 재추출 → 이후 Phase 2-3 이상 정상 진행.

  2-OCR-4. `_state.yaml` 에 OCR 마킹:
  ```yaml
  ocr_processed: true
  ocr_tool: ocrmypdf
  ocr_lang: kor+eng
  ocr_completed_at: "ISO8601"
  ```

  2-OCR-5. OCR 품질 경고: 추출 텍스트가 여전히 페이지 평균 100자 미만이면:
  ```
  ⚠️ OCR 후에도 텍스트 추출이 불충분합니다.
  스캔 품질이 낮거나 손상된 파일일 수 있습니다.
  계속 진행하시겠습니까? (Y/N)
  ```

2-3. 추출된 텍스트 → `inputs/<category>/<standard_id>/clauses.md` 임시 저장 (raw).  
2-4. 페이지번호·헤더·푸터·목차 페이지 제거.  
2-5. 추출 로그 → `qa/extraction_quality_report.md` 초안:
  - 총 페이지 수, 추출 성공 페이지 수, 추출 실패 페이지 목록.
  - 표·그림 추출 실패 항목.

---

### Phase 3. Structural Parsing

3-1. 표준 유형별 구조 패턴 적용:

| 표준 계열 | 구조 패턴 |
|---|---|
| ISO/IEC | Clause → Sub-clause → Note → Example → Annex |
| ASPICE | Process → Base Practice → Generic Practice → Indicator |
| CMMI | Practice Area → Practice → Example Work Product |
| IEC 62304 / ISO 26262 | Part → Clause → Requirement → Work Product |
| 국내 법령 | 조 → 항 → 호 → 목 |
| 자유 형식 (AsIs) | 제목 → 항목 (휴리스틱) |

3-2. `structure.yaml` 생성:
```yaml
standard_id: ISO9001
version: "2015"
source_type: international_standard
document_structure:
  - id: "4"
    title: Context of the organization
    sub_clauses:
      - id: "4.1"
        title: Understanding the organization and its context
      - id: "4.2"
        title: Understanding the needs and expectations of interested parties
  - id: "7"
    title: Support
    sub_clauses:
      - id: "7.5"
        title: Documented information
        sub_clauses:
          - id: "7.5.1"
            title: General
```

3-3. Annex, Note, Example 분리 태그 부착.  
3-4. 구조 파싱 실패 비율이 20% 초과 시 경고 → `qa/extraction_quality_report.md` 에 기록.

---

### Phase 4. Requirement Mining

4-1. 요구사항 후보 문장 탐지 패턴:

| 의무 수준 | 탐지 키워드 |
|---|---|
| `shall` | shall, must, is required to, shall be, shall include |
| `should` | should, it is recommended, ought to |
| `may` | may, is permitted to, is allowed to |
| 증적 | evidence shall, records shall, work product shall |
| 역할 | is responsible for, shall appoint, shall ensure |

4-2. 복합 문장 분리: "A shall B, and C shall D" → 2건의 독립 요구사항.  
4-3. 중복 문장 병합 (동일 절·유사도 95% 이상).  
4-4. 요구사항 ID 부여: `{STANDARD_ID}-{CLAUSE}-REQ-{NNN}`. 예: `ISO9001-7.5.1-REQ-001`

---

### Phase 5. Classification

5-1. 각 요구사항을 아래 유형으로 분류:

| 유형 | 설명 |
|---|---|
| `normative` | 반드시 준수해야 하는 요구사항 |
| `recommendation` | 권고사항 (should) |
| `informative_note` | 참고 설명 |
| `example` | 예시 |
| `definition` | 용어 정의 |
| `annex_guidance` | 부속서 가이드 |
| `evidence_requirement` | 산출물·증적 요구사항 |
| `process_requirement` | 프로세스 수행 요구사항 |
| `role_requirement` | 책임·역할 요구사항 |
| `record_requirement` | 기록 보관 요구사항 |

5-2. 후속 산출물 후보 매핑 (`target_asset_candidates`):

| 요구사항 유형 | 산출물 후보 |
|---|---|
| 정책 원칙 | POL |
| 프로세스 수행 | PRO, WI |
| 양식·기록 | TMP, REC |
| 증적·산출물 | TMP, EX, REC |
| 추적성 | MAT |
| 참고자료 | REF |

5-3. `requirements.yaml` 생성:
```yaml
requirements:
  - id: ISO9001-7.5.1-REQ-001
    clause: "7.5.1"
    clause_title: "Documented information — General"
    text: >
      The organization's quality management system shall include documented
      information required by this International Standard.
    obligation: shall
    type: normative
    classification: process_requirement
    target_asset_candidates:
      - POL
      - PRO
    evidence_candidates:
      - Quality Management System documentation
    tags: []
    status: active          # active | deprecated | modified (delta 모드용)
    notes: ""
```

---

### Phase 6. Traceability Mapping

6-1. 각 요구사항에 원문 위치 정보 연결 → `source_map.yaml`:
```yaml
source_map:
  - requirement_id: ISO9001-7.5.1-REQ-001
    source_file: sources/ISO9001_2015.pdf
    page: 23
    clause: "7.5.1"
    paragraph_index: 2
    source_text: >
      The organization's quality management system shall include documented
      information required by this International Standard.
    source_text_hash: "sha256:abc123..."
```

6-2. 조항 → 요구사항 매트릭스 생성 → `clause_to_requirement_matrix.yaml`:
```yaml
matrix:
  - clause: "7.5.1"
    requirement_ids:
      - ISO9001-7.5.1-REQ-001
      - ISO9001-7.5.1-REQ-002
  - clause: "7.5.2"
    requirement_ids:
      - ISO9001-7.5.2-REQ-001
```

6-3. 용어 정의 별도 추출 → `definitions.yaml`.  
6-4. Annex 내용 별도 정리 → `annexes.yaml`.

---

### Phase 7. QA Review → **HITL 강제 게이트**

7-1. 자동 품질 검사:

| 검사 항목 | 기준 |
|---|---|
| 누락 조항 탐지 | structure.yaml 조항 수 vs requirements.yaml 커버 조항 수 비교 |
| 단일 조항 요건 과소 | 규범적 조항에 REQ 0건 → 의심 |
| 복합 문장 미분리 | 단일 REQ에 shall 2회 이상 → 검토 권고 |
| 추출 실패 페이지 | extraction_quality_report 교차 확인 |
| 분류 미확정 | type = unknown 인 항목 |

7-2. `qa/review_request.md` 생성:
```markdown
---
standard_id: ISO9001
version: "2015"
generated_at: "2026-05-05T14:30:00"
status: pending_review
---

# ISO9001 인제스트 검토 요청

## 요약
- 총 조항: 87개 / 요건 추출: 142건 / 검토 필요: 11건

## ⚠️ 누락 의심 조항 (3건)
검토 후 [ ] 체크 표시

- [ ] §4.2 이해관계자 요구사항
  → 추출 텍스트 불완전 (47자). 원문 p.8 직접 확인 필요.
  → 관련 요건: requirements.yaml 에서 ISO9001-4.2 검색

- [ ] §9.1.3 분석 및 평가
  → 조항 경계 불명확. 인접 조항과 혼합 가능성.

- [ ] Annex A (전체)
  → 정보 제공용(Informative) 으로 분류됐으나 확인 필요.

## ❓ 모호한 요구사항 (7건)
- [ ] ISO9001-6.1.2-REQ-003
  → 복합 문장: "The organization shall plan actions ... and evaluate the effectiveness"
  → 분리 필요 여부 판단

- [ ] ISO9001-8.4.1-REQ-001
  → shall / should 혼재. 의무 수준 재확인.

(... 전체 목록 ...)

## ℹ️ 품질 정보
- 추출 실패 페이지: 없음
- 표 추출 실패: 3건 (p.34, p.67, p.89) — annexes.yaml 확인
- 전체 추출 품질: 양호

## 검토 방법
1. 이 파일의 체크박스를 완료 표시
2. 필요 시 requirements.yaml 직접 수정
3. 완료 후 실행:
   /process-ingest --confirm ISO9001
```

7-3. **프로세스 완전 정지**. 사용자 응답 전까지 Phase 8 진입 불가.  
7-4. `_state.yaml.overall_status: pending_review` 전환.  
7-5. 출력:
```
⏸  검토 대기 — ISO9001 인제스트 Phase 7 완료

📊 추출 결과:
   조항 87개 / 요건 142건 / 검토 필요 11건

📋 검토 파일:
   inputs/01_표준원문/ISO9001/qa/review_request.md

✏️  직접 수정 가능:
   inputs/01_표준원분/ISO9001/requirements.yaml

▶  검토 완료 후:
   /process-ingest --confirm ISO9001
```

---

### Phase 8. Handoff Package 확정 (confirm 후 실행)

8-1. `--confirm <standard_id>` 진입 시 `_state.yaml.overall_status == pending_review` 확인.  
8-2. `review_request.md` 의 체크박스 완료율 확인:
  - 미완료 항목 있으면: "미검토 항목 N건이 있습니다. 계속하시겠습니까? (Y/N)"  
8-3. `requirements.yaml` 최종 유효성 검사:
  - 필수 필드(`id`, `clause`, `text`, `obligation`, `type`) 누락 항목 확인.
  - 누락 시 목록 출력 + abort.  
8-4. `_state.yaml` 최종 집계:
```yaml
overall_status: done
confirmed_at: "ISO8601"
counts:
  clauses: 87
  requirements: 142
  normative: 98
  recommendation: 22
  informative: 22
  flagged_and_reviewed: 11
```
8-5. 완료 보고:
```
✅ ISO9001 인제스트 완료

📁 출력 위치: inputs/01_표준원문/ISO9001/
   ├── structure.yaml      (조항 구조)
   ├── requirements.yaml   (요건 142건)
   ├── clauses.md          (전문 텍스트)
   ├── definitions.yaml    (용어 31건)
   ├── annexes.yaml        (Annex A~C)
   └── source_map.yaml     (원문 위치 매핑)

📊 요건 분포:
   normative 98건 / recommendation 22건 / informative 22건

▶  다음 단계:
   /process-ingest sources/ISO27001.pdf --standard ISO27001   # 추가 표준 ingest
   /process-plan "OOO사 품질경영체계"                          # 프로세스 생성
```

---

### Phase 9. Business Flow 제안 — Agent `flow-proposer`

**`--confirm` 완료 직후 자동 실행.** 추가 표준 ingest 예정이면 사용자에게 확인 후 진행.

9-1. `inputs/06_목표흐름/business_flow.yaml` 존재 확인.
   - **있으면**: "기존 business_flow.yaml이 있습니다. 갱신(delta)하시겠습니까? (Y/N)"
   - **없으면**: 신규 생성 모드.
9-2. Agent `flow-proposer` 호출.
   - 표준 분석 → 시나리오 도출 → HITL 선택 → `inputs/06_목표흐름/business_flow.yaml` 저장.
9-3. 완료 보고:
```
✅ 업무 시나리오 확정 완료

📁 inputs/06_목표흐름/business_flow.yaml
   시나리오 N건 확정 (추가 M건 포함)

▶  다음 단계:
   /process-plan "OOO사 품질경영체계"    # 프로세스 생성
   (business_flow.yaml 을 직접 수정 후 재실행 가능)
```

---

## 4. delta 모드 — 표준 개정 처리

### 전제
- 기존 ingest 완료된 표준이 존재 (`overall_status: done`).
- 인간이 개정사항 문서를 `sources/` 에 직접 등록.
- delta 문서는 변경된 조항만 포함하거나, 개정 요약 문서 형태도 허용.

### 시퀀스

D-1. Phase 1~6 동일하게 수행 (delta 문서 기준으로 요건 추출).  
D-2. Phase 6 완료 후 **기존 `requirements.yaml` 과 대조**:
```yaml
# delta 처리 결과 표시
requirements:
  - id: ISO9001-7.5.1-REQ-001
    status: modified
    previous_text: "..."
    current_text: "..."
    change_summary: "문서화된 정보 범위 확대"

  - id: ISO9001-4.2-REQ-003
    status: deprecated
    deprecated_reason: "2024 개정에서 §4.2a로 재편"

  - id: ISO9001-4.2a-REQ-001
    status: added
    obligation: shall
    ...
```

D-3. `qa/delta_review_request.md` 생성 (ADD·MODIFIED·DEPRECATED 항목 목록).  
D-4. 동일한 HITL 강제 게이트.  
D-5. confirm 후 기존 `requirements.yaml` 에 delta 반영 + `_state.yaml` 버전 이력 누적.

---

## 5. 상태 관리

**경로**: `.claude/states/ingest_{standard_slug}_state.yaml`

**status 값**:

| status | 의미 |
|---|---|
| `running` | 처리 중 |
| `pending_review` | Phase 7 완료, 인간 검토 대기 (HITL 게이트) |
| `done` | confirm 완료, inputs/ 패키지 확정 |
| `aborted` | 스캔본 감지 또는 사용자 중단 |

---

## 6. 안전 가드

- **`sources/` 읽기 전용**: 원본 파일 절대 수정 안 함.
- **`inputs/` 바이너리 금지**: 본 커맨드가 `inputs/` 에 쓰는 파일은 YAML·MD·TXT 만 허용. 바이너리 생성 시 버그로 간주.
- **`vault/` 불가침**: 본 커맨드는 `vault/` 어떤 파일도 읽거나 쓰지 않는다.
- **스캔본**: `--ocr` 없으면 즉시 abort. `--ocr` 있으면 `ocrmypdf` 자동 처리. OCR 임시 파일은 `.claude/runs/ingest_*/` 에만 저장 — `sources/`·`inputs/` 에는 절대 쓰지 않음.
- **재실행 보호**: `overall_status: done` 상태에서 재실행 시 반드시 사용자 확인.

---

## 7. process-plan 연동 — 바이너리 가드

`/process-plan` 실행 시 `inputs/` 스캔:
- `.pdf` / `.docx` / `.pptx` / `.xlsx` / `.hwp` 발견 시:
  ```
  ❌ inputs/ 에 바이너리 파일이 있습니다 — 작업 중단

  발견된 파일:
    inputs/01_표준원문/ISO9001_2015.pdf

  조치:
    /process-ingest sources/ISO9001_2015.pdf --standard ISO9001 --version 2015
  ```
- 바이너리 파일이 없을 때만 process-plan 정상 진행.

---

## 8. 전체 파이프라인 위치

```
[sources/]           ← 인간이 원본 배치
      ↓
/process-ingest      ← 차원 0: 전처리
      ↓ (HITL 검토·confirm)
[inputs/]            ← 정규화된 YAML·MD 패키지
      ↓
/process-plan        ← 차원 1: 프로세스 생성
      ↓
[vault/02_적용요건/ + POL·PRO·WI·TMP·EX·MAT]
      ↓
/process-do          ← 차원 2: 실행
/process-check       ← 차원 3: 심사
/process-act         ← 차원 4: 개선
```
