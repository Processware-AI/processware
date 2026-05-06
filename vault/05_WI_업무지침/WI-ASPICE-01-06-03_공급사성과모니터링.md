---
doc_id: "WI-ASPICE-01-06-03"
title: "공급사 성과 모니터링 (ACQ.4)"
type: WI
version: "0.1"
status: draft
owner: "Supply Chain Engineer"
reviewer: "Project Manager / QA"
approver: "Procurement Manager"
scope: "계약 기간 중 → 공급사 산출물 품질·일정·ASPICE 성숙도 모니터링 → 성과 보고서 발행"
scope_type: project
scope_code: ASPICE
domain: ASPICE
parent_pro: "[[PRO-ASPICE-01-06_구매및공급망프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-06-03-01_공급사성과보고서]]"]
aspice_processes: ["ACQ.4"]
entry_gate: "WI-ASPICE-01-06-02.status == done"
standards: ["Automotive SPICE 4.0"]
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, ACQ.4, Supplier, PerformanceMonitoring]
---

# WI-ASPICE-01-06-03 — 공급사 성과 모니터링 (ACQ.4)

## 1. 업무 목적
공급사의 일정·품질·ASPICE 성숙도를 정량 KPI 로 정기 모니터링하여 위험 사전 식별 및 시정조치 의사결정에 활용한다. ASPICE 4.0 ACQ.4 의 성과 모니터링·평가 활동을 충족한다.

## 2. 수행 주체
- **주 수행자**: Supply Chain Engineer
- **검토자**: Project Manager / QA
- **승인자**: Procurement Manager

## 3. 범위
- 대상: 1차 공급사(Tier-1) 전수, 2차 공급사 중 핵심 부품 공급
- 주기: 분기(quarterly) 정기 + 이슈 발생 시 임시
- 제외: 신규 공급사 자격 평가는 별도 프로세스 적용

## 4. 입력 자료 / 산출물
**입력 자료**
- 계약상 KPI 정의 (SLA·품질·일정)
- 공급사 산출물 수령 기록 (CM)
- 결함 데이터 (SUP.9 연계)
- 회의록·Action Item 트래커 (WI-ASPICE-01-06-02)
- 공급사 ASPICE 평가 결과 (외부 평가)

**산출물**
- 공급사 성과 보고서(TMP-ASPICE-01-06-03-01)
- 공급사 스코어카드 (Green/Yellow/Red)
- 시정조치 요구 입력 (필요 시 WI-ASPICE-01-06-04 트리거)

## 5. 수행 절차

### 5.1 사전 준비
1. KPI 정의서·임계값(목표/경고/위험) 최신본 확인.
2. 모니터링 기간(분기) 데이터 수집 범위 확정.
3. 공급사 측 성과 자료(자기 보고) 수령.
4. 직전 보고서·Action Item 진행률 확인.

### 5.2 수행 단계
1. **데이터 수집** (ACQ.4 BP4) — KPI 별 실적 데이터를 출처 시스템에서 추출한다.
2. **KPI 산정** (ACQ.4 BP5) — 일정 준수율·결함 밀도·리뷰 지적 수 등 산정.
3. **ASPICE 성숙도 결과 통합** — 외부 평가(예: SWE.1~3 CL2) 결과를 통합한다.
4. **이슈·리스크 종합** — 회의록·트래커의 미해결 이슈를 위험으로 분류한다.
5. **종합 평가** (ACQ.4 BP6) — Green/Yellow/Red 신호등으로 종합 판정한다.
6. **조치 사항 권고** — Yellow 이상은 시정조치(WI-ASPICE-01-06-04) 트리거 권고.
7. **보고서 작성·승인** — 검토자 회람 후 Procurement Manager 결재.
8. **공급사 통보** — 공식 채널로 결과 통보 및 차기 검토일 안내.

### 5.3 완료 조건 체크리스트
- [ ] KPI 별 실적 데이터의 출처가 명시되었다.
- [ ] KPI 산정 결과가 임계값 대비 판정되었다.
- [ ] ASPICE 성숙도 결과가 통합되었다.
- [ ] 미해결 이슈/리스크가 분류되었다.
- [ ] 종합 신호등이 Green/Yellow/Red 로 판정되었다.
- [ ] Yellow 이상에 대해 시정조치 권고가 명시되었다.
- [ ] 보고서가 결재 완료되었다.
- [ ] 공급사 통보가 발송되었다.
- [ ] [[MAT-001_문서관리대장]] 갱신 완료.

## 6. 인터페이스 부서
- 프로젝트 관리: 일정 데이터 제공·리스크 합동 평가
- QA: 결함 데이터·리뷰 지적 데이터 제공
- 외부 평가팀: ASPICE 평가 결과 제공
- 법무: Red 판정 시 계약 조치 검토

## 7. 주의사항 / 예외 처리

### 7.1 데이터 누락
KPI 산정에 필요한 데이터가 누락되면 산정 불가 항목으로 표시하고 사유·예상 입수 일정을 기록한다. 임의 보간 금지.

### 7.2 Red 판정 발생
Red 판정 시 즉시 PM·법무에 통보하고 시정조치 요구서(WI-ASPICE-01-06-04)를 발행한다. 공급선 다변화 검토도 병행.

### 7.3 공급사 자기 보고와 실측 차이
공급사 자기 보고와 당사 실측 KPI 의 차이가 임계값(예: ±10%) 을 초과하면 차이의 원인을 회의 안건으로 등록.

### 7.4 임계값 자체의 적정성 의심
연속 2분기 모든 공급사가 Green 또는 Red 인 경우 임계값 재조정을 PM 협의로 검토한다.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-06-03-01_공급사성과보고서]]
- 작성예시: [[EX-ASPICE-01-06-03-01_공급사성과보고서_작성예시]]
- 상위 절차: [[PRO-ASPICE-01-06_구매및공급망프로세스]]
- 후속 단계: [[WI-ASPICE-01-06-04_합의변경및시정조치]]
- 추적성: [[MAT-007_요구사항추적매트릭스]]

## 9. 출처
```yaml
source_citation:
  - file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    section: "ACQ.4 / ASPICE 4.0"
    accessed: "2026-05-06"
standards:
  - "Automotive SPICE 4.0 — ACQ.4 Supplier Monitoring"
```

## 10. 개정 이력
| 버전 | 일자 | 변경 내용 | 승인자 |
|------|------|-----------|--------|
| 0.1 | 2026-05-06 | 최초 작성 (Draft) | Procurement Manager |
