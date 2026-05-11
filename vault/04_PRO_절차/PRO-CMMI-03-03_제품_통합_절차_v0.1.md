---
type: PRO
doc_id: PRO-CMMI-03-03
title: "제품 통합 절차"
version: "0.1"
status: draft
owner: "Integration Lead"
reviewer: "Chief Engineer"
approver: "Project Manager"
scope_code: CMMI
scope: "통합 전략·환경·절차 수립 → 인터페이스 호환성 → 통합·인도"
parent_pol: "[[POL-CMMI-03_엔지니어링_정책]]"
standards: [CMMI-DEV-ML3-V1.3]
standards_meta:
  publisher: "Software Engineering Institute (CMU/SEI)"
  year: 2010
  license: "internal_use_derivative_work"
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_acronym: PI
pa_full_name: "Product Integration"
pa_category: "Engineering"
pa_maturity: ML3
pro_type: mainstream
follows:
  - "[[PRO-CMMI-03-02_기술_솔루션_설계_절차]]"
precedes:
  - "[[PRO-CMMI-03-04_검증_절차]]"
  - "[[PRO-CMMI-03-05_확인_절차]]"
wi_sequence:
  - wi_id: WI-CMMI-03-03-01
    title: "통합 전략·환경·절차 수립 (SG1: SP1.1~1.3)"
    mandatory: true
    entry_condition: null
  - wi_id: WI-CMMI-03-03-02
    title: "인터페이스 완전성·관리 (SG2: SP2.1~2.2)"
    mandatory: true
    entry_condition: "WI-CMMI-03-03-01.status == done"
  - wi_id: WI-CMMI-03-03-03
    title: "컴포넌트 통합 준비·조립 (SG3: SP3.1~3.2)"
    mandatory: true
    entry_condition: "WI-CMMI-03-03-02.status == done"
  - wi_id: WI-CMMI-03-03-04
    title: "통합 평가·패키징·인도 (SG3: SP3.3~3.4)"
    mandatory: true
    entry_condition: "WI-CMMI-03-03-03.status == done"
created: 2026-05-11
updated: 2026-05-11
retention: "상시"
tags: [PRO, CMMI, PI, Engineering, ML3]
related:
  - "[[POL-CMMI-03_엔지니어링_정책]]"
---

# 제품 통합 절차 (PRO-CMMI-03-03)

상위 정책: [[POL-CMMI-03_엔지니어링_정책]] · 표준: CMMI-DEV V1.3 PI

## 1. 목적
통합 전략·환경·절차·기준을 수립하고, 인터페이스 호환성·완전성을 보장하며, 컴포넌트를 조립·평가·패키징하여 고객에게 인도한다.

## 2. 적용 범위
컴포넌트가 다수인 모든 제품의 통합 단계. 단일 컴포넌트 제품의 경우 SG2는 외부 인터페이스에 한정.

## 3. 정의
- **Integration Strategy** (SP1.1): 통합 순서·체계.
- **Integration Environment** (SP1.2): 통합·시험 환경.
- **Interface Description** (SP2.1): 컴포넌트 간 인터페이스 명세.

## 4. 역할과 책임 (RACI)
| 단계 | Integration Lead | Architect | Engineer | CM | 고객 |
|---|---|---|---|---|---|
| 전략 수립 (SP1.1) | **R** | C | C | I | I |
| 환경 수립 (SP1.2) | **R** | C | C | C | I |
| 절차·기준 (SP1.3) | **R** | C | C | I | I |
| 인터페이스 검토 (SP2.1) | **R** | C | C | I | I |
| 인터페이스 관리 (SP2.2) | **R** | C | C | C | I |
| 통합 준비 (SP3.1) | **R** | I | C | C | I |
| 조립 (SP3.2) | **R** | C | **R** | C | I |
| 평가 (SP3.3) | **R** | C | C | I | C |
| 패키징·인도 (SP3.4) | **R** | I | C | C | **A** |

## 5. 절차 흐름

