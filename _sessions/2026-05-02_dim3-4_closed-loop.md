---
type: session-recap
session_date: 2026-05-02
session_id: 917321d8-a06b-4032-b48c-c0a5e29f795d
duration_estimate: "단일 세션 (집중 1일)"
participants: ["dongseok", "Claude Opus 4.7 (1M context)"]
git_commits_added: 9                             # 본 세션 시작 ~ 종료 (be900cc 머지 포함)
git_branch: main                                  # 머지 완료
github_repo: Processware-AI/STD_Process_Builder
final_main_head: 79efdc5                          # README 갱신 commit
tags: [session, dim3-check, dim4-act, closed-loop, ml3-ml5, retrospective]
---

# 세션 회고 — 차원 3 + 4 자동화 + 폐쇄 루프 PoC + 환경·성숙도 분석

> 본 문서는 2026-05-02 단일 세션의 작업·결정·산출물·회고를 시간 순으로 정리한 회고록입니다.
> 4차원 PDCA AI 자동화 (차원 3 Phase 1~4 + 차원 4 Phase 1~2 + Phase 4.5 명세) 를 main 에 통합·polish 하고 운영 환경·성숙도 한계를 진단한 마라톤 세션.

---

## 0. 세션 진입 컨텍스트

**시작 시점**: 차원 2 (Do) 사이클 종료 직후. `feat/process-execution-harness` 브랜치에 차원 2 Phase 1~4 + 2.5/3.5 17 commit 누적 + push 완료 (08222dd).

**미해결 항목**:
- 차원 3 (Check) 미설계 — `4차원PDCA.md §3 차원 3 "현황: 미설계"`
- 차원 4 (Act) 미설계 — `§3 차원 4 "현황: 미설계"`
- 4차원 PDCA 폐쇄 루프 미실증

**사용자 요청**: "차원 3 진행해" → 옵션 ABC 추천 후 즉시 진입 패턴 (사용자 선호 협업 스타일 — 추천 1수 채택 + 단계별 검증).

---

## 1. 차원 3 (Check) Phase 1 — Core MVP

**Phase 0 결정 락** (5종):
1. 슬래시: `/audit` (ISO 용어 정렬)
2. 산출 위치: `vault/08_REC_기록/AUDIT/` (REC sub-type, 8종 체계 유지)
3. 식별번호: `REC-AUDIT-{POL2}-{PRO2}-{회차2}-{YYYY}-{NNN}`
4. 첫 PoC: PRO-CMMI-04-01 PQA (차원 2 trace 2건 보유)
5. 독립성 강제: `/audit start` 진입 시 (조기 실패)

**구현** (commit `bcec212`):
- `.claude/commands/audit.md` (338줄, 7 진입 모드)
- `.claude/agents/audit-planner.md` (218줄, PRO/WI 요건 → audit_plan.yaml)
- `.claude/agents/evidence-collector.md` (206줄, REC + trace + MAT-005 인덱싱)
- `.claude/agents/compliance-checker.md` (255줄, 4-tier 판정 + finding_id)
- `.claude/agents/audit-reporter.md` (307줄, REC-AUDIT + MAT-005 §심사이력)
- `표준_프로세스_심사_가이드.md` (315줄)
- MAT-005 §심사 이력 헤더 일관화 (9컬럼) + 1행 append

**PoC 검증** (run-a1c2d3e4):
- 대상: PRO-CMMI-04-01 PQA + 자식 WI 5
- 기간: 2026-01-01..2026-04-30
- 심사원 "이감사" ≠ executed_by "dongseok" → 독립성 통과
- 요건 12 → conformant 4 / partial 2 / nonconformant 2 / not_assessed 4
- Findings 4건: F-001 critical (REQ-005 종결 추적), F-002 major (REQ-007 KPI 종결율), F-003 minor (REQ-009 평가서 95%), F-004 critical (REQ-010 다단계 승인)
- 산출 보고서: `vault/08_REC_기록/AUDIT/REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서.md`
- trace.jsonl 40 이벤트

**주요 결정**:
- REC sub-type AUDIT/NCR 도입 (8종 체계 유지)
- 독립성 가드는 Phase 1 inline → Phase 4 정식 분리 예약

---

## 2. 차원 3 Phase 2 — NCR 자동 발행

