---
type: WI
doc_id: "WI-CMMI-003-04-03"
title: "VV 대상 및 방법 선정"
version: "1.0"
owner: "QA Lead"
reviewer: "PM"
approver: "PM"
scope: "검증·확인 대상·방법(테스트·시뮬·리뷰) 선정"
parent_pro: "[[PRO-CMMI-304_검증_및_확인_절차_v1.0]]"
parent_pol: "[[POL-CMMI-003_엔지니어링_정책_v1.0]]"
related_tmp: ["[[TMP-CMMI-003-04-03_VV_방법선정서_v1.0]]"]
related_ex: ["[[EX-CMMI-003-04-03_VV_방법선정서_작성예시_v1.0]]"]
standards: ["CMMI-DEV-ML3"]
scope_code: "CMMI"
status: approved
created: 2026-04-29
updated: 2026-04-29
tags: [WI, CMMI, VV]
---

# VV 대상 및 방법 선정 (WI-CMMI-003-04-03)

> 상위 절차: [[PRO-CMMI-304_검증_및_확인_절차_v1.0]]

## 1. 업무 목적
산출물별 적합한 V&V 대상·방법을 선정하여 효율적 품질 활동을 보장한다.

## 2. 수행 주체
- 주 수행자: QA Lead
- 검토자: PM
- 승인자: PM

## 3. 범위
- 모든 산출물

## 4. 입력 / 산출물
- Input: 산출물 목록, 위험
- Output: [[TMP-CMMI-003-04-03_VV_방법선정서_v1.0]]

## 5. 수행 절차

### 5.1 사전 준비
1. 방법 옵션(검증·시뮬·리뷰·인스펙션).
2. 비용·효과.

### 5.2 수행 단계
1. **분류**.
2. **방법 매핑**.
3. **자원 산정**.
4. **승인**.
5. **계획 등록**.
6. **갱신**.

### 5.3 완료 조건
- [ ] 선정서 승인본
- [ ] 자원 확보
- [ ] 계획 등록

## 6. 인터페이스 부서
- 개발, PM

## 7. 주의사항 / 예외 처리

### 7.1 자동화 가능
- 가능 시 우선.

### 7.2 비용 과다
- 우선순위 재조정.

### 7.3 변경
- 산출물 변경 시 재선정.

## 8. 연계 템플릿
- [[TMP-CMMI-003-04-03_VV_방법선정서_v1.0]]
- [[EX-CMMI-003-04-03_VV_방법선정서_작성예시_v1.0]]

## 9. KPI
| 지표 | 목표 | 주기 |
|---|---|---|
| 방법 적합도 | ≥ 90% | 분기 |

## 10. 출처
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/VV.pdf"
  locator: "VV 2.x — select target and method"
  license: "ISACA copyright — paraphrase only"
```

## 11. 개정 이력
| 1.0 | 2026-04-29 | 최초 승인 | PM |
