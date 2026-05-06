---
type: WI
doc_id: "WI-ASPICE-01-09-06"
title: "리스크 완화 추적 (MAN.5)"
version: "0.1"
owner: "Project Manager"
reviewer: "Tech Lead / QA"
approver: "Program Director"
scope: "리스크 등록 후 → 격주 완화 조치 실행 모니터링 → 잔여 리스크 재평가 → 리스크 종결 또는 에스컬레이션"
parent_pro: "[[PRO-ASPICE-01-09_프로젝트관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-09-06-01_리스크완화보고서]]"]
related_rec: []
aspice_processes: ["MAN.5"]
entry_gate: "WI-ASPICE-01-09-05.status == done"
standards: ["Automotive SPICE 4.0"]
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, MAN.5, RiskMitigation, RiskTracking]
---

# 리스크 완화 추적 (WI-ASPICE-01-09-06)

> 상위 절차: [[PRO-ASPICE-01-09_프로젝트관리프로세스]]

## 1. 업무 목적
리스크 대장에 등록된 리스크의 완화 조치를 격주 단위로 추적하여 잔여 점수를 재평가하고, SLA 내 미완화 HIGH 리스크는 에스컬레이션하며, 점수가 안정적으로 LOW 이하면 종결한다. ASPICE 4.0 MAN.5 BP4(리스크 처리 정의), BP5(리스크 모니터링), BP6(시정조치 실시)에 부합한다.

## 2. 수행 주체
- **주수행자**: Project Manager
- **검토자**: Tech Lead, QA Manager
- **승인자**: Program Director

## 3. 범위
리스크 대장에 등록된 모든 리스크를 대상으로 한다. HIGH 리스크는 주간, MEDIUM/LOW는 격주 검토를 원칙으로 하며, 단계 전환 시 전수 재평가한다.

## 4. 입력 자료 / 산출물
- **Input**: 리스크 대장(직전 버전), 완화 조치 진행 증빙(보고서·테스트 결과), 외부 변동 정보(고객/규제)
- **Output**: 리스크 완화 보고서(TMP-ASPICE-01-09-06-01), 갱신된 리스크 대장, 에스컬레이션 회의록

## 5. 수행 절차 (단계별)

### 5.1 사전 준비
1. 리스크 대장 직전 버전 및 직전 완화 보고서 조회.
2. 완화 조치 책임자별 진행 증빙 수집 요청(검토일 D-2).
3. HIGH 리스크 SLA 캘린더 확인.

### 5.2 수행 단계 (ASPICE BP 참조)
1. **BP4 처리 계획 점검** — 각 리스크의 완화 조치(액션) 진행률·증빙 수집.
2. **BP5 모니터링** — 잔여 리스크 점수 재평가(발생가능성·영향도 갱신).
3. **상태 갱신** — 등급 승강(HIGH→MEDIUM 등) 및 상태(Open/Mitigating/Closed) 변경.
4. **신규 리스크 추가** — 완화 과정에서 식별된 새 리스크는 WI-ASPICE-01-09-05 절차로 등록 후 본 보고서에 반영.
5. **종결 판정** — 잔여 점수 LOW 이하가 2회 연속 유지되면 종결 후보, Program Director 승인으로 종결.
6. **BP6 에스컬레이션** — HIGH 리스크가 SLA(예: 4주) 내 점수 감소 없을 시 Program Director에 즉시 보고.
7. **Lessons Learned** — 종결 리스크의 원인·대응을 사내 KB에 기록.

### 5.3 완료 조건 체크리스트
- [ ] 모든 Open 리스크의 완화 조치 진행률이 갱신되었는가
- [ ] 잔여 점수가 재평가되어 등급이 갱신되었는가
- [ ] 신규 리스크가 누락 없이 추가되었는가
- [ ] 종결 후보는 Program Director 승인을 받았는가
- [ ] 에스컬레이션 항목은 보고 완료되었는가
- [ ] [[MAT-001_문서관리대장]] 갱신이 완료되었는가

## 6. 인터페이스 부서
- 도메인 팀 — 완화 조치 실행 및 증빙 제공
- Safety/QA — 안전·품질 관련 리스크 재평가 검토
- 구매 — 공급업체 리스크 갱신
- 영업 — 외부(고객/규제) 변동 정보 공유

## 7. 주의사항 / 예외 처리
1. **증빙 미제출 시**: 진행률 0%로 간주하고 책임자에게 공식 통보, 1주 내 재제출 요구.
2. **잔여 점수 상승 시**: 완화 조치 실패로 판단, 즉시 PM·Tech Lead 합동 원인 분석.
3. **HIGH 리스크 SLA 초과**: Program Director 24시간 내 보고 의무. 자원 추가/범위 조정 결정.
4. **종결 후 재발 시**: Lessons Learned 미반영으로 분류, 원인 추적 + 프로세스 개선 연계.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-09-06-01_리스크완화보고서]]
- 작성예시: [[EX-ASPICE-01-09-06-01_리스크완화보고서_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. 출처 (source_citation)
- `inputs/01_표준원문/VWAY_Motors/requirements.yaml`
- Automotive SPICE 4.0 PAM, MAN.5 BP4/BP5/BP6

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 작성 | Program Director |
