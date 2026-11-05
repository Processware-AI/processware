---
description: '적용요건 정의 + 프로세스 모듈 구축 (차원 1 Plan) — inputs/ 분석 → 02_적용요건/{명칭}/적용요건.md 생성 → POL/PRO/WI/TMP/EX/MAT Obsidian vault 구축. 입력은 자유 명칭·표준코드·자연어 모두 수용. 체크포인트/재개·자가수정 루프 지원. 사용: /process-plan "OOO사 품질경영체계"'
argument-hint: "<모듈_또는_요건> [--restart] [--resume] [--from <phase>] [--skip-qa] [--cross] [--max-attempts N] [--org <id> | --org-root <path>]"
---

# 프로세스 모듈 빌드 파이프라인 (Level 3: 체크포인트 + 자가수정)

빌드 대상: **$ARGUMENTS**

## 조직 컨텍스트 (공통 — org-layer §3 단계 1~3)

본 문서와 에이전트 정의의 경로 변수는 **활성 조직 루트** 기준이다. 규약 전문: `.claude/utils/org_context.md`

| 변수 | 의미 | 경로 (조직 루트 기준) |
|---|---|---|
| `{VAULT}` | Obsidian vault | `{ORG_ROOT}/vault/` |
| `{INPUTS}` · `{SOURCES}` | ingest 산출물 · 원본 파일 | `{ORG_ROOT}/inputs/` · `sources/` |
| `{RUNS}` · `{QUEUES}` · `{STATES}` | 실행 trace · 인계 큐 · 체크포인트 | `{ORG_ROOT}/.processware/runs|queues|states/` |

1. 진입 직후 1회 해석한다. 인자 `--org-root <path>` > `--org <id>` > 환경변수 `PROCESSWARE_ORG_ROOT` > `PROCESSWARE_ORG`. 어느 것도 없으면 **즉시 실패** (default fallback 없음 — 플랫폼 repo 에는 vault 가 없다).
   ```bash
   python3 -m tools.org context --format env [--org <id> | --org-root <path>]
   ```
   exit ≠ 0 이면 즉시 중단하고 stderr 를 사용자에게 보여준다. 성공 시 `PROCESSWARE_VAULT` → `{VAULT}` 등으로 변수를 바인딩하고, `조직: {id} · 루트: {root}` 1줄을 출력하며, trace 첫 이벤트에 `org_id` · `org_root` · `org_source` 를 기록한다.
2. 에이전트에 위임할 때 바인딩된 변수 값을 프롬프트 첫머리에 그대로 전달한다 (에이전트는 전달받은 값을 쓰고, 없을 때만 직접 해석).
3. `--org-root` 로 받은 값은 하위 `python3 -m tools.*` 호출 전에 `PROCESSWARE_ORG_ROOT` 로 export 한다. 활성 조직 루트 밖에는 읽고 쓰지 않으며, git 작업(branch · commit)도 조직 루트 repo 에서 한다. `{VAULT}/00_공통관리` · `01_구성원칙` · `99_템플릿` · 폴더 `README.md` 는 플랫폼 관리 파일이라 수정하지 않는다 (sync-core 가 덮어씀). 플랫폼 자산(`.claude/agents|commands|utils|rbac`, `tools/`, `docs/`, `core/`) 은 변수화 대상이 아니다. 격리는 3중으로 강제된다: Claude Code PreToolUse 훅(`.claude/settings.json` → `tools.org.hook_guard`) · `tools.vault_rules validate` · qa-reviewer §13 — 확인이 필요하면 `python3 -m tools.org guard --path <경로>`.

---

## 실행 원칙
- 기준 문서: `{VAULT}/01_구성원칙/표준프로세스_구성원칙.md`
- 문서체계: `{VAULT}/00_공통관리/01_문서체계.md` (8종 유형)
- 번호체계: `{VAULT}/00_공통관리/02_문서번호체계.md`
- 입력자료 규칙: `{VAULT}/00_공통관리/05_입력자료_규칙.md`
- **파이프라인 상태 규약**: `{VAULT}/00_공통관리/06_파이프라인_상태규약.md` (체크포인트/재개/자가수정)
- 모든 산출물: Obsidian 호환 MD(frontmatter + `[[wikilink]]`)

