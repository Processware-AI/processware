---
type: WI
doc_id: "WI-ASPICE-01-09-01"
title: "프로젝트 계획 및 모니터링 (MAN.3 통합)"
version: "0.1"
owner: "Project Manager"
reviewer: "PMO Lead / QA"
approver: "CTO"
scope: "프로젝트 계획 수립 → WBS·일정 → 진척 모니터링 → 통제·보고"
parent_pro: "[[PRO-ASPICE-01-09_프로젝트관리프로세스]]"
related_tmp: []
related_rec: []
standards: ["Automotive SPICE 4.0"]
aspice_processes: ["MAN.3"]
entry_gate: null
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, MAN.3, PM, WBS]
---

# 프로젝트 계획 및 모니터링 업무지침 (WI-ASPICE-01-09-01)

> 상위 절차: [[PRO-ASPICE-01-09_프로젝트관리프로세스]]
> ASPICE 매핑: MAN.3 (Project Management) — BP1~BP10

## 1. 업무 목적

프로젝트의 범위·일정·자원·리스크를 계획·통제하여 OEM 약속 일정을 준수하고, 정량 지표 기반의 모니터링·보고로 의사결정을 지원한다.

## 2. 수행 주체
- **주 수행자**: Project Manager
- **검토자**: PMO Lead, QA, 도메인 Lead
- **승인자**: CTO

## 3. 범위
프로젝트 착수(Charter) 부터 종료(Closure) 까지 적용한다.

## 4. 입력 자료 / 산출물
- **Input**: 프로젝트 Charter, OEM 일정 약속, 자원 풀, 표준 프로세스
- **Output**: Project Plan, WBS, Schedule, Status Report, Closure Report

## 5. 수행 절차

### 5.1 사전 준비
1. PM 도구(MS Project, Jira) + 보고 양식 준비.
2. 도메인별 자원 가용성 확인.

### 5.2 수행 단계

1. **프로젝트 범위 정의** (MAN.3.BP1)
   - Charter, 산출물 목록, 마일스톤.

2. **실현가능성 평가** (MAN.3.BP2)
   - 일정·자원·기술 실현 가능성 분석.
   - 미실현 시 OEM 협상 또는 범위 조정.

3. **WBS·일정 수립** (MAN.3.BP3)
   - WBS 분해 + Critical Path 식별.
   - 마일스톤 + Gate Review 일정.

4. **자원·역량 배정** (MAN.3.BP4)
   - 도메인별 인력 + 환경(HW/도구) 배정.
   - 역량 매트릭스 갱신.

5. **이해관계자 인터페이스** (MAN.3.BP5)
   - OEM·내부·공급사 보고 채널·주기.

6. **진척 모니터링** (MAN.3.BP6/7)
   - 주간 Status Meeting + KPI 수집.
   - 일정 이탈 감지 시 즉시 시정.

7. **변경·이슈 통제** (MAN.3.BP8)
   - SUP.10 변경 + SUP.9 문제 연계.

8. **보고·검토** (MAN.3.BP9)
   - 마일스톤 검토 + 경영검토 입력.

9. **종료** (MAN.3.BP10)
   - Lessons Learned + Closure Report.

### 5.3 완료 조건 체크리스트
- [ ] Charter + WBS + Schedule 베이스라인 등록
- [ ] 자원 배정 + 역량 매트릭스 갱신 완료
- [ ] 주간 Status Meeting 100% 실행
- [ ] 마일스톤 Gate Review 결과 문서화
- [ ] 일정 이탈 시 시정조치 추적 완료
- [ ] Closure Report 작성 + Lessons Learned 보존
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **OEM Customer**: 일정·이슈 보고
- **도메인 Lead**: 자원 합의·진척
- **MAN.5 (Risk)**: 리스크 통합
- **MAN.6 (Measurement)**: KPI 수집
- **QA (SUP.1)**: 프로세스 준수 보증

## 7. 주의사항 / 예외 처리

### 7.1 일정 이탈 (Critical Path)
- Critical Path 활동 지연:
  - 즉시 영향 분석 + 회복 계획.
  - OEM 일정 영향 시 즉시 통보 + 협상.

### 7.2 자원 이탈 (인력 퇴사)
- 핵심 인력 이탈 시:
  - 즉시 후임 배정 + 인계 계획 (knowledge transfer).
  - 일정 영향 평가 + 보완 인력 채용·외주.

### 7.3 OEM 범위 추가 (Scope Creep)
- OEM 가 비공식 범위 확대 요구:
  - 정식 SUP.10 변경 절차 강제.
  - 일정·비용·자원 영향 협상 후 진행.

### 7.4 다중 프로젝트 충돌 (Resource Contention)
- 동일 인력의 다중 프로젝트 배정 충돌:
  - PMO 가 우선순위 조정 + 자원 재배정.
  - 미해결 시 CTO 결정.

## 8. 연계 템플릿 / 기록
- 기록 폴더: `vault/08_REC_기록/MAN.3/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-MAN.3-PURPOSE-001 / VWAY-MAN.3-BP1~BP10"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — MAN.3 BP1~BP10 통합 | (대기) |
