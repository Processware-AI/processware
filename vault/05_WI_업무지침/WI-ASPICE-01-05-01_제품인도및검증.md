---
type: WI
doc_id: "WI-ASPICE-01-05-01"
title: "제품 인도 및 검증 통합 (VAL.1 + SPL.2)"
version: "0.1"
owner: "Validation & Release Lead"
reviewer: "QA Lead / OEM Customer"
approver: "QA Lead + OEM 합의"
scope: "사용 환경 검증(VAL.1) → 릴리즈 빌드(SPL.2) → OEM 인도"
parent_pro: "[[PRO-ASPICE-01-05_검증및인도프로세스]]"
related_tmp: []
related_rec: []
standards: ["Automotive SPICE 4.0"]
aspice_processes: ["VAL.1", "SPL.2"]
entry_gate: null
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, VAL.1, SPL.2, Release, OEM]
---

# 제품 인도 및 검증 통합 업무지침 (WI-ASPICE-01-05-01)

> 상위 절차: [[PRO-ASPICE-01-05_검증및인도프로세스]]
> ASPICE 매핑: VAL.1 (Validation) + SPL.2 (Product Release)

## 1. 업무 목적

시스템 검증(SYS.5) 통과 후, 사용 환경(필드·차량) 에서의 검증(VAL.1) 을 수행하고, 모든 결함이 폐쇄·승인된 상태에서 릴리즈 패키지를 빌드하여 OEM 에 인도한다.

## 2. 수행 주체
- **주 수행자**: Validation Engineer + Release Engineer
- **검토자**: QA Lead, Safety Manager
- **승인자**: QA Lead + OEM Customer (서면 합의)

## 3. 범위
SYS.5 검증 보고서 등록 후부터 OEM 인도 + 인수 확인서 수령 시점까지 적용한다.

## 4. 입력 자료 / 산출물
- **Input**: SYS.5 검증 보고서, StRS, 통합 SW/HW/ML 빌드, 릴리즈 노트 초안
- **Output**: VAL Report, Release Package (SW Image + Documentation), OEM 인수 확인서

## 5. 수행 절차

### 5.1 사전 준비
1. 인도 환경(차량/HIL) 가용성 + 안전 점검.
2. 릴리즈 형상(빌드 ID, Hash) 확정.

### 5.2 수행 단계

1. **검증 계획 수립** (VAL.1.BP1)
   - 사용 시나리오 (운전자 시점) 도출 + 검증 케이스.

2. **사용 환경 검증 실행** (VAL.1.BP2/3)
   - 차량 통합 시험 + 도로 주행 시험.
   - OEM 입회 검증 시 OEM 시험 결과도 동시 수집.

3. **OEM 승인** (VAL.1.BP4)
   - VAL Report → OEM 검토 → 인수 합의.

4. **릴리즈 패키지 빌드** (SPL.2.BP1)
   - SW Image (signed/encrypted) + Documentation Set.
   - Build ID + 모든 컴포넌트 Hash 메타 첨부.

5. **OEM 인도** (SPL.2.BP2/3)
   - 인도 채널(보안 전송, 물리 매체) 결정.
   - 인수 확인서 수령 + 보관 (보존기간 SOP+15년).

### 5.3 완료 조건 체크리스트
- [ ] VAL Report 모든 케이스 결과 첨부
- [ ] OEM 인수 합의 서면(서명) 수령
- [ ] Release Package Hash + Build ID 메타 첨부
- [ ] OEM 인도 채널 보안 검증 완료
- [ ] 인수 확인서 수령 + 보관 등록
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **OEM Customer**: 검증·인수 합의
- **QA (SUP.1)**: 독립 승인
- **CM (SUP.8)**: Release 형상관리
- **Legal/Compliance**: 인도 계약 검토

## 7. 주의사항 / 예외 처리

### 7.1 VAL 결함 발견
- 사용 환경에서 신규 결함 발견 시:
  - SUP.9 등록 + Severity 분류.
  - Critical/Major 는 인도 보류 + 수정 후 재검증.

### 7.2 OEM 인수 거부
- OEM 가 인수를 거부한 경우:
  - 거부 사유 공식 문서화 + RCA.
  - SUP.10 변경 절차로 재작업 후 재인도.

### 7.3 인도 채널 보안 위반
- 전송 중 무결성 위반 의심:
  - 즉시 인도 중단 + 채널 차단.
  - Hash 비교로 무결성 검증.
  - 보안 사고로 처리 (Cybersecurity 통보).

### 7.4 인도 후 결함 (Field Issue)
- 인도 후 OEM 측에서 결함 보고:
  - SUP.9 즉시 등록 + Hot-fix 절차.
  - 영향 범위 분석 + Recall 가능성 평가 (법무 협의).

## 8. 연계 템플릿 / 기록
- 기록 폴더: `vault/08_REC_기록/VAL_SPL/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-VAL.1-* / VWAY-SPL.2-*"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — VAL.1 + SPL.2 통합 + OEM 인수 절차 | (대기) |
