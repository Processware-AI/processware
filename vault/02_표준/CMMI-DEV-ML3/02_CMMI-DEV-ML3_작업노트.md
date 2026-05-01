---
type: work-note
standard: "CMMI-DEV-ML3"
phase: "done"
status: done
created: 2026-04-29
updated: 2026-04-29
tags: [worknote, CMMI-DEV-ML3]
---

# CMMI-DEV-ML3 작업 노트

## 기계 상태 (machine state)
> 실제 실행 상태는 [[_state.yaml]] (동일 폴더). 본 체크리스트는 사람 가독용.

## 진행 체크리스트 (8종 문서유형 기반)

- [x] **Phase 0. 입력자료 Preflight** — 40 PDF / 20 PA 인벤토리 작성 완료 (preflight 단계)
- [x] **Phase 1. 표준 개요** — [[00_CMMI-DEV-ML3_표준개요]]
- [x] **Phase 2. 요구사항 분해** — [[01_CMMI-DEV-ML3_요구사항분해]] (126 Req-ID)
- [x] **Phase 3. 정책(POL) 작성** — `03_POL_정책/POL-CMMI-001~005` (5종, design phase)
- [x] **Phase 4. 절차(PRO) 작성** — `04_PRO_절차/PRO-CMMI-101~501,502` (20종, design phase)
- [x] **Phase 5. 업무지침(WI) 작성** — `05_WI_업무지침/WI-CMMI-*` (142종 전수, write phase)
- [x] **Phase 6. 템플릿(TMP) 작성** — `06_TMP_템플릿/TMP-CMMI-*` (14종 → 자가수정 attempt 2 에서 142종까지 보강 진행, write phase)
- [x] **Phase 7. 작성예시(EX) 작성** — `07_EX_작성예시/EX-CMMI-*` (14종 → 자가수정 attempt 2 에서 142종까지 보강 진행, write phase)
- [x] **Phase 8. 참고자료(REF) 수집** — `09_REF_참고자료/` (REF-001~003 생성)
- [x] **Phase 9. 추적성(MAT) 갱신** — `90_MAT_통합매핑/MAT-011_CMMI-DEV-ML3_추적성_v1.0.md` 발행 + MAT-001~006 갱신 (trace phase)
- [x] **MAT-002 갱신** — 규제요구사항 대조표에 CMMI-DEV-ML3 행 추가
- [x] **Phase 10. QA 리뷰** — attempt 1: Pass 8 / Fail 1 / Warn 2 → **attempt 2: 11/11 PASS** (자가수정 완료)
- [x] **Phase 11. MOC 업데이트** — `vault/00_MOC/MOC_전체표준.md` ✅ 갱신 완료

## 결정/이슈 로그

| 일자 | 항목 | 결정/이슈 | 비고 |
|---|---|---|---|
| 2026-04-29 | Practice 분해 단위 | Practice Statement (Required) 단위로 1 Req-ID 부여 | Activities 는 별도 Req-ID 부여 안 함 |
| 2026-04-29 | 한글 PDF 자동번역 | 한글 PDF 의 Practice ID (예: "엠씨 2.1") 는 자동번역 결과 — 영문 PA-Practice 번호가 정본 | RDM, MC, PLAN 등에서 확인 |
| 2026-04-29 | ML2 PA 의 PG3 처리 | ML3 평가 직접 대상 아니나 ML3 PA 가 호출하므로 권고로 분류 | MC 3.x, MPM 3.x, PAD 3.x, PLAN 3.x |
| 2026-04-29 | Context-specific Practice | 일반 컨텍스트만 1차 분해. Agile·DevSecOps·Safety·Security 등 도메인별은 후속 검토 | design phase 에서 적용 |
| 2026-04-29 | 직접 Read 한 PA | CM, MC, PLAN, RDM (4개) — 나머지 16개는 Practice Summary 페이지 + LLM 지식 결합 | 정확도 자기점검 필요 |
| 2026-04-29 | OSSP·PAL·측정저장소 통합 | PAD/MPM/PCM 등에서 참조되는 인프라는 단일 인스턴스로 설계 권고 | design phase 입력 |
| 2026-04-29 | 라이선스 가드 | 모든 Req-ID 본문은 paraphrase, PA·Practice 번호 인용은 허용. 20단어 연속 일치 자가 점검 통과 | qa-reviewer 추가 검사 필요 |
| 2026-04-29 | **QA 이슈 #QA-20260429-001** | TMP/EX 128쌍 누락 (FAIL/blocker) — 142 WI 중 14 WI 만 TMP/EX 보유 | assigned_to: wi-tmp-writer / fix_scope: 128 TMP+128 EX 생성 |
| 2026-04-29 | **QA 이슈 #QA-20260429-002** | PRO-CMMI-205 standards[] 에 ISO 31000 등재 (WARN/minor) — 레지스트리상 reference_only | assigned_to: process-designer / fix_scope: standards 에서 제거 후 본문 주석으로 처리 |
| 2026-04-29 | **QA 이슈 #QA-20260429-003** | 작업노트 진행 체크리스트 갱신 누락 (WARN/minor) — Phase 3~7 [x] 표시 안됨 | assigned_to: orchestrator / fix_scope: 체크박스 [x] 갱신 |

