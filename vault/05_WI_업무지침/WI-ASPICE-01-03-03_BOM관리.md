---
type: WI
doc_id: "WI-ASPICE-01-03-03"
title: "BOM 작성 및 CM 관리 (HWE.2.BP3)"
version: "0.1"
owner: "HW Engineer"
reviewer: "Procurement / CM (SUP.8) / Production Engineering"
approver: "HW Lead + CM Manager"
scope: "PCB Layout 인계 → BOM 작성 (특수특성·EoL·Vendor) → Gerber 발행 → CM 베이스라인 등록"
parent_pro: "[[PRO-ASPICE-01-03_하드웨어공학프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-03-03-01_BOM]]"]
related_rec: []
standards: ["Automotive SPICE 4.0", "AEC-Q100", "AEC-Q200", "IATF 16949", "VDA 6.3"]
aspice_processes: ["HWE.2"]
entry_gate: "WI-ASPICE-01-03-02.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, HWE.2, BOM, Gerber, CM, EoL]
---

# BOM 작성 및 CM 관리 업무지침 (WI-ASPICE-01-03-03)

> 상위 절차: [[PRO-ASPICE-01-03_하드웨어공학프로세스]] §5 단계 6
> ASPICE 매핑: HWE.2.BP3 (BOM·생산데이터 작성) + SUP.8 (CM)

## 1. 업무 목적

PCB Layout v1.0 을 기반으로 BOM (Bill of Materials) v1.0 을 작성하고, 모든 부품의 Manufacturer P/N·Vendor·Lifetime·EoL 위험도를 검증한 뒤, Gerber·Pick&Place·Drill 파일과 함께 CM (SUP.8) 베이스라인에 등록하여 시제·양산 데이터 정합성을 보장한다.

## 2. 수행 주체
- **주 수행자**: HW Engineer (BOM 작성), Production Engineer (제조 검토)
- **검토자**: Procurement, QA, Safety Engineer, Process Engineer
- **승인자**: HW Lead + CM Manager

## 3. 범위
PCB Layout 베이스라인 승인 시점부터 BOM v1.0 + 생산데이터 패키지 + CM 등록 완료까지 적용한다. 변경 발생 시 SUP.10 변경 절차를 따른다.

## 4. 입력 자료 / 산출물
- **Input**: Schematic v1.0, PCB Layout v1.0, AEC-Q100/Q200 부품 라이브러리, AVL (Approved Vendor List)
- **Output**: BOM v1.0 (Excel/CSV), Gerber Package, Pick&Place File, Drill File, AVL Match Report, EoL Risk Report, CM Baseline Tag

## 5. 수행 절차

### 5.1 사전 준비
1. AVL (Approved Vendor List) 최신화 확인.
2. 부품 Lifetime DB (IHS Markit / Z2Data 등) 접근 권한 확인.
3. CM 시스템 (Polarion / PLM) 접근 권한 확인.
4. PCB 제조사 Gerber/Drill 포맷 요구사항 수령 확인.

### 5.2 수행 단계

1. **BOM 추출** (HWE.2.BP3)
   - EDA 도구에서 BOM 자동 추출 (Reference Designator·Value·Footprint·P/N).
   - 누락 항목·중복 항목 점검.

2. **부품 정보 보강**
   - 각 부품 행에 다음 컬럼 추가/검증:
     - Manufacturer P/N (정확한 풀네임)
     - Manufacturer Name
     - Vendor (Authorized Distributor: Digikey, Mouser, Avnet 등)
     - Vendor P/N + Lead Time
     - AEC-Q100/Q200 Grade
     - Lifetime (years, Vendor 공식)
     - EoL Risk Level (Low/Medium/High)
     - Unit Price (양산 기준)

3. **특수특성 표시** (HWE.2.BP3)
   - Safety-critical / Cybersecurity-critical / EMC-critical 부품 식별.
   - 특수특성 컬럼에 마킹 (♦ Safety / § Cyber / ¤ EMC).
   - 변경 시 회귀 시험 강제 적용.

