---
type: session-recap
date: 2026-05-06
title: "Redmine 연동 구현 — Phase 1~5 전체 완료"
participants: ["dongseok"]
tags: [session, integration, redmine, vault-push, workspace, phase5, implementation]
---

# 세션 회고 — 2026-05-06 (3차)

## 1. 출발점

이전 세션(2차)에서 Headless CMS 모델 + Redmine 단방향 Push 아키텍처 설계까지 완료. 이번 세션에서 Phase 1~5 전체 구현 진행.

---

## 2. Phase 1 — 핵심 모듈 구현

### 구현 파일

| 파일 | 내용 |
|---|---|
| `publish/redmine/config.yaml` | Redmine URL/API KEY + project_mapping (by_scope_code, by_pro) + sync_rules + issue_trackers + custom_fields |
| `publish/redmine/requirements.txt` | python-frontmatter≥1.1.0, requests≥2.31.0, PyYAML≥6.0.1 |
| `publish/redmine/redmine_client.py` | RedmineClient — get/create project, upsert_wiki_page, create/update issue, ping, client_from_config |
| `publish/redmine/db.py` | SQLite: sync_map + workspace_map, init_db, upsert_sync, get_sync, mark_failed, get_status_summary |

### 주요 결정

- **SQLite DB**: sync_map 테이블로 vault_doc_id ↔ Redmine resource 매핑 추적 (갱신/재시도 판단)
- **Python 3.9 호환**: `from __future__ import annotations` + `Optional[T]` 사용 (나중에 `X | Y` 타입 오류 수정)

---

## 3. Phase 2 — 변환 + 메인 동기화 CLI

### 구현 파일

| 파일 | 내용 |
|---|---|
| `publish/redmine/transformer.py` | `transform()` — `_strip_frontmatter`, `_convert_wikilinks` (Obsidian `[[link]]` → Redmine), 자동생성 헤더 삽입 |
| `publish/redmine/sync.py` | CLI 메인: collect_vault_files, resolve_redmine_project, sync_file, `_sync_as_wiki`, `--setup`, `--changed`, `--dry-run`, `--status` |

### 동기화 규칙

- `status: draft` → skip
- POL/PRO/WI/TMP/EX/MAT → Wiki 페이지
- REC/REC-NCR → Issue (별도 issue_sync.py 위임)

---

## 4. Phase 3 — Library 초기화 + 이슈 동기화

### 구현 파일

| 파일 | 내용 |
|---|---|
| `publish/redmine/library_setup.py` | PRO 파일 스캔 → `lib-*` 프로젝트 자동 생성 → config.yaml `by_pro` 자동 갱신 + Wiki 인덱스 페이지 생성 |
| `publish/redmine/issue_sync.py` | REC → Redmine Issue, STATUS_MAP/PRIORITY_MAP, custom_fields, _find_existing_issue (DB 우선, custom field fallback), journal notes (갱신 시) |

### STATUS_MAP / PRIORITY_MAP

```
vault status → Redmine 상태
  open / in_progress → "진행중"
  closed / done      → "완료"
  withdrawn          → "종결"

NCR severity → Redmine 우선순위
  critical → "긴급"
  major    → "높음"
  minor    → "보통"
```

---

## 5. Phase 4 — Workspace

### 개념 확립 과정

- 초기에 "Redmine 프로젝트"와 "현업 프로젝트"가 동일 용어로 혼용되어 혼란 발생
- **Workspace** 개념 도입: 현업 업무를 위한 가상 공간 → Redmine에서는 복수 프로젝트로 구현
- Library Module: `lib-{scope_code}-{pro_slug}` (vault 관리, READ ONLY)
- Workspace Module: `ws-{slug}-{scope}-{pro_slug}` (팀 소유, 자율 편집)

### 구현 파일

`publish/redmine/workspace.py` — `cmd_create`, `cmd_sync`, `cmd_list`, `cmd_status`

### 버그 수정

1. **멀티 표준 충돌**: ISO27001과 CMMI가 동일한 PRO 번호(p001-001)를 가질 때 Workspace 서브프로젝트 identifier 충돌
   - 수정: `_pro_slug_from_identifier`가 scope 포함 전체 반환 (`iso27001-p001-001`, `cmmi-p001-001`)

2. **dry-run NoneType 오류**: `_copy_wiki_pages(client=None, dry_run=True)` 진입 시 `client.list_wiki_pages()` 호출
   - 수정: `dry_run=True`일 때 early return

3. **Python 3.9 `|` 타입 오류**: `sqlite3.Row | None` 구문 오류
   - 수정: 모든 관련 파일에 `from __future__ import annotations` + `Optional` import

---

## 6. Phase 5 — 자동화 인프라

### 구현 파일

| 파일 | 내용 |
|---|---|
| `publish/redmine/post-commit.hook` | git post-commit hook: `vault/*.md` 변경 감지 → 백그라운드 `sync.py --changed` |
| `publish/redmine/install-hook.sh` | hook 설치 스크립트: 기존 hook에 append 또는 신규 생성 |
| `.github/workflows/vault-push.yml` | GitHub Actions: `feat/*-output`, `main` 브랜치 + `vault/**/*.md` 트리거 → sync.py --changed → artifact 업로드 |

### GitHub Actions 특이사항

- `on:` 키가 PyYAML에서 Python `True`로 파싱됨 → GitHub Actions 자체는 정상 동작 (GitHub 파서가 처리)
- `fetch-depth: 2` 필요 (`--changed`가 HEAD~1 diff 사용)
- `REDMINE_URL` secret → Python 스크립트로 config.yaml에 패치 후 실행

---

## 7. 스킬 등록

| 파일 | 역할 |
|---|---|
| `.claude/commands/vault-push.md` | `/vault-push` 스킬: sync.py 옵션 전체 문서화 |
| `.claude/commands/workspace-create.md` | `/workspace-create` 스킬: workspace.py 4개 subcommand |

---

## 8. 산출물 목록

```
publish/redmine/
  config.yaml          (설정)
  requirements.txt     (의존성)
  redmine_client.py    (API 래퍼)
  db.py                (SQLite 상태 DB)
  transformer.py       (Obsidian→Redmine 변환)
  sync.py              (메인 CLI)
  library_setup.py     (Library 초기화)
  issue_sync.py        (REC/NCR → Issue)
  workspace.py         (Workspace 관리)
  post-commit.hook     (git hook)
  install-hook.sh      (hook 설치)
.github/workflows/vault-push.yml
.claude/commands/vault-push.md
.claude/commands/workspace-create.md
docs/Redmine_연동_설계서.md          (아키텍처 설계 문서)
```

---

## 9. 핵심 아키텍처 원칙

### Headless CMS 모델

```
vault (SSoT) ──→ /vault-push ──→ Redmine Process Library (READ ONLY)
                                      │
                                      └─→ /workspace-create ──→ Workspace (팀 편집)
```

- **단방향**: vault → Redmine. Redmine에서 vault로 역방향 없음
- **SSoT 강제**: Library Module 직접 편집 금지 (자동생성 헤더로 명시)
- **분리**: Library(원본)와 Workspace(복사본) 명확히 구분

---

## 10. 다음 단계 (미구현)

| 항목 | 내용 |
|---|---|
| Notion 연동 | vault → Notion Database API |
| Codebeamer 연동 | vault → TrackerItem REST API |
| AI Agent Gateway | Hermes/OpenClaw 등 AI agent가 vault API 직접 호출 |
| webhook receiver | Redmine/Jira → vault NCR 역방향 (선택적) |
| 멀티 조직 vault 격리 | 조직A / 조직B 독립 vault 운영 |
