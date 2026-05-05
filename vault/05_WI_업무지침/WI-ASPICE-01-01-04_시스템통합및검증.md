---
type: WI
doc_id: "WI-ASPICE-01-01-04"
title: "시스템 통합 및 통합 시험 (SYS.4)"
version: "0.1"
owner: "System Engineer"
reviewer: "QA / SW·HW·ML Lead"
approver: "System Engineering Lead"
scope: "SW/HW/ML 산출물 → 통합 전략·시험 설계·통합·시험 실행"
parent_pro: "[[PRO-ASPICE-01-01_시스템공학프로세스]]"
related_tmp:
  - "[[TMP-ASPICE-01-01-04-01_통합시험계획서및결과보고서]]"
related_rec: []
standards: ["Automotive SPICE 4.0"]
aspice_processes: ["SYS.4"]
entry_gate: "WI-ASPICE-01-01-03.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SYS.4, VWAY_Motors, Integration, HIL]
---

# 시스템 통합 및 통합 시험 업무지침 (WI-ASPICE-01-01-04)

> 상위 절차: [[PRO-ASPICE-01-01_시스템공학프로세스]] §5 단계 13~15
> ASPICE 매핑: SYS.4 (System Integration and Integration Test) — BP1~BP5

## 1. 업무 목적

SW/HW/ML 도메인에서 전달된 컴포넌트를 시스템 아키텍처에 따라 단계적으로 통합하고, 통합 단계마다 정의된 시험을 실행하여 결과를 기록·보고하며, 결함은 [[PRO-ASPICE-01-08_문제및변경관리프로세스]] 로 이관한다.

## 2. 수행 주체

- **주 수행자**: System Engineer (통합 책임)
- **공동 수행자**: SW/HW/ML Lead (도메인 산출물 인계)
- **검토자**: QA
- **승인자**: System Engineering Lead

## 3. 범위

WI-ASPICE-01-01-03 의 SAD/ICD 베이스라인 등록 후, SW/HW/ML 도메인에서 첫 통합 가능 컴포넌트를 인계받은 시점부터 통합 시험 결과 보고서 v1.0 등록까지 적용한다.

## 4. 입력 자료 / 산출물

- **Input**
  - SAD/ICD v1.0
  - SW 컴포넌트 빌드 산출물 ([[PRO-ASPICE-01-02_소프트웨어공학프로세스]])
  - HW 시제품 ([[PRO-ASPICE-01-03_하드웨어공학프로세스]])
  - ML 모델 산출물 ([[PRO-ASPICE-01-04_머신러닝공학프로세스]])
  - 분배 매트릭스

- **Output**
  - Integration Strategy v1.0
  - Integration Test Specification v1.0
  - Integration Test Report (실행본)
  - 통합 결함 리포트 (→ SUP.9 이관)

## 5. 수행 절차

### 5.1 사전 준비

1. 통합 환경(HIL bench, ECU 시제품, 측정 장비) 가용성을 점검한다.
2. SW/HW/ML 산출물의 인계 체크리스트를 확정한다 (버전·해시·릴리즈 노트).
3. 통합 시험 자동화 도구(CANoe, dSPACE) 의 시험 시나리오 라이브러리를 준비한다.

### 5.2 수행 단계

1. **통합 전략 수립** (SYS.4.BP1)
   - 통합 순서 결정: bottom-up / top-down / risk-driven 중 선택.
   - 통합 단계(Stage) 별 인터페이스·기능 범위 정의.
   - 결과: TMP-ASPICE-01-01-04-01 §2 "통합 전략".

2. **통합 시험 설계** (SYS.4.BP2)
   - 각 통합 단계마다 검증 측정치(Verification Measure) 정의.
   - 시험 케이스 = 입력 + 기대 출력 + 합격 기준.
   - ASIL D 인터페이스는 정상·경계·예외 시나리오 강제.
   - 결과: TMP-ASPICE-01-01-04-01 §3 "통합 시험 케이스".

