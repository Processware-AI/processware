---
type: PRO
doc_id: "PRO-CMMI-04-01"
title: "프로세스 품질보증 절차"
version: "1.1"
owner: "QA Manager"
reviewer: "PCB"
approver: "CEO"
scope: "프로세스 수행·작업산출물의 객관 평가, 부적합 식별·전달·종결"
parent_policy: "[[POL-CMMI-04_품질_구성_및_의사결정_정책_v1.0]]"
child_wi:
  - "[[WI-CMMI-04-01-01_부적합_식별_및_기록_v1.0]]"
  - "[[WI-CMMI-04-01-02_프로세스_평가_v1.0]]"
  - "[[WI-CMMI-04-01-03_작업산출물_평가_v1.0]]"
  - "[[WI-CMMI-04-01-04_품질이슈_에스컬레이션_및_종결_v1.0]]"
  - "[[WI-CMMI-04-01-05_품질보증_기록_관리_v1.0]]"
standards: ["CMMI-DEV-ML3", "ISO 9001"]
scope_code: "CMMI"
tier: "S"
status: approved
created: 2026-04-29
updated: 2026-05-15
revision_source:
  act_trace: run-c4f8a1b2
  asis_input: "vault/02_표준/CMMI-DEV-ML3/_inputs/04_AsIs/queue-qa1b2c3d4.md"
  ncr_resolved: ["REC-NCR-04-01-2026-001"]
  build_command: "/build-standard CMMI-DEV-ML3 --from write --target PRO-CMMI-04-01"
tags: [PRO, CMMI, PQA]
---

# 프로세스 품질보증 절차 (PRO-CMMI-04-01)

> 상위 정책: [[POL-CMMI-04_품질_구성_및_의사결정_정책_v1.0]]

## 1. 목적
독립된 QA 가 프로세스 수행·작업산출물을 객관 평가하여 부적합을 식별·전달·종결하고, 결과를 근거 기록으로 보관한다.

## 2. 적용 범위
- 정의된 모든 프로세스의 수행 활동
- 핵심 작업산출물 표본 평가
- 모든 프로젝트와 프로세스 자산

## 3. 역할과 책임 (RACI)
| 단계 | QA | Process Owner | PM | PCB | CEO |
|---|---|---|---|---|---|
| 부적합 식별 | **R** | C | I | A | I |
| 프로세스 평가 | **R** | C | C | A | I |
| 산출물 평가 | **R** | C | C | A | I |
| 에스컬레이션·종결 | **R** | **R** | **R** | **A** | I |
| QA 기록 | **R** | C | I | A | I |

## 4. 절차 흐름
```mermaid
flowchart TD
  A[감사 계획] --> B[프로세스 평가<br/>WI-004-01-02]
  A --> C[산출물 평가<br/>WI-004-01-03]
  B --> D[부적합 식별<br/>WI-004-01-01]
  C --> D
  D --> E{경미/중대}
  E -->|경미| F[현장 시정]
  E -->|중대| G[에스컬레이션<br/>WI-004-01-04]
  G --> H[PCB 심의]
  H --> I{종결?}
  I -->|No| G
  I -->|Yes| J[QA 기록<br/>WI-004-01-05]
  F --> J
```

## 5. 단계별 상세
| # | 단계 | 설명 | 담당 | 입력 | 출력 |
|---|---|---|---|---|---|
| 1 | 감사 계획 | 분기 감사 계획 수립 | QA | 정의된 프로세스 | 감사 계획서 |
| 2 | 프로세스 평가 | 객관 평가 수행 | QA | 활동 증적 | 평가서 |
| 3 | 산출물 평가 | 산출물 객관 평가 | QA | 산출물 | 평가서 |
| 4 | 부적합 식별 | 부적합 기록 | QA | 평가서 | 부적합 등록부 |
| 5 | 에스컬레이션 | 미해결 시 상위 보고 | QA/PM | 부적합 | 에스컬레이션 |
| 6 | 종결 추적 | **QA(R) 가 부적합 등급별 SLA 안에 종결 추적. 일정 관리 PM(A). SLA 50% 경과 시 PM 자동 알림, 100% 경과 시 PCB 보고.** SLA — critical 20영업일 / major 60일 / minor 90일 (§6.2 휴리스틱 준수). 종결 시점 = capa_rec 발행 시점. | QA(R), PM(A) | 시정조치 + SLA 추적 | 종결 기록 + SLA 준수 표기 |
| 7 | QA 기록 | 활동·결과 기록 보관 | QA | 모든 결과 | QA 기록부 |

