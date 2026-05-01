---
type: WI
doc_id: "WI-CMMI-03-04-04"
title: "VV 환경 관리"
version: "1.0"
owner: "DevOps"
reviewer: "QA Lead"
approver: "PM"
scope: "검증·확인 환경 셋업·운영"
parent_pro: "[[PRO-CMMI-03-04_검증_및_확인_절차_v1.0]]"
parent_pol: "[[POL-CMMI-03_엔지니어링_정책_v1.0]]"
related_tmp: ["[[TMP-CMMI-03-04-04-01_VV_환경_정의서_v1.0]]"]
related_ex: ["[[EX-CMMI-03-04-04-01_VV_환경_정의서_작성예시_v1.0]]"]
standards: ["CMMI-DEV-ML3"]
scope_code: "CMMI"
status: approved
created: 2026-04-29
updated: 2026-04-29
tags: [WI, CMMI, VV]
---

# VV 환경 관리 (WI-CMMI-03-04-04)

> 상위 절차: [[PRO-CMMI-03-04_검증_및_확인_절차_v1.0]]

## 1. 업무 목적
검증·확인 환경의 일관성·재현성을 보장하여 결과 신뢰성을 확보한다.

## 2. 수행 주체
- 주 수행자: DevOps
- 검토자: QA Lead
- 승인자: PM

## 3. 범위
- VV 전용 환경

## 4. 입력 / 산출물
- Input: 환경 사양
- Output: [[TMP-CMMI-03-04-04-01_VV_환경_정의서_v1.0]]

## 5. 수행 절차

### 5.1 사전 준비
1. 사양 확인.
2. 자동화.

### 5.2 수행 단계
1. **셋업**.
2. **데이터 준비**.
3. **격리**.
4. **모니터링**.
5. **롤백**.
6. **회수**.

### 5.3 완료 조건
- [ ] 환경 가용성
- [ ] 격리 검증
- [ ] 회수 절차

## 6. 인터페이스 부서
- IT

## 7. 주의사항 / 예외 처리

### 7.1 데이터 누설
- 익명화.

### 7.2 환경 표류
- 자동 재구축.

### 7.3 비용
- 자동 정지.

## 8. 연계 템플릿
- [[TMP-CMMI-03-04-04-01_VV_환경_정의서_v1.0]]
- [[EX-CMMI-03-04-04-01_VV_환경_정의서_작성예시_v1.0]]

## 9. KPI
| 지표 | 목표 | 주기 |
|---|---|---|
| 환경 가용성 | ≥ 99% | 월 |

## 10. 출처
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/VV.pdf"
  locator: "VV 2.x — environment"
  license: "ISACA copyright — paraphrase only"
```

## 11. 개정 이력
| 1.0 | 2026-04-29 | 최초 승인 | PM |
