---
type: WI
doc_id: "WI-ASPICE-01-01-01"
title: "이해관계자 요구사항 도출 (SYS.1)"
version: "0.1"
owner: "System Engineer"
reviewer: "System Engineering Lead"
approver: "Project Manager"
scope: "OEM RFQ 수령부터 이해관계자 요구사항 베이스라인 등록까지"
parent_pro: "[[PRO-ASPICE-01-01_시스템공학프로세스]]"
related_tmp:
  - "[[TMP-ASPICE-01-01-01-01_이해관계자요구사항명세서]]"
related_rec: []
standards: ["Automotive SPICE 4.0"]
aspice_processes: ["SYS.1"]
entry_gate: null
scope_type: "project"
domain: ASPICE
scope_code: ASPICE
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SYS.1, VWAY_Motors, 요구사항도출]
---

# 이해관계자 요구사항 도출 업무지침 (WI-ASPICE-01-01-01)

> 상위 절차: [[PRO-ASPICE-01-01_시스템공학프로세스]] §5 단계 1~3
> ASPICE 매핑: SYS.1 (Stakeholder Requirements Analysis) — BP1~BP6

## 1. 업무 목적

OEM(고객) 으로부터 수령한 RFQ·사양서를 출발점으로 모든 이해관계자(고객·내부·규제기관·공급사·인증기관)의 요구사항을 빠짐없이 도출·문서화하고, 합의된 베이스라인(Stakeholder Requirements Specification, StRS) 으로 등록하여 후속 SYS.2 단계의 신뢰할 수 있는 입력을 제공한다.

## 2. 수행 주체

- **주 수행자**: System Engineer (요구사항 도출·문서화 책임)
- **검토자**: System Engineering Lead, Safety Engineer (안전 관련), Cybersecurity Engineer
- **승인자**: Project Manager (베이스라인 승인) + OEM 고객 (외부 합의)

## 3. 범위

VWAY Motors 가 OEM 으로 인도하는 차량 ECU·도메인 컨트롤러·ADAS 시스템의 신규 개발 및 중대 변경 프로젝트에 적용한다. RFQ 수령일부터 StRS v1.0 베이스라인 등록일까지의 활동을 포함한다. 단순 BOM 변경·라벨 변경 등 시스템 아키텍처에 영향이 없는 경미 변경은 본 지침을 적용하지 않고 [[PRO-ASPICE-01-08_문제및변경관리프로세스]] 의 SUP.10 만 적용한다.

## 4. 입력 자료 / 산출물

- **Input**
  - OEM RFQ (Request for Quotation) 및 첨부 사양서
  - OEM 차량 사양서 (Vehicle Specification)
  - 적용 표준 목록 (ISO 26262, ISO 21434, UN R155/R156, AUTOSAR, ISO 11898 CAN, IEEE 802.3 Ethernet 등)
  - 조직도 / 이해관계자 컨택 포인트
  - 기존 동급 ECU 의 StRS (있을 경우 — 학습 베이스로 활용)

- **Output**
  - 이해관계자 식별 대장 (TMP-ASPICE-01-01-01-01 §1 부분)
  - Stakeholder Requirements Specification (StRS) v1.0 (TMP-ASPICE-01-01-01-01 §2~5)
  - 의사소통 채널 합의서 (회의 주기·보고 채널)
  - StRS 베이스라인 등록 기록 ([[PRO-ASPICE-01-07_품질보증및형상관리프로세스]] CM 등록)

## 5. 수행 절차

### 5.1 사전 준비

1. RFQ 원본·첨부물을 `inputs/05_프로젝트/{프로젝트코드}/RFQ/` 에 형상관리하고 SHA-256 해시를 기록한다.
2. 적용 표준 목록을 작성하고 각 표준의 최신판(개정 일자) 을 확인한다. 표준 변경 발견 시 즉시 Project Manager 에게 보고한다.
3. 프로젝트 코드(예: `VW-ADAS-2026-001`) 와 ECU 식별자, 차량 플랫폼 코드를 확정한다.
4. OEM 측 SPOC(Single Point of Contact) 와 이메일·정기 회의 주기를 합의한다.

### 5.2 수행 단계

1. **이해관계자 식별** (SYS.1.BP1)
   - 외부: OEM(System·Validation·Purchasing 부서), Tier-1 공급사, 인증기관(KATRI, TÜV), 규제기관(국토부)
   - 내부: System·SW·HW·ML Lead, QA, CM, Safety, Cybersecurity, Project Manager, Production
   - 각 이해관계자별로 의사소통 채널·주기·보고 책임자를 명시한다.
   - 결과: TMP-ASPICE-01-01-01-01 §1 "이해관계자 대장" 작성.

2. **요구사항 도출 워크숍·인터뷰 실시** (SYS.1.BP2)
   - OEM 과 최소 1회 Kick-off 워크숍 + 도메인별 2회 이상 인터뷰 실시.
   - 워크숍 의사록은 24시간 이내 공유하고 OEM 확인을 받는다.
   - 도출 기법: 문서 분석(RFQ·표준), 인터뷰, 시나리오 분석, 유사 ECU 벤치마킹.

3. **요구사항 분류·문서화** (SYS.1.BP3)
   - 요구사항을 다음 카테고리로 분류한다:
     - **기능 요구사항** (Functional): 시스템이 무엇을 해야 하는가
     - **비기능 요구사항** (Non-functional): 성능·신뢰성·내구성·EMC·환경 등
     - **인터페이스 요구사항**: CAN/Ethernet/SOME-IP/LIN 등 외부 I/F
     - **법규·인증 요구사항**: UN R155/R156, KMVSS 등
     - **운영·유지보수 요구사항**: 진단(UDS), DTC, OTA 등
   - 각 요구사항에 고유 ID(`STK-{프로젝트코드}-{NNN}`) 를 부여한다.
   - 결과: TMP-ASPICE-01-01-01-01 §2~4 작성.

