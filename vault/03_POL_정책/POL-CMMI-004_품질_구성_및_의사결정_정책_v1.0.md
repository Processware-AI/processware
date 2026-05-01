---
type: POL
doc_id: "POL-CMMI-004"
title: "품질·구성·의사결정 정책"
version: "1.0"
owner: "QA Manager"
reviewer: "Process Control Board (PCB)"
approver: "CEO"
scope: "프로세스 품질보증, 형상관리, 근본원인분석, 의사결정분석을 포함한 품질·통제 활동 일체"
child_pro:
  - "[[PRO-CMMI-401_프로세스_품질보증_절차_v1.0]]"
  - "[[PRO-CMMI-402_형상관리_절차_v1.0]]"
  - "[[PRO-CMMI-403_근본원인분석_및_해결_절차_v1.0]]"
  - "[[PRO-CMMI-404_의사결정_분석_및_해결_절차_v1.0]]"
standards: ["CMMI-DEV-ML3"]
scope_code: "CMMI"
tier: "S"
layer: "L2_engineering"
integration_mode: "interface_only"
status: approved
created: 2026-04-29
updated: 2026-04-29
retention: "상시"
tags: [POL, CMMI, quality, configuration, decision]
---

# 품질·구성·의사결정 정책 (POL-CMMI-004)

> 상위 기준: [[표준프로세스_구성원칙]] · 상위 정책: [[POL-CMMI-001_거버넌스_및_프로세스자산_정책_v1.0]]

## 1. 목적
본 정책은 CMMI-DEV ML3 의 **프로세스 품질보증(PQA)·구성관리(CM)·근본원인분석(CAR)·의사결정 분석(DAR)** Practice Area 가 요구하는 통제·품질 보장 체계를 정의한다. 모든 작업산출물의 무결성을 형상관리로 보장하고, 부적합·이슈를 객관적으로 평가·근본 해결하며, 중대 결정을 구조화된 분석으로 내리도록 한다.

## 2. 적용 범위
- 8종 문서(POL/PRO/WI/TMP/EX/REC/MAT/REF) 중 프로세스 자산
- 프로젝트가 생성·인도하는 모든 작업산출물(요구사항·설계·코드·시험·매뉴얼·릴리스 산출물)
- 형상관리 시스템(Git, 이슈트래커, 문서리포지토리)
- 의사결정 분석은 본 정책 §5 의 적용기준 충족 결정에만 강제 적용

## 3. 정책 원칙
1. **객관 평가(Objective Assurance)** — 프로세스·작업산출물 평가는 작업 수행자와 독립된 주체가 정해진 기준으로 수행한다.
2. **기준선 무결성(Baseline Integrity)** — 모든 인도 산출물은 통제된 기준선으로 식별·승인·관리되며 변경은 영향분석·승인을 거친다.
3. **추적 가능한 변경(Traceable Change)** — 모든 변경은 변경요청·승인·구현·검증의 사슬로 기록된다.
4. **근본 해결(Root-cause Resolution)** — 반복·중대 이슈는 근본원인분석을 통해 해결하고 효과를 측정한다.
5. **구조화된 결정(Structured Decision)** — 명시된 적용기준에 해당하는 결정은 대안·평가기준·평가방법을 정의하고 결과를 기록한다.

## 4. 역할과 책임
| 역할 | 책임 |
|---|---|
| **CEO** | 정책·CCB 거버넌스 승인, 중대 부적합 의사결정 |
| **QA Manager (Process Owner)** | PQA·CAR 운영, 부적합 추적, 품질 KPI 관리 |
| **Configuration Manager** | 형상항목(CI) 정의, 기준선·릴리스 통제, CM 시스템 운영 |
| **Change Control Board (CCB)** | 변경요청 심의·승인 |
| **PM / 작업 책임자** | 자기 산출물의 품질 자체점검, 부적합 시정조치 수행 |
| **결정자(Decision Authority)** | DAR 적용 결정 시 평가 결과에 기반한 선택 |

## 5. 준수 기준
- 프로젝트 종료 시까지 PQA 감사 결과는 [[MAT-005_심사증적_인덱스_v1.0]] 에 등재
- 형상항목(CI)은 착수 시점에 식별·기준선화하고 모든 변경은 CCB 승인
- 부적합 종결까지 [[PRO-CMMI-401_프로세스_품질보증_절차_v1.0]] 의 추적 의무
- DAR 적용기준 (예: 비용 임계 초과·기술 리스크 高·인터페이스 영향 多) 충족 결정은 의사결정평가서 작성
- 반복 부적합·중대 결과는 CAR 발의

## 6. 관련 하위 절차 (PRO)
- [[PRO-CMMI-401_프로세스_품질보증_절차_v1.0]] — PQA PA
- [[PRO-CMMI-402_형상관리_절차_v1.0]] — CM PA
- [[PRO-CMMI-403_근본원인분석_및_해결_절차_v1.0]] — CAR PA
- [[PRO-CMMI-404_의사결정_분석_및_해결_절차_v1.0]] — DAR PA

## 7. 표준 매핑 (Traceability)
| Practice | Req-ID | 반영 |
|---|---|---|
| PQA 1.1, 2.1~2.4 | CMMI-PQA-1.1, 2.1~2.4 | §3 원칙 1, §6 PRO-401 |
| CM 1.1, 2.1~2.6 | CMMI-CM-1.1, 2.1~2.6 | §3 원칙 2~3, §6 PRO-402 |
| CAR 1.1, 2.1~2.3, 3.1~3.2 | CMMI-CAR-1.1, 2.1~2.3, 3.1~3.2 | §3 원칙 4, §6 PRO-403 |
| DAR 1.1~1.2, 2.1~2.6 | CMMI-DAR-1.1~1.2, 2.1~2.6 | §3 원칙 5, §5 적용기준, §6 PRO-404 |

## 8. 출처 (source_citation)
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/PQA.pdf"
  locator: "Process Quality Assurance PG1~PG2"
  retrieved_at: "2026-04-29"
  license: "ISACA copyright — paraphrase only"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/CM.pdf"
  locator: "Configuration Management PG1~PG2 (직접 Read 확인)"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/CAR.pdf"
  locator: "Causal Analysis & Resolution PG1~PG3"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/DAR.pdf"
  locator: "Decision Analysis & Resolution PG1~PG2"
  paraphrase_only: true
```

## 9. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 1.0 | 2026-04-29 | 최초 승인 (CMMI-DEV-ML3 편입) | CEO |
