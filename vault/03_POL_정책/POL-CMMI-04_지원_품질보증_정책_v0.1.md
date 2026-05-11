---
type: POL
doc_id: POL-CMMI-04
title: "지원 및 품질보증 정책"
version: "0.1"
status: draft
owner: "QA Director"
reviewer: "Senior Management Steering Group"
approver: "CEO/CTO"
scope_code: CMMI
scope: "형상 관리·측정 및 분석·프로세스/제품 품질보증·의사결정 분석"
standards: [CMMI-DEV-ML3-V1.3]
standards_meta:
  publisher: "Software Engineering Institute (CMU/SEI)"
  year: 2010
  publication_report: "CMU/SEI-2010-TR-033"
  license: "internal_use_derivative_work"
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_coverage: [CM, MA, PPQA, DAR]
category: "Support"
child_pro:
  - "[[PRO-CMMI-04-01_형상_관리_절차]]"
  - "[[PRO-CMMI-04-02_측정_및_분석_절차]]"
  - "[[PRO-CMMI-04-03_프로세스_제품_품질보증_절차]]"
  - "[[PRO-CMMI-04-04_의사결정_분석_결정_절차]]"
created: 2026-05-11
updated: 2026-05-11
retention: "상시"
tags: [POL, CMMI, Support, CM, MA, PPQA, DAR]
related:
  - "[[적용요건]]"
  - "[[POL-CMMI-01_조직_프로세스_거버넌스_정책]]"
  - "[[POL-CMMI-02_프로젝트_관리_정책]]"
  - "[[POL-CMMI-03_엔지니어링_정책]]"
---

# 지원 및 품질보증 정책 (POL-CMMI-04)

## 1. 목적
본 정책은 CMMI-DEV-ML3 Support 카테고리(CM, MA, PPQA, DAR)의 요구를 충족하기 위해, 전 프로세스 영역(PA)을 횡단하여 **형상 무결성·측정 정보·객관적 평가·형식적 의사결정**을 제공하는 지원 활동의 방향을 정의한다.

## 2. 적용 범위
조직의 모든 프로세스 영역(Process Management/Project Management/Engineering)에 횡단 적용된다. CM은 전 PA의 work product 무결성을, MA는 측정정보를, PPQA는 객관적 평가를, DAR은 의사결정 형식화를 지원한다.

## 3. 정의
- **Configuration Item (CI)**: CM 통제 대상 산출물 단위.
- **Baseline**: 합의된 CI 집합 — 변경은 CCB 승인 후에만 가능.
- **CCB** (Configuration Control Board): 형상통제위원회.
- **Measurement Objective**: MA SP1.1이 정의하는, 측정의 목적·정보 니즈.
- **Noncompliance Issue**: PPQA가 식별한, 합의된 프로세스·표준에서 벗어난 사례.
- **Formal Evaluation Process**: DAR이 적용하는 가중·평가기준 기반 의사결정 프로세스.

## 4. 역할과 책임 (RACI 요지)
| 역할 | 책임 |
|---|---|
| **CEO/CTO** | 정책 승인, DAR 적용 기준 승인, 중대 부적합 시정 승인 |
| **QA Director** | 본 정책 유지, PPQA 독립성 보장, 시정 미해결 사항을 상위 보고 |
| **Configuration Manager** | CM 전체 운영, CCB 운영, 형상감사 |
| **Measurement Analyst** | MA SG1~SG2 실행, 조직 측정저장소 데이터 품질 |
| **QA Engineer (PPQA)** | 프로세스·산출물 객관적 평가, 부적합 보고 |
| **Decision Owner (per 결정)** | DAR 트리거 식별 + 형식 평가 적용 |

## 5. 정책 원칙
1. **무결성 보장 (CM)** — 모든 베이스라인·CI는 식별·통제·기록·감사된다 (CM SG1~SG3). 통제되지 않은 변경은 즉시 부적합으로 처리한다 (CM-supports-all).
2. **객관성 (PPQA)** — PPQA 평가자는 평가 대상 프로세스·산출물의 작성·실행자가 아니어야 하며, 평가 결과는 경영진에게 직접 보고 채널을 가진다 (PPQA SG1).
3. **데이터 기반 (MA)** — 모든 측정은 명시적 측정목적(MA SP1.1)에서 도출되며, 측정 결과는 의사결정과 환류된다 (MA-supports-all).
4. **형식적 의사결정 (DAR)** — 영향 큰 의사결정(고비용·비가역·이해관계자 다양·고리스크)은 DAR SP1.1의 지침에 따라 형식적 평가 프로세스를 적용한다 (DAR-supports-all).
5. **부적합 종결까지 추적** — PPQA가 식별한 부적합은 시정조치 종결까지 추적·보고한다 (PPQA SG2 + PMC SG2 연계).

## 6. 준수 기준
- CM 베이스라인 외 임의 변경 0건 (분기 점검).
- PPQA 평가 주기: 프로세스 월 1회 / 주요 산출물 마일스톤별.
- MA 측정 보고 주기: 프로젝트 월간 / 조직 분기.
- DAR 형식 평가 적용 기준은 [[PRO-CMMI-04-04_의사결정_분석_결정_절차]] SP1.1에 따른다.

## 7. 관련 하위 절차 (PRO)
- [[PRO-CMMI-04-01_형상_관리_절차]] — CM
- [[PRO-CMMI-04-02_측정_및_분석_절차]] — MA
- [[PRO-CMMI-04-03_프로세스_제품_품질보증_절차]] — PPQA
- [[PRO-CMMI-04-04_의사결정_분석_결정_절차]] — DAR

## 8. 표준 매핑 (Traceability)
| CMMI 조항 | Req-ID | 반영 |
|---|---|---|
| CM SG1~SG3 | CMMIDEV-CM-SG1~SG3-REQ-001 | §5-1, §7 PRO-CMMI-04-01 |
| MA SG1~SG2 | CMMIDEV-MA-SG1~SG2-REQ-001 | §5-3, §7 PRO-CMMI-04-02 |
| PPQA SG1~SG2 | CMMIDEV-PPQA-SG1~SG2-REQ-001 | §5-2,5, §7 PRO-CMMI-04-03 |
| DAR SG1 | CMMIDEV-DAR-SG1-REQ-001 | §5-4, §7 PRO-CMMI-04-04 |
| GP 2.6 (CM 연계) | CMMIDEV-GP2.6-REQ-001 | §5-1 무결성 보장 |
| GP 2.8 (모니터링) | CMMIDEV-GP2.8-REQ-001 | §5-3 데이터 기반 |
| GP 2.9 (PPQA 연계) | CMMIDEV-GP2.9-REQ-001 | §5-2 객관성 |
| Cross-cutting | CM/MA/PPQA/DAR-supports-all (p.51-53) | §2 횡단 적용 |

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-CM-SG1~SG3 (p.140-146)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-MA-SG1~SG2 (p.177-189)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-PPQA-SG1~SG2 (p.303-306)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-DAR-SG1 (p.151-156)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/pa_relationships.yaml"
  locator: "CM/MA/PPQA/DAR-supports-all (p.51-53)"
  retrieved_at: "2026-05-11"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (process-designer 생성) | - |
