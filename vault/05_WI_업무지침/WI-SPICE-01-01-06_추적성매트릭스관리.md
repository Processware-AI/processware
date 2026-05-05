---
type: WI
doc_id: "WI-SPICE-01-01-06"
title: "추적성 매트릭스 관리 (StRS↔SyRS↔Architecture↔Test)"
version: "0.1"
owner: "System Engineer"
reviewer: "QA"
approver: "System Engineering Lead"
scope: "이해관계자~시스템~아키텍처~검증 단계의 양방향 추적성 매트릭스 작성·유지·검증"
parent_pro: "[[PRO-SPICE-01-01_시스템공학프로세스]]"
related_tmp:
  - "[[TMP-SPICE-01-01-06-01_시스템추적성매트릭스]]"
related_rec: []
standards: ["Automotive SPICE 4.0"]
aspice_processes: ["SYS.2.BP5", "SYS.3.BP5", "SYS.5.BP4"]
entry_gate: "WI-SPICE-01-01-01.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SYS, VWAY_Motors, Traceability]
---

# 추적성 매트릭스 관리 업무지침 (WI-SPICE-01-01-06)

> 상위 절차: [[PRO-SPICE-01-01_시스템공학프로세스]] §5 단계 7·12 + §7 KPI
> ASPICE 매핑: SYS.2.BP5, SYS.3.BP5, SYS.5.BP4 (Bidirectional Traceability)

## 1. 업무 목적

이해관계자 요구사항(StRS) 부터 시스템 요구사항(SyRS), 시스템 아키텍처(SAD/ICD), 검증 결과(Verification) 까지의 **양방향 추적성** 을 매트릭스 형태로 관리하여, 누락·고아 항목을 조기 검출하고 변경 영향 분석의 신뢰성을 확보한다.

## 2. 수행 주체

- **주 수행자**: System Engineer (추적성 관리 책임)
- **검토자**: QA, Safety Engineer (ASIL 추적성)
- **승인자**: System Engineering Lead

## 3. 범위

WI-SPICE-01-01-01 의 StRS 베이스라인 등록 후부터 SYS.5 검증 보고서 등록 시점까지의 모든 단계에 횡단 적용한다. 다른 시스템공학 WI 와 병렬로 진행되며, 각 베이스라인 등록 시마다 매트릭스 갱신·검증을 수행한다.

## 4. 입력 자료 / 산출물

- **Input**
  - StRS, SyRS, SAD, ICD, 검증 시나리오/결과
  - 분배 매트릭스 (SW/HW/ML)

- **Output**
  - System Traceability Matrix (STM) v{n} — 마일스톤별 갱신
  - 추적성 GAP 보고서 (누락·고아 항목)
  - 변경 영향 분석 보고서 (요청 시)

## 5. 수행 절차

### 5.1 사전 준비

1. 추적성 도구(IBM DOORS / Polarion / Jama Connect / 자체 PLM) 의 데이터 모델을 확정한다.
2. 추적성 link 타입을 정의한다: `derives_from`, `satisfies`, `verifies`, `allocated_to`.
3. 마일스톤별 매트릭스 발행 일정을 PM 과 합의한다.

### 5.2 수행 단계

1. **StRS↔SyRS link** (SYS.2.BP5)
   - WI-SPICE-01-01-02 완료 시 각 SyRS 의 `derives_from: [STK-...]` 등록.
   - StRS 중 SyRS 로 분해되지 않은 항목 = "고아 StRS" 로 표시.
   - 결과: TMP-SPICE-01-01-06-01 §1.

2. **SyRS↔Architecture link** (SYS.3.BP5)
   - WI-SPICE-01-01-03 완료 시 각 아키텍처 요소의 `satisfies: [SYS-...]` 등록.
   - SyRS 중 어느 아키텍처에도 매핑되지 않은 항목 = "고아 SyRS" 표시.
   - 결과: TMP-SPICE-01-01-06-01 §2.

