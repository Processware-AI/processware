---
type: WI
doc_id: "WI-CMMI-003-04-05"
title: "VV 절차 및 기준"
version: "1.0"
owner: "QA Lead"
reviewer: "PM"
approver: "PM"
scope: "VV 단계별 절차·진입·종료 기준"
parent_pro: "[[PRO-CMMI-304_검증_및_확인_절차_v1.0]]"
parent_pol: "[[POL-CMMI-003_엔지니어링_정책_v1.0]]"
related_tmp: ["[[TMP-CMMI-003-04-05_VV_절차서_v1.0]]"]
related_ex: ["[[EX-CMMI-003-04-05_VV_절차서_작성예시_v1.0]]"]
standards: ["CMMI-DEV-ML3"]
scope_code: "CMMI"
status: approved
created: 2026-04-29
updated: 2026-04-29
tags: [WI, CMMI, VV]
---

# VV 절차 및 기준 (WI-CMMI-003-04-05)

> 상위 절차: [[PRO-CMMI-304_검증_및_확인_절차_v1.0]]

## 1. 업무 목적
VV 활동의 단계별 절차·게이트 기준을 명문화하여 품질 게이트를 확보한다.

## 2. 수행 주체
- 주 수행자: QA Lead
- 검토자: PM
- 승인자: PM

## 3. 범위
- 모든 VV 활동

## 4. 입력 / 산출물
- Input: 방법 선정서
- Output: [[TMP-CMMI-003-04-05_VV_절차서_v1.0]]

## 5. 수행 절차

### 5.1 사전 준비
1. 단계 정의.
2. 게이트 후보.

### 5.2 수행 단계
1. **진입 기준**.
2. **활동**.
3. **종료 기준**.
4. **롤백**.
5. **검토·승인**.
6. **공유**.

### 5.3 완료 조건
- [ ] 절차서 승인본
- [ ] 게이트 운영
- [ ] 롤백 검증

## 6. 인터페이스 부서
- 개발, CM

## 7. 주의사항 / 예외 처리

### 7.1 우회
- 우회 단계 무효화.

### 7.2 미충족
- 시정 후 재진입.

### 7.3 외부 의존
- 외부 합의 시점.

## 8. 연계 템플릿
- [[TMP-CMMI-003-04-05_VV_절차서_v1.0]]
- [[EX-CMMI-003-04-05_VV_절차서_작성예시_v1.0]]

## 9. KPI
| 지표 | 목표 | 주기 |
|---|---|---|
| 게이트 통과율 | ≥ 90% | 분기 |

## 10. 출처
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/VV.pdf"
  locator: "VV 2.x — procedure and criteria"
  license: "ISACA copyright — paraphrase only"
```

## 11. 개정 이력
| 1.0 | 2026-04-29 | 최초 승인 | PM |
