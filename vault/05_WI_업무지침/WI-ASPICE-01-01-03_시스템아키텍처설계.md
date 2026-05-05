---
type: WI
doc_id: "WI-ASPICE-01-01-03"
title: "시스템 아키텍처 설계 (SYS.3)"
version: "0.1"
owner: "System Engineer"
reviewer: "SW·HW·ML Lead / Safety Engineer / Cybersecurity Engineer"
approver: "System Engineering Lead"
scope: "SyRS → 시스템 아키텍처·인터페이스(ICD)·동적 행위·SW/HW/ML 분배"
parent_pro: "[[PRO-ASPICE-01-01_시스템공학프로세스]]"
related_tmp:
  - "[[TMP-ASPICE-01-01-03-01_시스템아키텍처기술서]]"
related_rec: []
standards: ["Automotive SPICE 4.0", "AUTOSAR", "ISO 11898", "IEEE 802.3"]
aspice_processes: ["SYS.3"]
entry_gate: "WI-ASPICE-01-01-02.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SYS.3, VWAY_Motors, Architecture, ICD, Allocation]
---

# 시스템 아키텍처 설계 업무지침 (WI-ASPICE-01-01-03)

> 상위 절차: [[PRO-ASPICE-01-01_시스템공학프로세스]] §5 단계 8~12
> ASPICE 매핑: SYS.3 (System Architectural Design) — BP1~BP6

## 1. 업무 목적

SyRS 베이스라인을 바탕으로 시스템의 **요소 구조·인터페이스·동적 행위** 를 정의하고, 각 시스템 요구사항을 SW/HW/ML 도메인 컴포넌트로 분배하여 후속 SWE/HWE/MLE 프로세스에 명확한 입력을 제공한다.

## 2. 수행 주체

- **주 수행자**: System Engineer (아키텍트)
- **공동 수행자**: SW Lead, HW Lead, ML Lead (분배 합의)
- **검토자**: Safety Engineer (안전 아키텍처), Cybersecurity Engineer (보안 아키텍처), QA
- **승인자**: System Engineering Lead

## 3. 범위

WI-ASPICE-01-01-02 의 SyRS v1.0 베이스라인 등록 후부터 System Architecture Description (SAD) v1.0 베이스라인 등록까지 적용한다.

## 4. 입력 자료 / 산출물

- **Input**
  - SyRS v1.0
  - StRS v1.0 (참고)
  - HARA/TARA 결과
  - 이전 동급 ECU 의 아키텍처 (벤치마킹용)

- **Output**
  - System Architecture Description (SAD) v1.0
  - Interface Control Document (ICD) v1.0
  - 동적 행위 명세 (시퀀스 다이어그램·상태 머신·타이밍)
  - SW/HW/ML 분배 매트릭스 (Allocation Matrix)
  - SyRS↔Architecture 추적성 매트릭스

## 5. 수행 절차

### 5.1 사전 준비

1. SAD 작성 도구(Enterprise Architect, Capella, Cameo Systems Modeler) 의 모델 저장소를 준비한다.
2. ICD 표기 규칙(CAN DBC / ARXML / SOME-IP) 을 확정한다.
3. 아키텍처 ID 체계(`ARCH-{프로젝트코드}-{NNN}`) 를 정의한다.

### 5.2 수행 단계

1. **아키텍처 정의** (SYS.3.BP1)
   - 시스템을 SW Component, HW Component, ML Component, External Interface 로 계층 분해.
   - 각 요소에 책임(Responsibility) 명시.
   - 결과: TMP-ASPICE-01-01-03-01 §2 "요소 분해 구조" 작성.

2. **인터페이스 명세 (ICD)** (SYS.3.BP2)
   - 각 요소 간 인터페이스를 다음 항목으로 명세:
     - 신호명·데이터 타입·범위·단위
     - 통신 채널 (CAN/CAN-FD/Ethernet/SOME-IP/LIN)
     - 송수신 주기·타임아웃
     - 안전성·보안성 요구사항 (서명/암호화 여부)
   - 외부 인터페이스(OEM 차량 버스) 는 OEM ICD 와 정합성 검증.

3. **동적 행위 분석** (SYS.3.BP3)
   - 주요 시나리오에 대한 시퀀스 다이어그램 작성.
   - Safety-critical 요소는 상태 머신 + 타이밍 분석 강제.
   - WCET (Worst-Case Execution Time) 분석은 SW Lead 와 합동.

