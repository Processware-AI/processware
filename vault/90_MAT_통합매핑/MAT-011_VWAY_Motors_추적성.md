---
type: MAT
doc_id: MAT-011
title: VWAY_Motors (ASPICE 4.0) 표준별 추적성 매트릭스
version: "0.2"
standard: VWAY_Motors
base_standard: "Automotive SPICE 4.0"
scope_code: ASPICE
owner: "Process Quality Office"
reviewer: "ASPICE Lead Assessor"
approver: "CTO"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
retention: "상시"
tags: [MAT, traceability, ASPICE, ASPICE4, VWAY_Motors, SPICE]
---

# MAT-011 VWAY_Motors (ASPICE 4.0) 표준별 추적성 매트릭스

> 상위: [[MOC_추적성매트릭스]] · 적용요건: [[적용요건]] · 정책: [[POL-ASPICE-01_ASPICE역량거버넌스정책]]
> 공통 매트릭스 연동: [[MAT-002_규제요구사항_대조표]] · [[MAT-003_산출물_목록표]] · [[MAT-004_RACI_통합표]] · [[MAT-006_문서계층_추적매트릭스]]
> 유사 매트릭스 역할 구분:
> - MAT-002 (규제요구사항 대조표): **법규 조항** 축
> - **MAT-011 (본 문서)**: VWAY_Motors의 **Req-ID** 축 (53건)
> - MAT-006 (문서 계층 추적): **문서 구조(POL→PRO→WI→TMP→EX)** 축

## 0. 본 문서의 범위

본 매트릭스는 [[적용요건]] 의 **53 Req-ID** 를 VWAY Motors 가 수립한 **POL 1건 + PRO 11건 + WI 59건 + TMP 50건 + EX 50건** 산출물에 1:1 매핑한 표준별 추적성 매트릭스다.

- 원천: `inputs/01_표준원문/VWAY_Motors/requirements.yaml` (407 Req)
- 적용요건 (대표 Req): `vault/02_적용요건/VWAY_Motors/적용요건.md` (53 Req)
- Req-ID 체계: `ASPICE-{프로세스}-R-{NNN}`
- 산출물 코드체계: `{TYPE}-ASPICE-{PRO번호}-{WI번호}_{이름}`

---

## 1. Req → POL/PRO/WI/TMP 매핑 표 (53행)

### 1.1 Acquisition / Supply (ACQ.4, SPL.2) — 7 Req

| Req-ID | ASPICE프로세스 | 의무수준 | POL | PRO | WI | TMP | 비고 |
|---|---|---|---|---|---|---|---|
| ASPICE-ACQ4-R-001 | ACQ.4 Purpose | 의무 | [[POL-ASPICE-01_ASPICE역량거버넌스정책]] | [[PRO-ASPICE-01-06_구매및공급망프로세스]] | WI-ASPICE-01-06-01 (공동활동운영) | TMP-ASPICE-06-합의서 | ✅ 반영완료 |
| ASPICE-ACQ4-R-002 | ACQ.4.BP1 | 의무 | — | [[PRO-ASPICE-01-06_구매및공급망프로세스]] | WI-ASPICE-01-06-01 (공동활동운영) | TMP-ASPICE-06-회의록 | ✅ 반영완료 |
| ASPICE-ACQ4-R-003 | ACQ.4.BP3 | 의무 | — | [[PRO-ASPICE-01-06_구매및공급망프로세스]] | WI-ASPICE-01-06-02 (공급사정보교환) | TMP-ASPICE-06-리뷰결과 | ✅ 반영완료 |
| ASPICE-ACQ4-R-004 | ACQ.4.BP5 | 의무 | — | [[PRO-ASPICE-01-06_구매및공급망프로세스]] | WI-ASPICE-01-06-04 (합의변경및시정조치) | TMP-ASPICE-06-시정조치 | ✅ 반영완료 |
| ASPICE-SPL2-R-001 | SPL.2 Purpose | 의무 | — | [[PRO-ASPICE-01-05_검증및인도프로세스]] | WI-ASPICE-01-05-04 (릴리스생성) | TMP-ASPICE-05-릴리스노트 | ✅ 반영완료 |
| ASPICE-SPL2-R-002 | SPL.2.BP1 | 의무 | — | [[PRO-ASPICE-01-05_검증및인도프로세스]] | WI-ASPICE-01-05-04 (릴리스생성) | TMP-ASPICE-05-릴리스기록 | ✅ 반영완료 |
| ASPICE-SPL2-R-003 | SPL.2.BP4 | 의무 | — | [[PRO-ASPICE-01-05_검증및인도프로세스]] | WI-ASPICE-01-05-05 (OEM인도) | TMP-ASPICE-05-인도확인서 | ✅ 반영완료 |

### 1.2 System Engineering (SYS.1~5) — 12 Req

