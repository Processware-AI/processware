---
type: MAT
doc_id: MAT-008
title: KPI 대시보드 (차원 3 정량 지표)
version: "0.1"
owner: "QMR"
status: draft
created: 2026-05-02
updated: 2026-05-02
retention: "심사 종료 후 5년"
tags: [MAT, kpi, audit-evidence, dashboard]
counts:
  total_standards: 0
  total_rounds: 0
  total_kpis_tracked: 0
  alerts_current: 0
  act_queues_pending: 0
  act_queues_in_progress: 0
  act_queues_done: 0
  act_queues_total: 0
---

# MAT-008 KPI 대시보드

> 차원 3 (Check) `/check-process --kpi` 하네스가 자동 갱신하는 정량 지표 대시보드. 자동 갱신 — 사람이 직접 수정 금지.
>
> **상위 인덱스**: [[MAT-005_심사증적_인덱스]] §"심사 이력" / [[MAT-009_NCR_관리대장]]
> **운영 가이드**: `vault/09_REF_참고자료/표준_프로세스_심사_가이드.md` §6.3 KPI 대시보드 / §11 트러블슈팅

## 1. 워크플로우

```
[/check-process --kpi start <표준코드> --period <from..to>]
   ├ kpi-collector → kpi_data.yaml (PRO/WI §KPI 추출 + REC/MAT 측정)
   └ kpi-analyzer → 임계 비교·회귀 판정·MAT-008 갱신·MAT-009 §통계 갱신

[정기 운영 (분기·반기 권장)]
   └ 표준별 회차 N → N+1 측정 시 baseline 자동 비교 (직전 회차 대비 회귀 탐지)

[차원 4 인계]
   └ verdict: critical 인 KPI 의 root cause → 차원 4 입력 큐
```

## 2. Verdict 4-tier

| 표시 | verdict | 조건 |
|---|---|---|
| 🟢 | healthy | 목표 충족 + 추세 stable/improved |
| 🟡 | watch | 목표 충족 + 추세 regressed |
| 🟠 | recovering | 목표 미달 + 추세 improved |
| 🔴 | critical | 목표 미달 + 추세 stable/regressed |
| ⚪ | data_gap | 측정 불가 (sample_size==0 또는 baseline 부재) |

## 3. KPI 정의 source

- **정의 KPI**: 각 PRO 의 §6 / §7 "통제점/KPI" 표 + WI 의 §9 "KPI" 표 자동 추출 (kpi-collector).
- **메타 KPI** (차원 3 자체):
  - `META-COVERAGE` 심사 Coverage (WI 단위) — target ≥ 80%
  - `META-FINDINGS-DENSITY` Findings 밀도 (finding/requirement) — target ≤ 20%
  - `META-INDEPENDENCE` 독립성 검증 통과율 — target = 100%
  - `META-NCR-CLOSURE` NCR 종결율 (전사) — target ≥ 95%
  - `META-NCR-SLA` NCR SLA 준수율 — target ≥ 90%

## 4. Baseline 운영 규칙

- 첫 측정 (회차 1) → baseline **seed** (회귀 비교 없음, 임계 비교만).
- 회차 ≥ 2 → 직전 회차의 같은 kpi_id 측정값을 baseline 으로 자동 사용.
- 회귀 임계 default: `±5.0%p`.
- 사용자 지정: `/check-process --kpi start ... --regression-threshold-pp 3.0`

---

> 표준 편입 후 `/check-process --kpi` 실행 시 표준별 섹션이 자동 append 됩니다.
