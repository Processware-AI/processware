---
type: WI
doc_id: "WI-ASPICE-01-08-01"
title: "문제 및 변경 처리 통합 (SUP.9 + SUP.10)"
version: "0.1"
owner: "Change Control Board (CCB) Chair"
reviewer: "QA / 도메인 Lead"
approver: "CCB"
scope: "문제 등록·RCA(SUP.9) + 변경요청·영향평가·CCB·구현·검증(SUP.10)"
parent_pro: "[[PRO-ASPICE-01-08_문제및변경관리프로세스]]"
related_tmp: []
related_rec: []
standards: ["Automotive SPICE 4.0"]
aspice_processes: ["SUP.9", "SUP.10"]
entry_gate: null
scope_type: "common"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SUP.9, SUP.10, CCB, RCA]
---

# 문제 및 변경 처리 통합 업무지침 (WI-ASPICE-01-08-01)

> 상위 절차: [[PRO-ASPICE-01-08_문제및변경관리프로세스]]
> ASPICE 매핑: SUP.9 (Problem Resolution) + SUP.10 (Change Request Management)

## 1. 업무 목적

식별된 문제(Problem) 와 변경요청(Change Request) 을 단일 트래킹 시스템에서 관리하고, RCA·영향평가·CCB 결재·구현·검증 절차로 일관되게 처리하여 품질·일정·리스크를 통제한다.

## 2. 수행 주체
- **주 수행자**: 문제·변경 등록자 + 책임 도메인
- **검토자**: QA, 도메인 Lead
- **승인자**: CCB (Change Control Board)

## 3. 범위
프로젝트 전 단계의 모든 문제·변경에 적용한다. 출시 후 Field Issue 도 동일 프로세스 적용.

## 4. 입력 자료 / 산출물
- **Input**: 문제 보고, 변경 요청
- **Output**: Problem Ticket, Change Request, 영향평가서, CCB 회의록, 변경 구현 결과, 검증 보고서

## 5. 수행 절차

### 5.1 사전 준비
1. 트래킹 도구(JIRA, Polarion, Redmine) 워크플로우 표준화.
2. CCB 정기 회의 일정 (예: 주 1회) 합의.

### 5.2 수행 단계

1. **문제 등록·분류** (SUP.9.BP1)
   - 발견 즉시 등록 + Severity (Critical/Major/Minor) + ASIL 영향.
   - 자동 책임 배정 (모듈 → 책임 도메인).

2. **RCA 실시** (SUP.9.BP2/3)
   - 5 Why / Fishbone 등 기법 사용.
   - Root Cause + 시정조치 + 재발 방지책 도출.

3. **변경요청 접수** (SUP.10.BP1)
   - 등록자·요지·범위·우선순위 명시.

4. **영향평가** (SUP.10.BP2)
   - 영향 받는 산출물·일정·비용·안전 분석.
   - 추적성 매트릭스 기반 자동 도출.

5. **CCB 결재** (SUP.10.BP3)
   - CCB 회의에서 승인/거부/보류 결정.
   - 결정 사유 + 회의록 보존.

6. **변경 구현** (SUP.10.BP4)
   - 책임 도메인이 구현 + 단위 시험.

7. **변경 검증** (SUP.10.BP5)
   - 영향 받는 모든 단계 회귀 시험.
   - QA 독립 검증.

8. **폐쇄·통보** (SUP.9.BP4 / SUP.10.BP6)
   - 폐쇄 시 모든 이해관계자 통보.

### 5.3 완료 조건 체크리스트
- [ ] 문제·변경 모두 트래킹 시스템 등록
- [ ] RCA 보고서 작성 (Critical/Major)
- [ ] 영향평가서 첨부 (변경)
- [ ] CCB 회의록 + 결재 기록 보존
- [ ] 변경 구현 + 회귀 시험 완료
- [ ] QA 독립 검증 + 폐쇄 통보 완료
- [ ] 추적성 매트릭스 갱신
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **CCB**: 변경 결재 (CTO·도메인 Lead·QA·Safety)
- **QA**: 독립 검증
- **Safety/Security Engineering**: ASIL/CAL 영향 검토
- **CM (SUP.8)**: 변경 형상관리

## 7. 주의사항 / 예외 처리

### 7.1 긴급 변경 (Hot-fix)
- 양산 ECU 의 안전 결함:
  - CCB 임시 결재 (이메일 또는 화상) → 24시간 내 정식 회의 보완.
  - 구현·검증 후 즉시 OEM 통보.

### 7.2 RCA 부실
- RCA 가 표면적 원인만 도출:
  - QA 가 재실시 요청 + Fishbone 표준 강제.
  - 반복 부실 시 RCA 교육 의무화.

### 7.3 변경 누락 (영향 산출물 미반영)
- 변경 후 일부 산출물 갱신 누락 발견:
  - 즉시 추가 변경 요청 등록 + 책임자 통보.
  - 누락 패턴 분석 + 추적성 도구 개선.

### 7.4 OEM 외부 변경 요청
- OEM 가 SyRS/StRS 변경 요청 시:
  - 본 절차로 정식 등록 + 영향평가 후 OEM 회신.
  - 합의 없는 임의 반영 금지.

## 8. 연계 템플릿 / 기록
- 기록 폴더: `vault/08_REC_기록/SUP.9_SUP.10/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SUP.9-* / VWAY-SUP.10-*"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SUP.9 + SUP.10 통합 + Hot-fix 절차 | (대기) |
