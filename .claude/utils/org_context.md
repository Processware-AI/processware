---
type: util-spec
title: 조직 컨텍스트 — 활성 조직 루트 해석 규약 (org-layer §3 단계 1~7)
version: "0.8"
owner: "QMR"
status: impl                            # 단계 1 tools/org/ + 단계 2 경로 변수화 + 단계 3 sync-core 완료
created: 2026-11-04
related_commands: [process-ingest, process-plan, process-do, process-backfill, process-check, process-audit, process-act, vault-push, workspace-create]
related_agents: ["(전체 29 — 경로 변수 {VAULT} {INPUTS} {SOURCES} {RUNS} {QUEUES} {STATES} 사용)"]
related_docs: ["docs/architecture/org-layer.md"]
---

# 조직 컨텍스트 — 활성 조직 루트 해석 규약

> 모든 슬래시 커맨드와 에이전트는 **활성 조직 루트** 를 기준으로 경로를 해석한다.
> 플랫폼 repo 에는 vault 가 없다. 조직 자산은 전부 조직 루트(별도 git repo)에 있고, 해석은 플랫폼 CLI `python3 -m tools.org` 에 위임한다.

---

## 1. 해석 우선순위

| 순위 | 근거 | 예 |
|---|---|---|
| 1 | 커맨드 인자 `--org-root <path>` | `/process-do WI-QMS-01-01-01 --org-root /work/acme` |
| 2 | 커맨드 인자 `--org <id>` (레지스트리 `~/.processware/orgs.yaml` 조회) | `/process-check start PRO-QMS-01 --org acme` |
| 3 | 환경변수 `PROCESSWARE_ORG_ROOT` | `export PROCESSWARE_ORG_ROOT=/work/acme` |
| 4 | 환경변수 `PROCESSWARE_ORG` (레지스트리 조회) | `export PROCESSWARE_ORG=acme` |

어느 것도 없으면 **즉시 실패** 한다. default fallback 은 단계 3 마이그레이션과 함께 제거되었다 (2026-11-04 결정).

---

## 2. 해석 절차 (커맨드 진입 직후 1회)

```bash
python3 -m tools.org context --format env [--org <id> | --org-root <path>]
```

exit ≠ 0 이면 **즉시 중단** 하고 stderr 메시지를 사용자에게 그대로 보여준다 (조직 미지정 · org.yaml 누락 · 검증 실패 · 레지스트리 미등록).

출력 (환경변수 형식):

| 변수 | 의미 | 값 |
|---|---|---|
| `PROCESSWARE_ORG_ID` | 조직 id | org.yaml 의 `org_id` |
| `PROCESSWARE_ORG_MODE` | 항상 `org` | `org` |
| `PROCESSWARE_ORG_SOURCE` | 해석 근거 | `arg:org-root` · `arg:org` · `env:PROCESSWARE_ORG_ROOT` · `env:PROCESSWARE_ORG` |
| `PROCESSWARE_ORG_ROOT` | 조직 루트 | `{ORG_ROOT}` |
| `PROCESSWARE_VAULT` | Obsidian vault | `{ORG_ROOT}/vault` |
| `PROCESSWARE_INPUTS` | ingest 산출물 | `{ORG_ROOT}/inputs` |
| `PROCESSWARE_SOURCES` | 원본 파일 | `{ORG_ROOT}/sources` |
| `PROCESSWARE_RUNS` | 실행 trace | `{ORG_ROOT}/.processware/runs` |
| `PROCESSWARE_QUEUES` | 인계 큐 (하위 `process-act/`) | `{ORG_ROOT}/.processware/queues` |
| `PROCESSWARE_STATES` | 차원 1 체크포인트 | `{ORG_ROOT}/.processware/states` |
| `PROCESSWARE_PLATFORM_ROOT` | 플랫폼 repo 루트 (에이전트 · 규칙 · 템플릿 · core/) | 플랫폼 체크아웃 경로 |
| `PROCESSWARE_ORG_YAML` | org.yaml 경로 | `{ORG_ROOT}/org.yaml` |

