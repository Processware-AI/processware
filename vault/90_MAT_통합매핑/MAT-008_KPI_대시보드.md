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
  total_standards: 1
  total_rounds: 1                  # 누적 측정 회차 (모든 표준 합)
  total_kpis_tracked: 11           # 정의 6 + 메타 5
  alerts_current: 4                # 모든 표준 현재 회차 critical+watch 합
---

# MAT-008 KPI 대시보드

> 차원 3 (Check) `/audit --kpi` 하네스가 자동 갱신하는 정량 지표 대시보드. 자동 갱신 — 사람이 직접 수정 금지.
>
> **상위 인덱스**: [[MAT-005_심사증적_인덱스]] §"심사 이력" / [[MAT-006_NCR_관리대장]]
> **운영 가이드**: `표준_프로세스_심사_가이드.md` §6.3 KPI 대시보드 / §11 트러블슈팅

## 1. 워크플로우

```
[/audit --kpi start <표준코드> --period <from..to>]
   ├ kpi-collector → kpi_data.yaml (PRO/WI §KPI 추출 + REC/MAT 측정)
   └ kpi-analyzer → 임계 비교·회귀 판정·MAT-008 갱신·MAT-006 §통계 갱신

[정기 운영 (분기·반기 권장)]
   └ 표준별 회차 N → N+1 측정 시 baseline 자동 비교 (직전 회차 대비 회귀 탐지)

[차원 4 인계 (Phase 4 자동화 예정)]
   └ verdict: critical 인 KPI 의 root cause → 차원 4 입력 큐
```

## 2. Verdict 4-tier

| 표시 | verdict | 조건 |
|---|---|---|
| 🟢 | healthy | 목표 충족 + 추세 stable/improved |
| 🟡 | watch | 목표 충족 + 추세 regressed (목표 충족이나 하락 중) |
| 🟠 | recovering | 목표 미달 + 추세 improved |
| 🔴 | critical | 목표 미달 + 추세 stable/regressed |
| ⚪ | data_gap | 측정 불가 (sample_size==0 또는 baseline 부재로 1회차 seed 등) |

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
- 회귀 임계 default: `±5.0%p` (방향성 휴리스틱은 `direction: higher_is_better / lower_is_better`).
- 사용자 지정: `/audit --kpi start ... --regression-threshold-pp 3.0`

---

## CMMI-DEV-ML3

> 차원 3 KPI 측정 시계열. `/audit --kpi` 가 자동 갱신. 회차별 KPI 1행 누적.

### 회차 시계열

| 회차 | 측정 기간 | 측정일 | KPI ID | KPI 명 | 카테고리 | 목표 | 측정값 | 단위 | verdict | baseline | delta | trace |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-01-01..2026-04-30 | 2026-05-02 | KPI-CMMI-04-01-01 | 감사 계획 준수율 | compliance | >=95% | — | % | ⚪ data_gap | — (seed) | — | run-k4f8d2a1 |
| 1 | 2026-01-01..2026-04-30 | 2026-05-02 | KPI-CMMI-04-01-02 | 부적합 종결율 | defect | >=95% | 0.0 | % | 🔴 critical | — (seed) | — | run-k4f8d2a1 |
| 1 | 2026-01-01..2026-04-30 | 2026-05-02 | KPI-CMMI-04-01-03 | 부적합 평균 종결 기간 | defect | <=20영업일 | — | 영업일 | ⚪ data_gap | — (seed) | — | run-k4f8d2a1 |
| 1 | 2026-01-01..2026-04-30 | 2026-05-02 | KPI-CMMI-04-01-04 | QA 독립성 점검 | independence | =100% | 100.0 | % | 🟢 healthy | — (seed) | — | run-k4f8d2a1 |
| 1 | 2026-01-01..2026-04-30 | 2026-05-02 | KPI-CMMI-04-01-05 | 동일 부적합 재발률 | defect | <10% | — | % | ⚪ data_gap | — (seed) | — | run-k4f8d2a1 |
| 1 | 2026-01-01..2026-04-30 | 2026-05-02 | KPI-WI-04-01-03-01 | 산출물 품질 점수 | quality | >=4.0 | 4.92 | 점/5.0 | 🟢 healthy | — (seed) | — | run-k4f8d2a1 |
| 1 | 2026-01-01..2026-04-30 | 2026-05-02 | META-COVERAGE | 심사 Coverage (WI) | compliance | >=80% | 40.0 | % | 🔴 critical | — (seed) | — | run-k4f8d2a1 |
| 1 | 2026-01-01..2026-04-30 | 2026-05-02 | META-FINDINGS-DENSITY | Findings 밀도 | defect | <=20% | 33.3 | % | 🔴 critical | — (seed) | — | run-k4f8d2a1 |
| 1 | 2026-01-01..2026-04-30 | 2026-05-02 | META-INDEPENDENCE | 독립성 통과율 | independence | =100% | 100.0 | % | 🟢 healthy | — (seed) | — | run-k4f8d2a1 |
| 1 | 2026-01-01..2026-04-30 | 2026-05-02 | META-NCR-CLOSURE | NCR 종결율 (전사) | defect | >=95% | 0.0 | % | 🔴 critical | — (seed) | — | run-k4f8d2a1 |
| 1 | 2026-01-01..2026-04-30 | 2026-05-02 | META-NCR-SLA | NCR SLA 준수율 | defect | >=90% | — | % | ⚪ data_gap | — (seed) | — | run-k4f8d2a1 |

