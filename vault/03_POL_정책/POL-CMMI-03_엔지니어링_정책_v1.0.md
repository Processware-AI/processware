---
type: POL
doc_id: "POL-CMMI-03"
title: "엔지니어링 정책"
version: "1.0"
owner: "Engineering Director"
reviewer: "Process Control Board (PCB)"
approver: "CEO"
scope: "요구사항 개발·관리, 기술솔루션, 제품통합, 검증·확인, 동료검토를 포함한 SW/시스템 엔지니어링 일체"
child_pro:
  - "[[PRO-CMMI-03-01_요구사항_개발_및_관리_절차_v1.0]]"
  - "[[PRO-CMMI-03-02_기술솔루션_절차_v1.0]]"
  - "[[PRO-CMMI-03-03_제품통합_절차_v1.0]]"
  - "[[PRO-CMMI-03-04_검증_및_확인_절차_v1.0]]"
  - "[[PRO-CMMI-03-05_동료검토_절차_v1.0]]"
standards: ["CMMI-DEV-ML3"]
scope_code: "CMMI"
tier: "C"
layer: "L2_engineering"
integration_mode: "interface_only"
status: approved
created: 2026-04-29
updated: 2026-04-29
retention: "상시"
tags: [POL, CMMI, engineering]
---

# 엔지니어링 정책 (POL-CMMI-03)

> 상위 기준: [[표준프로세스_구성원칙]] · 상위 정책: [[POL-CMMI-01_거버넌스_및_프로세스자산_정책_v1.0]]

## 1. 목적
본 정책은 CMMI-DEV ML3 의 **요구사항 개발·관리(RDM)·기술솔루션(TS)·제품통합(PI)·검증·확인(VV)·동료검토(PR)** Practice Area 의 의도와 가치를 실현하기 위한 엔지니어링 활동의 원칙·책임·통제 기준을 정의한다. 요구사항으로부터 인도까지 결함을 조기에 발견·예방하여 고객 가치를 보장한다.

## 2. 적용 범위
- 신규 SW/시스템 개발, 기능 개선, 기술 개조 프로젝트의 모든 엔지니어링 활동
- 외주 개발 시 인수자 측 엔지니어링 책임 활동(요구사항 정의, 통합, V&V, 검토 참여 등)
- 운영 단계 핫픽스·긴급 패치는 테일러링 후 축약 적용

## 3. 정책 원칙
1. **요구사항 추적성(Bidirectional Traceability)** — 이해관계자 요구로부터 솔루션 구성요소까지 양방향 추적성을 유지한다.
2. **대안 평가 우선(Alternatives First)** — 솔루션·구성요소 결정은 명시된 기준으로 대안을 분석한 후 선택한다.
3. **점진적 통합(Incremental Integration)** — 통합은 정의된 전략·환경·절차에 따라 단계적으로 수행하고 인터페이스를 항상 검증한다.
4. **검증과 확인의 분리(V & V Separation)** — 검증(요구사항 충족)과 확인(의도 환경 작동)을 분리 계획·실행·기록한다.
5. **결함 조기 발견(Defect Earliness)** — 동료검토를 핵심 작업산출물의 게이트로 두어 후공정 결함을 예방한다.

## 4. 역할과 책임
| 역할 | 책임 |
|---|---|
| **Engineering Director** | 엔지니어링 표준·환경·인프라 승인, 게이트 결과 검토 |
| **PM** | 엔지니어링 계획·일정·자원 보장, 게이트 통과 책임 |
| **요구사항 분석가(BA)** | 요구사항 도출·합의·추적성·검증 |
| **아키텍트 / 시니어 엔지니어** | 기술솔루션 대안분석·설계·인터페이스 정의 |
| **개발자** | 설계 준수 구현, 동료검토 참여, 단위검증 |
| **V&V 엔지니어** | 검증·확인 계획·환경·실행·결과 분석 |
| **이해관계자(고객·운영)** | 요구사항 합의, 인수확인 |

## 5. 준수 기준
- 요구사항은 [[PRO-CMMI-03-01_요구사항_개발_및_관리_절차_v1.0]] 에 따라 추적성 매트릭스에 등재
- 주요 설계 결정은 POL-CMMI-04 의 의사결정 분석(DAR) 적용 대상
- 통합·V&V 환경은 형상관리(POL-CMMI-04) 통제 하에 유지
- 동료검토 대상·기준은 [[PRO-CMMI-03-05_동료검토_절차_v1.0]] 정의 준수, 데이터는 측정저장소(POL-CMMI-01) 등재
- 인터페이스(ICD)·운영개념(OpsCon)·사용자 문서는 산출물 필수

## 6. 관련 하위 절차 (PRO)
- [[PRO-CMMI-03-01_요구사항_개발_및_관리_절차_v1.0]] — RDM PA
- [[PRO-CMMI-03-02_기술솔루션_절차_v1.0]] — TS PA
- [[PRO-CMMI-03-03_제품통합_절차_v1.0]] — PI PA
- [[PRO-CMMI-03-04_검증_및_확인_절차_v1.0]] — VV PA
- [[PRO-CMMI-03-05_동료검토_절차_v1.0]] — PR PA

## 7. 표준 매핑 (Traceability)
| Practice | Req-ID | 반영 |
|---|---|---|
| RDM 1.1~3.7 | CMMI-RDM-1.1, 2.1~2.5, 3.1~3.7 | §3 원칙 1, §6 PRO-301 |
| TS 1.1~3.2 | CMMI-TS-1.1, 2.1~2.5, 3.1~3.2 | §3 원칙 2, §6 PRO-302 |
| PI 1.1~3.4 | CMMI-PI-1.1, 2.1~2.3, 3.1~3.4 | §3 원칙 3, §6 PRO-303 |
| VV 1.1~3.3 | CMMI-VV-1.1~1.2, 2.1~2.3, 3.1~3.3 | §3 원칙 4, §6 PRO-304 |
| PR 1.1~3.1 | CMMI-PR-1.1, 2.1~2.3, 3.1 | §3 원칙 5, §6 PRO-305 |

## 8. 출처 (source_citation)
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/RDM.pdf"
  locator: "Requirements Development & Management PG1~PG3"
  retrieved_at: "2026-04-29"
  license: "ISACA copyright — paraphrase only"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Development PAs/TS.pdf"
  locator: "Technical Solution PG1~PG3"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Development PAs/PI.pdf"
  locator: "Product Integration PG1~PG3"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/VV.pdf"
  locator: "Verification & Validation PG1~PG3"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/PR.pdf"
  locator: "Peer Reviews PG1~PG3"
  paraphrase_only: true
```

## 9. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 1.0 | 2026-04-29 | 최초 승인 (CMMI-DEV-ML3 편입) | CEO |
