---
type: WI
doc_id: "WI-ASPICE-01-03-02"
title: "회로 및 PCB 설계 (HWE.2)"
version: "0.1"
owner: "HW Engineer"
reviewer: "HW Architect / SI·PI Engineer / EMC Engineer"
approver: "HW Lead"
scope: "HwRS 인계 → 회로도(Schematic) → PCB Layout → SI/PI/EMC 분석 → DRC 통과"
parent_pro: "[[PRO-ASPICE-01-03_하드웨어공학프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-03-02-01_회로및PCB설계서]]"]
related_rec: []
standards: ["Automotive SPICE 4.0", "ISO 26262", "AEC-Q100", "AEC-Q200", "IEC 61000 EMC", "IPC-2221", "IPC-7351"]
aspice_processes: ["HWE.2"]
entry_gate: "WI-ASPICE-01-03-01.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, HWE, Schematic, PCB, SI, PI, EMC, DRC]
---

# 회로 및 PCB 설계 업무지침 (WI-ASPICE-01-03-02)

> 상위 절차: [[PRO-ASPICE-01-03_하드웨어공학프로세스]] §5 단계 4~5
> ASPICE 매핑: HWE.2 (HW Design — Schematic & PCB Layout)

## 1. 업무 목적

HWE.1 에서 확정된 HwRS 를 회로도(Schematic) 와 PCB Layout 으로 구체화하고, 신호 무결성(SI)·전원 무결성(PI)·EMC 사전 분석을 수행하여 시제품 제작 가능 상태로 만든다. AEC-Q100/Q200 인증 부품을 강제 적용한다.

## 2. 수행 주체
- **주 수행자**: HW Engineer (회로 설계자, PCB Layout 설계자)
- **검토자**: HW Architect, SI·PI Engineer, EMC Engineer, Safety Engineer, QA
- **승인자**: HW Lead

## 3. 범위
HwRS 베이스라인 인계 시점부터 PCB Layout v1.0 + DRC Pass 까지 적용한다. BOM 작성·CM 등록은 [[WI-ASPICE-01-03-03_BOM관리]] 에서 수행한다.

## 4. 입력 자료 / 산출물
- **Input**: HwRS v1.0, SAD/ICD HW 분배분, AEC-Q100/Q200 부품 라이브러리, EMC 가이드라인
- **Output**: Schematic v1.0, PCB Layout v1.0, SI/PI 시뮬레이션 결과, EMC Pre-compliance 분석서, DRC Report

## 5. 수행 절차

### 5.1 사전 준비
1. 회로/PCB 설계 EDA 도구 (Altium Designer / KiCad / OrCAD) 라이선스·라이브러리 확인.
2. AEC-Q100/Q200 인증 부품 라이브러리 최신화 (Vendor Datasheet, AEC 인증서).
3. PCB 제조사 Stack-up·DRC Rule 파일 수령 확인.

### 5.2 수행 단계

1. **회로 토폴로지 설계** (HWE.2.BP1)
   - HwRS 의 기능·전기·인터페이스 요구사항을 회로 블록으로 분해.
   - 핵심 IC (MCU·SoC·Power·통신 PHY) 선정 — 모두 AEC-Q100 Grade 1/2 충족.
   - Safety-critical 회로 (ASIL B 이상) 는 다중화·다양성 검토.

2. **회로도 작성** (HWE.2.BP1)
   - 전원 회로, 통신 회로 (CAN/CAN-FD/Ethernet PHY), I/O 보호 회로, 클럭 회로 작성.
   - 모든 부품 Manufacturer P/N 명시, EoL 부품 0건.
   - Pin assignment · Net 명명 규칙 준수.

3. **PCB Stack-up 설계** (HWE.2.BP2)
   - 신호층·전원층·접지층 구성 결정 (4~12 layer).
   - 임피던스 컨트롤 (50Ω single-ended, 100Ω differential).

