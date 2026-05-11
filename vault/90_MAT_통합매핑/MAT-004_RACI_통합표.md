---
type: MAT
doc_id: MAT-004
title: RACI 통합표
version: "0.2"
owner: "QMR"
status: draft
created: 2026-04-16
updated: 2026-05-11
retention: "상시"
tags: [MAT, raci]
---

# MAT-004 RACI 통합표

> 전사 PRO 별 책임 분담을 단일 표로 집계. 역할 중복·공백 탐지용.

## 역할 리스트
- 경영진(CEO/CISO/CPO 등)
- 프로세스 오너
- 담당자
- 내부심사팀
- 외부 이해관계자

## RACI 매트릭스

| PRO | 활동 | CEO | 경영진 | PCB | SEPG | PO | 담당 | QA |
|---|---|---|---|---|---|---|---|---|

## §CMMI-DEV-ML3-V1.3 (편입: 2026-05-11)

> 18 PRO 의 frontmatter `owner` / `reviewer` / `approver` 에서 추출. CMMI 역할(EPG/PMO/QA 등)과 본 표의 일반 역할(SEPG/PO 등)을 매핑한 18행.

| PRO ID | 활동(PA) | Owner (R) | Reviewer (C) | Approver (A) | 비고 |
|---|---|---|---|---|---|
| [[PRO-CMMI-01-01_조직_표준프로세스_수립_유지_절차]] | OPD — OSSP 수립·유지 | EPG Lead | Senior Management Steering Group | CEO/CTO | Process Mgmt 카테고리 |
| [[PRO-CMMI-01-02_조직_프로세스_개선_배포_절차]] | OPF — 프로세스 개선·배포 | EPG Lead | Senior Management Steering Group | CEO/CTO | Process Mgmt 카테고리 |
| [[PRO-CMMI-01-03_조직_훈련_절차]] | OT — 조직 훈련 | Training Manager | EPG Lead | CEO/CTO | Process Mgmt 카테고리 |
| [[PRO-CMMI-02-01_프로젝트_계획_절차]] | PP — 프로젝트 계획 | PMO Director | Senior Management Steering Group | CEO/CTO | Project Mgmt 카테고리 |
| [[PRO-CMMI-02-02_프로젝트_모니터링_통제_절차]] | PMC — 모니터링·통제 | Project Manager | PMO Director | CEO/CTO | Project Mgmt 카테고리 |
| [[PRO-CMMI-02-03_요구사항_관리_절차]] | REQM — 요구사항 관리 | Requirements Engineer Lead | Project Manager | PMO Director | Project Mgmt 카테고리 |
| [[PRO-CMMI-02-04_공급자_협약_관리_절차]] | SAM — 공급자 협약 | Procurement Lead | Project Manager | PMO Director | Project Mgmt 카테고리 |
| [[PRO-CMMI-02-05_통합_프로젝트_관리_절차]] | IPM — 통합 프로젝트 관리 | Project Manager | EPG Lead | PMO Director | Project Mgmt 카테고리 |
| [[PRO-CMMI-02-06_리스크_관리_절차]] | RSKM — 리스크 관리 | Risk Manager | Project Manager | PMO Director | Project Mgmt 카테고리 |
| [[PRO-CMMI-03-01_요구사항_개발_절차]] | RD — 요구사항 개발 | Requirements Engineer Lead | Chief Engineer | Project Manager | Engineering 카테고리 |
| [[PRO-CMMI-03-02_기술_솔루션_설계_절차]] | TS — 기술 솔루션 | Chief Engineer / Lead Architect | Engineering Director | Project Manager | Engineering 카테고리 |
| [[PRO-CMMI-03-03_제품_통합_절차]] | PI — 제품 통합 | Integration Lead | Chief Engineer | Project Manager | Engineering 카테고리 |
| [[PRO-CMMI-03-04_검증_절차]] | VER — 검증 | Test/Verification Lead | Chief Engineer | Project Manager | Engineering 카테고리 |
| [[PRO-CMMI-03-05_확인_절차]] | VAL — 확인 | Validation Lead | Chief Engineer | Project Manager | Engineering 카테고리 |
| [[PRO-CMMI-04-01_형상_관리_절차]] | CM — 형상 관리 | Configuration Manager | QA Director | CEO/CTO | Support 카테고리 |
| [[PRO-CMMI-04-02_측정_및_분석_절차]] | MA — 측정·분석 | Measurement Analyst | QA Director | CEO/CTO | Support 카테고리 |
| [[PRO-CMMI-04-03_프로세스_제품_품질보증_절차]] | PPQA — 품질보증 | QA Lead (PPQA) | QA Director | CEO/CTO | Support 카테고리 |
| [[PRO-CMMI-04-04_의사결정_분석_결정_절차]] | DAR — 의사결정 | EPG Lead / Decision Facilitator | QA Director | CEO/CTO | Support 카테고리 |

### Accountable 분포 (CMMI 18 PRO)

| Approver | PRO 수 | PRO 목록 |
|---|---|---|
| CEO/CTO | 11 | OPD, OPF, OT, PP, PMC, CM, MA, PPQA, DAR |
| PMO Director | 4 | REQM, SAM, IPM, RSKM |
| Project Manager | 5 | RD, TS, PI, VER, VAL |

> Accountable 중복·누락 0건 — 모든 18 PRO 가 단일 approver 지정. (지원 출처: 각 PRO frontmatter)

## 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.2 | 2026-05-11 | CMMI-DEV-ML3-V1.3 18 PRO RACI 행 추가 (Process/Project/Engineering/Support 4 카테고리) — Phase 4 Trace, traceability-mapper | - |
