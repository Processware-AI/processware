---
type: PRO
doc_id: PRO-CMMI-03-01
title: "요구사항 개발 절차"
version: "0.1"
status: draft
owner: "Requirements Engineer Lead"
reviewer: "Chief Engineer"
approver: "Project Manager"
scope_code: CMMI
scope: "고객 요구사항 도출 → 제품 요구사항 도출·할당 → 요구사항 분석·확인"
parent_pol: "[[POL-CMMI-03_엔지니어링_정책]]"
standards: [CMMI-DEV-ML3-V1.3]
standards_meta:
  publisher: "Software Engineering Institute (CMU/SEI)"
  year: 2010
  license: "internal_use_derivative_work"
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_acronym: RD
pa_full_name: "Requirements Development"
pa_category: "Engineering"
pa_maturity: ML3
pro_type: mainstream
follows:
  - "[[PRO-CMMI-02-01_프로젝트_계획_절차]]"
precedes:
  - "[[PRO-CMMI-02-03_요구사항_관리_절차]]"
  - "[[PRO-CMMI-03-02_기술_솔루션_설계_절차]]"
wi_sequence:
  - wi_id: WI-CMMI-03-01-01
    title: "고객 요구사항 도출 (SG1: SP1.1~1.2)"
    mandatory: true
    entry_condition: null
  - wi_id: WI-CMMI-03-01-02
    title: "제품·인터페이스 요구사항 수립·할당 (SG2: SP2.1~2.3)"
    mandatory: true
    entry_condition: "WI-CMMI-03-01-01.status == done"
  - wi_id: WI-CMMI-03-01-03
    title: "운영 개념·기능·품질 정의 (SG3: SP3.1~3.3)"
    mandatory: true
    entry_condition: "WI-CMMI-03-01-02.status == done"
  - wi_id: WI-CMMI-03-01-04
    title: "균형 분석·요구사항 확인 (SG3: SP3.4~3.5)"
    mandatory: true
    entry_condition: "WI-CMMI-03-01-03.status == done"
created: 2026-05-11
updated: 2026-05-11
retention: "상시"
tags: [PRO, CMMI, RD, Engineering, ML3]
related:
  - "[[POL-CMMI-03_엔지니어링_정책]]"
---

# 요구사항 개발 절차 (PRO-CMMI-03-01)

상위 정책: [[POL-CMMI-03_엔지니어링_정책]] · 표준: CMMI-DEV V1.3 RD

## 1. 목적
이해관계자 니즈를 도출·우선순위화하여 고객 요구사항을 정의하고, 이를 제품·컴포넌트·인터페이스 요구사항으로 확장·할당하며, 운영 개념·기능·품질 속성을 분석하고 균형을 맞춰 요구사항을 확인한다.

## 2. 적용 범위
모든 신규 개발 및 주요 기능 추가 프로젝트의 요구사항 정의 단계. 후속 산출물은 [[PRO-CMMI-02-03_요구사항_관리_절차]] (REQM) 및 [[PRO-CMMI-03-02_기술_솔루션_설계_절차]] (TS) 로 인계.

## 3. 정의
- **Customer Requirements** (SG1): 고객 관점 요구사항.
- **Product / Product Component Requirements** (SG2): 도출된 제품·컴포넌트 수준 요구사항.
- **Operational Concept** (SP3.1): 제품 운영 시나리오·환경·사용자 상호작용 정의.
- **Quality Attributes** (SP3.2): 비기능 요구 (성능·신뢰성·보안 등).

## 4. 역할과 책임 (RACI)
| 단계 | Requirements Engineer | Engineer/Architect | 고객 | Project Manager | VAL Lead |
|---|---|---|---|---|---|
| Elicit (SP1.1) | **R** | C | C | C | C |
| Customer Req 변환 (SP1.2) | **R** | C | C | I | C |
| Product Req 수립 (SP2.1) | **R** | C | I | I | C |
| 할당 (SP2.2) | C | **R** | I | I | C |
| Interface Req (SP2.3) | C | **R** | I | I | C |
| Op Concept/Scenario (SP3.1) | **R** | C | C | I | C |
| 기능·품질 정의 (SP3.2) | **R** | **R** | I | I | C |
| 요구사항 분석 (SP3.3) | **R** | C | I | I | C |
| 균형 분석 (SP3.4) | C | **R** | C | A | C |
| 요구사항 확인 (SP3.5) | **R** | C | C | I | **R** |

## 5. 절차 흐름

