---
description: vault → 외부 시스템 Process Library 단방향 동기화. final 상태 문서를 Library Module로 push. --target으로 백엔드 선택 (기본값: publish/config.yaml의 default_target).
---

vault를 외부 시스템 Process Library에 단방향 Push하는 스킬입니다.

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

## 사용법

```
/vault-push [--target <backend>] [옵션]
```

| 명령 | 동작 |
|---|---|
| `/vault-push` | vault 전체 → Library 동기화 |
| `/vault-push --changed` | git diff 변경분만 |
| `/vault-push --setup` | Library 프로젝트 계층 자동 생성 |
| `/vault-push --setup --dry-run` | 생성 예정 프로젝트 미리보기 |
| `/vault-push WI-ISO27001-001-001-001` | 특정 문서 1건 |
| `/vault-push --type WI` | WI 전체 |
| `/vault-push --scope ISO27001` | 특정 표준 전체 |
| `/vault-push --dry-run` | 실제 전송 없이 미리보기 |
| `/vault-push --status` | 마지막 동기화 상태 |
| `/vault-push --target confluence` | Confluence 백엔드 사용 |

## 지원 백엔드

| backend | 어댑터 경로 | 상태 |
|---|---|---|
| `redmine` | `publish/redmine/adapter.py` | 구현 완료 |
| 기타 | `publish/{target}/adapter.py` | 어댑터 추가 시 자동 인식 |

기본값은 `publish/config.yaml`의 `default_target` 필드로 지정합니다.

## 실행 방법

모든 데이터(vault · 설정 · sync_map DB · 로그)는 **활성 조직 루트** 에 있고, 코드는 플랫폼에 있다 (org-layer 단계 6).

```bash
export PROCESSWARE_ORG_ROOT=/work/acme            # 또는 --org/--org-root → 하위 호출 전 export
python3 publish/dispatcher.py push [--target <backend>] [옵션]
```

예시:
```bash
python3 publish/dispatcher.py push --dry-run                 # enabled 와 무관하게 미리보기 가능
python3 publish/dispatcher.py push --target redmine --changed # 조직 루트 repo 의 HEAD~1 diff
python3 publish/dispatcher.py push --setup                    # lib-{prefix}-{scope}(없으면 생성) + lib-{prefix}-{scope}-{pro_slug}
```

Redmine 식별자는 조직 접두어(org.yaml `redmine.project_prefix`, 기본 org_id)를 포함한다: `lib-{prefix}-{scope}` · `lib-{prefix}-{scope}-{pro_slug}` · `ws-{prefix}-{slug}`.

## 사전 조건

1. 조직 루트 `org.yaml` → `redmine.enabled: true` (false 면 `--dry-run` · `--status` 외 호출은 전송 전에 중단)
2. `{ORG_ROOT}/publish/{target}/config.yaml` 에 접속 정보 입력 (`sync-core` 가 `core/org_base` 에서 시드)
3. 환경변수 설정: `export REDMINE_API_KEY=your_key` (Redmine 사용 시)
4. 의존 패키지 설치: `pip3 install -r publish/{target}/requirements.txt` (플랫폼)
5. `/vault-push --setup` 으로 Library 구조 초기화 (최초 1회) — `by_pro` 가 조직 config 에 자동 기록
6. 자동 push: 조직 repo 에 `bash publish/redmine/install-hook.sh --org-root {ORG_ROOT}` (post-commit) 또는 시드된 `.github/workflows/vault-push.yml` (시크릿 REDMINE_URL · REDMINE_API_KEY)

## 새 백엔드 추가 방법

1. `publish/{target}/` 폴더 생성
2. `publish/{target}/adapter.py` 에 `BaseAdapter` 상속 클래스 구현
3. `publish/{target}/config.yaml` 작성
4. `publish/config.yaml` 의 `default_target` 변경 (선택)

## 이 스킬이 호출되면

1. 조직 컨텍스트 해석 (공통 절) → `PROCESSWARE_ORG_ROOT` export
2. `publish/config.yaml` 에서 `default_target` 확인 (또는 `--target` 인수 우선)
3. `publish/{target}/adapter.py` 동적 로드
4. `{ORG_ROOT}/publish/{target}/config.yaml` 설정 로드 (없으면 `sync-core` 안내 후 중단)
5. 실제 전송이면 org.yaml `redmine.enabled` 확인
6. 사용자 요청에 맞는 메서드 실행
7. 결과(생성/갱신/건너뜀/오류) 보고 — sync_map 은 `{ORG_ROOT}/.processware/publish/{target}_sync.db`
