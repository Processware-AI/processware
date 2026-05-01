---
type: POL
doc_id: "POL-CMMI-005"
title: "자원·역량·공급자 정책"
version: "1.0"
owner: "HR & Procurement Director"
reviewer: "Process Control Board (PCB)"
approver: "CEO"
scope: "조직의 인적 역량(교육), 공급자 합의 관리"
child_pro:
  - "[[PRO-CMMI-501_조직_훈련_절차_v1.0]]"
  - "[[PRO-CMMI-502_공급자_합의_관리_절차_v1.0]]"
standards: ["CMMI-DEV-ML3", "ISO 9001"]
scope_code: "CMMI"
tier: "S"
layer: "L2_engineering"
integration_mode: "interface_only"
status: approved
created: 2026-04-29
updated: 2026-04-29
retention: "상시"
tags: [POL, CMMI, training, supplier]
---

# 자원·역량·공급자 정책 (POL-CMMI-005)

> 상위 기준: [[표준프로세스_구성원칙]] · 상위 정책: [[POL-CMMI-001_거버넌스_및_프로세스자산_정책_v1.0]]

## 1. 목적
본 정책은 CMMI-DEV ML3 의 **조직 훈련(OT)·공급자 합의 관리(SAM)** Practice Area 요구사항을 충족하여, 비즈니스 목표를 지원하는 인적 역량을 체계적으로 개발·유지하고, 외부 공급자가 제공하는 작업·산출물의 품질·일정·인수가 통제됨을 보장한다.

## 2. 적용 범위
- 전사 정직원·계약직·상시 외주 인력의 직무·전략 교육
- 모든 외부 공급자(SI·SW 부품·HW·서비스·컨설팅)와의 합의(계약) 수명주기
- 단발성 구매(소액·표준품)는 SAM 의 경량 테일러링 적용

## 3. 정책 원칙
1. **전략 정렬 교육(Strategic Training)** — 조직의 전략적 교육 요구를 식별하고 전술 교육계획을 수립하여 충족한다.
2. **역량 증빙(Evidence-based Competence)** — 모든 직무는 필요 역량을 정의하고 교육 이수·실적을 기록·증빙으로 관리한다.
3. **공급자 합의(Supplier Agreement First)** — 외부 인도 작업·산출물은 명시된 합의 없이 착수·수용하지 않는다.
4. **객관 선정(Objective Selection)** — 공급자 선정은 명시된 평가 기준·가중치에 따라 객관적으로 수행한다.
5. **수용 후 인도(Accept-then-Deliver)** — 공급자 인도 솔루션은 정의된 인수 기준 통과 후 환경에 통합된다.

## 4. 역할과 책임
| 역할 | 책임 |
|---|---|
| **CEO** | 전략 교육·중대 공급자 계약 승인 |
| **HR Director** | 교육 요구분석·계획·시행·평가, 교육 역량 인프라 |
| **Procurement Manager** | 공급자 선정·계약·실행·인수 종합 |
| **PM / 부서장** | 직무 교육 요구 식별, 합의 이행 모니터링 |
| **공급자 평가위원회** | 평가 기준·가중치 운영, 선정 결과 승인 |
| **임직원** | 지정 교육 이수, 합의 위반 발견 시 보고 |

## 5. 준수 기준
- 직무별 필수 역량·교육 매핑은 [[PRO-CMMI-501_조직_훈련_절차_v1.0]] 에 따라 연 1회 갱신
- 모든 교육 이수 기록은 보관기간 5년 이상
- 신규 공급자는 평가 기준 점수 ≥ 합격선 + CEO 또는 위임자 승인 후 등재
- 공급자 합의 미체결 상태에서 작업 착수 금지
- 인수 시점 적합성 검사 미통과 시 통합 환경 반입 금지

## 6. 관련 하위 절차 (PRO)
- [[PRO-CMMI-501_조직_훈련_절차_v1.0]] — OT PA
- [[PRO-CMMI-502_공급자_합의_관리_절차_v1.0]] — SAM PA

## 7. 표준 매핑 (Traceability)
| Practice | Req-ID | 반영 |
|---|---|---|
| OT 1.1, 2.1~2.2, 3.1~3.7 | CMMI-OT-1.1, 2.1~2.2, 3.1~3.7 | §3 원칙 1~2, §6 PRO-501 |
| SAM 1.1~1.2, 2.1~2.6 | CMMI-SAM-1.1~1.2, 2.1~2.6 | §3 원칙 3~5, §6 PRO-502 |
| (Interface) ISO 9001 §7.2 | — | OT — 역량 |
| (Interface) ISO 9001 §8.4 | — | SAM — 외부 제공 통제 |

## 8. 출처 (source_citation)
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/OT.pdf"
  locator: "Organizational Training PG1~PG3"
  retrieved_at: "2026-04-29"
  license: "ISACA copyright — paraphrase only"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Supplier PA/SAM.pdf"
  locator: "Supplier Agreement Management PG1~PG2"
  paraphrase_only: true
```

## 9. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 1.0 | 2026-04-29 | 최초 승인 (CMMI-DEV-ML3 편입) | CEO |
