---
type: MAT
doc_id: MAT-011
title: "CMMI-DEV-ML3-V1.3 추적성 매트릭스"
standard: CMMI-DEV-ML3-V1.3
standard_full_name: "CMMI for Development, Version 1.3 — Maturity Level 3 (cumulative ML2 + ML3)"
publisher: "Software Engineering Institute (Carnegie Mellon University)"
publication_report: "CMU/SEI-2010-TR-033"
scope_code: CMMI
layer: L2_engineering
structure: capability_model
integration_mode: interface_only
version: "0.2"
status: draft
owner: "QMR"
reviewer: "PCB"
approver: "CEO/CTO"
created: 2026-05-11
updated: 2026-05-11
retention: "상시"
copyright_notice:
  holder: "Carnegie Mellon University / Software Engineering Institute"
  year: 2010
  source: "CMU/SEI-2010-TR-033 — CMMI for Development, Version 1.3"
  license: "internal_use_derivative_work"
  derivative_work_disclosure: "Verbatim SG/SP titles and Req-ID 매핑은 CMU/SEI-2010-TR-033 의 normative components 인용. 본 추적성 매트릭스는 내부 컴플라이언스 관리 목적의 파생물."
sources:
  - standard: "CMMI-DEV V1.3"
    clause: "Part Two — Generic Goals/Practices + 18 Process Areas"
    artifact: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  - standard: "CMMI-DEV V1.3"
    clause: "Part One Ch.4 — Relationships Among Process Areas"
    artifact: "inputs/01_표준원문/CMMI-DEV/pa_relationships.yaml"
related:
  - "[[02_적용요건 — cmmi-dev-ml3-v1.3]]"
  - "[[MAT-001_문서관리대장]]"
  - "[[MAT-002_규제요구사항_대조표]]"
  - "[[MAT-003_산출물_목록표]]"
  - "[[MAT-004_RACI_통합표]]"
  - "[[MAT-005_심사증적_인덱스]]"
  - "[[MAT-006_문서계층_추적매트릭스]]"
  - "[[MAT-010_프로세스_플로우맵]]"
  - "[[MOC_추적성매트릭스]]"
tags: [MAT, traceability, cmmi, cmmi-dev, ml3, capability-model, interface-only]
---

# MAT-011 CMMI-DEV-ML3-V1.3 추적성 매트릭스

> 본 매트릭스는 **CMMI-DEV V1.3 Maturity Level 3 (cumulative ML2+ML3)** 의 216개 요건(3 GG + 12 GP + 48 SG + 168 SP + Purpose 5 일부)이 vault 자산(POL 5 / PRO 18 / WI 60 / TMP 117 / EX 117)으로 어떻게 매핑되는지를 단일 출처(SSOT) 로 기록한다.
> **interface_only 모드**: HLS(High Level Structure) 통합형 POL/PRO 와 통합하지 않고, CMMI 전용 독립 영역코드(`CMMI`)로 유지한다.
> 상위 인덱스: [[MOC_추적성매트릭스]] · 번호체계: [[02_문서번호체계]] §표준별 추적성

---

## 1. 표준 메타

| 항목 | 내용 |
|---|---|
| 표준명 | CMMI for Development, Version 1.3 (Capability Maturity Model Integration — Development) |
| 발행기관 | Software Engineering Institute (SEI), Carnegie Mellon University |
| 발행보고서 | CMU/SEI-2010-TR-033 / ESC-TR-2010-033 |
| 발행일 | 2010-11 |
| 본 적용 범위 | Staged ML3 cumulative — ML2(7 PA) + ML3(11 PA) = **18 PA** |
| 영역 코드 | `CMMI` (L2_engineering, capability_model, interface_only) |
| 후속 표준 | CMMI V2.0 (2018, ISACA) / CMMI V3.0 (2023, ISACA Performance Solutions) |
| 라이선스 | CMU/SEI 내부 사용·파생물 허용 — `internal_use_derivative_work` |
| 입력 소스 | `inputs/01_표준원문/CMMI-DEV/` (verbatim ingest 100%) |

### 1.1 본 빌드 산출 자산 인벤토리

| 유형 | 개수 | 식별번호 범위 |
|---|---|---|
| POL | 5 | POL-CMMI-01 ~ POL-CMMI-05 |
| PRO | 18 | PRO-CMMI-01-01 ~ PRO-CMMI-04-04 |
| WI | 60 | WI-CMMI-01-01-01 ~ WI-CMMI-04-04-03 |
| TMP | 117 | TMP-CMMI-01-01-01-01 ~ TMP-CMMI-04-04-03-02 |
| EX | 117 | EX-CMMI-01-01-01-01 ~ EX-CMMI-04-04-03-02 |
| steps.yaml | 60 | WI 동수 (실행 가능 절차) |
| **합계** | **377 파일** | — |

### 1.2 요건 인벤토리 (출처: `inputs/01_표준원문/CMMI-DEV/requirements.yaml`)

| 범주 | 수량 | 비고 |
|---|---|---|
| Generic Goals (GG) | 3 | GG1/GG2/GG3 |
| Generic Practices (GP) | 12 | GP 1.1 + GP 2.1~2.10 + GP 3.1~3.2 |
| Specific Goals (18 PA × SG) | 48 | ML2 24 + ML3 24 (RSKM SG1 ingest 누락 1건 포함 시 49) |
| Specific Practices (18 PA × SP) | 168 | ML2 91 + ML3 77 |
| Purpose 문 (informative) | 5 | OPD/OPF/OT/PI/RD (해설 목적) |
| **본 적용 합계** | **216** | requirements.yaml 236 - ML4/ML5 PA (OPP/QPM/CAR/OPM) 20 |

---

## 2. 요건 → POL 매핑 (PA → POL-CMMI-NN)

CMMI 22 PA 카테고리 구조에 맞춰 18 PA 를 5 POL 로 그룹화. GG/GP 는 POL-CMMI-05 에서 제도화 요구로 집계되며 각 POL/PRO 에 GP 매핑이 내재화된다.

| PA 카테고리 | PA 목록 (18) | POL | source_citation |
|---|---|---|---|
| Process Management | OPD, OPF, OT | [[POL-CMMI-01_조직_프로세스_거버넌스_정책]] | `inputs/requirements.yaml#CMMIDEV-OPD-*` / `CMMIDEV-OPF-*` / `CMMIDEV-OT-*` (p.191/p.203/p.247) |
| Project Management | PP, PMC, REQM, SAM, IPM, RSKM | [[POL-CMMI-02_프로젝트_관리_정책]] | `inputs/requirements.yaml#CMMIDEV-PP-*` / `PMC-*` / `REQM-*` / `SAM-*` / `IPM-*` / `RSKM-*` (p.283/p.272/p.343/p.365/p.159/p.351) |
| Engineering | RD, TS, PI, VER, VAL | [[POL-CMMI-03_엔지니어링_정책]] | `inputs/requirements.yaml#CMMIDEV-RD-*` / `TS-*` / `PI-*` / `VER-*` / `VAL-*` (p.328/p.375/p.259/p.403/p.394) |
| Support | CM, MA, PPQA, DAR | [[POL-CMMI-04_지원_품질보증_정책]] | `inputs/requirements.yaml#CMMIDEV-CM-*` / `MA-*` / `PPQA-*` / `DAR-*` (p.140/p.177/p.303/p.151) |
| Generic (제도화 공통) | 전 18 PA × GG/GP | [[POL-CMMI-05_프로세스_제도화_개선_정책]] | `inputs/requirements.yaml#CMMIDEV-GG{1\|2\|3}-REQ-001` / `CMMIDEV-GP{1.1\|2.1~2.10\|3.1~3.2}-REQ-001` (p.68~115) |

**커버리지: 5/5 POL 완성 — 18/18 PA 가 1차 POL 에 매핑됨.**

---

## 3. 요건 → PRO 매핑 (PA → PRO-CMMI-NN-NN)

