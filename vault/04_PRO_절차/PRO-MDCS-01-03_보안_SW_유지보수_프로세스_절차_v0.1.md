---
type: PRO
doc_id: "PRO-MDCS-01-03"
title: "보안 SW 유지보수 프로세스 절차"
version: "0.1"
owner: "보안책임자(PSO)"
reviewer: "보안운영위원회(PSGB)"
approver: "경영책임자(Top Management)"
scope: "SUPPORTED/MAINTAINED 헬스SW 의 취약점 모니터링·보안 업데이트 정책·검증·제공 (Clause 6)"
parent_policy: "[[POL-MDCS-01_헬스SW_제품_보안_거버넌스_방침_v0.1]]"
child_wi: []
standards: ["IEC 81001-5-1"]
tier: "C"
pro_type: core
scope_type: project
source_scenarios: []
follows: ["PRO-MDCS-01-02"]
precedes: ["PRO-MDCS-01-05"]
interface_with: [IEC62304]
covers_requirements: [6.1.1-REQ-001, 6.1.1-REQ-002, 6.2.1-REQ-001, 6.2.2-REQ-001, 6.2.2-REQ-002, 6.3.1-REQ-001, 6.3.2-REQ-001, 6.3.3-REQ-001]
wi_sequence:
  - wi_id: WI-MDCS-01-03-01
    title: "보안 업데이트 정책 수립(전달 시간대·영향평가 기준)"
    mandatory: true
    entry_condition: null
  - wi_id: WI-MDCS-01-03-02
    title: "취약점 정보원 능동 모니터링"
    mandatory: true
    entry_condition: null
  - wi_id: WI-MDCS-01-03-03
    title: "보안 업데이트 검증(효과·회귀)"
    mandatory: true
    entry_condition: null
  - wi_id: WI-MDCS-01-03-04
    title: "보안 업데이트 안내·제공·무결성 검증"
    mandatory: true
    entry_condition: "WI-MDCS-01-03-03.status == done"
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [PRO, MDCS, cybersecurity, maintenance, IEC81001-5-1]
---

# 보안 SW 유지보수 프로세스 절차 (PRO-MDCS-01-03)

> 상위 정책: [[POL-MDCS-01_헬스SW_제품_보안_거버넌스_방침_v0.1]] · 기준: [[표준프로세스_구성원칙]]

## 1. 목적
출시된 헬스SW(SUPPORTED/MAINTAINED SOFTWARE)에 대해 취약점 정보를 능동 수집하고, 영향평가 기준에 따라 보안 업데이트를 적시 검증·제공하여 운영 단계의 보안을 유지한다.

## 2. 적용 범위
SUPPORTED SOFTWARE(취약점 모니터링 대상) 및 MAINTAINED SOFTWARE(보안 업데이트 제공 대상) 에 적용한다. *(향후 연계: [[IEC 62304 MDSW]] §6)*

## 3. 역할과 책임 (RACI)
| 단계 | PSO | 보안 운영 | 개발자 | 검증 인력 | 제품 사용자 통보 |
|---|---|---|---|---|---|
| 업데이트 정책 수립 | **A** | C | I | I | - |
| 취약점 모니터링 | C | **R** | I | - | - |
| 업데이트 검증 | C | C | **R** | **R** | - |
| 업데이트 안내·제공 | **A** | **R** | C | C | **R** |

## 4. 절차 흐름
```mermaid
flowchart TD
  A[보안 업데이트 정책 수립<br/>전달 시간대·영향평가 기준<br/>WI-01] --> B[취약점 정보원 능동 모니터링<br/>WI-02]
  B --> C{취약점<br/>식별?}
  C -->|예| D[문제해결 프로세스 연계<br/>PRO-MDCS-01-05]
  D --> E[보안 업데이트 생성]
  E --> F[업데이트 효과 검증<br/>+ 회귀(의도치 않은 영향)<br/>WI-03]
  F --> G{호환성·승인<br/>판정}
  G -->|MAINTAINED| H[업데이트 제공<br/>무결성 검증 가능 방식<br/>WI-04]
  G -->|SUPPORTED| I[업데이트 안내<br/>호환성/대체 완화책]
  C -->|아니오| B
```

## 5. 단계별 상세
| # | 단계 | 설명 | 담당 | 입력 | 출력 |
|---|---|---|---|---|---|
| 1 | 정책 수립 | 업데이트 전달·검증 시간대 + 영향평가 기준(영향·인지도·익스플로잇·배포량·외부통제) 규정 | PSO | 제품 컨텍스트 | 보안 업데이트 정책 |
| 2 | 모니터링 | SUPPORTED SW 취약점 정보원 능동 수집·검토 | 보안 운영 | 정보원 목록 | 모니터링 기록 |
| 3 | 검증 | 업데이트가 의도 취약점 해결·기능/품질 미영향(회귀) 검증 | 검증 인력 | 업데이트 | 검증·회귀 시험 기록 |
| 4 | 안내·제공 | MAINTAINED 무결성 검증 가능 제공 / SUPPORTED 호환성·대체 완화책 안내 | 보안 운영 | 검증 결과 | 배포 증적·안내·무결성 증적 |

## 6. 연계 업무지침 (WI)
- [[WI-MDCS-01-03-01_보안_업데이트_정책_수립_v0.1]] — (6.1.1)
- [[WI-MDCS-01-03-02_취약점_정보원_모니터링_v0.1]] — (6.2.1)
- [[WI-MDCS-01-03-03_보안_업데이트_검증_회귀_v0.1]] — (6.2.2)
- [[WI-MDCS-01-03-04_보안_업데이트_안내_제공_무결성_v0.1]] — (6.3.1~6.3.3)

## 7. 통제점 / KPI
| 통제점 | 지표 | 목표 | 주기 |
|---|---|---|---|
| 취약점 모니터링 | 정보원 검토 주기 준수율 | 100% | 주 |
| 업데이트 전달 SLA | 정책상 시간대 준수율 | ≥ 95% | 월 |
| 회귀 검증 | 업데이트별 회귀 시험 실시율 | 100% | 릴리스 |
| 업데이트 무결성 | 무결성 검증 적용률 | 100% | 배포 |

## 8. 표준 매핑 (Traceability)
| 표준 조항 | Req-ID | 반영 위치 |
|---|---|---|
| §6.1.1 | 6.1.1-REQ-001~002 | §5 단계1 |
| §6.2.1 | 6.2.1-REQ-001 | §5 단계2 |
| §6.2.2 | 6.2.2-REQ-001~002 | §5 단계3 |
| §6.3.1~6.3.3 | 6.3.1-REQ-001, 6.3.2-REQ-001, 6.3.3-REQ-001 | §5 단계4 |

## 9. 출처 (source_citation)
```yaml
- type: standard_original
  file: "inputs/01_표준원문/IEC81001-5-1/requirements.yaml"
  locator: "§6.1–6.3 (Software maintenance PROCESS)"
  retrieved_at: "2026-06-18"
  license: "IEC copyright — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| v0.1 | 2026-06-18 | 최초 작성 — Clause 6 보안 SW 유지보수 프로세스 | (미승인 초안) |