```mermaid
flowchart TD
  A[설계 베이스라인 + 컴포넌트] --> B[통합 전략 수립<br/>SP1.1]
  B --> C[통합 환경 수립<br/>SP1.2]
  C --> D[통합 절차·기준<br/>SP1.3]
  D --> E[인터페이스 검토<br/>SP2.1]
  E --> F{호환?}
  F -->|No| G[Interface 변경 — TS SP2.3 회귀]
  G --> E
  F -->|Yes| H[인터페이스 관리<br/>SP2.2]
  H --> I[컴포넌트 통합 준비<br/>SP3.1]
  I --> J[컴포넌트 조립<br/>SP3.2]
  J --> K[평가<br/>SP3.3]
  K --> L{합격?}
  L -->|No| M[부적합 시정]
  M --> J
  L -->|Yes| N[패키징·인도<br/>SP3.4]
```

## 6. SG/SP 매핑 및 단계별 상세

| #   | SP    | 단계 | 입력 | 출력 (TMP 후보) |
|---|---|---|---|---|
| 1 | SP1.1 | 통합 전략 수립 | 설계 | 제품 통합 전략서 |
| 2 | SP1.2 | 통합 환경 수립 | 전략 | 통합 환경 명세 |
| 3 | SP1.3 | 통합 절차·기준 | 환경, 인터페이스 | 통합 절차·기준 |
| 4 | SP2.1 | 인터페이스 검토 | ICD (TS SP2.3) | 인터페이스 카테고리/목록/매핑 |
| 5 | SP2.2 | 인터페이스 관리 | ICD, CM | ICD 변경관리 기록 |
| 6 | SP3.1 | 통합 준비 확인 | 컴포넌트, 절차 | 인수 문서 |
| 7 | SP3.2 | 컴포넌트 조립 | 컴포넌트, 절차 | 조립 결과 |
| 8 | SP3.3 | 통합 평가 | 조립 결과, 기준 | 통합 요약 보고서 |
| 9 | SP3.4 | 패키징·인도 | 평가 통과 제품 | 패키징 명세, 인도 문서 |

### 6.1 SG/SP source citation
| Req-ID | Title | 출처 |
|---|---|---|
| CMMIDEV-PI-SG1-REQ-001 | Prepare for Product Integration | requirements.yaml#CMMIDEV-PI-SG1-REQ-001 (p.259) |
| CMMIDEV-PI-SP1.1~1.3-REQ-001 | Strategy/Environment/Procedures | requirements.yaml (p.259-262) |
| CMMIDEV-PI-SG2-REQ-001 | Ensure Interface Compatibility | requirements.yaml#CMMIDEV-PI-SG2-REQ-001 (p.263) |
| CMMIDEV-PI-SP2.1~2.2-REQ-001 | Review/Manage Interfaces | requirements.yaml (p.263-264) |
| CMMIDEV-PI-SG3-REQ-001 | Assemble Product Components and Deliver the Product | requirements.yaml#CMMIDEV-PI-SG3-REQ-001 (p.266) |
| CMMIDEV-PI-SP3.1~3.4-REQ-001 | Confirm/Assemble/Evaluate/Package | requirements.yaml (p.266-268) |

## 7. 통제점 / KPI
| 통제점 | 지표 | 목표 | 주기 |
|---|---|---|---|
| 인터페이스 부적합 | PI 발견 인터페이스 결함 | ≤ 5건/제품 | 마일스톤 |
| 통합 평가 통과율 | 1차 시도 통과 / 시도 | ≥ 80% | 통합 라운드 |
| 인도 후 결함 | 인도 후 1개월 내 결함 | ≤ 2건 | 인도 후 |
| 통합 환경 가용성 | 환경 가용 시간 / 계획 | ≥ 95% | 월 |

## 8. 표준 매핑 (Traceability)
- PI SG1~SG3 → §5 흐름, §6 단계
- Engineering Flow: TS→PI; PI→Customer
- CM-supports-all → §5 인터페이스 관리, 조립 베이스라인

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-PI-SG1~SG3-REQ-001 (p.259-268)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (process-designer 생성) | - |