3. **SyRS↔Verification link** (SYS.5.BP4)
   - WI-SPICE-01-01-05 완료 시 각 검증 케이스의 `verifies: [SYS-...]` 등록.
   - 미검증 SyRS 식별.
   - 결과: TMP-SPICE-01-01-06-01 §3.

4. **분배 추적성** (SYS.3.BP4 후속)
   - 각 SyRS 가 SW/HW/ML 중 어느 도메인 컴포넌트에 분배되었는지 link.
   - 후속 SWE/HWE/MLE 추적성과 자동 연결되도록 설정.

5. **GAP 분석** (정기)
   - 마일스톤마다 자동 GAP 분석 실행 → 누락 항목·고아 항목 보고.
   - 누락 ≥ 5% 발생 시 즉시 PM·QA 통보.
   - 결과: TMP-SPICE-01-01-06-01 §4 "GAP 보고서".

6. **변경 영향 분석 지원**
   - StRS/SyRS/Architecture 변경 요청 시 추적성 매트릭스 기반 영향 범위 자동 도출.
   - 5 영업일 이내 회신을 SLA 로 한다.

7. **베이스라인 발행**
   - 마일스톤별 STM v{n} 발행 → CM 베이스라인 + MAT-001 등록.

### 5.3 완료 조건 체크리스트

- [ ] StRS↔SyRS 양방향 link 커버리지 ≥ 95%
- [ ] SyRS↔Architecture 양방향 link 커버리지 ≥ 95%
- [ ] SyRS↔Verification link 커버리지 ≥ 95% (ASIL D 는 100%)
- [ ] 고아 항목 0건 (또는 사유 기록)
- [ ] 분배 매트릭스가 추적성 도구에 동기화 완료
- [ ] GAP 보고서 발행 + PM 회신 완료
- [ ] STM v{n} 베이스라인 등록 + MAT-001 갱신

## 6. 인터페이스 부서

- **PM (MAN.3)**: GAP 결과 의사결정
- **QA (SUP.1)**: 추적성 검토 게이트
- **CM (SUP.8)**: STM 베이스라인
- **SW/HW/ML Lead**: 후속 도메인 추적성 인계

## 7. 주의사항 / 예외 처리

### 7.1 도구 마이그레이션 중 데이터 손실
- 추적성 도구 변경(예: DOORS → Polarion) 시 link 손실 위험:
  - 마이그레이션 전 STM v{n} 스냅샷 보존.
  - 마이그레이션 후 자동 비교 스크립트로 link 무결성 검증.
  - 손실 link 발견 시 수동 복구 + 검증.

### 7.2 도메인(SW/HW/ML) 추적성 지연
- SWE/HWE/MLE 도메인의 추적성 link 가 미동기화 상태:
  - System Engineer 가 도메인 Lead 에 정기(주 1회) 동기화 요청.
  - 2주 이상 지연 시 PM 에스컬레이션.

### 7.3 추적성 위반 (변경 후 link 누락)
- 변경 후 link 갱신을 누락한 산출물 발견 시:
  - 즉시 변경 작성자에게 통보 + 5 영업일 내 갱신 요청.
  - 회신 미수신 시 SUP.9 결함 등록.

### 7.4 고아 SyRS 의 처리
- SyRS 중 어떤 아키텍처에도 매핑되지 않은 항목 발견 시:
  - 1) 시험가능성 결여 → SyRS 재정의 또는 강등.
  - 2) 아키텍처 누락 → SAD 보완.
  - 3) 범위 외 → SyRS 에 `out_of_scope` 태그 + StRS 회귀 협의.
  - 모든 결정은 회의록·이메일로 증적화.

## 8. 연계 템플릿 / 기록

- 템플릿: [[TMP-SPICE-01-01-06-01_시스템추적성매트릭스]]
- 작성예시: [[EX-SPICE-01-01-06-01_시스템추적성매트릭스_작성예시]]
- 기록 폴더: `vault/08_REC_기록/SYS_Traceability/`

## 9. 출처 (source_citation)

```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SYS.2-BP5 / VWAY-SYS.3-BP5 / VWAY-SYS.5-BP4"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력

| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — 추적성 횡단 관리 + GAP 분석 절차 | (대기) |
