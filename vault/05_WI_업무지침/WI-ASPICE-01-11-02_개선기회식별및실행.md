---
type: WI
doc_id: "WI-ASPICE-01-11-02"
title: "개선 기회 식별 및 실행 (PIM.3)"
version: "0.1"
owner: "Process Engineer"
reviewer: "QA Manager / Project Manager"
approver: "Process Improvement Board"
scope: "프로세스 평가 결과 / MAN.6 측정 경보 / SUP.1 QA 발견 → 개선 기회 등록 → 개선 실행 → 효과 검증"
parent_pro: "[[PRO-ASPICE-01-11_프로세스개선및재사용]]"
related_tmp: ["[[TMP-ASPICE-01-11-02-01_개선기회등록서]]"]
related_rec: []
aspice_processes: ["PIM.3"]
entry_gate: "WI-ASPICE-01-11-01.status == done"
scope_type: "common"
standards: ["Automotive SPICE 4.0"]
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, PIM.3, ProcessImprovement, OPP]
---

# 개선 기회 식별 및 실행 (WI-ASPICE-01-11-02)

> 상위 절차: [[PRO-ASPICE-01-11_프로세스개선및재사용]]
> ASPICE 4.0 PIM.3.BP3/BP4/BP5 — 개선 기회 식별·실행·효과 측정

## 1. 업무 목적

본 지침은 [[WI-ASPICE-01-11-01_프로세스평가]] 결과 + MAN.6 측정 경보 + SUP.1 QA 발견 + 회고(Retrospective) 등 다양한 출처에서 발생한 **프로세스 개선 기회를 등록·우선순위화·파일럿·전사 배포** 의 단계로 운영하여, 프로세스 자산(SPP) 의 지속적 개선을 실현하는 데 목적이 있다.

## 2. 수행 주체

| 역할 | 담당 |
|---|---|
| 주수행자 | Process Engineer |
| 검토자 | QA Manager / Project Manager |
| 승인자 | Process Improvement Board |

## 3. 범위

VWAY Motors 의 모든 조직 표준 프로세스(11개 PRO + 하위 WI/TMP) 와 운영 도구(JIRA, Polarion, Git/Gerrit 등)에 대한 개선 활동에 적용한다. 1회성 프로젝트 차원의 개선(고유 도구 설정 변경 등) 은 본 절차 대상이 아니다.

## 4. 입력 자료 / 산출물

- **Input**:
  - [[WI-ASPICE-01-11-01_프로세스평가]] 평가 보고서 (Gap·Strength)
  - MAN.6 측정 데이터 경보(예: 결함 밀도 임계 초과)
  - SUP.1 QA 감사 발견 사항
  - 프로젝트 회고(Retrospective) 결과
  - 고객 피드백 / VOC
- **Output**:
  - [[TMP-ASPICE-01-11-02-01_개선기회등록서]] 작성 산출물
  - OPP 백로그(Organization Process Performance Backlog)
  - 개선 실행 결과 보고 (개선 전후 KPI 비교)
  - 갱신된 프로세스 자산(WI/TMP/PRO 변경 PR)

## 5. 수행 절차

### 5.1 사전 준비

1. 개선 기회 출처 채널(Process Assessment, MAN.6 알림, SUP.1 보고, Retrospective, VOC)을 정의하고 수집 주기를 정한다 (월 1회 정기).
2. OPP 백로그 도구(JIRA Project: OPP) 를 확인하고 중복 등록 여부를 점검한다.
3. 우선순위 평가 기준(Impact × Effort 매트릭스, ICE 점수 등) 을 합의한다.
4. Process Improvement Board 정기 회의 일정을 확보한다 (월 1회).
5. 파일럿 대상 팀·범위·기간 후보를 사전 검토한다.

### 5.2 수행 단계 (ASPICE PIM.3.BP3/BP4/BP5 참조)