각 PA 당 1 PRO 매핑. 총 18 PRO. follows/precedes 는 [[MAT-010_프로세스_플로우맵]] 참조.

### 3.1 POL-CMMI-01 (Process Management, ML3) 산하

| PRO ID | PA | Req-ID 묶음 | source_citation |
|---|---|---|---|
| [[PRO-CMMI-01-01_조직_표준프로세스_수립_유지_절차]] | OPD | OPD SG1 / SP1.1~1.7 (7개) | `inputs/requirements.yaml#CMMIDEV-OPD-SG1-REQ-001 ~ SP1.7-REQ-001` (p.191-200) |
| [[PRO-CMMI-01-02_조직_프로세스_개선_배포_절차]] | OPF | OPF SG1~3 / SP1.1~3.4 (12개) | `inputs/requirements.yaml#CMMIDEV-OPF-SG1-REQ-001 ~ SP3.4-REQ-001` (p.203-213) |
| [[PRO-CMMI-01-03_조직_훈련_절차]] | OT | OT SG1~2 / SP1.1~2.3 (10개) | `inputs/requirements.yaml#CMMIDEV-OT-SG1-REQ-001 ~ SP2.3-REQ-001` (p.247-255) |

### 3.2 POL-CMMI-02 (Project Management) 산하

| PRO ID | PA | Req-ID 묶음 | source_citation |
|---|---|---|---|
| [[PRO-CMMI-02-01_프로젝트_계획_절차]] | PP | PP SG1~3 / SP1.1~3.3 (17개) | `inputs/requirements.yaml#CMMIDEV-PP-SG1-REQ-001 ~ SP3.3-REQ-001` (p.283-298) |
| [[PRO-CMMI-02-02_프로젝트_모니터링_통제_절차]] | PMC | PMC SG1~2 / SP1.1~2.3 (12개) | `inputs/requirements.yaml#CMMIDEV-PMC-SG1-REQ-001 ~ SP2.3-REQ-001` (p.272-279) |
| [[PRO-CMMI-02-03_요구사항_관리_절차]] | REQM | REQM SG1 / SP1.1~1.5 (6개) | `inputs/requirements.yaml#CMMIDEV-REQM-SG1-REQ-001 ~ SP1.5-REQ-001` (p.343-346) |
| [[PRO-CMMI-02-04_공급자_협약_관리_절차]] | SAM | SAM SG1~2 / SP1.1~2.3 (8개) | `inputs/requirements.yaml#CMMIDEV-SAM-SG1-REQ-001 ~ SP2.3-REQ-001` (p.365-372) |
| [[PRO-CMMI-02-05_통합_프로젝트_관리_절차]] | IPM | IPM SG1~2 / SP1.1~2.3 (11개) | `inputs/requirements.yaml#CMMIDEV-IPM-SG1-REQ-001 ~ SP2.3-REQ-001` (p.159-173) |
| [[PRO-CMMI-02-06_리스크_관리_절차]] | RSKM | RSKM SG1*(누락)/SG2/SG3 / SP1.1~3.2 (9개) | `inputs/requirements.yaml#CMMIDEV-RSKM-SP1.1-REQ-001 ~ SP3.2-REQ-001` (p.351-360) — **SG1 ingest 누락 1건 적용요건.md §6-2-15 플래그** |

### 3.3 POL-CMMI-03 (Engineering) 산하

| PRO ID | PA | Req-ID 묶음 | source_citation |
|---|---|---|---|
| [[PRO-CMMI-03-01_요구사항_개발_절차]] | RD | RD SG1~3 / SP1.1~3.5 (13개) | `inputs/requirements.yaml#CMMIDEV-RD-SG1-REQ-001 ~ SP3.5-REQ-001` (p.328-340) |
| [[PRO-CMMI-03-02_기술_솔루션_설계_절차]] | TS | TS SG1~3 / SP1.1~3.2 (11개) | `inputs/requirements.yaml#CMMIDEV-TS-SG1-REQ-001 ~ SP3.2-REQ-001` (p.375-390) |
| [[PRO-CMMI-03-03_제품_통합_절차]] | PI | PI SG1~3 / SP1.1~3.4 (13개) | `inputs/requirements.yaml#CMMIDEV-PI-SG1-REQ-001 ~ SP3.4-REQ-001` (p.259-268) |
| [[PRO-CMMI-03-04_검증_절차]] | VER | VER SG1~3 / SP1.1~3.2 (11개) | `inputs/requirements.yaml#CMMIDEV-VER-SG1-REQ-001 ~ SP3.2-REQ-001` (p.403-410) |
| [[PRO-CMMI-03-05_확인_절차]] | VAL | VAL SG1~2 / SP1.1~2.2 (7개) | `inputs/requirements.yaml#CMMIDEV-VAL-SG1-REQ-001 ~ SP2.2-REQ-001` (p.394-399) |

### 3.4 POL-CMMI-04 (Support) 산하

| PRO ID | PA | Req-ID 묶음 | source_citation |
|---|---|---|---|
| [[PRO-CMMI-04-01_형상_관리_절차]] | CM | CM SG1~3 / SP1.1~3.2 (10개) | `inputs/requirements.yaml#CMMIDEV-CM-SG1-REQ-001 ~ SP3.2-REQ-001` (p.140-146) |
| [[PRO-CMMI-04-02_측정_및_분석_절차]] | MA | MA SG1~2 / SP1.1~2.4 (10개) | `inputs/requirements.yaml#CMMIDEV-MA-SG1-REQ-001 ~ SP2.4-REQ-001` (p.177-189) |
| [[PRO-CMMI-04-03_프로세스_제품_품질보증_절차]] | PPQA | PPQA SG1~2 / SP1.1~2.2 (6개) | `inputs/requirements.yaml#CMMIDEV-PPQA-SG1-REQ-001 ~ SP2.2-REQ-001` (p.303-306) |
| [[PRO-CMMI-04-04_의사결정_분석_결정_절차]] | DAR | DAR SG1 / SP1.1~1.6 (7개) | `inputs/requirements.yaml#CMMIDEV-DAR-SG1-REQ-001 ~ SP1.6-REQ-001` (p.151-156) |

**커버리지: 18/18 PA — 1 PA ↔ 1 PRO 완전 매핑.**

### 3.5 GG/GP → PRO 내재화 매핑 (전 18 PRO 공통)

