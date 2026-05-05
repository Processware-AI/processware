---
type: standard-overview
standard: "VWAY_Motors"
title: "Automotive SPICE 4.0 표준 개요 (VWAY Motors 적용)"
version: "4.0"
domain: "SPICE"
layer: "L2_engineering"
structure: "capability_model"
integration_mode: "interface_only"
status: draft
owner: "Process Quality Office"
reviewer: "ASPICE Lead Assessor"
approver: "CTO"
created: 2026-05-06
updated: 2026-05-06
tags: [standard, ASPICE, ASPICE4, automotive, capability-model, VWAY_Motors]
---

# Automotive SPICE 4.0 표준 개요 (VWAY_Motors)

> 상위 기준: [[표준프로세스_구성원칙]] · 문서체계: [[01_문서체계]] · 분류 레지스트리: [[07_표준분류레지스트리]]
> 요구사항 분해: [[적용요건]]

---

## 1. 표준 식별

| 항목 | 값 |
|---|---|
| **표준 코드** | VWAY_Motors / ASPICE 4.0 |
| **정식 명칭(영문)** | Automotive SPICE® Process Reference Model / Process Assessment Model — Version 4.0 |
| **정식 명칭(국문)** | 자동차 SPICE 프로세스 참조 모델 / 프로세스 평가 모델 4.0 |
| **발행기관** | VDA QMC (Verband der Automobilindustrie — Quality Management Center), Working Group 13 |
| **발행일** | 2023-11-29 |
| **국내 대응 표준** | (없음 — 국제 사실상 표준) · 참조: ISO/IEC 33020, ISO/IEC 330xx 시리즈 |
| **관련 법규/표준** | ISO 26262 (기능안전), ISO/SAE 21434 (사이버보안), ISO 21448 (SOTIF), IATF 16949, ISO/IEC IEEE 12207 |
| **영역 코드** | SPICE |
| **레이어** | L2_engineering (capability_model) |
| **통합 모드** | interface_only — 상위 IMS(L1)에 인터페이스로만 결합 |

---

## 2. 적용 범위 (Scope)

VWAY Motors 의 **자동차용 임베디드 시스템·소프트웨어·기계학습·하드웨어 개발 프로젝트**에 대해 ASPICE 4.0 의 **32개 프로세스**를 적용한다. 적용 의도는 다음과 같다.

- **OEM/Tier-1 평가 대응**: 고객사 SOQ(Statement of Quality) 가 요구하는 Capability Level 2~3 달성
- **내부 역량 거버넌스**: 신규 ML/HW 프로세스를 포함한 V-모델 기반 개발 라이프사이클 표준화
- **공급사 모니터링(ACQ.4)**: 외주 개발 산출물의 ASPICE 정합성 보장
- **재사용·플랫폼 전략(REU.2)**: 차종 간 SW/HW/ML 자산 재활용 거버넌스

**적용 제외 / 단계적 도입**
- ACQ.3 (계약 합의), SPL.1 (공급 요구사항 분석), MAN.7 (정보 보안 관리) 등은 v4.0 PRM/PAM 기본 32개에 포함되지 않으므로 **단계 2 확장 후보**.
- MLE 그룹은 ML 컴포넌트가 포함된 프로젝트에 한해 활성화.

---

## 3. 핵심 구조 — 11 프로세스 그룹 / 32 프로세스

ASPICE 4.0 은 **High-Level Structure(HLS)** 가 아닌 **프로세스 참조 모델 + 평가 모델(PRM/PAM)** 구조를 따른다. 따라서 본 표준은 IMS HLS와 **항(Clause)** 매핑이 아니라 **프로세스 그룹(Process Group)** 매핑으로 통합된다.

### 3.1 카테고리별 프로세스 그룹

| 카테고리 | 그룹 코드 | 그룹명 | 프로세스 수 | 주요 프로세스 |
|---|---|---|---|---|
| **Primary Life Cycle** | ACQ | Acquisition | 1 | ACQ.4 |
| Primary Life Cycle | SPL | Supply | 1 | SPL.2 |
| Primary Life Cycle | SYS | System Engineering | 5 | SYS.1~SYS.5 |
| Primary Life Cycle | VAL | Validation | 1 | VAL.1 |
| Primary Life Cycle | SWE | Software Engineering | 6 | SWE.1~SWE.6 |
| Primary Life Cycle | MLE | Machine Learning Engineering ★신규 | 4 | MLE.1~MLE.4 |
| Primary Life Cycle | HWE | Hardware Engineering | 4 | HWE.1~HWE.4 |
| **Supporting** | SUP | Supporting | 5 | SUP.1, SUP.8, SUP.9, SUP.10, SUP.11 |
| **Organizational** | MAN | Management | 3 | MAN.3, MAN.5, MAN.6 |
| Organizational | PIM | Process Improvement | 1 | PIM.3 |
| Organizational | REU | Reuse | 1 | REU.2 |
| **합계** | — | — | **32** | — |