### 회차 1 결과 요약 (2026-05-02, run-k4f8d2a1)

- **🟢 healthy**: 3건 (KPI-04-01-04 독립성 / KPI-WI-04-01-03-01 산출물 품질 / META-INDEPENDENCE)
- **🟡 watch**: 0건 (1회차 baseline seed 라 추세 비교 미수행)
- **🟠 recovering**: 0건
- **🔴 critical**: 4건 (KPI-04-01-02 종결율 / META-COVERAGE / META-FINDINGS-DENSITY / META-NCR-CLOSURE)
- **⚪ data_gap**: 4건 (KPI-04-01-01 감사 계획 준수율 / KPI-04-01-03 평균 종결 기간 / KPI-04-01-05 재발률 / META-NCR-SLA)
- 총 측정: 7건 / 정의된 KPI: 11건 (정의 6 + 메타 5)

### 회귀 알림 (current round 1)

> 1회차는 baseline seed 라 회귀 판정은 미수행. 본 회차의 critical 4건은 **임계 미달** 만으로 발생.

| KPI ID | KPI 명 | 측정값 / 목표 | verdict | 차원 4 (Act) 권고 |
|---|---|---|---|---|
| KPI-CMMI-04-01-02 | 부적합 종결율 | 0.0% / >=95% | 🔴 critical | NCR-001 (F-001) / NCR-002 (F-002) 종결 가속 — SLA 2026-05-30 |
| META-COVERAGE | 심사 Coverage (WI) | 40.0% / >=80% | 🔴 critical | WI-04-01-01 / WI-04-01-02 / WI-04-01-05 운영 시작 (REQ-003·REQ-006·REQ-011·REQ-012 not_assessed 해결) |
| META-FINDINGS-DENSITY | Findings 밀도 | 33.3% / <=20% | 🔴 critical | F-001~F-004 NCR 종결 + 차원 4 권고 §6 의 PRO/WI 개정으로 다음 분기 finding 감소 유도 |
| META-NCR-CLOSURE | NCR 종결율 (전사) | 0.0% / >=95% | 🔴 critical | KPI-04-01-02 와 동일 — NCR 4건 시정조치 종결 우선 |

### data_gap 분석 (회차 1)

| KPI ID | 데이터 부재 사유 | 측정 가능 시점 |
|---|---|---|
| KPI-CMMI-04-01-01 감사 계획 준수율 | 감사 계획서 REC 0건 (REQ-003 not_assessed) | WI-04-01-02 운영 시작 후 |
| KPI-CMMI-04-01-03 평균 종결 기간 | NCR 종결 0건 (n=0) | 첫 NCR 종결 후 |
| KPI-CMMI-04-01-05 재발률 | 1회차 — 재발 비교 baseline 부재 | 회차 ≥ 2 |
| META-NCR-SLA | NCR 종결 0건 (n=0) | 첫 NCR 종결 후 |

### 다음 회차 권고

- **회차 2 측정 시점**: 2026-Q3 (2026-07-01 ~ 09-30) 또는 NCR 일부 종결 후 임의 시점.
- **목표**: data_gap 4건 중 ≥ 2건 측정 가능 상태 도달 + critical 4건 중 ≥ 1건 recovering 으로 전환.
- **명령**: `/audit --kpi start CMMI-DEV-ML3 --period 2026-04-01..2026-06-30` (2회차 자동 baseline 비교).

---

> 본 대시보드는 자동 갱신됩니다. 직접 수정 시 차원 3 시계열 추적성이 손상되며, 다음 `/audit --kpi` 실행 시 검증 위반으로 처리됩니다.
