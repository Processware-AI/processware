---
type: MAT
doc_id: MAT-004
title: RACI 통합표
version: "0.2"
owner: "QMR"
status: draft
created: 2026-04-16
updated: 2026-05-06
retention: "상시"
tags: [MAT, raci]
---

# MAT-004 RACI 통합표

> 전사 PRO 별 책임 분담을 단일 표로 집계. 역할 중복·공백 탐지용.

## 역할 리스트
- 경영진(CEO/CISO/CPO 등)
- 프로세스 오너
- 담당자
- 내부심사팀
- 외부 이해관계자

## RACI 매트릭스

| PRO | 활동 | CEO | 경영진 | PCB | SEPG | PO | 담당 | QA |
|---|---|---|---|---|---|---|---|---|

## SPICE 영역 RACI (VWAY_Motors / Automotive SPICE 4.0)

> 11 PRO 의 핵심 활동 단위 RACI. 단계당 Accountable 1인 원칙.
> 역할 약어: **CTO** (Chief Tech Officer) / **PQO** (Process Quality Office) / **QA** (Quality Assurance Lead, SUP.1) / **CM** (Configuration Manager, SUP.8) / **PM** (Project Manager) / **SE** (System Engineer) / **SW** (Software Lead) / **HW** (Hardware Lead) / **ML** (ML Engineering Lead) / **VAL** (Validation Lead) / **PROC** (Procurement Lead) / **DEV** (개발팀 일반)

| PRO | 활동 | CEO | CTO | PQO | PM | QA | CM | SE | SW | HW | ML | VAL | PROC | DEV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PRO-SPICE-01-01 | SYS.1 이해관계자 요구사항 도출 | I | A | I | A | I | I | **R** | C | C | C | I | I | C |
| PRO-SPICE-01-01 | SYS.2 시스템 요구사항 분석 | I | A | C | A | C | I | **R** | C | C | C | I | I | C |
| PRO-SPICE-01-01 | SYS.3 시스템 아키텍처 설계 | I | A | C | A | C | I | **R** | C | C | C | I | I | C |
| PRO-SPICE-01-01 | SYS.4 시스템 통합 | I | A | C | A | C | C | **R** | C | C | C | I | I | C |
| PRO-SPICE-01-01 | SYS.5 시스템 검증 | I | A | C | I | **A(QA)** | I | **R** | C | C | C | C | I | C |
| PRO-SPICE-01-02 | SWE.1 SW 요구사항 분석 | I | A | C | A | C | I | C | **R** | I | I | I | I | C |
| PRO-SPICE-01-02 | SWE.2 SW 아키텍처 설계 | I | A | C | A | C | I | C | **R** | I | I | I | I | C |
| PRO-SPICE-01-02 | SWE.3 상세설계·단위구현 | I | A | C | A | I | I | I | **R** | I | I | I | I | **R** |
| PRO-SPICE-01-02 | SWE.4 단위 검증 | I | A | C | I | C | I | I | **R** | I | I | I | I | **R** |
| PRO-SPICE-01-02 | SWE.5/6 SW 통합·검증 | I | A | C | I | **A(QA)** | I | C | **R** | I | I | C | I | C |
| PRO-SPICE-01-03 | HWE.1 HW 요구사항 분석 | I | A | C | A | C | I | C | I | **R** | I | I | I | C |
| PRO-SPICE-01-03 | HWE.2 HW 설계 | I | A | C | A | C | I | C | I | **R** | I | I | C | C |
| PRO-SPICE-01-03 | HWE.3/4 HW 검증 | I | A | C | I | **A(QA)** | I | C | I | **R** | I | C | I | C |
| PRO-SPICE-01-04 | MLE.1 ML 요구사항 분석 | I | A | C | A | C | I | C | C | I | **R** | I | I | C |
| PRO-SPICE-01-04 | MLE.2 ML 아키텍처 설계 | I | A | C | A | C | I | C | C | I | **R** | I | I | C |
| PRO-SPICE-01-04 | MLE.3 ML 학습 | I | A | C | A | C | I | I | I | I | **R** | I | I | **R** |
| PRO-SPICE-01-04 | MLE.4 모델 테스트 | I | A | C | I | **A(QA)** | I | I | I | I | **R** | C | I | C |
| PRO-SPICE-01-05 | VAL.1 사용자 검증 | I | A | C | A | C | I | C | C | C | C | **R** | I | C |
| PRO-SPICE-01-05 | SPL.2 제품 릴리스·인도 | I | A | C | A | C | C | C | C | C | C | **R** | I | C |
| PRO-SPICE-01-06 | ACQ.4 공급사 모니터링 | I | A | I | A | C | I | I | C | C | I | I | **R** | C |
| PRO-SPICE-01-07 | SUP.1 QA 감사 | I | A | C | I | **R** | I | I | I | I | I | I | I | I |
| PRO-SPICE-01-07 | SUP.1.BP4 QA 에스컬레이션 | **A** | C | I | I | **R** | I | I | I | I | I | I | I | I |
| PRO-SPICE-01-07 | SUP.8 형상관리 (CM) | I | A | C | I | C | **R** | C | C | C | C | C | C | C |
| PRO-SPICE-01-08 | SUP.9 문제해결 | I | A | C | A | C | I | C | C | C | C | C | I | **R** |
| PRO-SPICE-01-08 | SUP.10 변경관리 (CR) | I | A | C | A | **A(QA)** | C | C | C | C | C | C | C | **R** |
| PRO-SPICE-01-09 | MAN.3 프로젝트 관리 | I | A | C | **R** | C | I | C | C | C | C | I | I | C |
| PRO-SPICE-01-09 | MAN.5 리스크 관리 | I | A | C | **R** | C | I | C | C | C | C | I | I | C |
| PRO-SPICE-01-09 | MAN.6 측정 | I | A | C | **R** | C | I | I | I | I | I | I | I | I |
| PRO-SPICE-01-10 | SUP.11 ML 데이터 관리 | I | A | C | A | C | C | I | I | I | **R** | I | I | C |
| PRO-SPICE-01-11 | PIM.3 프로세스 개선 | I | A | **R** | C | C | I | I | I | I | I | I | I | I |
| PRO-SPICE-01-11 | REU.2 재사용 자산 관리 | I | A | **R** | C | C | C | C | C | C | C | C | C | C |

> **검증 결과 (Accountable)**:
> - 단계당 Accountable 1인 보장: ✓ (단, SYS.5/SWE.5/HWE.3/MLE.4 검증 단계는 QA 가 A — ASPICE 독립성 원칙)
> - QA 에스컬레이션은 CEO 가 A — 독립 보고선 보장
> - CTO 가 모든 PRO 의 기본 A — 단일 기술 거버넌스 책임
> - **누락·중복 없음**

## 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-04-16 | 최초 작성 (빈 표) | (대기) |
| 0.2 | 2026-05-06 | VWAY_Motors / SPICE 영역 30개 활동 RACI 추가 | (대기) |