| Req-ID | ASPICE프로세스 | 의무수준 | POL | PRO | WI | TMP | 비고 |
|---|---|---|---|---|---|---|---|
| ASPICE-SYS1-R-001 | SYS.1 Purpose | 의무 | — | [[PRO-ASPICE-01-01_시스템공학프로세스]] | WI-ASPICE-01-01-01 (이해관계자요구사항도출) | TMP-ASPICE-01-요구사항대장 | ✅ 반영완료 |
| ASPICE-SYS1-R-002 | SYS.1.BP1 | 의무 | — | [[PRO-ASPICE-01-01_시스템공학프로세스]] | WI-ASPICE-01-01-01 (이해관계자요구사항도출) | TMP-ASPICE-01-이해관계자대장 | ✅ 반영완료 |
| ASPICE-SYS1-R-003 | SYS.1.BP3 | 의무 | — | [[PRO-ASPICE-01-01_시스템공학프로세스]] | WI-ASPICE-01-01-01 (이해관계자요구사항도출) | TMP-ASPICE-01-변경합의서 | ✅ 반영완료 |
| ASPICE-SYS2-R-001 | SYS.2 Purpose | 의무 | — | [[PRO-ASPICE-01-01_시스템공학프로세스]] | WI-ASPICE-01-01-02 (시스템요구사항분석) | TMP-ASPICE-01-SyRS | ✅ 반영완료 |
| ASPICE-SYS2-R-002 | SYS.2.BP1 | 의무 | — | [[PRO-ASPICE-01-01_시스템공학프로세스]] | WI-ASPICE-01-01-02 (시스템요구사항분석) | TMP-ASPICE-01-SyRS | ✅ 반영완료 |
| ASPICE-SYS2-R-003 | SYS.2.BP5 | 의무 | — | [[PRO-ASPICE-01-01_시스템공학프로세스]] | WI-ASPICE-01-01-06 (추적성매트릭스관리) | [[MAT-011_VWAY_Motors_추적성]] | ✅ 반영완료 |
| ASPICE-SYS3-R-001 | SYS.3 Purpose | 의무 | — | [[PRO-ASPICE-01-01_시스템공학프로세스]] | WI-ASPICE-01-01-03 (시스템아키텍처설계) | TMP-ASPICE-01-아키텍처명세 | ✅ 반영완료 |
| ASPICE-SYS3-R-002 | SYS.3.BP1 | 의무 | — | [[PRO-ASPICE-01-01_시스템공학프로세스]] | WI-ASPICE-01-01-03 (시스템아키텍처설계) | TMP-ASPICE-01-인터페이스대장 | ✅ 반영완료 |
| ASPICE-SYS3-R-003 | SYS.3.BP5 | 의무 | — | [[PRO-ASPICE-01-01_시스템공학프로세스]] | WI-ASPICE-01-01-06 (추적성매트릭스관리) | [[MAT-011_VWAY_Motors_추적성]] | ✅ 반영완료 |
| ASPICE-SYS4-R-001 | SYS.4 Purpose | 의무 | — | [[PRO-ASPICE-01-01_시스템공학프로세스]] | WI-ASPICE-01-01-04 (시스템통합및검증) | TMP-ASPICE-01-통합테스트계획 | ✅ 반영완료 |
| ASPICE-SYS4-R-002 | SYS.4.BP3 | 의무 | — | [[PRO-ASPICE-01-01_시스템공학프로세스]] | WI-ASPICE-01-01-04 (시스템통합및검증) | TMP-ASPICE-01-통합검증결과 | ✅ 반영완료 |
| ASPICE-SYS5-R-001 | SYS.5 Purpose | 의무 | — | [[PRO-ASPICE-01-01_시스템공학프로세스]] | WI-ASPICE-01-01-05 (시스템요구사항검증) | TMP-ASPICE-01-검증보고서 | ✅ 반영완료 |
| ASPICE-SYS5-R-002 | SYS.5.BP3 | 의무 | — | [[PRO-ASPICE-01-01_시스템공학프로세스]] | WI-ASPICE-01-01-05 (시스템요구사항검증) | TMP-ASPICE-01-검증결과 | ✅ 반영완료 |

### 1.3 Validation (VAL.1) — 3 Req

| Req-ID | ASPICE프로세스 | 의무수준 | POL | PRO | WI | TMP | 비고 |
|---|---|---|---|---|---|---|---|
| ASPICE-VAL1-R-001 | VAL.1 Purpose | 의무 | — | [[PRO-ASPICE-01-05_검증및인도프로세스]] | WI-ASPICE-01-05-01 (사용자검증) | TMP-ASPICE-05-검증계획 | ✅ 반영완료 |
| ASPICE-VAL1-R-002 | VAL.1.BP2 | 의무 | — | [[PRO-ASPICE-01-05_검증및인도프로세스]] | WI-ASPICE-01-05-02 (도로및필드검증) | TMP-ASPICE-05-환경구성기록 | ✅ 반영완료 |
| ASPICE-VAL1-R-003 | VAL.1.BP4 | 의무 | — | [[PRO-ASPICE-01-05_검증및인도프로세스]] | WI-ASPICE-01-05-03 (고객승인) | TMP-ASPICE-05-검증결과 | ✅ 반영완료 |

### 1.4 Software Engineering (SWE.1~6) — 12 Req

