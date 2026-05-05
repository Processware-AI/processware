---
description: 'REC 백필 (기존 산출물 → REC 변환) — 레거시 문서(DOCX/XLSX/PDF 등)를 WI 자동 매칭 후 표준 REC 로 변환. 배치·단건 모두 지원. 사용: /process-backfill <path> | --confirm <trace> | --resume <trace> | --status <trace> | --list'
argument-hint: "<파일|폴더> [--wi WI-XX] [--backfiller <이름>] [--date YYYY-MM] [--scope <레이블>] [--ocr] [--dry-run] | --confirm <trace_id> | --resume <trace_id> | --status <trace_id> | --list"
---

# REC 백필 하네스

대상 입력: **$ARGUMENTS**

레거시 문서(Word·Excel·PDF 등)를 MAT-007 기반 자동 매칭 후 표준 REC 로 변환한다.  
생성된 REC 는 `verdict_type: legacy_evidence` 로 마킹되어 `/process-check` 심사 시 별도 처리된다.

---

## 0. 실행 원칙

- **기존 자산 절대 수정 금지**: POL/PRO/WI/TMP/EX/MAT 파일 읽기 전용.
- **REC 만 신규 생성**: `vault/08_REC_기록/` 에만 쓴다.
- **legacy_evidence 명시**: 모든 백필 REC 의 frontmatter 에 `status: backfilled` + `verdict_type: legacy_evidence` 기록.
- **75% 임계값**: confidence < 75% 는 ⚠️ 경고 표시 + 사람 확정 필수.
- **매칭 불가 파일**: ❌ 표시 후 제외. 강제 진행하지 않는다.
- **배치 HITL 단일화**: 파일별 HITL 반복 없이 전체 결과를 한 테이블로 한 번만 제시.

---

## 1. 진입 모드

### 1-1. `start` 모드

```
/process-backfill sources/old_docs/                        # 배치 (폴더)
/process-backfill sources/sprint_review.docx               # 단건
/process-backfill sources/old_docs/ --backfiller "홍길동" --date 2026-03
/process-backfill sources/old.docx --wi WI-CMMI-04-01-03   # 단건 + 수동 WI 지정
/process-backfill sources/scan.pdf --ocr                   # 스캔본 PDF OCR 처리
/process-backfill sources/old_docs/ --ocr --dry-run        # 스캔본 포함 폴더 미리보기
```

`--wi` 는 단건 전용. 폴더 배치 시 `--wi` 지정은 무시하고 자동 매칭 적용.

→ Phase 1 진입.

### 1-2. `confirm` 모드 — `/process-backfill --confirm <trace_id>`

HITL 확정 후 Phase 5 (Map) 부터 재개.  
`state.yaml.status == pending_hitl_confirmation` 인 trace 에만 적용.

### 1-3. `resume` 모드 — `/process-backfill --resume <trace_id>`

중단된 trace 이어 실행. state.yaml 의 last_phase 부터 재개.

### 1-4. `status` 모드 — `/process-backfill --status <trace_id>`

trace 진행 상태·결과 조회.

### 1-5. `list` 모드 — `/process-backfill --list`

`.claude/runs/run-b*/state.yaml` Glob → 백필 이력 테이블 출력.

---

## 2. 파이프라인 (7 Phase)

### Phase 1 — Scan

1-1. 입력 경로가 폴더인 경우: `DOCX / XLSX / PDF / PPTX / PPT / XLS / DOC` 확장자 재귀 수집.  
1-2. 단건인 경우: 해당 파일 1건 목록.  
1-3. 지원 확장자 외 파일은 목록에서 제외하고 로그.  
1-4. trace_id 생성: `run-b{8자리 hex}`.  
1-5. `.claude/runs/{trace_id}/state.yaml` 초기화:

```yaml
trace_id: run-bXXXXXXXX
type: backfill
status: running
last_phase: scan
source_path: <입력 경로>
backfiller: <--backfiller 값 또는 "unknown">
backfill_date: <--date 값 또는 오늘 날짜 YYYY-MM>
options:
  dry_run: false
  forced_wi: null     # --wi 지정 시 채움
  scope_explicit: <--scope 값 또는 null>  # null이면 파일별 경로 자동 추론
files: []             # Phase 1 완료 후 채워짐
```

1-6. 파일 목록을 state.yaml `files[]` 에 저장 (path, size, extension).

