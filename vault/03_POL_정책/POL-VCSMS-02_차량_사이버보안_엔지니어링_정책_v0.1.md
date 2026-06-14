---
type: POL
doc_id: "POL-VCSMS-02"
title: "차량 사이버보안 엔지니어링 정책"
version: "0.1"
owner: "Cybersecurity Manager (CSM)"
reviewer: "Process Control Board (PCB)"
approver: "Top Management (경영진)"
scope: "프로젝트 차원 차량 사이버보안 엔지니어링 — 프로젝트 관리·TARA·컨셉·개발·검증·생산·공급망·운영·폐기"
child_pro:
  - "[[PRO-VCSMS-02-01_프로젝트_사이버보안_관리_절차]]"
  - "[[PRO-VCSMS-02-02_사이버보안_케이스_평가_및_릴리스_절차]]"
  - "[[PRO-VCSMS-02-03_위협분석_및_리스크평가_TARA_절차]]"
  - "[[PRO-VCSMS-02-04_컨셉_단계_사이버보안_엔지니어링_절차]]"
  - "[[PRO-VCSMS-02-05_제품개발_사이버보안_엔지니어링_절차]]"
  - "[[PRO-VCSMS-02-06_차량_수준_사이버보안_검증_절차]]"
  - "[[PRO-VCSMS-02-07_생산_사이버보안_통제_절차]]"
  - "[[PRO-VCSMS-02-08_분산_사이버보안_활동_및_공급망_절차]]"
  - "[[PRO-VCSMS-02-09_운영_업데이트_및_지원종료_폐기_절차]]"
standards: ["ISO/SAE 21434"]
area_code: VCSMS
module_display: ACSMS
layer: L2_engineering
integration_mode: interface_only
status: draft
created: 2026-06-14
updated: 2026-06-14
retention: "상시"
tags: [POL, VCSMS, ISO21434, cybersecurity, automotive, engineering, V-model, TARA, interface_only]
---

# 차량 사이버보안 엔지니어링 정책 (POL-VCSMS-02)

> 상위 기준: [[표준프로세스_구성원칙]] · 상위 거버넌스: [[POL-VCSMS-01_자동차_사이버보안_거버넌스_정책]] · 분류: [[07_표준분류레지스트리]]
> 통합방식: **interface_only** — 독립 엔지니어링 V-model 체계. 경계면(공급자·변경·형상·리스크 거버넌스)은 "참조" 링크로만 연결.

## 1. 목적
본 정책은 차량 item/component 의 **컨셉부터 개발·검증·생산·운영·지원종료·폐기에 이르는 프로젝트 차원 사이버보안 엔지니어링**의 원칙을 정의한다. 프로젝트 사이버보안 관리, 위협분석·리스크평가(TARA), V-model 기반 컨셉·개발·검증, 분산(공급망) 활동, post-development 활동을 리스크 기반으로 일관되게 수행하도록 한다.

## 2. 적용 범위
사이버보안 관련성이 인정된 모든 차량 개발·사후개발 프로젝트에 적용한다. 컨셉(Clause 9), 제품개발(Clause 10), 검증(Clause 11), 생산(Clause 12), 운영·유지(Clause 13.4), 지원종료·폐기(Clause 14), 프로젝트 의존 관리(Clause 6), 분산 활동(Clause 7), TARA 방법론(Clause 15)을 포괄한다. 전사 거버넌스·지속활동·사고대응은 [[POL-VCSMS-01_자동차_사이버보안_거버넌스_정책]] 이 관장한다.

## 3. 정책 원칙
1. **리스크 기반 엔지니어링** — 모든 사이버보안 활동은 TARA(Clause 15)로 도출된 리스크값에 비례하여 계획·수행하며, 리스크값 1 위협 시나리오 등은 정당한 근거 하에 테일러링한다.
2. **계획·테일러링·추적성** — 프로젝트마다 목표·의존성·담당·자원·기간·산출물을 포함한 사이버보안 계획을 수립하고, 형상·변경·요구사항·문서 관리(상위 QMS 참조)로 작업산출물의 추적성을 유지한다.
3. **V-model 일관성** — 목표→요구→사양→설계→구현→통합→검증→차량 수준 검증으로 하향·상향 추적성을 보장하고, 각 단계 결과의 완전·정확·일관성을 검증한다.
4. **케이스·독립평가 기반 릴리스** — 작업산출물로 뒷받침되는 사이버보안 케이스와 (해당 시) 독립 사이버보안 평가의 권고를 충족한 후에만 post-development 으로 릴리스한다.
5. **공급망·사후개발 책임 명확화** — 분산 활동은 사이버보안 인터페이스 합의(CIA)로 책임을 명시하고, 생산·운영·지원종료·폐기까지 post-development 사이버보안 요구를 유지한다.

## 4. 역할과 책임
| 역할 | 책임 |
|---|---|
| **Top Management (경영진)** | 정책 승인, 릴리스 게이트 최종 권한 |
| **Cybersecurity Manager (CSM)** | 엔지니어링 정책 유지, 프로젝트 계획 승인, 케이스 검토 |
| **Project Cybersecurity Lead** | 프로젝트 사이버보안 계획·테일러링·케이스 작성, 활동 추적 |
| **독립 사이버보안 평가자 (Assessor)** | 평가 수행 여부 검토, 독립 평가, 수용/조건부/거부 권고 |
| **TARA 분석가 / 보안 설계·검증 엔지니어** | TARA·설계·구현·통합·검증 수행, 약점·취약점 분석 |
| **공급자 / 조달 담당** | 역량 제공, CIA 합의, RFQ 대응 |

