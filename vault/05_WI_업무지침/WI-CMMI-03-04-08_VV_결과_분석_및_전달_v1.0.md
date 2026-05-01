---
type: WI
doc_id: "WI-CMMI-03-04-08"
title: "VV 결과 분석 및 전달"
version: "1.0"
owner: "QA Lead"
reviewer: "PM"
approver: "PM"
scope: "VV 결과 통계 분석·이해관계자 전달"
parent_pro: "[[PRO-CMMI-03-04_검증_및_확인_절차_v1.0]]"
parent_pol: "[[POL-CMMI-03_엔지니어링_정책_v1.0]]"
related_tmp: ["[[TMP-CMMI-03-04-08-01_VV_결과_분석서_v1.0]]"]
related_ex: ["[[EX-CMMI-03-04-08-01_VV_결과_분석서_작성예시_v1.0]]"]
standards: ["CMMI-DEV-ML3"]
scope_code: "CMMI"
status: approved
created: 2026-04-29
updated: 2026-04-29
tags: [WI, CMMI, VV]
---

# VV 결과 분석 및 전달 (WI-CMMI-03-04-08)

> 상위 절차: [[PRO-CMMI-03-04_검증_및_확인_절차_v1.0]]

## 1. 업무 목적
VV 결과 데이터를 통계 분석하고 이해관계자에게 전달하여 의사결정에 입력한다.

## 2. 수행 주체
- 주 수행자: QA 분석
- 검토자: PM
- 승인자: PM

## 3. 범위
- 분기 1회 + 베이스라인 시

## 4. 입력 / 산출물
- Input: VV 데이터
- Output: [[TMP-CMMI-03-04-08-01_VV_결과_분석서_v1.0]]

## 5. 수행 절차

### 5.1 사전 준비
1. 분석 가설.
2. 데이터 정합.

### 5.2 수행 단계
1. **수집**.
2. **분석**.
3. **시각화**.
4. **권고**.
5. **전달**.
6. **이행 추적**.

### 5.3 완료 조건
- [ ] 분석서
- [ ] 권고
- [ ] 이행 추적

## 6. 인터페이스 부서
- PCB, 개발

## 7. 주의사항 / 예외 처리

### 7.1 표본 부족
- 정성 보조.

### 7.2 외부 변수
- 분리 분석.

### 7.3 해석 편향
- 2인 검토.

## 8. 연계 템플릿
- [[TMP-CMMI-03-04-08-01_VV_결과_분석서_v1.0]]
- [[EX-CMMI-03-04-08-01_VV_결과_분석서_작성예시_v1.0]]

## 9. KPI
| 지표 | 목표 | 주기 |
|---|---|---|
| 분기 분석 적시성 | 분기말 +15일 | 분기 |

## 10. 출처
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/VV.pdf"
  locator: "VV 3.x — analyze and communicate"
  license: "ISACA copyright — paraphrase only"
```

## 11. 개정 이력
| 1.0 | 2026-04-29 | 최초 승인 | PM |