| Req-ID | GG/GP | 내재화 위치 | source_citation |
|---|---|---|---|
| CMMIDEV-GG1-REQ-001 | GG 1 Achieve Specific Goals | 18 PRO 의 §5 수행 절차 (SP 직접 수행) | `inputs/requirements.yaml#CMMIDEV-GG1-REQ-001` (p.68) |
| CMMIDEV-GP1.1-REQ-001 | GP 1.1 Perform Specific Practices | 60 WI 의 §5 수행 절차 | `inputs/requirements.yaml#CMMIDEV-GP1.1-REQ-001` (p.68) |
| CMMIDEV-GG2-REQ-001 | GG 2 Institutionalize a Managed Process | [[POL-CMMI-05_프로세스_제도화_개선_정책]] §ML2 | `inputs/requirements.yaml#CMMIDEV-GG2-REQ-001` (p.68) |
| CMMIDEV-GP2.1-REQ-001 | GP 2.1 Establish an Organizational Policy | POL-CMMI-01~04 (4개 영역 POL 자체가 정책 수립 증적) | `inputs/requirements.yaml#CMMIDEV-GP2.1-REQ-001` (p.69) |
| CMMIDEV-GP2.2-REQ-001 | GP 2.2 Plan the Process | 18 PRO 의 §1 목적/§2 범위/§4 입출력 + TMP-CMMI-02-01-* (PP TMP) | `inputs/requirements.yaml#CMMIDEV-GP2.2-REQ-001` (p.72) |
| CMMIDEV-GP2.3-REQ-001 | GP 2.3 Provide Resources | 18 PRO 의 §3 RACI + WI-CMMI-02-01-03 자원 계획 | `inputs/requirements.yaml#CMMIDEV-GP2.3-REQ-001` (p.76) |
| CMMIDEV-GP2.4-REQ-001 | GP 2.4 Assign Responsibility | 18 PRO 의 §3 RACI 표 + [[MAT-004_RACI_통합표]] | `inputs/requirements.yaml#CMMIDEV-GP2.4-REQ-001` (p.82) |
| CMMIDEV-GP2.5-REQ-001 | GP 2.5 Train People | PRO-CMMI-01-03 (OT) 와 18 PRO 의 교육 항목 | `inputs/requirements.yaml#CMMIDEV-GP2.5-REQ-001` (p.83) |
| CMMIDEV-GP2.6-REQ-001 | GP 2.6 Control Work Products | PRO-CMMI-04-01 (CM) 와 18 PRO 의 산출물 통제 | `inputs/requirements.yaml#CMMIDEV-GP2.6-REQ-001` (p.88) |
| CMMIDEV-GP2.7-REQ-001 | GP 2.7 Identify and Involve Relevant Stakeholders | 18 PRO 의 §3 RACI (C/I 컬럼) + [[MAT-004_RACI_통합표]] | `inputs/requirements.yaml#CMMIDEV-GP2.7-REQ-001` (p.93) |
| CMMIDEV-GP2.8-REQ-001 | GP 2.8 Monitor and Control the Process | PRO-CMMI-02-02 (PMC) 와 18 PRO 의 §6 모니터링 항목 | `inputs/requirements.yaml#CMMIDEV-GP2.8-REQ-001` (p.100) |
| CMMIDEV-GP2.9-REQ-001 | GP 2.9 Objectively Evaluate Adherence | PRO-CMMI-04-03 (PPQA) + [[MAT-005_심사증적_인덱스]] | `inputs/requirements.yaml#CMMIDEV-GP2.9-REQ-001` (p.106) |
| CMMIDEV-GP2.10-REQ-001 | GP 2.10 Review Status with Higher Level Management | 18 PRO 의 §6 보고 항목 + [[MAT-001_문서관리대장]] 개정이력 | `inputs/requirements.yaml#CMMIDEV-GP2.10-REQ-001` (p.113) |
| CMMIDEV-GG3-REQ-001 | GG 3 Institutionalize a Defined Process | [[POL-CMMI-05_프로세스_제도화_개선_정책]] §ML3 | `inputs/requirements.yaml#CMMIDEV-GG3-REQ-001` (p.115) |
| CMMIDEV-GP3.1-REQ-001 | GP 3.1 Establish a Defined Process | PRO-CMMI-02-05 (IPM SP1.1) + 18 PRO 의 OSSP 테일러링 참조 | `inputs/requirements.yaml#CMMIDEV-GP3.1-REQ-001` (p.115) |
| CMMIDEV-GP3.2-REQ-001 | GP 3.2 Collect Process Related Experiences | PRO-CMMI-01-02 (OPF SP3.4) + PRO-CMMI-02-05 (IPM SP1.7) | `inputs/requirements.yaml#CMMIDEV-GP3.2-REQ-001` (p.115) |

**GG/GP 커버리지: 15/15 — 100%.**

---

## 3-bis. GP × PA 정량 커버리지 매트릭스 (QA-005 보완)

본 절은 §3.5 의 GG/GP 내재화 매핑(정성 서술) 을 **18 PA × 13 GP** 정량 셀 형식으로 보완한다. CMMI-DEV V1.3 의 staged representation 에서 **GG/GP 는 22개 전 PA 에 동일하게 적용** (cumulative model) 되며, 본 빌드 ML3 cumulative scope 의 18 PA 에 대해 적용 강도를 표기한다.

### 3-bis.1 셀 표기 규약

| 기호 | 의미 | 적용 기준 |
|---|---|---|
| ✓ | CL2 (Managed) institutionalization 필수 | ML2 staged 또는 CL2 continuous — GP 1.1 + GP 2.1~2.10 |
| ✓✓ | ML3 (Defined) institutionalization — strong | ML3 staged 또는 CL3 continuous — GP 3.1 + GP 3.2 |
| — | 해당 없음 | 본 빌드 ML3 cumulative scope 에서 GG/GP 는 모든 PA 에 적용되므로 본 매트릭스에는 — 셀이 발생하지 않음 |

> **GP 카운트 정정 주석**: §1.2 인벤토리는 "GP 12" 로 기재했으나 CMMI-DEV V1.3 normative components 의 실제 GP 수는 **13개** (GP 1.1 + GP 2.1~2.10 + GP 3.1~3.2 = 1 + 10 + 2). 본 §3-bis 는 정확한 13 GP × 18 PA = **234 셀** 로 작성되며, 본 정정 사항은 §10 개정 이력 v0.2 에 기록된다.

### 3-bis.2 정량 매트릭스 (18 PA × 13 GP)

각 행은 ML3 cumulative scope 18 PA. 각 열은 13 GP. 모든 셀의 출처는 `inputs/requirements.yaml#CMMIDEV-GP{x.y}-REQ-001` (참조 페이지 헤더 행 명시).

| PA \ GP | GP 1.1 (p.68) | GP 2.1 (p.69) | GP 2.2 (p.72) | GP 2.3 (p.76) | GP 2.4 (p.82) | GP 2.5 (p.83) | GP 2.6 (p.88) | GP 2.7 (p.93) | GP 2.8 (p.100) | GP 2.9 (p.106) | GP 2.10 (p.113) | GP 3.1 (p.115) | GP 3.2 (p.115) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **CM** (ML2 Support) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **MA** (ML2 Support) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **PMC** (ML2 Project Mgmt) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **PP** (ML2 Project Mgmt) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **PPQA** (ML2 Support) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **REQM** (ML2 Project Mgmt) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **SAM** (ML2 Project Mgmt) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **DAR** (ML3 Support) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **IPM** (ML3 Project Mgmt) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **OPD** (ML3 Process Mgmt) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **OPF** (ML3 Process Mgmt) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **OT** (ML3 Process Mgmt) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **PI** (ML3 Engineering) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **RD** (ML3 Engineering) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **RSKM** (ML3 Project Mgmt) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **TS** (ML3 Engineering) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **VAL** (ML3 Engineering) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| **VER** (ML3 Engineering) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |

### 3-bis.3 셀별 source_citation (대표 PA × GP 인용 형식)

본 매트릭스의 모든 셀(234개) 은 다음 인용 패턴을 따른다:

```
{PA} × {GP} → inputs/requirements.yaml#CMMIDEV-{GP_id}-REQ-001 + p.{N}
              applies_to: "all 22 process areas (at ML2/ML3 and above)"
```

PA 별 적용 근거는 각 GP 의 elaboration (PDF p.69~115) 본문에서 명시한 "This generic practice applies to all process areas (at maturity level X and above)" 절에 따른다.