## 5. 준수 기준
- 사이버보안 계획·작업산출물은 형상·변경·요구사항·문서 관리 대상으로 한다 — 상위 QMS(§5.4.4 [RQ-05-11]) **참조** (interface).
- 공급자 관리·계약은 상위 공급자관리(§8.4) 와 정합하며, 사이버보안 측면은 CIA 로 명시한다 (interface).
- 변경·형상 관리는 상위 변경관리(§8.5)·구성관리(§7.5) 를 **참조**한다 (interface).
- 리스크 거버넌스는 상위 §6.1 및 거버넌스 정책([[POL-VCSMS-01_자동차_사이버보안_거버넌스_정책]])과 정합한다.
- 안전 관련 영향등급 도출은 ISO 26262-3:2018 §6.4.3 을 참조한다 ([[REF-003_ISO26262_기능안전_경계면_v0.1]]).
- 차량 내 업데이트·업데이트 역량은 UNECE R156(SUMS)와 정합한다 ([[REF-002_UNECE_R156_SUMS_요약_v0.1]]).

> **경계면(Interface) 표기** — 위 참조 항목은 MAT-07 Interface 테이블 등록 대상이다.

## 6. 관련 하위 절차 (PRO)
- [[PRO-VCSMS-02-01_프로젝트_사이버보안_관리_절차]] — 계획·테일러링·재사용·OTS/OOC (Clause 6.4.1–6.4.6)
- [[PRO-VCSMS-02-02_사이버보안_케이스_평가_및_릴리스_절차]] — 케이스·평가·릴리스 (§6.4.7–6.4.9)
- [[PRO-VCSMS-02-03_위협분석_및_리스크평가_TARA_절차]] — TARA 횡단 방법론 (Clause 15)
- [[PRO-VCSMS-02-04_컨셉_단계_사이버보안_엔지니어링_절차]] — 아이템정의·목표·컨셉 (Clause 9)
- [[PRO-VCSMS-02-05_제품개발_사이버보안_엔지니어링_절차]] — 사양·설계·구현·통합·검증 (Clause 10)
- [[PRO-VCSMS-02-06_차량_수준_사이버보안_검증_절차]] — 차량 수준 검증 (Clause 11)
- [[PRO-VCSMS-02-07_생산_사이버보안_통제_절차]] — 생산 통제 계획 (Clause 12)
- [[PRO-VCSMS-02-08_분산_사이버보안_활동_및_공급망_절차]] — 역량평가·RFQ·CIA (Clause 7)
- [[PRO-VCSMS-02-09_운영_업데이트_및_지원종료_폐기_절차]] — 업데이트·지원종료·폐기 (§13.4, Clause 14)

## 7. 표준 매핑 (Traceability)
| 표준 조항 | Req-ID (native) | 반영 |
|---|---|---|
| ISO/SAE 21434 Clause 6 | VCSMS-R-018~051 ([RQ/PM-06-01~34]) | §6 PRO-02-01, 02-02 |
| ISO/SAE 21434 Clause 7 | VCSMS-R-052~059 ([RQ/RC-07-01~08]) | §6 PRO-02-08 |
| ISO/SAE 21434 Clause 9 | VCSMS-R-068~078 ([RQ-09-01~11]) | §6 PRO-02-04 |
| ISO/SAE 21434 Clause 10 | VCSMS-R-079~091 ([RQ/RC-10-01~13]) | §6 PRO-02-05 |
| ISO/SAE 21434 Clause 11 | VCSMS-R-092, 093 ([RQ-11-01~02]) | §6 PRO-02-06 |
| ISO/SAE 21434 Clause 12 | VCSMS-R-094~096 ([RQ-12-01~03]) | §6 PRO-02-07 |
| ISO/SAE 21434 §13.4, Clause 14 | VCSMS-R-099~101 ([RQ-13-03], [RQ-14-01~02]) | §6 PRO-02-09 |
| ISO/SAE 21434 Clause 15 | VCSMS-R-102~118 ([RQ/RC/PM-15-01~17]) | §6 PRO-02-03 |

## 8. 출처 (source_citation)
```yaml
- type: standard_original
  file: "inputs/01_표준원문/AutoCyberSec/requirements.yaml"
  locator: "ISO/SAE 21434:2021 Clause 6,7,9,10,11,12,13.4,14,15 (normative)"
  retrieved_at: "2026-06-14"
  license: "ISO/SAE copyright"
  paraphrase_only: true
- type: standard_original
  file: "vault/02_적용요건/VCSMS_자동차사이버보안/적용요건.md"
  locator: "§3.2 Clause 6, §3.3 Clause 7, §3.5–3.11"
  retrieved_at: "2026-06-14"
  license: "ISO/SAE copyright"
  paraphrase_only: true
```

## 9. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-06-14 | 최초 초안 — ISO/SAE 21434 Clause 6,7,9–15 엔지니어링 정책 (interface_only) | (미승인) |
