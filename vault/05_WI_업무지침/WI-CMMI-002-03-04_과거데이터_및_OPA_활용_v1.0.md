---
type: WI
doc_id: "WI-CMMI-002-03-04"
title: "과거 데이터 및 OPA 활용"
version: "1.0"
owner: "EST 전문가"
reviewer: "PMO"
approver: "PM"
scope: "조직 측정저장소·교훈을 추정 입력으로 활용"
parent_pro: "[[PRO-CMMI-203_추정_관리_절차_v1.0]]"
parent_pol: "[[POL-CMMI-002_프로젝트관리_정책_v1.0]]"
related_tmp:
  - "[[TMP-CMMI-002-03-04_OPA_조회_요청서_v1.0]]"
related_ex:
  - "[[EX-CMMI-002-03-04_OPA_조회_요청서_작성예시_v1.0]]"
standards: ["CMMI-DEV-ML3"]
scope_code: "CMMI"
status: approved
created: 2026-04-29
updated: 2026-04-29
tags: [WI, CMMI, EST, PAD]
---

# 과거 데이터 및 OPA 활용 (WI-CMMI-002-03-04)

> 상위 절차: [[PRO-CMMI-203_추정_관리_절차_v1.0]]

## 1. 업무 목적
조직 측정저장소·교훈 등 OPA 를 활용해 추정 신뢰성을 높인다.

## 2. 수행 주체
- 주 수행자: EST 전문가
- 검토자: PMO
- 승인자: PM

## 3. 범위
- 신규 추정 시

## 4. 입력 / 산출물
- Input: 측정저장소, 교훈, OPA
- Output: [[TMP-CMMI-002-03-04_OPA_조회_요청서_v1.0]], 분석 리포트

## 5. 수행 절차

### 5.1 사전 준비
1. 검색 키워드 정의.
2. 비교 가능 프로젝트 식별.

### 5.2 수행 단계
1. **OPA 조회**.
2. **유사도 평가**.
3. **데이터 추출·정제**.
4. **추정 매개변수 도출**.
5. **신뢰구간 부여**.
6. **이력 등재**.

### 5.3 완료 조건
- [ ] 조회 요청서 보관
- [ ] 분석 리포트
- [ ] 추정에 인용

## 6. 인터페이스 부서
- SEPG, MPM

## 7. 주의사항 / 예외 처리

### 7.1 유사 프로젝트 부재
- 부재 시 산업 벤치마크 보조.

### 7.2 데이터 노후
- 3년 이상 데이터는 가중치 하향.

### 7.3 외부 데이터
- 외부 데이터 인용 시 출처·라이선스 확인.

## 8. 연계 템플릿
- [[TMP-CMMI-002-03-04_OPA_조회_요청서_v1.0]]
- [[EX-CMMI-002-03-04_OPA_조회_요청서_작성예시_v1.0]]

## 9. KPI
| 지표 | 목표 | 주기 |
|---|---|---|
| OPA 활용률 | ≥ 80% | 분기 |

## 10. 출처
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/EST.pdf"
  locator: "EST 3.x — historical data and OPA"
  license: "ISACA copyright — paraphrase only"
```

## 11. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 1.0 | 2026-04-29 | 최초 승인 | PM |