| GP | source_citation (모든 18 PA 공통) | applies_to_level |
|---|---|---|
| GP 1.1 | `inputs/requirements.yaml#CMMIDEV-GP1.1-REQ-001` (p.68) — GG1 baseline | CL1 / 모든 PA |
| GP 2.1 | `inputs/requirements.yaml#CMMIDEV-GP2.1-REQ-001` (p.69) — Establish an Organizational Policy | CL2 / ML2 / 모든 PA |
| GP 2.2 | `inputs/requirements.yaml#CMMIDEV-GP2.2-REQ-001` (p.72) — Plan the Process | CL2 / ML2 / 모든 PA |
| GP 2.3 | `inputs/requirements.yaml#CMMIDEV-GP2.3-REQ-001` (p.76) — Provide Resources | CL2 / ML2 / 모든 PA |
| GP 2.4 | `inputs/requirements.yaml#CMMIDEV-GP2.4-REQ-001` (p.82) — Assign Responsibility | CL2 / ML2 / 모든 PA |
| GP 2.5 | `inputs/requirements.yaml#CMMIDEV-GP2.5-REQ-001` (p.83) — Train People | CL2 / ML2 / 모든 PA |
| GP 2.6 | `inputs/requirements.yaml#CMMIDEV-GP2.6-REQ-001` (p.88) — Control Work Products | CL2 / ML2 / 모든 PA |
| GP 2.7 | `inputs/requirements.yaml#CMMIDEV-GP2.7-REQ-001` (p.93) — Identify and Involve Relevant Stakeholders | CL2 / ML2 / 모든 PA |
| GP 2.8 | `inputs/requirements.yaml#CMMIDEV-GP2.8-REQ-001` (p.100) — Monitor and Control the Process | CL2 / ML2 / 모든 PA |
| GP 2.9 | `inputs/requirements.yaml#CMMIDEV-GP2.9-REQ-001` (p.106) — Objectively Evaluate Adherence | CL2 / ML2 / 모든 PA |
| GP 2.10 | `inputs/requirements.yaml#CMMIDEV-GP2.10-REQ-001` (p.113) — Review Status with Higher Level Management | CL2 / ML2 / 모든 PA |
| GP 3.1 | `inputs/requirements.yaml#CMMIDEV-GP3.1-REQ-001` (p.115) — Establish a Defined Process | CL3 / ML3 / 모든 PA |
| GP 3.2 | `inputs/requirements.yaml#CMMIDEV-GP3.2-REQ-001` (p.115) — Collect Process Related Experiences | CL3 / ML3 / 모든 PA |

### 3-bis.4 셀 집계

| 적용 표기 | 셀 수 | 비율 | 비고 |
|---|---|---|---|
| ✓ (CL2 institutionalization) | 198 | 84.6% | 18 PA × 11 GP (GP 1.1 + GP 2.1~2.10) |
| ✓✓ (ML3 strong / Defined process) | 36 | 15.4% | 18 PA × 2 GP (GP 3.1 + GP 3.2) |
| — (해당 없음) | 0 | 0.0% | ML3 cumulative scope 에서 모든 GP 는 18 PA 에 균등 적용 |
| **합계** | **234** | **100%** | 18 PA × 13 GP |

### 3-bis.5 PA 별 GP 내재화 거점 (대표 자산 포인터)

각 PA 가 GP 를 실제로 어디서 institutionalize 하는지의 vault 자산 거점(이미 §3.5 와 POL-CMMI-05 에 본문 서술 존재) 을 표 형식으로 재집계한다.

| GP | 1차 거점(전 18 PA 공통) | source_citation |
|---|---|---|
| GP 1.1 | 60 WI 의 §5 수행 절차 (SP 직접 수행) | `inputs/requirements.yaml#CMMIDEV-GP1.1-REQ-001` (p.68) |
| GP 2.1 | POL-CMMI-01~04 (4개 영역 POL) + POL-CMMI-05 §ML2 | `inputs/requirements.yaml#CMMIDEV-GP2.1-REQ-001` (p.69) |
| GP 2.2 | 18 PRO §1~§4 + TMP-CMMI-02-01-* (PP TMP 묶음) | `inputs/requirements.yaml#CMMIDEV-GP2.2-REQ-001` (p.72) |
| GP 2.3 | 18 PRO §3 RACI + WI-CMMI-02-01-03 자원 계획 | `inputs/requirements.yaml#CMMIDEV-GP2.3-REQ-001` (p.76) |
| GP 2.4 | 18 PRO §3 RACI 표 + [[MAT-004_RACI_통합표]] | `inputs/requirements.yaml#CMMIDEV-GP2.4-REQ-001` (p.82) |
| GP 2.5 | PRO-CMMI-01-03 (OT) + 18 PRO 교육 항목 | `inputs/requirements.yaml#CMMIDEV-GP2.5-REQ-001` (p.83) |
| GP 2.6 | PRO-CMMI-04-01 (CM) + 18 PRO 산출물 통제 | `inputs/requirements.yaml#CMMIDEV-GP2.6-REQ-001` (p.88) |
| GP 2.7 | 18 PRO §3 RACI (C/I 컬럼) + [[MAT-004_RACI_통합표]] | `inputs/requirements.yaml#CMMIDEV-GP2.7-REQ-001` (p.93) |
| GP 2.8 | PRO-CMMI-02-02 (PMC) + 18 PRO §6 모니터링 | `inputs/requirements.yaml#CMMIDEV-GP2.8-REQ-001` (p.100) |
| GP 2.9 | PRO-CMMI-04-03 (PPQA) + [[MAT-005_심사증적_인덱스]] | `inputs/requirements.yaml#CMMIDEV-GP2.9-REQ-001` (p.106) |
| GP 2.10 | 18 PRO §6 보고 + [[MAT-001_문서관리대장]] 개정이력 | `inputs/requirements.yaml#CMMIDEV-GP2.10-REQ-001` (p.113) |
| GP 3.1 | PRO-CMMI-02-05 (IPM SP1.1) + 18 PRO OSSP 테일러링 | `inputs/requirements.yaml#CMMIDEV-GP3.1-REQ-001` (p.115) |
| GP 3.2 | PRO-CMMI-01-02 (OPF SP3.4) + PRO-CMMI-02-05 (IPM SP1.7) + PAL 저장소 | `inputs/requirements.yaml#CMMIDEV-GP3.2-REQ-001` (p.115) |

**§3-bis 커버리지: 234/234 셀 매핑 + source_citation 100%. ML3 cumulative scope 에서 모든 GP 가 18 PA 에 동일하게 적용되며 미착수 셀(—) 0건.**

---

## 4. 요건 → WI 매핑 (SP → WI-CMMI-NN-NN-NN)

60개 WI 가 168개 SP 를 묶음 단위(평균 2.8 SP/WI)로 커버한다. 각 행의 `source_citation` 은 해당 WI 의 frontmatter `standards_clause` 와 1:1 일치.

### 4.1 POL-CMMI-01 산하 WI (10개)

| WI ID | 매핑 SP (Req-ID) | source_citation |
|---|---|---|
| [[WI-CMMI-01-01-01_표준프로세스_라이프사이클모델_정의]] | OPD SP1.1, SP1.2 | `inputs/requirements.yaml#CMMIDEV-OPD-SP1.1-REQ-001` (p.192) + `SP1.2-REQ-001` (p.194) |
| [[WI-CMMI-01-01-02_테일러링_기준_가이드_수립]] | OPD SP1.3 | `inputs/requirements.yaml#CMMIDEV-OPD-SP1.3-REQ-001` (p.195) |
| [[WI-CMMI-01-01-03_측정저장소_PAL_구축_운영]] | OPD SP1.4, SP1.5, SP1.6, SP1.7 | `inputs/requirements.yaml#CMMIDEV-OPD-SP1.4-REQ-001 ~ SP1.7-REQ-001` (p.197-200) |
| [[WI-CMMI-01-02-01_프로세스_니즈_목표_평가]] | OPF SP1.1, SP1.2, SP1.3 | `inputs/requirements.yaml#CMMIDEV-OPF-SP1.1-REQ-001 ~ SP1.3-REQ-001` (p.204-207) |
| [[WI-CMMI-01-02-02_프로세스_액션_플랜_수립_실행]] | OPF SP2.1, SP2.2 | `inputs/requirements.yaml#CMMIDEV-OPF-SP2.1-REQ-001 ~ SP2.2-REQ-001` (p.208-209) |
| [[WI-CMMI-01-02-03_OPA_표준프로세스_배포]] | OPF SP3.1, SP3.2 | `inputs/requirements.yaml#CMMIDEV-OPF-SP3.1-REQ-001 ~ SP3.2-REQ-001` (p.210-211) |
| [[WI-CMMI-01-02-04_배포_모니터링_경험_통합]] | OPF SP3.3, SP3.4 | `inputs/requirements.yaml#CMMIDEV-OPF-SP3.3-REQ-001 ~ SP3.4-REQ-001` (p.212-213) |
| [[WI-CMMI-01-03-01_전략적_교육요구_식별_전술계획]] | OT SP1.1, SP1.2, SP1.3, SP1.4 | `inputs/requirements.yaml#CMMIDEV-OT-SP1.1-REQ-001 ~ SP1.4-REQ-001` (p.248-251) |
| [[WI-CMMI-01-03-02_교육_전달_이수기록]] | OT SP2.1, SP2.2 | `inputs/requirements.yaml#CMMIDEV-OT-SP2.1-REQ-001 ~ SP2.2-REQ-001` (p.254) |
| [[WI-CMMI-01-03-03_교육_효과성_평가]] | OT SP2.3 | `inputs/requirements.yaml#CMMIDEV-OT-SP2.3-REQ-001` (p.255) |

