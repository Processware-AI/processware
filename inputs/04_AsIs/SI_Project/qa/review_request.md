---
standard_id: SI_Project
version: "2026.04"
generated_at: "2026-05-13T01:13:48"
status: pending_review
---

# SI_Project (RFP) 인제스트 검토 요청

## 요약
- 사업명: 보건환경종합정보시스템 고도화 사업
- 발주: 대구광역시 보건환경연구원
- 사업비: 342백만원(부가가치세 포함) / 사업기간: 계약체결일로부터 180일
- 추출 단락: 4285건
- 요구사항 추출: 상세 78건 / 목록표 77건
- 검토 필요: 약 9건

## ⚠️ 목록표와 상세 영역 불일치 (1건)
검토 후 [ ] → [x] 표시

- [x] **DAR-008** — 상세 영역에는 있으나 요구사항 목록표(Ⅲ.3)에 누락됨
  → 조치: requirements.yaml 의 DAR-008 항목 유지 결정 시 그대로 두고, 목록표 등록 누락은 RFP 발주처에 질의 사항으로 기록

## ❓ 상세 본문 짧음 / 표 구조 평탄화로 인한 손실 가능성 (8건)
표(테이블) 셀이 단락 단위로 분리되어 일부 텍스트가 라벨 영역으로 합쳐졌을 수 있음. 원문 단락 인덱스를 참조해 clauses.md 또는 sources/RFP.hwpx 에서 직접 확인.

- [x] **SFR-002** :: 로그인 정책관리  (details 길이 43자)
  → clauses.md 단락 [0640] 부터 검토. 누락된 세부내용 보강 시 requirements.yaml 직접 수정.
- [x] **SFR-016** :: 시스템 관리 중 권한관리 기능  (details 길이 46자)
  → clauses.md 단락 [0975] 부터 검토. 누락된 세부내용 보강 시 requirements.yaml 직접 수정.
- [x] **SIR-003** :: 전자문서 결재 시스템 연동  (details 길이 44자)
  → clauses.md 단락 [1168] 부터 검토. 누락된 세부내용 보강 시 requirements.yaml 직접 수정.
- [x] **PMR-003** :: 정기보고  (details 길이 41자)
  → clauses.md 단락 [2039] 부터 검토. 누락된 세부내용 보강 시 requirements.yaml 직접 수정.
- [x] **PMR-004** :: 수시보고  (details 길이 41자)
  → clauses.md 단락 [2057] 부터 검토. 누락된 세부내용 보강 시 requirements.yaml 직접 수정.
- [x] **PMR-013** :: 일정계획  (details 길이 45자)
  → clauses.md 단락 [2333] 부터 검토. 누락된 세부내용 보강 시 requirements.yaml 직접 수정.
- [x] **PMR-014** :: 공동수급형태의 제안  (details 길이 40자)
  → clauses.md 단락 [2352] 부터 검토. 누락된 세부내용 보강 시 requirements.yaml 직접 수정.
- [x] **PSR-005** :: EA 현행화  (details 길이 40자)
  → clauses.md 단락 [2504] 부터 검토. 누락된 세부내용 보강 시 requirements.yaml 직접 수정.

## ℹ️ 자동 분류 가정 — 재확인 권고
- 의무 수준(obligation)은 한국어 키워드 휴리스틱으로 결정 — 기본값은 `shall` (RFP 특성상 거의 모든 요구사항이 계약 명세).
- ECR-* → PRO/WI/REF, SFR-* → PRO/WI/TMP, SER-* → POL/PRO/WI 등으로 target_asset_candidates 가 사전 매핑됨. process-plan 단계에서 재조정 가능.
- 본 RFP 는 단일 프로젝트의 발주 명세이므로 일반 표준(ISO 등)과 달리 '조항(clause)' 개념이 약함. clause 필드는 카테고리 코드 기반으로 'III.4.{category}' 형식으로 일괄 부여.

## ✅ 자동 추출 정상 항목 (확인용)
- 78개 요구사항 ID 전부 식별 (ECR×4, SFR×20, PER×2, SIR×4, DAR×8, TER×3, SER×5, QUR×2, COR×8, PMR×16, PSR×6)
- 각 요구사항의 name·definition·outputs(산출정보) 자동 추출
- 용어 정의(definitions.yaml) — HEIS, LIMS, RDMS, DBMS 등 11건 사전 정의

## 검토 방법
1. 이 파일의 체크박스를 완료 표시 (`- [ ]` → `- [x]`)
2. 필요 시 `inputs/04_AsIs/SI_Project/requirements.yaml` 직접 수정
3. 원문 참조: `inputs/04_AsIs/SI_Project/clauses.md` 또는 `sources/RFP.hwpx`
4. 완료 후 실행:
   ```
   /process-ingest --confirm SI_Project
   ```