**Phase 0 결정 락** (5종):
1. NCR 식별번호: `REC-NCR-{POL2}-{PRO2}-{YYYY}-{NNN}`
2. 발행 시점: confirm 직후 자동 (option `--no-ncr` 보류)
3. SLA 휴리스틱: critical 20영업일 / major 60일 / minor 90일 (PRO §7 KPI 정합)
4. status flow: open → in_progress → closed
5. R/A 휴리스틱: 카테고리별 (raci/approval → PM/PO, procedure/dod/output → QA/PM, kpi → QA/QMR, regulatory → CO/CEO)

**구현** (commit `f9a9596`):
- `.claude/agents/ncr-drafter.md` (363줄, issue / close 2 모드)
- `vault/90_MAT_통합매핑/MAT-006_NCR_관리대장.md` (open/closed 두 섹션) — **나중에 MAT-009 로 재번호 (§11 참조)**
- /audit `--list-ncr` / `--close-ncr` / `--no-ncr` 모드 활성화
- audit-reporter Phase C-NCR 단계 신설 (ncr-drafter 위임 + frontmatter ncr_refs + §4 NCR 링크)

**PoC 확장** (run-a1c2d3e4):
- finding 4건 → NCR 4건 발행 (REC-NCR-04-01-2026-001~004)
- MAT-006 §발행 4행 append (critical 2 / major 1 / minor 1)
- REC-AUDIT 보고서 갱신 (ncr_refs + §4 NCR 링크 4줄)

**변경량**: +1192 / -58 / 12 파일 (5 신규).

---

## 3. 차원 3 Phase 3 — KPI 대시보드

**Phase 0 결정 락** (6종):
1. 슬래시: `/audit --kpi <subcommand>` (start/show/update/check-regressions)
2. KPI 정의 source: PRO/WI §KPI 표 (자동 추출) + 메타 KPI 5종
3. baseline: 1회차 = seed (회귀 비교 없음)
4. 회귀 임계: default ±5%p
5. 산출 위치: `vault/90_MAT_통합매핑/MAT-008_KPI_대시보드.md`
6. trace prefix: `run-k*` (audit run-a* 와 분리)

**구현** (commit `c8f885c`):
- `.claude/agents/kpi-collector.md` (262줄, PRO/WI §KPI + REC/MAT 측정)
- `.claude/agents/kpi-analyzer.md` (251줄, baseline·회귀·MAT-008 갱신 + MAT-006 §통계 hook)
- `vault/90_MAT_통합매핑/MAT-008_KPI_대시보드.md` (신규)
- /audit `--kpi` 모드 추가
- 4-tier verdict (healthy / watch / recovering / critical / data_gap)
- 메타 KPI 5종: COVERAGE / FINDINGS-DENSITY / INDEPENDENCE / NCR-CLOSURE / NCR-SLA

**PoC** (run-k4f8d2a1, CMMI-DEV-ML3, 2026-01-01..04-30):
- KPI 11건 추출·측정 (정의 6 + 메타 5)
- verdict: healthy 3 / critical 4 / data_gap 4 (baseline seed)
- critical: KPI-04-01-02 부적합 종결율 / META-COVERAGE / META-FINDINGS-DENSITY / META-NCR-CLOSURE
- data_gap: KPI-04-01-01 / KPI-04-01-03 / KPI-04-01-05 / META-NCR-SLA
- MAT-008 §"CMMI-DEV-ML3" 11행 append + Mermaid gantt + MAT-006 §통계 9 항목

**변경량**: +1159 / -38 / 9 파일 (6 신규).

---

## 4. 차원 3 Phase 4 — RBAC + act-trigger + 차원 4 인계

**Phase 0 결정 락** (6종):
1. independence-guard 정식 분리 (independence_check + rbac_check 2 모드)
2. RBAC 6 역할 (auditor / executor / process_owner / qmr / admin / viewer)
3. 차원 4 큐: `.claude/queues/act/queue-q{8자hex}.yaml`
4. act-trigger 발행 시점: confirm 직후 (audit-reporter 위임) + kpi-analyzer finalize 직후
5. 영업일 휴리스틱: ncr-drafter 28일 근사 유지 (정식 계산기는 가이드 부록 B 명세만)
6. 외부 보고서 양식 → Phase 4.5 분리

**구현** (commit `fb19ba2`):
- `.claude/agents/independence-guard.md` (186줄, Phase 1 inline → 정식 에이전트)
- `.claude/agents/act-trigger.md` (232줄, from_audit + from_kpi 2 모드)
- `.claude/rbac/policy.yaml` (6 역할 + extensions 4종 명세)
- /audit `--act-queue list|show|dispatch|done` + `--rbac-check` 모드 활성화
- audit-reporter Phase C-ACT + kpi-analyzer Phase D-ACT (act-trigger 위임)
- `--no-act-queue` 옵션