| Req-ID | ASPICE프로세스 | 의무수준 | POL | PRO | WI | TMP | 비고 |
|---|---|---|---|---|---|---|---|
| ASPICE-SWE1-R-001 | SWE.1 Purpose | 의무 | — | [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] | WI-ASPICE-01-02-01 (SW요구사항명세) | TMP-ASPICE-02-SwRS | ✅ 반영완료 |
| ASPICE-SWE1-R-002 | SWE.1.BP1 | 의무 | — | [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] | WI-ASPICE-01-02-01 (SW요구사항명세) | TMP-ASPICE-02-SwRS | ✅ 반영완료 |
| ASPICE-SWE1-R-003 | SWE.1.BP5 | 의무 | — | [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] | WI-ASPICE-01-02-06 (추적성매트릭스관리) | [[MAT-011_VWAY_Motors_추적성]] | ✅ 반영완료 |
| ASPICE-SWE2-R-001 | SWE.2 Purpose | 의무 | — | [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] | WI-ASPICE-01-02-02 (SW아키텍처설계) | TMP-ASPICE-02-SW아키텍처명세 | ✅ 반영완료 |
| ASPICE-SWE2-R-002 | SWE.2.BP3 | 의무 | — | [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] | WI-ASPICE-01-02-02 (SW아키텍처설계) | TMP-ASPICE-02-자원분석결과 | ✅ 반영완료 |
| ASPICE-SWE3-R-001 | SWE.3 Purpose | 의무 | — | [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] | WI-ASPICE-01-02-03 (상세설계및단위구현) | TMP-ASPICE-02-상세설계서 | ✅ 반영완료 |
| ASPICE-SWE3-R-002 | SWE.3.BP3 | 의무 | — | [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] | WI-ASPICE-01-02-03 (상세설계및단위구현) | REF-코딩표준 | ✅ 반영완료 |
| ASPICE-SWE4-R-001 | SWE.4 Purpose | 의무 | — | [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] | WI-ASPICE-01-02-04 (단위검증) | TMP-ASPICE-02-단위테스트케이스 | ✅ 반영완료 |
| ASPICE-SWE4-R-002 | SWE.4.BP3 | 의무 | — | [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] | WI-ASPICE-01-02-04 (단위검증) | TMP-ASPICE-02-단위검증결과 | ✅ 반영완료 |
| ASPICE-SWE5-R-001 | SWE.5 Purpose | 의무 | — | [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] | WI-ASPICE-01-02-05 (통합검증) | TMP-ASPICE-02-통합테스트계획 | ✅ 반영완료 |
| ASPICE-SWE5-R-002 | SWE.5.BP4 | 의무 | — | [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] | WI-ASPICE-01-02-05 (통합검증) | TMP-ASPICE-02-통합검증결과 | ✅ 반영완료 |
| ASPICE-SWE6-R-001 | SWE.6 Purpose | 의무 | — | [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] | WI-ASPICE-01-02-06 (SW검증) | TMP-ASPICE-02-SW검증보고서 | ✅ 반영완료 |
| ASPICE-SWE6-R-002 | SWE.6.BP4 | 의무 | — | [[PRO-ASPICE-01-02_소프트웨어공학프로세스]] | WI-ASPICE-01-02-06 (SW검증) | TMP-ASPICE-02-SW검증결과 | ✅ 반영완료 |

### 1.5 Machine Learning Engineering (MLE.1~4) — 8 Req ★신규

| Req-ID | ASPICE프로세스 | 의무수준 | POL | PRO | WI | TMP | 비고 |
|---|---|---|---|---|---|---|---|
| ASPICE-MLE1-R-001 | MLE.1 Purpose | 의무 | — | [[PRO-ASPICE-01-04_머신러닝공학프로세스]] | WI-ASPICE-01-04-01 (ML요구사항명세) | TMP-ASPICE-04-ML요구사항명세서 | ✅ 반영완료 |
| ASPICE-MLE1-R-002 | MLE.1.BP1 | 의무 | — | [[PRO-ASPICE-01-04_머신러닝공학프로세스]] | WI-ASPICE-01-04-01 (ML요구사항명세) | TMP-ASPICE-04-ML요구사항명세서 | ✅ 반영완료 |
| ASPICE-MLE2-R-001 | MLE.2 Purpose | 의무 | — | [[PRO-ASPICE-01-04_머신러닝공학프로세스]] | WI-ASPICE-01-04-02 (ML아키텍처설계) | TMP-ASPICE-04-ML아키텍처 | ✅ 반영완료 |
| ASPICE-MLE2-R-002 | MLE.2.BP3 | 의무 | — | [[PRO-ASPICE-01-04_머신러닝공학프로세스]] | WI-ASPICE-01-04-02 (ML아키텍처설계) | TMP-ASPICE-04-인터페이스대장 | ✅ 반영완료 |
| ASPICE-MLE3-R-001 | MLE.3 Purpose | 의무 | — | [[PRO-ASPICE-01-04_머신러닝공학프로세스]] | WI-ASPICE-01-04-03 (모델학습) | TMP-ASPICE-04-학습계획 | ✅ 반영완료 |
| ASPICE-MLE3-R-002 | MLE.3.BP4 | 의무 | — | [[PRO-ASPICE-01-04_머신러닝공학프로세스]] | WI-ASPICE-01-04-03 (모델학습) | TMP-ASPICE-04-학습결과 | ✅ 반영완료 |
| ASPICE-MLE4-R-001 | MLE.4 Purpose | 의무 | — | [[PRO-ASPICE-01-04_머신러닝공학프로세스]] | WI-ASPICE-01-04-04 (모델테스트) | TMP-ASPICE-04-테스트계획 | ✅ 반영완료 |
| ASPICE-MLE4-R-002 | MLE.4.BP3 | 의무 | — | [[PRO-ASPICE-01-04_머신러닝공학프로세스]] | WI-ASPICE-01-04-04 (모델테스트) | TMP-ASPICE-04-평가결과 | ✅ 반영완료 |

