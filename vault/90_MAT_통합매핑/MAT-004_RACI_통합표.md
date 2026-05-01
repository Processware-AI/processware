---
type: MAT
doc_id: MAT-004
title: RACI 통합표
version: "0.2"
owner: "QMR"
status: draft
created: 2026-04-16
updated: 2026-04-29
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
| PRO-QMS-101 | 경영검토 | A | — | — | — | R | — | I |
| **CMMI-DEV-ML3** | | | | | | | | |
| [[PRO-CMMI-01-01_거버넌스_운영_절차_v1.0]] | 거버넌스 운영(GOV) | **A** | R | C | C | — | — | I |
| [[PRO-CMMI-01-02_프로세스_자산_개발_절차_v1.0]] | OSSP·PAL 개발(PAD) | I | A | C | **R** | — | — | C |
| [[PRO-CMMI-01-03_프로세스_관리_및_개선_절차_v1.0]] | 프로세스 관리·개선(PCM) | I | A | C | **R** | — | — | C |
| [[PRO-CMMI-01-04_구현_인프라_운영_절차_v1.0]] | 구현 인프라(II) | I | A | C | **R** | — | C | C |
| [[PRO-CMMI-02-01_프로젝트_계획_절차_v1.0]] | 프로젝트 계획(PLAN) | I | C | C | C | **A** | R | I |
| [[PRO-CMMI-02-02_프로젝트_모니터링_및_통제_절차_v1.0]] | M&C(MC) | I | I | I | C | **A** | R | I |
| [[PRO-CMMI-02-03_추정_관리_절차_v1.0]] | 추정(EST) | I | I | I | C | **A** | R | I |
| [[PRO-CMMI-02-04_성과_및_측정_관리_절차_v1.0]] | 측정(MPM) | I | I | C | R | **A** | R | C |
| [[PRO-CMMI-02-05_리스크_및_기회_관리_절차_v1.0]] | 위험·기회(RSK) | I | C | C | C | **A** | R | I |
| [[PRO-CMMI-03-01_요구사항_개발_및_관리_절차_v1.0]] | 요구사항(RDM) | I | I | C | C | **A** | R | C |
| [[PRO-CMMI-03-02_기술솔루션_절차_v1.0]] | 기술솔루션(TS) | I | I | C | C | **A** | R | I |
| [[PRO-CMMI-03-03_제품통합_절차_v1.0]] | 제품통합(PI) | I | I | C | C | **A** | R | C |
| [[PRO-CMMI-03-04_검증_및_확인_절차_v1.0]] | 검증·확인(VV) | I | I | C | C | **A** | R | **R** |
| [[PRO-CMMI-03-05_동료검토_절차_v1.0]] | 동료검토(PR) | I | I | C | C | **A** | R | I |
| [[PRO-CMMI-04-01_프로세스_품질보증_절차_v1.0]] | PQA(PQA) | I | C | C | C | C | I | **A/R** |
| [[PRO-CMMI-04-02_형상관리_절차_v1.0]] | 형상관리(CM) | I | I | C | C | **A** | R | C |
| [[PRO-CMMI-04-03_근본원인분석_및_해결_절차_v1.0]] | 근본원인분석(CAR) | I | C | C | R | **A** | R | C |
| [[PRO-CMMI-04-04_의사결정_분석_및_해결_절차_v1.0]] | 의사결정 분석(DAR) | C | C | C | C | **A** | R | I |
| [[PRO-CMMI-05-01_조직_훈련_절차_v1.0]] | 조직 교육(OT) | I | A | C | R | — | — | C |
| [[PRO-CMMI-05-02_공급자_합의_관리_절차_v1.0]] | 공급자 합의(SAM) | I | C | C | C | **A** | R | C |

> 각 셀: R(Responsible), A(Accountable, 최대 1명), C(Consulted), I(Informed). 공란/— 은 무관여.
> 표기 단순화: 위 표는 PA 단위 대표 활동 1행. PRO 별 단계별 RACI 는 각 PRO §3 표 참조.

## WI Owner 분포 (142건 요약)

| 영역 | WI 건수 | 대표 Owner |
|---|---|---|
| 001 (GOV·PAD·PCM·II) | 24 | CEO·SEPG Lead |
| 002 (PLAN·MC·EST·MPM·RSK) | 36 | PM·SEPG |
| 003 (RDM·TS·PI·VV·PR) | 41 | RE·SE·SW Lead·V&V Lead |
| 004 (PQA·CM·CAR·DAR) | 26 | QA Lead·CM Lead·SEPG |
| 005 (OT·SAM) | 17 | HRD·구매팀 |

## 공백·중복 알림
- [x] ~~Accountable 이 누락된 PRO 목록~~ → 본 트레이스에서 20 PRO 모두 단일 Accountable 확인 (PQA 는 QA Lead 가 R 동시 담당)
- [x] ~~Accountable 2명 이상인 PRO~~ → 0건 (PQA-401 의 A/R 동시 표기는 QA Lead 1명에 대한 통합 표기로 단일 A 유지)
- [ ] PRO-201 PLAN 의 A=PO 와 PRO-202 MC 의 A=PO 가 동일 인물 가능성 — 대형 프로젝트에서는 분리 권고 (운영 단계 검토)
