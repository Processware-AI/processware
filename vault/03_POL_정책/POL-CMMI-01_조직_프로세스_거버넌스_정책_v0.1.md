---
type: POL
doc_id: POL-CMMI-01
title: "조직 프로세스 거버넌스 정책"
version: "0.1"
status: draft
owner: "EPG Lead (Engineering Process Group)"
reviewer: "Senior Management Steering Group"
approver: "CEO/CTO"
scope_code: CMMI
scope: "조직 표준프로세스(OSSP)의 정의·유지·배포·교육 및 조직 차원의 프로세스 개선 활동"
standards: [CMMI-DEV-ML3-V1.3]
standards_meta:
  publisher: "Software Engineering Institute (CMU/SEI)"
  year: 2010
  publication_report: "CMU/SEI-2010-TR-033"
  license: "internal_use_derivative_work"
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_coverage: [OPD, OPF, OT]
category: "Process Management"
child_pro:
  - "[[PRO-CMMI-01-01_조직_표준프로세스_수립_유지_절차]]"
  - "[[PRO-CMMI-01-02_조직_프로세스_개선_배포_절차]]"
  - "[[PRO-CMMI-01-03_조직_훈련_절차]]"
created: 2026-05-11
updated: 2026-05-11
retention: "상시"
tags: [POL, CMMI, Process-Management, OPD, OPF, OT]
related:
  - "[[적용요건]]"
  - "[[07_표준분류레지스트리]]"
  - "[[MAT-002_규제요구사항_대조표]]"
---

# 조직 프로세스 거버넌스 정책 (POL-CMMI-01)

## 1. 목적
본 정책은 CMMI-DEV-ML3 Process Management 카테고리(OPD, OPF, OT)의 요구를 충족하기 위해, 조직이 표준프로세스(OSSP)와 프로세스 자산(OPA)을 **정의·유지·배포·개선·교육**하는 거버넌스 방향을 정의한다.

## 2. 적용 범위
조직 차원에서 운영되는 모든 표준프로세스, 프로세스 자산 라이브러리(PAL), 측정저장소, 라이프사이클 모델, 테일러링 가이드, 조직 교육에 적용한다. 프로젝트별 정의 프로세스(IPM 산출)는 본 정책의 상위 통제 아래 [[POL-CMMI-02_프로젝트_관리_정책]] 에 위임한다.

## 3. 정의
- **OSSP** (Organization's Set of Standard Processes): 조직 표준프로세스 집합.
- **OPA** (Organizational Process Assets): OSSP·라이프사이클 모델·테일러링 가이드·측정저장소·PAL을 포함하는 조직 자산.
- **EPG** (Engineering Process Group): 조직 표준프로세스 정의·개선을 책임지는 그룹.

## 4. 역할과 책임 (RACI 요지)
| 역할 | 책임 |
|---|---|
| **CEO/CTO** | 정책 승인, 프로세스 개선 자원 배정, OPF 액션 플랜 최종 승인 |
| **Senior Management Steering Group** | 조직 프로세스 니즈·개선 우선순위 결정, 분기 검토 |
| **EPG Lead** | OSSP/OPA 유지·개정, OPF SP1.1~3.4 실행, 본 정책 유지 |
| **Training Manager** | OT SP1.3 전술계획 수립, 교육 전달·기록·효과성 평가 |
| **Process Owner (per process)** | 담당 표준프로세스의 정확성·일관성 유지 |
| **모든 프로젝트** | 배포된 OSSP를 기반으로 정의된 프로세스 운영 (GP 3.1) |

## 5. 정책 원칙
1. **OSSP 단일 출처 원칙** — 조직 표준프로세스는 PAL에 단일 출처로 게시하며, 모든 프로젝트는 PAL에서 테일러링한다 (OPD SG1, GP 3.1).
2. **정기적 개선 사이클 운영** — OPF SG1~SG3에 따라 프로세스 평가·개선 계획·배포·실행 모니터링·경험 통합의 사이클을 연 1회 이상 운영한다.
3. **전략적 교육 정렬** — 조직 교육은 조직 전략·표준프로세스 니즈에서 도출하며 (OT SP1.1~1.2), 프로젝트·개인의 일회성 요구는 별도 채널로 처리한다.
4. **측정 기반 의사결정** — 조직 측정저장소(OPD SP1.4)의 데이터를 OPF 의사결정·OT 효과성 평가에 사용한다.
5. **경험 환류** — 모든 프로젝트는 종료 시 교훈·측정값·개선제안을 OPA에 환류한다 (OPF SP3.4, IPM SP1.7).

## 6. 준수 기준
- OSSP 모든 표준프로세스에 대해 본 정책 + GP 2.1(조직 정책 수립)이 적용됨을 PPQA(객관적 평가)로 입증.
- OPA 변경은 [[PRO-CMMI-04-01_형상_관리_절차]] (CM)의 베이스라인 통제를 따른다.
- 교육 이수율 ≥ 95%, 효과성 평가 ≥ 4.0/5.0 유지.

## 7. 관련 하위 절차 (PRO)
- [[PRO-CMMI-01-01_조직_표준프로세스_수립_유지_절차]] — OPD SG1
- [[PRO-CMMI-01-02_조직_프로세스_개선_배포_절차]] — OPF SG1~SG3
- [[PRO-CMMI-01-03_조직_훈련_절차]] — OT SG1~SG2

## 8. 표준 매핑 (Traceability)
| CMMI 조항 | Req-ID | 반영 |
|---|---|---|
| OPD SG1 | CMMIDEV-OPD-SG1-REQ-001 | §5-1 OSSP 단일 출처 |
| OPD SP1.1~1.7 | CMMIDEV-OPD-SP1.1~1.7-REQ-001 | §7 PRO-CMMI-01-01 |
| OPF SG1~SG3 | CMMIDEV-OPF-SG1~SG3-REQ-001 | §5-2 정기적 개선, §7 PRO-CMMI-01-02 |
| OPF SP1.1~3.4 | CMMIDEV-OPF-SP1.1~3.4-REQ-001 | §7 PRO-CMMI-01-02 |
| OT SG1~SG2 | CMMIDEV-OT-SG1~SG2-REQ-001 | §5-3 전략적 교육 정렬 |
| OT SP1.1~2.3 | CMMIDEV-OT-SP1.1~2.3-REQ-001 | §7 PRO-CMMI-01-03 |
| GG 2 / GP 2.1 | CMMIDEV-GG2-REQ-001, CMMIDEV-GP2.1-REQ-001 | 본 POL 자체 (정책 수립) |
| GG 3 / GP 3.1, 3.2 | CMMIDEV-GG3-REQ-001, GP3.1/3.2 | §5-5 경험 환류 |

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-OPD-SG1-REQ-001 (p.192)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-OPF-SG1~SG3-REQ-001 (p.204-213)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-OT-SG1~SG2-REQ-001 (p.248-255)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/pa_relationships.yaml"
  locator: "BPM-feeds-OT (p.40)"
  retrieved_at: "2026-05-11"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (process-designer 생성) | - |
