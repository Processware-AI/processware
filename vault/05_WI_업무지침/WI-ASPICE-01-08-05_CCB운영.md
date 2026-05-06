---
doc_id: "WI-ASPICE-01-08-05"
title: "CCB 운영 (SUP.10)"
type: WI
version: "0.1"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
owner: "Project Manager"
reviewer: "CCB Members"
approver: "Program Director"
scope: "영향 평가 완료 → CCB 회의 소집·의결·결과 배포 → CR 상태 갱신"
scope_code: "ASPICE"
scope_type: "process"
domain: "ASPICE"
parent_pol: "[[POL-ASPICE-01_ASPICE품질정책]]"
parent_pro: "[[PRO-ASPICE-01-08_문제및변경관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-08-05-01_CCB회의록]]"]
aspice_processes: ["SUP.10"]
entry_gate: "WI-ASPICE-01-08-04.status == done"
standards: ["Automotive SPICE 4.0"]
tags: [WI, ASPICE, SUP.10, CCB, ChangeControl]
---

# WI-ASPICE-01-08-05 CCB 운영 (SUP.10)

## 1. 업무 목적
변경통제위원회(CCB)를 정기·임시로 소집하여 영향 평가가 완료된 CR 에 대한 의사결정(승인/조건부/
반려/보류)을 내리고, 결정 결과를 CR 상태에 즉시 반영한다. ASPICE SUP.10 BP4(변경 승인) 를 수행한다.

## 2. 수행 주체
- 주 수행자: Project Manager (CCB 간사)
- 검토자: CCB Members (PM, Tech Lead, QA, Safety Eng, Cybersecurity Eng, CM)
- 승인자: Program Director (CCB Chair)

## 3. 범위
- 대상: 영향 평가가 완료된 모든 CR
- 시점: 정기 CCB (주 1회), 임시 CCB (Emergency CR), 대면·원격 모두 가능
- 제외: 안전·보안 영향 없는 단순 문서 정정(Process Owner 직접 처리, CCB 우회)

## 4. 입력 자료 / 산출물
| 구분 | 항목 | 출처/위치 |
|---|---|---|
| 입력 | 영향 평가 보고서 | TMP-ASPICE-01-08-04-01 결재본 |
| 입력 | CR 상세 (Jira) | SUP.10 시스템 |
| 입력 | 활성 베이스라인 등록서 | TMP-ASPICE-01-07-05-01 |
| 출력 | CCB 회의록 | TMP-ASPICE-01-08-05-01 |
| 출력 | CR 상태 갱신 (Approved/Rejected/Deferred) | SUP.10 시스템 |
| 출력 | 결과 배포 메일 | 이메일 |

## 5. 수행 절차

### 5.1 사전 준비
1. 정기 CCB 일정 확정 (예: 매주 화요일 14:00).
2. 의제 CR 목록 확정 (영향 평가 완료된 CR).
3. CCB Members 에게 의제 + 영향 평가 보고서 사전 배포 (회의 24h 전).
4. 정족수 확인 (CCB 구성원 과반 + 영향 분야 전문가 필수).

### 5.2 수행 단계
1. **개회 및 정족수 확인** — Chair 가 참석자 확인, 정족수 미달 시 회의 연기 (SUP.10 BP4).
2. **이전 회의 결정 후속 확인** — 지난 CCB 결정의 구현 진행 상황 보고.
3. **CR 별 검토** — CR 마다: 요청자 발표 → 영향 평가 보고서 검토 → 질의응답 → 토의.
4. **의결** — Chair 가 결정 옵션 제시: 승인 / 조건부 승인 / 반려 / 보류.
5. **결정 기록** — 회의록에 결정·조건·반려 사유 명시.
6. **CR 상태 즉시 갱신** — 회의 종료 직후 SUP.10 시스템에서 상태 변경 (Approved / Conditional / Rejected / Deferred).
7. **회의록 작성·배포** — TMP-ASPICE-01-08-05-01 작성, 회의 종료 24h 내 참석자·요청자·구현 책임자에게 배포.
8. **차기 CCB 의제 예약** — 보류 CR 은 차기 CCB 의제로 자동 등록.

### 5.3 완료 조건 체크리스트
- [ ] 정족수 충족 확인됨
- [ ] 모든 의제 CR 에 대한 결정이 회의록에 기록됨
- [ ] 조건부 승인의 조건이 측정 가능하게 명시됨
- [ ] 반려의 사유가 명시됨
- [ ] CR 상태가 SUP.10 시스템에 갱신됨
- [ ] 회의록이 24h 내 배포됨
- [ ] 차기 CCB 의제 등록됨
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- All Engineering Disciplines: CCB Members 로 참여
- Functional Safety / Cybersecurity Team: 안전·보안 영향 CR 의 의결권 보유
- Configuration Management: 승인 후 베이스라인 갱신 인계
- Change Implementation Team: 승인 CR 의 구현 인계 (WI-ASPICE-01-08-06)

## 7. 주의사항 / 예외 처리

### 7.1 정족수 미달 시
필수 분야(안전·보안 영향 CR 시 Safety/Cybersecurity Engineer) 결석 시 해당 CR 만 보류,
나머지 CR 만 의결. 다음 CCB 까지 위임 결정 금지.

### 7.2 Emergency CCB
24시간 이내 결정이 필요한 Emergency CR 은 Chair 가 즉시 임시 회의 소집 (대면/원격/이메일 의결 가능).
이메일 의결 시 모든 필수 구성원의 명시적 동의(Reply All) 필수, 추후 정식 회의록으로 보완.

### 7.3 이해 충돌 (Conflict of Interest)
구성원이 본인 직접 작성·구현한 CR 의결에 참여 시 의결권 행사 불가. Chair 가 회의록에 명시.

### 7.4 결정 번복 절차
CCB 결정은 차기 정기 CCB 의 정식 안건 재상정으로만 번복 가능. 이메일·구두 번복 금지.

## 8. 연계 템플릿 / 기록
- 양식: [[TMP-ASPICE-01-08-05-01_CCB회의록]]
- 작성예시: [[EX-ASPICE-01-08-05-01_CCB회의록_작성예시]]
- 선행 절차: [[WI-ASPICE-01-08-04_영향평가]]
- 후속 절차: [[WI-ASPICE-01-08-06_변경구현및검증]]
- 연계 기록: 변경 요청서, 영향 평가 보고서, CR 상태 로그

## 9. 출처
```yaml
source_citation:
  - source: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    standard: "Automotive SPICE 4.0"
    process: "SUP.10 — Change Request Management"
    base_practices: ["BP4", "BP5"]
    work_products: ["13-21 Change control record", "14-08 Meeting support record"]
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 작성 (draft) | Program Director |