---

## Phase −2: Git Branch 격리 (state 결정 직전)

본 파이프라인은 **branch-per-standard** 정책을 따른다. 기준 브랜치 `{BASE}`(보통 main)는 조직 설정 · 등록 메타 · sync-core 결과만 누적하고, 표준별 산출물은 격리된 feature branch 에 영구 보존한다.

**git 작업 대상은 조직 루트 repo `{ORG_ROOT}` 하나다.** 플랫폼 repo(Claude Code 의 현재 작업 디렉토리일 수 있다)에서는 git 명령을 실행하지 않는다. 모든 git 명령은 `git -C {ORG_ROOT} …` 로 호출하고 `cd` 로 작업 디렉토리를 바꾸지 않는다 (하위 `python3 -m tools.*` 호출이 플랫폼 루트 기준이기 때문). `git add` 경로는 조직 루트 상대 경로(`vault/…`, `.processware/…`)다.

**예외**: `--no-branch` 플래그이면 −2-2 · −2-4 를 건너뛰고 `{BASE}` 단일 브랜치로 작업한다. −2-0 검증과 −2-1 등록은 그대로 수행한다.

### −2-0. 대상 repo 검증 · 기준 브랜치 결정

```bash
git -C {ORG_ROOT} rev-parse --show-toplevel                      # (1) repo 여부 · 최상위 경로
git -C {ORG_ROOT} symbolic-ref --short refs/remotes/origin/HEAD  # (2) 기준 브랜치 (origin/main 등)
git -C {ORG_ROOT} remote get-url origin                          # (3) 원격 유무
git -C {ORG_ROOT} status --porcelain                             # (4) 미커밋 변경
git -C {ORG_ROOT} branch --list "feat/{슬러그}-output*"           # (5) 기존 빌드 브랜치
```

| 검사 | 조건 | 동작 |
|---|---|---|
| (1) | 실패 — git repo 아님 | 질문: **A)** `git -C {ORG_ROOT} init -b main` → `git -C {ORG_ROOT} add -A` → `commit -m "chore(org): 조직 루트 초기화 ({org_id})"` 후 진행 (권장) · **B)** `--no-branch` 모드로 계속 (branch 격리 없음 — 최종 보고에 명시) |
| (1) | 최상위 ≠ `{ORG_ROOT}` (상위 repo 에 중첩) 또는 최상위 = `{PLATFORM_ROOT}` | **즉시 중단** — 조직 루트는 별도 repo 여야 한다 (org-layer §5 결정 1). 상위 repo 에서 분리하거나 다른 루트를 지정하도록 안내 |
| (2) | 원격 HEAD 없음 | `main` → `master` → 현재 브랜치 순으로 존재하는 첫 브랜치를 `{BASE}` 로 |
| (3) | origin 없음 | pull · push 단계 생략. 로컬 브랜치만 운영하고 최종 보고에 `origin 없음` 표시 |
| (4) | 변경 있음 | 목록을 보여주고 질문: 커밋/stash 후 진행 또는 그대로 진행(미커밋 변경은 체크아웃을 따라간다). 변경이 `vault/00_공통관리` · `01_구성원칙` · `99_템플릿` · 폴더 `README.md` · `org.yaml platform_version` · `.processware/sync-core.yaml` 뿐이면 sync-core 결과이므로 `{BASE}` 에 `chore(sync-core): platform {platform_version}` 로 먼저 커밋 |
| (5) | `feat/{슬러그}-output` 존재 · `--restart` 아님 | 재개 후보 — 해당 브랜치를 체크아웃한 뒤 Phase −1 로 (`_state.yaml` 은 그 브랜치에 있다). `--restart` 면 일자 suffix 브랜치를 새로 만든다 |

`조직 repo: {ORG_ROOT} · 기준: {BASE} · origin: 있음/없음` 1줄을 출력하고 trace 첫 이벤트에 `git_base` · `git_remote` 를 기록한다. 플랫폼 repo 의 `git -C {PLATFORM_ROOT} status --porcelain` 결과를 보관해 Phase Final 에서 대조한다.