1. **개선 기회 수집** — 5개 출처 채널에서 발생한 개선 후보를 OPP 백로그에 표준 양식으로 등록한다 (제안자·출처·문제 기술·기대 효과).
2. **중복 통합 및 분류** — 동일 또는 유사 개선 기회를 통합하고, 영향 프로세스 영역(SWE / SUP / MAN / SPL 등) 별로 분류한다.
3. **우선순위 평가** — 각 기회를 Impact(품질·생산성·리스크 영향) × Effort(소요 공수·복잡도) 로 평가하고 High / Medium / Low 우선순위를 부여한다.
4. **선택 및 책임자 지정** — Process Improvement Board 가 분기당 3~5건의 High 우선순위를 선택하고 개선 책임자를 지정한다.
5. **개선안 설계** — 책임자가 개선 방법(프로세스 변경, 도구 자동화, 체크리스트 신설 등) 과 파일럿 범위·기간을 정의한다.
6. **개선 전 KPI 측정** — 개선 효과 측정의 베이스라인을 위해 개선 전 KPI 값을 기록한다 (예: 코드 리뷰 효과성 = 결함/리뷰시간).
7. **파일럿 실행** — 1~2개 팀에서 4~8주 파일럿을 실행하고, 운영 이슈를 수집한다.
8. **개선 후 KPI 측정 및 효과 검증** — 파일럿 종료 시 개선 후 KPI 를 측정하고, 통계적 유의성·목표 달성 여부를 평가한다.
9. **전사 배포 또는 폐기** — 효과 검증 시 SPP 자산을 갱신하고 전사 배포한다. 효과 미달 시 원인 분석 후 폐기 또는 재설계.
10. **종결 선언** — Process Improvement Board 가 종결 결재를 한다. 갱신된 자산은 [[WI-ASPICE-01-01-04_조직표준프로세스개정관리]] 또는 동등 절차로 정식 개정한다.

### 5.3 완료 조건 체크리스트

- [ ] 5개 출처 채널의 개선 기회가 OPP 백로그에 등록되었다.
- [ ] 중복 통합 및 영역별 분류가 완료되었다.
- [ ] 우선순위 평가(Impact × Effort) 결과가 기록되었다.
- [ ] Process Improvement Board 가 선택 결정을 결재하였다.
- [ ] 개선 전 KPI 베이스라인이 측정·기록되었다.
- [ ] 파일럿이 4~8주 동안 실행되었다.
- [ ] 개선 후 KPI 가 측정되고 효과 판정이 완료되었다.
- [ ] 효과 검증 시 SPP 자산(WI/TMP) 갱신 PR 이 머지되었다.
- [ ] 종결 선언 결재가 완료되었다.
- [ ] [[TMP-ASPICE-01-11-02-01_개선기회등록서]] 가 결재 완료되어 `08_REC_기록/` 에 보관되었다.
- [ ] [[MAT-001_문서관리대장]] 에 본 산출물이 등록되었다.

## 6. 인터페이스 부서

| 부서 | 인터페이스 내용 |
|---|---|
| Process Quality Office | 개선 기회 수집·통합·우선순위 평가 주관 |
| QA (SUP.1) | QA 발견 사항 제공, 개선 검증 참여 |
| Project Management Office | 프로젝트 회고 결과 제공, 파일럿 협조 |
| Engineering Teams | 파일럿 수행, KPI 데이터 제공 |
| MAN.6 측정팀 | 측정 데이터 경보 제공, 효과 검증 분석 |

## 7. 주의사항 / 예외 처리

1. **개선 기회 폭주 시 우선순위 충돌** — 분기 신규 등록이 30건을 초과하면 Process Improvement Board 가 임시 회의를 열어 카테고리별 상한(SWE 2건, SUP 1건 등)을 적용한다.
2. **파일럿 효과 미달** — 개선 후 KPI 가 베이스라인 대비 통계적으로 유의한 개선이 없으면 자동 폐기. 부분 효과는 보완 설계 후 재파일럿(1회 한정).
3. **전사 배포 중 부작용 발생** — 배포 후 다른 KPI 가 악화되면 즉시 롤백하고 원인 분석. 1주 이내 롤백 결정 미수행 시 자동 롤백.
4. **고객 보안 규정 위반 우려** — 개선안이 고객사 보안 정책(코드 외부 공유 제한 등) 과 충돌하면 보류하고 [[PRO-ASPICE-01-09_사이버보안프로세스]] 와 협의한다.

## 8. 연계 템플릿 / 기록

- 템플릿: [[TMP-ASPICE-01-11-02-01_개선기회등록서]]
- 작성예시: [[EX-ASPICE-01-11-02-01_개선기회등록서_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. 출처 (source_citation)

```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-PIM.3-BP3, VWAY-PIM.3-BP4, VWAY-PIM.3-BP5"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력

| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — PIM.3 개선 기회 식별·실행 정의 | (대기) |