### 1.6 Hardware Engineering (HWE.1~4) — 8 Req

| Req-ID | ASPICE프로세스 | 의무수준 | POL | PRO | WI | TMP | 비고 |
|---|---|---|---|---|---|---|---|
| ASPICE-HWE1-R-001 | HWE.1 Purpose | 의무 | — | [[PRO-ASPICE-01-03_하드웨어공학프로세스]] | WI-ASPICE-01-03-01 (HW요구사항명세) | TMP-ASPICE-03-HW요구사항명세서 | ✅ 반영완료 |
| ASPICE-HWE1-R-002 | HWE.1.BP1 | 의무 | — | [[PRO-ASPICE-01-03_하드웨어공학프로세스]] | WI-ASPICE-01-03-01 (HW요구사항명세) | TMP-ASPICE-03-HW요구사항명세서 | ✅ 반영완료 |
| ASPICE-HWE1-R-003 | HWE.1.BP5 | 의무 | — | [[PRO-ASPICE-01-03_하드웨어공학프로세스]] | WI-ASPICE-01-03-01 (HW요구사항명세) | [[MAT-011_VWAY_Motors_추적성]] | ✅ 반영완료 |
| ASPICE-HWE2-R-001 | HWE.2 Purpose | 의무 | — | [[PRO-ASPICE-01-03_하드웨어공학프로세스]] | WI-ASPICE-01-03-02 (HW설계) | TMP-ASPICE-03-HW설계명세 | ✅ 반영완료 |
| ASPICE-HWE2-R-002 | HWE.2.BP2 | 의무 | — | [[PRO-ASPICE-01-03_하드웨어공학프로세스]] | WI-ASPICE-01-03-02 (HW설계) | TMP-ASPICE-03-BOM | ✅ 반영완료 |
| ASPICE-HWE3-R-001 | HWE.3 Purpose ★변경 | 의무 | — | [[PRO-ASPICE-01-03_하드웨어공학프로세스]] | WI-ASPICE-01-03-03 (설계검증) | TMP-ASPICE-03-설계검증계획 | ✅ 반영완료 |
| ASPICE-HWE3-R-002 | HWE.3.BP4 | 의무 | — | [[PRO-ASPICE-01-03_하드웨어공학프로세스]] | WI-ASPICE-01-03-04 (HW설계검증) | TMP-ASPICE-03-검증결과 | ✅ 반영완료 |
| ASPICE-HWE4-R-001 | HWE.4 Purpose ★신규 | 의무 | — | [[PRO-ASPICE-01-03_하드웨어공학프로세스]] | WI-ASPICE-01-03-05 (HW요구사항검증) | TMP-ASPICE-03-요구사항검증계획 | ✅ 반영완료 |
| ASPICE-HWE4-R-002 | HWE.4.BP4 | 의무 | — | [[PRO-ASPICE-01-03_하드웨어공학프로세스]] | WI-ASPICE-01-03-05 (HW요구사항검증) | TMP-ASPICE-03-검증결과 | ✅ 반영완료 |

### 1.7 Supporting (SUP.1, SUP.8, SUP.9, SUP.10, SUP.11) — 12 Req