**PoC act queue 6건** (run-a1c2d3e4 + run-k4f8d2a1 결과):
- queue-qa1b2c3d4 — NCR-001 critical (KPI 3개 통합)
- queue-qe5f6a7b8 — NCR-002 major
- queue-q9c8d7e6f — NCR-003 minor
- queue-qf1e2d3c4 — NCR-004 critical (권고 통합)
- queue-q5a6b7c8d — META-COVERAGE kpi_critical
- queue-q9d8c7b6a — 단독 권고

**MAT-008 §"차원 4 인계"** + Mermaid gantt 6 큐 시각화.

**변경량**: +1306 / -53 / 19 파일 (9 신규).

**차원 3 사이클 종료** (Phase 1~4 누적): +4836 / -149 / 35 파일 / 4 commit.

---

## 5. 차원 4 (Act) Phase 1 — Core MVP

**Phase 0 결정 락** (6종):
1. 슬래시: `/act` (4차원 PDCA Act)
2. trace prefix: `run-c*` (change/CAPA — audit/kpi 와 분리)
3. 산출 위치: `vault/02_표준/{표준}/_inputs/04_AsIs/queue-q*.md` (차원 1 입력)
4. MAT-001 §"개정 이력" 자동 누적 (기존 MAT-001 새 섹션)
5. PoC 대상: queue-qa1b2c3d4 (NCR-001 critical / root cause 큐)
6. PCB 승인: auto-approve PoC 한정

**구현** (commit `5a5e3f3`):
- `.claude/commands/act.md` (374줄, 7 진입 모드)
- `.claude/agents/rca-analyzer.md` (270줄, 5-Why / Fishbone / both)
- `.claude/agents/revision-planner.md` (311줄, 5종 rebuild_mode + 6단계 actions + 의존성)
- `.claude/agents/pcb-gatekeeper.md` (218줄, gate_enter / gate_response + auto-approve PoC)
- `.claude/agents/act-coordinator.md` (315줄, As-Is + MAT-001 + 큐 done + MAT-008 갱신)
- `vault/02_표준/CMMI-DEV-ML3/_inputs/04_AsIs/queue-qa1b2c3d4.md` (As-Is 입력)
- `표준_프로세스_제개정_가이드.md` (485줄, 10 섹션 + 부록 A 4차원 동형성)
- `.gitignore` 예외: `!/vault/02_표준/*/_inputs/04_AsIs/queue-q*.md`

**PoC** (run-c4f8a1b2):
- RBAC: actor "박팀장" (process_owner) → action "act.start" allowed
- RCA 5-Why depth 5: primary=method (PRO §5-6 SLA 미정의), confidence high
- revision_plan: PRO-CMMI-04-01 v1.0 → v1.1, --from write, impact=medium, 8h
- PCB 승인 (auto): pcb_approved
- As-Is 파일 작성 + MAT-001 §개정 이력 1행 + 큐 status: pending → done
- MAT-008 §차원 4 인계 status: pending → done

**변경량**: +2179 / -8 / 16 파일 (12 신규).

**4차원 PDCA 자동화 완성**: 차원 1 (`/build-standard`) + 2 (`/do`) + 3 (`/audit`) + 4 (`/act`) — 모든 차원 슬래시 + 23 에이전트 보유.

---

## 6. 폐쇄 루프 실증 PoC

**시나리오**: 차원 4 Phase 1 의 다음 단계 — As-Is 입력을 차원 1 빌드의 입력으로 사용해 PRO v1.0 → v1.1 산출 + 후속 차원 2/3 으로 폐쇄 루프 검증.

**구현** (commit `6579b8d`):

### 6-1. 차원 1 (Plan) — PRO v1.1 개정
- `vault/04_PRO_절차/PRO-CMMI-04-01_*.md` 직접 편집:
  - frontmatter version: 1.0 → 1.1 + revision_source (act_trace / asis_input / ncr_resolved)
  - §5-6 종결 추적: SLA 등급별 (critical 20영업일/major 60일/minor 90일) + R/A 분리 (QA-R / PM-A) + 자동 알림
  - §7 KPI: 측정 시점 정의 정합 (발견 = §5-4, 종결 = §5-6 capa_rec) + 분기 측정 보고서 산출물 신설
  - §10 개정 이력 v1.1 행 추가