커맨드는 시작 시 다음 1줄을 출력하고 trace 의 첫 이벤트에 `org_id` · `org_root` · `org_source` 를 기록한다:

```
조직: {PROCESSWARE_ORG_ID} · 루트: {PROCESSWARE_ORG_ROOT}
```

---

## 3. 경로 변수 표기 (단계 2)

커맨드 · 에이전트 정의 문서는 리터럴 경로 대신 아래 **경로 변수** 를 쓴다. 커맨드가 §2 의 해석 결과를 변수에 바인딩하고, 에이전트 위임 시 값을 프롬프트 첫머리에 전달한다.

| 변수 | 바인딩 원천 | 경로 |
|---|---|---|
| `{VAULT}` | `PROCESSWARE_VAULT` | `{ORG_ROOT}/vault` |
| `{INPUTS}` | `PROCESSWARE_INPUTS` | `{ORG_ROOT}/inputs` |
| `{SOURCES}` | `PROCESSWARE_SOURCES` | `{ORG_ROOT}/sources` |
| `{RUNS}` | `PROCESSWARE_RUNS` | `{ORG_ROOT}/.processware/runs` |
| `{QUEUES}` | `PROCESSWARE_QUEUES` | `{ORG_ROOT}/.processware/queues` |
| `{STATES}` | `PROCESSWARE_STATES` | `{ORG_ROOT}/.processware/states` |

**변수화하지 않는 플랫폼 자산**: `.claude/agents|commands|utils|rbac`, `tools/`, `docs/`, `core/`. 항상 `{PROCESSWARE_PLATFORM_ROOT}` 기준이다.

**frontmatter 는 예외**: 커맨드 · 에이전트의 `description` · `argument-hint` 는 사용자가 실제로 타이핑하는 예시(`/process-ingest sources/ISO9001.pdf`)이므로 리터럴을 유지한다. 사용자가 준 상대 경로는 커맨드가 `{SOURCES}` 등 활성 조직 루트 기준으로 해석한다.

**사용자 가이드 (`{VAULT}/09_REF_참고자료/*_가이드.md` · `사용자_매뉴얼/`)** 는 `vault/`, `.claude/runs/` 같은 리터럴로 설명한다. 조직 루트 기준으로 읽는다 (`.claude/runs` → `.processware/runs`). 본문 갱신은 후속 과제.

---

## 4. 격리 원칙

- 활성 조직 루트 **밖** 의 vault/inputs/sources/runs/queues/states 에는 읽기 · 쓰기 모두 하지 않는다.
- 플랫폼 자산은 읽기 전용. `/process-act` 의 개정 제안도 조직 vault 안의 자산만 대상으로 한다.
- `{VAULT}/00_공통관리` · `01_구성원칙` · `99_템플릿` · 각 폴더 `README.md` 는 **플랫폼 관리(managed)** 파일이다. 에이전트는 이 파일들을 수정하지 않는다 (sync-core 가 덮어쓴다). 조직별 추가는 별도 파일로.
- git 작업(branch · commit · push)은 조직 루트 repo 에서만 수행한다 — 항상 `git -C {ORG_ROOT} …` (작업 디렉토리는 바꾸지 않는다). 플랫폼 repo 에서는 git 명령을 실행하지 않는다. 조직 루트가 다른 repo(특히 플랫폼 repo) 안에 중첩되어 있으면 중단한다. 브랜치 규약(branch-per-standard · 기준 브랜치 판정 · 등록 위치 · 재개)은 `/process-plan` Phase −2 가 정의한다.
- 관리 폴더 안의 조직 추가 파일은 `*_조직추가.md` 패턴만 허용된다 (`core/vault_base/_manifest.yaml` → `org_owned`). 예: `00_공통관리/07_표준분류레지스트리_조직추가.md`.
- **강제 (단계 5)** — `tools/org/guard.py` 가 경로를 org / platform / outside 로 분류하고 쓰기를 판정한다 (org 허용 · managed 거부 · platform 거부 · outside 거부):
  1. **Claude Code 훅**: `.claude/settings.json` PreToolUse (Write/Edit/MultiEdit/NotebookEdit) → `python3 -m tools.org.hook_guard`. 조직 컨텍스트가 있을 때 managed 파일 · 제거된 플랫폼 `vault/` 등 · outside 쓰기를 exit 2 로 차단. 플랫폼 자산 편집(개발 작업)은 차단하지 않는다.
  2. **`tools.vault_rules validate`**: 조직 vault 밖이거나 managed 파일이면 `격리 위반` 오류.
  3. **qa-reviewer §13**: 산출물 전수를 `python3 -m tools.org guard --mode write --path …` 로 검사, 위반은 blocker.

