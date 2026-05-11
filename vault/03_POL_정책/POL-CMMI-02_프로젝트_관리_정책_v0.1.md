---
type: POL
doc_id: POL-CMMI-02
title: "프로젝트 관리 정책"
version: "0.1"
status: draft
owner: "PMO Director"
reviewer: "Senior Management Steering Group"
approver: "CEO/CTO"
scope_code: CMMI
scope: "프로젝트 계획·모니터링·요구사항 관리·공급자 협약·통합 PM·리스크 관리"
standards: [CMMI-DEV-ML3-V1.3]
standards_meta:
  publisher: "Software Engineering Institute (CMU/SEI)"
  year: 2010
  publication_report: "CMU/SEI-2010-TR-033"
  license: "internal_use_derivative_work"
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_coverage: [PP, PMC, REQM, SAM, IPM, RSKM]
category: "Project Management"
child_pro:
  - "[[PRO-CMMI-02-01_프로젝트_계획_절차]]"
  - "[[PRO-CMMI-02-02_프로젝트_모니터링_통제_절차]]"
  - "[[PRO-CMMI-02-03_요구사항_관리_절차]]"
  - "[[PRO-CMMI-02-04_공급자_협약_관리_절차]]"
  - "[[PRO-CMMI-02-05_통합_프로젝트_관리_절차]]"
  - "[[PRO-CMMI-02-06_리스크_관리_절차]]"
created: 2026-05-11
updated: 2026-05-11
retention: "상시"
tags: [POL, CMMI, Project-Management, PP, PMC, REQM, SAM, IPM, RSKM]
related:
  - "[[적용요건]]"
  - "[[POL-CMMI-01_조직_프로세스_거버넌스_정책]]"
---

# 프로젝트 관리 정책 (POL-CMMI-02)

## 1. 목적
본 정책은 CMMI-DEV-ML3 Project Management 카테고리(Basic: PP, PMC, REQM, SAM / Advanced: IPM, RSKM)의 요구를 충족하기 위해, 모든 개발 프로젝트가 **계획·모니터링·약정·리스크·공급자·통합**의 통제된 프로젝트 운영을 수행하도록 방향을 정의한다.

## 2. 적용 범위
조직이 수행하는 모든 개발 프로젝트(자체·외주 포함)에 적용한다. 비개발성 운영 업무는 제외한다.

## 3. 정의
- **Project Plan**: PP가 산출하는 통합 프로젝트 계획서(WBS+일정+예산+리스크+자원+이해관계자+데이터관리 통합).
- **Defined Process** (프로젝트 정의 프로세스): OSSP를 [[PRO-CMMI-01-01_조직_표준프로세스_수립_유지_절차]] 의 테일러링 가이드에 따라 프로젝트가 정의한 프로세스 (IPM SP1.1).
- **Commitment**: 프로젝트 약정 — 관련 이해관계자가 일정·산출·자원에 동의한 약속 (PP SP3.3).

## 4. 역할과 책임 (RACI 요지)
| 역할 | 책임 |
|---|---|
| **CEO/CTO** | 정책 승인, 중요 프로젝트 약정 승인, 리스크 임계치 결정 |
| **PMO Director** | 본 정책 유지, 프로젝트 포트폴리오 검토 |
| **Project Manager** | PP/PMC/REQM/SAM/IPM/RSKM 전반 실행 책임 |
| **EPG Lead** | OSSP 테일러링 가이드 제공 (IPM SP1.1) |
| **Risk Manager** | 조직 리스크 관리 전략, 임계치 모니터링 (RSKM 협업) |
| **Procurement Lead** | SAM SG1~SG2 실행 책임 |