### 6-2. 차원 2 (Do) — CAPA REC 발행
- `REC-CMMI-04-01-04-01-2026-003_품질_이슈_에스컬레이션_시정.md` (run-e3a7b9c1)
- applied_pro_version: 1.1 (개정판 첫 실행)
- 다단계 정상 승인 (PM 박팀장 → Sponsor 박상무) — REC-002 의 반려 케이스와 대조
- capa_for_ncr: REC-NCR-04-01-2026-001
- MAT-005 §실행기록 1행 (PRO v1.1 표기)

### 6-3. 차원 3 (Check) — NCR close
- REC-NCR-04-01-2026-001 frontmatter status: open → closed + capa_rec / closed_at / closed_by / SLA 15일 단축
- §7 종결 기록 표 채움
- MAT-006 §발행 행 제거 → §종결 행 추가
- MAT-006 §통계: 종결율 0% → 25%, SLA 준수율 100% (n=1), 평균 종결 기간 9 영업일

### 6-4. 차원 3 (Check) — KPI round 2
- run-k7d2e8f3 (period 2026-04-01..06-30) — round 1 baseline 자동 비교
- verdict 변화: critical 4→1, healthy 3→6, recovering 0→2, data_gap 4→2
- 회복 사례:
  - KPI-04-01-02 부적합 종결율: 0.0% → 50.0% (+50%p) — recovering
  - KPI-04-01-03 평균 종결 기간: data_gap → 9 영업일 — healthy (목표 ≤ 20)
  - KPI-04-01-05 재발률: data_gap → 0.0% — healthy
  - META-NCR-CLOSURE: 0.0% → 25.0% (+25%p) — recovering
  - META-NCR-SLA: data_gap → 100.0% — healthy (15일 단축)
- 잔존 critical: META-COVERAGE (queue-q5a6b7c8d 미진행)
- MAT-008 §회차 시계열 11행 + §회귀 알림 round 2 + Mermaid gantt 갱신

### 6-5. 추적성
- As-Is `queue-qa1b2c3d4.md` frontmatter applied: { status: applied, capa_rec, closed_ncr, kpi_recovery_round }
- MAT-001 §개정 이력 status: "차원 1 재트리거 대기" → "✅ 완료"
- MAT-008 frontmatter closed_loop_demonstrated: true

**변경량**: +511 / -44 / 16 파일.

**폐쇄 루프 효과 입증**: 단일 차원 4 사이클로 critical 3건 회복 + data_gap 2건 해소.

---

## 7. 차원 4 Phase 2 — 다중 큐 일괄 + 의존성 그래프 + 통합 As-Is

**구현** (commit `8530d80`):
- /act `start --batch <ids>` / `--batch-related <id>` 모드 추가
- rca-analyzer batch 모드: per_queue[] + merged_root_cause + min confidence
- revision-planner batch: 통합 rebuild_command + dependency_graph_mermaid (graph TD 자동 생성)
- act-coordinator batch: 통합 As-Is `queue-batch-{id}.md` + linked_queues[] + 큐 일괄 done

**PoC** (run-c8b3d4f7 / batch 2 큐):
- 입력: queue-qe5f6a7b8 (NCR-002 major) + queue-q9d8c7b6a (단독 권고)
- merged_root_cause: PRO-CMMI-04-01 §7 KPI 측정 시점 정의 분리 + 측정 보고서 TMP 부재 (confidence high)
- 통합 rebuild_plan: PRO v1.1 → v1.2 + WI-04-01-06 신규 + TMP-04-01-06-01 신규 (3 자산 일괄, impact medium-high, 16h)
- 통합 As-Is: `vault/02_표준/CMMI-DEV-ML3/_inputs/04_AsIs/queue-batch-e5f6a7b8.md`
- 두 큐 일괄 status: done

**변경량**: +234 / -18 / 11 파일.

---

## 8. Phase 4.5 — 외부 연동 hook + 영업일 + PCB quorum + 자동 트렌드

**구현** (commit `318c255`):

### 8-1. RBAC policy.yaml extensions 활성화
- `external_idp` (OIDC) — issuer/role_mapping/fallback
- `delegation` — max 30일, revocable, audit_log 필수
- `audit_log` — 5 이벤트 5년 보존
- `external_notifications` (신규) — email/slack/jira 3 채널 + PCB·NCR·KPI 알림 트리거 + 비밀 환경변수 + file_drop_out fallback

