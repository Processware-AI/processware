---
type: WI
doc_id: "WI-ASPICE-01-03-01"
title: "HW 요구사항 분석 및 설계 통합 (HWE.1+HWE.2)"
version: "0.1"
owner: "HW Engineer"
reviewer: "HW Architect / Safety Engineer / EMC Engineer"
approver: "HW Lead"
scope: "SyRS·SAD HW 분배 → HW 요구사항(HwRS) → 회로/PCB/BOM 설계"
parent_pro: "[[PRO-ASPICE-01-03_하드웨어공학프로세스]]"
related_tmp: []
related_rec: []
standards: ["Automotive SPICE 4.0", "ISO 26262", "AEC-Q100", "IEC 61000 EMC"]
aspice_processes: ["HWE.1", "HWE.2"]
entry_gate: null
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, HWE, BOM, EMC, AEC-Q100]
---

# HW 요구사항 분석 및 설계 통합 업무지침 (WI-ASPICE-01-03-01)

> 상위 절차: [[PRO-ASPICE-01-03_하드웨어공학프로세스]] §5
> ASPICE 매핑: HWE.1 + HWE.2 (HW Requirements Analysis + HW Design)

## 1. 업무 목적

SYS.3 에서 분배된 HW 요구사항을 정제하여 HwRS 를 작성하고, 이를 회로도·PCB Layout·BOM 으로 구체화한다. AEC-Q100 부품 사용·EMC·내환경 조건을 준수한다.

## 2. 수행 주체
- **주 수행자**: HW Engineer
- **검토자**: HW Architect, Safety Engineer, EMC Engineer, QA
- **승인자**: HW Lead

## 3. 범위
SAD/ICD 의 HW 분배분 인계 시점부터 HW 시제품 제작 가능 상태(BOM v1.0 + Gerber 발행) 까지 적용한다.

## 4. 입력 자료 / 산출물
- **Input**: SyRS, SAD/ICD, HW 분배 매트릭스
- **Output**: HwRS, 회로도(Schematic), PCB Layout, BOM v1.0, EMC/내환경 분석서

## 5. 수행 절차

### 5.1 사전 준비
1. 회로/PCB 설계 도구(Altium, KiCad, OrCAD) 라이선스·라이브러리 확인.
2. AEC-Q100/Q200 인증 부품 라이브러리 갱신 확인.

### 5.2 수행 단계
1. **HW 요구사항 도출** (HWE.1.BP1~3)
   - 기능: 입출력·전원·통신.
   - 비기능: 동작 온도(-40~+85°C 또는 +105°C), EMC, 진동, IP 등급.
   - 결과: HwRS.

2. **분류·우선순위·추적성** (HWE.1.BP4~6)
   - ASIL 상속, 시험가능성, SyRS↔HwRS 양방향 link.

3. **회로 설계** (HWE.2.BP1)
   - 핵심 IC, 전원 회로, 통신 회로(CAN/Ethernet PHY) 설계.
   - 모든 부품 AEC-Q100/Q200 인증 + Lifetime 확인.

4. **PCB Layout** (HWE.2.BP2)
   - 신호 무결성·전원 무결성·EMC 가이드라인 준수.
   - Safety-critical 신호 분리 + 차폐.

5. **BOM 작성** (HWE.2.BP3)
   - 모든 부품 Manufacturer P/N + Vendor + Lifetime + Lead Time.
   - End-of-Life (EoL) 부품 사용 금지.

6. **EMC/내환경 사전 분석** (HWE.2.BP4)
   - 시뮬레이션 + Pre-compliance 분석서 작성.

### 5.3 완료 조건 체크리스트
- [ ] HwRS 의 모든 항목 ASIL 상속 명시
- [ ] SyRS↔HwRS 양방향 추적성 ≥ 95%
- [ ] 모든 부품 AEC-Q100/Q200 인증 확인
- [ ] EoL 부품 0건
- [ ] PCB Layout DRC (Design Rule Check) Pass
- [ ] EMC 사전 분석서 첨부
- [ ] BOM v1.0 + Gerber 발행 + CM 등록
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **System Engineering**: SyRS 협의
- **SW Lead**: HW-SW 인터페이스 합의
- **Procurement ([[PRO-ASPICE-01-06]])**: 부품 가용성·Lifetime
- **Safety Engineering**: ASIL 상속 검토

## 7. 주의사항 / 예외 처리

### 7.1 EoL 부품 발견
- 설계 진행 중 EoL 통지 수령 시:
  - 즉시 대체 부품 식별 + 호환성 검토.
  - 변경 영향 분석 (회로/PCB/펌웨어 영향).
  - SUP.10 변경 절차 적용.

### 7.2 EMC Pre-compliance 미달
- 시뮬레이션에서 EMC 한계 초과:
  - 1) 차폐·필터 추가. 2) PCB Layout 재설계. 3) IC 변경.
  - 미해결 시 일정 영향 분석 + PM 보고.

### 7.3 부품 수급 위기
- 글로벌 반도체 부족 등으로 부품 입수 불가:
  - 대체 부품 2종 이상 미리 검증 (Second Source).
  - 안전 재고 확보 (Procurement 협의).

### 7.4 ASIL D 안전 회로 설계
- ASIL D 회로:
  - 다중화·다양성 설계 강제.
  - Safety Manager 공동 검토.
  - HW Failure Rate 분석서 (FIT) 첨부.

## 8. 연계 템플릿 / 기록
- 기록 폴더: `vault/08_REC_기록/HWE/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-HWE.1-* / VWAY-HWE.2-*"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — HWE.1+2 통합 (요구사항+설계) | (대기) |
