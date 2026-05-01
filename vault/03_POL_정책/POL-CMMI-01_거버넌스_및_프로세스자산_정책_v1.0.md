---
type: POL
doc_id: "POL-CMMI-01"
title: "거버넌스 및 프로세스자산 정책"
version: "1.0"
owner: "SEPG Lead"
reviewer: "Process Control Board (PCB)"
approver: "CEO"
scope: "조직 표준 프로세스 집합(OSSP)·프로세스 자산 라이브러리(PAL)·측정 저장소를 포함한 전사 프로세스 거버넌스 일체"
child_pro:
  - "[[PRO-CMMI-01-01_거버넌스_운영_절차_v1.0]]"
  - "[[PRO-CMMI-01-02_프로세스_자산_개발_절차_v1.0]]"
  - "[[PRO-CMMI-01-03_프로세스_관리_및_개선_절차_v1.0]]"
  - "[[PRO-CMMI-01-04_구현_인프라_운영_절차_v1.0]]"
standards: ["CMMI-DEV-ML3"]
scope_code: "CMMI"
tier: "M"
layer: "L2_engineering"
integration_mode: "interface_only"
status: approved
created: 2026-04-29
updated: 2026-04-29
retention: "상시"
tags: [POL, CMMI, governance, process-asset]
---

# 거버넌스 및 프로세스자산 정책 (POL-CMMI-01)

> 상위 기준: [[표준프로세스_구성원칙]] · 표준 분류: [[07_표준분류레지스트리]] · 영역코드: `CMMI`

## 1. 목적
본 정책은 CMMI-DEV v3.0 ML3 의 **거버넌스(GOV)·프로세스 자산 개발(PAD)·프로세스 관리(PCM)·구현 인프라(II)** Practice Area 가 요구하는 조직 차원의 방향성·자원·자산·내재화 체계를 정의하여, 조직의 모든 개발 활동이 일관된 정의 프로세스에 따라 수행되고 비즈니스 목표 달성에 기여하도록 한다.

## 2. 적용 범위
- 전사 개발 부문(연구개발·SW엔지니어링·시스템엔지니어링)
- 조직 표준 프로세스 집합(OSSP), 테일러링 지침, 프로세스 자산 라이브러리(PAL), 조직 측정 저장소
- 프로세스 정의·전개·내재화·개선 활동 일체
- 임시 프로토타이핑·연구탐색 단계는 테일러링 적용 후 제외 가능

## 3. 정책 원칙
1. **경영진 책임(Governance)** — 고위 경영진은 프로세스의 방향·자원·역량 보장에 대한 최종 책임을 갖고 정해진 주기로 활동·상태·결과를 검토한다.
2. **단일 표준 프로세스(OSSP)** — 조직은 하나의 표준 프로세스 집합과 테일러링 지침을 유지하며, 모든 프로젝트는 이를 기반으로 자신의 프로세스를 정의한다.
3. **자산 재사용(PAL)** — 검증된 산출물·교훈·측정데이터는 프로세스 자산 라이브러리에 등재하여 재사용한다.
4. **내재화 우선(Implementation Infrastructure)** — 프로세스가 정의된 대로 일관 수행되도록 자원·교육·코칭·점검을 제공한다.
5. **측정 기반 개선(Performance Driven)** — 프로세스 활동의 비용·효익·성과를 측정값으로 확인하여 개선 의사결정을 정량적으로 내린다.

## 4. 역할과 책임
| 역할 | 책임 |
|---|---|
| **CEO / 고위 경영진** | 프로세스 정책·자원·예산 승인, 분기 거버넌스 검토 주재 |
| **Process Control Board (PCB)** | 프로세스 정책·OSSP 변경 심의, 개선과제 우선순위 결정 |
| **SEPG (Process Owner)** | OSSP·PAL·측정저장소 개발·유지, 테일러링 지침 관리 |
| **QA / 내부심사팀** | 프로세스 준수 객관 평가, 부적합 보고 |
| **프로젝트관리자(PM)** | 자기 프로젝트의 프로세스 정의(테일러링)·준수·개선 제안 |
| **모든 임직원** | 정의된 프로세스 사용, 개선 의견 제시, 교육 이수 |

## 5. 준수 기준
- 거버넌스 검토는 분기 1회 이상 정기 개최, 회의록·시정조치를 [[MAT-005_심사증적_인덱스_v1.0]] 에 등재
- OSSP 변경은 PCB 심의 + 영향평가 + CEO 승인 후 배포
- 프로젝트는 착수 30일 내 OSSP 기반 테일러링된 프로세스를 정의·승인 (PRO-CMMI-02-01 연계)
- 모든 PA 활동은 II PG2~PG3 의 자원·도구·교육·내재화 점검을 통과해야 함
- 프로세스 자산 등재 전 형상관리(POL-CMMI-04) 통과 필수

## 6. 관련 하위 절차 (PRO)
- [[PRO-CMMI-01-01_거버넌스_운영_절차_v1.0]] — GOV PA (경영진 방향·자원·검토)
- [[PRO-CMMI-01-02_프로세스_자산_개발_절차_v1.0]] — PAD PA (OSSP·테일러링·PAL)
- [[PRO-CMMI-01-03_프로세스_관리_및_개선_절차_v1.0]] — PCM PA (개선기회·전개·평가)
- [[PRO-CMMI-01-04_구현_인프라_운영_절차_v1.0]] — II PA (자원제공·일관실행·준수검토)

## 7. 표준 매핑 (Traceability)
| Practice | Req-ID | 반영 |
|---|---|---|
| GOV 1.1, 2.1~2.6, 3.1~3.2 | CMMI-GOV-1.1, 2.1~2.6, 3.1~3.2 | §3 원칙 1, §4 CEO/PCB, §5 거버넌스 검토 |
| PAD 1.1, 2.1~2.2, 3.1~3.6 | CMMI-PAD-1.1, 2.1~2.2, 3.1~3.6 | §3 원칙 2~3, §4 SEPG, §6 PRO-102 |
| PCM 1.1, 2.1~2.2, 3.1~3.4 | CMMI-PCM-1.1, 2.1~2.2, 3.1~3.4 | §3 원칙 5, §6 PRO-103 |
| II 1.1, 2.1~2.2, 3.1~3.3 | CMMI-II-1.1, 2.1~2.2, 3.1~3.3 | §3 원칙 4, §6 PRO-104 |

## 8. 출처 (source_citation)
```yaml
- type: standard_original
  publisher: "ISACA / CMMI Institute"
  publication: "CMMI for Development v3.0 — Governance (GOV) Practice Area"
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/GOV.pdf"
  locator: "PA-2 Governance, PG1~PG3 Practice Statements"
  retrieved_at: "2026-04-29"
  license: "ISACA copyright — paraphrase only"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/PAD.pdf"
  locator: "Process Asset Development PG1~PG3"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/PCM.pdf"
  locator: "Process Management PG1~PG3"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/II.pdf"
  locator: "Implementation Infrastructure PG1~PG3"
  paraphrase_only: true
```

## 9. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 1.0 | 2026-04-29 | 최초 승인 (CMMI-DEV-ML3 편입) | CEO |
