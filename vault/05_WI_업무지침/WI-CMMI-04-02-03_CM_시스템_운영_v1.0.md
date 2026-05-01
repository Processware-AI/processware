---
type: WI
doc_id: "WI-CMMI-04-02-03"
title: "CM 시스템 운영"
version: "1.0"
owner: "DevOps"
reviewer: "CM Manager"
approver: "PM"
scope: "CM 시스템 운영·백업·접근 관리"
parent_pro: "[[PRO-CMMI-04-02_형상관리_절차_v1.0]]"
parent_pol: "[[POL-CMMI-04_품질_구성_및_의사결정_정책_v1.0]]"
related_tmp: ["[[TMP-CMMI-04-02-03-01_CM_시스템_운영표_v1.0]]"]
related_ex: ["[[EX-CMMI-04-02-03-01_CM_시스템_운영표_작성예시_v1.0]]"]
standards: ["CMMI-DEV-ML3", "ISO 9001"]
scope_code: "CMMI"
status: approved
created: 2026-04-29
updated: 2026-04-29
tags: [WI, CMMI, CM]
---

# CM 시스템 운영 (WI-CMMI-04-02-03)

> 상위 절차: [[PRO-CMMI-04-02_형상관리_절차_v1.0]]

## 1. 업무 목적
CM 도구·저장소를 안정 운영하고 데이터 손실·접근 위험을 통제한다.

## 2. 수행 주체
- 주 수행자: DevOps
- 검토자: CM Manager, 보안
- 승인자: PM

## 3. 범위
- Git·아티팩트 저장소·DB

## 4. 입력 / 산출물
- Input: 운영 정책
- Output: [[TMP-CMMI-04-02-03-01_CM_시스템_운영표_v1.0]]

## 5. 수행 절차

### 5.1 사전 준비
1. SLA 정의.
2. 백업 일정.

### 5.2 수행 단계
1. **모니터링**.
2. **백업**.
3. **권한 점검**.
4. **DR 훈련**.
5. **장애 대응**.
6. **보고**.

### 5.3 완료 조건
- [ ] 가용성 ≥ 99%
- [ ] 백업 검증
- [ ] DR 훈련 연 1회

## 6. 인터페이스 부서
- IT, 보안

## 7. 주의사항 / 예외 처리

### 7.1 장애
- RTO·RPO 준수.

### 7.2 권한 누설
- 즉시 회수.

### 7.3 백업 실패
- 즉시 IT 통보.

## 8. 연계 템플릿
- [[TMP-CMMI-04-02-03-01_CM_시스템_운영표_v1.0]]
- [[EX-CMMI-04-02-03-01_CM_시스템_운영표_작성예시_v1.0]]

## 9. KPI
| 지표 | 목표 | 주기 |
|---|---|---|
| 가용성 | ≥ 99% | 월 |

## 10. 출처
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/CM.pdf"
  locator: "CM 2.x — system operation"
  license: "ISACA copyright — paraphrase only"
```

## 11. 개정 이력
| 1.0 | 2026-04-29 | 최초 승인 | PM |
