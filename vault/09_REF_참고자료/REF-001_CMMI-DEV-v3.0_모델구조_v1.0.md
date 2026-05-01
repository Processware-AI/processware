---
type: REF
doc_id: "REF-001"
title: "CMMI for Development v3.0 — 모델 구조 요약"
version: "1.0"
source: "ISACA / CMMI Institute, CMMI for Development v3.0"
source_date: "2023"
author: "ISACA / CMMI Institute"
status: draft
created: 2026-04-29
updated: 2026-04-29
tags: [REF, CMMI, capability-model, paraphrase]
---

# CMMI for Development v3.0 — 모델 구조 (REF-001)

> 원문 출처: ISACA / CMMI Institute, *CMMI for Development, Version 3.0*
> 라이선스: ISACA — paraphrase only, 원문 직접 인용 금지
> 최종 확인일: 2026-04-29

## 요약

CMMI v3.0 은 개발(DEV)·서비스(SVC)·공급자관리(SPM) 등 도메인별 View 를 가진 capability model 이다. 본 REF 는 **CMMI-DEV View** 에 한해 모델 구조를 paraphrase 로 정리한다.

## 핵심 구조

### 1. 모델 계층

```
Domain View (DEV/SVC/SPM)
 └─ Practice Area (PA)         ← 본 편입 = 20개 PA (Core 17 + Dev 2 + Supplier 1)
      └─ Practice Group (PG)    ← PG1~PG5 (성숙도 단계)
           └─ Practice          ← 각 PA 별 PG 단위로 Practice Statement 보유
                ├─ Required:    Practice Statement (의무)
                ├─ Expected:    Intent / Value
                └─ Informative: Activities / Work Products (예시)
```

### 2. Practice Group 의 의미

| PG | 의미 | 평가 매핑 |
|---|---|---|
| PG1 | Initial — 기본 수행 | (성숙도 평가 직접 대상 아님) |
| PG2 | Managed — 계획·관리 | ML2 평가 충족 기준 |
| PG3 | Defined — 조직 표준화 | ML3 평가 충족 기준 |
| PG4 | Quantitatively managed — 정량 관리 | ML4 평가 충족 기준 |
| PG5 | Optimizing — 지속 개선 | ML5 평가 충족 기준 |

### 3. Maturity Level 평가 모델

ML 평가는 **누적**: ML3 = ML2 PA 의 PG2 + ML3 PA 의 PG3.

| ML | 충족 PA |
|---|---|
| ML2 (Managed) | CM, MC, MPM, PAD, PLAN, PQA, RDM, RSK, SAM (+ GOV·II 의 PG2) |
| ML3 (Defined) | ML2 + CAR, DAR, EST, GOV(PG3), II(PG3), OT, PCM, PR, VV, PI, TS |

### 4. PA 카테고리 (CMMI v3.0)

#### Doing (실행)
- **Ensuring Quality**: RDM, PQA, PR, VV
- **Engineering & Developing Products**: TS, PI
- **Selecting & Managing Suppliers**: SAM

#### Managing (관리)
- **Planning & Managing Work**: EST, PLAN, MC
- **Managing Business Resilience**: RSK
- **Managing the Workforce**: OT

#### Enabling (지원)
- **Supporting Implementation**: CM, CAR, DAR

#### Improving (개선)
- **Sustaining Habit & Persistence**: GOV, II
- **Improving Performance**: MPM, PCM, PAD

### 5. Context Tags (컨텍스트별 추가 정보)

각 Practice 는 컨텍스트별 추가 적용 정보를 제공:
- **CMMI-DEV** (개발)
- **Agile Development** (애자일)
- **DevSecOps**
- **CMMI-SAF** (안전)
- **CMMI-SEC** (보안)
- **CMMI Data** (데이터)
- **CMMI-PPL** (인력)
- **CMMI-SPM** (공급자)
- **CMMI-SVC** (서비스)

## 핵심 조항 / 요구사항 (Practice 카운트)

| PA | PG1 | PG2 | PG3 | PG4 | PG5 | 합계 |
|---|---|---|---|---|---|---|
| CAR | 1 | 3 | 2 | (PG4·5 추가) | — | 6+ |
| CM | 1 | 6 | — | — | — | 7 |
| DAR | 2 | 6 | — | — | — | 8 |
| EST | 1 | 2 | 2 | (PG4 추가) | — | 5+ |
| GOV | 1 | 6 | 2 | (PG4 추가) | — | 9+ |
| II | 1 | 2 | 3 | — | — | 6 |
| MC | 2 | 4 | 4 | — | — | 10 |
| MPM | 2 | 6 | 6 | (PG4·5 추가) | — | 14+ |
| OT | 1 | 2 | 7 | — | — | 10 |
| PAD | 1 | 2 | 6 | — | — | 9 |
| PCM | 1 | 2 | 4 | (PG4·5 추가) | — | 7+ |
| PLAN | 2 | 8 | 4 | 1 | — | 15 |
| PQA | 1 | 4 | — | — | — | 5 |
| PR | 1 | 3 | 1 | — | — | 5 |
| RDM | 1 | 5 | 7 | — | — | 13 |
| RSK | 2 | 5 | 3 | — | — | 10 |
| VV | 2 | 3 | 3 | — | — | 8 |
| PI | 1 | 3 | 4 | — | — | 8 |
| TS | 1 | 5 | 2 | — | — | 8 |
| SAM | 2 | 6 | — | — | — | 8 |

## 적용 영향

### 본 체계(CMMI-DEV-ML3 편입) 에 미치는 영향
- **POL/PRO 영역코드**: `CMMI` 단일 코드 사용 (interface_only)
- **추적성**: MAT-011 에서 Req-ID(CMMI-{PA}-{level}.{num}) → POL/PRO/WI 매핑 필수
- **평가 증적**: 각 Practice Statement 충족 증거(WI 수행 기록 + REC) 보유 필요

## 관련 내부 문서

- [[00_CMMI-DEV-ML3_표준개요]]
- [[01_CMMI-DEV-ML3_요구사항분해]]
- [[REF-002_CMMI-DEV_ML평가체계_v1.0]]
- [[REF-003_CMMI-vs-ASPICE_비교_v1.0]]

## 원문 인용

> 본 REF 는 paraphrase 만 포함. 원문 인용은 ISACA 라이선스에 따라 금지.

## 변경 알림

- 외부 원문 개정(예: CMMI v2.x 신규 PA 추가) 시: 본 REF 버전 업 + MAT-002 동기화 + Req-ID 분해표 갱신
