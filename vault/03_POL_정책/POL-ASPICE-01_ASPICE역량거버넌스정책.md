---
type: POL
doc_id: "POL-ASPICE-01"
title: "ASPICE 역량 거버넌스 정책"
version: "0.1"
owner: "CTO"
reviewer: "Process Quality Office"
approver: "CEO"
scope: "VWAY Motors 전 개발 프로세스 (시스템/SW/HW/ML/지원/관리)"
domain: ASPICE
scope_code: ASPICE
child_pro:
  - "[[PRO-ASPICE-01-01_시스템공학프로세스]]"
  - "[[PRO-ASPICE-01-02_소프트웨어공학프로세스]]"
  - "[[PRO-ASPICE-01-03_하드웨어공학프로세스]]"
  - "[[PRO-ASPICE-01-04_머신러닝공학프로세스]]"
  - "[[PRO-ASPICE-01-05_검증및인도프로세스]]"
  - "[[PRO-ASPICE-01-06_구매및공급망프로세스]]"
  - "[[PRO-ASPICE-01-07_품질보증및형상관리프로세스]]"
  - "[[PRO-ASPICE-01-08_문제및변경관리프로세스]]"
  - "[[PRO-ASPICE-01-09_프로젝트관리프로세스]]"
  - "[[PRO-ASPICE-01-10_ML데이터관리프로세스]]"
  - "[[PRO-ASPICE-01-11_프로세스개선및재사용]]"
standards: ["Automotive SPICE 4.0"]
status: draft
created: "2026-05-06"
updated: "2026-05-06"
retention: "상시"
tags: [POL, ASPICE, ASPICE4, capability-governance, VWAY_Motors]
---

# ASPICE 역량 거버넌스 정책 (POL-ASPICE-01)

> 상위 기준: [[표준프로세스_구성원칙]] · 분류: [[07_표준분류레지스트리]]
> 적용요건: [[적용요건]] · 추적성: [[MAT-011_VWAY_Motors_추적성]]

---

## 1. 목적

본 정책은 VWAY Motors 가 차량용 ECU·ADAS·자율주행 시스템을 개발·인도하는 전 과정에서 **Automotive SPICE 4.0** 의 32 개 프로세스(Acquisition·Supply·System·Software·Hardware·Machine Learning·Support·Management·Process Improvement·Reuse) 에 대해 **정의된 Capability Level 목표를 일관되게 달성·유지** 하는 역량 거버넌스의 방향과 책임을 정한다.

본 정책은 다음을 보장한다:
- 개발 프로젝트 단위에서의 **Process Performance(PA 1.1)** 이행
- 조직 단위에서의 **Process Management(PA 2.1) / Work Product Management(PA 2.2)** 제도화
- 핵심 프로세스에 대한 **Process Definition(PA 3.1) / Process Deployment(PA 3.2)** 표준화

## 2. 적용 범위

VWAY Motors 의 모든 자동차 SW/HW/ML 개발 프로젝트(양산·선행·연구) 와 이를 지원하는 조직 차원 활동에 적용한다. 외주 개발(Tier 2/3 공급사 포함)은 ACQ.4 경계면을 통해 적용된다. 비개발(예: 단순 구매·시설 운영) 활동은 본 정책의 직접 적용 대상이 아니다.

## 3. 정책 원칙

1. **Base Practice 이행 우선** — 32 프로세스의 모든 BP 는 프로젝트에서 **이행 가능(Performable)** 해야 한다. 비이행 BP 는 명시적 테일러링 승인을 거쳐야 한다.
2. **Generic Practice 제도화** — Capability Level 2 이상의 GP 는 표준 프로세스(SPP) 와 인프라(도구·템플릿) 로 흡수되어 프로젝트별 재발명을 금한다.
3. **추적성 우선** — 이해관계자 → 시스템 → SW/HW/ML → 검증 → 인도까지 **양방향 추적성**을 유지한다. 추적성은 평가의 1차 증적이다.
4. **독립성 확보** — Quality Assurance(SUP.1) 의 **독립적 보고선·에스컬레이션 권한**을 보장한다. QA 는 개발 라인 책임자에게 종속되지 않는다.
5. **Capability Level 목표 차등화** — 모든 프로세스를 Level 3 으로 끌어올리지 않는다. 프로세스의 위험·빈도·계약 요구를 기준으로 차등 목표를 둔다(§5).

## 4. 역할과 책임

| 역할 | 책임 |
|---|---|
| **CEO** | 정책 승인, 자원·조직 배정 |
| **CTO** | 정책 유지·연 1회 유효성 검토, Capability Level 목표 승인 |
| **Process Quality Office (PQO)** | 표준 프로세스 정의·배포·평가 (PA 3.1/3.2 책임 조직) |
| **ASPICE Lead Assessor (내부)** | 정기 자가평가·외부평가 대응, gap 도출 |
| **Project Manager** | 프로젝트별 ASPICE 이행 책임 (PA 1.1/2.1/2.2) |
| **Quality Assurance Lead (SUP.1)** | 독립적 QA 활동·에스컬레이션 권한 행사 |
| **Process Owner (프로세스별)** | 32 프로세스 각각의 BP 이행·증적 보존 |

