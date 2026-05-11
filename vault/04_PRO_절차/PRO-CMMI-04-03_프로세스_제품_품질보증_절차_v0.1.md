---
type: PRO
doc_id: PRO-CMMI-04-03
title: "프로세스·제품 품질보증 절차"
version: "0.1"
status: draft
owner: "QA Lead (PPQA)"
reviewer: "QA Director"
approver: "CEO/CTO"
scope_code: CMMI
scope: "프로세스·산출물 객관적 평가 → 부적합 의사소통·해결·기록"
parent_pol: "[[POL-CMMI-04_지원_품질보증_정책]]"
standards: [CMMI-DEV-ML3-V1.3]
standards_meta:
  publisher: "Software Engineering Institute (CMU/SEI)"
  year: 2010
  license: "internal_use_derivative_work"
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_acronym: PPQA
pa_full_name: "Process and Product Quality Assurance"
pa_category: "Support"
pa_maturity: ML2
pro_type: support
follows: []
precedes: []
wi_sequence:
  - wi_id: WI-CMMI-04-03-01
    title: "프로세스·산출물 객관적 평가 (SG1: SP1.1~1.2)"
    mandatory: true
    entry_condition: null
  - wi_id: WI-CMMI-04-03-02
    title: "부적합 의사소통·해결·기록 (SG2: SP2.1~2.2)"
    mandatory: true
    entry_condition: "WI-CMMI-04-03-01.status == done"
created: 2026-05-11
updated: 2026-05-11
retention: "상시"
tags: [PRO, CMMI, PPQA, Support, ML2]
related:
  - "[[POL-CMMI-04_지원_품질보증_정책]]"
---

# 프로세스·제품 품질보증 절차 (PRO-CMMI-04-03)

상위 정책: [[POL-CMMI-04_지원_품질보증_정책]] · 표준: CMMI-DEV V1.3 PPQA

## 1. 목적
프로세스 수행과 산출물에 대해 정의된 기준 대비 객관적 준수 평가를 수행하고, 부적합을 의사소통·해결·기록하여 객관적 통찰을 경영진과 프로젝트에 제공한다. 전 PA에 객관적 평가 지원 (PPQA-supports-all).

## 2. 적용 범위
조직의 모든 PA·프로젝트·산출물. 평가자는 평가 대상의 작성·실행자가 아니어야 한다(객관성).

## 3. 정의
- **Objectively Evaluate** (SG1): 정의된 기준에 따라 편향 없이 평가.
- **Noncompliance Issue**: 합의된 프로세스·표준에서 벗어난 사례.
- **Escalation**: 부적합 미해결 시 상위 보고 경로.

## 4. 역할과 책임 (RACI)
| 단계 | QA Engineer (PPQA) | Process Owner | Project Manager | Senior Mgmt |
|---|---|---|---|---|
| 프로세스 평가 (SP1.1) | **R** | C | C | A |
| 산출물 평가 (SP1.2) | **R** | C | C | A |
| 부적합 의사소통·해결 (SP2.1) | **R** | **R** (시정) | C | C (escalation) |
| 기록 (SP2.2) | **R** | I | I | I |

## 5. 절차 흐름

```mermaid
flowchart TD
  A[평가 계획] --> B[프로세스 객관적 평가<br/>SP1.1]
  A --> C[산출물 객관적 평가<br/>SP1.2]
  B --> D{부적합?}
  C --> D
  D -->|No| E[적합 기록]
  D -->|Yes| F[부적합 의사소통<br/>SP2.1]
  F --> G[Process Owner 시정 계획]
  G --> H{종결?}
  H -->|No (기한 초과)| I[Senior Mgmt 에스컬레이션]
  H -->|Yes| J[기록 작성<br/>SP2.2]
  E --> J
  I --> J
```

## 6. SG/SP 매핑 및 단계별 상세

| #   | SP    | 단계 | 입력 | 출력 (TMP 후보) |
|---|---|---|---|---|
| 1 | SP1.1 | 프로세스 객관적 평가 | 평가 계획, 정의된 프로세스 | 프로세스 평가보고서 |
| 2 | SP1.2 | 산출물 객관적 평가 | 산출물, 기준 | 부적합 보고서 |
| 3 | SP2.1 | 부적합 의사소통·해결 | 부적합 보고 | QA 시정조치 보고서 |
| 4 | SP2.2 | 기록 | 평가·시정 결과 | 품질 트렌드 보고서, 평가로그 |

### 6.1 SG/SP source citation
| Req-ID | Title | 출처 |
|---|---|---|
| CMMIDEV-PPQA-SG1-REQ-001 | Objectively Evaluate Processes and Work Products | requirements.yaml#CMMIDEV-PPQA-SG1-REQ-001 (p.303) |
| CMMIDEV-PPQA-SP1.1-REQ-001 | Objectively Evaluate Processes | requirements.yaml#CMMIDEV-PPQA-SP1.1-REQ-001 (p.303) |
| CMMIDEV-PPQA-SP1.2-REQ-001 | Objectively Evaluate Work Products | requirements.yaml#CMMIDEV-PPQA-SP1.2-REQ-001 (p.304) |
| CMMIDEV-PPQA-SG2-REQ-001 | Provide Objective Insight | requirements.yaml#CMMIDEV-PPQA-SG2-REQ-001 (p.305) |
| CMMIDEV-PPQA-SP2.1-REQ-001 | Communicate and Resolve Noncompliance Issues | requirements.yaml#CMMIDEV-PPQA-SP2.1-REQ-001 (p.305) |
| CMMIDEV-PPQA-SP2.2-REQ-001 | Establish Records | requirements.yaml#CMMIDEV-PPQA-SP2.2-REQ-001 (p.306) |

## 7. 통제점 / KPI
| 통제점 | 지표 | 목표 | 주기 |
|---|---|---|---|
| 평가 수행율 | 계획 평가 vs 실시 | ≥ 95% | 분기 |
| 부적합 종결 리드타임 | 식별→종결 | ≤ 30일 | 월 |
| 미해결 부적합 | 30일 이상 미종결 | 0건 | 월 |
| 에스컬레이션 비율 | 에스컬레이션 / 부적합 | ≤ 10% | 분기 |

## 8. 표준 매핑 (Traceability)
- PPQA SG1~SG2 → §5 흐름, §6 단계
- PPQA-supports-all (p.51) → 본 PRO는 전 PA의 객관적 평가 지원
- GP 2.9 (Evaluate Adherence) → 본 PRO와 연계

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-PPQA-SG1~SG2-REQ-001 (p.303-306)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/pa_relationships.yaml"
  locator: "PPQA-supports-all (p.51)"
  retrieved_at: "2026-05-11"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (process-designer 생성) | - |