1-7. **scope 추론** (파일별):
   - `--scope` 명시 시: 모든 파일에 해당 값 적용.
   - `--scope` 미지정 + 폴더 입력: 입력 루트 바로 아래 첫 번째 서브폴더명을 scope 레이블로 사용.
     - 예: `sources/projects/project-A/sprint.docx` → scope: `"project-A"` (입력 루트가 `sources/`인 경우)
     - 예: `sources/old_docs/2024/Q1/sprint.docx` → scope: `"2024"` (입력 루트가 `sources/old_docs/`인 경우는 `"2024"`)
     실제로는 입력 루트 바로 아래 첫 번째 디렉토리명을 사용.
   - `--scope` 미지정 + 단건 입력: scope: `"(미지정)"`.
   - 추론된 scope 는 `files[].scope` 에 기록. HITL Phase 4 에서 사용자가 수정 가능.

### Phase 2 — Extract

2-1. 각 파일에서 텍스트 추출:

| 확장자 | 처리 방식 |
|---|---|
| DOCX / DOC | XML 파싱 → 단락·표 추출 |
| XLSX / XLS | 시트별 셀 값 추출 |
| PPTX / PPT | 슬라이드별 텍스트 추출 |
| PDF (텍스트 기반) | 텍스트 레이어 추출 |
| PDF (스캔본) | `--ocr` 없으면 ❌ 제외 / `--ocr` 있으면 Phase 2-OCR 분기 |

2-2. **스캔본 PDF 감지**: 페이지 평균 추출 텍스트 100자 미만.

  **`--ocr` 없는 경우**: `files[].status: excluded_scan_no_ocr` 로 제외 + 로그.
  ```
  ⚠️ scan.pdf — 스캔본 PDF (OCR 처리 필요). 제외됨.
     처리하려면: /process-backfill <path> --ocr
  ```

  **`--ocr` 있는 경우** → Phase 2-OCR 분기:

  2-OCR-1. `ocrmypdf` 설치 확인 (`which ocrmypdf`). 미설치 시 즉시 abort:
  ```
  ❌ ocrmypdf 미설치 — OCR 처리 불가
  설치: brew install ocrmypdf
  ```

  2-OCR-2. OCR 실행 (스캔본 파일별):
  ```bash
  ocrmypdf --force-ocr -l kor+eng \
    <원본_스캔본.pdf> \
    .claude/runs/{trace_id}/ocr/<원본_스캔본_ocr.pdf>
  ```
  - `-l kor+eng`: 한국어 + 영어 동시 인식.
  - `--force-ocr`: 혼합 PDF (텍스트+이미지) 전체 재인식.
  - OCR 임시 파일은 `.claude/runs/{trace_id}/ocr/` 에만 저장. `sources/` 에는 절대 쓰지 않는다.

  2-OCR-3. OCR'd PDF에서 텍스트 재추출. 여전히 100자 미만이면:
  ```
  ⚠️ scan.pdf — OCR 후에도 텍스트 불충분 (스캔 품질 불량).
  제외 처리합니다.
  ```
  `files[].status: excluded_ocr_quality_low`.

  2-OCR-4. OCR 성공 파일: `files[].ocr_processed: true` 마킹.

2-3. 추출 결과를 `sources/legacy/{상대경로}.md` 에 저장. 상대경로는 입력 루트 기준으로 계산한다.

  **경로 계산 규칙**:
  - 폴더 입력: 입력 루트(`source_path`)를 기준으로 상대경로 보존.
    - 예: 입력 `sources/old_docs/`, 파일 `sources/old_docs/2024/Q1/sprint.docx`
    - → `sources/legacy/2024/Q1/sprint.md`
  - 단건 입력: 파일명만 사용.
    - 예: 입력 `sources/sprint.docx` → `sources/legacy/sprint.md`
  - 중간 디렉토리는 자동 생성한다.

  **MD 형식 (Obsidian 호환)**:

  ```markdown
  ---
  source_doc: sources/{원본파일명}
  source_hash: sha256:<hash>
  extracted_at: "<ISO8601>"
  scope: "<--scope 값 또는 경로 자동 추론 결과>"
  doc_type_signals: [<평가서|검토표|회의록|보고서 등>]
  metadata:
    date: "<추출된 날짜 또는 미확인>"
    author: "<추출된 작성자 또는 미확인>"
    approver: "<추출된 승인자 또는 미확인>"
  ocr_processed: <true|false>
  status: pending_confirm
  ---

  # {문서 제목}

  ## {섹션 제목}
  {단락 내용}

  | {표 헤더1} | {표 헤더2} | ... |
  |---|---|---|
  | {셀} | {셀} | ... |
  ```

  추출 규칙:
  - DOCX: XML 파싱 → H1(문서 제목) + H2/H3(단락 제목) + MD 표(표 구조) 보존.
  - XLSX: 시트별 H2 제목 + MD 표.
  - PPTX: 슬라이드별 H2(슬라이드 제목) + 내용.
  - PDF: 텍스트 레이어 → 페이지 구조 최대한 보존.
  - `doc_type_signals`: 문서 제목·첫 heading 에서 유형 키워드 추출 (평가서, 검토표, 회의록, 보고서, 계획서, 결과서 등).
  - `metadata.date/author/approver`: 본문·표에서 날짜·작성자·승인자 추출. 불명확하면 `"(미확인)"`.

