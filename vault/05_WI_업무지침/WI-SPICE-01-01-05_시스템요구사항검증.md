---
type: WI
doc_id: "WI-SPICE-01-01-05"
title: "시스템 요구사항 검증 (SYS.5)"
version: "0.1"
owner: "System Engineer"
reviewer: "QA Lead"
approver: "QA Lead"
scope: "SyRS 대비 시스템 검증 설계·실행·결과 보고 + 결함 이관"
parent_pro: "[[PRO-SPICE-01-01_시스템공학프로세스]]"
related_tmp:
  - "[[TMP-SPICE-01-01-05-01_시스템검증보고서]]"
related_rec: []
standards: ["Automotive SPICE 4.0"]
aspice_processes: ["SYS.5"]
entry_gate: "WI-SPICE-01-01-04.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SYS.5, VWAY_Motors, Verification, HIL, Bench]
---

# 시스템 요구사항 검증 업무지침 (WI-SPICE-01-01-05)

> 상위 절차: [[PRO-SPICE-01-01_시스템공학프로세스]] §5 단계 16~18
> ASPICE 매핑: SYS.5 (System Verification) — BP1~BP5

## 1. 업무 목적

통합된 시스템이 SyRS 의 모든 요구사항(특히 ASIL/CAL 등급) 을 충족함을 HIL/Bench/차량 검증 환경에서 입증하고, 결과를 객관적 증적으로 보고한다. 검증 단계의 **승인자(Accountable) 는 독립성 원칙에 따라 QA Lead** 이다.

## 2. 수행 주체

- **주 수행자**: System Engineer (검증 실행)
- **검토자**: SW/HW/ML Lead, Safety Engineer
- **승인자**: QA Lead (독립성 원칙 — 개발 라인 외)

## 3. 범위

WI-SPICE-01-01-04 의 통합 시험 종료(통합 보고서 승인) 후부터 SYS.5 검증 보고서 v1.0 등록 + 검증 결과의 [[PRO-SPICE-01-05]] (VAL/SPL) 인계 시점까지 적용한다.

## 4. 입력 자료 / 산출물

- **Input**
  - SyRS v1.0 (검증 대상)
  - 통합된 시스템 (HW + SW + ML)
  - SYS.4 통합 시험 결과 보고서

- **Output**
  - System Verification Specification v1.0 (검증 시나리오·합격 기준)
  - System Verification Report v1.0 (실행 결과)
  - 결함 리포트 (→ SUP.9)
  - SyRS↔Verification 추적성 매트릭스

## 5. 수행 절차

### 5.1 사전 준비

1. 검증 환경(HIL bench, 차량, 시험 트랙) 가용성과 캘리브레이션 상태를 점검한다.
2. 검증 도구의 측정 정확도·무결성을 확인하고 마지막 캘리브레이션 일자를 기록한다.
3. 검증 시나리오 ID 체계(`VER-{프로젝트코드}-{NNN}`) 를 정의한다.

### 5.2 수행 단계

1. **검증 전략 수립** (SYS.5.BP1)
   - 검증 환경 매트릭스: SyRS 별로 HIL / Bench / 차량 / 시험 트랙 중 적합 환경 결정.
   - ASIL D/CAL4 요구사항은 최소 2개 환경에서 교차 검증.

2. **검증 시나리오 설계** (SYS.5.BP2)
   - 각 SyRS 에 대해 1개 이상의 검증 케이스 정의.
   - 케이스 = 입력 + 환경 조건 + 기대 출력 + 합격 기준 + 측정 방법.
   - 결과: TMP-SPICE-01-01-05-01 §2 "검증 케이스".

3. **검증 실행** (SYS.5.BP3)
   - 환경별로 검증 케이스를 실행하고 결과를 자동/반자동으로 기록.
   - 측정값은 원본 데이터(raw) + 분석 데이터 모두 보존.
   - 차량 검증은 안전·법규(공도 사용 시 임시운행허가) 준수.
   - 결과: TMP-SPICE-01-01-05-01 §3 "실행 결과 로그".