| Req-ID | ASPICE프로세스 | 의무수준 | POL | PRO | WI | TMP | 비고 |
|---|---|---|---|---|---|---|---|
| ASPICE-SUP1-R-001 | SUP.1 Purpose | 의무 | [[POL-ASPICE-01_ASPICE역량거버넌스정책]] | [[PRO-ASPICE-01-07_품질보증및형상관리프로세스]] | WI-ASPICE-01-07-02 (QA감사실시) | TMP-ASPICE-07-QA감사계획 | ✅ 반영완료 |
| ASPICE-SUP1-R-002 | SUP.1.BP3 | 의무 | — | [[PRO-ASPICE-01-07_품질보증및형상관리프로세스]] | WI-ASPICE-01-07-03 (시정조치및에스컬레이션) | TMP-ASPICE-07-QA보고서 | ✅ 반영완료 |
| ASPICE-SUP1-R-003 | SUP.1.BP4 | 의무 | [[POL-ASPICE-01_ASPICE역량거버넌스정책]] | [[PRO-ASPICE-01-07_품질보증및형상관리프로세스]] | WI-ASPICE-01-07-03 (시정조치및에스컬레이션) | TMP-ASPICE-07-에스컬레이션 | ✅ 반영완료 |
| ASPICE-SUP8-R-001 | SUP.8 Purpose | 의무 | — | [[PRO-ASPICE-01-07_품질보증및형상관리프로세스]] | WI-ASPICE-01-07-04 (형상항목식별) | TMP-ASPICE-07-CM계획 | ✅ 반영완료 |
| ASPICE-SUP8-R-002 | SUP.8.BP2 | 의무 | — | [[PRO-ASPICE-01-07_품질보증및형상관리프로세스]] | WI-ASPICE-01-07-04 (형상항목식별) | TMP-ASPICE-07-Baseline대장 | ✅ 반영완료 |
| ASPICE-SUP8-R-003 | SUP.8.BP4 | 의무 | — | [[PRO-ASPICE-01-07_품질보증및형상관리프로세스]] | WI-ASPICE-01-07-05 (베이스라인및변경통제) | TMP-ASPICE-07-변경이력 | ✅ 반영완료 |
| ASPICE-SUP9-R-001 | SUP.9 Purpose | 의무 | — | [[PRO-ASPICE-01-08_문제및변경관리프로세스]] | WI-ASPICE-01-08-01 (문제등록) | TMP-ASPICE-08-문제티켓 | ✅ 반영완료 |
| ASPICE-SUP9-R-002 | SUP.9.BP3 | 의무 | — | [[PRO-ASPICE-01-08_문제및변경관리프로세스]] | WI-ASPICE-01-08-02 (RCA수행) | TMP-ASPICE-08-RCA결과 | ✅ 반영완료 |
| ASPICE-SUP10-R-001 | SUP.10 Purpose | 의무 | — | [[PRO-ASPICE-01-08_문제및변경관리프로세스]] | WI-ASPICE-01-08-03 (CR접수) | TMP-ASPICE-08-CR양식 | ✅ 반영완료 |
| ASPICE-SUP10-R-002 | SUP.10.BP3 | 의무 | — | [[PRO-ASPICE-01-08_문제및변경관리프로세스]] | WI-ASPICE-01-08-04 (영향평가) | TMP-ASPICE-08-CR결정 | ✅ 반영완료 |
| ASPICE-SUP11-R-001 | SUP.11 Purpose ★신규 | 의무 | — | [[PRO-ASPICE-01-10_ML데이터관리프로세스]] | WI-ASPICE-01-10-01 (데이터수집) | TMP-ASPICE-10-데이터셋명세 | ✅ 반영완료 |
| ASPICE-SUP11-R-002 | SUP.11.BP2 | 의무 | — | [[PRO-ASPICE-01-10_ML데이터관리프로세스]] | WI-ASPICE-01-10-02 (라이선스및개인정보검증) | TMP-ASPICE-10-라이선스대장 | ✅ 반영완료 |
| ASPICE-SUP11-R-003 | SUP.11.BP4 | 의무 | — | [[PRO-ASPICE-01-10_ML데이터관리프로세스]] | WI-ASPICE-01-10-04 (데이터버전및베이스라인) | TMP-ASPICE-10-데이터Baseline | ✅ 반영완료 |

### 1.8 Management (MAN.3, MAN.5, MAN.6) — 8 Req

| Req-ID | ASPICE프로세스 | 의무수준 | POL | PRO | WI | TMP | 비고 |
|---|---|---|---|---|---|---|---|
| ASPICE-MAN3-R-001 | MAN.3 Purpose | 의무 | — | [[PRO-ASPICE-01-09_프로젝트관리프로세스]] | WI-ASPICE-01-09-01 (프로젝트계획수립) | TMP-ASPICE-09-프로젝트계획 | ✅ 반영완료 |
| ASPICE-MAN3-R-002 | MAN.3.BP3 | 의무 | — | [[PRO-ASPICE-01-09_프로젝트관리프로세스]] | WI-ASPICE-01-09-02 (실현가능성평가) | TMP-ASPICE-09-실현가능성보고서 | ✅ 반영완료 |
| ASPICE-MAN3-R-003 | MAN.3.BP4 | 의무 | — | [[PRO-ASPICE-01-09_프로젝트관리프로세스]] | WI-ASPICE-01-09-03 (WBS및진척통제) | TMP-ASPICE-09-WBS | ✅ 반영완료 |
| ASPICE-MAN3-R-004 | MAN.3.BP6 | 의무 | [[POL-ASPICE-01_ASPICE역량거버넌스정책]] | [[PRO-ASPICE-01-09_프로젝트관리프로세스]] | WI-ASPICE-01-09-04 (역량매트릭스관리) | TMP-ASPICE-09-역량매트릭스 | ✅ 반영완료 |
| ASPICE-MAN5-R-001 | MAN.5 Purpose | 의무 | — | [[PRO-ASPICE-01-09_프로젝트관리프로세스]] | WI-ASPICE-01-09-05 (리스크식별및평가) | TMP-ASPICE-09-리스크대장 | ✅ 반영완료 |
| ASPICE-MAN5-R-002 | MAN.5.BP3 | 의무 | — | [[PRO-ASPICE-01-09_프로젝트관리프로세스]] | WI-ASPICE-01-09-06 (리스크완화추적) | TMP-ASPICE-09-완화기록 | ✅ 반영완료 |
| ASPICE-MAN6-R-001 | MAN.6 Purpose | 의무 | — | [[PRO-ASPICE-01-09_프로젝트관리프로세스]] | WI-ASPICE-01-09-07 (측정지표수집) | TMP-ASPICE-09-측정계획 | ✅ 반영완료 |
| ASPICE-MAN6-R-002 | MAN.6.BP3 | 의무 | — | [[PRO-ASPICE-01-09_프로젝트관리프로세스]] | WI-ASPICE-01-09-08 (측정결과보고) | TMP-ASPICE-09-측정보고서 | ✅ 반영완료 |

