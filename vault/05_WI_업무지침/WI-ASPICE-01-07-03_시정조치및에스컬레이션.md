---
doc_id: "WI-ASPICE-01-07-03"
title: "시정 조치 및 에스컬레이션 (SUP.1)"
type: WI
version: "0.1"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
owner: "QA Engineer"
reviewer: "Project Manager / Process Owner"
approver: "QA Manager"
scope: "QA 감사 Major 발견 → 시정 조치 계획 수립·실행·검증 → 미해결 시 에스컬레이션"
scope_code: "ASPICE"
scope_type: "process"
domain: "ASPICE"
parent_pol: "[[POL-ASPICE-01_ASPICE품질정책]]"
parent_pro: "[[PRO-ASPICE-01-07_품질보증및형상관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-07-03-01_시정조치계획서]]"]
aspice_processes: ["SUP.1"]
entry_gate: "audit_finding_detected == true"
standards: ["Automotive SPICE 4.0"]
tags: [WI, ASPICE, SUP.1, QA, CorrectiveAction, Escalation]
---

# WI-ASPICE-01-07-03 시정 조치 및 에스컬레이션 (SUP.1)

## 1. 업무 목적
QA 감사(WI-ASPICE-01-07-02) 또는 운영 중 식별된 부적합에 대해 근본원인 분석 → 시정 조치 →
효과 검증 → 종결의 닫힌 루프(closed-loop)를 운영하고, 마감 초과·반복 발생 시 즉시
경영진에게 에스컬레이션한다. ASPICE SUP.1 BP6(부적합 추적·종결) 을 수행한다.

## 2. 수행 주체
- 주 수행자: QA Engineer
- 검토자: Project Manager, 해당 Process Owner
- 승인자: QA Manager

## 3. 범위
- 대상: QA 감사 Major 발견사항 + 운영 중 SUP.9 등록된 프로세스 부적합
- 시점: 감사 보고서 종결 미팅 직후 ~ 시정 종결까지
- 제외: 제품 결함(별도 SUP.9 결함관리) — 본 WI 는 프로세스 부적합 한정

## 4. 입력 자료 / 산출물
| 구분 | 항목 | 출처/위치 |
|---|---|---|
| 입력 | QA 감사 보고서 (Major 발견사항) | TMP-ASPICE-01-07-02-01 |
| 입력 | SUP.9 문제 보고서 | 문제관리 시스템 |
| 출력 | 시정 조치 계획서 | TMP-ASPICE-01-07-03-01 |
| 출력 | 효과 검증 결과 | 시정 조치 계획서 §5 |
| 출력 | 에스컬레이션 통보(필요 시) | 이메일·회의록 |

## 5. 수행 절차

### 5.1 사전 준비
1. 시정 대상 발견사항 목록 확정(감사 보고서 §6 후속 조치 계획).
2. 발견사항별 책임자 지명 확인(미지명 시 PM 과 협의 후 지정).
3. 근본원인 분석 도구(5 Why, Fishbone 등) 선정.

### 5.2 수행 단계
1. **근본원인 분석(RCA)** — 발견사항별 5 Why 또는 Fishbone 으로 근본 원인 식별 (SUP.1 BP6).
2. **시정 조치 수립** — 즉각 조치(임시) + 장기 조치(재발방지) 구분 작성.
3. **계획서 결재** — TMP-ASPICE-01-07-03-01 작성 → QA Manager 승인.
4. **조치 실행** — 책임자가 계획대로 실행, 진행 상황 주간 보고.
5. **마감일 모니터링** — QA Engineer 가 매주 진행률 확인.
6. **효과 검증** — 마감 후 정의된 검증 방법(재감사·증적 확인·KPI 측정)으로 효과 평가.
7. **종결 처리** — 효과 입증 시 SUP.9 문제 보고서 종결, MAT-001 갱신.
8. **에스컬레이션** — 마감 초과 또는 효과 미입증 시 7-1 절차 실행.

### 5.3 완료 조건 체크리스트
- [ ] 근본원인이 명문화됨
- [ ] 시정 조치가 즉각·장기로 구분 기재됨
- [ ] 책임자·마감일이 지정됨
- [ ] 효과 검증 방법이 사전 정의됨
- [ ] 효과 검증 결과가 객관 증거와 함께 기록됨
- [ ] SUP.9 문제 보고서 상태가 Closed 로 갱신됨
- [ ] 에스컬레이션 발생 시 통보 이력이 보존됨
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- Project Management Office: 자원·일정 조정, 에스컬레이션 1차 수신
- 피감 부서(SW/HW/Systems): 시정 조치 실행 책임
- Process Engineering: 프로세스 변경이 필요한 경우 표준 갱신
- Configuration Management: 시정 조치로 인한 베이스라인 갱신 지원

## 7. 주의사항 / 예외 처리

### 7.1 마감 초과 에스컬레이션 단계
- 1차 (마감일 +3일): 책임자 → QA Engineer 사유 보고
- 2차 (마감일 +7일): PM 통보, 자원 재할당 검토
- 3차 (마감일 +14일): QA Director / Program Director 에게 공식 에스컬레이션, Risk Register 등록

### 7.2 반복 발생 시
동일 유형의 부적합이 6개월 내 2회 이상 발생 시 단순 시정으로 종결하지 않고
프로세스 자체 개선(POL/PRO 개정)을 트리거. 개선 PRO 변경 요청을 SUP.10 으로 등록.

### 7.3 효과 미입증 시
정의된 검증 방법으로 효과가 입증되지 않으면 종결 불가. RCA 부터 재실시하고 새 시정 조치 계획서 작성.

### 7.4 에스컬레이션 시 비공식 종결 금지
경영진 개입 후에도 정식 효과 검증 없이 "구두 종결" 하지 말 것. 모든 종결은 검증 증거 기반.

## 8. 연계 템플릿 / 기록
- 양식: [[TMP-ASPICE-01-07-03-01_시정조치계획서]]
- 작성예시: [[EX-ASPICE-01-07-03-01_시정조치계획서_작성예시]]
- 선행 절차: [[WI-ASPICE-01-07-02_QA감사실시]]
- 연계 기록: SUP.9 문제 보고서, 에스컬레이션 통보 이메일

## 9. 출처
```yaml
source_citation:
  - source: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    standard: "Automotive SPICE 4.0"
    process: "SUP.1 — Quality Assurance"
    base_practices: ["BP6"]
    work_products: ["15-19 Quality assurance report", "08-19 Problem record"]
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 작성 (draft) | QA Manager |