```mermaid
flowchart TD
  A[프로젝트 헌장 + 이해관계자] --> B[니즈 elicit<br/>SP1.1]
  B --> C[고객 요구사항 변환<br/>SP1.2]
  C --> D[제품 요구사항 수립<br/>SP2.1]
  D --> E[컴포넌트 요구사항 할당<br/>SP2.2]
  E --> F[인터페이스 요구사항 식별<br/>SP2.3]
  F --> G[Op Concept·시나리오<br/>SP3.1]
  G --> H[기능·품질 속성 정의<br/>SP3.2]
  H --> I[요구사항 분석<br/>SP3.3]
  I --> J[균형 분석 — 비용·일정·기술<br/>SP3.4]
  J --> K[요구사항 확인 (VAL)<br/>SP3.5]
  K --> L[REQM 인계 + TS 인계]
```

## 6. SG/SP 매핑 및 단계별 상세

| #   | SP    | 단계 | 입력 | 출력 (TMP 후보) |
|---|---|---|---|---|
| 1 | SP1.1 | Elicit needs | 이해관계자 인터뷰 | 요구 elicitation 결과 |
| 2 | SP1.2 | Customer Req 변환 | elicit 결과 | 우선순위 고객 요구사항 |
| 3 | SP2.1 | Product Req 수립 | 고객 요구사항 | 제품·제품컴포넌트 요구사항 |
| 4 | SP2.2 | 컴포넌트 할당 | 제품 요구사항 | 도출 요구사항·할당 |
| 5 | SP2.3 | Interface Req | 아키텍처 가설 | 인터페이스 요구사항 |
| 6 | SP3.1 | Op Concept·시나리오 | 고객·제품 요구사항 | Operational Concept, 시나리오·use case |
| 7 | SP3.2 | 기능·품질 속성 | Op Concept | 기능·품질속성 정의서 |
| 8 | SP3.3 | 요구사항 분석 | 정의서 | 요구사항 결함 보고 |
| 9 | SP3.4 | 균형 분석 | 분석 결과 | 균형 분석 보고 |
| 10 | SP3.5 | 요구사항 확인 (VAL) | 균형 결과 | 요구사항 검증결과 기록 |

### 6.1 SG/SP source citation
| Req-ID | Title | 출처 |
|---|---|---|
| CMMIDEV-RD-SG1-REQ-001 | Develop Customer Requirements | requirements.yaml#CMMIDEV-RD-SG1-REQ-001 (p.328) |
| CMMIDEV-RD-SP1.1-REQ-001 | Elicit Needs | requirements.yaml#CMMIDEV-RD-SP1.1-REQ-001 (p.329) |
| CMMIDEV-RD-SP1.2-REQ-001 | Transform Stakeholder Needs | requirements.yaml#CMMIDEV-RD-SP1.2-REQ-001 (p.330) |
| CMMIDEV-RD-SG2-REQ-001 | Develop Product Requirements | requirements.yaml#CMMIDEV-RD-SG2-REQ-001 (p.331) |
| CMMIDEV-RD-SP2.1~2.3-REQ-001 | Product/Allocate/Interface Req | requirements.yaml (p.331-334) |
| CMMIDEV-RD-SG3-REQ-001 | Analyze and Validate Requirements | requirements.yaml#CMMIDEV-RD-SG3-REQ-001 (p.334) |
| CMMIDEV-RD-SP3.1~3.5-REQ-001 | OpConcept/Functions/Analyze/Balance/Validate | requirements.yaml (p.335-340) |

## 7. 통제점 / KPI
| 통제점 | 지표 | 목표 | 주기 |
|---|---|---|---|
| 요구사항 결함 밀도 | 분석 시 검출 / 요구사항 수 | 추세 감소 | 마일스톤 |
| 인터페이스 누락 | PI에서 발견된 누락 인터페이스 | ≤ 2건/제품 | 프로젝트 종료 |
| 균형 분석 적용율 | 영향 큰 결정 중 분석 적용 비율 | 100% | 마일스톤 |
| VAL 확인 부적합 | VAL 결과 부적합 / 전체 | ≤ 5% | 마일스톤 |

## 8. 표준 매핑 (Traceability)
- RD SG1~SG3 → §5 흐름, §6 단계
- Engineering Flow (p.47-49): Customer→RD; PM→RD; RD→TS; VER feeds back to RD
- REQM-feeds-RD-TS (p.45) → 변경된 요구사항 본 PRO로 재유입

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-RD-SG1~SG3-REQ-001 (p.328-340)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/pa_relationships.yaml"
  locator: "engineering_process_flow (p.47-49)"
  retrieved_at: "2026-05-11"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (process-designer 생성) | - |