### 8-2. .claude/utils/business_days_kr.md (한국 영업일 정식)
- 공휴일 14개 (2026 기준): 신정/설날 3/삼일절(대체)/어린이날/부처님오신날(대체)/현충일/광복절/추석 3/개천절/한글날/성탄절
- add_business_days / diff_business_days / is_business_day 의사 코드
- ncr-drafter SLA 휴리스틱 (28/60/90일) → 정식 영업일 (20/42/63 영업일) 매핑
- act-coordinator 50%/100% 자동 알림 시점 계산
- NCR-001 PoC 검증: 13 calendar = 9 영업일 (5/5 어린이날 1건 영향)

### 8-3. .claude/utils/pcb_quorum.md (PCB 다단계 quorum)
- 4 quorum 모드: simple_majority / supermajority / unanimous / chair_veto
- 위원회 구성 예시 (4명 — chairperson + voting_member 3)
- 자동 quorum 결정 (revision_plan.estimated_impact 기반)
- 응답 처리 (위원별 /act --approve / --reject 누적 → quorum_evaluation)
- 타임아웃·에스컬레이션 (default 7일)

### 8-4. .claude/utils/auto_trend_mermaid.md (자동 트렌드 다이어그램)
- round ≥ 2 부터 활성화 (kpi-analyzer Phase D-Trend 신규 단계)
- 3 다이어그램 자동 생성:
  - KPI 라인 차트 (11개, target line 함께)
  - verdict 분포 stacked bar (round 간 비교)
  - 사이클 흐름 graph TD (round 노드 + 차원 4 trace edge)
- Mermaid xy-chart-beta 사용
- round ≤ 8 안정, Phase 5 외부 BI 마이그레이션

**변경량**: +470 / -8 / 5 파일 (3 신규 utils).

---

## 9. main 머지 + push

**사용자 요청**: "pr 생성하지 말고 그냥 main에 merge 해."

**작업** (merge commit `be900cc`):
1. main 위치 검증: cefd8ac (분기 후 1 commit 추가, worktree 가이드 문서)
2. local main vs origin/main 동기화 확인
3. checkout main → merge feat/process-execution-harness --no-ff
4. merge commit 메시지: "merge: 4차원 PDCA AI 자동화 완성 (차원 2~4 + 폐쇄 루프 PoC)"
5. push origin main: `cefd8ac..be900cc  main -> main`

**누적**: 31 commits / 661 files / +45,698 / -230 줄. 충돌 0건.

---

## 10. feat 브랜치 정리

**사용자 요청**: "feat 브랜치 정리하자."

**작업**:
1. `git worktree list` 확인 — feat/cmmi-dev-ml3-output 은 별도 worktree (`/Users/dongseok/MyProjects/CMMI-DEV-ML3-view`) 운영 중
2. 정책 (표준_빌드_워크플로우_가이드.md) 상 산출물 열람 worktree 보존 권장
3. **feat/process-execution-harness 만 정리**:
   - `git branch -d` → 거부 (origin/feat 가 아직 origin/main 비교 시 unique 없음에도 -d 가 origin tracking 비교)
   - 안전 검증: `git log feat ^origin/main` = 빈 결과 → commit 분실 위험 0
   - `git branch -D feat/process-execution-harness` (local 삭제)
   - `git push origin --delete feat/process-execution-harness` (remote 삭제)

**결과**: local + remote 모두 삭제. feat/cmmi-dev-ml3-output 은 worktree 와 함께 보존.

---

## 11. MAT-006 동명 이건 해소

**문제 발견**: GitHub 구조 보고 시 `vault/90_MAT_통합매핑/` 에 `doc_id: MAT-006` 인 파일 2개 발견:
- MAT-006_문서계층_추적매트릭스.md (legacy, 4-29 운영, 5건 cross-ref)
- MAT-006_NCR_관리대장.md (Phase 2 신규, 8건 인용)

**원인**: 차원 3 Phase 2 commit (f9a9596) 작성 시 정책 표 (vault/00_공통관리/02_문서번호체계.md) 사전 검증 미흡. MAT-007 (프로세스 카탈로그) / MAT-008 (KPI 대시보드) 도 같은 패턴.

