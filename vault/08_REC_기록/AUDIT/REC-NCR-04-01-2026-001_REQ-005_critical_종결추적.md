---
type: REC
subtype: NCR
doc_id: "REC-NCR-04-01-2026-001"
title: "[NCR-001] 종결 추적 미완료 (REQ-005)"
parent_audit: "[[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]]"
parent_pro: "[[PRO-CMMI-04-01_프로세스_품질보증_절차_v1.0]]"
parent_pol: "[[POL-CMMI-04_품질_구성_및_의사결정_정책_v1.0]]"
finding_id: F-001
req_id: REQ-005
req_source: PRO-CMMI-04-01
req_section: "§5-6 종결 추적"
category: procedure
severity: critical
status: closed
issued_at: "2026-05-02T10:06:30+09:00"
issued_by: "audit-harness/ncr-drafter (claude-opus-4-7)"
auditor: "이감사"
audit_trace_id: "run-a1c2d3e4"
sla_due_date: "2026-05-30"
assignment:
  responsible_role: "QA"
  approver_role: "PM"
  suggested: true
  responsible_name: "dongseok (QA)"
  approver_name: "박팀장 (PM)"
evidence_refs:
  - rec_id: REC-CMMI-04-01-03-01-2026-001
    rec_path: "vault/08_REC_기록/REC-CMMI-04-01-03-01-2026-001_작업산출물_평가표.md"
    trace_id: run-b7d4e3c5
  - rec_id: REC-CMMI-04-01-04-01-2026-002
    rec_path: "vault/08_REC_기록/REC-CMMI-04-01-04-01-2026-002_품질_이슈_에스컬레이션_REJECTED.md"
    trace_id: run-d8a3f6b7
capa_rec: "REC-CMMI-04-01-04-01-2026-003"
closed_at: "2026-05-15T14:55:00+09:00"
closed_by: "박팀장 (PM)"
closed_reason: "PRO-CMMI-04-01 v1.0 → v1.1 개정 완료 (§5-6 SLA + §7 측정 시점 정의). Sponsor 회의 정식 개최 후 WI-04-01-04 재실행 정상 승인 — REC-04-01-04-001-2026-003 발행. 본 시정 13일 만에 완료 (Major 60일 SLA 대비 47일 단축)."
act_trace: "run-c4f8a1b2"
revision_applied: "PRO-CMMI-04-01 v1.0 → v1.1"
standards: ["CMMI-DEV-ML3"]
scope_code: "CMMI"
retention: "심사 종료 후 5년"
created: "2026-05-02"
tags: [REC, NCR, CMMI, PQA, F-001, critical]
---

# [NCR-001] 종결 추적 미완료 — 등급 Critical

> 본 부적합은 차원 3 (Check) 자동 심사 결과로 발행되었으며, 심사원 **이감사** 의 확정 후 자동 작성되었습니다.
> 발행일: 2026-05-02 · 종결 기한: **2026-05-30** (SLA critical 20 영업일)
> 모(母) 심사 보고서: [[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]]
> 추적 ID: run-a1c2d3e4 / Finding F-001

## 1. 위반 요건
| 항목 | 내용 |
|---|---|
| Req ID | REQ-005 |
| 출처 | PRO-CMMI-04-01 §5-6 종결 추적 |
| 카테고리 | procedure |
| 요건 (paraphrase) | "식별된 부적합은 시정조치가 종결될 때까지 추적되어 종결 기록이 남아야 한다." |

## 2. 부적합 사실 (관찰)

본 PRO 의 핵심 통제 절차인 "종결 추적" 이 본 분기 두 trace 모두 미완료:

- [[REC-CMMI-04-01-03-01-2026-001_작업산출물_평가표]] (run-b7d4e3c5)
  - §(자동 추가) 완료 조건 충족 결과: "부적합 종결 ❌ (재점검 2026-05-15 예정)"
  - 본 심사 시점 (2026-05-02) 기준 종결 미완료, 후속 REC 미발행.
