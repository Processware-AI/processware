---
type: WI
doc_id: "WI-SPICE-01-02-01"
title: "SW 요구사항 분석 (SWE.1)"
version: "0.1"
owner: "SW Engineer"
reviewer: "SW Architect / Safety Engineer"
approver: "SW Lead"
scope: "SyRS·SAD → SW Requirements Specification (SwRS) 도출·분류·추적성"
parent_pro: "[[PRO-SPICE-01-02_소프트웨어공학프로세스]]"
related_tmp:
  - "[[TMP-SPICE-01-02-01-01_SW요구사항명세서]]"
related_rec: []
standards: ["Automotive SPICE 4.0", "ISO 26262", "AUTOSAR"]
aspice_processes: ["SWE.1"]
entry_gate: null
scope_type: "project"
domain: SPICE
scope_code: SPICE
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SWE.1, VWAY_Motors, SwRS]
---

# SW 요구사항 분석 업무지침 (WI-SPICE-01-02-01)

> 상위 절차: [[PRO-SPICE-01-02_소프트웨어공학프로세스]] §5 단계 1~3
> ASPICE 매핑: SWE.1 (Software Requirements Analysis) — BP1~BP6

## 1. 업무 목적

SYS.3 에서 SW 도메인으로 분배된 시스템 요구사항(SyRS) 과 시스템 아키텍처(SAD/ICD) 를 입력으로, **SW 요구사항(SwRS)** 을 도출·분류·문서화하고 SyRS↔SwRS 양방향 추적성을 확립한다.

## 2. 수행 주체

- **주 수행자**: SW Engineer
- **검토자**: SW Architect, Safety Engineer (ASIL 상속), QA
- **승인자**: SW Lead

## 3. 범위

PRO-SPICE-01-01 에서 SAD/ICD v1.0 베이스라인 + SW 분배 매트릭스 인계 시점부터 SwRS v1.0 베이스라인 등록 시점까지 적용한다.

## 4. 입력 자료 / 산출물

- **Input**
  - SyRS v1.0 (SW 분배분)
  - SAD/ICD v1.0
  - 분배 매트릭스 (SW 컴포넌트 식별)
  - AUTOSAR 컴포넌트 표준 (Classic / Adaptive 식별)

- **Output**
  - SW Requirements Specification (SwRS) v1.0
  - SyRS↔SwRS 추적성 매트릭스
  - SwRS 검토 보고서

## 5. 수행 절차

### 5.1 사전 준비

1. SyRS 의 SW 분배분만 추출하여 작업 범위 확정.
2. AUTOSAR Classic / Adaptive 환경 구분 확정 (Classic = ECU 임베디드, Adaptive = HPC).
3. SwRS ID 체계(`SWR-{프로젝트코드}-{NNN}`) 확정.

### 5.2 수행 단계

1. **SW 요구사항 도출** (SWE.1.BP1)
   - 분배된 SyRS 를 SW 관점에서 1개 이상의 SwRS 로 분해.
   - 기능 요구사항: SW 컴포넌트의 입출력·알고리즘·제약 조건.
   - 비기능 요구사항: 응답시간(ms), 메모리 사용량, 코드 커버리지 목표 등.
   - 인터페이스: AUTOSAR Port Interface, SOME-IP Service.

2. **분류·속성 부여** (SWE.1.BP2)
   - ASIL 상속: SyRS 의 ASIL 등급을 SwRS 에 그대로 상속(분리 가능 시 분리 분배 절차 적용).
   - 시험가능성: 각 SwRS 가 단위 시험·통합 시험에서 검증 가능한지 평가.

3. **일관성 분석** (SWE.1.BP3)
   - 모순·중복·미명세 항목 검출.
   - SwRS 간 충돌 시 SW Architect 와 협의.

4. **자원 분석** (SWE.1.BP4)
   - 예상 메모리·CPU·통신 대역폭을 분석하여 HW 사양 만족 여부 판단.
   - 초과 시 [[PRO-SPICE-01-08_문제및변경관리프로세스]] 변경 절차 회귀.

5. **SyRS↔SwRS 추적성** (SWE.1.BP5)
   - 양방향 link 등록.
   - SyRS 중 SwRS 로 분해되지 않은 항목 발견 시 사유 기록.

6. **변경 영향 분석** (SWE.1.BP6)
   - SyRS 변경 시 영향 받는 SwRS 자동 식별 도구 설정.

7. **SwRS 검토 게이트** (→ SUP.1)
   - QA + SW Architect 검토 → 코멘트 종결 → SwRS v1.0 베이스라인.

### 5.3 완료 조건 체크리스트

- [ ] SW 분배 SyRS 가 모두 SwRS 로 분해 (또는 사유 기록)
- [ ] 모든 SwRS 에 ASIL 등급 명시 (QM 포함)
- [ ] 모든 SwRS 의 시험가능성 검증 기준 명시
- [ ] 자원 분석 결과 HW 사양 만족 확인
- [ ] SyRS↔SwRS 양방향 추적성 ≥ 95%
- [ ] QA + Architect 검토 코멘트 종결
- [ ] SwRS v1.0 베이스라인 + MAT-001 갱신

## 6. 인터페이스 부서

- **System Engineering ([[PRO-SPICE-01-01_시스템공학프로세스]])**: SyRS 변경 협의
- **HW/ML Lead**: 자원·인터페이스 합의
- **Safety Engineering**: ASIL 상속 검토
- **CM (SUP.8)**: SwRS 베이스라인
- **QA (SUP.1)**: SwRS 검토

## 7. 주의사항 / 예외 처리

### 7.1 ASIL 상속 분리 (Decomposition)
- 단일 ASIL D SyRS 를 ASIL B + ASIL B 등 분리 분배할 때:
  - ISO 26262-9 Clause 5 의 ASIL Decomposition 규칙 엄격 적용.
  - Safety Engineer 의 분리 정합성 검토 + 결재 필수.
  - 결정 사유와 분리 후 의존성을 SwRS 에 명시.

### 7.2 자원 부족 (메모리/CPU)
- 자원 분석 결과 HW 한계 초과 시:
  - 1순위: 알고리즘 최적화 (메모리/CPU 절감).
  - 2순위: SW 아키텍처 재설계 (별도 컴포넌트 분리).
  - 3순위: HW 사양 상향 협상 → SyRS 변경 회귀.

### 7.3 AUTOSAR 호환성 위반
- 도출한 SwRS 가 AUTOSAR Standard Port Interface 와 호환 불가 시:
  - 1) Custom Port 로 정의 + 사유 기록 (호환성 영향 분석 첨부).
  - 2) SyRS 변경 협의 → 표준 Port 로 매핑.
  - Custom Port 사용은 SW Architect 결재 필수.

### 7.4 시험 불가능 SwRS
- 정량 측정 불가능한 SwRS 발견 시:
  - SyRS 단계로 회귀 → 측정 기준 합의.
  - 합의 불가 시 `informational` 강등 (SW Lead 승인).

## 8. 연계 템플릿 / 기록

- 템플릿: [[TMP-SPICE-01-02-01-01_SW요구사항명세서]]
- 작성예시: [[EX-SPICE-01-02-01-01_SW요구사항명세서_작성예시]]
- 기록 폴더: `vault/08_REC_기록/SWE.1/`

## 9. 출처 (source_citation)

```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SWE.1-PURPOSE-001 / VWAY-SWE.1-BP1~BP6"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력

| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SWE.1 BP1~BP6 + ASIL Decomposition | (대기) |
