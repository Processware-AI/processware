---
type: REC
subtype: NCR
doc_id: "REC-NCR-04-01-2026-004"
title: "[NCR-004] 다단계 승인 — Sponsor 단계 차단 (REQ-010)"
parent_audit: "[[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]]"
parent_pro: "[[PRO-CMMI-04-01_프로세스_품질보증_절차_v1.0]]"
parent_pol: "[[POL-CMMI-04_품질_구성_및_의사결정_정책_v1.0]]"
finding_id: F-004
req_id: REQ-010
req_source: WI-CMMI-04-01-04
req_section: "§2 수행 주체 / §5 다단계 승인"
category: approval
severity: critical
status: open
issued_at: "2026-05-02T10:06:30+09:00"
issued_by: "audit-harness/ncr-drafter (claude-opus-4-7)"
auditor: "이감사"
audit_trace_id: "run-a1c2d3e4"
sla_due_date: "2026-05-30"
assignment:
  responsible_role: "PM"
  approver_role: "Process Owner"
  suggested: true
  responsible_name: null
  approver_name: null
evidence_refs:
  - rec_id: REC-CMMI-04-01-04-01-2026-002
    rec_path: "vault/08_REC_기록/REC-CMMI-04-01-04-01-2026-002_품질_이슈_에스컬레이션_REJECTED.md"
    trace_id: run-d8a3f6b7
capa_rec: null
closed_at: null
closed_by: null
closed_reason: null
standards: ["CMMI-DEV-ML3"]
scope_code: "CMMI"
retention: "심사 종료 후 5년"
created: "2026-05-02"
tags: [REC, NCR, CMMI, PQA, F-004, critical, approval]
---

# [NCR-004] 다단계 승인 — Sponsor 단계 차단 — 등급 Critical

> 본 부적합은 차원 3 (Check) 자동 심사 결과로 발행되었으며, 심사원 **이감사** 의 확정 후 자동 작성되었습니다.
> 발행일: 2026-05-02 · 종결 기한: **2026-05-30** (SLA critical 20 영업일)
> 모(母) 심사 보고서: [[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]]
> 추적 ID: run-a1c2d3e4 / Finding F-004

## 1. 위반 요건
| 항목 | 내용 |
|---|---|
| Req ID | REQ-010 |
| 출처 | WI-CMMI-04-01-04 §2 수행 주체 / §5 다단계 승인 |
| 카테고리 | approval |
| 요건 (paraphrase) | "WI-04-01-04 결재는 PM 검토 후 Sponsor 승인을 받아야 한다 (다단계)." |

## 2. 부적합 사실 (관찰)

[[REC-CMMI-04-01-04-01-2026-002_품질_이슈_에스컬레이션_REJECTED]] (run-d8a3f6b7):
- §결재: "❌ 반려 — 박상무 Sponsor (PM 단독 검토만, Sponsor 미참석)"
- state.yaml hitl.decision: rejected
- 반려 사유: SLA 미정의 + Sponsor 회의 미참석 (WI §7.1 결정 지연 분기 적용).

대조 증적 — 동일 WI 의 정상 trace:
- REC-CMMI-04-01-04-01-2026-001 (run-c5f8a9d2): PM → Sponsor 정상 다단계 승인. 절차 자체는 가능.

## 3. 영향도 / 등급 판정

- **등급**: Critical
- **근거**: 동일 WI 의 두 trace 가 정상 승인과 승인 차단을 모두 보여, 절차의 가능성은 입증되나 **재현성** 이 결여. Sponsor 회의 일정·SLA 미정의가 절차 종속성을 깨고 있음. ISO §9.2 독립 의사결정 원칙 관점에서도 보완 필요.
- **영향 범위**: WI-04-01-04 의 모든 향후 실행. 차원 2 의 다단계 HITL 흐름 자체의 재현성 위협.

## 4. 시정조치 권고 (CAPA)

| # | 액션 | 책임자 | 기한 |
|---|---|---|---|
| 1 | WI-04-01-04 §5.1.1 에 SLA 임계 기준 (Critical / Major / Minor 기간) 정식 정의 — REC-...04-002 자체에 시정조치 요청 1번으로 이미 기재 | Process Owner, PM | 2026-05-15 |
| 2 | Sponsor 결정 회의의 정기 운영 일정 확정 (월 1회 또는 이슈 발생 시 7일 이내) | Process Owner | 2026-05-22 |
| 3 | 위 1·2 완료 후 본 WI 재실행 (`/do WI-CMMI-04-01-04`) → 신규 REC 로 본 finding 종결 | QA, PM | 2026-05-30 |
| 4 | (차원 4 권고) 표준 자산 보완을 위한 부분 재실행 — `/build-standard CMMI-DEV-ML3 --from write --target WI-CMMI-04-01-04` | QMR | 2026-06-15 |

## 5. 종결 조건 (Definition of Closed)

| 항목 | 충족 기준 |
|---|---|
| 시정조치 완료 | WI 개정 (SLA 정의) + Sponsor 회의 일정 확정 + WI 재실행 정상 승인 |
| 증적 첨부 | 신규 REC (run-a + ID 신규) 발행 + WI v1.1 (개정판) doc_id |
| 책임자 종결 합의 | A 역할 (Process Owner) 의 종결 응답 |
| 종결 명령 | `/audit --close-ncr REC-NCR-04-01-2026-004 --capa <REC>` |

## 6. 추적성

| 단계 | 식별자 |
|---|---|
| 모(母) 심사 | [[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]] |
| Finding | F-004 (run-a1c2d3e4) |
| 위반 요건 | REQ-010 (WI-CMMI-04-01-04 §2·§5) |
| 증적 REC | REC-CMMI-04-01-04-01-2026-002 (반려) / REC-CMMI-04-01-04-01-2026-001 (정상 — 대조) |
| MAT-006 인덱스 | [[MAT-006_NCR_관리대장]] |
| 차원 4 인계 | WI-04-01-04 v1.1 개정 트리거 후보 (Phase 4 자동화 시 차원 4 큐) |

## 7. 종결 기록

> ⏸ 미종결 (status: open) — 종결 시 자동 채워집니다.

---

> 본 NCR 은 자동 발행되었으며, 심사 증적 무결성을 위해 직접 수정하지 마십시오.
> 종결: `/audit --close-ncr REC-NCR-04-01-2026-004 --capa <REC>`
