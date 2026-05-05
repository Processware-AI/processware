---
type: WI
doc_id: "WI-ASPICE-01-02-04"
title: "SW 유닛 검증 (SWE.4)"
version: "0.1"
owner: "SW Engineer"
reviewer: "QA"
approver: "SW Lead"
scope: "유닛 시험 설계·실행·코드 커버리지 측정 + Pass/Fail 보고"
parent_pro: "[[PRO-ASPICE-01-02_소프트웨어공학프로세스]]"
related_tmp:
  - "[[TMP-ASPICE-01-02-04-01_유닛시험계획서및결과보고서]]"
related_rec: []
standards: ["Automotive SPICE 4.0", "ISO 26262"]
aspice_processes: ["SWE.4"]
entry_gate: "WI-ASPICE-01-02-03.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SWE.4, UnitTest, Coverage]
---

# SW 유닛 검증 업무지침 (WI-ASPICE-01-02-04)

> 상위 절차: [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] §5 단계 9
> ASPICE 매핑: SWE.4 (Software Unit Verification) — BP1~BP5

## 1. 업무 목적

각 SW 유닛(모듈/함수) 의 동작이 상세설계 사양을 충족함을 화이트박스 시험으로 입증하고, ISO 26262 ASIL 등급별 코드 커버리지(Statement / Branch / MC/DC) 를 달성한다.

## 2. 수행 주체

- **주 수행자**: SW Engineer
- **검토자**: QA, 동료(시험 케이스 리뷰)
- **승인자**: SW Lead

## 3. 범위

WI-ASPICE-01-02-03 의 유닛 코드 커밋 후부터 모든 유닛의 시험 + 커버리지 목표 달성 + 결과 보고서 등록까지 적용한다.

## 4. 입력 자료 / 산출물

- **Input**: Source Code, 상세설계서, SwRS (검증 대상 사양)
- **Output**: Unit Test Specification, Unit Test Code, Test Report, Coverage Report

## 5. 수행 절차

### 5.1 사전 준비
1. 단위 시험 프레임워크(Cantata, VectorCAST, GoogleTest) 환경 구성.
2. 커버리지 측정 도구 + Stub/Mock 라이브러리 준비.
3. ASIL 별 커버리지 목표 확정:
   - QM: Statement ≥ 90%
   - ASIL A/B: Statement 100%, Branch ≥ 90%
   - ASIL C: Statement 100%, Branch 100%
   - ASIL D: Statement 100%, Branch 100%, MC/DC 100%

### 5.2 수행 단계

1. **유닛 시험 케이스 설계** (SWE.4.BP1)
   - 함수별 정상·경계·예외 시나리오 도출.
   - Equivalence Partitioning + Boundary Value Analysis 적용.
   - 결과: TMP-ASPICE-01-02-04-01 §2 "시험 케이스".

2. **시험 케이스 리뷰** (SWE.4.BP2)
   - 동료 + QA 가 케이스의 충분성·정확성 검토.

3. **시험 코드 구현·실행** (SWE.4.BP3)
   - 시험 코드 작성 + Stub/Mock 구성.
   - 자동 실행 (CI 파이프라인) → 결과 자동 수집.
   - 결과: Test Report (Pass/Fail + 측정값).

4. **커버리지 측정·달성** (SWE.4.BP4)
   - ASIL 별 목표 달성 확인.
   - 미달 시 추가 시험 케이스 작성 → 재실행.
   - Dead Code 식별 시 SwRS 회귀 확인 (불필요 코드 제거 대상).

5. **결과 보고·이슈 이관** (SWE.4.BP5)
   - Fail 결함은 [[WI-ASPICE-01-08-01_문제등록및분류]] 로 등록.
   - 통과 모듈은 다음 단계(SWE.5) 인계.

### 5.3 완료 조건 체크리스트
- [ ] 모든 함수에 정상·경계·예외 케이스 작성
- [ ] 시험 케이스 동료 + QA 리뷰 완료
- [ ] ASIL 별 커버리지 목표 달성 (QM 90%, ASIL D MC/DC 100% 등)
- [ ] Dead Code 0건 (또는 사유 기록)
- [ ] 모든 Fail 결함 SUP.9 등록
- [ ] CI 파이프라인 자동 실행 결과 첨부
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **CM (SUP.8)**: 시험 코드 형상관리
- **QA (SUP.1)**: 시험 결과 검토
- **Build/CI**: 자동화 실행

## 7. 주의사항 / 예외 처리

### 7.1 커버리지 미달 (불가피)
- HW Dependent 코드, Defensive Code 등 시험 불가능 영역:
  - Justification 문서 작성 + Safety Engineer 승인.
  - 가능한 경우 HIL/Bench 통합 시험으로 보완 검증.

### 7.2 Stub/Mock 신뢰성 결여
- Stub/Mock 의 동작이 실제 모듈과 다를 위험:
  - Mock 명세서 별도 작성 + Architect 검토.
  - 통합 시험 단계에서 실제 동작 교차 확인.

### 7.3 시험 결과 무결성 위반
- 시험 결과 변조·삭제 의심:
  - CI 파이프라인 로그 + Git 커밋 이력으로 교차 검증.
  - 위반 확인 시 시험 재실행 + 책임자 조사.

### 7.4 Flaky Test (간헐적 실패)
- 동일 케이스가 비결정적으로 Pass/Fail:
  - 즉시 격리 (CI 에서 quarantine).
  - 24시간 내 RCA → 결정성 복구 또는 케이스 재설계.
  - 미해결 케이스의 결과는 신뢰할 수 없음 — 무효 처리.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-02-04-01_유닛시험계획서및결과보고서]]
- 작성예시: [[EX-ASPICE-01-02-04-01_유닛시험계획서및결과보고서_작성예시]]
- 기록 폴더: `vault/08_REC_기록/SWE.4/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SWE.4-PURPOSE-001 / VWAY-SWE.4-BP1~BP5"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SWE.4 BP1~BP5 + ASIL 커버리지 매트릭스 | (대기) |
