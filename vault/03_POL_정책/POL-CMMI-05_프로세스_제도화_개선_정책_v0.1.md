---
type: POL
doc_id: POL-CMMI-05
title: "프로세스 제도화 및 개선 정책"
version: "0.1"
status: draft
owner: "EPG Lead"
reviewer: "Senior Management Steering Group"
approver: "CEO/CTO"
scope_code: CMMI
scope: "GG2(Managed Process)·GG3(Defined Process) 제도화 원칙 — 전 18 PA 공통"
standards: [CMMI-DEV-ML3-V1.3]
standards_meta:
  publisher: "Software Engineering Institute (CMU/SEI)"
  year: 2010
  publication_report: "CMU/SEI-2010-TR-033"
  license: "internal_use_derivative_work"
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_coverage: "ALL_18_PA (GG1/GG2/GG3 instantiation)"
category: "Generic Goals / Institutionalization"
child_pro:
  - "(GG2/GG3 GP는 별도 PRO 없이 각 PA의 PRO에 내재화)"
created: 2026-05-11
updated: 2026-05-11
retention: "상시"
tags: [POL, CMMI, GG, GP, Institutionalization, ML2, ML3]
related:
  - "[[적용요건]]"
  - "[[POL-CMMI-01_조직_프로세스_거버넌스_정책]]"
  - "[[POL-CMMI-02_프로젝트_관리_정책]]"
  - "[[POL-CMMI-03_엔지니어링_정책]]"
  - "[[POL-CMMI-04_지원_품질보증_정책]]"
---

# 프로세스 제도화 및 개선 정책 (POL-CMMI-05)

## 1. 목적
본 정책은 CMMI-DEV-ML3의 Generic Goals(GG1/GG2/GG3) 및 Generic Practices(GP 1.1, GP 2.1~2.10, GP 3.1~3.2)를 전 18 PA에 일관되게 제도화(institutionalize)하는 조직 차원의 방향을 정의한다. ML3 cumulative — 모든 PA는 Managed Process(GG2) 및 Defined Process(GG3) 수준으로 운영되어야 한다.

## 2. 적용 범위
ML3 적용 범위 내 모든 18개 PA(ML2 7 + ML3 11)에 횡단 적용된다. 각 PA의 PRO는 본 정책의 GP 요구를 내재화하여 작성·운영한다.

## 3. 정의
- **Institutionalization** (제도화): 프로세스가 일회성이 아닌, 조직 문화·행동·자원에 내장되어 인력 교체에도 지속되는 상태.
- **Managed Process** (GG2): 정책 수립·계획·자원·역할 할당·교육·통제·이해관계자 참여·모니터링·준수 평가·상위 검토를 갖춘 프로세스.
- **Defined Process** (GG3): OSSP에서 테일러링되어 프로젝트의 정의된 프로세스로 운영되고, 경험이 OPA에 환류되는 프로세스.

## 4. 역할과 책임 (RACI 요지)
| 역할 | 책임 |
|---|---|
| **CEO/CTO** | 본 정책 + 각 PA 정책(POL-CMMI-01~04) 승인, 자원 배정 |
| **Senior Management** | 분기별 프로세스 상태 검토 (GP 2.10) |
| **EPG Lead** | GG3 정의된 프로세스 가이드 제공, 경험 통합 (GP 3.2) |
| **Process Owner (per PA)** | 담당 PA의 GP 2.1~2.10 + GP 3.1~3.2 충족 |
| **PPQA** | GP 2.9 (객관적 준수 평가) 수행 |
| **CM** | GP 2.6 (work product 통제) 지원 |
| **OT (Training Mgr)** | GP 2.5 (교육) 지원 |
| **MA (Measurement Analyst)** | GP 2.8 (모니터링 측정) 지원 |