### −2-1. 사전 등록 (`{BASE}` 작업 — 조직 소유 파일만)

표준 빌드 시작 전 신규 표준 식별 정보를 등록하고 `{BASE}` 에 직접 commit·push 한다. **플랫폼 관리 파일(`{VAULT}/00_공통관리/02_문서번호체계.md` · `07_표준분류레지스트리.md` 등)은 수정하지 않는다** — PreToolUse 훅이 막고 sync-core 가 덮어쓴다. 등록 위치는 모두 조직 소유 파일이다:

| 항목 | 위치 (조직 소유) | 내용 |
|---|---|---|
| 영역코드 편입 | `{ORG_ROOT}/org.yaml` → `scopes` | 영역코드 추가 (예: `scopes: [QMS, ISMS]`). `python3 -m tools.org validate` 로 확인 — 플랫폼 레지스트리에 없는 코드는 warning 만 낸다 |
| 플랫폼 레지스트리에 없는 **신규 표준** | `{VAULT}/00_공통관리/07_표준분류레지스트리_조직추가.md` (없으면 생성) | 플랫폼 레지스트리 §2 형식의 row + §6 형식의 메타 모델 YAML block. `standard-analyzer` · `process-designer` · `qa-reviewer` 는 플랫폼 레지스트리와 이 파일을 함께 조회한다. 플랫폼 레지스트리 편입은 플랫폼 PCB 심의 (별도 PR) |
| 표준별 추적성 MAT 예약 | `{VAULT}/00_MOC/MOC_추적성매트릭스.md` §표준별 추적성 매트릭스 | 번호(MAT-011 부터 다음 미사용) · 표준 · 편입일 행 추가 — Trace 단계에서 traceability-mapper 가 확정 |

```bash
git -C {ORG_ROOT} checkout {BASE}
git -C {ORG_ROOT} pull --ff-only                        # origin 있을 때만
# (위 파일 편집)
git -C {ORG_ROOT} add org.yaml vault/00_MOC/MOC_추적성매트릭스.md vault/00_공통관리/07_표준분류레지스트리_조직추가.md
git -C {ORG_ROOT} commit -m "feat(registry): {표준코드} 영역코드 등록 — org.yaml scopes + MOC 추적성 예약"
git -C {ORG_ROOT} push origin {BASE}                    # origin 있을 때만
```

이미 `scopes` 에 있고 MOC 에 등재된 표준(재빌드)이면 변경 없음으로 통과한다.

### −2-2. Feature branch 생성

`{BASE}` 의 등록 commit 위에서 분기:

```bash
git -C {ORG_ROOT} checkout -b feat/{모듈슬러그}-output
```

이후 모든 phase (preflight ~ qa, 자가수정) 는 이 branch 에서 작업. `_state.yaml` 에 `org_id` 와 `git: {branch, base}` 를 기록한다 (T14 템플릿 필드) — 재개 시 −2-0 (5) 와 대조하고, 현재 브랜치가 다르면 기록된 브랜치로 체크아웃한다.

**branch 명 컨벤션**:
- 형식: `feat/{모듈슬러그}-output`
- 모듈슬러그 결정 규칙:
  - 표준 코드 입력: 소문자 그대로. 예: `feat/iso9001-output`, `feat/cmmi-dev-ml3-output`
  - PA 그룹명 입력: 소문자·하이픈. 예: `feat/cmmi-prj-planning-output`
  - 자연어 입력: 핵심 키워드 추출 후 소문자·하이픈. 예: "프로젝트 계획·추정·리스크 관리" → `feat/prj-planning-est-risk-output`
  - 슬러그 결정 후 사용자에게 확인 후 진행
- 동일 모듈 재빌드 시: `feat/{모듈슬러그}-output-{YYYYMMDD}` 로 일자 suffix

### −2-3. 작업 도중 commit 정책