**해결** (commit `ed853b1`):
- 옵션 A 채택 (legacy 보존, 신규 → MAT-009 재번호)
- `git mv MAT-006_NCR_관리대장.md MAT-009_NCR_관리대장.md` (97% 유사도 자동 인식)
- 일괄 변환 (NCR 컨텍스트만, legacy 참조는 보존):
  - 파일 frontmatter doc_id: MAT-006 → MAT-009
  - NCR 4건 / MAT-008 / 에이전트 8종 / commands/audit.md / trace 3건 의 본문
  - 이벤트 명: `mat006_*` → `mat009_*` (3 trace 포함)
- 정책 표 갱신: 6종 → 9종 운영 (MAT-007/008/009 추가, MAT-010 만 예약)
- vault/90_MAT_통합매핑/README.md 표 갱신 (도입 차원 컬럼 + 관리 담당 4 차원 재정리)

**변경량**: +132 / -126 / 25 파일.

**검증**: 잔여 NCR MAT-006 / mat006: 0건. legacy MAT-006 참조 10 파일 보존 확인.

---

## 12. README.md 4차원 PDCA 갱신

**사용자 요청**: "루트의 README.md를 업데이트 해줘."

**작업** (commit `79efdc5`):
- 제목: "전사 표준 프로세스 구축 하네스" → "4차원 PDCA AI 자동화 플랫폼"
- 신규 섹션 8건:
  1. 4차원 자동화 매트릭스 (4 슬래시 / 23 에이전트)
  2. 차원 2/3/4 특징
  3. 폐쇄 루프 (4차원 통합)
  4. Phase 4.5 명세
  5. 4차원 PDCA 폐쇄 루프 흐름 (전체 ASCII)
  6. 사용법 §2~5 (/do, /audit, /act, 폐쇄 루프 시나리오)
  7. RBAC 6 역할 표 + extensions
  8. 폐쇄 루프 PoC 검증 결과 (round 1 → 2 회복 통계) + 누적 통계
- 기존 갱신: 디렉터리 구조 / 에이전트 파이프라인 / MAT 6종 → 9종

**변경량**: 199줄 → 435줄 (+336 / -100). main push 완료.

---

## 13. 운영 환경 한계 분석

**사용자 관찰**: "지금 현재 실행환경은 로컬 PC에 리파지토리를 clone 하고, ... 1명의 프로세스 책임자/담당자에 의해서 record를 생성하고, 실행된 결과를 self audit하고, audit 결과에 따라 self revise 되는 구조잖아."

**진단**:
- **단일 사용자 / 단일 머신 / 자기 자신과의 폐쇄 루프** 구조
- 1 인 사용자가 6 RBAC 역할 모두 수행 — 가상 이름 ("이감사" / "박팀장" / "박상무") 으로 시뮬레이션
- 거버넌스 무결성: **인터페이스만 갖춰진 상태** (1 인 신뢰 기반)
- 외부 검증성: 외부 심사원이 "심사원 ≠ 이행자" 시스템적으로 입증 불가
- 확장성 부재: 다수 사용자 동시성·접근 제어 미동작

**진화 경로**:
1. Phase 4.5 실 구현 (Python 모듈 + 외부 IdP/Jira)
2. Phase 5 SaaS 마이그레이션 (PostgreSQL/S3/Redis + 멀티 사용자)
3. ISO 17021 인정 인증기관 수용 가능 수준

---

## 14. CMMI ML3 vs ML4/ML5 격차 분석

**사용자 관찰**: "cmmi를 비롯한 타 국제 표준 기반 프로세스의 경우, ml 3 수준은 되는데, ml4, ml5 수준을 항시적으로 유지하기 위한 고려는 되어 있지 않지?"

**진단**:

### ML3 (Defined) — ✅ 충족
- 표준 프로세스 정의 (차원 1) + 이행 (차원 2) + 추적성

### ML4 (Quantitatively Managed) — ⚠ 부분 토대만
- KPI 측정 ✅ but PPM (Process Performance Models) 없음
- verdict 4-tier ✅ but SPC (Statistical Process Control / control chart / Cpk) 없음
- 회귀 탐지 ±5%p ✅ but 변동성 분석 (자연 vs 특수 원인) 없음
- 분기 측정 ✅ but 연속 측정 / 실시간 ingest 없음
- 비즈니스 OKR → KPI 카스케이드 없음

### ML5 (Optimizing) — ⚠ Reactive 만, Proactive 부재
- RCA (5-Why / Fishbone) ✅ but 통계 가설 검증 (CAR statistical) 없음
- 단발 사이클 ✅ but 전사 carry-over (OPM) 없음
- 매 개정 즉시 전사 적용 — pilot 메커니즘 없음
- PPM 기반 예측 (다음 round 시뮬레이션) 없음
- 재발 root cause 학습 (improvement-memory) 없음

