---
doc_id: "WI-ASPICE-01-08-04"
title: "영향 평가 (SUP.10)"
type: WI
version: "0.1"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
owner: "Change Control Engineer"
reviewer: "Technical Lead / Safety Engineer / QA"
approver: "CCB Chair"
scope: "변경 요청 접수 후 → 기술·일정·비용·안전 영향 분석 → CCB 상정 준비"
scope_code: "ASPICE"
scope_type: "process"
domain: "ASPICE"
parent_pol: "[[POL-ASPICE-01_ASPICE품질정책]]"
parent_pro: "[[PRO-ASPICE-01-08_문제및변경관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-08-04-01_영향평가보고서]]"]
aspice_processes: ["SUP.10"]
entry_gate: "WI-ASPICE-01-08-03.status == done"
standards: ["Automotive SPICE 4.0"]
tags: [WI, ASPICE, SUP.10, ChangeManagement, ImpactAnalysis]
---

# WI-ASPICE-01-08-04 영향 평가 (SUP.10)

## 1. 업무 목적
접수된 변경 요청(CR)이 시스템·SW·HW·일정·비용·안전·보안에 미치는 영향을 정량·정성적으로
분석하여 CCB 가 합리적 의사결정을 내릴 근거를 제공한다. ASPICE SUP.10 BP3(영향 평가) 를 수행한다.

## 2. 수행 주체
- 주 수행자: Change Control Engineer
- 검토자: Technical Lead, Safety Engineer, QA
- 승인자: CCB Chair (영향 평가 보고서 검토 후 CCB 상정 승인)

## 3. 범위
- 대상: SUP.10 시스템에 등록된 모든 CR (Minor / Major / Emergency)
- 시점: CR 접수 ~ CCB 상정 전
- 제외: 안전·보안 영향 없는 단순 오타·문서 포맷 변경 (Process Owner 직접 처리)

## 4. 입력 자료 / 산출물
| 구분 | 항목 | 출처/위치 |
|---|---|---|
| 입력 | 변경 요청서 | SUP.10 시스템 (Jira) |
| 입력 | 추적성 매트릭스 (RTM) | SWE.6 산출물 |
| 입력 | 활성 베이스라인 등록서 | TMP-ASPICE-01-07-05-01 |
| 입력 | Safety Case / TARA | 안전·보안팀 보유 |
| 출력 | 영향 평가 보고서 | TMP-ASPICE-01-08-04-01 |
| 출력 | CCB 상정 자료 | CCB 회의 패키지 |

## 5. 수행 절차

### 5.1 사전 준비
1. CR 내용 확인 → 변경 유형 잠정 분류 (Minor / Major / Emergency).
2. 영향 분석에 필요한 산출물 (RTM, 베이스라인, Safety Case) 확보.
3. 분야별 분석자 (기술/안전/일정/비용) 지정.

### 5.2 수행 단계
1. **변경 유형 확정** — 영향 범위·위험도에 따라 Minor / Major / Emergency 확정 (SUP.10 BP3).
2. **기술 영향 분석** — 영향 받는 CI 목록 도출 (RTM 역추적), 변경되는 모듈·인터페이스 식별.
3. **안전 영향 분석** — ASIL 등급 변동 여부, Safety Case 갱신 필요성, FMEA 재실시 필요성 평가.
4. **사이버보안 영향 분석** — TARA 갱신 필요성, 신규 취약점 도입 여부 평가.
5. **일정 영향 분석** — 추가 작업량(MD) 산정, 마일스톤 영향, 재시험 일정 산정.
6. **비용 영향 분석** — 인건비·도구비·외부 의뢰비 산정.
7. **검증 계획 변경 평가** — 추가 시험 케이스, 재시험 범위 정의.
8. **CCB 권고안 작성** — 승인 / 조건부 승인 / 반려 / 보류 중 권고와 근거 명시.
9. **영향 평가 보고서 결재** — TMP-ASPICE-01-08-04-01 작성, 검토자 서명 후 CCB 상정.

### 5.3 완료 조건 체크리스트
- [ ] 변경 유형(Minor/Major/Emergency) 확정
- [ ] 영향 받는 CI 목록이 RTM 기반으로 도출됨
- [ ] ASIL 변동 여부 평가됨
- [ ] TARA 갱신 필요성 평가됨
- [ ] 일정·비용 영향 정량 산정됨
- [ ] 검증 계획 변경안 작성됨
- [ ] CCB 권고안과 근거가 명시됨
- [ ] 검토자 (Tech Lead / Safety / QA) 서명 완료
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- Systems / SW / HW Engineering: 기술 영향 분석 협조
- Functional Safety Team: 안전 영향 평가 (ASIL, Safety Case)
- Cybersecurity Team: TARA 영향 평가
- Project Management Office: 일정·비용 영향 검증
- QA: 검증 계획 변경 검토
- Configuration Management: 베이스라인 영향 확인

## 7. 주의사항 / 예외 처리

### 7.1 Emergency CR (긴급 변경)
안전·보안 사고 또는 양산 정지 위험 시 영향 평가를 6시간 내 압축 수행. 핵심 분석(안전·기술 영향)
만 우선 수행 후 Emergency CCB 소집. 일정·비용 분석은 사후 보완.

### 7.2 ASIL 등급 영향 발견 시
ASIL 등급이 변동되거나 Safety Case 갱신이 필요하면 자동으로 변경 유형을 Major 로 격상,
Functional Safety Manager 의 별도 승인 추가 필수.

### 7.3 추적성 단절 발견 시
영향 평가 중 RTM 단절 발견 시 평가를 중단하고 SWE.6 추적성 보완 후 재개.
추적성 부재 상태에서의 영향 평가는 신뢰성 없음.

### 7.4 다수 CR 의 상호 의존성
동일 CI 에 영향을 주는 복수 CR 이 동시에 평가될 경우 의존 관계를 명시하고 CCB 에 일괄 상정.
개별 처리로 인한 충돌·중복 작업 방지.

## 8. 연계 템플릿 / 기록
- 양식: [[TMP-ASPICE-01-08-04-01_영향평가보고서]]
- 작성예시: [[EX-ASPICE-01-08-04-01_영향평가보고서_작성예시]]
- 후속 절차: [[WI-ASPICE-01-08-05_CCB운영]]
- 연계 기록: 변경 요청서, RTM, Safety Case, TARA

## 9. 출처
```yaml
source_citation:
  - source: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    standard: "Automotive SPICE 4.0"
    process: "SUP.10 — Change Request Management"
    base_practices: ["BP2", "BP3", "BP4"]
    work_products: ["13-16 Change request", "13-21 Change control record"]
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 작성 (draft) | CCB Chair |