### 3.2 V-모델 매핑 개요

```
[요구사항/엘리시테이션] SYS.1
        ↓
[시스템 요구사항]     SYS.2 ─────────────────────  SYS.5 [시스템 검증]
        ↓                                              ↑
[시스템 아키텍처]     SYS.3 ─────────────  SYS.4 [통합 검증]
        ↓                                              ↑
   ┌────┴────┬──────────┐                  ┌──────────┴──────────┐
SWE.1~6   MLE.1~4    HWE.1~4   ───→   소프트웨어/ML/HW 개별 검증
   │         │          │
   ↓         ↓          ↓
[소프트웨어/ML 모델/하드웨어 단위 구현]

         [VAL.1 — 사용자/운영 환경 검증]
         [SUP.* — QA, 형상관리, 문제·변경 관리, ML 데이터 관리]
         [MAN.* — 프로젝트/리스크/측정]
         [PIM.3 / REU.2 — 조직 차원 개선·재사용]
```

---

## 4. 역량 수준(Capability Level) 및 프로세스 속성(PA)

ASPICE 4.0 은 ISO/IEC 33020 의 6단계 역량 모델을 채택한다. 평가 시 각 PA 의 달성도 N/P/L/F 등급을 합산해 Capability Level 을 결정한다.

| Level | 명칭 | 달성 PA |
|---|---|---|
| **Level 0** | Incomplete | (없음) |
| **Level 1** | Performed | PA 1.1 Process Performance |
| **Level 2** | Managed | PA 2.1 Performance Management + PA 2.2 Work Product Management |
| **Level 3** | Established | PA 3.1 Process Definition + PA 3.2 Process Deployment |
| **Level 4** | Predictable | PA 4.1 Quantitative Analysis + PA 4.2 Quantitative Control |
| **Level 5** | Innovating | PA 5.1 Process Innovation + PA 5.2 Process Innovation Implementation |

VWAY Motors **목표 수준**: 양산 프로젝트 = **Level 2 전체 + 핵심 프로세스(SYS.2/SYS.5/SWE.1/SWE.6/SUP.1/SUP.8/SUP.9/MAN.3) Level 3**.

---

## 5. ASPICE 3.1 → 4.0 주요 변경사항

| 변경 유형 | 항목 | 3.1 | 4.0 | 영향 |
|---|---|---|---|---|
| **삭제** | SUP.2 (Verification) | 존재 | **삭제** | SWE.4/5/6, HWE.3/4 등 각 검증으로 흡수 |
| **신규 그룹** | MLE (Machine Learning Engineering) | — | **신설 4 프로세스** | ML 모델 개발 거버넌스 추가 |
| **신규 프로세스** | SUP.11 (Machine Learning Data Management) | — | **신설** | 학습 데이터 품질·라이선스·개인정보 관리 |
| **명칭 변경** | HWE.3 | "Verification of HW" | **"Verification against Hardware Design"** | 검증 기준 명확화 |
| **명칭 변경** | HWE.4 | (없음/V-side 부재) | **"Verification against HW Requirements"** | HW V-모델 좌우 분리 |
| **재구성** | SWE 그룹 | SWE.1~6 + SUP.2 | SWE.1~6 단독 | 단위 검증·통합 검증 책임 명확화 |
| **재구성** | SYS.4/SYS.5 | "System Integration Test", "System Qualification Test" | "System Integration and Integration Verification", "System Verification" | 명칭의 검증/통합 의미 강화 |
| **강화** | Traceability/Consistency | 권고 톤 | **모든 엔지니어링 프로세스에 명시적 BP** | 양방향 추적성 의무화 |
| **신규 BP 패턴** | "Communicate agreed ..." | 일부 | **모든 출력 산출물에 표준화** | 합의·전달 기록 필수 |

> 출처: `inputs/01_표준원문/VWAY_Motors/structure.yaml` 및 `requirements.yaml` (Purpose/Outcomes/BP 항목 분포 분석).

---

## 6. 타 표준과의 관계 (IMS 통합 관점)

ASPICE 4.0 은 **L2 엔지니어링 표준 (capability_model)** 으로 분류되어, 상위 IMS(L1: ISO 9001/IATF 16949 등)와는 **interface_only** 모드로 결합한다.

