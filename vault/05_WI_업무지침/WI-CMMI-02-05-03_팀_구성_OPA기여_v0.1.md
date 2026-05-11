---
type: WI
doc_id: WI-CMMI-02-05-03
title: "팀 구성 + OPA 기여 (SG1: SP1.6~1.7)"
version: "0.1"
status: draft
owner: "Project Manager"
reviewer: "HR Lead, EPG Lead"
approver: "PMO Director"
scope: "프로젝트 팀 헌장·공유 비전 수립 + 프로젝트 종료 후 OPA 기여"
scope_code: CMMI
parent_pro: "[[PRO-CMMI-02-05_통합_프로젝트_관리_절차]]"
parent_pol: "[[POL-CMMI-02_프로젝트_관리_정책]]"
related_tmp:
  - "[[TMP-CMMI-02-05-03-01_팀_헌장_공유_비전]]"
  - "[[TMP-CMMI-02-05-03-02_OPA_기여_자료]]"
related_rec: []
standards: [CMMI-DEV-ML3-V1.3]
standards_meta:
  publisher: "Software Engineering Institute (CMU/SEI)"
  year: 2010
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_acronym: IPM
sg_sp_refs:
  - "CMMIDEV-IPM-SP1.6-REQ-001"
  - "CMMIDEV-IPM-SP1.7-REQ-001"
entry_gate: "WI-CMMI-02-05-01.status == done"
scope_type: project
created: 2026-05-11
updated: 2026-05-11
tags: [WI, CMMI, IPM, ML3]
---

# 팀 구성 + OPA 기여 (WI-CMMI-02-05-03)

> 상위 절차: [[PRO-CMMI-02-05_통합_프로젝트_관리_절차]]

## 1. 업무 목적
프로젝트 시작 시 팀 헌장·공유 비전을 수립하여 협업 기반을 마련하고, 종료 시 측정값·교훈·개선제안을 OPA(PAL)에 기여한다 (GP 3.2 "Collect Experiences").

## 2. 수행 주체
- **주 수행자**: Project Manager
- **검토자**: HR Lead (팀 헌장), EPG Lead (OPA 기여)
- **승인자**: PMO Director

## 3. 범위
PRO-CMMI-02-05 §5 의 **SP1.6 (팀 구성) ~ SP1.7 (OPA 기여)**.

## 4. 입력 자료 / 산출물
- **Input**
  - 조직 팀 운영 표준 (OPD SP1.7)
  - 프로젝트 정의 프로세스
  - (종료 시) 프로젝트 측정 데이터·교훈
- **Output**
  - [[TMP-CMMI-02-05-03-01_팀_헌장_공유_비전]]
  - [[TMP-CMMI-02-05-03-02_OPA_기여_자료]] (종료 시)

## 5. 수행 절차

### 5.1 사전 준비
1. (팀 구성) 조직 팀 운영 표준 확보, kick-off 워크숍 일정.
2. (OPA 기여) 프로젝트 종료 시점 도래 확인.

### 5.2 수행 단계
1. **팀 헌장 작성 (SP1.6)** — 팀 비전, 역할·책임, 운영 규칙 (회의·의사소통·갈등 해결).
2. **공유 비전 워크숍** — 팀 모두 참여, 비전 합의.
3. **팀 운영 시작** — 정기 standup/회고 일정 가동.
4. **(프로젝트 종료 단계) OPA 기여 자료 수집 (SP1.7)** — 측정값 (effort, defect rate 등), 교훈 (잘된 점·개선점), 개선 제안.
5. **EPG 인계** — PAL 등록 ([[WI-CMMI-01-01-03]]).

### 5.3 완료 조건
- [ ] 팀 헌장 작성 + 전원 합의
- [ ] 공유 비전 워크숍 수행
- [ ] 정기 운영 (standup/회고) 가동
- [ ] (종료 시) OPA 기여 자료 ≥ 3 자산 (측정값, 교훈, 개선 제안 각 1+)
- [ ] EPG 인계 + PAL 등록 ID

## 6. 인터페이스 부서
- **HR**: 팀 운영 표준 자문
- **EPG**: OPA 기여 인수 ([[PRO-CMMI-01-01]])
- **PAL 운영자**: 자산 등록 ([[WI-CMMI-01-01-03]])
- **OPF**: 개선 제안 입력 ([[PRO-CMMI-01-02]] SP1.1)

## 7. 주의사항 / 예외 처리

### 7.1 팀원 변경 (mid-project)
- 핵심 팀원 변경 시 팀 헌장 갱신 + 신규 팀원 onboarding.
- 비전 재합의 시도 권장.

### 7.2 OPA 기여 자료 부족 (< 3건)
- 작은 프로젝트라 측정·교훈 부족한 경우: 최소 1건 (가장 가치 있는 교훈) 기여.
- 조직 차원에서 작은 프로젝트는 합산 통계로 PAL 등록 가능.

### 7.3 비전 불일치
- 워크숍에서 비전 합의 안 되는 경우: Sponsor 의견 청취 후 재합의.
- 분기 결정 안 되면 PMO Director 결정.

## 8. 연계 템플릿 / 기록
- 템플릿:
  - [[TMP-CMMI-02-05-03-01_팀_헌장_공유_비전]]
  - [[TMP-CMMI-02-05-03-02_OPA_기여_자료]]
- 작성예시:
  - [[EX-CMMI-02-05-03-01_팀_헌장_공유_비전_작성예시]]
  - [[EX-CMMI-02-05-03-02_OPA_기여_자료_작성예시]]

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-IPM-SP1.6-REQ-001 (p.167)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-IPM-SP1.7-REQ-001 (p.169)"
  retrieved_at: "2026-05-11"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (wi-tmp-writer) | - |
