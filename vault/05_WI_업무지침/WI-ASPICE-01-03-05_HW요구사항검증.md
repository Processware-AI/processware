---
doc_id: "WI-ASPICE-01-03-05"
title: "HW 요구사항 검증 (HWE.4)"
type: WI
version: "0.1"
status: draft
owner: "HW Verification Engineer"
reviewer: "System Engineer / Safety Engineer / QA"
approver: "HW Lead"
scope: "HwRS 요구사항 대비 시제/DV 시험 → 합격 판정 → HWE.4 완료"
scope_type: project
scope_code: ASPICE
domain: ASPICE
parent_pro: "[[PRO-ASPICE-01-03_하드웨어공학프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-03-05-01_HW요구사항검증보고서]]"]
aspice_processes: ["HWE.4"]
entry_gate: "WI-ASPICE-01-03-04.status == done"
standards: ["Automotive SPICE 4.0"]
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, HWE.4, DV, RequirementsVerification]
---

# WI-ASPICE-01-03-05 — HW 요구사항 검증 (HWE.4)

## 1. 업무 목적
HW 요구사항 명세서(HwRS)에 정의된 모든 요구사항이 실제 시제품(prototype) 및 설계 검증(DV, Design Verification) 시험을 통해 충족됨을 객관적 증적으로 입증한다. ASPICE 4.0 HWE.4 의 BP1~BP6 활동을 수행하여 HW 인도 전 합격 판정을 확정한다.

## 2. 수행 주체
- **주 수행자**: HW Verification Engineer
- **검토자**: System Engineer / Safety Engineer / QA
- **승인자**: HW Lead

## 3. 범위
- 대상: HwRS 등록 요구사항 전체(전기·기계·환경·EMC·기능안전·통신)
- 시험 단계: DV 시제품 시험(샘플 단위 시험 + 통합 시험)
- 제외: 양산 검증(PV)·고객 인수시험은 별도 PRO 적용
- 적용 표준: Automotive SPICE 4.0 HWE.4, ISO 26262-5 (ASIL D 적용 항목)

## 4. 입력 자료 / 산출물
**입력 자료**
- HW 요구사항 명세서(HwRS) — WI-ASPICE-01-03-01 산출물
- HW 시험 명세서(Test Specification) — WI-ASPICE-01-03-04 산출물
- 시험 환경·계측 장비 교정 기록
- DV 시제품 빌드 정보(CM 베이스라인)

**산출물**
- HW 요구사항 검증 보고서(TMP-ASPICE-01-03-05-01)
- 시험 원시 데이터(raw log) 일체 — CM 등록
- 결함 등록부(SUP.9 연계) 갱신
- 추적성 매트릭스(HwRS ↔ 시험케이스) 갱신

## 5. 수행 절차

### 5.1 사전 준비
1. HwRS 최신 베이스라인 및 시험 명세서 버전 일치 확인.
2. DV 시제품 식별번호와 CM 베이스라인 일치 확인.
3. 시험 환경·계측 장비 교정 유효기간 확인.
4. 안전 요구사항(ASIL D 항목) 별도 식별 및 시험 우선순위 부여.

### 5.2 수행 단계
1. **시험 케이스 실행** (HWE.4 BP1) — 각 HwRS 요구사항에 매핑된 시험 케이스를 시험 명세서에 따라 순차 실행한다.
2. **시험 결과 기록** (HWE.4 BP2) — 측정값·합부 판정·환경 조건을 raw log 와 보고서에 기록한다.
3. **HwRS ↔ 시험케이스 추적성 갱신** (HWE.4 BP3) — 양방향 추적성 매트릭스에 시험 결과를 반영한다.
4. **ASIL 커버리지 검증** (HWE.4 BP4) — ASIL D 요구사항이 100% 커버됨을 확인. 미달 시 즉시 에스컬레이션.
5. **불합격 항목 처리** (HWE.4 BP5) — 결함은 SUP.9 결함관리 프로세스로 등록하고 재시험 계획을 수립한다.
6. **종합 판정** (HWE.4 BP6) — Pass/Conditional Pass/Fail 중 하나로 판정한다. Conditional Pass 는 잔여 결함 처리 계획을 첨부한다.
7. **검증 보고서 발행** — 검토자 회람 후 승인자 결재를 득한다.
8. **CM 등록 및 베이스라인 태깅** — 최종 보고서·raw log 를 CM 시스템에 등록한다.

### 5.3 완료 조건 체크리스트
- [ ] HwRS 모든 요구사항이 시험 케이스에 매핑되어 있다.
- [ ] 모든 시험 케이스가 실행되고 결과가 기록되었다.
- [ ] ASIL D 요구사항 100% Pass 가 확인되었다.
- [ ] 불합격 항목이 SUP.9 에 등록되고 처리 계획이 수립되었다.
- [ ] 양방향 추적성 매트릭스가 갱신되었다.
- [ ] 종합 판정이 결재 완료되었다.
- [ ] 검증 보고서·raw log 가 CM 등록되었다.
- [ ] [[MAT-001_문서관리대장]] 갱신 완료.

## 6. 인터페이스 부서
- 시스템 엔지니어링: 요구사항 추적성 일관성 확인
- 기능안전팀: ASIL 항목 평가 및 안전 케이스 갱신
- QA: 검증 활동 독립 감사
- CM: 시제품·산출물 베이스라인 관리
- SUP.9 결함관리팀: 결함 등록·추적

## 7. 주의사항 / 예외 처리

### 7.1 안전 요구사항(ASIL D) 미달
ASIL D 요구사항이 1건이라도 Fail 또는 Conditional Pass 인 경우 즉시 HW Lead·Safety Engineer 에 에스컬레이션하며, HW 인도를 중단하고 설계 변경(HWE.2 회귀) 또는 재검증을 결정한다.

### 7.2 시험 환경 이상
시험 중 계측 장비 오작동·교정 만료가 확인되면 해당 시험 결과는 무효 처리하고 환경 정상화 후 전량 재시험한다.

### 7.3 시제품-베이스라인 불일치
DV 시제품이 CM 베이스라인과 일치하지 않으면(부품 변경·임시 패치 포함) 즉시 시험을 중단하고 CM 동기화 후 재개한다.

### 7.4 추적성 누락 발견
시험 도중 HwRS 에는 있으나 시험 케이스가 없는 요구사항이 발견되면 결함으로 등록하고 시험 명세서를 보완한 후 재실행한다.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-03-05-01_HW요구사항검증보고서]]
- 작성예시: [[EX-ASPICE-01-03-05-01_HW요구사항검증보고서_작성예시]]
- 상위 절차: [[PRO-ASPICE-01-03_하드웨어공학프로세스]]
- 결함관리: SUP.9 결함관리 프로세스
- 추적성: [[MAT-007_요구사항추적매트릭스]]

## 9. 출처
```yaml
source_citation:
  - file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    section: "HWE.4 / ASPICE 4.0"
    accessed: "2026-05-06"
standards:
  - "Automotive SPICE 4.0 — HWE.4 Hardware Verification"
  - "ISO 26262-5:2018 — Hardware level"
```

## 10. 개정 이력
| 버전 | 일자 | 변경 내용 | 승인자 |
|------|------|-----------|--------|
| 0.1 | 2026-05-06 | 최초 작성 (Draft) | HW Lead |