## 5. 역량 수준 목표 (Capability Level Target)

| 프로세스 그룹 | 대상 프로세스 | 1년 차 목표 | 3년 차 목표 |
|---|---|---|---|
| System Engineering | SYS.1~5 | L2 | L3 |
| Software Engineering | SWE.1~6 | L2 | L3 |
| Hardware Engineering | HWE.1~4 | L1 | L2 |
| Machine Learning Engineering | MLE.1~4 | L1 | L2 |
| Validation & Release | VAL.1, SPL.2 | L1 | L2 |
| Acquisition | ACQ.4 | L1 | L2 |
| Support (QA·CM) | SUP.1, SUP.8 | L2 | L3 |
| Support (PR·CR·ML Data) | SUP.9, SUP.10, SUP.11 | L1 | L2 |
| Management | MAN.3, MAN.5, MAN.6 | L2 | L3 |
| Process Improvement / Reuse | PIM.3, REU.2 | L1 | L2 |

> 차등 사유: OEM 평가 대상(SYS·SWE·SUP.1·MAN.3) 은 우선 L2~L3, 신규 그룹(MLE·SUP.11) 은 점진 상승, HWE 는 외주 비중 고려 L1 출발.

## 6. 준수 기준

- **자가평가 주기**: 분기 1회 (PA 1.1) + 연 1회 (PA 2.1~3.2 통합)
- **외부평가 주기**: OEM 요청 시 또는 2년 주기 자체 인증
- **증적 보존 기간**: 프로젝트 SOP 후 **15년** (자동차 산업 관행 + IATF 16949 정합)
- **Gap 시정 기한**: Major NC 30 일, Minor NC 60 일 내 시정조치
- **테일러링 승인**: PQO 검토 + CTO 승인. 승인 없는 BP 비이행 금지

## 7. 관련 하위 절차 (PRO)

본 정책은 11 개 하위 PRO 로 분해되어 운영된다:

- [[PRO-ASPICE-01-01_시스템공학프로세스]] — SYS.1~5
- [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] — SWE.1~6
- [[PRO-ASPICE-01-03_하드웨어공학프로세스]] — HWE.1~4
- [[PRO-ASPICE-01-04_머신러닝공학프로세스]] — MLE.1~4
- [[PRO-ASPICE-01-05_검증및인도프로세스]] — VAL.1, SPL.2
- [[PRO-ASPICE-01-06_구매및공급망프로세스]] — ACQ.4
- [[PRO-ASPICE-01-07_품질보증및형상관리프로세스]] — SUP.1, SUP.8
- [[PRO-ASPICE-01-08_문제및변경관리프로세스]] — SUP.9, SUP.10
- [[PRO-ASPICE-01-09_프로젝트관리프로세스]] — MAN.3, MAN.5, MAN.6
- [[PRO-ASPICE-01-10_ML데이터관리프로세스]] — SUP.11
- [[PRO-ASPICE-01-11_프로세스개선및재사용]] — PIM.3, REU.2

## 8. 표준 매핑 (Traceability)

| 표준 조항 | Req-ID | 반영 |
|---|---|---|
| ASPICE 4.0 PA 1.1 (Process Performance) | ASPICE-GOV-R-001 | §3 원칙 1, §6 자가평가 |
| ASPICE 4.0 PA 2.1 (Performance Mgmt) | ASPICE-GOV-R-001 | §4 역할, §6 시정조치 |
| ASPICE 4.0 PA 2.2 (Work Product Mgmt) | ASPICE-GOV-R-001 | §3 원칙 3 (추적성) |
| ASPICE 4.0 PA 3.1 (Process Definition) | ASPICE-GOV-R-001 | §4 PQO 책임 |
| ASPICE 4.0 PA 3.2 (Process Deployment) | ASPICE-GOV-R-001 | §5 차등 목표, §7 하위 PRO |
| ASPICE SUP.1.BP4 (QA 독립성) | ASPICE-SUP1-R-003 | §3 원칙 4, §4 QA Lead |
| ASPICE MAN.3.BP6 (역량 식별) | ASPICE-MAN3-R-004 | §4·§5 (역량/Level 차등) |
| ASPICE PIM.3 Purpose | ASPICE-PIM3-R-001 | §6 평가 주기, §7 PRO-11 |

## 9. 출처 (source_citation)

```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "PA 1.1 ~ PA 3.2 (ISO/IEC 33020 기반)"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/structure.yaml"
  locator: "11 process groups (Primary/Supporting/Organizational)"
  paraphrase_only: true
- type: llm_inference
  basis: "32 프로세스를 통합 거버넌스로 묶기 위한 합성 — 적용요건 §1.10 ASPICE-GOV-R-001 정의"
  retrieved_at: "2026-05-06"
  paraphrase_only: false
```

## 10. 개정 이력

| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — 32 프로세스 거버넌스 정책 정의 | (대기) |
