---
type: WI
doc_id: "WI-CMMI-004-02-05"
title: "변경요청 및 CCB 승인"
version: "1.0"
owner: "CCB 위원장"
reviewer: "PM"
approver: "Sponsor"
scope: "변경요청 접수·영향평가·CCB 심의·결정"
parent_pro: "[[PRO-CMMI-402_형상관리_절차_v1.0]]"
parent_pol: "[[POL-CMMI-004_품질_구성_및_의사결정_정책_v1.0]]"
related_tmp: ["[[TMP-CMMI-004-02-05_변경요청서_v1.0]]"]
related_ex: ["[[EX-CMMI-004-02-05_변경요청서_작성예시_v1.0]]"]
standards: ["CMMI-DEV-ML3", "ISO 9001"]
scope_code: "CMMI"
status: approved
created: 2026-04-29
updated: 2026-04-29
tags: [WI, CMMI, CM]
---

# 변경요청 및 CCB 승인 (WI-CMMI-004-02-05)

> 상위 절차: [[PRO-CMMI-402_형상관리_절차_v1.0]]

## 1. 업무 목적
기준선에 대한 변경을 통제된 절차로 심의·승인한다.

## 2. 수행 주체
- 주 수행자: CCB 위원장
- 검토자: PM, QA
- 승인자: Sponsor(Major)

## 3. 범위
- 베이스라인 후 모든 변경

## 4. 입력 / 산출물
- Input: 변경요청서
- Output: [[TMP-CMMI-004-02-05_변경요청서_v1.0]] 승인본, CCB 회의록

## 5. 수행 절차

### 5.1 사전 준비
1. 영향 평가.
2. 의제.

### 5.2 수행 단계
1. **요청 접수**.
2. **영향 평가**.
3. **CCB 심의**.
4. **결정**.
5. **이행**.
6. **검증**.

### 5.3 완료 조건
- [ ] 승인본
- [ ] 회의록
- [ ] 추적성 갱신

## 6. 인터페이스 부서
- 모든 팀

## 7. 주의사항 / 예외 처리

### 7.1 긴급 변경
- 사후 보완.

### 7.2 거절
- 사유 기록.

### 7.3 영향 누락
- 재평가.

## 8. 연계 템플릿
- [[TMP-CMMI-004-02-05_변경요청서_v1.0]]
- [[EX-CMMI-004-02-05_변경요청서_작성예시_v1.0]]

## 9. KPI
| 지표 | 목표 | 주기 |
|---|---|---|
| CCB 처리 SLA | ≤ 10영업일 | 분기 |

## 10. 출처
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/CM.pdf"
  locator: "CM 3.x — change control"
  license: "ISACA copyright — paraphrase only"
```

## 11. 개정 이력
| 1.0 | 2026-04-29 | 최초 승인 | Sponsor |