| 관련 표준 | 관계 | 통합 인터페이스 |
|---|---|---|
| IATF 16949 | 자동차 QMS 모표준 | ASPICE 결과를 `MAT-002` 규제 대조표에 IATF 8.3(설계개발) 요건과 매핑 |
| ISO 26262 | 기능안전 | ASPICE 산출물(SYS/SWE/HWE) 위에 ASIL 결정·안전요구사항 트레이스 추가 (별도 PRO) |
| ISO/SAE 21434 | 사이버보안 | TARA 결과를 SYS.1/SYS.2 입력으로 결합 |
| ISO 21448 (SOTIF) | 의도된 기능의 안전성 | MLE / VAL.1 입력 강화 |
| ISO/IEC IEEE 12207 | SW 라이프사이클 | ASPICE 가 자동차 도메인 특화로 채택 |

- 공통 MOC: [[MOC_전체표준]]
- 통합 매핑: [[MAT-002_규제요구사항_대조표]]

---

## 7. 입력자료(`inputs/`) 인벤토리

| 파일 | 카테고리 | 출처 | 라이선스 | 비고 |
|---|---|---|---|---|
| `inputs/01_표준원문/VWAY_Motors/structure.yaml` | 표준원문(구조) | VDA QMC | © VDA QMC — 내부 paraphrase only | 11 그룹 / 32 프로세스 |
| `inputs/01_표준원문/VWAY_Motors/requirements.yaml` | 표준원문(요건) | VDA QMC | © VDA QMC — 내부 paraphrase only | 407건 (Purpose 32 + OC 181 + BP 194) |
| `inputs/01_표준원문/VWAY_Motors/clauses.md` | 표준원문(전문) | VDA QMC | © VDA QMC — verbatim, 직접 인용 금지 | content_mode: verbatim |
| `inputs/01_표준원문/VWAY_Motors/definitions.yaml` | 표준원문(용어) | VDA QMC | © VDA QMC — 내부 참조 only | 핵심 용어 10건 |
| `inputs/01_표준원문/VWAY_Motors/annexes.yaml` | 표준원문(부속서) | VDA QMC | © VDA QMC — 내부 참조 only | Annex A~D |

- 입력자료 규칙: [[05_입력자료_규칙]]
- 라이선스 가드: 본 문서 및 후속 산출물에서 ASPICE 원문 20단어 이상 연속 인용 금지, paraphrase 만 허용.

---

## 8. 산출물 링크

| 유형 | 링크 |
|---|---|
| 요구사항 분해 | [[적용요건]] |
| 정책(POL) — 역량 거버넌스 | (Phase 2 design 단계에서 생성) |
| 절차(PRO) — 프로세스 그룹별 32개 | (Phase 2 design 단계에서 생성) |
| 추적성(MAT) | [[MAT-011_VWAY_Motors_추적성]] (예정) · [[MAT-002_규제요구사항_대조표]] |
| 참고자료(REF) | (필요 시 후속 단계에서 추가) |
| MOC | [[MOC_전체표준]] |

---

## 9. 해석 노트

- **"Capability Model" vs "Management System Model"**: ASPICE 는 "이 프로세스를 얼마나 잘 수행하는가"를 평가하는 모델이며, ISO 9001 식의 "조직이 무엇을 해야 하는가"와는 결이 다르다. 따라서 **POL 은 최소화**(역량 거버넌스 1건)하고, **PRO 는 32개 프로세스 단위로 1:1** 또는 **그룹 단위 묶음**으로 매핑한다.
- **Outcome vs Base Practice**: Outcome 은 결과 상태(WHAT), BP 는 그 결과를 달성하는 권장 활동(HOW). 본 적용요건에서는 **Outcome 을 검증 기준**, **BP 를 절차 단계**로 분리 매핑한다.
- **MLE 도입 정책**: 모든 신규 프로젝트의 MLE 활성 여부는 MAN.3 프로젝트 계획 단계에서 결정하고 그 결정 자체를 기록한다.

---

## 10. 미해결 이슈 (Open Issue)

- [ ] ACQ.3, SPL.1, MAN.7 등 ASPICE 3.1 이전부터 존재했던 프로세스의 단계 2 확장 여부 확정 필요
- [ ] PA 4/5 (Predictable/Innovating) 도입 로드맵은 Phase 2 design 후 별도 문서화
- [ ] MLE.1~4 의 학습데이터 거버넌스(SUP.11) 와 GDPR/개인정보보호법 정합성 검토 필요

---

## 11. 참고 문헌

- VDA QMC, *Automotive SPICE® Process Assessment / Reference Model — Version 4.0*, 2023-11-29.
- ISO/IEC 33020:2019, *Information technology — Process assessment — Process measurement framework for assessment of process capability*.
- ISO/IEC IEEE 12207:2017, *Systems and software engineering — Software life cycle processes*.
- ISO 26262 series, *Road vehicles — Functional safety*.
- ISO/SAE 21434:2021, *Road vehicles — Cybersecurity engineering*.
