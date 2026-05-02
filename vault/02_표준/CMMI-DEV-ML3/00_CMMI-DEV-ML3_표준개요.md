---
type: standard-overview
standard: "CMMI-DEV-ML3"
title: "CMMI for Development v3.0 — Maturity Level 3 표준 개요"
version: "v3.0"
domain: "CMMI"
layer: "L2_engineering"
structure: "capability_model"
integration_mode: "interface_only"
status: draft
created: 2026-04-29
updated: 2026-04-29
tags: [standard, CMMI-DEV-ML3, capability-model, poc]
poc: true
poc_purpose: "인증 모델(CMMI-DEV ML3) 전체를 /process-plan 파이프라인이 소화할 수 있음을 검증. 조직·프로젝트 레벨 PA 혼재, 멀티 프로젝트 대응 미비 등 모듈화 필요성 도출."
poc_date: 2026-04-29
---

> **[PoC]** 이 브랜치(`feat/cmmi-dev-ml3-output`)는 인증 모델 전체 편입 가능성을 검증한 PoC입니다.
> 실운영에서는 PA 그룹 단위(`/process-plan "..."`)로 필요한 모듈만 빌드하세요.
> 발견된 한계: 조직/프로젝트 레벨 PA 혼재 · 멀티 프로젝트 TMP 미비 · 인증 요건 종속 구조.

# CMMI-DEV-ML3 표준 개요

> 상위 기준: [[표준프로세스_구성원칙]] · 문서체계: [[01_문서체계]] · 분류: [[07_표준분류레지스트리]]

## 1. 표준 식별
- **표준 코드**: CMMI-DEV-ML3
- **정식 명칭(영문)**: Capability Maturity Model Integration for Development (CMMI-DEV) v3.0 — Maturity Level 3
- **정식 명칭(국문)**: 개발용 능력 성숙도 모델 통합 v3.0 — 성숙도 레벨 3
- **발행기관 / 발행년도**: ISACA / CMMI Institute, v3.0 (2023, 이후 지속 갱신)
- **국내 대응 표준**: 없음 (자율 채택 모델)
- **관련 법규**: 없음 (자율 채택 — 법적 강제 없음)
- **영역 코드**: `CMMI`
- **Layer**: L2_engineering
- **Structure**: capability_model (성숙도 평가 모델)
- **Integration Mode**: interface_only (독립 체계 + 경계면 연결)

## 2. 적용 범위 (Scope)

본 편입은 CMMI-DEV v3.0 의 **Maturity Level 3 (ML3) 평가 통과 가능 수준** 의 프로세스 체계 수립을 목표로 한다.

- **대상 조직**: 소프트웨어·시스템 개발 조직 (CMMI-DEV View)
- **포함 PA 수**: 20개
  - **Core PAs (17종)**: CAR, CM, DAR, EST, GOV, II, MC, MPM, OT, PAD, PCM, PLAN, PQA, PR, RDM, RSK, VV
  - **Development PAs (2종)**: PI, TS
  - **Supplier PA (1종)**: SAM
- **평가 범위**:
  - ML2 PA (PG2 까지): CM, MC, MPM, PAD, PLAN, PQA, RDM, RSK, SAM, GOV, II
  - ML3 PA (PG3 까지): 위 + CAR, DAR, EST, OT, PCM, PR, VV, PI, TS

> **Practice Group (PG)** 구조: PG1 (Initial) → PG2 (Managed) → PG3 (Defined) → PG4 (Quantitatively managed) → PG5 (Optimizing). ML3 평가는 ML2 PA 의 PG2 + ML3 PA 의 PG3 까지 충족 필요.

## 3. 핵심 구조

### 3.1 Practice Area 카테고리 (CMMI v3.0)

| 카테고리 | 영역 | 포함 PA |
|---|---|---|
| **Doing** (실행) | Ensuring Quality | RDM, PQA, PR, VV |
| | Engineering & Developing Products | TS, PI |
| | Delivering & Managing Services | (본 편입 외) |
| | Selecting & Managing Suppliers | SAM |
| **Managing** (관리) | Planning & Managing Work | EST, PLAN, MC |
| | Managing Business Resilience | RSK |
| | Managing the Workforce | OT |
| **Enabling** (지원) | Supporting Implementation | CM, CAR, DAR |
| **Improving** (개선) | Sustaining Habit & Persistence | GOV, II |
| | Improving Performance | MPM, PCM, PAD |