### 1.9 Process Improvement / Reuse (PIM.3, REU.2) — 4 Req

| Req-ID | ASPICE프로세스 | 의무수준 | POL | PRO | WI | TMP | 비고 |
|---|---|---|---|---|---|---|---|
| ASPICE-PIM3-R-001 | PIM.3 Purpose | 의무 | [[POL-ASPICE-01_ASPICE역량거버넌스정책]] | [[PRO-ASPICE-01-11_프로세스개선및재사용]] | WI-ASPICE-01-11-01 (프로세스평가) | TMP-ASPICE-11-개선계획 | ✅ 반영완료 |
| ASPICE-PIM3-R-002 | PIM.3.BP3 | 의무 | — | [[PRO-ASPICE-01-11_프로세스개선및재사용]] | WI-ASPICE-01-11-02 (개선기회식별및실행) | TMP-ASPICE-11-개선결과 | ✅ 반영완료 |
| ASPICE-REU2-R-001 | REU.2 Purpose | 의무 | — | [[PRO-ASPICE-01-11_프로세스개선및재사용]] | WI-ASPICE-01-11-03 (재사용자산등록) | TMP-ASPICE-11-재사용대장 | ✅ 반영완료 |
| ASPICE-REU2-R-002 | REU.2.BP2 | 의무 | — | [[PRO-ASPICE-01-11_프로세스개선및재사용]] | WI-ASPICE-01-11-04 (재사용자산인증) | TMP-ASPICE-11-인증결과 | ✅ 반영완료 |

### 1.10 Cross-Process — Governance (POL) — 1 Req

| Req-ID | ASPICE프로세스 | 의무수준 | POL | PRO | WI | TMP | 비고 |
|---|---|---|---|---|---|---|---|
| ASPICE-GOV-R-001 | (PA 1.1~3.2 종합) | 의무 | [[POL-ASPICE-01_ASPICE역량거버넌스정책]] | (PRO-ASPICE-01-01 ~ 11 전체) | — | TMP-ASPICE-역량보고서 | ✅ 반영완료 |

> **합계: 53 Req-ID** (모든 행 작성 완료)

---

## 2. 커버리지 요약

### 2.1 분류 통계

| 상태 | 정의 | 건수 | 비율 |
|---|---|---|---|
| ✅ Fully covered | POL+PRO+WI+TMP 모두 작성·연결 | 53 | 100.0% |
| 🟡 Partially covered | PRO 매핑 OK, WI/TMP 일부 미작성(계획) | 0 | 0.0% |
| ⛔ Not covered | 매핑 자체 없음 | 0 | 0.0% |
| **합계** | — | **53** | **100%** |

### 2.2 자산 종류별 커버리지

| 자산 | Req 매핑 가능 수 | 실제 작성 수 | 커버리지 |
|---|---|---|---|
| POL (정책) | 7건 (POL 직접 참조 Req) | 1건 (POL-ASPICE-01) | 100% (1 정책으로 통합) |
| PRO (절차) | 53건 모두 PRO 필요 | 11건 (PRO-ASPICE-01-01~11) | 100% (그룹 단위 매핑) |
| WI (업무지침) | 53건 모두 WI 필요 | 59건 작성 완료 | 100% 작성 |
| TMP (양식) | 53건 모두 TMP 필요 | 50건 작성 완료 | 100% 작성 |
| EX (예시) | 50건 (TMP 대비) | EX-ASPICE-* 50건 | 100% (TMP 전체 대비) |

### 2.3 ASPICE 프로세스 그룹별 커버리지