### 항시 유지가 요구하는 것
- A. 통계 인프라: PPM / SPC / 변동성 분석 / 분포 검정 / 연속 측정
- B. 예측·사전 개입: KPI 예측 / SLA 위반 D-N 일 사전 알림 / Anomaly detection / What-if 시뮬레이션
- C. 카스케이드·전개: OKR → KPI → sub-KPI / 다수 PRO 횡단 학습 / Pilot 전개 / 개선 효과 정량화 (₩ 비즈니스 가치)
- D. 자가 학습: 재발 root cause 패턴 / 개정-효과 메모리 / LLM fine-tuning

### 비전 문서와 정합
`AI-Driven CMMI Operating Platform.md` 의 Layer 2 (ML4) / Layer 3 (ML5) 가 정확히 본 격차의 로드맵. 본 PoC 는 Phase 1 (Layer 1 = ML3) 만 검증.

### 추가 필요한 신규 자산
- `ppm-modeler` 에이전트 (Phase 5)
- `spc-monitor` 에이전트 (Phase 5)
- `kpi-predictor` 에이전트 (Phase 5)
- `bizkpi-aligner` 에이전트 (Phase 6)
- `car-statistical` 에이전트 (Phase 5)
- `pilot-orchestrator` 에이전트 (Phase 6)
- `improvement-memory` 에이전트 (Phase 6)
- 신규 MAT-010 = OKR 카스케이드
- 데이터 인프라: 시계열 DB (TimescaleDB / InfluxDB) + 통계 모델 저장소 (S3 / MLflow)

---

## 15. 본 세션의 주요 산출물·메트릭

### Git commit (9건, 본 세션 시작 ~ 종료)

| Commit | 메시지 |
|---|---|
| bcec212 | feat(audit): 차원 3 Phase 1 — /audit + 4 에이전트 + PoC + 가이드 |
| f9a9596 | feat(audit): 차원 3 Phase 2 — ncr-drafter + MAT-006 + --list-ncr/--close-ncr + PoC NCR 4건 |
| c8f885c | feat(audit): 차원 3 Phase 3 — KPI 대시보드 + kpi-collector + kpi-analyzer + MAT-008 |
| fb19ba2 | feat(audit): 차원 3 Phase 4 — independence-guard + RBAC + act-trigger + 차원 4 인계 hook |
| 5a5e3f3 | feat(act): 차원 4 Phase 1 — /act + 4 에이전트 + RCA + PCB 승인 + 차원 1 재트리거 인계 |
| 6579b8d | feat(closed-loop): 폐쇄 루프 실증 PoC — PRO v1.1 + NCR close + KPI round 2 회복 |
| 8530d80 | feat(act): 차원 4 Phase 2 — 다중 큐 일괄 + 의존성 그래프 + 통합 As-Is |
| 318c255 | feat(audit+act): Phase 4.5 — 외부 연동 hook + 영업일 정식 + PCB quorum + 자동 트렌드 |
| **be900cc** | **merge: 4차원 PDCA AI 자동화 완성 (차원 2~4 + 폐쇄 루프 PoC)** |
| ed853b1 | fix(numbering): MAT-006 동명 이건 해소 — NCR 관리대장 → MAT-009 + 정책 표 갱신 |
| 79efdc5 | docs(readme): 4차원 PDCA AI 자동화 플랫폼 — 차원 2/3/4 + 폐쇄 루프 + Phase 4.5 반영 |

### 메트릭 (본 세션 누적)
- 변경량: +6,808 / -287 (대략) — 9 feature commit + 1 merge + 1 fix + 1 docs
- 신규 에이전트: 13 (차원 3: 9 / 차원 4: 4)
- 신규 슬래시: 2 (`/audit` + `/act`)
- 신규 MAT: 3 (MAT-006 NCR → MAT-009 / MAT-008 KPI 대시보드 — 차원 3 결과로)
- 신규 가이드: 1 (제·개정 가이드 / 심사 가이드는 갱신)
- PoC trace: 5 신규 (run-a1c2d3e4 / run-k4f8d2a1 / run-k7d2e8f3 / run-c4f8a1b2 / run-c8b3d4f7)
- act queue: 6 (3 done — 1 단일 + 2 batch / 3 pending)
- Phase 4.5 utils: 3 (영업일 / PCB quorum / 자동 트렌드)
- 정책 표 갱신: MAT 6종 운영 → 9종 운영
- main 통합: 31 commits → main, GitHub 동기화 완료

