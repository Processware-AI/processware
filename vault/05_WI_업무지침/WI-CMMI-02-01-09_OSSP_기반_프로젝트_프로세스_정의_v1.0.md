---
type: WI
doc_id: "WI-CMMI-02-01-09"
title: "OSSP 기반 프로젝트 프로세스 정의(PDP)"
version: "1.0"
owner: "Project PM"
reviewer: "SEPG"
approver: "SEPG Lead"
scope: "OSSP 의 프로젝트별 테일러링 결과로 PDP 정의"
parent_pro: "[[PRO-CMMI-02-01_프로젝트_계획_절차_v1.0]]"
parent_pol: "[[POL-CMMI-02_프로젝트관리_정책_v1.0]]"
related_tmp:
  - "[[TMP-CMMI-02-01-09-01_프로젝트_정의_프로세스_PDP_v1.0]]"
related_ex:
  - "[[EX-CMMI-02-01-09-01_프로젝트_정의_프로세스_PDP_작성예시_v1.0]]"
standards: ["CMMI-DEV-ML3"]
scope_code: "CMMI"
status: approved
created: 2026-04-29
updated: 2026-04-29
tags: [WI, CMMI, PLAN, PAD]
---

# OSSP 기반 PDP 정의 (WI-CMMI-02-01-09)

> 상위 절차: [[PRO-CMMI-02-01_프로젝트_계획_절차_v1.0]]

## 1. 업무 목적
프로젝트가 OSSP 를 기반으로 테일러링한 정의 프로세스(PDP) 를 명문화하여 프로젝트 활동의 표준 기준을 명확히 한다.

## 2. 수행 주체
- 주 수행자: PM
- 검토자: SEPG
- 승인자: SEPG Lead

## 3. 범위
- 모든 신규 프로젝트(ML3 평가 대상 의무)

## 4. 입력 / 산출물
- Input: OSSP, 테일러링 요청서
- Output: [[TMP-CMMI-02-01-09-01_프로젝트_정의_프로세스_PDP_v1.0]] 승인본

## 5. 수행 절차

### 5.1 사전 준비
1. OSSP 버전 확인.
2. 테일러링 항목 식별.

### 5.2 수행 단계
1. **PDP 초안 작성**.
2. **테일러링 적용**.
3. **SEPG 검토**.
4. **SEPG Lead 승인**.
5. **프로젝트 계획서 첨부**.
6. **OSSP 변경 시 PDP 갱신**.

### 5.3 완료 조건
- [ ] PDP 승인본
- [ ] 프로젝트 계획서 첨부
- [ ] OSSP 변경 모니터링

## 6. 인터페이스 부서
- SEPG, PMO

## 7. 주의사항 / 예외 처리

### 7.1 핵심 통제 누락
- QA·CM·VV 누락 금지. 발견 시 PDP 거절.

### 7.2 OSSP 갱신
- OSSP 갱신 30일 내 PDP 영향 분석·갱신.

### 7.3 ML3 평가 직전
- 평가 90일 전 PDP 정합성 재검증.

## 8. 연계 템플릿
- [[TMP-CMMI-02-01-09-01_프로젝트_정의_프로세스_PDP_v1.0]]
- [[EX-CMMI-02-01-09-01_프로젝트_정의_프로세스_PDP_작성예시_v1.0]]

## 9. KPI
| 지표 | 목표 | 주기 |
|---|---|---|
| PDP 등록률(신규 프로젝트) | 100% | 분기 |
| OSSP 갱신 시 PDP 갱신 SLA | ≤ 30일 | 분기 |

## 10. 출처
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/PLAN.pdf"
  locator: "PLAN 3.x — define project process"
  license: "ISACA copyright — paraphrase only"
```

## 11. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 1.0 | 2026-04-29 | 최초 승인 | SEPG Lead |