## 5. 정책 원칙 (GG1/GG2/GG3 instantiation)
1. **모든 PA에 정책 + 계획 + 자원 + 책임 + 교육 적용** — GP 2.1~2.5는 모든 PA에 적용된다. 각 PA의 PRO는 정책 링크(POL-CMMI-01~04)·계획·자원·책임·교육 항목을 명시적으로 포함해야 한다.
2. **모든 PA의 work product를 통제** — GP 2.6에 따라 모든 PA의 산출물은 [[PRO-CMMI-04-01_형상_관리_절차]] (CM)의 적절한 통제 수준으로 관리한다.
3. **이해관계자 참여를 식별·관리** — GP 2.7에 따라 각 PA는 관련 이해관계자를 식별하고 관여 시점·방식을 계획·기록한다.
4. **프로세스를 모니터링·평가** — GP 2.8(MA 연계)·GP 2.9(PPQA 연계)에 따라 각 PA는 측정·객관 평가의 대상이 된다.
5. **상위 경영진 검토** — GP 2.10에 따라 각 PA의 상태·이슈·결과는 정기적으로 상위 경영진에 보고된다 (POL-CMMI-02 PMC SP1.6 + IPM 보고와 연계).
6. **OSSP 테일러링** — GP 3.1에 따라 각 프로젝트·조직 단위는 OSSP를 테일러링한 정의된 프로세스를 보유한다 (OPD SP1.3 + IPM SP1.1).
7. **경험 환류** — GP 3.2에 따라 각 PA의 측정값·교훈·산출물·개선제안은 OPA에 환류된다 (OPF SP3.4 + IPM SP1.7).

## 6. 준수 기준
- 모든 PA의 PRO는 본 정책의 §5-1~7 항목을 frontmatter 또는 본문 §X (GP 매핑)에 명시.
- PPQA 분기 감사: 각 PA의 GG2/GG3 GP 충족 여부 평가.
- OPF 연 1회 SCAMPI B/C 평가 또는 동등 평가로 GG2/GG3 만족도 측정.

## 7. 하위 PRO 위임 방식
본 정책은 별도 PRO를 두지 않고, 각 PA의 PRO(PRO-CMMI-01-01 ~ 04-04)에 다음 형태로 내재화된다.

| GP | 내재화 위치 |
|---|---|
| GP 1.1 (Perform Specific Practices) | 각 PRO의 §4 절차 흐름 본문 |
| GP 2.1 (Establish Policy) | 각 PRO의 `parent_policy` frontmatter |
| GP 2.2 (Plan the Process) | 각 PRO의 §5 단계별 상세 + 연계 TMP(계획서) |
| GP 2.3 (Provide Resources) | 각 PRO의 §3 역할 + IPM SP1.4 통합 계획 |
| GP 2.4 (Assign Responsibility) | 각 PRO의 §3 RACI |
| GP 2.5 (Train People) | 각 PRO의 §6 연계 — OT 교육 커리큘럼 |
| GP 2.6 (Control Work Products) | 각 PRO의 §6 연계 — CM 베이스라인 |
| GP 2.7 (Involve Stakeholders) | 각 PRO의 §3 RACI + §5 단계별 stakeholder column |
| GP 2.8 (Monitor & Control) | 각 PRO의 §7 KPI + PMC 연계 |
| GP 2.9 (Evaluate Adherence) | 각 PRO의 §7 KPI + PPQA 연계 |
| GP 2.10 (Higher Mgmt Review) | 각 PRO의 §7 KPI + 분기 경영진 검토 보고 |
| GP 3.1 (Defined Process) | 각 PRO의 IPM SP1.1 테일러링 연계 |
| GP 3.2 (Collect Experiences) | 각 PRO의 §6 연계 — OPF SP3.4 / IPM SP1.7 |

## 8. 표준 매핑 (Traceability)
| CMMI 조항 | Req-ID | 반영 |
|---|---|---|
| GG 1 | CMMIDEV-GG1-REQ-001 | §5 전체 (specific goals 달성 전제) |
| GP 1.1 | CMMIDEV-GP1.1-REQ-001 | §7 GP 1.1 row |
| GG 2 | CMMIDEV-GG2-REQ-001 | §3 Managed Process 정의 + §5 |
| GP 2.1~2.10 | CMMIDEV-GP2.1~2.10-REQ-001 | §5 + §7 GP rows |
| GG 3 | CMMIDEV-GG3-REQ-001 | §3 Defined Process + §5-6,7 |
| GP 3.1, 3.2 | CMMIDEV-GP3.1-REQ-001, GP3.2-REQ-001 | §5-6,7 + §7 GP rows |

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-GG1-REQ-001 (p.68)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-GG2-REQ-001 (p.68) + GP2.1~2.10 (p.69-113)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-GG3-REQ-001 + GP3.1, GP3.2 (p.115)"
  retrieved_at: "2026-05-11"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (process-designer 생성) | - |
