---
type: WI
doc_id: "WI-ASPICE-01-09-04"
title: "역량 매트릭스 관리 (MAN.3)"
version: "0.1"
owner: "Project Manager"
reviewer: "HR / Tech Lead"
approver: "Program Director"
scope: "프로젝트 착수 → 역할별 역량 요건 정의 → 팀원 역량 평가 → GAP 분석 → 교육·훈련 계획"
parent_pro: "[[PRO-ASPICE-01-09_프로젝트관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-09-04-01_역량매트릭스]]"]
related_rec: []
aspice_processes: ["MAN.3"]
entry_gate: "WI-ASPICE-01-09-01.status == done"
standards: ["Automotive SPICE 4.0"]
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, MAN.3, CompetencyMatrix, Training, ProjectManagement]
---

# 역량 매트릭스 관리 (WI-ASPICE-01-09-04)

> 상위 절차: [[PRO-ASPICE-01-09_프로젝트관리프로세스]]

## 1. 업무 목적
프로젝트 역할별 필수 역량을 정의하고, 팀원 역량을 정량 평가하여 GAP을 도출, 교육·훈련 계획으로 연결한다. ASPICE 4.0 MAN.3 BP3(프로젝트 인력 자원·기량 정의)에 부합한다.

## 2. 수행 주체
- **주수행자**: Project Manager
- **검토자**: HR Manager, Tech Lead
- **승인자**: Program Director

## 3. 범위
프로젝트 모든 인력(정규직, 파견, 외주) 및 모든 V-model 도메인(SW/HW/ML/QA/Safety) 역할에 적용한다. 매 프로젝트 단계 전환 시 갱신한다.

## 4. 입력 자료 / 산출물
- **Input**: 프로젝트 SOW, 사내 직무 카탈로그, 인사 평가 자료, 외부 자격(인증) 기록
- **Output**: 역량 매트릭스(TMP-ASPICE-01-09-04-01), 교육·훈련 계획표

## 5. 수행 절차 (단계별)

### 5.1 사전 준비
1. 사내 직무 카탈로그 및 ASPICE 4.0 PAM 발췌(역할별 요구 역량) 확인.
2. 팀원 명단·소속·이전 프로젝트 이력 수집.
3. HR과 인사평가/교육이수 데이터 공유 합의(개인정보 처리방침 준수).

### 5.2 수행 단계 (ASPICE BP 참조)
1. **BP3 역할별 필수 역량 정의** — 역할(SW/HW/ML/QA/Safety/PM)별로 필수 역량 항목과 최소 수준(1~5)을 정의.
2. **팀원 역량 평가** — 자가 평가 + Tech Lead 평가 + HR 데이터(자격증)로 1~5 점수 산정.
3. **GAP 분석** — 필수 최소 수준 미달 항목·인원수·GAP 크기 산출.
4. **교육·훈련 계획 수립** — 역량별로 사내 교육/외부 교육/OJT/멘토링 중 적합 방법 선정, 담당·마감 지정.
5. **승인 및 배포** — Program Director 승인 후 팀원에게 개별 통지.
6. **이행 점검** — 분기별 교육 이수 여부 확인, 매트릭스 갱신.
7. **단계 전환 시 재평가** — 단계 전환(SYS.2 → SWE.1 등) 시 새로운 역량 요구를 반영한 재평가 수행.

### 5.3 완료 조건 체크리스트
- [ ] 역할별 필수 역량과 최소 수준이 정의되어 있는가
- [ ] 모든 팀원의 역량 점수가 산정되어 있는가
- [ ] GAP 항목 각각에 교육 방법·담당·마감이 지정되어 있는가
- [ ] Program Director 승인이 기록되어 있는가
- [ ] 분기별 갱신 일정이 캘린더에 등록되어 있는가
- [ ] [[MAT-001_문서관리대장]] 갱신이 완료되었는가

## 6. 인터페이스 부서
- HR — 인사평가·교육이수·자격 데이터 제공
- Training Center — 사내 교육 일정·장소 조율
- 외부 교육기관 — 위탁 교육 진행

## 7. 주의사항 / 예외 처리
1. **개인정보 보호**: 역량 점수는 직무 적합성 판단 외 목적으로 활용 금지. 매트릭스 접근권한 PM/Tech Lead/HR로 제한.
2. **외주 인력**: 외주는 역량 요건만 계약 SOW에 명시하고, 점수 평가는 사내 인력으로 한정.
3. **GAP 미해소 시**: 교육 마감 후에도 미달이면 역할 재배정 또는 멘토링 강화로 대체.
4. **신규 합류자**: 합류 2주 내 평가·교육 계획 수립 의무화.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-09-04-01_역량매트릭스]]
- 작성예시: [[EX-ASPICE-01-09-04-01_역량매트릭스_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. 출처 (source_citation)
- `inputs/01_표준원문/VWAY_Motors/requirements.yaml`
- Automotive SPICE 4.0 PAM, MAN.3 BP3

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 작성 | Program Director |
