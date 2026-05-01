---
type: util-spec
title: 한국 영업일 계산기 — 정식 명세 (Phase 4.5)
version: "0.1"
owner: "QMR"
status: spec                            # spec → impl (Phase 4.5 실 구현 시) → validated
created: 2026-05-16
related_agents: [ncr-drafter, act-coordinator, kpi-collector]
related_kpis: ["KPI-CMMI-04-01-03 부적합 평균 종결 기간"]
---

# 한국 영업일 계산기 — 정식 명세 (Phase 4.5)

> Phase 4 까지의 휴리스틱 (28일 ≈ 20영업일) 을 KST 정식 영업일로 대체하는 정식 명세.
> 실 구현은 Phase 4.5 외부 인프라 연동 시점에. 본 명세는 인터페이스 + 알고리즘 정의만.

## 1. 적용 영역

- **ncr-drafter** Phase B-4 SLA 종결 기한 계산 (현재 critical 28일 / major 60일 / minor 90일 — 정식 영업일로 대체).
- **act-coordinator** Phase B 의 Phase 4 자동 알림 시점 (SLA 50% 경과 자동 알림).
- **kpi-collector** B-3 의 "평균 종결 기간 (영업일)" 측정 (현재 일수 × 5/7 근사 — 정식 영업일로 대체).
- **rec-writer** REC frontmatter 의 "보관기간" 영업일 환산.

## 2. 한국 공휴일 (2026 기준)

| 일자 | 공휴일 | 비고 |
|---|---|---|
| 2026-01-01 (목) | 신정 | |
| 2026-02-16 (월) | 설날 전날 | |
| 2026-02-17 (화) | 설날 | |
| 2026-02-18 (수) | 설날 다음날 | |
| 2026-03-02 (월) | 삼일절 (대체) | 3-1 일요일 → 월요일 대체 |
| 2026-05-05 (화) | 어린이날 | |
| 2026-05-24 (일) → 2026-05-25 (월) | 부처님오신날 (대체) | 5-24 일요일 → 월요일 대체 |
| 2026-06-06 (토) | 현충일 | (대체 없음 — 토요일 공휴일) |
| 2026-08-15 (토) | 광복절 | (대체 없음) |
| 2026-09-24 (목) | 추석 전날 | |
| 2026-09-25 (금) | 추석 | |
| 2026-09-26 (토) | 추석 다음날 | (대체 없음) |
| 2026-10-03 (토) | 개천절 | (대체 없음) |
| 2026-10-09 (금) | 한글날 | |
| 2026-12-25 (금) | 성탄절 | |

> 대체공휴일 규칙 (관공서공휴일 §3): 일요일이거나 공휴일 중복 시 다음 평일을 대체공휴일로. 토요일은 대체 없음.
> 임시공휴일 (선거·특별 지정) 은 별도 갱신.

## 3. 알고리즘 (의사 코드)

```python
from datetime import date, timedelta

KR_HOLIDAYS_2026 = {
    date(2026, 1, 1),
    date(2026, 2, 16), date(2026, 2, 17), date(2026, 2, 18),
    date(2026, 3, 2),                     # 3-1 → 3-2 대체
    date(2026, 5, 5),
    date(2026, 5, 25),                    # 부처님 5-24 → 5-25 대체
    date(2026, 6, 6),
    date(2026, 8, 15),
    date(2026, 9, 24), date(2026, 9, 25), date(2026, 9, 26),
    date(2026, 10, 3),
    date(2026, 10, 9),
    date(2026, 12, 25),
}

def is_business_day(d: date, holidays: set = KR_HOLIDAYS_2026) -> bool:
    """한국 영업일 (월~금 + 공휴일 아님)."""
    if d.weekday() >= 5:                  # 5=토 / 6=일
        return False
    if d in holidays:
        return False
    return True

def add_business_days(start: date, n: int, holidays: set = KR_HOLIDAYS_2026) -> date:
    """start 기준 n 영업일 후의 날짜.

    예: start=2026-05-02 (토) + 20 영업일 = 2026-05-29 (금).
        - 5/4 (월) 부터 영업일 1.
        - 5/5 (화) 어린이날 — skip.
        - 5/6~8 평일 (영업일 2/3/4).
        - 5/11~15 평일 (영업일 5/6/7/8/9).
        - ... 계속 ...
        - 5/29 (금) 영업일 20 도달.
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    current = start
    days_added = 0
    while days_added < n:
        current += timedelta(days=1)
        if is_business_day(current, holidays):
            days_added += 1
    return current

def diff_business_days(start: date, end: date, holidays: set = KR_HOLIDAYS_2026) -> int:
    """start ~ end 사이의 영업일 수 (양 끝 포함 안 함)."""
    if end < start:
        return -diff_business_days(end, start, holidays)
    count = 0
    current = start
    while current < end:
        current += timedelta(days=1)
        if is_business_day(current, holidays):
            count += 1
    return count
```