### 3.2 Practice 구조 (각 PA 공통 양식)
- **Intent (의향)**: PA 의 목적
- **Value (가치)**: PA 수행으로 얻는 비즈니스 효과
- **Practice Statement (실천 선언문)**: 각 Practice 의 핵심 요구
- **Value (Practice 단위)**: 해당 Practice 가 제공하는 가치
- **Example Activities (예시 활동)**: 권고 활동 (필수 아님 — Practice 충족 방식 자유)
- **Example Work Products (예시 작업 산출물)**: 권고 산출물

> 출처: ISACA CMMI v3.0 PA PDF 공통 구조 (paraphrase). 본 평가 모델은 Required(=Practice Statement) / Expected(=의도/가치) / Informative(=Activities/Products) 의 3단계 정보를 제공.

### 3.3 ML3 평가 통과 조건 (요지)
1. ML2 9개 PA 의 모든 PG2 Practice 를 정의·수행·증적 보유
2. ML3 추가 PA 의 모든 PG3 Practice 까지 정의·수행·증적 보유
3. 조직 표준 프로세스 집합(OSSP) + Tailoring 지침을 통한 프로젝트 프로세스 정의
4. 프로세스 자산 라이브러리(PAL), 측정 저장소(Measurement Repository) 운영

## 4. 타 표준과의 관계 (Interface 관점)

본 표준은 `interface_only` 표준이므로, 상위 L1 (HLS 경영시스템) 또는 다른 L2 표준과 **경계면(Interface)** 만 통합하고 본문은 독립 체계로 유지한다.

### 4.1 직접 Interface 대상

| 경계면 | 본 표준 PA | 외부 표준 |
|---|---|---|
| 품질경영 | PQA, GOV | ISO 9001 §5, §9 |
| 문서·구성관리 | CM, PAD | ISO 9001 §7.5, ASPICE SUP.7/8 |
| 변경관리 | CM 2.4, RDM 2.5 | ISO 9001 §8.5, ASPICE SUP.10 |
| 공급자관리 | SAM | ISO 9001 §8.4, ASPICE ACQ |
| 위험관리 | RSK | ISO 31000, ISO 9001 §6.1 |
| 측정·성과 | MPM | ISO 9001 §9.1 |
| 인적자원·교육 | OT | ISO 9001 §7.2 |
| SW 수명주기 | TS, PI, VV | ISO/IEC/IEEE 12207, IEC 62304 |
| 시스템 수명주기 | TS, PI, VV | ISO/IEC/IEEE 15288 |

### 4.2 유사·비교 표준

| 표준 | 비교 |
|---|---|
| **ASPICE** | 자동차 도메인의 capability_model. CMMI 와 유사한 PA-Practice 구조이나 V-model 기반·ISO 26262 연계 |
| **ISO/IEC 33000 (SPICE)** | 일반 SW 프로세스 평가 프레임워크. CMMI 와 평가 방법론 차이 |
| **ISO/IEC/IEEE 12207** | SW 수명주기 프로세스 정의 (CMMI 가 평가, 12207 이 정의 측면) |
| **ISO 9001** | 일반 QMS — CMMI 의 PCM/PAD/PQA/GOV 와 부분 중첩 |

### 4.3 통합 매뉴얼 노트
- `interface_only` 이므로 본 표준은 **CMMI 영역코드 전용** POL/PRO/WI 를 생성한다.
- 상위 ISO 9001 (`QMS`) 가 도입된 조직에서는 CMMI 의 GOV·PCM 일부가 QMS 의 경영검토·내부심사와 중첩될 수 있으므로 MAT-006 계층 매트릭스에 교차 매핑한다.

## 5. 입력자료(_inputs) 인벤토리