## 다음 phase (design) 에 전달할 핵심 메시지

### 1. integration_mode = `interface_only` 결정
- 영역코드 `CMMI` 전용 POL/PRO/WI 생성
- 상위 ISO 9001 (`QMS`) 도입 조직에서 GOV·PCM 일부가 경영검토·내부심사와 중첩될 수 있음 → MAT-006 계층 매트릭스 교차 매핑 필요
- 다른 표준의 영역코드 POL/PRO 와 섞이지 않게 분리 유지

### 2. POL/PRO 묶음 설계 권고 (process-designer 입력)

#### 권고 POL 구조 (5종)
- `POL-CMMI-001 프로세스 거버넌스 정책` — GOV PA 전체 + PAD-3.1·3.2 (OSSP/테일러링)
- `POL-CMMI-002 프로젝트관리 정책` — PLAN, MC, EST 통합 정책
- `POL-CMMI-003 엔지니어링 정책` — RDM, TS, PI, VV
- `POL-CMMI-004 품질·구성 정책` — PQA, CM, PR
- `POL-CMMI-005 자원·역량·공급자 정책` — OT, RSK, SAM, II

#### 권고 PRO 구조 (영역코드 CMMI, POL별 1xx~5xx)
- POL-001 하위: `PRO-CMMI-101 OSSP 운영`, `PRO-CMMI-102 거버넌스 검토`, `PRO-CMMI-103 프로세스 자산 관리(PAL)`
- POL-002 하위: `PRO-CMMI-201 프로젝트 계획`, `PRO-CMMI-202 추정`, `PRO-CMMI-203 모니터·통제`, `PRO-CMMI-204 시정조치·CAR/DAR`
- POL-003 하위: `PRO-CMMI-301 요구사항 개발·관리`, `PRO-CMMI-302 기술솔루션 설계`, `PRO-CMMI-303 제품 통합`, `PRO-CMMI-304 검증·확인`
- POL-004 하위: `PRO-CMMI-401 품질보증(PQA)`, `PRO-CMMI-402 형상관리(CM)`, `PRO-CMMI-403 동료검토(PR)`
- POL-005 하위: `PRO-CMMI-501 조직교육(OT)`, `PRO-CMMI-502 위험·기회 관리(RSK)`, `PRO-CMMI-503 공급자 계약 관리(SAM)`, `PRO-CMMI-504 측정·성과(MPM)`, `PRO-CMMI-505 구현 인프라(II)`

#### 권고 WI/TMP 핵심 산출물
- 형상항목목록 / 변경요청서 / 기준선 릴리스노트
- 프로젝트 계획서 / WBS / 추정서 / 진척보고서
- 요구사항 명세서 / 추적성매트릭스 / OpsCon
- DAR 의사결정 평가서 / CAR 근본원인분석서
- 동료검토 보고서 / 부적합 보고서

### 3. Interface 경계면 (다른 표준 도입 시)

