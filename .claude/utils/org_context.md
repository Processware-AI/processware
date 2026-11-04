---
type: util-spec
title: 조직 컨텍스트 — 활성 조직 루트 해석 규약 (org-layer §3 단계 1)
version: "0.1"
owner: "QMR"
status: impl                            # tools/org/ 구현 완료. 단계 2(경로 치환)·3(sync-core) 는 미착수
created: 2026-11-04
related_commands: [process-ingest, process-plan, process-do, process-backfill, process-check, process-audit, process-act, vault-push, workspace-create]
related_agents: ["(전체 — 단계 2 에서 경로 변수 치환 시 적용)"]
related_docs: ["docs/architecture/org-layer.md"]
---

# 조직 컨텍스트 — 활성 조직 루트 해석 규약

> 모든 슬래시 커맨드와 에이전트는 **활성 조직 루트** 를 기준으로 경로를 해석한다.
> 해석은 플랫폼 CLI `python3 -m tools.org` 에 위임하고, 결과를 환경변수 형태로 받아 쓴다.

---

## 1. 해석 우선순위

| 순위 | 근거 | 예 |
|---|---|---|
| 1 | 커맨드 인자 `--org-root <path>` | `/process-do WI-QMS-01-01-01 --org-root /work/acme` |
| 2 | 커맨드 인자 `--org <id>` (레지스트리 `~/.processware/orgs.yaml` 조회) | `/process-check start PRO-QMS-01 --org acme` |
| 3 | 환경변수 `PROCESSWARE_ORG_ROOT` | `export PROCESSWARE_ORG_ROOT=/work/acme` |
| 4 | 환경변수 `PROCESSWARE_ORG` (레지스트리 조회) | `export PROCESSWARE_ORG=acme` |
| 5 | **fallback: default 조직** = 플랫폼 repo 의 `vault/` | (아무것도 없을 때) |

> fallback 은 **단계 3 마이그레이션 완료 후 제거** 된다 (2026-11-04 결정). 그 이후 미설정 시 커맨드는 즉시 실패한다.

---

## 2. 해석 절차 (커맨드 진입 직후 1회)

```bash
python3 -m tools.org context --format env [--org <id> | --org-root <path>]
```

exit ≠ 0 이면 **즉시 중단** 하고 stderr 메시지를 사용자에게 그대로 보여준다 (org.yaml 누락·검증 실패·레지스트리 미등록 등).

출력 (환경변수 형식):

| 변수 | 의미 | default 모드 값 | 조직 모드 값 |
|---|---|---|---|
| `PROCESSWARE_ORG_ID` | 조직 id | `default` | org.yaml 의 `org_id` |
| `PROCESSWARE_ORG_MODE` | `default` \| `org` | `default` | `org` |
| `PROCESSWARE_ORG_SOURCE` | 해석 근거 | `fallback:default` | `arg:org-root` 등 |
| `PROCESSWARE_ORG_ROOT` | 조직 루트 | 플랫폼 repo 루트 | `{ORG_ROOT}` |
| `PROCESSWARE_VAULT` | Obsidian vault | `{repo}/vault` | `{ORG_ROOT}/vault` |
| `PROCESSWARE_INPUTS` | ingest 산출물 | `{repo}/inputs` | `{ORG_ROOT}/inputs` |
| `PROCESSWARE_SOURCES` | 원본 파일 | `{repo}/sources` | `{ORG_ROOT}/sources` |
| `PROCESSWARE_RUNS` | 실행 trace | `{repo}/.claude/runs` | `{ORG_ROOT}/.processware/runs` |
| `PROCESSWARE_QUEUES` | 인계 큐 (하위 `process-act/`) | `{repo}/.claude/queues` | `{ORG_ROOT}/.processware/queues` |
| `PROCESSWARE_STATES` | 차원 1 체크포인트 | `{repo}/.claude/states` | `{ORG_ROOT}/.processware/states` |
| `PROCESSWARE_PLATFORM_ROOT` | 플랫폼 repo 루트 (에이전트·규칙·템플릿) | `{repo}` | `{repo}` |
| `PROCESSWARE_ORG_YAML` | org.yaml 경로 | (빈 값) | `{ORG_ROOT}/org.yaml` |