2-4. 추출 실패(OCR 외 오류) 파일은 `files[].status: extract_failed` 로 표시 + 제외.

### Phase 3 — Match

3-1. `backfill-matcher` 에이전트 위임:
```yaml
trace_id: run-bXXXXXXXX
legacy_dir: sources/legacy/
forced_wi: <--wi 값 또는 null>
confidence_threshold: 75
scope_explicit: <--scope 값 또는 null>
```

3-2. backfill-matcher 가 반환한 `mapping_draft.yaml` 을 `.claude/runs/{trace_id}/` 에 저장.  
3-3. state.yaml `last_phase: match` 갱신.

### Phase 4 — HITL

4-1. `mapping_draft.yaml` 읽어 테이블 구성:

```
[Back-fill 매핑 검토] — run-bXXXXXXXX
총 {N}건 | 자동 매칭 {n1}건 | ⚠️ 저신뢰도 {n2}건 | ❌ 매칭 불가 {n3}건

No. 파일                              scope          추천 WI               confidence
──────────────────────────────────────────────────────────────────────────────────
1.  sprint_review_2026Q1.docx       project-A      WI-CMMI-04-01-03     87%  ✅
2.  peer_review_api.xlsx            project-A      WI-CMMI-04-01-05     72%  ⚠️
3.  test_report_2026-03.docx        project-B      WI-CMMI-04-02-01     65%  ⚠️
4.  meeting_kick_off.docx           hr             (매칭 불가)           --   ❌

❌ 항목(4번)은 자동 제외됩니다.
⚠️ 항목은 WI 수정 권장. 수정: "2=WI-CMMI-04-01-04" 형식.
그대로 진행: "확정"
```

4-2. 사용자 응답 파싱:

| 입력 예시 | 동작 |
|---|---|
| `"확정"` | 현재 매핑 그대로 진행 |
| `"2=WI-CMMI-04-01-04"` | 2번 파일의 WI 수정 |
| `"3 scope=전사-품질"` | 3번 파일의 scope 수정 |
| `"3 제외"` | 3번 파일 제외 (REC 미생성) |
| `"2=WI-CMMI-04-01-04, 3 scope=전사-품질"` | 복합 수정 |
| `"전체 취소"` | 작업 중단 |

- `"확정"` → state.yaml `status: pending_hitl_confirmation` + 확정 내용 반영.
- `"2=WI-XX, 3 제외"` 등 → mapping_draft.yaml 수정 후 테이블 재출력.
- `"3 scope=..."` → mapping_draft.yaml 해당 파일의 scope 필드 수정 후 테이블 재출력.
- `"전체 취소"` → state.yaml `status: cancelled` 후 종료.

4-3. ❌ 항목은 `state.yaml files[].status: excluded_no_match` 로 기록 (REC 미생성).

4-4. 확정 완료 시:
```
✅ 매핑 확정 — {n}건 진행, {m}건 제외

📂 sources/legacy/ 에 추출된 MD 파일이 생성되었습니다.
   Obsidian 에서 내용을 검토·수정한 후 아래 명령으로 계속 진행하세요.
   (수정 없이 그대로 진행해도 됩니다.)

▶ /process-backfill --confirm run-bXXXXXXXX
```

state.yaml `status: pending_hitl_confirmation` 으로 정지.