### Pull Request 미사용
- 사용자 요청에 따라 PR 미생성 — 직접 `--no-ff` merge → push origin main.

### 메모리 갱신
- `project_4d_pdca_dimension3_phase1.md` (차원 3 Phase 1~4)
- `project_4d_pdca_dimension4_phase1.md` (차원 4 Phase 1+2 + 폐쇄 루프 + Phase 4.5)
- `MEMORY.md` 인덱스 갱신 (3 entries — 차원 2 / 3 / 4)

---

## 16. 협업 스타일 회고 (메모리 검증)

세션 전반의 사용자-AI 상호작용 패턴이 기존 메모리 (`feedback_collaboration_style.md`) 와 정확히 일치:
- 옵션 ABC + 추천 1수 제시 → 사용자 "a로 진행해" 응답 (15+회 반복)
- 단계별 검증 (PoC → commit → 다음 Phase) 흐름 유지
- 큰 결정 (main 머지 / feat 브랜치 정리 / MAT-009 재번호) 도 추천 채택
- 운영 환경·성숙도 한계 같은 메타 질문은 답변만 + 다음 옵션 제시 패턴

---

## 17. 미해결·후속 작업

### 즉시 후속 (선택)
- 남은 act queue 4건 (queue-q9c8d7e6f / qf1e2d3c4 / q5a6b7c8d) 의 차원 4 사이클 → round 3 측정으로 추가 회복
- feat/cmmi-dev-ml3-output worktree 정리 결정 (현재 보존 중)

### 구조적 후속 (큰 작업)
- ML4/ML5 항시 유지 — 7 신규 에이전트 + 데이터 인프라 (Phase 5/6)
- SaaS 마이그레이션 — 다수 사용자 / 외부 IdP / 외부 알림 실 연동 (Phase 5)
- ISO 17021 인증기관 수용성 검증 (Phase 6+)
- `전용AI에이전트_프레임워크_설계안.md` 와 본 4차원 자동화 통합 — Python 독립 프레임워크 승격

### 문서 후속 (선택)
- `현재_운영_한계_및_확장_경로.md` 신규 (운영 환경 + ML4/ML5 격차 통합) — 사용자 "a + b" 추천 후 미실행
- `ML4_ML5_항시유지_설계메모.md` 신규 — 7 신규 에이전트 + Phase 5/6 분기 설계
- `AI-Driven CMMI Operating Platform.md` Layer 2/3 비전 갱신 (PoC 결과 반영)

---

## 18. 본 세션의 의의

**시작**: 차원 2 사이클 종료 직후, 차원 3/4 미설계 상태.

**종료**: 4차원 PDCA AI 자동화 main 통합 + 폐쇄 루프 PoC 실증 + Phase 4.5 명세 + ML4/ML5 격차 진단.

**핵심 가치**:
1. **세계 최초 (?)** ISO/CMMI 표준 프로세스의 4차원 PDCA 전체를 AI 에이전트로 자동화한 PoC.
2. **방법론·구조·추적성** 검증 완료 (단일 사용자 단일 머신 한정).
3. **확장 경로 명확** — Layer 2/3 (ML4/ML5) + SaaS (멀티 사용자) 두 축으로 진화 가능.
4. **8종 문서유형 체계 유지** — 4차원 자동화에도 구성원칙 §8 부합.
5. **추적성 무결성** — Plan→Do→Check→Act→Plan' 사이클이 단일 trace 그래프로 추적 가능 (run-c* / run-a* / run-k* / run-{hex} prefix 분리).

**남은 핵심 갭**:
1. 1 인 운영 → 다수 사용자 운영 (Phase 5 SaaS)
2. ML3 정의 → ML4/ML5 항시 유지 (Phase 5/6 통계 인프라)
3. PoC 검증 → 인증기관 수용 (Phase 6+ 거버넌스 강화)

본 세션은 **AI 기반 표준 운영 시스템의 PoC 단계 종료 + 운영 시스템 진화 로드맵의 분기점**.

---

> 본 회고록은 2026-05-02 단일 세션의 기록입니다.
> 다음 세션 시작 시 본 문서 + memory 시스템 (project_4d_pdca_*) + git log main 을 컨텍스트로 사용하면 즉시 이어 작업 가능.