---

## 5. Python 도구와의 연동

- `tools/vault_rules` — `--vault` 미지정 시 활성 조직의 vault 를 쓴다. 조직 미지정 시 실패. `next-seq --glob` 의 상대 경로는 조직 루트 기준.
- `tools/org sync-core` — 플랫폼 `core/vault_base` → `{VAULT}`, `core/org_base` → `{ORG_ROOT}` 동기화. `core/vault_base/_manifest.yaml` 의 managed(덮어쓰기) / seed(없을 때만) 규칙.
- `tools/org overview` — 교차 조직 뷰 (단계 7). 레지스트리의 모든 조직을 읽기 전용으로 집계 (`--format table|md|json`, `--out`, `--org`, `--root`). 어떤 조직 루트에도 쓰지 않는다.
- `tools/org guard` — 격리 판정 (단계 5). `--path` 반복, `--mode read|write`, `--allow-platform`, exit 0/2. 훅 진입점은 `tools/org/hook_guard.py`.
- `tools/org rbac` — 권한 판정 (단계 4). 역할 정의 `.claude/rbac/policy.yaml` (플랫폼) + 배정 `org.yaml` → `rbac` (조직). `check --user U --action A [--target T]` exit 0/2, `independence --auditor A --executors a,b`, `roles`, `users`, `log`. 감사 로그 `{ORG_ROOT}/.processware/rbac_audit.jsonl`. 사용자 기본값 `PROCESSWARE_USER`.
- `publish/*` — `publish/orgctx.py` 가 활성 조직을 해석한다 (단계 6). vault `{VAULT}`, 설정 `{ORG_ROOT}/publish/{target}/config.yaml`, sync_map `{ORG_ROOT}/.processware/publish/{target}_sync.db`, 접두어 org.yaml `redmine.project_prefix`. 실제 전송은 org.yaml `redmine.enabled: true` 일 때만.
- 라이브러리 사용: `from tools.org import resolve; ctx = resolve()` → `ctx.vault`, `ctx.runs` …

---

## 6. 조직 루트 만들기 · 갱신

```bash
python3 -m tools.org init /work/acme --org-id acme --name "ACME 주식회사" --register
#   → org.yaml + sources/ inputs/ vault/ .processware/ 생성 + sync-core (vault 공통 폴더 · MAT 시드 · 조직 README · .gitignore)
export PROCESSWARE_ORG_ROOT=/work/acme            # 또는 export PROCESSWARE_ORG=acme
python3 -m tools.org context --format table       # 해석 확인
python3 -m tools.org validate                     # org.yaml 검증
python3 -m tools.org sync-core [--dry-run] [-v]   # 플랫폼 갱신 반영 — managed 덮어쓰기 · seed 보존 · platform_version 갱신
python3 -m tools.org sync-core --force            # seed(MAT · MOC) 재시드 (조직 내용 덮어씀 — 주의)
python3 -m tools.org list                         # 등록된 조직
```

`org.yaml` 스키마: `tools/org/schema.py` (필수 `org_id` · `name`, 선택 `scopes` · `rbac.users` · `redmine`). `platform_version` 은 sync-core 가 자동 갱신한다.