### 5.1 카테고리 분포
| 카테고리 | 파일 수 | 라이선스 | content_mode |
|---|---|---|---|
| 01_표준원문 | 40 (영문 20 + 한글 20) | ISACA — paraphrase only | paraphrase |
| 02_법규 | 0 | — | — |
| 03_해설서 | 0 | — | — |
| 04_AsIs | 0 | — | — |
| 05_산업가이드 | 0 | — | — |

### 5.2 PA 별 인벤토리

| PA | Category | 영문 PDF | 한글 PDF |
|---|---|---|---|
| CAR | Core | `_inputs/01_표준원문/CMMI-DEV/Core PAs/CAR.pdf` | `CAR(한글).pdf` |
| CM | Core | `Core PAs/CM.pdf` | `CM(한글).pdf` |
| DAR | Core | `Core PAs/DAR.pdf` | `DAR(한글).pdf` |
| EST | Core | `Core PAs/EST.pdf` | `EST(한글).pdf` |
| GOV | Core | `Core PAs/GOV.pdf` | `GOV(한글).pdf` |
| II | Core | `Core PAs/II.pdf` | `II(한글).pdf` |
| MC | Core | `Core PAs/MC.pdf` | `MC(한글).pdf` |
| MPM | Core | `Core PAs/MPM.pdf` | `MPM(한글).pdf` |
| OT | Core | `Core PAs/OT.pdf` | `OT(한글).pdf` |
| PAD | Core | `Core PAs/PAD.pdf` | `PAD(한글).pdf` |
| PCM | Core | `Core PAs/PCM.pdf` | `PCM(한글).pdf` |
| PLAN | Core | `Core PAs/PLAN.pdf` | `PLAN(한글).pdf` |
| PQA | Core | `Core PAs/PQA.pdf` | `PQA(한글).pdf` |
| PR | Core | `Core PAs/PR.pdf` | `PR(한글).pdf` |
| RDM | Core | `Core PAs/RDM.pdf` | `RDM(한글).pdf` |
| RSK | Core | `Core PAs/RSK.pdf` | `RSK(한글).pdf` |
| VV | Core | `Core PAs/VV.pdf` | `VV(한글).pdf` |
| PI | Development | `Development PAs/PI.pdf` | `PI(한글).pdf` |
| TS | Development | `Development PAs/TS.pdf` | `TS(한글).pdf` |
| SAM | Supplier | `Supplier PA/SAM.pdf` | `SAM(한글).pdf` |

### 5.3 저작권 가드
- 모든 PA PDF는 ISACA / CMMI Institute 저작권 보호 자료
- **20단어 이상 연속 일치 금지** ([[05_입력자료_규칙]] §6)
- 본문 인용은 **paraphrase only**. PA 명칭, Practice 번호 인용은 허용
- 한글 PDF의 일부 표현은 자동번역 결과(예: "엠씨"=MC, "센티엠"=CM, "엠피엠"=MPM)이며 영문 원문이 우선

## 6. 산출물 링크

- **요구사항 분해**: [[01_CMMI-DEV-ML3_요구사항분해]]
- **작업노트**: [[02_CMMI-DEV-ML3_작업노트]]
- **추적성 매트릭스**: `MAT-011_CMMI-DEV-ML3_추적성_v0.1.md` (design phase 후 생성)
- **참고자료(REF)**:
  - [[REF-001_CMMI-DEV-v3.0_모델구조_v1.0]]
  - [[REF-002_CMMI-DEV_ML평가체계_v1.0]]
  - [[REF-003_CMMI-vs-ASPICE_비교_v1.0]]
- **정책(POL)**: design phase 에서 생성 예정
- **절차(PRO)**: design phase 에서 생성 예정

## 7. 참고 문헌

1. ISACA / CMMI Institute, *CMMI for Development, Version 3.0*, 2023 (지속 갱신)
2. CMMI Institute, *CMMI Model — Practice Areas* (PA별 PDF)
3. SEI Carnegie Mellon, *CMMI for Development, Version 1.3* (legacy 참고)
4. ISO/IEC/IEEE 12207:2017 — Systems and software engineering — Software life cycle processes
5. ISO/IEC 33001~33004 — Process assessment framework