4. **PCB 부품 배치 및 라우팅** (HWE.2.BP2)
   - SI/PI 가이드라인 (트레이스 길이 매칭, 차폐, GND 분리) 준수.
   - EMC 가이드라인 (Crystal 위치, Filter, Shield Can) 준수.
   - Safety-critical 신호 격리·차폐 적용.

5. **SI/PI 시뮬레이션** (HWE.2.BP4)
   - HyperLynx / SIwave 등으로 고속 신호 (CAN-FD, Ethernet, DDR) 시뮬.
   - 전원 임피던스 분석 (PDN), Decoupling Cap 검증.

6. **EMC Pre-compliance 분석** (HWE.2.BP4)
   - 방사·전도 EMI 시뮬 + 입력 보호회로(TVS, Common-mode choke) 검증.
   - CISPR 25 Class 5 / ISO 11452 기준선 비교.

7. **DRC (Design Rule Check)**
   - PCB 제조사 DRC Rule 적용 → 위반 0건까지 반복.
   - DFM (Design for Manufacturability) 검토.

8. **설계 검토 (Design Review)**
   - HW Architect, SI·PI, EMC, Safety, QA 합동 검토.
   - 검토 결과 → Schematic v1.0 / PCB Layout v1.0 승인.

### 5.3 완료 조건 체크리스트
- [ ] Schematic 모든 부품 AEC-Q100/Q200 인증 표기
- [ ] EoL 부품 0건
- [ ] PCB Stack-up·임피던스 명세 첨부
- [ ] SI/PI 시뮬레이션 결과 첨부 (Eye diagram, PDN impedance)
- [ ] EMC Pre-compliance 분석서 첨부 (CISPR 25 기준 충족)
- [ ] DRC 위반 0건 (Report 첨부)
- [ ] HwRS↔Schematic 추적성 매트릭스 ≥ 95%
- [ ] Design Review 회의록 + 승인 기록
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **HwRS 작성자 ([[WI-ASPICE-01-03-01_HW요구사항및설계]])**: 요구사항 명확화 협의
- **SW Lead**: HW-SW 핀맵·인터럽트 합의
- **EMC/Safety**: ASIL 상속·EMC 사전 검토
- **Procurement ([[PRO-ASPICE-01-06]])**: 부품 가용성·Lifetime 확인
- **CM (SUP.8)**: Schematic·Layout 베이스라인 등록

## 7. 주의사항 / 예외 처리

### 7.1 SI/PI 시뮬 결과 마진 부족
- Eye diagram 마진 < 20% 또는 PDN 임피던스 한계 초과 시:
  - 1) Trace 라우팅 재설계 (length matching, via 최소화).
  - 2) Decoupling Cap 추가 / 변경.
  - 3) Stack-up 재조정 (참조 GND 추가).
  - 미해결 시 IC 변경 또는 일정 영향 분석 + PM 보고.

### 7.2 EMC Pre-compliance 한계 초과
- 시뮬에서 CISPR 25 Class 5 미달:
  - 1) Common-mode choke / Ferrite bead 추가.
  - 2) Shield Can 적용.
  - 3) 회로 토폴로지 변경 (LDO → Switching → LDO 격리 등).
  - 시제 시험 단계로 넘기지 않고 사전 해결 원칙.

### 7.3 DRC 위반 다수 발생
- DRC 위반이 50건 이상이거나 구조적 위반 발생 시:
  - 회로 토폴로지·부품 배치부터 재검토.
  - 패치성 수정 금지 — 근본 재설계 후 검토 회의 재개최.

### 7.4 ASIL D 회로 다중화
- ASIL D 신호 경로:
  - 다중화·다양성 설계 강제 (Lockstep MCU, Voter 회로).
  - HW Failure Rate (FIT) 계산서 첨부.
  - Safety Manager 공동 검토 + 승인.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-03-02-01_회로및PCB설계서]]
- 기록 폴더: `vault/08_REC_기록/HWE/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-HWE.2-*"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — HWE.2 회로/PCB 설계 분리 정의 | (대기) |
