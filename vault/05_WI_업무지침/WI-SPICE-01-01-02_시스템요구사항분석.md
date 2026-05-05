---
type: WI
doc_id: "WI-SPICE-01-01-02"
title: "시스템 요구사항 분석 (SYS.2)"
version: "0.1"
owner: "System Engineer"
reviewer: "Safety Engineer / Cybersecurity Engineer / SW·HW·ML Lead"
approver: "System Engineering Lead"
scope: "StRS → SyRS 정제, ASIL/CAL 분류, 일관성 분석, StRS↔SyRS 추적성"
parent_pro: "[[PRO-SPICE-01-01_시스템공학프로세스]]"
related_tmp:
  - "[[TMP-SPICE-01-01-02-01_시스템요구사항명세서]]"
related_rec: []
standards: ["Automotive SPICE 4.0", "ISO 26262", "ISO/SAE 21434"]
aspice_processes: ["SYS.2"]
entry_gate: "WI-SPICE-01-01-01.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SYS.2, VWAY_Motors, ASIL, CAL]
---

# 시스템 요구사항 분석 업무지침 (WI-SPICE-01-01-02)

> 상위 절차: [[PRO-SPICE-01-01_시스템공학프로세스]] §5 단계 4~7
> ASPICE 매핑: SYS.2 (System Requirements Analysis) — BP1~BP6

## 1. 업무 목적

베이스라인된 이해관계자 요구사항(StRS) 을 시스템 관점의 기능·비기능 요구사항(SyRS) 으로 정제·분해하고, ISO 26262 ASIL 및 ISO/SAE 21434 CAL 등급을 부여하며, 일관성·완전성·시험가능성을 분석한 뒤 StRS↔SyRS 양방향 추적성을 확립한다.

## 2. 수행 주체

- **주 수행자**: System Engineer
- **검토자**: Safety Engineer (ASIL), Cybersecurity Engineer (CAL), SW/HW/ML Lead (구현 가능성), QA (검토)
- **승인자**: System Engineering Lead

## 3. 범위

WI-SPICE-01-01-01 에서 베이스라인된 StRS 가 입력으로 도착한 시점부터 SyRS v1.0 베이스라인 등록 시점까지 적용한다.

## 4. 입력 자료 / 산출물

- **Input**
  - StRS v1.0 (베이스라인) — WI-01-01 산출물
  - 적용 표준 (ISO 26262, ISO 21434, AUTOSAR 등)
  - HARA(Hazard Analysis and Risk Assessment) 결과 — Safety 팀에서 제공
  - TARA(Threat Analysis and Risk Assessment) 결과 — Cybersecurity 팀에서 제공

- **Output**
  - System Requirements Specification (SyRS) v1.0
  - ASIL/CAL 분배표
  - 일관성·영향 분석 보고서
  - StRS↔SyRS 추적성 매트릭스

## 5. 수행 절차

### 5.1 사전 준비

1. StRS v1.0 의 변경 freeze 여부를 CM 시스템에서 확인한다.
2. HARA·TARA 결과 수령 여부 확인. 미수령 시 Safety/Security 팀에 즉시 요청.
3. SyRS 의 ID 체계(`SYS-{프로젝트코드}-{NNN}`) 와 속성 컬럼(우선순위, ASIL, CAL, 시험가능성) 을 확정한다.

### 5.2 수행 단계

1. **시스템 요구사항 정제** (SYS.2.BP1)
   - StRS 의 각 항목을 분석하여 시스템 관점에서 1개 이상의 SyRS 로 분해한다.
   - 1:N 관계 가능 — 추적성 매트릭스에 모두 기록.
   - 기능 요구사항: 동작·입출력·트리거 조건을 명시.
   - 비기능 요구사항: 정량 수치(예: "시동 후 200ms 이내 CAN 메시지 송신") 로 표현.
   - 결과: TMP-SPICE-01-01-02-01 §2 작성.

2. **ASIL/CAL/속성 부여** (SYS.2.BP2)
   - HARA 결과를 참조하여 각 SyRS 에 ASIL(QM/A/B/C/D) 부여.
   - TARA 결과를 참조하여 각 SyRS 에 CAL(CAL1~CAL4) 부여.
   - ASIL D / CAL4 인 요구사항은 Safety/Security 분리 검토 강제.
   - 결과: TMP-SPICE-01-01-02-01 §3 ASIL/CAL 분배표.

3. **영향·일관성 분석** (SYS.2.BP3)
   - 모순 검출: 동일 동작에 대해 상이한 시점/조건이 명시된 경우 즉시 이슈 등록.
   - 중복 검출: 의미가 동일한 2개 이상 SyRS 발견 시 통합 또는 분리 사유 명시.
   - 시험가능성 검토: 각 SyRS 가 측정 가능한 검증 기준을 가지는지 확인.
   - 결과: 분석 보고서 작성, 미해결 이슈는 [[PRO-SPICE-01-08_문제및변경관리프로세스]] SUP.9 로 등록.