4. **SW/HW/ML 요소 분배** (SYS.3.BP4)
   - SyRS 의 각 요구사항을 SW/HW/ML/Cross 카테고리로 분배.
   - 분배 시 ASIL/CAL 등급 상속 규칙 적용 (예: ASIL D SyRS → 분배된 SW Component 도 ASIL D).
   - 합동 회의로 SW·HW·ML Lead 의 동의를 확보.
   - 결과: TMP-ASPICE-01-01-03-01 §4 "분배 매트릭스".

5. **자원·실현가능성 재검토** (SYS.3.BP4 후속)
   - 분배 결과로 각 도메인의 자원 부담을 재계산.
   - 과부하 감지 시 아키텍처 재설계 또는 SyRS 변경 협의.

6. **SyRS↔Architecture 추적성** (SYS.3.BP5)
   - 각 요소·인터페이스가 어떤 SyRS 를 만족하는지 양방향 link 등록.
   - 모든 SyRS 가 1개 이상의 아키텍처 요소에 매핑되었는지 확인.

7. **변경 영향 분석** (SYS.3.BP6)
   - SyRS 변경 시 영향 받는 아키텍처 요소·ICD 자동 식별 도구 설정.

8. **아키텍처 검토 게이트** (→ SUP.1)
   - QA + Safety + Security 합동 검토.
   - 코멘트 종결 후 SAD/ICD v1.0 베이스라인 등록.

### 5.3 완료 조건 체크리스트

- [ ] SAD 의 모든 요소에 책임 명시 완료
- [ ] ICD 의 모든 인터페이스에 데이터 타입·범위·단위·주기 명시
- [ ] 외부 인터페이스가 OEM ICD 와 정합성 검증 완료
- [ ] Safety-critical 요소에 상태 머신 + 타이밍 분석 첨부
- [ ] SyRS↔Architecture 추적성 커버리지 ≥ 95%
- [ ] 분배 매트릭스에 ASIL/CAL 상속 명시
- [ ] SW·HW·ML Lead 의 분배 합의 회의록 첨부
- [ ] QA + Safety + Security 합동 검토 코멘트 종결
- [ ] SAD v1.0 / ICD v1.0 베이스라인 등록 + MAT-001 갱신

## 6. 인터페이스 부서

- **SW/HW/ML Lead**: 분배 합의·실현 가능성 검토
- **Safety Engineering**: 안전 아키텍처 검토 (분리·중복화)
- **Cybersecurity Engineering**: 신뢰 경계·암호화 영역 검토
- **CM (SUP.8)**: SAD/ICD 베이스라인
- **QA (SUP.1)**: 아키텍처 검토 게이트

## 7. 주의사항 / 예외 처리

### 7.1 OEM ICD 와 충돌
- 내부 ICD 와 OEM 제공 ICD 가 충돌하는 경우:
  - OEM ICD 우선 원칙 적용.
  - 내부 ICD 변경 또는 OEM 측 변경 협상 결과는 회의록 증적화.
  - StRS/SyRS 영향 시 SUP.10 변경 절차 회귀.

### 7.2 분배 합의 실패
- SW·HW·ML Lead 간 분배 합의가 이루어지지 않을 때:
  - System Engineering Lead 중재 → 결정 권한자 지정.
  - 결정 사유(성능·비용·일정·역량) 를 회의록에 명시.
  - 결정에 대한 이의는 7 영업일 이내 정식 이슈 등록 — 그 후 변경 절차 적용.

### 7.3 자원 과부하 (CPU/Memory/전력)
- 분배 후 도메인별 자원 부담이 한계 초과한 경우:
  - 1순위: 아키텍처 재설계 (다른 컴포넌트로 책임 이전).
  - 2순위: HW 사양 상향 협상 (OEM 또는 내부).
  - 3순위: SyRS 우선순위 조정 → SUP.10 변경 절차.
  - 미해결 시 Project Manager 에스컬레이션.

### 7.4 ICD 버전 충돌 (다중 ECU 환경)
- 다른 ECU 와 공유 버스(CAN/Ethernet) 의 ICD 버전이 충돌할 때:
  - OEM 의 통합 ICD 를 단일 출처로 한다.
  - 내부 ICD 는 통합 ICD 의 subset 이어야 한다.
  - 통합 ICD 갱신 시 본 ICD 동기화는 5 영업일 이내.

## 8. 연계 템플릿 / 기록

- 템플릿: [[TMP-ASPICE-01-01-03-01_시스템아키텍처기술서]]
- 작성예시: [[EX-ASPICE-01-01-03-01_시스템아키텍처기술서_작성예시]]
- 기록 폴더: `vault/08_REC_기록/SYS.3/`

## 9. 출처 (source_citation)

```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SYS.3-PURPOSE-001 / VWAY-SYS.3-BP1~BP6"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력

| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SYS.3 BP1~BP6 + 분배 합의 절차 | (대기) |
