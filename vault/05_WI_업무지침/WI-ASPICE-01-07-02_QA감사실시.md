---
doc_id: "WI-ASPICE-01-07-02"
title: "QA 감사 실시 (SUP.1)"
type: WI
version: "0.1"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
owner: "QA Engineer"
reviewer: "Process Engineer / Project Manager"
approver: "QA Manager"
scope: "QA 계획 승인 후 → 프로세스·산출물 감사 실시 → 감사 보고서 발행 → 부적합 SUP.9 등록"
scope_code: "ASPICE"
scope_type: "process"
domain: "ASPICE"
parent_pol: "[[POL-ASPICE-01_ASPICE품질정책]]"
parent_pro: "[[PRO-ASPICE-01-07_품질보증및형상관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-07-02-01_QA감사보고서]]"]
aspice_processes: ["SUP.1"]
entry_gate: "WI-ASPICE-01-07-01.status == done"
standards: ["Automotive SPICE 4.0"]
tags: [WI, ASPICE, SUP.1, QA, Audit]
---

# WI-ASPICE-01-07-02 QA 감사 실시 (SUP.1)

## 1. 업무 목적
승인된 QA 계획을 근거로 프로젝트의 프로세스 준수 여부와 산출물 품질을 객관적·증거기반으로 감사하고,
부적합을 발견·분류·등록하여 시정 조치 루프(SUP.10/WI-ASPICE-01-07-03)로 인계한다.
ASPICE SUP.1 BP1~BP6 의 BP3(감사 수행) ~ BP5(부적합 보고) 를 수행한다.

## 2. 수행 주체
- 주 수행자: QA Engineer
- 검토자: Process Engineer, Project Manager
- 승인자: QA Manager

## 3. 범위
- 대상 프로세스: SYS.1~SYS.5, SWE.1~SWE.6, SUP.8, SUP.10, MAN.3 등 QA 계획에 명시된 모든 프로세스
- 대상 산출물: 각 프로세스의 Work Product
- 시점: QA 계획서의 감사 일정(정기/마일스톤/이벤트 기반)
- 제외: 외부 협력사 단독 감사(별도 SUP.9 절차)

## 4. 입력 자료 / 산출물
| 구분 | 항목 | 출처/위치 |
|---|---|---|
| 입력 | 승인된 QA 계획서 | WI-ASPICE-01-07-01 결재본 |
| 입력 | 감사 체크리스트 | QA 계획서 부속 |
| 입력 | 대상 프로세스 산출물 | CM 시스템(Git/Confluence/Jira) |
| 출력 | QA 감사 보고서 | TMP-ASPICE-01-07-02-01 |
| 출력 | SUP.9 문제 보고서(Major별 1건) | WI-ASPICE-01-08-01 연계 |

## 5. 수행 절차

### 5.1 사전 준비
1. 승인된 QA 계획서에서 금주/금월 감사 대상 식별.
2. 감사 체크리스트 최신본 확보(없으면 ASPICE 4.0 BP 기준으로 도출).
3. 대상 프로세스 담당자에게 감사 일정·범위 사전 공지(최소 5 영업일 전).
4. 감사 증적 수집 채널(Git/Jira/Confluence) 접근 권한 확인.

### 5.2 수행 단계
1. **킥오프 미팅 개최** — 감사 범위·기준·일정·결과 통보 절차 합의 (SUP.1 BP3).
2. **증적 수집** — 체크리스트 항목별로 산출물·도구 로그·면담 기록 수집.
3. **항목별 판정** — Pass / Fail / N/A 판정 및 근거 ID(증적 ID) 기재.
4. **발견사항 분류** — Major(프로세스 중대 결함, 결과 신뢰성 훼손) / Minor(경미한 절차 누락) / Observation(개선 권고).
5. **종합 판정** — Pass / Conditional Pass(조건부 통과) / Fail.
6. **감사 보고서 작성** — TMP-ASPICE-01-07-02-01 양식 사용 (SUP.1 BP5).
7. **SUP.9 문제 보고서 등록** — 모든 Major 발견사항을 1:1로 SUP.9 시스템에 등록.
8. **결과 배포 및 종료 미팅** — 감사 보고서를 PM·프로세스 오너·QA Manager 에게 배포, 종료 미팅에서 합의.
9. **후속 조치 추적** — Major 는 WI-ASPICE-01-07-03(시정 조치)로 인계, 종결까지 모니터링 (SUP.1 BP6).

### 5.3 완료 조건 체크리스트
- [ ] 감사 체크리스트 전 항목 판정 완료
- [ ] 모든 발견사항 분류(Major/Minor/Observation) 완료
- [ ] Major 발견사항이 SUP.9 에 1:1 등록됨
- [ ] 감사 보고서가 QA Manager 결재됨
- [ ] 종료 미팅 의사록이 배포됨
- [ ] 후속 조치 책임자·마감일이 지정됨
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- Project Management Office: 감사 일정 조정, PM 대상 결과 보고
- Software/Hardware/Systems Engineering: 피감 부서 — 증적 제공, 시정 책임
- Process Engineering: 체크리스트·기준 제공
- Configuration Management: 산출물·베이스라인 접근 지원

## 7. 주의사항 / 예외 처리

### 7.1 증적 미제출 시
피감 부서가 요청 후 3 영업일 내 증적을 제출하지 못하면 해당 항목은 자동 Fail 처리하고
감사 보고서 비고란에 사유 기재. 반복 시 PM 에 공식 에스컬레이션.

### 7.2 감사 중 안전·보안 이슈 발견 시
ASIL 등급에 영향을 주는 결함 또는 사이버보안 노출 발견 시 감사 진행을 중단하고
즉시 Safety Manager / Cybersecurity Manager 에 통보, Emergency CCB 소집 요청.

### 7.3 감사자 독립성 충돌
QA Engineer 가 피감 산출물 작성에 직접 참여한 경우 감사자 교체 요청. 교체 불가 시
QA Manager 가 동석하여 객관성 보증.

### 7.4 감사 결과 이의 신청
피감 부서는 감사 보고서 수령 후 5 영업일 내 이의 신청 가능. QA Manager 가 재심하여
결과를 갱신하거나 원안 유지.

## 8. 연계 템플릿 / 기록
- 양식: [[TMP-ASPICE-01-07-02-01_QA감사보고서]]
- 작성예시: [[EX-ASPICE-01-07-02-01_QA감사보고서_작성예시]]
- 후속 절차: [[WI-ASPICE-01-07-03_시정조치및에스컬레이션]]
- 연계 기록: SUP.9 문제 보고서, 종료 미팅 의사록

## 9. 출처
```yaml
source_citation:
  - source: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    standard: "Automotive SPICE 4.0"
    process: "SUP.1 — Quality Assurance"
    base_practices: ["BP3", "BP4", "BP5", "BP6"]
    work_products: ["13-04 Quality record", "15-19 Quality assurance report"]
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 작성 (draft) | QA Manager |
