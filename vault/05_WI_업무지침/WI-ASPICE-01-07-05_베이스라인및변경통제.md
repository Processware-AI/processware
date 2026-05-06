---
doc_id: "WI-ASPICE-01-07-05"
title: "베이스라인 및 변경 통제 (SUP.8)"
type: WI
version: "0.1"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
owner: "CM Engineer"
reviewer: "Project Manager / QA"
approver: "CM Manager"
scope: "형상 항목 등록 후 → 마일스톤 베이스라인 동결 → 변경 요청 통제 → 베이스라인 무결성 유지"
scope_code: "ASPICE"
scope_type: "process"
domain: "ASPICE"
parent_pol: "[[POL-ASPICE-01_ASPICE품질정책]]"
parent_pro: "[[PRO-ASPICE-01-07_품질보증및형상관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-07-05-01_베이스라인등록서]]"]
aspice_processes: ["SUP.8"]
entry_gate: "WI-ASPICE-01-07-04.status == done"
standards: ["Automotive SPICE 4.0"]
tags: [WI, ASPICE, SUP.8, CM, Baseline, ChangeControl]
---

# WI-ASPICE-01-07-05 베이스라인 및 변경 통제 (SUP.8)

## 1. 업무 목적
프로젝트 마일스톤마다 형상 항목을 동결하여 베이스라인을 생성하고, 베이스라인 이후 발생하는
모든 변경을 SUP.10 변경통제 프로세스로 통제한다. ASPICE SUP.8 BP4(베이스라인 수립) ~ BP6(형상 통제)
및 BP7(상태 보고) 의 일부를 수행한다.

## 2. 수행 주체
- 주 수행자: CM Engineer
- 검토자: Project Manager, QA
- 승인자: CM Manager

## 3. 범위
- 대상: WI-ASPICE-01-07-04 로 등록된 모든 CI
- 베이스라인 트리거: SYS.2/SYS.4/SWE.2/SWE.4/SWE.6 완료 시점, Release 시점
- 제외: 임시 빌드(개발 일일 빌드 등)

## 4. 입력 자료 / 산출물
| 구분 | 항목 | 출처/위치 |
|---|---|---|
| 입력 | 형상 항목 목록 | TMP-ASPICE-01-07-04-01 결재본 |
| 입력 | 마일스톤 일정 | 프로젝트 계획서 |
| 입력 | 변경 요청 | SUP.10 시스템 (Jira) |
| 출력 | 베이스라인 등록서 | TMP-ASPICE-01-07-05-01 |
| 출력 | 베이스라인 태그 | CM 도구 (Git tag, Artifactory tag) |
| 출력 | 무결성 검사 결과 | 베이스라인 등록서 §4 |

## 5. 수행 절차

### 5.1 사전 준비
1. 마일스톤 도래 확인 → 베이스라인 대상 CI 목록 추출.
2. 각 CI 의 현재 버전·체크섬 사전 수집.
3. 베이스라인 명명 규칙(BL-{프로젝트}-{마일스톤}-vX.Y) 확인.

### 5.2 수행 단계
1. **베이스라인 ID 부여** — 명명 규칙에 따라 ID 발급 (SUP.8 BP4).
2. **CI 동결** — 각 CI 저장소에 read-only 태그/락 설정.
3. **체크섬 계산** — 각 CI 의 SHA-256 등 체크섬 산출 → 등록서에 기록.
4. **무결성 검사** — 등록 직전 vs 직후 체크섬 일치 검증.
5. **베이스라인 등록서 작성** — TMP-ASPICE-01-07-05-01 작성, CM Manager 승인.
6. **변경 통제 모드 전환** — 베이스라인 이후 해당 CI 변경은 SUP.10 CR 승인 필수 (SUP.8 BP6).
7. **변경 적용 후 베이스라인 갱신** — 승인된 CR 구현 완료 시 새 베이스라인(BL-...-vX.Y+1) 발행.
8. **롤백 절차** — 베이스라인 이후 결함 발견 시 이전 베이스라인 태그로 즉시 복원 가능 상태 유지.
9. **상태 보고** — 주간 CM 상태 보고서에 활성 베이스라인·CR 진행 현황 포함 (SUP.8 BP7).

### 5.3 완료 조건 체크리스트
- [ ] 베이스라인 ID 가 명명 규칙에 부합
- [ ] 모든 대상 CI 가 동결(read-only) 됨
- [ ] 모든 CI 체크섬이 기록됨
- [ ] 무결성 검사 결과 Pass
- [ ] 베이스라인 등록서가 CM Manager 결재됨
- [ ] CM 도구에 태그가 생성됨
- [ ] 변경 통제 모드 전환이 공지됨
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- Project Management Office: 마일스톤 일정·릴리즈 일정 제공
- SW/HW/Systems Engineering: CI 동결 협조, 변경 발생 시 CR 제출
- QA: 베이스라인 후속 형상 감사(WI-ASPICE-01-07-06) 수행
- DevOps: CM 도구 태그·락 자동화 지원

## 7. 주의사항 / 예외 처리

### 7.1 동결 후 무단 수정 발견 시
정기 무결성 검사에서 베이스라인 CI 의 체크섬 불일치 발견 시 즉시 변경 통제 위반으로
SUP.9 등록 → 원인 분석 → 무단 변경 롤백 또는 사후 CR 처리 결정.

### 7.2 Emergency Change 처리
안전·보안·치명 결함으로 즉시 변경이 필요한 경우 Emergency CCB(긴급 회의) 소집,
구두 승인 후 24h 내 정식 CR 등록·서면 승인 절차 보완.

### 7.3 외부 의존성(EXT) 베이스라인
오픈소스 신규 버전 자동 업데이트 금지. EXT CI 는 베이스라인 시점의 commit hash/tag 로 고정.
보안 패치는 별도 CR.

### 7.4 베이스라인 인도(Release Baseline) 시
고객 인도용 베이스라인은 형상 감사(WI-ASPICE-01-07-06) PCA + FCA 통과가 필수.
미통과 시 인도 보류.

## 8. 연계 템플릿 / 기록
- 양식: [[TMP-ASPICE-01-07-05-01_베이스라인등록서]]
- 작성예시: [[EX-ASPICE-01-07-05-01_베이스라인등록서_작성예시]]
- 선행 절차: [[WI-ASPICE-01-07-04_형상항목식별]]
- 후속 절차: [[WI-ASPICE-01-07-06_형상감사]]
- 연계 절차: [[WI-ASPICE-01-08-04_영향평가]], [[WI-ASPICE-01-08-05_CCB운영]], [[WI-ASPICE-01-08-06_변경구현및검증]]

## 9. 출처
```yaml
source_citation:
  - source: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    standard: "Automotive SPICE 4.0"
    process: "SUP.8 — Configuration Management"
    base_practices: ["BP4", "BP5", "BP6", "BP7"]
    work_products: ["08-04 Configuration management plan", "16-06 Configuration item baseline"]
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 작성 (draft) | CM Manager |