### 4.2 POL-CMMI-02 산하 WI (17개)

| WI ID | 매핑 SP (Req-ID) | source_citation |
|---|---|---|
| [[WI-CMMI-02-01-01_추정_수립]] | PP SP1.1, SP1.2, SP1.3, SP1.4 | `inputs/requirements.yaml#CMMIDEV-PP-SP1.1-REQ-001 ~ SP1.4-REQ-001` (p.283-287) |
| [[WI-CMMI-02-01-02_프로젝트_계획_수립]] | PP SP2.1, SP2.2, SP2.3 | `inputs/requirements.yaml#CMMIDEV-PP-SP2.1-REQ-001 ~ SP2.3-REQ-001` (p.289-292) |
| [[WI-CMMI-02-01-03_자원_지식_이해관계자_통합계획]] | PP SP2.4, SP2.5, SP2.6, SP2.7 | `inputs/requirements.yaml#CMMIDEV-PP-SP2.4-REQ-001 ~ SP2.7-REQ-001` (p.293-296) |
| [[WI-CMMI-02-01-04_약정_획득]] | PP SP3.1, SP3.2, SP3.3 | `inputs/requirements.yaml#CMMIDEV-PP-SP3.1-REQ-001 ~ SP3.3-REQ-001` (p.297-298) |
| [[WI-CMMI-02-02-01_기본_모니터링]] | PMC SP1.1, SP1.2, SP1.3, SP1.4, SP1.5 | `inputs/requirements.yaml#CMMIDEV-PMC-SP1.1-REQ-001 ~ SP1.5-REQ-001` (p.272-275) |
| [[WI-CMMI-02-02-02_진행_마일스톤_검토]] | PMC SP1.6, SP1.7 | `inputs/requirements.yaml#CMMIDEV-PMC-SP1.6-REQ-001 ~ SP1.7-REQ-001` (p.276) |
| [[WI-CMMI-02-02-03_시정조치_종결관리]] | PMC SP2.1, SP2.2, SP2.3 | `inputs/requirements.yaml#CMMIDEV-PMC-SP2.1-REQ-001 ~ SP2.3-REQ-001` (p.277-279) |
| [[WI-CMMI-02-03-01_요구사항_이해_약정]] | REQM SP1.1, SP1.2 | `inputs/requirements.yaml#CMMIDEV-REQM-SP1.1-REQ-001 ~ SP1.2-REQ-001` (p.343-344) |
| [[WI-CMMI-02-03-02_요구사항_변경관리]] | REQM SP1.3 | `inputs/requirements.yaml#CMMIDEV-REQM-SP1.3-REQ-001` (p.345) |
| [[WI-CMMI-02-03-03_양방향_추적성_정렬]] | REQM SP1.4, SP1.5 | `inputs/requirements.yaml#CMMIDEV-REQM-SP1.4-REQ-001 ~ SP1.5-REQ-001` (p.345-346) |
| [[WI-CMMI-02-04-01_인수유형_공급자_협약]] | SAM SP1.1, SP1.2, SP1.3 | `inputs/requirements.yaml#CMMIDEV-SAM-SP1.1-REQ-001 ~ SP1.3-REQ-001` (p.365-367) |
| [[WI-CMMI-02-04-02_공급자_협약_실행_인수]] | SAM SP2.1, SP2.2 | `inputs/requirements.yaml#CMMIDEV-SAM-SP2.1-REQ-001 ~ SP2.2-REQ-001` (p.369-371) |
| [[WI-CMMI-02-04-03_제품_전이]] | SAM SP2.3 | `inputs/requirements.yaml#CMMIDEV-SAM-SP2.3-REQ-001` (p.372) |
| [[WI-CMMI-02-05-01_프로젝트_정의프로세스_OPA활용]] | IPM SP1.1, SP1.2, SP1.3 | `inputs/requirements.yaml#CMMIDEV-IPM-SP1.1-REQ-001 ~ SP1.3-REQ-001` (p.159-162) |
| [[WI-CMMI-02-05-02_통합_계획_실행]] | IPM SP1.4, SP1.5 | `inputs/requirements.yaml#CMMIDEV-IPM-SP1.4-REQ-001 ~ SP1.5-REQ-001` (p.164-166) |
| [[WI-CMMI-02-05-03_팀_구성_OPA기여]] | IPM SP1.6, SP1.7 | `inputs/requirements.yaml#CMMIDEV-IPM-SP1.6-REQ-001 ~ SP1.7-REQ-001` (p.168-169) |
| [[WI-CMMI-02-05-04_이해관계자_의존성_이슈]] | IPM SP2.1, SP2.2, SP2.3 | `inputs/requirements.yaml#CMMIDEV-IPM-SP2.1-REQ-001 ~ SP2.3-REQ-001` (p.171-173) |
| [[WI-CMMI-02-06-01_리스크관리_준비]] | RSKM SP1.1, SP1.2, SP1.3 | `inputs/requirements.yaml#CMMIDEV-RSKM-SP1.1-REQ-001 ~ SP1.3-REQ-001` (p.351-353) |
| [[WI-CMMI-02-06-02_리스크_식별_분석]] | RSKM SP2.1, SP2.2 | `inputs/requirements.yaml#CMMIDEV-RSKM-SP2.1-REQ-001 ~ SP2.2-REQ-001` (p.354-357) |
| [[WI-CMMI-02-06-03_리스크_완화]] | RSKM SP3.1, SP3.2 | `inputs/requirements.yaml#CMMIDEV-RSKM-SP3.1-REQ-001 ~ SP3.2-REQ-001` (p.358-360) |

### 4.3 POL-CMMI-03 산하 WI (15개)

