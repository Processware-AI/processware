---
type: MAT
doc_id: MAT-004
title: RACI 통합표
version: "0.1"
owner: "QMR"
status: draft
created: 2026-04-16
updated: 2026-04-16
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

---

## §MDCS. IEC 81001-5-1 (MDCS) PRO RACI

> 출처: 각 PRO frontmatter `owner`(R) / `reviewer`(C) / `approver`(A). 역할 약어: TM=경영책임자(Top Management) · PSGB=보안운영위원회 · PSO=보안책임자 · DEV=개발/실무팀.
> A(Accountable)=approver, R(Responsible)=owner, C(Consulted)=reviewer, I(Informed)=관련 실무자.

| PRO | 활동(절차) | TM | PSGB | PSO | DEV |
|---|---|---|---|---|---|
| PRO-MDCS-01-01 | 보안 거버넌스 및 일반요건 관리 | A | C | R | I |
| PRO-MDCS-01-02 | 보안 SW 개발 프로세스 | A | C | R | R |
| PRO-MDCS-01-03 | 보안 SW 유지보수 프로세스 | A | C | R | R |
| PRO-MDCS-01-04 | 보안 형상관리 프로세스 | A | C | R | R |
| PRO-MDCS-01-05 | 보안 문제해결 프로세스 | A | C | R | R |
| PRO-MDCS-01-06 | 과도기 헬스SW 관리 | A | C | R | R |
| PRO-MDCS-02-01 | 보안 리스크 관리 프로세스 | A | C | R | R |

### Accountable 무결성 점검
- **Accountable(A) 누락**: 없음 — 7개 PRO 전부 단일 A(경영책임자=TM) 보유. ✅
- **Accountable(A) 중복**: 없음 — 각 PRO 당 A 정확히 1개. ✅
- **Responsible(R) 보유**: 7개 PRO 전부 PSO(또는 PSO+DEV) 보유. ✅
- 경고: 없음.

## 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| v0.2 | 2026-06-18 | IEC 81001-5-1 (MDCS) §MDCS RACI 7개 PRO 추가 — Accountable 단일·무중복 확인 (traceability-mapper) | (초안) |