- [[REC-CMMI-04-01-04-01-2026-002_품질_이슈_에스컬레이션_REJECTED]] (run-d8a3f6b7)
  - §결재: "❌ 반려 (박상무 Sponsor)"
  - state.yaml hitl.decision: rejected
  - 종결 합의 ❌ — 시정조치 후 신규 REC 발행 필요한데 미발행.

## 3. 영향도 / 등급 판정

- **등급**: Critical
- **근거**: PRO §7 KPI "부적합 종결율 ≥ 95%" 와 "평균 종결 기간 ≤ 20영업일" 의 달성 가능성을 전제부터 차단함. 본 finding 은 F-002 (부적합 종결율 KPI) 의 root cause.
- **영향 범위**: PRO-CMMI-04-01 + 자식 WI-04-01-03 / WI-04-01-04. 다음 분기 KPI 회귀 위험 높음.

## 4. 시정조치 권고 (CAPA — Corrective Action Plan)

| # | 액션 | 책임자 | 기한 |
|---|---|---|---|
| 1 | REC-CMMI-04-01-03-01-2026-001 의 부적합 (설계서 §3.2 트레이서빌리티 매트릭스) 시정조치 → 후속 REC 발행 (재점검 약속 이행) | QA | 2026-05-15 |
| 2 | REC-CMMI-04-01-04-01-2026-002 의 SLA 미정의 + Sponsor 회의 미참석 시정 후 본 WI 재실행 → 신규 REC 발행 | QA, PM | 2026-05-22 |
| 3 | PRO §5-6 의 "종결 추적" 단계에 종결 기한 SLA 명시 (예: 발견 후 20영업일) 정합 — REQ-007 KPI 와 정합 | Process Owner | 2026-05-30 |

## 5. 종결 조건 (Definition of Closed)

| 항목 | 충족 기준 |
|---|---|
| 시정조치 완료 | 후속 REC (`/do {WI번호}` 또는 `/build-standard --from write`) 발행 |
| 증적 첨부 | 본 NCR 의 `capa_rec` 필드에 후속 REC doc_id 명시 |
| 책임자 종결 합의 | A 역할 (PM) 의 종결 응답 |
| 종결 명령 | `/audit --close-ncr REC-NCR-04-01-2026-001 --capa <REC>` |

## 6. 추적성

| 단계 | 식별자 |
|---|---|
| 모(母) 심사 | [[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]] |
| Finding | F-001 (run-a1c2d3e4) |
| 위반 요건 | REQ-005 (PRO-CMMI-04-01 §5-6) |
| 증적 REC | REC-CMMI-04-01-03-01-2026-001, REC-CMMI-04-01-04-01-2026-002 |
| MAT-006 인덱스 | [[MAT-006_NCR_관리대장]] §"NCR 발행 현황 (open)" |
| 차원 4 인계 | (대기 — Phase 4 자동화 시 차원 4 큐) |

## 7. 종결 기록 (closed)

| 항목 | 값 |
|---|---|
| 종결일시 | 2026-05-15 14:55 KST |
| 종결자 | 박팀장 (PM) |
| 시정조치 REC | [[REC-CMMI-04-01-04-01-2026-003_품질_이슈_에스컬레이션_시정]] |
| 적용 자산 개정 | PRO-CMMI-04-01 v1.0 → v1.1 (§5-6 SLA + §7 측정 시점) |
| 차원 4 trace | run-c4f8a1b2 |
| 종결 사유 | PRO 개정 후 Sponsor 회의 정식 개최 + WI-04-01-04 재실행 정상 다단계 승인 |
| **SLA 준수** | ✅ critical 20영업일 (2026-05-30) 대비 **15일 단축** (2026-05-15 종결) |

---

> 본 NCR 은 자동 발행되었으며, 심사 증적 무결성을 위해 직접 수정하지 마십시오.
> 종결: `/audit --close-ncr REC-NCR-04-01-2026-001 --capa <REC>`