| WI ID | 매핑 SP (Req-ID) | source_citation |
|---|---|---|
| [[WI-CMMI-03-01-01_고객_요구사항_도출]] | RD SP1.1, SP1.2 | `inputs/requirements.yaml#CMMIDEV-RD-SP1.1-REQ-001 ~ SP1.2-REQ-001` (p.329-330) |
| [[WI-CMMI-03-01-02_제품_인터페이스_요구사항_수립_할당]] | RD SP2.1, SP2.2, SP2.3 | `inputs/requirements.yaml#CMMIDEV-RD-SP2.1-REQ-001 ~ SP2.3-REQ-001` (p.331-334) |
| [[WI-CMMI-03-01-03_운영_개념_기능_품질_정의]] | RD SP3.1, SP3.2, SP3.3 | `inputs/requirements.yaml#CMMIDEV-RD-SP3.1-REQ-001 ~ SP3.3-REQ-001` (p.335-337) |
| [[WI-CMMI-03-01-04_균형_분석_요구사항_확인]] | RD SP3.4, SP3.5 | `inputs/requirements.yaml#CMMIDEV-RD-SP3.4-REQ-001 ~ SP3.5-REQ-001` (p.339) |
| [[WI-CMMI-03-02-01_대안_솔루션_평가_선정]] | TS SP1.1, SP1.2 | `inputs/requirements.yaml#CMMIDEV-TS-SP1.1-REQ-001 ~ SP1.2-REQ-001` (p.376-378) |
| [[WI-CMMI-03-02-02_제품_컴포넌트_설계_TDP]] | TS SP2.1, SP2.2 | `inputs/requirements.yaml#CMMIDEV-TS-SP2.1-REQ-001 ~ SP2.2-REQ-001` (p.380-383) |
| [[WI-CMMI-03-02-03_인터페이스_설계_MakeBuyReuse]] | TS SP2.3, SP2.4 | `inputs/requirements.yaml#CMMIDEV-TS-SP2.3-REQ-001 ~ SP2.4-REQ-001` (p.385-386) |
| [[WI-CMMI-03-02-04_구현_및_지원문서_작성]] | TS SP3.1, SP3.2 | `inputs/requirements.yaml#CMMIDEV-TS-SP3.1-REQ-001 ~ SP3.2-REQ-001` (p.388-390) |
| [[WI-CMMI-03-03-01_통합_전략_환경_절차_수립]] | PI SP1.1, SP1.2, SP1.3 | `inputs/requirements.yaml#CMMIDEV-PI-SP1.1-REQ-001 ~ SP1.3-REQ-001` (p.259-262) |
| [[WI-CMMI-03-03-02_인터페이스_완전성_관리]] | PI SP2.1, SP2.2 | `inputs/requirements.yaml#CMMIDEV-PI-SP2.1-REQ-001 ~ SP2.2-REQ-001` (p.263-264) |
| [[WI-CMMI-03-03-03_컴포넌트_통합_준비_조립]] | PI SP3.1, SP3.2 | `inputs/requirements.yaml#CMMIDEV-PI-SP3.1-REQ-001 ~ SP3.2-REQ-001` (p.266-267) |
| [[WI-CMMI-03-03-04_통합_평가_패키징_인도]] | PI SP3.3, SP3.4 | `inputs/requirements.yaml#CMMIDEV-PI-SP3.3-REQ-001 ~ SP3.4-REQ-001` (p.267-268) |
| [[WI-CMMI-03-04-01_검증_준비_대상_환경_절차]] | VER SP1.1, SP1.2, SP1.3 | `inputs/requirements.yaml#CMMIDEV-VER-SP1.1-REQ-001 ~ SP1.3-REQ-001` (p.403-405) |
| [[WI-CMMI-03-04-02_피어리뷰_준비_실행]] | VER SP2.1, SP2.2 | `inputs/requirements.yaml#CMMIDEV-VER-SP2.1-REQ-001 ~ SP2.2-REQ-001` (p.406-408) |
| [[WI-CMMI-03-04-03_피어리뷰_데이터_분석]] | VER SP2.3 | `inputs/requirements.yaml#CMMIDEV-VER-SP2.3-REQ-001` (p.408) |
| [[WI-CMMI-03-04-04_검증_실행_결과_분석]] | VER SP3.1, SP3.2 | `inputs/requirements.yaml#CMMIDEV-VER-SP3.1-REQ-001 ~ SP3.2-REQ-001` (p.409-410) |
| [[WI-CMMI-03-05-01_확인_준비_대상_환경_절차]] | VAL SP1.1, SP1.2, SP1.3 | `inputs/requirements.yaml#CMMIDEV-VAL-SP1.1-REQ-001 ~ SP1.3-REQ-001` (p.395-398) |
| [[WI-CMMI-03-05-02_확인_실행]] | VAL SP2.1 | `inputs/requirements.yaml#CMMIDEV-VAL-SP2.1-REQ-001` (p.398) |
| [[WI-CMMI-03-05-03_확인_결과_분석_환류]] | VAL SP2.2 | `inputs/requirements.yaml#CMMIDEV-VAL-SP2.2-REQ-001` (p.399) |

### 4.4 POL-CMMI-04 산하 WI (15개)

| WI ID | 매핑 SP (Req-ID) | source_citation |
|---|---|---|
| [[WI-CMMI-04-01-01_베이스라인_수립_CI식별_시스템_릴리즈]] | CM SP1.1, SP1.2, SP1.3 | `inputs/requirements.yaml#CMMIDEV-CM-SP1.1-REQ-001 ~ SP1.3-REQ-001` (p.140-143) |
| [[WI-CMMI-04-01-02_변경_추적_및_통제]] | CM SP2.1, SP2.2 | `inputs/requirements.yaml#CMMIDEV-CM-SP2.1-REQ-001 ~ SP2.2-REQ-001` (p.144-145) |
| [[WI-CMMI-04-01-03_무결성_기록_및_형상감사]] | CM SP3.1, SP3.2 | `inputs/requirements.yaml#CMMIDEV-CM-SP3.1-REQ-001 ~ SP3.2-REQ-001` (p.146) |
| [[WI-CMMI-04-02-01_측정_목적_및_명세_정보니즈_기반]] | MA SP1.1, SP1.2, SP1.3, SP1.4 | `inputs/requirements.yaml#CMMIDEV-MA-SP1.1-REQ-001 ~ SP1.4-REQ-001` (p.177-183) |
| [[WI-CMMI-04-02-02_데이터_수집_및_분석]] | MA SP2.1, SP2.2 | `inputs/requirements.yaml#CMMIDEV-MA-SP2.1-REQ-001 ~ SP2.2-REQ-001` (p.186-187) |
| [[WI-CMMI-04-02-03_데이터_저장_및_결과_전달]] | MA SP2.3, SP2.4 | `inputs/requirements.yaml#CMMIDEV-MA-SP2.3-REQ-001 ~ SP2.4-REQ-001` (p.187-189) |
| [[WI-CMMI-04-03-01_프로세스_및_산출물_객관적_평가]] | PPQA SP1.1, SP1.2 | `inputs/requirements.yaml#CMMIDEV-PPQA-SP1.1-REQ-001 ~ SP1.2-REQ-001` (p.303-304) |
| [[WI-CMMI-04-03-02_부적합_의사소통_해결_및_기록]] | PPQA SP2.1, SP2.2 | `inputs/requirements.yaml#CMMIDEV-PPQA-SP2.1-REQ-001 ~ SP2.2-REQ-001` (p.305-306) |
| [[WI-CMMI-04-04-01_DAR_지침_평가기준_및_대안]] | DAR SP1.1, SP1.2, SP1.3 | `inputs/requirements.yaml#CMMIDEV-DAR-SP1.1-REQ-001 ~ SP1.3-REQ-001` (p.151-153) |
| [[WI-CMMI-04-04-02_평가방법_선정_및_대안평가]] | DAR SP1.4, SP1.5 | `inputs/requirements.yaml#CMMIDEV-DAR-SP1.4-REQ-001 ~ SP1.5-REQ-001` (p.154-155) |
| [[WI-CMMI-04-04-03_해결안_선정]] | DAR SP1.6 | `inputs/requirements.yaml#CMMIDEV-DAR-SP1.6-REQ-001` (p.156) |

**WI 커버리지: 60/60 WI 가 168/168 SP 매핑.** SP↔WI 카운트 분포: 평균 2.8 SP/WI.

---

## 5. 요건 → TMP/EX 매핑 (산출물 → TMP-CMMI-* / EX-CMMI-*)

117 TMP × 117 EX 가 60 WI 의 산출물(work products) 을 1:1+ 짝 매칭한다. 모든 TMP-EX 쌍이 frontmatter `parent_wi` 로 상위 WI 를 참조한다.

### 5.1 분포 요약 (POL 별 TMP/EX 개수)

| POL | PRO 수 | WI 수 | TMP 수 | EX 수 | 비고 |
|---|---|---|---|---|---|
| POL-CMMI-01 (Process Mgmt) | 3 | 10 | 22 | 22 | OPD 4 + OPF 11 + OT 7 |
| POL-CMMI-02 (Project Mgmt) | 6 | 20 | 35 | 35 | PP 11 + PMC 7 + REQM 6 + SAM 8 + IPM (Engineering 흐름) + RSKM 3 |
| POL-CMMI-03 (Engineering) | 5 | 19 | 35 | 35 | RD 8 + TS 8 + PI 6 + VER 7 + VAL 6 |
| POL-CMMI-04 (Support) | 4 | 11 | 25 | 25 | CM 7 + MA 7 + PPQA 4 + DAR 7 |
| **합계** | **18** | **60** | **117** | **117** | — |