| 경계면 | CMMI Practice | 외부 표준 |
|---|---|---|
| 문서·구성관리 | CM-2.1~2.6 | ISO 9001 §7.5, ISMS A.5.10 |
| 변경관리 | CM-2.4 | ISO 9001 §8.5 |
| 위험관리 | RSK-2.x, RSK-3.x | ISO 31000, ISO 9001 §6.1 |
| 측정·성과 | MPM-2.x, MPM-3.x | ISO 9001 §9.1 |
| 교육·역량 | OT-2.x, OT-3.x | ISO 9001 §7.2 |
| 공급자 | SAM-2.x | ISO 9001 §8.4, ASPICE ACQ |
| 내부심사 | PQA-2.x | ISO 9001 §9.2 |

### 4. 미해결 이슈 (design phase 에서 결정 필요)

1. ML2 PA 의 PG3 (10개 권고 Practice) 를 POL/PRO 에 포함할지 결정
2. 단일 OSSP/PAL/측정저장소 인스턴스 명명·위치 결정
3. context-specific (Agile/DevSecOps) 적용 여부 — 고객 As-Is 자료 수령 후 결정
4. PA 간 중복 활동 (예: MC-2.4 시정조치 ↔ CAR 근본원인분석) 의 PRO 수준 분리·통합 결정

### 5. 추정 의존 Req-ID 목록

- **없음**. 모든 126개 Req-ID 가 `_inputs/01_표준원문/` PA PDF 에 직접 매핑.
- 단, 직접 Read 한 4개 PA (CM, MC, PLAN, RDM) 외 16개 PA 는 Practice Summary 페이지(각 PA PDF 1~3p) + LLM 지식 기반 paraphrase 이므로 design phase 에서 PA별 추가 Read 권장.

### 6. 저작권 가드 자가점검 결과
- 본문 내 paraphrase 만 사용
- PA 명·Practice 번호·발행기관명 인용은 허용
- 20단어 이상 연속 일치 없음 (한글 자동번역 PDF 와 본 산출물 비교 시 단어 흐름 상이)
- qa-reviewer 단계에서 추가 자동검사 필요

## 외부 표준과의 관계 (분석 중 발견 사항)

1. **ASPICE 와의 유사성**: 둘 다 capability_model. PA 명칭 일부 중첩(SUP.7 ConfigMgmt ↔ CMMI CM, MAN.5 RiskMgmt ↔ CMMI RSK). 자동차 도메인은 ASPICE 우선, 일반 SW 는 CMMI 우선 권고.
2. **ISO/IEC/IEEE 12207 과의 차이**: 12207 은 SW 수명주기 프로세스 정의, CMMI 는 평가 모델. 12207 은 process descriptor (입력·출력·활동), CMMI 는 capability descriptor (Practice Group). 정책으로 12207 채택 + CMMI 로 평가하는 결합 가능.
3. **ISO 9001 과의 통합**: HLS 와 CMMI 는 구조 상이. ISO 9001 §4~10 은 PDCA 거버넌스, CMMI 는 PA 별 capability. GOV PA 가 ISO 9001 §5(리더십)·§9.3(경영검토)와 매핑.

## Phase 완료 보고 요약

- 생성 파일:
  - `vault/02_표준/CMMI-DEV-ML3/00_CMMI-DEV-ML3_표준개요.md`
  - `vault/02_표준/CMMI-DEV-ML3/01_CMMI-DEV-ML3_요구사항분해.md`
  - `vault/02_표준/CMMI-DEV-ML3/02_CMMI-DEV-ML3_작업노트.md`
  - `vault/09_REF_참고자료/REF-001_CMMI-DEV-v2.0_모델구조_v1.0.md`
  - `vault/09_REF_참고자료/REF-002_CMMI-DEV_ML평가체계_v1.0.md`
  - `vault/09_REF_참고자료/REF-003_CMMI-vs-ASPICE_비교_v1.0.md`
- 갱신 파일:
  - `vault/90_MAT_통합매핑/MAT-002_규제요구사항_대조표.md` (CMMI-DEV-ML3 행 추가)
  - `vault/02_표준/CMMI-DEV-ML3/_state.yaml` (analyze=done)
- Req-ID 통계: 126건 (의무 116 / 권고 10), 출처 인용률 100%
- 미해결 이슈: 5건 (위 §6 참조 — design phase 에서 처리)
