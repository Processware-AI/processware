---
type: WI
doc_id: "WI-SPICE-01-02-06"
title: "SW 검증 (SWE.6)"
version: "0.1"
owner: "SW Engineer"
reviewer: "QA Lead"
approver: "QA Lead"
scope: "SwRS 대비 통합 SW 검증 + Pass/Fail 보고 + SYS.4 인계"
parent_pro: "[[PRO-SPICE-01-02_소프트웨어공학프로세스]]"
related_tmp:
  - "[[TMP-SPICE-01-02-06-01_SW검증보고서]]"
related_rec: []
standards: ["Automotive SPICE 4.0"]
aspice_processes: ["SWE.6"]
entry_gate: "WI-SPICE-01-02-05.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SWE.6, Verification]
---

# SW 검증 업무지침 (WI-SPICE-01-02-06)

> 상위 절차: [[PRO-SPICE-01-02_소프트웨어공학프로세스]] §5 단계 11~12
> ASPICE 매핑: SWE.6 (Software Verification) — BP1~BP4

## 1. 업무 목적

통합된 SW 가 SwRS 의 모든 요구사항(특히 ASIL 등급) 을 충족함을 SW 단위 검증 환경(SIL/PIL/HIL 의 SW 부분) 에서 입증한다. **승인자(Accountable) 는 독립성 원칙에 따라 QA Lead** 이다.

## 2. 수행 주체
- **주 수행자**: SW Engineer
- **검토자**: SW Architect
- **승인자**: QA Lead (독립성 원칙)

## 3. 범위
WI-SPICE-01-02-05 의 통합 빌드 + 보고서 등록 후부터 SW 검증 보고서 v1.0 등록 + SYS.4 (시스템 통합) 인계 시점까지 적용한다.

## 4. 입력 자료 / 산출물
- **Input**: SwRS v1.0, Integrated SW Build, Integration Test Report
- **Output**: SW Verification Specification, SW Verification Report, SwRS↔Verification 추적성

## 5. 수행 절차

### 5.1 사전 준비
1. SIL/PIL 환경 구성 + 측정 도구 캘리브레이션.
2. SwRS↔Verification 매트릭스 템플릿 준비.

### 5.2 수행 단계
1. **검증 시나리오 설계** (SWE.6.BP1)
   - 각 SwRS 에 1개 이상의 검증 케이스.
   - 정상·경계·예외 시나리오 + ASIL 등급별 강건성.

2. **검증 실행** (SWE.6.BP2/3)
   - SIL/PIL 환경에서 자동 실행.
   - 측정 데이터 raw + 분석 보존.

3. **결과 분석·결함 등록** (SWE.6.BP4)
   - Fail 결함 → SUP.9 등록.
   - 통과율·잔여 리스크 보고서 작성.

4. **SwRS↔Verification 추적성**
   - 매트릭스 작성 + 미검증 SwRS 0건 확인.

5. **QA Lead 독립 승인**
   - 보고서 제출 + QA 의 독립적 검토 + 승인.

### 5.3 완료 조건 체크리스트
- [ ] 모든 SwRS 에 검증 케이스 매핑 (≥ 95%, ASIL D 100%)
- [ ] 측정 환경 캘리브레이션 인증서 첨부
- [ ] 모든 Fail 결함 SUP.9 등록 + 추적
- [ ] 측정 raw 데이터 보존 (보존기간 SOP+15년)
- [ ] QA Lead 독립 승인 서명 확보
- [ ] SyRS↔Verification 추적성 ≥ 95%
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **QA (SUP.1)**: 독립 승인
- **System Engineering ([[PRO-SPICE-01-01]])**: SYS.4 시스템 통합 인계
- **CM (SUP.8)**: 검증 빌드 형상관리

## 7. 주의사항 / 예외 처리

### 7.1 결함 폐쇄 vs 일정
- 잔여 결함 + 일정 충돌:
  - ASIL C/D 결함은 폐쇄 없이 인계 금지.
  - QM 결함은 QA Lead + Safety Manager 합의로 Deviation.

### 7.2 환경 결함 (도구)
- 측정 도구 결함 의심:
  - 즉시 캘리브레이션 + 자가진단.
  - 영향 케이스 무효 처리 + 재실행.

### 7.3 데이터 무결성
- raw 데이터 변조 의심:
  - 별도 저장소 백업과 비교.
  - 위반 확인 시 검증 재실행 + 책임자 조사.

### 7.4 회귀 결함 (이전 버전 통과 케이스 실패)
- 이전 빌드에서 Pass 한 케이스가 현 빌드에서 Fail:
  - 즉시 SUP.9 등록 + Critical 분류.
  - 변경 영향 분석 + 책임 모듈 회귀.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-SPICE-01-02-06-01_SW검증보고서]]
- 작성예시: [[EX-SPICE-01-02-06-01_SW검증보고서_작성예시]]
- 기록 폴더: `vault/08_REC_기록/SWE.6/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SWE.6-PURPOSE-001 / VWAY-SWE.6-BP1~BP4"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SWE.6 BP1~BP4 + QA 독립 승인 | (대기) |