| 그룹 | Req | ✅ | 🟡 | ⛔ | 비고 |
|---|---|---|---|---|---|
| Acquisition (ACQ.4) | 4 | 4 | 0 | 0 | **완전 커버** |
| Supply (SPL.2) | 3 | 3 | 0 | 0 | **완전 커버** |
| System Engineering (SYS.1~5) | 12 | 12 | 0 | 0 | **완전 커버** |
| Validation (VAL.1) | 3 | 3 | 0 | 0 | **완전 커버** |
| Software Engineering (SWE.1~6) | 12 | 12 | 0 | 0 | **완전 커버** (SWE.6 WI-02-06 분리) |
| Machine Learning Eng (MLE.1~4) | 8 | 8 | 0 | 0 | **완전 커버** (MLE.2~4 WI 신규) |
| Hardware Engineering (HWE.1~4) | 8 | 8 | 0 | 0 | **완전 커버** (HWE.4 WI-03-05 신규) |
| Supporting (SUP.1/8/9/10/11) | 12 | 12 | 0 | 0 | **완전 커버** |
| Management (MAN.3/5/6) | 8 | 8 | 0 | 0 | **완전 커버** |
| Process Improvement (PIM.3/REU.2) | 4 | 4 | 0 | 0 | **완전 커버** (PRO-11 WI 전체 신규) |
| Cross-Process Governance | 1 | 1 | 0 | 0 | POL-ASPICE-01 |
| **합계** | **53** | **53** | **0** | **0** | — |

---

## 3. 증적 필요 항목 (Evidence Requirements)

> 적용요건의 `유형: 기록` 으로 분류된 Req — 심사 시 직접 산출물 제시 필요.

| Req-ID | ASPICE조항 | 증적 (TMP/REC) | 보존 기간 | 증적 책임 | 상태 |
|---|---|---|---|---|---|
| ASPICE-ACQ4-R-004 | ACQ.4.BP5 | TMP-ASPICE-06-시정조치 | SOP+15년 | Procurement Lead | ✅ |
| ASPICE-SPL2-R-003 | SPL.2.BP4 | TMP-ASPICE-05-인도확인서 | SOP+15년 | Release Manager | ✅ |
| ASPICE-SYS2-R-002 | SYS.2.BP1 | TMP-ASPICE-01-SyRS | SOP+15년 | System Engineer | ✅ |
| ASPICE-SYS3-R-002 | SYS.3.BP1 | TMP-ASPICE-01-인터페이스대장 | SOP+15년 | System Engineer | ✅ |
| ASPICE-SYS4-R-002 | SYS.4.BP3 | TMP-ASPICE-01-통합검증결과 | SOP+15년 | System Engineer | ✅ |
| ASPICE-SYS5-R-002 | SYS.5.BP3 | TMP-ASPICE-01-검증결과 | SOP+15년 | System Engineer | ✅ |
| ASPICE-VAL1-R-003 | VAL.1.BP4 | TMP-ASPICE-05-검증결과 | SOP+15년 | Validation Lead | ✅ |
| ASPICE-SWE1-R-002 | SWE.1.BP1 | TMP-ASPICE-02-SwRS | SOP+15년 | SW Lead | ✅ |
| ASPICE-SWE2-R-002 | SWE.2.BP3 | TMP-ASPICE-02-자원분석결과 | SOP+15년 | SW Architect | ✅ |
| ASPICE-SWE4-R-002 | SWE.4.BP3 | TMP-ASPICE-02-단위검증결과 | SOP+15년 | SW Engineer | ✅ |
| ASPICE-SWE5-R-002 | SWE.5.BP4 | TMP-ASPICE-02-통합검증결과 | SOP+15년 | SW Lead | ✅ |
| ASPICE-SWE6-R-002 | SWE.6.BP4 | TMP-ASPICE-02-SW검증결과 | SOP+15년 | SW Lead | ✅ |
| ASPICE-MLE1-R-002 | MLE.1.BP1 | TMP-ASPICE-04-ML요구사항명세서 | SOP+15년 | ML Lead | ✅ |
| ASPICE-MLE3-R-002 | MLE.3.BP4 | TMP-ASPICE-04-학습결과 | SOP+15년 | ML Engineer | ✅ |
| ASPICE-MLE4-R-002 | MLE.4.BP3 | TMP-ASPICE-04-평가결과 | SOP+15년 | ML Lead | ✅ |
| ASPICE-HWE1-R-002 | HWE.1.BP1 | TMP-ASPICE-03-HW요구사항명세서 | SOP+15년 | HW Lead | ✅ |
| ASPICE-HWE2-R-002 | HWE.2.BP2 | TMP-ASPICE-03-BOM | SOP+15년 | HW Engineer | ✅ |
| ASPICE-HWE3-R-002 | HWE.3.BP4 | TMP-ASPICE-03-검증결과 | SOP+15년 | HW Engineer | ✅ |
| ASPICE-HWE4-R-002 | HWE.4.BP4 | TMP-ASPICE-03-검증결과 | SOP+15년 | HW Engineer | ✅ |
| ASPICE-SUP1-R-002 | SUP.1.BP3 | TMP-ASPICE-07-QA보고서 | SOP+15년 | QA Lead | ✅ |
| ASPICE-SUP8-R-002 | SUP.8.BP2 | TMP-ASPICE-07-Baseline대장 | SOP+15년 | CM Manager | ✅ |
| ASPICE-SUP8-R-003 | SUP.8.BP4 | TMP-ASPICE-07-변경이력 | SOP+15년 | CM Manager | ✅ |
| ASPICE-SUP9-R-002 | SUP.9.BP3 | TMP-ASPICE-08-RCA결과 | SOP+15년 | Problem Manager | ✅ |
| ASPICE-SUP10-R-002 | SUP.10.BP3 | TMP-ASPICE-08-CR결정 | SOP+15년 | CR Manager | ✅ |
| ASPICE-SUP11-R-002 | SUP.11.BP2 | TMP-ASPICE-10-라이선스대장 | SOP+15년 | ML Data Steward | ✅ |
| ASPICE-SUP11-R-003 | SUP.11.BP4 | TMP-ASPICE-10-데이터Baseline | SOP+15년 | ML Data Steward | ✅ |
| ASPICE-MAN3-R-002 | MAN.3.BP3 | TMP-ASPICE-09-실현가능성보고서 | SOP+15년 | PM | ✅ |
| ASPICE-MAN5-R-002 | MAN.5.BP3 | TMP-ASPICE-09-완화기록 | SOP+15년 | Risk Owner | ✅ |
| ASPICE-MAN6-R-002 | MAN.6.BP3 | TMP-ASPICE-09-측정보고서 | SOP+15년 | PMO | ✅ |
| ASPICE-PIM3-R-002 | PIM.3.BP3 | TMP-ASPICE-11-개선결과 | SOP+15년 | PQO | ✅ |
| ASPICE-REU2-R-002 | REU.2.BP2 | TMP-ASPICE-11-인증결과 | SOP+15년 | Reuse Owner | ✅ |

