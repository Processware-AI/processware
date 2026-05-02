---
type: MAT
doc_id: MAT-009
title: NCR (부적합) 관리대장
version: "0.1"
owner: "QMR"
status: draft
created: 2026-05-02
updated: 2026-05-02
retention: "심사 종료 후 5년"
tags: [MAT, ncr, audit-evidence]
---

# MAT-009 NCR 관리대장

> 차원 3 (Check) `/audit` 하네스 + `ncr-drafter` 가 자동 발행한 부적합(NCR) 의 전사 인덱스. 자동 갱신 — 사람이 직접 수정 금지.
>
> **상위 인덱스**: [[MAT-005_심사증적_인덱스]] §"심사 이력" — 모(母) 심사 보고서 추적.
> **개별 NCR 본문**: `vault/08_REC_기록/AUDIT/REC-NCR-*.md`
> **관련 운영 가이드**: `vault/09_REF_참고자료/표준_프로세스_심사_가이드.md` §6.2 부적합 NCR / §11 트러블슈팅

## 1. 워크플로우

```
[/audit --confirm <trace>]
   └ audit-reporter 위임
       └ ncr-drafter (issue 모드)
           ├ REC-NCR-*.md 1건/finding 발행
           └ §"NCR 발행 현황 (open)" 1행 append/finding

[시정조치 후]
[/audit --close-ncr <ncr_id> --capa <REC>]
   └ ncr-drafter (close 모드)
       ├ NCR frontmatter status: closed + capa_rec + closed_*
       ├ §"NCR 발행 현황 (open)" 행 제거
       └ §"NCR 종결 현황 (closed)" 1행 append
```

## 2. 식별번호 체계

- 패턴: `REC-NCR-{POL2}-{PRO2}-{YYYY}-{NNN}`
- 8종 문서유형 체계 유지 — REC sub-type NCR.
- 동일 (POL2, PRO2, YYYY) 내 NNN 중복 금지.
- 단일 audit 의 N finding 은 연속 일련번호 (001 → 002 → ...).

## 3. SLA 휴리스틱

| 등급 | 종결 기한 |
|---|---|
| **critical** | 발행일 + **20 영업일** |
| major | 발행일 + 60 일 |
| minor | 발행일 + 90 일 |

## 4. R/A 책임자 휴리스틱

| Finding 카테고리 | R (Responsible) | A (Accountable) |
|---|---|---|
| raci, approval | PM | Process Owner |
| procedure, dod, output | QA | PM |
| kpi | QA | QMR |
| regulatory | Compliance Officer | CEO |
| exception | 발견자 | PM |

## 5. 운영 규칙

- **§"NCR 발행 현황 (open)"** — `status in [open, in_progress]` 인 NCR. 발행 시 자동 append.
- **§"NCR 종결 현황 (closed)"** — `status == closed` 인 NCR. 종결 시 open 행 제거 → closed 행 append.
- 행 순서: 발행 일자 오름차순.

---

## NCR 발행 현황 (open)

| NCR ID | Finding | 발행일 | 표준 | 출처 | Req | 등급 | 제목 (요약) | R/A | SLA 기한 | 상태 | 모(母) 심사 |
|---|---|---|---|---|---|---|---|---|---|---|---|

## NCR 종결 현황 (closed)

| NCR ID | Finding | 발행일 | 종결일 | 표준 | 출처 | 등급 | 종결자 | CAPA REC | SLA 준수 |
|---|---|---|---|---|---|---|---|---|---|

## NCR 통계

> 본 섹션은 차원 3 Phase 3 의 `kpi-analyzer` 가 `/audit --kpi` 실행 시 자동 갱신. 직접 수정 금지.

| 지표 | 값 | source |
|---|---|---|
| 총 발행 NCR (누적) | 0 | — |
| 종결 완료 (CAPA 첨부) | 0 | — |
| 미종결 (open) | 0 | — |
| 종결율 | — | — |
| SLA 준수율 | — | — |
| 평균 종결 기간 | — | — |

---

> 본 대장은 자동 갱신됩니다. 직접 수정 시 차원 3 추적성이 손상됩니다.