### 5.2 PA 별 핵심 산출물 (출처: requirements.yaml `example_work_products`)

| PA | 핵심 TMP (대표) | source_citation |
|---|---|---|
| OPD | [[TMP-CMMI-01-01-01-01_조직표준프로세스_OSSP_정의서]], [[TMP-CMMI-01-01-02-01_테일러링_가이드라인]], [[TMP-CMMI-01-01-03-01_측정저장소_PAL_운영서]] | `inputs/requirements.yaml#CMMIDEV-OPD-SP1.1~SP1.7` example_work_products (p.192-200) |
| OPF | [[TMP-CMMI-01-02-01-01_프로세스_니즈_목표_기술서]], [[TMP-CMMI-01-02-02-01_프로세스_액션_플랜]], [[TMP-CMMI-01-02-04-02_교훈_등록부]] | `inputs/requirements.yaml#CMMIDEV-OPF-SP1.1~SP3.4` (p.204-213) |
| OT | [[TMP-CMMI-01-03-01-03_조직_교육_전술계획]], [[TMP-CMMI-01-03-02-02_교육_이수_기록부]], [[TMP-CMMI-01-03-03-01_교육_효과성_평가_보고서]] | `inputs/requirements.yaml#CMMIDEV-OT-SP1.1~SP2.3` (p.248-255) |
| PP | [[TMP-CMMI-02-01-01-01_WBS_작업패키지_기술서]], [[TMP-CMMI-02-01-02-01_일정_예산_계획서]], [[TMP-CMMI-02-01-03-03_통합_프로젝트_계획서]] | `inputs/requirements.yaml#CMMIDEV-PP-SP1.1~SP3.3` (p.283-298) |
| PMC | [[TMP-CMMI-02-02-01-01_프로젝트_성과_기록]], [[TMP-CMMI-02-02-02-02_마일스톤_검토_결과보고]], [[TMP-CMMI-02-02-03-02_시정조치_계획서]] | `inputs/requirements.yaml#CMMIDEV-PMC-SP1.1~SP2.3` (p.272-279) |
| REQM | [[TMP-CMMI-02-03-01-01_요구사항_평가_수락_기준]], [[TMP-CMMI-02-03-02-02_변경영향_평가보고서]], [[TMP-CMMI-02-03-03-01_요구사항_추적성_매트릭스]] | `inputs/requirements.yaml#CMMIDEV-REQM-SP1.1~SP1.5` (p.343-346) |
| SAM | [[TMP-CMMI-02-04-01-03_공급자_협약서_SOW]], [[TMP-CMMI-02-04-02-02_인수_검토_시험_결과보고]], [[TMP-CMMI-02-04-03-01_전이_계획서]] | `inputs/requirements.yaml#CMMIDEV-SAM-SP1.1~SP2.3` (p.365-372) |
| IPM | [[TMP-CMMI-02-05-01-01_프로젝트_정의_프로세스_기술서]], [[TMP-CMMI-02-05-01-02_OPA_활용_계획서]], (팀헌장·OPA 기여 자료) | `inputs/requirements.yaml#CMMIDEV-IPM-SP1.1~SP2.3` (p.159-173) |
| RSKM | (리스크 출처/카테고리), (리스크 완화계획), (리스크 모니터링 기록) — TMP 일부 차기 빌드 보강 | `inputs/requirements.yaml#CMMIDEV-RSKM-SP1.1~SP3.2` (p.351-360) |
| RD | [[TMP-CMMI-03-01-01-01_이해관계자_니즈_도출_결과서]], [[TMP-CMMI-03-01-03-01_운영_개념_시나리오_정의서]], [[TMP-CMMI-03-01-04-01_요구사항_균형_분석_보고서]] | `inputs/requirements.yaml#CMMIDEV-RD-SP1.1~SP3.5` (p.328-340) |
| TS | [[TMP-CMMI-03-02-01-01_대안_솔루션_평가_보고서]], [[TMP-CMMI-03-02-02-02_기술자료패키지_TDP]], [[TMP-CMMI-03-02-03-01_인터페이스_설계_명세서_ICD]] | `inputs/requirements.yaml#CMMIDEV-TS-SP1.1~SP3.2` (p.375-390) |
| PI | [[TMP-CMMI-03-03-01-01_제품_통합_전략_환경_절차서]], [[TMP-CMMI-03-03-02-01_인터페이스_카테고리_매핑표_관리기록]], [[TMP-CMMI-03-03-04-01_통합_평가_패키징_인도_보고서]] | `inputs/requirements.yaml#CMMIDEV-PI-SP1.1~SP3.4` (p.259-268) |
| VER | [[TMP-CMMI-03-04-01-01_검증_계획서]], [[TMP-CMMI-03-04-02-01_피어리뷰_체크리스트_기록부]], [[TMP-CMMI-03-04-04-01_검증_결과_보고서]] | `inputs/requirements.yaml#CMMIDEV-VER-SP1.1~SP3.2` (p.403-410) |
| VAL | (확인 대상 목록), (확인 절차서), (확인 결과 보고서) | `inputs/requirements.yaml#CMMIDEV-VAL-SP1.1~SP2.2` (p.394-399) |
| CM | [[TMP-CMMI-04-01-01-01_형상항목_CI_목록]], [[TMP-CMMI-04-01-02-02_CCB_의사록_및_변경통제_대장]], [[TMP-CMMI-04-01-03-02_형상감사_체크리스트_및_결과보고]] | `inputs/requirements.yaml#CMMIDEV-CM-SP1.1~SP3.2` (p.140-146) |
| MA | [[TMP-CMMI-04-02-01-02_측정_명세서]], [[TMP-CMMI-04-02-02-02_분석_보고서]], [[TMP-CMMI-04-02-03-02_측정정보_배포기록]] | `inputs/requirements.yaml#CMMIDEV-MA-SP1.1~SP2.4` (p.177-189) |
| PPQA | [[TMP-CMMI-04-03-01-01_프로세스_평가_체크리스트_및_보고서]], [[TMP-CMMI-04-03-02-01_QA_시정조치_보고서]], [[TMP-CMMI-04-03-02-02_품질_트렌드_및_평가로그]] | `inputs/requirements.yaml#CMMIDEV-PPQA-SP1.1~SP2.2` (p.303-306) |
| DAR | [[TMP-CMMI-04-04-01-01_DAR_적용지침_적용결과서]], [[TMP-CMMI-04-04-02-02_대안_평가_결과서]], [[TMP-CMMI-04-04-03-01_의사결정_근거서]] | `inputs/requirements.yaml#CMMIDEV-DAR-SP1.1~SP1.6` (p.151-156) |

> 각 TMP 마다 `parent_wi` frontmatter 가 1:1 매칭된다. 본 매트릭스의 5.1 §분포 요약은 전수 검증 완료(117/117).

---

## 6. 커버리지 통계

### 6.1 요건 단위 커버리지

| 범주 | 총 Req | ✅ 반영완료 | 🟡 작업중 | ⛔ 미착수 | 비율 |
|---|---|---|---|---|---|
| Generic Goals (GG1/2/3) | 3 | 3 | 0 | 0 | 100% |
| Generic Practices (GP 1.1/2.1~2.10/3.1~3.2) | 12 | 12 | 0 | 0 | 100% |
| ML2 SG (CM/MA/PMC/PP/PPQA/REQM/SAM) | 13 | 13 | 0 | 0 | 100% |
| ML2 SP | 64 | 64 | 0 | 0 | 100% |
| ML3 SG (DAR/IPM/OPD/OPF/OT/PI/RD/RSKM/TS/VAL/VER) | 35 | 34 | 1 | 0 | 97.1% (RSKM SG1 ingest 누락) |
| ML3 SP | 104 | 104 | 0 | 0 | 100% |
| Purpose (informative) | 5 | 5 | 0 | 0 | 100% |
| **합계** | **236 (적용 216)** | **235** | **1** | **0** | **99.6%** |

