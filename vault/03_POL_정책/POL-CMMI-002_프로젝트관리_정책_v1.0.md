---
type: POL
doc_id: "POL-CMMI-002"
title: "프로젝트관리 정책"
version: "1.0"
owner: "PMO Lead"
reviewer: "Process Control Board (PCB)"
approver: "CEO"
scope: "전사 모든 개발 프로젝트의 계획·추정·모니터·통제·성과·리스크 관리"
child_pro:
  - "[[PRO-CMMI-201_프로젝트_계획_절차_v1.0]]"
  - "[[PRO-CMMI-202_프로젝트_모니터링_및_통제_절차_v1.0]]"
  - "[[PRO-CMMI-203_추정_관리_절차_v1.0]]"
  - "[[PRO-CMMI-204_성과_및_측정_관리_절차_v1.0]]"
  - "[[PRO-CMMI-205_리스크_및_기회_관리_절차_v1.0]]"
standards: ["CMMI-DEV-ML3"]
scope_code: "CMMI"
tier: "C"
layer: "L2_engineering"
integration_mode: "interface_only"
status: approved
created: 2026-04-29
updated: 2026-04-29
retention: "상시"
tags: [POL, CMMI, project-management]
---

# 프로젝트관리 정책 (POL-CMMI-002)

> 상위 기준: [[표준프로세스_구성원칙]] · 상위 정책: [[POL-CMMI-001_거버넌스_및_프로세스자산_정책_v1.0]]

## 1. 목적
본 정책은 CMMI-DEV ML3 의 **계획수립(PLAN)·모니터·통제(MC)·추정(EST)·성과·측정관리(MPM)·리스크·기회 관리(RSK)** Practice Area 요구사항을 충족하기 위한 전사 프로젝트관리 방향과 책임을 정의한다. 모든 개발 프로젝트가 사실(추정·측정)에 기반해 계획되고, 성과·리스크가 가시화·통제됨을 보장한다.

## 2. 적용 범위
- 사외 인도형 SI/SM 프로젝트, 사내 제품개발 프로젝트, R&D 프로젝트
- 외주·공동개발 프로젝트는 인수자 측 책임 범위에 적용 (공급자 본인 활동은 POL-CMMI-005 참조)
- 1인 1주 미만의 단순 작업·연구 탐색은 테일러링 후 적용 가능

## 3. 정책 원칙
1. **사실 기반 계획(Fact-based)** — 모든 프로젝트는 작업·산출물 규모·작업량·자원·일정의 추정 근거를 기록·유지하고 이를 계획에 반영한다.
2. **명시된 약속(Committed Plan)** — 계획은 영향받는 이해관계자의 검토·약속을 거쳐 승인되며, 미승인 계획에는 자원을 투입하지 않는다.
3. **상시 가시성(Visibility)** — 진척·자원·이슈·리스크·성과 데이터는 정해진 주기로 측정·보고되어 의사결정 가능 상태를 유지한다.
4. **편차 시정(Variance Closure)** — 실적이 계획에서 유의하게 벗어날 때 시정조치를 즉시 발의하고 종결까지 추적한다.
5. **리스크·기회 능동관리(Active Risk & Opportunity)** — 위협뿐 아니라 기회를 함께 식별·평가·대응하여 가치 창출을 극대화한다.

## 4. 역할과 책임
| 역할 | 책임 |
|---|---|
| **CEO / 임원** | 프로젝트 헌장·예산·핵심 위험 승인 |
| **PMO** | 추정·계획·MPM·리스크 표준 운영, 포트폴리오 가시화 |
| **프로젝트관리자(PM)** | 계획 수립·승인·갱신, 진척·성과·리스크 보고, 시정조치 발의 |
| **PM Office Reviewer** | 계획 검토, 추정 근거 검증, 게이트 점검 |
| **SEPG** | 추정·측정 모델·리스크 분류 등 OSSP 자산 제공 |
| **이해관계자(고객·영업·운영)** | 약속 검토·승인, 계획 변경 협의 |

## 5. 준수 기준
- 모든 프로젝트는 착수 시 [[PRO-CMMI-201_프로젝트_계획_절차_v1.0]] 에 따라 계획서를 작성·승인 받음
- 추정은 [[PRO-CMMI-203_추정_관리_절차_v1.0]] 의 모델·과거데이터(PAL) 사용을 원칙으로 함
- 진척·성과·리스크 보고 주기는 프로젝트 등급별로 [[PRO-CMMI-202_프로젝트_모니터링_및_통제_절차_v1.0]] 정의 준수
- 측정 데이터는 [[PRO-CMMI-204_성과_및_측정_관리_절차_v1.0]] 에 따라 조직 측정 저장소에 등재
- 계획 대비 일정·예산 ±10% 또는 핵심 리스크 발생 시 시정조치 절차 가동

## 6. 관련 하위 절차 (PRO)
- [[PRO-CMMI-201_프로젝트_계획_절차_v1.0]] — PLAN PA
- [[PRO-CMMI-202_프로젝트_모니터링_및_통제_절차_v1.0]] — MC PA
- [[PRO-CMMI-203_추정_관리_절차_v1.0]] — EST PA
- [[PRO-CMMI-204_성과_및_측정_관리_절차_v1.0]] — MPM PA
- [[PRO-CMMI-205_리스크_및_기회_관리_절차_v1.0]] — RSK PA

## 7. 표준 매핑 (Traceability)
| Practice | Req-ID | 반영 |
|---|---|---|
| PLAN 1.1~3.4 | CMMI-PLAN-1.1, 2.1~2.8, 3.1~3.4 | §3 원칙 1~2, §6 PRO-201 |
| MC 1.1~3.4 | CMMI-MC-1.1~1.2, 2.1~2.4, 3.1~3.4 | §3 원칙 3~4, §6 PRO-202 |
| EST 1.1~3.2 | CMMI-EST-1.1, 2.1~2.2, 3.1~3.2 | §3 원칙 1, §6 PRO-203 |
| MPM 1.1~3.6 | CMMI-MPM-1.1~1.2, 2.1~2.6, 3.1~3.6 | §3 원칙 3, §6 PRO-204 |
| RSK 1.1~3.3 | CMMI-RSK-1.1~1.2, 2.1~2.5, 3.1~3.3 | §3 원칙 5, §6 PRO-205 |

## 8. 출처 (source_citation)
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/PLAN.pdf"
  locator: "Planning PG1~PG3 Practice Statements"
  retrieved_at: "2026-04-29"
  license: "ISACA copyright — paraphrase only"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/MC.pdf"
  locator: "Monitor & Control PG1~PG3"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/EST.pdf"
  locator: "Estimating PG1~PG3"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/MPM.pdf"
  locator: "Managing Performance & Measurement PG1~PG3"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/RSK.pdf"
  locator: "Risk & Opportunity Management PG1~PG3"
  paraphrase_only: true
```

## 9. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 1.0 | 2026-04-29 | 최초 승인 (CMMI-DEV-ML3 편입) | CEO |
