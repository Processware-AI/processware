---
type: WI
doc_id: "WI-ASPICE-01-09-03"
title: "WBS 및 진척 통제 (MAN.3)"
version: "0.1"
owner: "Project Manager"
reviewer: "Tech Lead / PMO"
approver: "Program Director"
scope: "프로젝트 착수 후 → WBS 작성·기준선 설정 → 주간 진척 모니터링 → 이탈 시 시정"
parent_pro: "[[PRO-ASPICE-01-09_프로젝트관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-09-03-01_WBS및진척보고서]]"]
related_rec: []
aspice_processes: ["MAN.3"]
entry_gate: "WI-ASPICE-01-09-02.status == done"
standards: ["Automotive SPICE 4.0"]
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, MAN.3, WBS, ProgressControl, ProjectManagement]
---

# WBS 및 진척 통제 (WI-ASPICE-01-09-03)

> 상위 절차: [[PRO-ASPICE-01-09_프로젝트관리프로세스]]

## 1. 업무 목적
프로젝트 범위를 작업 패키지(work package) 수준으로 분해하여 일정·자원·산출물을 기준선화하고, 주간 단위로 진척과 편차(SPI/CPI)를 통제한다. ASPICE 4.0 MAN.3 BP4(프로젝트 활동·자원 정의), BP6(일정 정의·유지), BP9(진척 모니터링·통제)에 부합한다.

## 2. 수행 주체
- **주수행자**: Project Manager
- **검토자**: Tech Lead, PMO
- **승인자**: Program Director

## 3. 범위
모든 신규 및 변경 프로젝트의 착수~종결 전 기간에 적용한다. 주간 진척 보고는 의무, 월간 경영진 보고는 별도 양식으로 통합된다.

## 4. 입력 자료 / 산출물
- **Input**: 실현 가능성 평가 보고서, 고객 SOW, 사내 표준 V-model 일정 템플릿
- **Output**: WBS, 기준선 일정(Gantt), 주간 WBS·진척 보고서(TMP-ASPICE-01-09-03-01)

## 5. 수행 절차 (단계별)

### 5.1 사전 준비
1. 사내 V-model 표준 일정 템플릿 확보.
2. WBS 작성 도구(MS Project / Jira) 라이선스·접근 권한 확인.
3. 작업 패키지 책임자 후보군 식별.

### 5.2 수행 단계 (ASPICE BP 참조)
1. **BP4 활동·자원 정의** — V-model 단계별(SYS.1~SUP.10) 작업 패키지를 Level 3까지 분해.
2. **공수·기간 추정** — 3점 추정(낙관/보통/비관) 또는 과거 실적 기반 산정. 각 패키지 책임자(RACI A) 지정.
3. **BP6 기준선 일정 수립** — 의존성·임계 경로(Critical Path) 분석, 마일스톤 확정. Program Director 결재로 baseline freeze.
4. **BP9 진척 모니터링** — 주간 단위로 작업 패키지별 계획 % vs 실적 % 입력, SPI(=EV/PV), CPI(=EV/AC) 산출.
5. **편차 분석** — SPI/CPI 임계값(±10%) 초과 패키지 원인 분석.
6. **시정 조치** — 자원 추가 투입, 범위 조정, 일정 재계획 중 적합한 조치를 결정·실행.
7. **보고·승인** — 주간 진척 보고서를 Tech Lead/PMO 검토 후 Program Director에 제출.

### 5.3 완료 조건 체크리스트
- [ ] WBS Level 3까지 분해되어 있는가
- [ ] 작업 패키지별 책임자가 지정되어 있는가
- [ ] 기준선(Baseline) Gantt가 결재 freeze 되어 있는가
- [ ] 주간 진척 보고서가 정해진 요일에 제출되었는가
- [ ] SPI/CPI 임계 초과 항목에 시정 조치가 정의되었는가
- [ ] [[MAT-001_문서관리대장]] 갱신이 완료되었는가

## 6. 인터페이스 부서
- 각 도메인 팀(SW/HW/ML/QA/Safety) — 작업 패키지 실적 입력
- PMO — 측정 지표 통합
- 구매팀 — 외주 일정 동기화

## 7. 주의사항 / 예외 처리
1. **베이스라인 변경 요청 시**: ECR(Engineering Change Request) 절차를 통해 정식 baseline rebaseline을 거친다. 임의 수정 금지.
2. **인력 이탈/병가 발생 시**: 7일 이내 대체 인력 투입 계획을 보고하고 SPI 영향분석 첨부.
3. **외주 지연 시**: 페널티 조항 검토 + 사내 백업 작업으로 임계경로 보호.
4. **SPI < 0.85 (심각)**: Program Director 즉시 보고 + 회복 계획 2주 내 수립.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-09-03-01_WBS및진척보고서]]
- 작성예시: [[EX-ASPICE-01-09-03-01_WBS및진척보고서_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. 출처 (source_citation)
- `inputs/01_표준원문/VWAY_Motors/requirements.yaml`
- Automotive SPICE 4.0 PAM, MAN.3 BP4/BP6/BP9

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 작성 | Program Director |