## 5. 정책 원칙
1. **계획 우선** — 모든 프로젝트는 착수 전 PP SG1~SG3의 추정·계획·약정 단계를 완료하고, 그 산출물(통합 프로젝트 계획서)을 PMC의 베이스라인으로 사용한다 (PP-baseline-for-PMC).
2. **요구사항 변경의 통제된 전파** — REQM SP1.3의 요구사항 변경은 영향평가 후 RD/TS/PI/계획에 통제된 방식으로 전파한다 (REQM-feeds-RD-TS).
3. **약정 기반 모니터링** — PMC SG1은 약정·계획 베이스라인 대비 실제 성과·리스크·약정·데이터관리·이해관계자 참여·진행·마일스톤을 정기적으로 평가한다.
4. **리스크의 사전 관리** — RSKM SG1~SG3에 따라 리스크는 식별·분석 → 완화계획 → 실행 모니터링의 사전 사이클로 관리한다. 사후 대응(PMC SG2 시정조치)으로만 다루지 않는다.
5. **공급자 통제** — SAM SG1~SG2에 따라 외주는 공식 협약·인수·전이를 거치며, 협약 후 진행은 PMC 베이스라인에 통합 추적한다.
6. **OSSP 테일러링** — 모든 프로젝트는 IPM SP1.1에 따라 OSSP를 테일러링한 정의된 프로세스를 보유한다 (GP 3.1).

## 6. 준수 기준
- 모든 프로젝트는 PP 산출 통합 계획서 + IPM 정의 프로세스 + RSKM 리스크 관리 전략을 착수 단계 게이트로 충족해야 한다.
- 요구사항 RTM(REQM SP1.4) 양방향 추적성 100% 유지.
- 리스크 high 이상은 주간, medium 이하는 월간 검토.
- 공급자 협약(SAM SP1.3)은 법무·재무 검토 필수.

## 7. 관련 하위 절차 (PRO)
- [[PRO-CMMI-02-01_프로젝트_계획_절차]] — PP
- [[PRO-CMMI-02-02_프로젝트_모니터링_통제_절차]] — PMC
- [[PRO-CMMI-02-03_요구사항_관리_절차]] — REQM
- [[PRO-CMMI-02-04_공급자_협약_관리_절차]] — SAM
- [[PRO-CMMI-02-05_통합_프로젝트_관리_절차]] — IPM
- [[PRO-CMMI-02-06_리스크_관리_절차]] — RSKM

## 8. 표준 매핑 (Traceability)
| CMMI 조항 | Req-ID | 반영 |
|---|---|---|
| PP SG1~SG3 | CMMIDEV-PP-SG1~SG3-REQ-001 | §5-1, §7 PRO-CMMI-02-01 |
| PMC SG1~SG2 | CMMIDEV-PMC-SG1~SG2-REQ-001 | §5-3, §7 PRO-CMMI-02-02 |
| REQM SG1 | CMMIDEV-REQM-SG1-REQ-001 | §5-2, §7 PRO-CMMI-02-03 |
| SAM SG1~SG2 | CMMIDEV-SAM-SG1~SG2-REQ-001 | §5-5, §7 PRO-CMMI-02-04 |
| IPM SG1~SG2 | CMMIDEV-IPM-SG1~SG2-REQ-001 | §5-6, §7 PRO-CMMI-02-05 |
| RSKM SG1~SG3 | CMMIDEV-RSKM-SG2~SG3-REQ-001 + SP1.1~1.3 | §5-4, §7 PRO-CMMI-02-06 |
| Cross-cutting | pa_relationships.yaml — PP-baseline-for-PMC, REQM-feeds-RD-TS, BPM-enables-APM | §5 정책 원칙 전반 |

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-PP-SG1~SG3 (p.283-298)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-PMC-SG1~SG2 (p.272-279)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-REQM-SG1 (p.343-346)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-SAM-SG1~SG2 (p.365-372)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-IPM-SG1~SG2 (p.159-173)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-RSKM-SP1.1~SP3.2 (p.351-360)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/pa_relationships.yaml"
  locator: "PP-baseline-for-PMC (p.44), REQM-feeds-RD-TS (p.45), BPM-enables-APM (p.45)"
  retrieved_at: "2026-05-11"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (process-designer 생성) | - |