4. **자원·기술적 실현 가능성 분석** (SYS.2.BP4)
   - SW/HW/ML Lead 와 합동 검토 — 구현 가능성·자원(메모리·CPU·전력) 검토.
   - 실현 불가 항목은 OEM 협의 후 StRS 변경 절차(SUP.10) 로 회귀.

5. **StRS↔SyRS 추적성 확립** (SYS.2.BP5)
   - 각 SyRS 가 어떤 StRS 에서 파생되었는지 양방향 link 등록.
   - StRS 중 SyRS 로 분해되지 않은 항목 발견 시 누락 사유 분석.
   - 결과: 추적성 매트릭스 (TMP-SPICE-01-01-02-01 §5).

6. **변경 영향 분석 자동화** (SYS.2.BP6)
   - StRS 변경 시 영향 받는 SyRS 자동 식별 도구(PLM/DOORS) 설정.
   - 영향 분석 결과 5 영업일 이내 회신을 SLA 로 한다.

7. **SyRS 검토 게이트** (→ SUP.1)
   - QA 가 SyRS 의 일관성·완전성·시험가능성·추적성 검토.
   - 코멘트 종결 후 SyRS v1.0 베이스라인 등록.

### 5.3 완료 조건 체크리스트

- [ ] StRS 의 모든 항목이 1개 이상 SyRS 로 분해되었거나 누락 사유 기록 완료
- [ ] 모든 SyRS 에 ASIL·CAL 부여 완료 (해당 없을 때 명시적으로 "QM" / "CAL1" 표기)
- [ ] ASIL D / CAL4 항목에 대한 Safety/Security 분리 검토 완료
- [ ] 모순·중복 0건 (또는 이슈 등록 완료)
- [ ] 모든 SyRS 의 검증 기준이 측정 가능한 형태로 기술됨
- [ ] StRS↔SyRS 양방향 추적성 매트릭스 커버리지 ≥ 95%
- [ ] QA 검토 코멘트 종결
- [ ] SyRS v1.0 베이스라인 등록 + MAT-001 갱신

## 6. 인터페이스 부서

- **Safety Engineering**: HARA 결과 제공, ASIL 분배 검토
- **Cybersecurity Engineering**: TARA 결과 제공, CAL 분배 검토
- **SW/HW/ML Lead**: 실현 가능성 검토
- **CM (SUP.8)**: SyRS 베이스라인 등록
- **QA (SUP.1)**: SyRS 품질 게이트

## 7. 주의사항 / 예외 처리

### 7.1 HARA/TARA 결과 미수령 시
- HARA·TARA 가 분석 시점에 미완료된 경우:
  - 임시로 보수적 등급(ASIL D / CAL4) 부여 후 `pending_safety_review` 태그.
  - HARA/TARA 완료 시 정식 등급으로 재분배.
  - 재분배 결과는 SyRS 의 v1.x 또는 v2.0 으로 개정 처리.

### 7.2 ASIL 분배 충돌
- 동일 SyRS 에 대해 Safety 팀과 System Engineer 의 ASIL 의견이 다를 때:
  - **보수적 원칙**: 두 의견 중 더 높은 등급을 채택.
  - 결정 사유는 회의록·이메일로 증적화.
  - 분쟁이 지속되면 Project Manager + CTO 에 에스컬레이션.

### 7.3 시험 불가능 요구사항 발견
- 측정 기준을 정량화할 수 없는 SyRS(예: "직관적인 UI") 발견 시:
  - StRS 단계로 회귀 → OEM 와 측정 기준 합의.
  - 합의 불가 시 본 SyRS 를 `informational` 로 강등하고 검증 대상에서 제외.
  - 강등 결정은 System Engineering Lead 가 승인.

### 7.4 추적성 누락
- StRS 항목이 SyRS 로 분해되지 않은 채 발견 시:
  - 의도적 누락(범위 외) 인지 실수 누락인지 분류.
  - 의도적이면 StRS 항목에 `out_of_scope` 태그 + 사유 기록.
  - 실수면 즉시 SyRS 보완 작성 + 추적성 매트릭스 갱신.

## 8. 연계 템플릿 / 기록

- 템플릿: [[TMP-SPICE-01-01-02-01_시스템요구사항명세서]]
- 작성예시: [[EX-SPICE-01-01-02-01_시스템요구사항명세서_작성예시]]
- 기록 폴더: `vault/08_REC_기록/SYS.2/`

## 9. 출처 (source_citation)

```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SYS.2-PURPOSE-001 / VWAY-SYS.2-BP1~BP6"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력

| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SYS.2 BP1~BP6 + ASIL/CAL 분배 통합 | (대기) |