커밋 범위는 `vault/` 산출물 + `.processware/states/{슬러그}_state.yaml` + `.processware/runs/` (감사 증적) 이다. `vault/00_공통관리` 등 관리 폴더 변경이 diff 에 섞이면 산출물 커밋에 넣지 말고 `chore(sync-core): …` 로 분리한다.

각 phase 종료 시 **선택적 중간 commit** (사용자 옵션 `--commit-per-phase` 시):
- analyze 종료: `feat({슬러그}): analyze 완료 — 적용요건 REQ N건`
- design 종료: `feat({슬러그}): design 완료 — POL N / PRO M`
- write 종료: `feat({슬러그}): write 완료 — WI/TMP/EX N×3`
- trace 종료: `chore({슬러그}): MAT 갱신 + MAT-{NNN} 신규`
- qa 종료: `chore({슬러그}): QA attempt N — Pass/Fail 통계`

기본은 **종료 시 일괄 4개 분할 commit** (모두 `git -C {ORG_ROOT}`):
1. `feat({슬러그}): 산출물 + 적용요건 (POL/PRO/WI/TMP/EX/REF)`
2. `chore(MAT): MAT-001~006 갱신 + MAT-{NNN} 신규`
3. `docs(MOC): 전체표준·추적성매트릭스 인덱스 갱신 + state·trace`
4. (필요 시) `fix({표준코드}): self-heal 후속 보정`

### −2-4. 종료 시 push

`overall_status: done` 도달 시:
```bash
git -C {ORG_ROOT} push -u origin feat/{슬러그}-output      # origin 있을 때만
```

`{BASE}` 에 merge 는 사용자 결정 사항. PR 생성 안내만 출력한다 (실행하지 않음):
```bash
gh pr create -R <조직 repo> --base {BASE} --head feat/{슬러그}-output --title "feat({슬러그}): 표준 산출물"
```
조직 repo 에 `.github/workflows/vault-push.yml` 이 있고 `org.yaml redmine.enabled: true` 이면, `{BASE}` merge 시 Redmine Library push 가 자동 실행됨을 함께 알린다.

### −2-5. 안전 가드

- 플랫폼 repo 에서는 git 명령을 실행하지 않는다. Phase Final 에서 `git -C {PLATFORM_ROOT} status --porcelain` 이 −2-0 보관본과 다르면 🚩 로 보고한다 (플랫폼 오염).
- `{BASE}` 에 절대 force-push 하지 않는다.
- branch 에 force-push 가 필요하면 `--force-with-lease` 사용.
- 빌드 실패·중단 시 branch 는 그대로 보존 (다음 attempt 재개 가능).
- `git -C {ORG_ROOT} add` 에 `{ORG_ROOT}` 밖 경로를 넣지 않는다. `-A` 는 −2-0 (1)-A 초기화 때만.

---

## Phase −1: State 결정 (가장 먼저)

### −1-1. `_state.yaml` 탐색
경로: `{STATES}/{슬러그}_state.yaml`

| 상황 | 기본 동작 | 플래그 override |
|---|---|---|
| 파일 없음 | **Fresh 시작** — 템플릿 `T14_파이프라인상태.yaml` 복사 | — |
| `overall_status: done` | 사용자에게 "이미 완료. 재실행?" 질문 | `--restart` 강제 |
| `overall_status: halted` | "중단됨. 이어서? 새로 시작?" 질문 | `--resume` 자동 이어서 / `--restart` 신규 |
| `overall_status: running` (전 세션 중단) | 현재 `current_phase` 부터 재개 제안 | `--resume` 자동 / `--from <phase>` 지정 |

### −1-2. `--restart` 처리
기존 `{슬러그}_state.yaml` 을 `{슬러그}_state_{YYYYMMDD_HHMM}.yaml` 으로 rename 보존 → 신규 상태 파일 생성.

### −1-3. 진행 결정 보고
사용자에게 현재 attempt·다음 실행 phase·생략될 phase 를 요약 보고 후 진행.

---

## Phase 0: 입력자료·골든샘플 Preflight

(Fresh 시작 또는 `--from preflight` 시에만 실행. 재개 시엔 state 에서 done 이면 생략.)

