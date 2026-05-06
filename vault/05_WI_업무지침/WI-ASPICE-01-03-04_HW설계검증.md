---
type: WI
doc_id: "WI-ASPICE-01-03-04"
title: "HW 설계 검증 (HWE.3)"
version: "0.1"
owner: "HW Engineer"
reviewer: "SI/PI Engineer / EMC Engineer / QA"
approver: "HW Lead"
scope: "HW 설계 검증 계획 → SI/EMC 시뮬레이션 → 시제 PCB 측정 → PCB ↔ 설계 일치 검증"
parent_pro: "[[PRO-ASPICE-01-03_하드웨어공학프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-03-04-01_HW설계검증보고서]]"]
related_rec: []
standards: ["Automotive SPICE 4.0", "ISO 26262", "CISPR 25", "ISO 11452", "IPC-A-610"]
aspice_processes: ["HWE.3"]
entry_gate: "WI-ASPICE-01-03-03.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, HWE.3, DesignVerification, SI, EMC]
---

# HW 설계 검증 업무지침 (WI-ASPICE-01-03-04)

> 상위 절차: [[PRO-ASPICE-01-03_하드웨어공학프로세스]] §5 단계 7
> ASPICE 매핑: HWE.3 (HW Design Verification — 생산 데이터 호환 HW vs 설계 일치)

## 1. 업무 목적

ASPICE 4.0 의 HWE.3 정의에 따라 **시제 PCB가 설계 산출물(Schematic·Layout·BOM)과 일치하는지** 검증한다. SI/PI/EMC 시뮬레이션 결과를 시제 측정값과 비교하여 설계 모델의 타당성을 확인하고, 후속 HWE.4 요구사항 검증의 입력 신뢰도를 확보한다.

## 2. 수행 주체
- **주 수행자**: HW Engineer (검증 실행)
- **검토자**: SI/PI Engineer, EMC Engineer, Safety Engineer, QA
- **승인자**: HW Lead

## 3. 범위
시제 PCB 수령 시점부터 Design Verification Report v1.0 발행까지 적용한다. 요구사항 적합성 검증(DV/PV)은 [[WI-ASPICE-01-03-05_HW요구사항검증]] 에서 수행한다.

## 4. 입력 자료 / 산출물
- **Input**: Design Package (Schematic v1.0, PCB Layout v1.0, BOM v1.0), 시제 PCB Lot, SI/PI/EMC 시뮬레이션 결과 (HWE.2)
- **Output**: HW Design Verification Plan, HW Design Verification Report, 측정 Raw Data, PCB↔설계 일치 보고서

## 5. 수행 절차

### 5.1 사전 준비
1. 시제 PCB Lot 수령·외관 검사 (IPC-A-610 Class 2/3 기준).
2. 측정 장비 (Oscilloscope, VNA, EMI Receiver, Power Analyzer) 교정 유효 여부 확인.
3. 시뮬레이션 결과 (HWE.2.BP4) 사본 확보.
4. Schematic / PCB Layout / BOM v1.0 베이스라인 동결 확인.

### 5.2 수행 단계

1. **검증 계획 수립** (HWE.3.BP1)
   - 검증 범위: SI (Eye diagram, Jitter), PI (PDN impedance), EMC (방사·전도), 전원 안정성, 기능 동작.
   - 시뮬레이션 결과 vs 시제 측정 비교 항목 정의.
   - 합격 기준·측정 조건·반복 횟수 명시.

2. **PCB ↔ 설계 일치성 검증** (HWE.3.BP2)
   - 시제 PCB Visual / X-ray 검사 → BOM 부품 실장 일치 확인.
   - PCB Stack-up 단면 분석 (마이크로섹션) → 설계 Stack-up 일치.
   - Net 연결성 ICT (In-Circuit Test) → Schematic Netlist 일치.

3. **SI 측정** (HWE.3.BP3)
   - 고속 신호 (CAN-FD, Ethernet, DDR) Eye diagram 측정.
   - Jitter, Rise/Fall time, Crosstalk 측정.
   - 시뮬값 vs 측정값 차이 분석 (목표 ±20% 이내).

4. **PI 측정** (HWE.3.BP3)
   - PDN Impedance 측정 (VNA + Probe).
   - Decoupling Cap 효과 검증.
   - 부하 변동 시 전압 강하 측정.

5. **EMC 측정** (HWE.3.BP3)
   - 방사 EMI (CISPR 25 Class 5), 전도 EMI 측정.
   - BCI (Bulk Current Injection, ISO 11452-4) 면역 시험.
   - Pre-compliance 시뮬값 vs 측정값 비교.

6. **결과 분석 및 보고** (HWE.3.BP4)
   - 시뮬값↔측정값 차이 분석 → 모델 타당성 평가.
   - 한계 초과 항목 식별 → SUP.9 결함 등록 (필요 시).
   - Design Verification Report 작성 + HW Lead 승인.

### 5.3 완료 조건 체크리스트
- [ ] 시제 PCB Visual 검사 IPC-A-610 Pass
- [ ] PCB ↔ Schematic Netlist 일치 100%
- [ ] BOM ↔ 실장 부품 일치 100%
- [ ] Stack-up 단면 분석 일치
- [ ] SI 측정값 시뮬 대비 차이 ≤ 20%
- [ ] PI 측정값 시뮬 대비 차이 ≤ 20%
- [ ] EMC 측정값 CISPR 25 Class 5 충족
- [ ] 측정 Raw Data 보관 (CM 등록)
- [ ] 미달 항목 SUP.9 결함 등록
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **CM (SUP.8)**: Design Package 베이스라인 확인
- **Production Eng.**: 시제 제작 일정·품질
- **EMC Lab**: EMC 시험 일정·장비
- **Test Lab**: SI/PI 측정 장비
- **QA (SUP.1)**: 검증 절차 검토

## 7. 주의사항 / 예외 처리

### 7.1 시제 PCB ↔ 설계 불일치 발견
- ICT/Visual 결과 BOM·Schematic 불일치:
  - 시제 사용 즉시 중지.
  - 원인 분석 — PCB 제조 오류 vs 설계 오류 vs BOM 오류.
  - SUP.9 Critical 결함 등록 + SUP.10 변경 절차.
  - 정정 후 재시제 또는 정정 BOM 발행.

### 7.2 시뮬값 ↔ 측정값 차이 큰 경우
- 차이 > 20%:
  - 1) 측정 setup 오류 점검 (Probe, Cable, Termination).
  - 2) 시뮬 모델 정확도 검토 (IBIS, S-parameter).
  - 3) 모델 vs 실 부품 차이 (Vendor SPICE 모델 갱신).
  - 모델 재정합 후 추가 시뮬·측정 반복.

### 7.3 EMC Class 5 미달
- 방사·전도 EMC 한계 초과:
  - 1) 차폐 보강 (Shield Can, Ferrite).
  - 2) PCB Layout 변경 가능 여부 검토.
  - 3) Filter 추가 (수동소자 BOM 변경).
  - 변경 시 SUP.10 + HWE.3 재실행.

### 7.4 측정 장비 교정 만료
- 측정 장비 교정 만료 또는 교정증서 누락:
  - 측정 결과 무효 처리.
  - 교정 완료 후 재측정.
  - QA 에 사유 보고.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-03-04-01_HW설계검증보고서]]
- 기록 폴더: `vault/08_REC_기록/HWE/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-HWE.3-*"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — HWE.3 설계 검증 (PCB↔설계 일치) 정의 | (대기) |