4. **요구사항 우선순위 부여** (SYS.1.BP4)
   - MoSCoW(Must/Should/Could/Won't) 기준으로 우선순위 분류.
   - Safety/Security 관련 요구사항은 자동으로 Must 로 분류한다.

5. **변경 합의 및 베이스라인** (SYS.1.BP5)
   - StRS draft 를 OEM 에 송부하여 검토 받는다(검토 기간 표준 10 영업일).
   - 회신된 코멘트를 [[TMP-ASPICE-01-01-01-01]] §5 "변경 이력" 에 기록·반영한다.
   - 모든 요구사항에 대해 OEM 의 서면 합의(이메일 또는 결재 시스템) 를 확보한다.
   - StRS v1.0 으로 확정 후 CM 시스템(Git/PLM) 에 베이스라인 등록한다.

6. **이해관계자 평가·관리** (SYS.1.BP6)
   - 정기(월 1회) 이해관계자 영향력·관심도 매트릭스 갱신.
   - 변경 영향 큰 이해관계자(OEM·인증기관) 의 변경 신호를 모니터링한다.

7. **StRS 검토 게이트 통과** (→ SUP.1)
   - QA 가 StRS 의 일관성·완전성·시험가능성을 검토한다.
   - 검토 코멘트 종결 후 다음 단계(SYS.2) 진입을 승인한다.

### 5.3 완료 조건 체크리스트

- [ ] 이해관계자 대장에 외부·내부 각 카테고리별 SPOC 명시 완료
- [ ] StRS 의 모든 요구사항에 고유 ID(STK-...) 부여 완료
- [ ] StRS 의 모든 요구사항에 우선순위(MoSCoW) 부여 완료
- [ ] Safety/Security 요구사항이 Must 로 분류되었는지 재확인
- [ ] OEM 으로부터 서면 합의(이메일 회신 또는 전자결재) 수령 완료
- [ ] StRS v1.0 이 CM 시스템에 베이스라인 등록되고 변경관리 가능 상태
- [ ] QA 검토 코멘트 0건 또는 모두 종결
- [ ] [[MAT-001_문서관리대장]] 에 StRS 등록 완료

## 6. 인터페이스 부서

- **OEM Customer**: 요구사항 합의·변경 협상 (외부)
- **Safety Engineering**: ASIL 후보 식별 (사전 검토)
- **Cybersecurity Engineering**: CAL 후보 식별 (사전 검토)
- **CM (SUP.8)**: 베이스라인 등록·변경관리
- **QA (SUP.1)**: StRS 품질 검토 게이트
- **Project Manager**: 일정·자원·승인

## 7. 주의사항 / 예외 처리

### 7.1 RFQ 사양 모호 / 누락 시
- OEM 사양서의 표현이 모호하거나(예: "충분히 안전한") 수치가 누락된 경우:
  - **금지**: System Engineer 임의로 수치 가정·작성 → 감사 부적합 사유.
  - **수행**: TMP-ASPICE-01-01-01-01 §6 "Open Issue" 에 등록 → OEM 회신 받을 때까지 해당 요구사항을 `status: pending` 으로 표시 → 회신 도착 시 정식 요구사항화.
  - 5 영업일 이상 회신 지연 시 Project Manager 에게 에스컬레이션.

### 7.2 OEM 요구사항이 표준·법규와 충돌 시
- 예: OEM 가 ISO 26262 위반 가능 설계를 요청한 경우.
  - 즉시 Safety Engineer + Project Manager 에 알림.
  - OEM 에 공식 서면(이슈 노트) 으로 표준 위반 가능성 통지.
  - 표준 준수 대안 설계 제안 → OEM 합의 후 변경 진행.
  - 본 절차의 결과는 반드시 회의록·이메일로 증적화한다.

### 7.3 베이스라인 후 긴급 변경 (Hot StRS Change)
- 차량 출시 임박 단계에서 OEM 가 긴급 요구사항 변경을 요청한 경우:
  - [[PRO-ASPICE-01-08_문제및변경관리프로세스]] 의 SUP.10 변경 절차로 즉시 이관.
  - StRS 단독 수정 금지 — CCB 영향 평가 후 v1.x 또는 v2.0 으로 재발행.

### 7.4 다국어/이중 표기 요구사항
- OEM RFQ 가 영문·한글·독일어 등 다국어로 제공된 경우:
  - 정본은 OEM 가 지정한 언어 1종으로 한다.
  - 번역본은 참고용이며 정본과 충돌 시 정본 우선.
  - 번역 차이로 인한 이슈 발견 시 §7.1 절차로 처리.

## 8. 연계 템플릿 / 기록

- 템플릿: [[TMP-ASPICE-01-01-01-01_이해관계자요구사항명세서]]
- 작성예시: [[EX-ASPICE-01-01-01-01_이해관계자요구사항명세서_작성예시]]
- 기록 폴더: `vault/08_REC_기록/SYS.1/` (REC-SYS1-{프로젝트코드}-{YYYYMMDD})

## 9. 출처 (source_citation)

```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SYS.1-PURPOSE-001 / VWAY-SYS.1-BP1~BP6"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
- type: standard_original
  file: "inputs/06_목표흐름/business_flow.yaml"
  locator: "SCN-001 (이해관계자 요구사항 도출)"
  retrieved_at: "2026-05-06"
```

## 10. 개정 이력

| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SYS.1 BP1~BP6 매핑 | (대기) |