0-1. `{INPUTS}/` 존재 확인
   - 없으면 사용자에게:
     ```
     [Preflight 경고] {INPUTS}/ 에 입력자료가 없습니다.
     옵션:
       A) 지금 입력자료를 배치하고 재실행 (권장)
       B) LLM 추정만으로 진행 (정확도·감사 방어력 낮음)
     ```
   - B 선택 시에만 다음 단계 진행.

0-2. 입력물 인벤토리 요약 보고(파일 수·카테고리·라이선스 상태).

0-4. **골든샘플 3종 선행 로드** (`{VAULT}/99_템플릿/_골든샘플/`): GS-POL-QMS-002 / GS-PRO-QMS-102 / GS-WI-102-04.

0-5. `_state.yaml` 의 `phases.preflight` 를 `status: done` 으로 갱신, `current_phase: analyze`.

---

## 정상 파이프라인 (Attempt N, 첫 실행)

각 에이전트는 **Phase −1(자체 Prerequisite 확인)** 을 실행하고, 완료 시 **done-marker 갱신** 을 한다 (상태규약 §4).

1. **Analyze** — Agent `standard-analyzer`
   - 1-0. `{VAULT}/02_적용요건/{슬러그}/적용요건.md` 존재 확인
     - **있으면**: 기존 적용요건.md 를 requirements baseline 으로 로드 → Phase 2(design) 로
     - **없으면**: standard-analyzer 가 `{INPUTS}/` 분석 → 적용요건.md 생성 후 → Phase 2(design) 로
   - 출력: `02_적용요건/{슬러그}/적용요건.md` (신규 생성 시), `09_REF_참고자료/`, `90_MAT/MAT-002`
   - done-marker 로 `phases.analyze` 완료 기록

2. **Design** — Agent `process-designer`
   - 출력: `03_POL_정책/POL-*`, `04_PRO_절차/PRO-*`, `90_MAT/MAT-003`
   - done-marker: `phases.design`

3. **Write** — Agent `wi-tmp-writer`
   - 출력: `05_WI_업무지침/`, `06_TMP_템플릿/`, `07_EX_작성예시/`, `90_MAT/MAT-001`
   - done-marker: `phases.write`

3.5. **Flow** — Agent `flow-mapper`
   - 입력: `{VAULT}/04_PRO_절차/PRO-*.md` frontmatter (pro_type, follows, precedes, wi_sequence)
   - 출력: `90_MAT_통합매핑/MAT-010_프로세스_플로우맵.md` (파생 문서, 덮어쓰기)
   - done-marker: `phases.flow`
   - **`--flow` 단독 실행 시**: 이 단계만 실행 (1~3 단계 생략). PRO/WI 가 이미 존재해야 함.

4. **Trace** — Agent `traceability-mapper`
   - 출력: `90_MAT_통합매핑/MAT-{NNN}_{표준코드}_추적성_*` (NNN 은 MAT-011 부터 순차. 기존 번호 스캔 후 max+1), 공통 매트릭스(MAT-001·003·004·005·006) 최신화, `00_MOC/MOC_추적성매트릭스.md` §표준별 추적성 표 확정 (관리 파일 `02_문서번호체계.md` 는 수정하지 않음)
   - done-marker: `phases.trace`

5. **QA** — Agent `qa-reviewer` (옵션 `--skip-qa` 시 생략)
   - 리포트: `02_적용요건/{슬러그}/99_QA리포트_{YYYYMMDD}_attempt{N}.md`
   - done-marker + `qa_failures[]` (Fail 있을 때)

---

## 자가수정 루프 (Self-Correction Loop)

```
Attempt N 종료 시점에 qa_failures 평가:
  ├─ 빈 배열 (ALL PASS)
  │     → overall_status: done · current_phase: done · MOC ✅ 갱신 · 종료
  │
  ├─ 비어있고 N >= max_attempts (기본 3)
  │     → overall_status: halted · 사용자 에스컬레이션
  │
  └─ 비어있고 N < max_attempts
        → 자가수정 모드로 Attempt N+1 개시
```

