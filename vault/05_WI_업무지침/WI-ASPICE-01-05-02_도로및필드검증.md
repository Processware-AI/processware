---
type: WI
doc_id: "WI-ASPICE-01-05-02"
title: "도로 및 필드 검증 수행 (VAL.1.BP3)"
version: "0.1"
owner: "Validation Engineer"
reviewer: "Validation Lead / Safety Engineer / QA"
approver: "Validation & Release Lead"
scope: "Validation Plan/Spec 기반 실차·시뮬레이터·필드 환경 시험 실행 및 결과 기록"
parent_pro: "[[PRO-ASPICE-01-05_검증및인도프로세스]]"
related_tmp:
  - "[[TMP-ASPICE-01-05-02-01_검증시험결과보고서]]"
related_rec: []
standards: ["Automotive SPICE 4.0"]
aspice_processes: ["VAL.1"]
entry_gate: "WI-ASPICE-01-05-01.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, VAL, Validation, Road, Field]
---

# 도로 및 필드 검증 수행 업무지침 (WI-ASPICE-01-05-02)

> 상위 절차: [[PRO-ASPICE-01-05_검증및인도프로세스]] §5 단계 3~4
> ASPICE 매핑: VAL.1.BP3 (Perform validation in operating environment)

## 1. 업무 목적

Validation Plan 과 Validation Spec 에 정의된 도로·필드·시뮬레이터 시나리오를 통제된 환경에서 수행하고, 객관적 결과를 기록한다. 사용자 의도(Stakeholder Need) 충족 증거를 확보하고, 편차 발견 시 SUP.9 결함 절차로 이관한다.

## 2. 수행 주체
- **주 수행자**: Validation Engineer
- **검토자**: Validation Lead, Safety Engineer, QA
- **승인자**: Validation & Release Lead

## 3. 범위

WI-ASPICE-01-05-01 (검증 계획 수립) 완료 후, OEM 고객 승인(WI-ASPICE-01-05-03) 진입 전까지의 도로·필드·시뮬레이터 시험 실행 전 구간에 적용한다.

## 4. 입력 자료 / 산출물
- **Input**: Validation Plan, Validation Spec(시나리오 목록), 환경 구성 기록(Env. Config Record), 대상 차량/시뮬레이터 식별, 안전 운전자 자격
- **Output**: Validation Report(시험 결과 + 증적), 결함 보고(편차 발견 시 SUP.9 NCR), 시험 데이터 로그(CAN/Camera/IMU 등)

## 5. 수행 절차

### 5.1 사전 준비
1. Validation Plan/Spec 최신 베이스라인(CM 등록본) 확인.
2. 시험 차량(Mule/EVT/PVT) Lot No. 와 SW Build ID 일치 확인 → 불일치 시 시험 중단.
3. 시험장 사용 허가(KATRI 또는 OEM Proving Ground) 와 안전 절차 브리핑 완료.
4. 데이터 로거(VBOX, RTK-GPS, CAN Logger) 캘리브레이션 유효기간 확인.
5. 안전 운전자(Safety Driver) 면허·트레이닝 이수 증빙 확인.

### 5.2 수행 단계
1. **검증 환경 구성** (VAL.1.BP2 연계)
   - 실차 시험: 시험 차량 캘리브레이션, 센서 정렬, 통신 채널 점검.
   - 시뮬레이터: HIL/DIL/SIL 환경 부트, 시나리오 시드 검증.
   - 필드: 도로 폐쇄 또는 공도 구간 사전 답사 + 통신 음영 확인.

2. **시나리오 실행** (VAL.1.BP3)
   - Spec 의 시나리오 ID 순서대로 실행.
   - 각 시나리오 실행 전 Pre-condition (차속·기어·기상) 만족 확인.
   - 자동 데이터 로깅 + 안전 운전자 음성 코멘트 동기화.
   - 안전 위험 발생 시 즉시 종료 → 사고 보고서 작성.

3. **결과 판정** (VAL.1.BP3)
   - Pass/Fail 기준은 Spec 의 정량 기준에 따름(예: AEB 정지 거리, LKA 차선 이탈량).
   - 주관 평가(체감 편차) 는 별도 컬럼에 분리 기록.
   - 편차 발견 시 SUP.9 NCR 발행 + 결함 등록.

4. **결과 기록 및 검토** (VAL.1.BP3)
   - Validation Report 작성: 시나리오별 Pass/Fail, 증적 파일 경로, 운전자 코멘트.
   - 시험 데이터 백업(Raw + Processed) → CM 등록.
   - Validation Lead 검토 + Safety Engineer 안전 영향 검토.

5. **미합의 항목 추적**
   - Pass 가 아닌 모든 항목은 Open Issue 로 등록 → WI-ASPICE-01-05-03(고객 승인) 협의 대상으로 이관.

### 5.3 완료 조건 체크리스트
- [ ] Validation Spec 의 모든 시나리오 실행 (Skip 사유 명시 시 예외)
- [ ] 시나리오 커버리지 ≥ 95% (PRO-05 §7 통제점)
- [ ] 모든 시험 데이터(Raw/Processed) CM 등록
- [ ] Pass/Fail 판정 근거 정량 기준 매핑
- [ ] 편차 항목 전수 SUP.9 NCR 발행 확인
- [ ] Safety Engineer 안전 영향 검토 결과 첨부
- [ ] Validation Report v1.0 발행 + Validation & Release Lead 승인
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **Validation Plan 작성팀(WI-05-01)**: 시나리오·환경 정의 인계
- **Safety Engineering**: 시험 중 안전 위험 평가 + ASIL 영향 검토
- **CM (SUP.8)**: 시험 SW Build ID·차량 Lot 일치 확인
- **SUP.9 (Problem Resolution)**: 편차 발견 시 NCR 이관
- **Procurement**: 시험장 사용 계약 및 보험

## 7. 주의사항 / 예외 처리

### 7.1 시험 차량 SW Build 불일치
- 시험 직전 SW Build ID 가 베이스라인과 다를 경우:
  - 즉시 시험 중단.
  - CM 시스템에서 정본 Build 재플래싱.
  - 재시험 일정 조정 + Validation Lead 보고.

### 7.2 안전 위험 발생 (운전자 위협)
- 시험 중 차량 거동 이상 또는 안전 운전자 위협 감지:
  - 즉시 시험 종료(Emergency Stop).
  - 사고/Near-miss 보고서 작성 (24h 이내).
  - Safety Engineer 와 결함 분석 → SUP.9 우선순위 P1 등록.
  - 동일 결함 재현 가능성 검증 전까지 동일 시나리오 재시험 금지.

### 7.3 기상 조건 미충족
- Spec 에 정의된 기상 조건(우천·야간·역광) 충족 불가:
  - 대기 또는 일정 재조정.
  - 시뮬레이터 보완 시험 가능성 검토 → Validation Lead 승인 후 적용.
  - 보완 시험은 Spec 에 변경 이력 기록.

### 7.4 시험 데이터 손실/변조
- 데이터 로거 오작동·저장 매체 손상:
  - 미백업 데이터는 시험 무효 처리.
  - 동일 시나리오 재실행 + 데이터 백업 절차 강화(이중 저장).
  - SUP.9 절차로 데이터 무결성 부적합 등록.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-05-02-01_검증시험결과보고서]]
- 작성예시: [[EX-ASPICE-01-05-02-01_검증시험결과보고서_작성예시]]
- 기록 폴더: `vault/08_REC_기록/VAL/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-VAL.1-BP3"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — VAL.1.BP3 도로/필드 검증 절차 정의 | (대기) |
