---
doc_id: "WI-ASPICE-01-07-06"
title: "형상 감사 (SUP.8)"
type: WI
version: "0.1"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
owner: "CM Engineer"
reviewer: "QA / Project Manager"
approver: "CM Manager"
scope: "베이스라인 동결 후 → 물리적 형상 감사(PCA) + 기능 형상 감사(FCA) → 감사 보고서 발행"
scope_code: "ASPICE"
scope_type: "process"
domain: "ASPICE"
parent_pol: "[[POL-ASPICE-01_ASPICE품질정책]]"
parent_pro: "[[PRO-ASPICE-01-07_품질보증및형상관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-07-06-01_형상감사보고서]]"]
aspice_processes: ["SUP.8"]
entry_gate: "WI-ASPICE-01-07-05.status == done"
standards: ["Automotive SPICE 4.0"]
tags: [WI, ASPICE, SUP.8, CM, ConfigurationAudit, PCA, FCA]
---

# WI-ASPICE-01-07-06 형상 감사 (SUP.8)

## 1. 업무 목적
베이스라인의 물리적 일치성(PCA, Physical Configuration Audit)과 기능적 충족성
(FCA, Functional Configuration Audit)을 독립적으로 검증하여 인도(Release) 적격성을
판정한다. ASPICE SUP.8 BP8(형상 감사) 을 수행한다.

## 2. 수행 주체
- 주 수행자: CM Engineer (PCA), QA (FCA 주관)
- 검토자: Project Manager
- 승인자: CM Manager

## 3. 범위
- 대상: WI-ASPICE-01-07-05 로 동결된 베이스라인
- 시점: 마일스톤·릴리즈 베이스라인 동결 후 인도 전
- 제외: 임시 베이스라인(개발 일일 빌드)

## 4. 입력 자료 / 산출물
| 구분 | 항목 | 출처/위치 |
|---|---|---|
| 입력 | 베이스라인 등록서 | TMP-ASPICE-01-07-05-01 결재본 |
| 입력 | 요구사항 명세서·추적성 매트릭스 | SYS.2 / SWE.1 산출물 |
| 입력 | 시험 결과 보고서 | SWE.5 / SWE.6 산출물 |
| 출력 | 형상 감사 보고서 | TMP-ASPICE-01-07-06-01 |
| 출력 | 인도 승인서 (Release Baseline 한정) | 별도 양식 |

## 5. 수행 절차

### 5.1 사전 준비
1. 감사 대상 베이스라인 ID 확정.
2. 베이스라인 등록서 § 2 CI 목록 + 체크섬 확보.
3. FCA 기준이 되는 요구사항 ID 목록 + 추적성 매트릭스 확보.
4. 시험 결과 (Pass/Fail/Open) 최신본 확보.

### 5.2 수행 단계
1. **PCA 실시** — 베이스라인 등록서 CI 목록과 CM 도구의 실제 등록 항목 1:1 대조 (SUP.8 BP8).
2. **PCA 체크섬 검증** — 등록서 SHA-256 vs 현 저장소 SHA-256 일치 여부.
3. **PCA 누락·과다 항목 식별** — 등록서에는 있으나 저장소에 없거나, 저장소에는 있으나 등록서에 없는 CI 식별.
4. **FCA 실시** — 베이스라인이 만족해야 하는 요구사항 목록 도출, 각 요구사항별 충족 증거(시험 결과·검토 의사록·정적분석) 확인.
5. **FCA 미충족 식별** — 시험 Fail / 미실시 / 추적성 단절 항목 목록화.
6. **불일치 분류** — Critical(인도 차단) / Major(조건부) / Minor(권고).
7. **인도 승인 판정** — 모든 Critical 해소 시 Pass, 미해소 시 Fail 또는 Conditional.
8. **감사 보고서 작성** — TMP-ASPICE-01-07-06-01.
9. **결재·배포** — CM Manager 승인 → PM·QA·고객 인도 담당자에게 배포.

### 5.3 완료 조건 체크리스트
- [ ] PCA 가 베이스라인 전 CI 에 대해 수행됨
- [ ] FCA 가 대상 요구사항 전 항목에 대해 수행됨
- [ ] 모든 불일치가 Critical/Major/Minor 로 분류됨
- [ ] Critical 불일치는 SUP.9 등록 또는 즉시 시정됨
- [ ] 인도 승인 여부가 명시됨
- [ ] 감사 보고서가 CM Manager 결재됨
- [ ] 결재본이 관계자에게 배포됨
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- QA: FCA 공동 수행, 독립성 확보
- Systems / SW Engineering: 요구사항·시험 결과 증거 제공
- Project Management Office: 인도 일정 협의
- Customer Interface: Release Baseline 인도 시 승인서 전달

## 7. 주의사항 / 예외 처리

### 7.1 PCA 체크섬 불일치 발견 시
즉시 베이스라인 무결성 위반으로 SUP.9 등록 → 변경 통제 위반 조사 → 베이스라인 재발행 또는
사후 CR 처리. 인도 절대 진행 불가.

### 7.2 FCA 시험 Fail 항목 처리
- Critical (안전·보안): 인도 차단, 즉시 시정 후 재감사
- Major: 조건부 인도 가능 (잔존 위험 명시 + 고객 동의)
- Minor: 후속 패치 계획과 함께 인도

### 7.3 추적성 단절 발견 시
요구사항 ↔ 설계 ↔ 코드 ↔ 시험 추적성이 끊긴 항목은 FCA Fail 처리. SWE.6 추적성 보완 후 재감사.

### 7.4 감사자 독립성
PCA 는 CM Engineer (CI 등록자와 동일 가능), FCA 는 반드시 QA (개발 미참여) 가 주관.
이중 점검으로 객관성 확보.

## 8. 연계 템플릿 / 기록
- 양식: [[TMP-ASPICE-01-07-06-01_형상감사보고서]]
- 작성예시: [[EX-ASPICE-01-07-06-01_형상감사보고서_작성예시]]
- 선행 절차: [[WI-ASPICE-01-07-05_베이스라인및변경통제]]
- 연계 기록: 인도 승인서, SUP.9 문제 보고서

## 9. 출처
```yaml
source_citation:
  - source: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    standard: "Automotive SPICE 4.0"
    process: "SUP.8 — Configuration Management"
    base_practices: ["BP8"]
    work_products: ["15-22 Configuration audit report", "16-06 Configuration item baseline"]
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 작성 (draft) | CM Manager |