> **§5-6 변경 (v1.1)** — 기존 v1.0 의 "시정조치 종결까지 추적" 표현을 등급별 SLA·R/A 분리·자동 알림으로 구체화. As-Is `queue-qa1b2c3d4.md` §3-1 반영. KPI §7 의 "평균 종결 기간" 측정 시점과 정합.

## 6. 연계 업무지침 (WI)
- [[WI-CMMI-04-01-01_부적합_식별_및_기록_v1.0]]
- [[WI-CMMI-04-01-02_프로세스_평가_v1.0]]
- [[WI-CMMI-04-01-03_작업산출물_평가_v1.0]]
- [[WI-CMMI-04-01-04_품질이슈_에스컬레이션_및_종결_v1.0]]
- [[WI-CMMI-04-01-05_품질보증_기록_관리_v1.0]]

## 7. 통제점 / KPI
| 통제점 | 지표 | 목표 | 주기 | 측정 시점 정의 (v1.1) |
|---|---|---|---|---|
| 감사 계획 준수율 | 계획 대비 실시 | ≥ 95% | 분기 | 계획 = §5-1 감사 계획서 발행 / 실시 = MAT-005 §실행기록 의 본 PRO 관련 trace |
| 부적합 종결율 | 발견 대비 종결 | ≥ 95% | 분기 | 발견 = NCR 발행 (MAT-009 §발행) / 종결 = capa_rec 인용 후 §종결 행 이동 |
| 부적합 평균 종결 기간 | 발견→종결 | ≤ 20 영업일 | 분기 | **발견** = §5-4 부적합 식별 시점 (WI-04-01-01 의 REC 발행 또는 NCR 발행) / **종결** = §5-6 capa_rec 발행 시점. **영업일** = 한국 공휴일 제외 (자세한 명세는 vault/09_REF_참고자료/표준_프로세스_심사_가이드.md 부록 B). |
| QA 독립성 점검 | 평가자 vs 수행자 분리 | 100% | 분기 | independence-guard 의 audit trace 별 violations: [] 비율 |
| 동일 부적합 재발률 | 재발 비율 | < 10% | 반기 | (동일 PRO·Req 의 NCR 2회 이상) / (전체 NCR). MAT-009 §"반복 부적합 TOP" 인용 |
| **분기 측정 보고서 산출** (v1.1 신규) | 본 표 5개 지표의 측정값 보고서 | 분기 1회 발행 | 분기 | TMP-CMMI-04-01-XX-XX (Phase 4.5 신설 예정 — queue-q9d8c7b6a 통합) |

> **§7 변경 (v1.1)** — 기존 v1.0 의 측정 시점이 모호한 점을 등급별·시점별 정합으로 구체화. As-Is `queue-qa1b2c3d4.md` §3-2 반영. queue-qe5f6a7b8 (KPI 종결율) / queue-q9d8c7b6a (KPI 측정 명문화) 와 root cause 통합.

## 8. 표준 매핑 (Traceability)
| Practice | Req-ID | 반영 위치 |
|---|---|---|
| PQA 1.1 | CMMI-PQA-1.1 | §5-4 부적합 식별 |
| PQA 2.1 | CMMI-PQA-2.1 | §5-2 프로세스 평가 |
| PQA 2.2 | CMMI-PQA-2.2 | §5-3 산출물 평가 |
| PQA 2.3 | CMMI-PQA-2.3 | §5-5,6 에스컬레이션·종결 |
| PQA 2.4 | CMMI-PQA-2.4 | §5-7 QA 기록 |

## 9. 출처 (source_citation)
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/PQA.pdf"
  locator: "Process Quality Assurance PG1~PG2"
  retrieved_at: "2026-04-29"
  license: "ISACA copyright — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 1.0 | 2026-04-29 | 최초 승인 (CMMI-DEV-ML3 편입) | CEO |
| 1.1 | 2026-05-15 | §5-6 종결 추적 SLA·R/A 분리 명시 (등급별 critical 20영업일/major 60일/minor 90일) + §7 KPI 측정 시점 정의 보강 + §7 분기 측정 보고서 산출물 신설. As-Is queue-qa1b2c3d4 (NCR-001 critical / F-001 / REQ-005) 반영. 4차원 PDCA 첫 폐쇄 루프 실증. | PCB (auto-approved Phase 1 PoC) |