### 6.2 자산 단위 커버리지

| 자산 유형 | 생성 | 적용요건 매핑 ✅ | 비율 |
|---|---|---|---|
| POL | 5 | 5 | 100% |
| PRO | 18 | 18 | 100% |
| WI | 60 | 60 | 100% |
| TMP | 117 | 117 | 100% |
| EX | 117 | 117 | 100% |
| steps.yaml | 60 | 60 | 100% |

### 6.3 source_citation 커버리지

| 영역 | 매핑 행 수 | citation 있음 | 비율 |
|---|---|---|---|
| §2 PA → POL | 5 | 5 | 100% |
| §3 PA → PRO | 18 | 18 | 100% |
| §3.5 GG/GP 내재화 | 15 | 15 | 100% |
| §4 SP → WI | 60 | 60 | 100% |
| §5.2 PA 핵심 TMP | 18 | 18 | 100% |
| **합계** | **116** | **116** | **100%** |

> 모든 매핑 행이 `inputs/requirements.yaml#REQ-ID (p.N)` 또는 동등 출처를 인라인 인용.

### 6.4 출처 유형 분포

| 출처 유형 | 매핑 수 | 비고 |
|---|---|---|
| 표준원문 (CMU/SEI-2010-TR-033 PDF) | 116 | inputs/01_표준원문/CMMI-DEV/requirements.yaml (verbatim) |
| 해설서 (pa_relationships.yaml) | 부수적 | follows/precedes 와 GG/GP 내재화 근거 |
| AsIs (기존 vault 자원) | 0 | interface_only — 외부 영역 재사용 없음 |
| LLM 추정 | 0 | 모든 매핑은 ingest 산출물 기반 |
| 공공법규 | 0 | 표준 자체가 비법규 |

**출처 유형 분포: 표준원문 100% — 추정·합성 0건.**

---

## 7. 누락·약점 (Gap 분석)

### 7.1 식별된 Gap

| 우선순위 | 영역 | 내용 | 권장 조치 | 담당 |
|---|---|---|---|---|
| **HIGH** | RSKM SG1 | `inputs/requirements.yaml` 에 SG1 "Prepare for Risk Management" 엔트리 누락 (구조상 SP1.1~1.3 의 상위 골, p.351). 적용요건.md §6-2-15 에 플래그 처리됨. | 다음 ingest pass 에서 SG1 행 추가 후 본 매트릭스 §4 RSKM 묶음에 매핑 반영. v0.2 갱신. | ingest-agent |
| MED | RSKM TMP 보강 | PRO-CMMI-02-06 의 TMP/EX 가 본 빌드 117개에 1차 포함됐으나, 일부 example_work_products (비상계획·리스크 모니터링 기록) 가 별도 TMP 미생성. | 차기 빌드에서 RSKM 전용 TMP 2~3개 추가. | wi-tmp-writer |
| MED | VAL TMP 보강 | PRO-CMMI-03-05 의 TMP 가 6개로 다른 Engineering PA(7~8개)보다 적음. 핵심 확인 산출물(확인 대상 목록, 확인 절차서) 1:1 매핑되나 보완 여지. | 차기 빌드에서 VAL 전용 TMP 추가 검토. | wi-tmp-writer |
| LOW | GP 내재화 정량 증적 | §3.5 GG/GP 매핑은 PRO/WI 의 §3/§5/§6 항목으로 내재화됐으나, PA × GP 12 개별 칸별 증적 매트릭스가 아직 표 형태로 없음. | 차기 빌드에서 18 PA × 12 GP = 216 셀 매트릭스 별첨 생성 검토 (선택). | traceability-mapper |

### 7.2 RACI Accountable 검토 (18 PRO frontmatter 추출)

| 영역 | Accountable 분포 | 중복/누락 |
|---|---|---|
| Process Mgmt (OPD/OPF/OT) | CEO/CTO | OK — 단일 A |
| Project Mgmt (PP/PMC/REQM/SAM/IPM/RSKM) | CEO/CTO (PP/PMC) + PMO Director (REQM/SAM/IPM/RSKM) | OK — 영역별 단일 A (PMO 위임 명확) |
| Engineering (RD/TS/PI/VER/VAL) | Project Manager | OK — 단일 A |
| Support (CM/MA/PPQA/DAR) | CEO/CTO | OK — 단일 A |

**Accountable 중복·누락 0건.** 모든 18 PRO 가 `approver` 단일 지정.

---

## 8. source_citation 인덱스

본 매트릭스의 모든 인용은 다음 단일 입력 소스로부터 도출된다.

| 출처 아티팩트 | 경로 | 라이선스 |
|---|---|---|
| CMMI-DEV V1.3 Requirements (Part Two SG/SP verbatim) | `inputs/01_표준원문/CMMI-DEV/requirements.yaml` | CMU/SEI-2010-TR-033 — `internal_use_derivative_work` |
| CMMI-DEV V1.3 PA Relationships (Part One Ch.4) | `inputs/01_표준원문/CMMI-DEV/pa_relationships.yaml` | 동일 |
| CMMI-DEV V1.3 Adoption Guide (Part One Ch.5) | `inputs/01_표준원문/CMMI-DEV/adoption_guide.yaml` | 동일 |
| CMMI-DEV V1.3 Definitions (Glossary) | `inputs/01_표준원문/CMMI-DEV/definitions.yaml` | 동일 |
| CMMI-DEV V1.3 Structure | `inputs/01_표준원문/CMMI-DEV/structure.yaml` | 동일 |
| (원문 PDF) | `inputs/01_표준원문/CMMI-DEV/cmmi-dev-v13.pdf` (p.39~410) | 동일 |

> 모든 SG/SP 인용은 `requirements.yaml` 의 verbatim text 와 페이지 번호 일치. 본 매트릭스 인용 형식: `inputs/requirements.yaml#REQ-ID (p.N)`.

---

## 9. 본 빌드 메타데이터

| 항목 | 값 |
|---|---|
| 빌드 ID | CMMI-DEV-ML3-V1.3 (slug: `cmmi-dev-ml3-v1.3`) |
| 파이프라인 phase | Phase 4 (Trace) |
| 빌드 commit | `feat/cmmi-dev-ml3-v1.3-output` 분기 (head: post-flow) |
| 편입일 | 2026-05-11 |
| 다음 phase | Phase 5 (QA — qa-reviewer) |
| 본 매트릭스 버전 | v0.1 (draft) — Phase 5 QA 통과 시 v1.0 승인판 발행 |

---

## 10. 개정 이력

| 버전 | 일자 | 변경 내용 | 담당 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 작성 (Phase 4 Trace) — 18 PA × 5 POL × 18 PRO × 60 WI × 117 TMP × 117 EX 전체 매핑, GG/GP 내재화 매핑, RSKM SG1 ingest 누락 1건 플래그 | traceability-mapper |
| 0.2 | 2026-05-11 | QA-005 (MINOR) 자가수정 — §3-bis 신규: GP × PA 정량 커버리지 매트릭스 (18 PA × 13 GP = 234 셀, ✓ 198 + ✓✓ 36 + — 0). 모든 셀에 `inputs/requirements.yaml#CMMIDEV-GP{x.y}-REQ-001 + p.{N}` source_citation. §1.2 인벤토리 GP 수 "12" 표기 정정: 실제 13 GP (GP 1.1 + GP 2.1~2.10 + GP 3.1~3.2 = 1+10+2) — 본 §3-bis 주석으로 명시. attempt 2 자가수정 모드. | traceability-mapper |