### Phase 5 — Map (confirm 후 진입)

5-1. 확정된 매핑 목록 순회.  
5-2. 각 파일 + 대응 WI 의 TMP 읽기.  
5-3. `sources/legacy/{파일명}.md` 에서 TMP 필드 값 추출 (LLM):
   - frontmatter `metadata` (date/author/approver) 우선 추출.
   - 필드명·섹션명과 MD 본문·표를 대조하여 최적 값 매핑.
   - 사용자가 Obsidian 에서 수정한 내용이 그대로 반영됨.
   - 매핑 불가 필드는 `"(원본 미확인)"` 으로 채움.
5-4. 파일별 `backfill_payload.yaml` 을 `.claude/runs/{trace_id}/payloads/` 에 저장:

```yaml
source_doc: sources/sprint_review_2026Q1.docx
source_hash: sha256:<hash>
wi_id: WI-CMMI-04-01-03
wi_path: vault/05_WI_업무지침/WI-CMMI-04-01-03_*.md
tmp_id: TMP-CMMI-04-01-03-01
tmp_path: vault/06_TMP_템플릿/TMP-CMMI-04-01-03-01_*.md
backfiller: 홍길동
backfill_date: "2026-03"
fields:
  평가대상: "API 모듈 v2.3"
  평가일: "2026-03-14"
  평가자: "(원본 미확인)"
  ...
```

### Phase 6 — Generate

6-1. 각 `backfill_payload.yaml` 에 대해 `rec-writer` 에이전트를 `mode: backfill` 로 위임:

```yaml
mode: backfill
trace_id: run-bXXXXXXXX
payload_path: .claude/runs/{trace_id}/payloads/{파일}.yaml
options:
  dry_run: <--dry-run 여부>
```

6-2. dry_run 이면 미리보기 출력 후 종료.

### Phase 7 — Index

7-1. 생성된 모든 REC 에 대해 MAT-005 `## 실행 기록` 섹션에 1행 append:

```
| {backfill_date} | run-bXXXXXXXX | {표준} | [[WI-...]] | [[REC-...]] | {backfiller} | ⚠️ 백필 | backfilled |
```

7-2. trace.jsonl 에 `backfill_complete` 이벤트.  
7-3. state.yaml `status: completed` 갱신.

---

## 3. 완료 보고

```
✅ REC 백필 완료 — run-bXXXXXXXX

📁 생성된 REC ({n}건):
   vault/08_REC_기록/REC-CMMI-04-01-03-01-2026-001_작업산출물_평가표.md  (backfilled)
   vault/08_REC_기록/REC-CMMI-04-01-05-01-2026-001_동료검토_결과표.md   (backfilled)

❌ 제외 ({m}건):
   meeting_kick_off.docx — 매칭 불가

📋 MAT-005 §실행기록 {n}행 추가
⚠️  verdict_type: legacy_evidence — /process-check 심사 시 partial 로 계산됨
```

---

## 4. 옵션 목록

| 옵션 | 설명 |
|---|---|
| `--wi <WI번호>` | 수동 WI 지정 (단건 전용, confidence 100% 처리) |
| `--backfiller <이름>` | 백필 담당자 명시 (REC에 기록됨) |
| `--date <YYYY-MM>` | 원본 문서 생성 시점 (미지정 시 오늘 날짜) |
| `--scope <레이블>` | 조직 범위 레이블 (예: "프로젝트-A", "HR팀", "전사-품질"). 미지정 시 폴더명 자동 추론 |
| `--ocr` | 스캔본 PDF OCR 처리 활성화 |
| `--dry-run` | 실제 REC 생성 없이 결과 미리보기 |

---

## 5. 강제 규칙

- 쓰기 허용 경로: `sources/legacy/` (추출 MD), `vault/08_REC_기록/` (REC), `vault/90_MAT_통합매핑/MAT-005_*.md` (인덱스). 그 외 쓰기 금지.
- OCR 임시 PDF는 `.claude/runs/{trace_id}/ocr/` 에만 저장. OCR'd PDF를 `sources/` 에 직접 쓰지 않는다.
- 매칭 불가 파일은 절대 강제 진행하지 않는다.
- `verdict_type: legacy_evidence` 누락 금지 — 백필 REC 임을 항상 명시.
- source_hash 기록 필수 — 원본 문서 추적성 보장.