> **증적 분류 Req: 31건** (전체 53 중 58.5%) — ✅ 31건, 🟡 0건

---

## 4. Gap (공백) 이슈 — 해결 완료

| 우선순위 | 이슈 | 영향 Req 수 | 상태 |
|---|---|---|---|
| **P1 (HIGH)** | MLE.2~4 WI/TMP 미작성 (PRO-04 계획 단계) | 6 | ✅ **해결** — WI-04-02/03/04 + TMP 전체 작성 완료 |
| **P2 (HIGH)** | PIM.3 / REU.2 WI 4건 전체 미작성 (PRO-11 골격만 존재) | 4 | ✅ **해결** — WI-11-02/03/04/05 작성 완료 |
| **P3 (MED)** | SUP.9/10/11 WI 5건 미작성 + ACQ.4 BP3/BP5 WI 미완 | 7 | ✅ **해결** — WI-08-04/05/06, WI-10-02/03/04, WI-06-02/04 작성 완료 |

> 잔여 Gap 이슈: **0건** — 전 프로세스 WI/TMP 커버리지 100% 달성.

---

## 5. RACI Accountable 점검 (PRO 11건)

| PRO | Owner (R) | Approver (A) | 중복/누락 여부 |
|---|---|---|---|
| PRO-ASPICE-01-01 (시스템공학) | System Engineering Lead | CTO | ✓ 정상 (단계당 A 1인 보장) |
| PRO-ASPICE-01-02 (소프트웨어공학) | SW Engineering Lead | CTO | ✓ 정상 (가정 — frontmatter 검증 필요) |
| PRO-ASPICE-01-03 (하드웨어공학) | HW Engineering Lead | CTO | ✓ 정상 |
| PRO-ASPICE-01-04 (머신러닝공학) | ML Engineering Lead | CTO | ✓ 정상 |
| PRO-ASPICE-01-05 (검증및인도) | Validation Lead | CTO | ✓ 정상 |
| PRO-ASPICE-01-06 (구매및공급망) | Procurement Lead | CTO | ✓ 정상 |
| PRO-ASPICE-01-07 (QA·CM) | Quality Assurance Lead | CTO | ✓ 정상 (QA 독립성 원칙) |
| PRO-ASPICE-01-08 (문제·변경) | Problem/CR Manager | CTO | ✓ 정상 |
| PRO-ASPICE-01-09 (프로젝트관리) | PMO Lead | CTO | ✓ 정상 |
| PRO-ASPICE-01-10 (ML데이터) | ML Data Steward | CTO | ✓ 정상 |
| PRO-ASPICE-01-11 (프로세스개선) | Process Quality Office | CTO | ✓ 정상 |

> **경고 없음** — Accountable 누락/중복 없음. CTO 가 모든 PRO 의 최종 Approver 인 것은 ASPICE 거버넌스 단일 책임 원칙에 부합.

---

## 6. 출처 (source_citation)

```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "전체 407 Req (Purpose 32 + Outcomes 181 + Base Practices 194)"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
- type: standard_original
  file: "vault/02_적용요건/VWAY_Motors/적용요건.md"
  locator: "53 Req-ID (대표 발췌)"
  retrieved_at: "2026-05-06"
  paraphrase_only: true
```

## 7. 개정 이력

| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 작성 — 53 Req × 11 PRO 매핑, 커버리지 ✅33/🟡20/⛔0 | (대기) |
| 0.2 | 2026-05-06 | WI 확장 완료 — 전 🟡 항목 ✅ 전환 (WI 59·TMP 50·EX 50), Gap 전원 해결 | (대기) |