커맨드는 시작 시 다음 1줄을 출력하고 trace 의 첫 이벤트에 `org_id` · `org_root` · `org_source` 를 기록한다:

```
조직: {PROCESSWARE_ORG_ID} ({PROCESSWARE_ORG_MODE}) · 루트: {PROCESSWARE_ORG_ROOT}
```

default 모드일 때는 추가로 fallback 경고를 그대로 전달한다 (stderr 의 `[org] …` 줄).

---

## 3. 경로 치환 규칙 — 단계 2 완료 전 임시 브리지

커맨드·에이전트 정의 문서에 적힌 리터럴 경로는 아래 표대로 **읽어서 해석** 한다. 단계 2 에서 문서 자체가 변수 표기로 치환되면 이 절은 삭제된다.

| 문서의 리터럴 | 해석 |
|---|---|
| `vault/…` | `{PROCESSWARE_VAULT}/…` |
| `inputs/…` | `{PROCESSWARE_INPUTS}/…` |
| `sources/…` | `{PROCESSWARE_SOURCES}/…` |
| `.claude/runs/…` | `{PROCESSWARE_RUNS}/…` |
| `.claude/queues/…` | `{PROCESSWARE_QUEUES}/…` |
| `.claude/states/…` | `{PROCESSWARE_STATES}/…` |

**치환하지 않는 플랫폼 자산**: `.claude/agents|commands|utils|rbac`, `tools/`, `docs/`, `core/` (단계 3 신설). 이들은 항상 `{PROCESSWARE_PLATFORM_ROOT}` 기준이다.

> 주의: default 모드에서는 두 표현이 같은 경로를 가리키므로 동작 차이가 없다. 조직 모드에서만 분기된다.

---

## 4. 격리 원칙

- 활성 조직 루트 **밖** 의 vault/inputs/sources/runs/queues/states 에는 읽기·쓰기 모두 하지 않는다.
- 플랫폼 자산은 읽기 전용. `/process-act` 의 개정 제안도 조직 vault 안의 자산만 대상으로 한다.
- 단계 5 에서 `tools.org.OrgContext.contains(path)` 를 qa-reviewer 와 `vault_rules validate` 가 강제한다.

---

## 5. Python 도구와의 연동

- `tools/vault_rules` — `--vault` 미지정 시 활성 조직의 vault 를 기본값으로 쓴다. `next-seq --glob` 의 상대 경로는 조직 루트 기준.
- `publish/redmine/*` — 단계 6 전까지는 default 모드 전제. 조직 모드에서 `/vault-push` 를 호출하면 환경변수를 그대로 하위 프로세스에 넘기되, Python 쪽은 아직 `vault/` 리터럴을 쓴다 (알려진 제한).
- 라이브러리 사용: `from tools.org import resolve; ctx = resolve()` → `ctx.vault`, `ctx.runs` …

---

## 6. 조직 루트 만들기 · 등록

```bash
python3 -m tools.org init /work/acme --org-id acme --name "ACME 주식회사" --register
export PROCESSWARE_ORG_ROOT=/work/acme          # 또는 export PROCESSWARE_ORG=acme
python3 -m tools.org validate                     # org.yaml 검증
python3 -m tools.org list                         # 등록된 조직
```

`init` 은 `org.yaml` + 폴더 뼈대만 만든다. vault 의 공통 폴더(00_공통관리 · 01_구성원칙 · 99_템플릿) 복사는 **단계 3 `sync-core`** 에서 제공한다. 그 전까지 조직 모드로 `/process-plan` 을 돌리면 기준 문서를 찾지 못한다.

`org.yaml` 스키마: `tools/org/schema.py` (필수 `org_id` · `name`, 선택 `scopes` · `rbac.users` · `redmine`).
