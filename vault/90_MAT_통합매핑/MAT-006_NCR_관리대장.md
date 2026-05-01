---
type: MAT
doc_id: MAT-006
title: NCR (부적합) 관리대장
version: "0.1"
owner: "QMR"
status: draft
created: 2026-05-02
updated: 2026-05-02
retention: "심사 종료 후 5년"
tags: [MAT, ncr, audit-evidence]
---

# MAT-006 NCR 관리대장

> 차원 3 (Check) `/audit` 하네스 + `ncr-drafter` 가 자동 발행한 부적합(NCR) 의 전사 인덱스. 자동 갱신 — 사람이 직접 수정 금지.
>
> **상위 인덱스**: [[MAT-005_심사증적_인덱스]] §"심사 이력" — 모(母) 심사 보고서 추적.
> **개별 NCR 본문**: `vault/08_REC_기록/AUDIT/REC-NCR-*.md`
> **관련 운영 가이드**: `표준_프로세스_심사_가이드.md` §6.2 부적합 NCR / §11 트러블슈팅

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

[차원 4 인계 (Phase 4 자동화 예정)]
   └ NCR 의 시정조치 권고 → /build-standard --from write 재트리거
```

## 2. 식별번호 체계

- 패턴: `REC-NCR-{POL2}-{PRO2}-{YYYY}-{NNN}`
- 8종 문서유형 체계 유지 — REC sub-type NCR (구성원칙 위반 회피).
- 동일 (POL2, PRO2, YYYY) 내 NNN 중복 금지.
- 단일 audit 의 N finding 은 연속 일련번호 (001 → 002 → 003 → ...).

## 3. SLA 휴리스틱 (Phase 2 기본)

| 등급 | 종결 기한 | 근거 |
|---|---|---|
| **critical** | 발행일 + **20 영업일** | PRO-CMMI-04-01 §7 KPI "부적합 평균 종결 기간 ≤ 20영업일" 정합 |
| major | 발행일 + 60 일 | 일반 관행 |
| minor | 발행일 + 90 일 | 다음 분기 이전 종결 |

> 영업일 계산은 Phase 2 에서 단순 일수 근사 (KST 휴일 미반영). Phase 4 에서 정식 영업일 계산기 도입 권장.

## 4. R/A 책임자 휴리스틱 (Phase 2 자동 추정)

| Finding 카테고리 | R (Responsible) | A (Accountable) |
|---|---|---|
| raci, approval | PM | Process Owner |
| procedure, dod, output | QA | PM |
| kpi | QA | QMR |
| regulatory | Compliance Officer | CEO |
| exception | 발견자 | PM |

> 모든 추정에는 NCR frontmatter 의 `assignment.suggested: true` 가 명시됨. **실 책임자 지정은 사람의 결정**. Phase 4 에서 정식 RBAC 매핑.

## 5. 본 대장의 두 섹션 운영 규칙

- **§"NCR 발행 현황 (open)"** — `status in [open, in_progress]` 인 NCR 모두. 발행 시 자동 append.
- **§"NCR 종결 현황 (closed)"** — `status == closed` 인 NCR 모두. 종결 시 open 행 제거 → closed 행 append (이동).
- 행 순서: 발행 일자 오름차순 (최근이 아래).

---

## NCR 발행 현황 (open)

| NCR ID | Finding | 발행일 | 표준 | 출처 | Req | 등급 | 제목 (요약) | R/A | SLA 기한 | 상태 | 모(母) 심사 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [[REC-NCR-04-01-2026-001_REQ-005_critical_종결추적]] | F-001 | 2026-05-02 | CMMI-DEV-ML3 | PRO-CMMI-04-01 §5-6 | REQ-005 | critical | 종결 추적 미완료 | QA / PM | 2026-05-30 | open | [[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]] |
| [[REC-NCR-04-01-2026-002_REQ-007_major_KPI종결율]] | F-002 | 2026-05-02 | CMMI-DEV-ML3 | PRO-CMMI-04-01 §7 KPI | REQ-007 | major | 부적합 종결율 KPI 미달 | QA / QMR | 2026-07-01 | open | [[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]] |
| [[REC-NCR-04-01-2026-003_REQ-009_minor_평가서완전성]] | F-003 | 2026-05-02 | CMMI-DEV-ML3 | WI-CMMI-04-01-03 §4·§5.3 | REQ-009 | minor | 평가서 완전성 100% 미달 | QA / PM | 2026-07-31 | open | [[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]] |
| [[REC-NCR-04-01-2026-004_REQ-010_critical_다단계승인]] | F-004 | 2026-05-02 | CMMI-DEV-ML3 | WI-CMMI-04-01-04 §2·§5 | REQ-010 | critical | 다단계 승인 — Sponsor 단계 차단 | PM / Process Owner | 2026-05-30 | open | [[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]] |

## NCR 종결 현황 (closed)

| NCR ID | Finding | 발행일 | 종결일 | 표준 | 출처 | 등급 | 종결자 | CAPA REC | SLA 준수 |
|---|---|---|---|---|---|---|---|---|---|

## NCR 통계 (Phase 3 자동 갱신 예정)

> Phase 2 에서는 수동 — Phase 3 KPI 대시보드(MAT-008) 가 자동 갱신.

| 지표 | 값 |
|---|---|
| 총 발행 NCR (누적) | 4 |
| 종결 완료 (CAPA 첨부) | 0 |
| 미종결 (open) | 4 |
| 종결율 (= 종결 / 발행) | 0% |
| SLA 준수율 (= 기한 내 종결 / 종결 완료) | — (n=0) |
| 평균 종결 기간 (영업일) | — (n=0) |
| 등급별 누적 (critical / major / minor) | 2 / 1 / 1 |
| 반복 부적합 TOP (동일 PRO·Req 의 재발) | (Phase 3 자동 분석) |

---

> 본 대장은 자동 갱신됩니다. 직접 수정 시 차원 3 추적성이 손상되며, 다음 `/audit` 실행 시 검증 위반으로 처리됩니다.
