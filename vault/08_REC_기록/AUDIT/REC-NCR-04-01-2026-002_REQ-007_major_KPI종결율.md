---
type: REC
subtype: NCR
doc_id: "REC-NCR-04-01-2026-002"
title: "[NCR-002] 부적합 종결율 KPI 미달 (REQ-007)"
parent_audit: "[[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]]"
parent_pro: "[[PRO-CMMI-04-01_프로세스_품질보증_절차_v1.0]]"
parent_pol: "[[POL-CMMI-04_품질_구성_및_의사결정_정책_v1.0]]"
finding_id: F-002
req_id: REQ-007
req_source: PRO-CMMI-04-01
req_section: "§7 KPI — 부적합 종결율"
category: kpi
severity: major
status: open
issued_at: "2026-05-02T10:06:30+09:00"
issued_by: "audit-harness/ncr-drafter (claude-opus-4-7)"
auditor: "이감사"
audit_trace_id: "run-a1c2d3e4"
sla_due_date: "2026-07-01"
assignment:
  responsible_role: "QA"
  approver_role: "QMR"
  suggested: true
  responsible_name: null
  approver_name: null
evidence_refs:
  - rec_id: REC-CMMI-04-01-03-01-2026-001
    rec_path: "vault/08_REC_기록/REC-CMMI-04-01-03-01-2026-001_작업산출물_평가표.md"
  - rec_id: REC-CMMI-04-01-04-01-2026-002
    rec_path: "vault/08_REC_기록/REC-CMMI-04-01-04-01-2026-002_품질_이슈_에스컬레이션_REJECTED.md"
capa_rec: null
closed_at: null
closed_by: null
closed_reason: null
standards: ["CMMI-DEV-ML3"]
scope_code: "CMMI"
retention: "심사 종료 후 5년"
created: "2026-05-02"
tags: [REC, NCR, CMMI, PQA, F-002, major, kpi]
---

# [NCR-002] 부적합 종결율 KPI 미달 — 등급 Major

> 본 부적합은 차원 3 (Check) 자동 심사 결과로 발행되었으며, 심사원 **이감사** 의 확정 후 자동 작성되었습니다.
> 발행일: 2026-05-02 · 종결 기한: **2026-07-01** (SLA major 60일)
> 모(母) 심사 보고서: [[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]]
> 추적 ID: run-a1c2d3e4 / Finding F-002

## 1. 위반 요건
| 항목 | 내용 |
|---|---|
| Req ID | REQ-007 |
| 출처 | PRO-CMMI-04-01 §7 KPI 표 |
| 카테고리 | kpi |
| 요건 (paraphrase) | "부적합 종결율 ≥ 95% (분기 측정) 를 충족해야 한다." |

## 2. 부적합 사실 (관찰)

MAT-005 §실행기록 의 본 PRO 관련 REC 3건 중 final 2 (REC-...03-001, REC-...04-001) / rejected 1 (REC-...04-002).
종결 측정 가능한 부적합 row 2건 모두 종결 ❌:
- REC-CMMI-04-01-03-01-2026-001 §DoD: "부적합 종결 ❌ (재점검 2026-05-15 예정)"
- REC-CMMI-04-01-04-01-2026-002 §결재: "❌ 반려"

→ 종결 성공 0/2 = **0%** (목표 95% 대비 심각 미달).

## 3. 영향도 / 등급 판정

- **등급**: Major
- **근거**: 측정값은 KPI 목표 대비 명백 미달이나, 본 분기 첫 운영으로 표본 n=2 의 통계적 유의성 부족 → strict 모드였다면 nonconformant 였을 것이나 normal 에서는 partial → major. 다음 분기 표본이 n≥10 누적 시 동일 추세면 critical 격상 권고.
- **연계**: F-001 (종결 추적 미완료) 의 KPI 측정 결과 — F-001 의 시정이 본 NCR 종결의 직접 경로.

## 4. 시정조치 권고 (CAPA)

| # | 액션 | 책임자 | 기한 |
|---|---|---|---|
| 1 | F-001 (종결 추적) 시정조치 완료 — 본 KPI 의 root cause 처리 | QA | 2026-05-30 |
| 2 | 분기마다 KPI 측정 보고서를 REC 로 발행하도록 PRO §7 절차 명문화 (현재 "분기" 만 명시, 측정 산출물 부재) | Process Owner | 2026-06-30 |
| 3 | 다음 분기 (2026-Q3) KPI 재측정 — 표본 n≥10 확보 후 95% 충족 검증 | QA, QMR | 2026-09-30 (다음 심사) |

## 5. 종결 조건 (Definition of Closed)

| 항목 | 충족 기준 |
|---|---|
| 시정조치 완료 | F-001 종결 + PRO §7 KPI 측정 절차 명문화 (개정판 PRO) |
| 증적 첨부 | KPI 측정 REC 1건 이상 발행, 종결율 ≥ 95% 입증 |
| 책임자 종결 합의 | A 역할 (QMR) 의 종결 응답 |
| 종결 명령 | `/audit --close-ncr REC-NCR-04-01-2026-002 --capa <REC>` |

## 6. 추적성

| 단계 | 식별자 |
|---|---|
| 모(母) 심사 | [[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]] |
| Finding | F-002 (run-a1c2d3e4) |
| 위반 요건 | REQ-007 (PRO-CMMI-04-01 §7 KPI) |
| 연계 NCR | [[REC-NCR-04-01-2026-001_REQ-005_critical_종결추적]] (F-001 — root cause) |
| MAT-009 인덱스 | [[MAT-009_NCR_관리대장]] |
| 차원 4 인계 | (대기 — KPI 측정 절차 명문화 → /build-standard --from write 후보) |

## 7. 종결 기록

> ⏸ 미종결 (status: open) — 종결 시 자동 채워집니다.

---

> 본 NCR 은 자동 발행되었으며, 심사 증적 무결성을 위해 직접 수정하지 마십시오.
> 종결: `/audit --close-ncr REC-NCR-04-01-2026-002 --capa <REC>`
