---
doc_id: "WI-ASPICE-01-08-06"
title: "변경 구현 및 검증 (SUP.10)"
type: WI
version: "0.1"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
owner: "Change Implementation Engineer"
reviewer: "Tech Lead / QA / Safety Engineer"
approver: "CCB Chair"
scope: "CCB 승인 후 → 변경 구현 → 재검증 → CM 베이스라인 갱신 → CR 종결"
scope_code: "ASPICE"
scope_type: "process"
domain: "ASPICE"
parent_pol: "[[POL-ASPICE-01_ASPICE품질정책]]"
parent_pro: "[[PRO-ASPICE-01-08_문제및변경관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-08-06-01_변경구현확인서]]"]
aspice_processes: ["SUP.10"]
entry_gate: "WI-ASPICE-01-08-05.status == approved"
standards: ["Automotive SPICE 4.0"]
tags: [WI, ASPICE, SUP.10, ChangeManagement, Implementation, Verification]
---

# WI-ASPICE-01-08-06 변경 구현 및 검증 (SUP.10)

## 1. 업무 목적
CCB 승인된 CR 을 정의된 범위 내에서 구현하고, 영향 받는 모든 검증 활동을 재실행하여
변경의 품질을 보증한 뒤 CM 베이스라인을 갱신하고 CR 을 종결한다.
ASPICE SUP.10 BP5(변경 구현) ~ BP6(변경 검증·종결) 을 수행한다.

## 2. 수행 주체
- 주 수행자: Change Implementation Engineer (해당 도메인 개발자)
- 검토자: Tech Lead, QA, Safety Engineer (안전 영향 시)
- 승인자: CCB Chair (CR 종결 승인)

## 3. 범위
- 대상: CCB Approved / Conditional Approved 상태의 CR
- 시점: CCB 결정 직후 ~ CR 종결까지
- 제외: Rejected / Deferred CR

## 4. 입력 자료 / 산출물
| 구분 | 항목 | 출처/위치 |
|---|---|---|
| 입력 | CCB 회의록 (결정 + 조건) | TMP-ASPICE-01-08-05-01 결재본 |
| 입력 | 영향 평가 보고서 | TMP-ASPICE-01-08-04-01 결재본 |
| 입력 | 활성 베이스라인 등록서 | TMP-ASPICE-01-07-05-01 |
| 출력 | 변경 구현 확인서 | TMP-ASPICE-01-08-06-01 |
| 출력 | 신규 베이스라인 등록서 | TMP-ASPICE-01-07-05-01 (다음 버전) |
| 출력 | CR 종결 통보 | 이메일 / Jira 상태 갱신 |

## 5. 수행 절차

### 5.1 사전 준비
1. CCB 결정 + 조건 + 영향 평가 보고서 정독.
2. 구현 책임자(Implementer) 지정 (영향 평가 §6 인력 계획 기반).
3. 작업 브랜치 생성 (예: `feature/CR-007-canfd-msg-id`).
4. 재검증 대상 시험 케이스 목록 확보 (영향 평가 §7).

### 5.2 수행 단계
1. **변경 구현** — 영향 받는 CI 에 대해 코드·문서·설계 변경을 정확히 영향 평가 범위 내에서 수행 (SUP.10 BP5).
2. **단위 자체 검증** — 구현자 본인 단위시험·정적분석 통과 확인.
3. **피어 리뷰** — 코드/문서 리뷰 수행, 리뷰 의사록 첨부.
4. **재검증 실행** — 영향 평가에서 정의된 시험 케이스 전부 재실행 (SUP.10 BP6).
5. **추적성 갱신** — RTM 에 변경 반영 (요구사항 ↔ 설계 ↔ 코드 ↔ 시험).
6. **조건 충족 확인** — Conditional Approved 의 경우 모든 조건 충족 증거 수집.
7. **CM 베이스라인 갱신** — WI-ASPICE-01-07-05 절차로 신규 베이스라인 발행.
8. **변경 구현 확인서 작성** — TMP-ASPICE-01-08-06-01 작성.
9. **CR 종결 승인** — Tech Lead·QA·Safety(필요 시) 검토 → CCB Chair 종결 승인.
10. **CR 상태 Closed 갱신 및 통보** — SUP.10 시스템 상태 변경, 관련자 통보.

### 5.3 완료 조건 체크리스트
- [ ] 변경이 영향 평가 범위 내에서 구현됨 (범위 외 변경 없음)
- [ ] 피어 리뷰 의사록이 첨부됨
- [ ] 재검증 시험 결과가 모두 Pass
- [ ] 추적성(RTM) 갱신이 완료됨
- [ ] Conditional 조건이 모두 충족됨 (해당 시)
- [ ] 신규 베이스라인이 발행됨
- [ ] 변경 구현 확인서가 CCB Chair 결재됨
- [ ] CR 상태가 Closed 로 갱신됨
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- SW/HW/Systems Engineering: 변경 구현 실행
- QA: 재검증 결과 검토, 종결 검토
- Functional Safety / Cybersecurity: 안전·보안 영향 시 재검토
- Configuration Management: 신규 베이스라인 발행 인계
- Customer Interface: 외부 영향 시 변경 통보

## 7. 주의사항 / 예외 처리

### 7.1 영향 평가 범위 초과 변경 발견 시
구현 중 영향 평가에 누락된 추가 변경 필요성 발견 시 즉시 작업 중단, 영향 평가 보고서 보완 후
CCB 재상정. 임의 확장 구현 금지(범위 크리프 방지).

### 7.2 재검증 시험 Fail 시
재검증 중 Fail 발생 시 SUP.9 문제 보고서 등록, 결함 수정 후 재시험. 종결 절차 진행 불가.
ASIL 영향 시 안전 게이트 통과 필수.

### 7.3 조건 미충족 시
Conditional Approved CR 의 조건 미충족 시 CR 종결 불가. 조건 충족까지 In-Progress 상태 유지.
조건 변경 필요 시 CCB 재상정.

### 7.4 Rollback 절차
신규 베이스라인 발행 후 운영 중 결함 발견 시 즉시 이전 베이스라인 태그로 롤백 가능 상태 유지.
Rollback 도 CR 로 등록하여 추적.

## 8. 연계 템플릿 / 기록
- 양식: [[TMP-ASPICE-01-08-06-01_변경구현확인서]]
- 작성예시: [[EX-ASPICE-01-08-06-01_변경구현확인서_작성예시]]
- 선행 절차: [[WI-ASPICE-01-08-05_CCB운영]]
- 연계 절차: [[WI-ASPICE-01-07-05_베이스라인및변경통제]] (신규 베이스라인 발행)
- 연계 기록: 코드 리뷰 의사록, 재검증 시험 보고서, 신규 베이스라인 등록서

## 9. 출처
```yaml
source_citation:
  - source: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    standard: "Automotive SPICE 4.0"
    process: "SUP.10 — Change Request Management"
    base_practices: ["BP5", "BP6", "BP7"]
    work_products: ["13-21 Change control record", "15-19 Verification report"]
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 작성 (draft) | CCB Chair |
