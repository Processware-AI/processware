---
type: WI
doc_id: "WI-SPICE-01-02-02"
title: "SW 아키텍처 설계 (SWE.2)"
version: "0.1"
owner: "SW Architect"
reviewer: "SW Engineer / Safety Engineer / QA"
approver: "SW Lead"
scope: "SwRS → SW 아키텍처(컴포넌트·인터페이스·자원·타이밍)"
parent_pro: "[[PRO-SPICE-01-02_소프트웨어공학프로세스]]"
related_tmp:
  - "[[TMP-SPICE-01-02-02-01_SW아키텍처기술서]]"
related_rec: []
standards: ["Automotive SPICE 4.0", "AUTOSAR", "ISO 26262"]
aspice_processes: ["SWE.2"]
entry_gate: "WI-SPICE-01-02-01.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SWE.2, AUTOSAR, RTE, WCET]
---

# SW 아키텍처 설계 업무지침 (WI-SPICE-01-02-02)

> 상위 절차: [[PRO-SPICE-01-02_소프트웨어공학프로세스]] §5 단계 4~5
> ASPICE 매핑: SWE.2 (Software Architectural Design) — BP1~BP5

## 1. 업무 목적

SwRS 를 입력으로 SW 컴포넌트 구조·인터페이스·자원·타이밍을 정의하여 후속 상세설계(SWE.3) 의 기반을 마련한다. AUTOSAR Classic/Adaptive 환경에서는 RTE Layer 와 BSW 인터페이스를 명세한다.

## 2. 수행 주체

- **주 수행자**: SW Architect
- **공동 수행자**: SW Engineer (실현 가능성 검토)
- **검토자**: Safety Engineer (분리·중복화), QA
- **승인자**: SW Lead

## 3. 범위

WI-SPICE-01-02-01 의 SwRS v1.0 베이스라인 등록 후부터 SW Architecture Description (SwAD) v1.0 베이스라인 등록까지 적용한다.

## 4. 입력 자료 / 산출물

- **Input**: SwRS v1.0, ICD (시스템 인터페이스), 자원 예산
- **Output**: SwAD v1.0, Interface Spec, Resource/Timing Analysis, SwRS↔SwAD 추적성

## 5. 수행 절차

### 5.1 사전 준비
1. AUTOSAR 환경(Classic/Adaptive) 확정 + 모델링 도구(DaVinci/EB tresos) 준비.
2. RTE Generation 파이프라인 점검.

### 5.2 수행 단계
1. **SW 아키텍처 정의** (SWE.2.BP1)
   - SwRS → 컴포넌트(SWC) 분해. AUTOSAR Classic 의 경우 ASW + BSW 계층 구분.
   - 각 SWC 의 책임·인터페이스 명시.

2. **인터페이스 명세** (SWE.2.BP2)
   - Sender/Receiver Port, Client/Server Port, Service Interface (Adaptive).
   - 데이터 타입·범위·QoS·Timeout 정의.

3. **자원·타이밍 분석** (SWE.2.BP3)
   - WCET (Worst-Case Execution Time) 추정.
   - 메모리 사용량·CPU 점유율·통신 대역폭 모델링.
   - 결과: TMP-SPICE-01-02-02-01 §3 "자원/타이밍 분석".

4. **동적 거동 명세** (SWE.2.BP4)
   - Task 스케줄링·Runnable 매핑·Event 트리거.
   - Safety-critical Runnable 은 우선순위·실행 보장 명시.

5. **SwRS↔SwAD 추적성** (SWE.2.BP5)
   - 양방향 link 등록.

6. **검토 게이트** (→ SUP.1)
   - QA + Safety + Architect 합동 검토 → SwAD v1.0 베이스라인.

### 5.3 완료 조건 체크리스트
- [ ] 모든 SWC 의 책임·인터페이스 명시
- [ ] AUTOSAR Port Interface 모두 정의 (Custom 의 경우 사유 기록)
- [ ] WCET·메모리·CPU 분석 완료 + HW 한계 미만 확인
- [ ] Task 스케줄·Runnable 매핑 명시
- [ ] SwRS↔SwAD 양방향 추적성 ≥ 95%
- [ ] QA + Safety 검토 코멘트 종결
- [ ] SwAD v1.0 베이스라인 + MAT-001 갱신

## 6. 인터페이스 부서
- **System Engineering**: 시스템 인터페이스 정합성
- **HW Lead**: 자원 한계 합의
- **Safety Engineering**: ASIL 분리·중복화 검토
- **CM·QA**: 베이스라인·검토

## 7. 주의사항 / 예외 처리

### 7.1 RTE 생성 실패
- DaVinci/EB tresos 에서 RTE Generation 실패 시:
  - 즉시 도구 로그 분석 + AUTOSAR 표준 위반 여부 확인.
  - 위반이면 인터페이스 재정의, 도구 결함이면 벤더에 RFC 요청.
  - 회피용 수동 RTE 작성은 Safety Manager 승인 후에만 허용.

### 7.2 WCET 한계 초과
- WCET 추정값이 Task 마감 시간 초과 시:
  - 1) 알고리즘 최적화. 2) Task 분할. 3) HW 사양 상향 협상.
  - 미해결 시 SyRS 회귀.

### 7.3 ASIL 혼재 (Mixed Criticality)
- 단일 ECU 에 ASIL D + QM Task 혼재 시:
  - Memory Protection Unit (MPU) 분리 강제.
  - Freedom from Interference 분석서 첨부.

### 7.4 Adaptive AUTOSAR 신규 적용
- Adaptive 환경 첫 적용 프로젝트:
  - PoC (Proof of Concept) 1주 사전 수행 + 결과 SW Lead 보고.
  - SOA (Service-Oriented Architecture) 패턴 가이드라인 별도 작성.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-SPICE-01-02-02-01_SW아키텍처기술서]]
- 작성예시: [[EX-SPICE-01-02-02-01_SW아키텍처기술서_작성예시]]
- 기록 폴더: `vault/08_REC_기록/SWE.2/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SWE.2-PURPOSE-001 / VWAY-SWE.2-BP1~BP5"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SWE.2 BP1~BP5 + AUTOSAR Classic/Adaptive | (대기) |