### 자가수정 실행 순서
R-1. `_state.yaml` 의 `attempts` +1, `history` 에 `event: self_heal_start` append.
R-2. `qa_failures[]` 를 `assigned_to` 로 그룹화.
R-3. **그룹 순서**: `standard-analyzer` → `process-designer` → `wi-tmp-writer` → `traceability-mapper` 순서(상류부터 하류로).
R-4. 각 그룹당 해당 에이전트를 **자가수정 모드**로 재호출. 프롬프트에 명시:
   ```
   [자가수정 모드]
   아래 qa_failures 이슈만 처리하시오. 다른 작업 금지.
   이슈 목록:
   - issue_id / severity / description / fix_scope
   ...
   처리 완료 시 _state.yaml 의 qa_failures 에서 해당 issue_id 제거.
   phases.{자기} status 는 done 유지, history 에 phase_rerun_for_fix 기록.
   ```
R-5. 모든 그룹 처리 후 **Agent `qa-reviewer` 재실행**.
R-6. QA 결과로 루프 재평가.

### `assigned_to: manual` 처리
- 자동 수정 불가 → 루프 중단하고 사용자에게 직접 보고·지시 요청.

### `--skip-qa` 플래그
- QA·자가수정 루프 생략. `overall_status: done` 으로 직접 이동 (프로덕션 비권장).

---

## Phase Final: 마무리
- `00_MOC/MOC_전체표준.md` 상태 ✅ 갱신
- `_state.yaml` 의 `overall_status: done` 확인
- 플랫폼 repo 오염 검사: `git -C {PLATFORM_ROOT} status --porcelain` 이 Phase −2-0 보관본과 같은지 확인 (다르면 🚩)
- 생성/수정 파일 요약, 잔여 Issue 보고

---

## 플래그 정리

| 플래그 | 효과 |
|---|---|
| (기본) | state 감지 자동 판단, QA·자가수정 포함 |
| `--restart` | 기존 state 아카이브 후 처음부터 |
| `--resume` | 질문 없이 현재 phase 부터 자동 재개 |
| `--from <phase>` | 강제 특정 phase 부터 시작 (preflight/analyze/design/write/trace/qa) |
| `--skip-qa` | QA·자가수정 루프 생략 |
| `--cross` | trace 단계에서 교차 표준 통합 분석 포함 |
| `--max-attempts N` | 자가수정 최대 횟수 변경 (기본 3) |
| `--no-branch` | Phase −2 의 −2-2 · −2-4 skip — 조직 repo `{BASE}` 단일 브랜치 모드 (−2-0 검증 · −2-1 등록은 수행) |
| `--commit-per-phase` | 각 phase 종료 시 중간 commit (기본은 종료 시 일괄 4분할) |
| `--flow` | Phase 3.5 (flow-mapper) 만 단독 실행. PRO/WI 가 이미 존재해야 함. MAT-010 재생성. |

---

## 규칙
- 각 phase 는 **state.yaml 선행 확인** 후 진행
- 구성원칙·문서체계 위반 결정은 즉시 정지 후 질문
- REC(기록)은 본 파이프라인에서 **생성하지 않음** — 운영 단계에서만

---

## 최종 보고
- 🧭 state 요약 (attempts, 최종 overall_status, 각 phase 소요 시간)
- 📥 `{INPUTS}/` 활용 요약
- 📋 적용요건.md 경로 (`{VAULT}/02_적용요건/{슬러그}/적용요건.md`) + REQ 수
- 🔄 자가수정 루프 요약 (attempt 별 Pass/Fail, 수정 건수)
- ✅ 생성 파일 트리
- 📊 요구사항 커버리지
- 🔗 `source_citation` 누락 건수 (목표: 0)
- 📋 MAT 5종 갱신 요약
- 🚩 잔여 Issue (`manual` 에스컬레이션 + 미해결)
- 🌿 git 정보 (조직 repo 경로 · `{BASE}` / 현재 branch / origin push 결과 또는 `origin 없음` / PR 생성 안내 / 플랫폼 repo 변경 없음 확인)
- ➡️ 다음 권장 빌드 (연관 모듈·갭 보완 제안)