3. **요소 인계 검증** (SYS.4.BP3 사전)
   - SW/HW/ML 산출물 수령 시 인계 체크리스트로 검증.
   - 누락·불일치 발견 시 인계 거부 → 도메인에 회신.

4. **단계적 통합·시험 실행** (SYS.4.BP3/4)
   - 통합 단계별로 컴포넌트 결합 → 시험 실행 → 결과 기록.
   - 각 시험은 Pass/Fail 자동 판정 + 측정값 기록.
   - Fail 발견 시 즉시 [[WI-ASPICE-01-08-01_문제등록및분류]] 로 결함 등록.
   - 결과: TMP-ASPICE-01-01-04-01 §4 "시험 결과 로그".

5. **회귀 시험 운영** (SYS.4.BP4 후속)
   - 수정된 컴포넌트 재인계 시 영향 범위 회귀 시험 실행.
   - 자동화 가능한 시험은 CI 파이프라인으로 운영.

6. **통합 결과 보고** (SYS.4.BP5)
   - 통합 단계 종료 시 보고서 작성: 통과율, 결함 수, 잔여 리스크.
   - QA 검토 후 다음 단계(SYS.5 시스템 검증) 로 인계.

### 5.3 완료 조건 체크리스트

- [ ] 통합 전략 문서에 단계·순서·종료 기준 명시
- [ ] 통합 시험 케이스가 모든 인터페이스를 커버 (≥ 95%)
- [ ] ASIL D 인터페이스의 정상·경계·예외 시험 100% 실행
- [ ] 모든 Fail 결함이 SUP.9 에 등록되고 추적 가능
- [ ] 회귀 시험 실행 결과 무결성 확인
- [ ] 통합 결과 보고서 QA 승인 완료
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서

- **SW/HW/ML Lead**: 산출물 인계
- **QA (SUP.1)**: 통합 결과 검토 + 다음 단계 승인
- **CM (SUP.8)**: 통합 빌드 형상 등록
- **PM (MAN.3)**: 통합 일정 추적

## 7. 주의사항 / 예외 처리

### 7.1 인계 산출물 품질 미달
- SW/HW/ML 인계물이 체크리스트를 만족하지 않을 때:
  - 인계 거부 → 도메인에 결함 통지 (5 영업일 내 재인계).
  - 본 절차 일정 영향 평가 → PM 보고.
  - 반복(2회 이상) 발생 시 도메인 RCA 요청 (SUP.9).

### 7.2 HIL/Bench 가용성 부족
- 시험 환경 부족으로 일정 지연 위험 시:
  - 외부 임대 또는 야간/주말 이용 검토.
  - 시뮬레이션(MIL/SIL) 으로 1차 사전 검증, HW-in-the-Loop 은 우선순위 시험만 실행.

### 7.3 결함 폭증 (회귀 폭주)
- 단일 변경으로 회귀 시험 다수 실패 시:
  - 즉시 통합 중단 + 변경 롤백.
  - 도메인에 RCA 요청 후 재변경 승인 후 재개.

### 7.4 안전 관련 결함
- ASIL C/D 결함 발견 시:
  - 즉시 Safety Engineer 통보.
  - Safety Manager 승인 없이 Workaround 적용 금지.
  - 결함 폐쇄 전 시스템 검증(SYS.5) 진입 금지.

## 8. 연계 템플릿 / 기록

- 템플릿: [[TMP-ASPICE-01-01-04-01_통합시험계획서및결과보고서]]
- 작성예시: [[EX-ASPICE-01-01-04-01_통합시험계획서및결과보고서_작성예시]]
- 기록 폴더: `vault/08_REC_기록/SYS.4/`

## 9. 출처 (source_citation)

```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SYS.4-PURPOSE-001 / VWAY-SYS.4-BP1~BP5"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력

| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SYS.4 BP1~BP5 + HIL/회귀 운영 통합 | (대기) |
