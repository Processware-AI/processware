---
type: WI
doc_id: "WI-ASPICE-01-05-03"
title: "OEM 고객 승인 (VAL.1.BP4)"
version: "0.1"
owner: "Release Manager"
reviewer: "Validation Lead / QA / Project Manager"
approver: "Validation & Release Lead"
scope: "검증 결과를 OEM 에 제출하여 sign-off 획득 및 미합의 항목 추적"
parent_pro: "[[PRO-ASPICE-01-05_검증및인도프로세스]]"
related_tmp:
  - "[[TMP-ASPICE-01-05-03-01_고객승인서]]"
related_rec: []
standards: ["Automotive SPICE 4.0"]
aspice_processes: ["VAL.1"]
entry_gate: "WI-ASPICE-01-05-02.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, VAL, Customer, Approval, Sign-off]
---

# OEM 고객 승인 업무지침 (WI-ASPICE-01-05-03)

> 상위 절차: [[PRO-ASPICE-01-05_검증및인도프로세스]] §5 단계 5
> ASPICE 매핑: VAL.1.BP4 (Provide validation results to relevant stakeholders)

## 1. 업무 목적

검증 결과를 OEM 에 공식 제출하고, 고객 검토 회의를 주관하여 양산 인도 전 sign-off 를 획득한다. 미합의 항목은 추적 관리 후 해소·합의에 도달한다. 승인서는 형상관리(SUP.8) 베이스라인에 등록한다.

## 2. 수행 주체
- **주 수행자**: Release Manager
- **검토자**: Validation Lead, QA, Project Manager
- **승인자**: Validation & Release Lead (내부) + OEM Customer Sign-off (외부)

## 3. 범위

WI-ASPICE-01-05-02 (도로/필드 검증) 완료 후 Validation Report 발행 시점부터 OEM Approval Record 베이스라인 등록까지 적용한다.

## 4. 입력 자료 / 산출물
- **Input**: Validation Report (v1.0 이상), Validation Plan/Spec, Open Issue 목록, OEM RFQ/계약 요건
- **Output**: OEM Approval Record (sign-off 문서), 회의록(Customer Review Minutes), 미합의 항목 추적표, CM 등록 증적

## 5. 수행 절차

### 5.1 사전 준비
1. Validation Report 의 OEM 제출본(영문/한글) 준비.
2. OEM 측 Approval 담당자(Decision Maker) SPOC 확인.
3. 회의 일정·장소·참석자 사전 합의 (대면/화상).
4. NDA·기밀자료 분류 등급 확인 → 외부 공유 가능 형태로 정제.

### 5.2 수행 단계
1. **검증 결과 공식 제출** (VAL.1.BP4)
   - Validation Report + 첨부 증적(샘플 데이터) OEM 포털/이메일 송부.
   - 송부 증적(타임스탬프·수신 확인) 보존.

2. **고객 검토 회의 주관**
   - Agenda: ① 시나리오 커버리지 요약 ② Pass/Fail 결과 ③ Open Issue 협의 ④ Sign-off 조건.
   - OEM 질의 응답 + 추가 시험 요청 협의.
   - 회의록 작성 → 양사 합의 서명.

3. **미합의 항목 추적**
   - Open Issue 별 책임자·기한·합의 방식(추가 시험/조건부 승인/ODD 축소) 명시.
   - 매주 진행 상황 OEM 공유.

4. **Sign-off 획득** (VAL.1.BP4)
   - 모든 합의 조건 충족 후 OEM 공식 승인서 수령(서명/e-sign).
   - 조건부 승인 시 조건·기한·해소 책임 명시.

5. **CM 등록**
   - 승인서·회의록·합의 이메일 묶음을 CM 베이스라인으로 등록.
   - WI-ASPICE-01-05-04(릴리즈 패키지 빌드) 진입 게이트 충족 처리.

### 5.3 완료 조건 체크리스트
- [ ] Validation Report 공식 제출 증적 보존
- [ ] 고객 검토 회의록 양사 서명 완료
- [ ] 모든 Open Issue 합의 또는 조건부 처리 명시
- [ ] OEM Approval Record 수령 (무조건/조건부 명확)
- [ ] 조건부 승인 시 조건·기한·책임자 명시
- [ ] 승인 적시성 ≤ 10 영업일 (PRO-05 §7 통제점)
- [ ] CM 시스템 베이스라인 등록 (Approval-XXX-v1.0)
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **Validation Engineer (WI-05-02)**: Validation Report 인수
- **OEM Customer**: 검토·승인 주체
- **Project Manager**: 일정·계약 영향 조정
- **QA (SUP.1)**: 승인 절차 적정성 감사
- **CM (SUP.8)**: 승인서 베이스라인 등록
- **법무팀**: 조건부 승인 시 계약 영향 검토

## 7. 주의사항 / 예외 처리

### 7.1 OEM 승인 거절
- OEM 이 Validation Report 수용 거절:
  - 거절 사유 공식 문서 수령.
  - 영향 분석(범위·일정·원가) → PM 보고.
  - 재검증 또는 범위 조정 협상 → 합의 변경(Amendment) 진행.
  - SUP.9 결함으로 등록.

### 7.2 조건부 승인 (Conditional Sign-off)
- OEM 이 조건 부여:
  - 조건 항목별 책임자·기한·검증 방법 합의서 작성.
  - 조건 미해소 시 인도 보류 명시.
  - QA 가 조건 해소 추적 (별도 NCR 등록).

### 7.3 승인 지연 (10 영업일 초과)
- OEM 응답 지연:
  - 7 영업일 시점에 1차 reminder.
  - 10 영업일 초과 시 PM·CTO 에스컬레이션.
  - 일정 영향 분석 + Release Plan 재조정.

### 7.4 미합의 항목 양산 진입 압력
- 일정 압박으로 미해소 항목을 무시하고 양산 진입 시도:
  - 절대 금지 — QA 가 거부권 행사.
  - 양산 진입은 무조건 승인 또는 조건부 승인 + 조건 해소 후만 허용.
  - 위반 시 CTO 에스컬레이션 + 감사 NCR 발행.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-05-03-01_고객승인서]]
- 작성예시: [[EX-ASPICE-01-05-03-01_고객승인서_작성예시]]
- 기록 폴더: `vault/08_REC_기록/VAL/Approval/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-VAL.1-BP4"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — VAL.1.BP4 OEM Sign-off 절차 정의 | (대기) |