## 4. ncr-drafter 의 SLA 휴리스틱 → 정식 매핑

```python
# Phase 4 (현재 휴리스틱)
SLA_DAYS_HEURISTIC = { "critical": 28, "major": 60, "minor": 90 }   # 단순 일수
sla_due = issued_at + timedelta(days=SLA_DAYS_HEURISTIC[severity])

# Phase 4.5 (정식 영업일)
SLA_BIZ_DAYS = { "critical": 20, "major": 42, "minor": 63 }          # 영업일 (60일 ≈ 42 영업일, 90일 ≈ 63)
sla_due = add_business_days(issued_at.date(), SLA_BIZ_DAYS[severity])
```

> 휴리스틱 (28일) 과 정식 영업일 (20 영업일) 의 차이:
> - 2026-05-02 (토) + 28일 = 2026-05-30 (토) — 휴리스틱
> - 2026-05-02 + 20 영업일 = 2026-05-29 (금) — 정식 (1일 차이, 어린이날 1건 영향)
>
> Phase 4.5 도입 시 NCR-001 의 SLA 기한이 2026-05-30 → 2026-05-29 로 정정됨. 기존 데이터는 보존, 신규 NCR 부터 적용.

## 5. 자동 알림 시점 (Phase 4.5 act-coordinator hook)

```python
# 50% / 100% 자동 알림 (한국 영업일 기준)
sla_total_biz_days = SLA_BIZ_DAYS[severity]
elapsed_biz_days = diff_business_days(issued_at.date(), today)

if elapsed_biz_days >= sla_total_biz_days * 0.5 and not notified_50:
    notify_pm(ncr_id, level="50% SLA 경과")
    notified_50 = True

if elapsed_biz_days >= sla_total_biz_days and status not in ["closed", "in_progress"]:
    escalate_to_pcb(ncr_id, level="SLA 경과 — 에스컬레이션 필요")
```

## 6. 검증

| 입력 | 휴리스틱 결과 | 정식 영업일 결과 | 일치? |
|---|---|---|---|
| 2026-05-02 + critical | 2026-05-30 (28일) | 2026-05-29 (20영업일) | -1일 |
| 2026-05-02 + major | 2026-07-01 (60일) | 2026-06-30 (42영업일) | -1일 |
| 2026-05-02 + minor | 2026-07-31 (90일) | 2026-08-04 (63영업일) | +4일 |
| NCR-001 종결 13 calendar days = 9 biz days (PoC kpi round 2) | n/a | 9 영업일 (5/2 토 → 5/15 금, 5/5 어린이날 1건) | ✅ |

## 7. 환경 의존성

- 한국 공휴일 데이터는 매년 갱신 필요 (관공서공휴일 + 임시공휴일).
- 갱신 절차: 매년 11월 다음년도 공휴일 확정 후 본 파일 §2 표 갱신 + git commit.
- 외부 데이터 소스: 한국천문연구원 API (`http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService`) 또는 행정안전부 공휴일 데이터.

## 8. Phase 로드맵

- Phase 4.5 (지금): 본 명세 정의. 휴리스틱 그대로 유지.
- Phase 4.5+ (실 구현): Python module `.claude/utils/business_days_kr.py` 작성 + ncr-drafter / act-coordinator / kpi-collector 가 import 사용.
- Phase 5 (외부 데이터): 한국천문연구원 API 연동 — 공휴일 데이터 자동 갱신.