4. **AVL 매칭 검증**
   - 모든 부품이 AVL 등재 여부 확인.
   - 미등재 부품 → Procurement 에 AVL 등록 요청.

5. **EoL Risk 분석**
   - Lifetime DB 조회 → Last Time Buy / NRND / EoL 상태 부품 식별.
   - High Risk 부품 → Second Source 부품 2종 이상 사전 확보.

6. **생산데이터 (Production Data) 패키징**
   - Gerber (RS-274X), Drill (Excellon), Pick&Place 파일 생성.
   - PCB 제조사 양식·DRC 요구사항 점검.

7. **BOM 및 생산데이터 검토**
   - HW Lead, Procurement, Production Eng., QA 합동 검토.
   - 검토 결과 → BOM v1.0 / 생산데이터 v1.0 승인.

8. **CM 베이스라인 등록** (SUP.8)
   - CM 시스템에 BOM·Gerber·Pick&Place·Drill 패키지 업로드.
   - Baseline Tag 부여 + 변경 ID 추적.

### 5.3 완료 조건 체크리스트
- [ ] BOM 모든 행 Manufacturer P/N 완전 기재
- [ ] 모든 부품 AEC-Q100/Q200 Grade 명시
- [ ] EoL/NRND/LTB 부품 0건 (또는 Second Source 확보)
- [ ] 특수특성 (Safety/Cyber/EMC) 마킹 완료
- [ ] AVL 매칭률 100%
- [ ] Gerber/Drill/Pick&Place 파일 패키징 완료
- [ ] PCB 제조사 DRC Pre-check Pass
- [ ] CM 베이스라인 Tag 발행
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **Procurement ([[PRO-ASPICE-01-06]])**: 부품 가용성·AVL·EoL 정보
- **CM (SUP.8)**: 베이스라인 등록 절차
- **Production Engineering**: 생산데이터 양식·DFM 검토
- **QA (SUP.1)**: 특수특성 검토
- **Safety Engineering**: Safety-critical 부품 검토

## 7. 주의사항 / 예외 처리

### 7.1 EoL 부품 발견
- BOM 작성 또는 검토 중 EoL/NRND 통지 수령 시:
  - 즉시 부품 영향 분석 (해당 회로·SW·기능 영향).
  - Second Source 부품 후보 2종 이상 식별 및 호환성 검토.
  - SUP.10 변경 절차 적용 (회로·PCB·BOM 동시 변경).
  - 안전 재고 (Safety Stock) 사전 확보.

### 7.2 AVL 미등재 부품
- AVL 미등재 부품 사용 필요 시:
  - Procurement 에 AVL 등록 요청 + Vendor 평가 (IATF 16949 인증 확인).
  - 등록 완료 전 BOM v1.0 발행 금지.
  - 긴급 시 임시 승인 (Conditional AVL) + 정식 등록 일정 명시.

### 7.3 특수특성 부품 변경
- Safety/Cyber/EMC 특수특성 부품 변경 시:
  - 회귀 시험 (Regression Test) 강제 (HWE.4 + SUP.9).
  - Safety Manager / Cybersecurity Engineer 공동 승인.
  - 변경 영향 분석서 첨부.

### 7.4 BOM 과 실 PCB 불일치
- 시제 PCB 수령 후 BOM 과 부품 불일치 발견 시:
  - 즉시 SUP.9 결함 등록 (Critical).
  - 시제 사용 중지 + 원인 분석 (PCB 제조사 또는 BOM 오류).
  - 차이 0 확인 후 재시제 또는 정정 BOM 발행.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-03-03-01_BOM]]
- 기록 폴더: `vault/08_REC_기록/HWE/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-HWE.2-BP3 / VWAY-SUP.8-*"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — BOM·생산데이터·CM 등록 통합 정의 | (대기) |