4. **결과 분석·결함 등록** (SYS.5.BP4)
   - Pass/Fail 판정 + 통계(통과율, 결함 분류).
   - Fail 결함은 [[WI-SPICE-01-08-01_문제등록및분류]] 로 등록.
   - 임계치 미달 결함은 ASIL/CAL 등급별 폐쇄 우선순위 부여.

5. **SyRS↔Verification 추적성** (SYS.5.BP4 후속)
   - 각 SyRS 에 대해 어떤 검증 케이스가 수행되었는지 매트릭스 작성.
   - 미검증 SyRS 0건 목표 (있을 경우 사유 기록).

6. **검증 결과 보고** (SYS.5.BP5)
   - QA Lead 에게 보고서 제출 → QA 가 독립적 승인.
   - 결함 폐쇄율·잔여 리스크가 출시 게이트 기준 미달 시 [[PRO-SPICE-01-05]] 인계 보류.

### 5.3 완료 조건 체크리스트

- [ ] 검증 시나리오가 모든 SyRS 를 커버 (≥ 95%, ASIL D 는 100%)
- [ ] 검증 환경 캘리브레이션 인증서 첨부
- [ ] 측정 원본 데이터 보존 (보존기간: 프로젝트 SOP+15년)
- [ ] 모든 Fail 결함이 SUP.9 에 등록되고 추적
- [ ] ASIL D/CAL4 요구사항 교차 검증 100% 실행
- [ ] SyRS↔Verification 추적성 매트릭스 커버리지 ≥ 95%
- [ ] QA Lead 의 독립적 승인 서명 확보
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서

- **QA (SUP.1)**: 검증 결과 독립 승인 (Accountable)
- **Safety Engineering**: ASIL D 케이스 검토
- **Cybersecurity Engineering**: CAL4 케이스 검토
- **Validation/Release ([[PRO-SPICE-01-05]])**: 검증 결과 인계 수령
- **PM (MAN.3)**: 출시 게이트 의사결정

## 7. 주의사항 / 예외 처리

### 7.1 검증 환경 결함 (도구 장애)
- 검증 도구·HIL bench 의 결함이 의심되는 경우:
  - 즉시 검증 일시 중단 + 도구 캘리브레이션·자가진단 실행.
  - 의심 케이스 재실행. 환경 결함 확정 시 결과 무효 처리 + 사유 기록.

### 7.2 결함 폐쇄 vs 출시 일정 충돌
- 잔여 결함이 있으나 출시 일정이 임박한 경우:
  - ASIL D/CAL4 결함은 폐쇄 없이 출시 절대 금지.
  - QM 결함은 OEM·QA Lead·Safety Manager 합의로 Deviation 승인 가능 (조건: 후속 패치 일정 명시).
  - 모든 Deviation 은 [[PRO-SPICE-01-08]] CCB 결재 + 공식 문서화.

### 7.3 차량 검증 사고 발생
- 시험 트랙·공도 검증 중 사고 발생 시:
  - 즉시 검증 중단 + 사고 보고 (사내 + 보험 + 관할 기관).
  - 사고 원인 RCA 후 재개 승인 (PM + 안전 책임자).
  - 사고가 시스템 결함 원인일 경우 즉시 SUP.9 등록.

### 7.4 검증 결과 데이터 무결성
- 측정 데이터 변조·삭제 의심 시:
  - 즉시 QA Lead + Project Manager 통보.
  - 원본 데이터 백업본(별도 저장소) 으로 비교 검증.
  - 무결성 위반 확인 시 검증 재실행 + 책임자 조사.

## 8. 연계 템플릿 / 기록

- 템플릿: [[TMP-SPICE-01-01-05-01_시스템검증보고서]]
- 작성예시: [[EX-SPICE-01-01-05-01_시스템검증보고서_작성예시]]
- 기록 폴더: `vault/08_REC_기록/SYS.5/`

## 9. 출처 (source_citation)

```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SYS.5-PURPOSE-001 / VWAY-SYS.5-BP1~BP5"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력

| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SYS.5 BP1~BP5 + QA 독립 승인 | (대기) |
