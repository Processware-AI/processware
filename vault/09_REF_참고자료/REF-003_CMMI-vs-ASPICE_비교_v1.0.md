---
type: REF
doc_id: "REF-003"
title: "CMMI-DEV-ML3 vs ASPICE — 비교 가이드"
version: "1.0"
source: "ISACA CMMI v3.0 + VDA Automotive SPICE v3.1/4.0"
source_date: "ASPICE v3.1 (2017), v4.0 (2023)"
author: "ISACA / VDA QMC"
status: draft
created: 2026-04-29
updated: 2026-04-29
tags: [REF, CMMI, ASPICE, comparison, paraphrase]
---

# CMMI-DEV-ML3 vs ASPICE — 비교 가이드 (REF-003)

> 출처: ISACA CMMI v3.0 + VDA Automotive SPICE v3.1/4.0 (둘 다 paraphrase only)
> 최종 확인일: 2026-04-29

## 요약

CMMI 와 ASPICE 는 둘 다 **capability_model** 이며 PA-Practice 구조가 유사하지만, 적용 도메인·구조·평가 방식이 다르다. 본 REF 는 두 표준의 핵심 차이를 paraphrase 로 정리하여 동시 도입 또는 선택 시 의사결정을 돕는다.

## 핵심 비교

### 1. 기본 정보

| 항목 | CMMI-DEV v3.0 | ASPICE v3.1/4.0 |
|---|---|---|
| 발행기관 | ISACA / CMMI Institute | VDA QMC (독일자동차산업협회 품질경영센터) |
| 적용 도메인 | 일반 SW·시스템 개발 (특히 미국) | 자동차 SW (특히 유럽) |
| Layer 분류 | L2_engineering | L2_engineering |
| Structure | capability_model | capability_model |
| Maturity 단계 | 5단계 ML (1~5) | 5단계 CL (Capability Level 0~5) |
| 평가 단위 | OU 전체 (조직 성숙도) | PA별 (프로세스별 능력) |

### 2. 구조 비교

| 비교 축 | CMMI v3.0 | ASPICE |
|---|---|---|
| 단위 | Practice Area (PA) | Process |
| Practice 그룹화 | Practice Group (PG1~5) | Base Practice + Generic Practice |
| 평가 모델 | Benchmark Appraisal | VDA Scope Process Assessment |
| 적용 모델 | Practice Statement (Required) | Base Practice + Outcome |

### 3. PA / Process 매핑 (주요)

| 영역 | CMMI PA | ASPICE Process |
|---|---|---|
| 요구사항 개발 | RDM | SYS.1, SYS.2, SWE.1 |
| 설계 | TS | SYS.3, SWE.2 |
| 구현 | TS-2.4 | SWE.3 |
| 단위 검증 | VV | SWE.4 |
| 통합 검증 | PI, VV | SWE.5, SWE.6, SYS.4, SYS.5 |
| 형상관리 | CM | SUP.8 |
| 변경관리 | CM-2.4 | SUP.10 |
| 품질보증 | PQA | SUP.1 |
| 동료검토 | PR | SUP.4 |
| 문서관리 | PAD-3.3, CM | SUP.7 |
| 측정 | MPM | (Generic Practice GP 2.x) |
| 위험관리 | RSK | MAN.5 |
| 프로젝트관리 | PLAN, MC, EST | MAN.3 |
| 공급자관리 | SAM | ACQ.4 |

### 4. 차이점

| 특성 | CMMI | ASPICE |
|---|---|---|
| **V-model 강조** | 약함 (라이프사이클 중립) | 강함 (좌측=설계, 우측=검증·통합) |
| **자동차 특화** | 없음 (Generic) | 강함 (HARA·기능안전 연계) |
| **Tailoring 강조** | 강함 (PAD-3.2 명시) | 중간 (Process Definition 가이드) |
| **거버넌스 PA** | GOV (별도 PA) | (GP 2.4 ~ 5.x 분산) |
| **계약·공급자** | SAM (별도 PA) | ACQ family |
| **인적자원** | OT (별도 PA) | (GP 2.5 분산) |
| **측정 저장소** | MPM PA + PAD-3.5 (명시) | (조직 GP 만) |

### 5. 평가 통과의 의미

| ML/CL | CMMI ML3 | ASPICE CL3 |
|---|---|---|
| 의미 | 조직 표준 프로세스 정의·운영 | 프로세스가 정의·표준화 |
| 범위 | OU 전체 (모든 PA × PG3) | 평가 대상 Process × CL3 |
| 자동차 산업 요구 | 권고 (Defense·일부 IT 기업 우선) | 사실상 필수 (OEM tier 1·2) |

## 의사결정 가이드

### 어느 표준을 선택할까?

| 상황 | 권고 |
|---|---|
| 자동차 도메인 (OEM 공급자) | ASPICE CL2~3 우선 |
| 의료기기·금융·국방 SW | CMMI ML3 |
| 일반 ICT 기업 (B2C·B2B) | CMMI ML3 또는 ISO/IEC/IEEE 12207 + ISO 9001 |
| 멀티 도메인 글로벌 기업 | 두 표준 동시 도입 가능 (interface_only 통합) |

### 동시 도입 시 통합 전략 (둘 다 interface_only)

1. **공통 OSSP 정의**: 두 표준이 모두 요구하는 프로세스 정의 일원화
2. **PA·Process 양쪽 추적**: 단일 PRO 가 CMMI Practice + ASPICE Base Practice 동시 충족
3. **별도 영역코드 유지**: `CMMI` + `SPICE` 코드 혼동 방지
4. **MAT-006 계층 매트릭스**: 두 표준의 동일 영역(예: CM↔SUP.8) 교차 매핑

## 본 체계 적용 영향

- 본 편입은 `CMMI-DEV-ML3` 단독. 추후 자동차 도메인 확장 시 `ASPICE` 영역코드 추가 편입 가능 ([[07_표준분류레지스트리]] 등록 완료)
- `MAT-006_문서계층추적매트릭스.md` 에서 CMMI ↔ ASPICE 양쪽 매핑 가능

## 관련 내부 문서

- [[00_CMMI-DEV-ML3_표준개요]]
- [[REF-001_CMMI-DEV-v3.0_모델구조_v1.0]]
- [[REF-002_CMMI-DEV_ML평가체계_v1.0]]
- [[07_표준분류레지스트리]] §2.5

## 원문 인용

> 두 표준 모두 paraphrase only. 원문 직접 인용 금지.

## 변경 알림

- ASPICE v4.0 (2023) 의 Cybersecurity 추가 등 개정 시: 본 REF 버전 업
