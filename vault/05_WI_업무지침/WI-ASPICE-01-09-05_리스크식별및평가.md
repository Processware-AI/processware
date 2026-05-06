---
type: WI
doc_id: "WI-ASPICE-01-09-05"
title: "리스크 식별 및 평가 (MAN.5)"
version: "0.1"
owner: "Project Manager"
reviewer: "Tech Lead / QA / Safety Engineer"
approver: "Program Director"
scope: "프로젝트 전 기간 → 리스크 식별(브레인스토밍·체크리스트) → 발생가능성·영향도 평가 → 리스크 대장 등록"
parent_pro: "[[PRO-ASPICE-01-09_프로젝트관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-09-05-01_리스크대장]]"]
related_rec: []
aspice_processes: ["MAN.5"]
entry_gate: null
standards: ["Automotive SPICE 4.0"]
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, MAN.5, RiskManagement, RiskIdentification]
---

# 리스크 식별 및 평가 (WI-ASPICE-01-09-05)

> 상위 절차: [[PRO-ASPICE-01-09_프로젝트관리프로세스]]

## 1. 업무 목적
프로젝트 전 기간에 걸쳐 잠재 리스크를 체계적으로 식별·분류하고 발생가능성×영향도 매트릭스로 정량 평가하여 리스크 대장에 등록한다. ASPICE 4.0 MAN.5 BP1(리스크 관리 범위 정의), BP2(리스크 식별), BP3(리스크 분석)에 부합한다.

## 2. 수행 주체
- **주수행자**: Project Manager
- **검토자**: Tech Lead, QA Manager, Safety Engineer
- **승인자**: Program Director

## 3. 범위
프로젝트 착수~종결 전 기간에 적용한다. 신규 리스크는 수시로 등록 가능하며, 정식 식별 워크숍은 단계 전환 시(SYS.2 → SWE.1 등) 의무 실시한다.

## 4. 입력 자료 / 산출물
- **Input**: 실현 가능성 평가 보고서, 사내 리스크 분류표(taxonomy), 과거 프로젝트 Lessons Learned, 표준 체크리스트(ISO 26262 / ASPICE)
- **Output**: 리스크 대장(TMP-ASPICE-01-09-05-01)

## 5. 수행 절차 (단계별)

### 5.1 사전 준비
1. 사내 리스크 분류표(기술/일정/자원/공급업체/안전/규제) 최신본 확인.
2. 식별 워크숍 참가자(도메인 전문가 + Safety + QA) 일정 조율.
3. 과거 유사 프로젝트 Lessons Learned 조회.

### 5.2 수행 단계 (ASPICE BP 참조)
1. **BP1 범위 정의** — 리스크 관리 대상(전 단계/특정 단계), 평가 주기, 의사결정 권한 정의.
2. **BP2 리스크 식별** — 브레인스토밍 + 체크리스트 + Lessons Learned 기반으로 리스크 후보를 수집.
3. **분류** — 6개 카테고리(기술/일정/자원/공급업체/안전/규제)로 분류, 중복 제거.
4. **BP3 리스크 분석** — 발생가능성(1~5) × 영향도(1~5) 매트릭스 평가, 리스크 점수 산출.
5. **등급 부여** — HIGH (≥15), MEDIUM (8~14), LOW (≤7) 자동 분류.
6. **리스크 담당자 지정** — 카테고리에 따라 적합 담당자(예: 기술→Tech Lead, 안전→Safety Eng) 지정.
7. **초기 완화 전략** — 회피/이전/감소/수용 4가지 중 선택, 향후 추적 대상 표기.
8. **대장 등록 및 승인** — Program Director 결재 후 공식 베이스라인.

### 5.3 완료 조건 체크리스트
- [ ] 리스크 식별 워크숍 회의록이 보존되어 있는가
- [ ] 모든 리스크가 6개 카테고리로 분류되어 있는가
- [ ] 발생가능성·영향도·점수가 정량 표기되어 있는가
- [ ] HIGH 리스크 각각에 담당자와 완화 전략이 지정되어 있는가
- [ ] Program Director 승인이 기록되어 있는가
- [ ] [[MAT-001_문서관리대장]] 갱신이 완료되었는가

## 6. 인터페이스 부서
- 도메인 팀(SW/HW/ML) — 기술 리스크 식별
- Safety팀 — ISO 26262 hazard 연계
- 구매팀 — 공급업체 리스크 정보
- QA — 규제/심사 리스크

## 7. 주의사항 / 예외 처리
1. **신규 리스크 발생 시**: 워크숍을 기다리지 말고 즉시 PM에게 보고, 24시간 내 가평가 → 다음 검토 회의에서 정식 등록.
2. **점수 산정 의견 불일치 시**: 보수적 값(높은 점수)을 채택하고 사유를 비고에 기록.
3. **외부(고객/규제기관) 발견 리스크**: 외부 출처를 명시하고 우선순위 +1 가산.
4. **안전 관련 리스크**: ISO 26262 hazard analysis 결과와 교차 확인 후 등록.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-09-05-01_리스크대장]]
- 작성예시: [[EX-ASPICE-01-09-05-01_리스크대장_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. 출처 (source_citation)
- `inputs/01_표준원문/VWAY_Motors/requirements.yaml`
- Automotive SPICE 4.0 PAM, MAN.5 BP1/BP2/BP3

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 작성 | Program Director |
