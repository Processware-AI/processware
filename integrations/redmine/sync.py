"""vault → Redmine Library 단방향 동기화 메인 로직."""

from __future__ import annotations

import os
import sys
import subprocess
import argparse
from datetime import datetime, timezone
from pathlib import Path

import frontmatter
import yaml

from redmine_client import RedmineClient, client_from_config
from transformer import transform
from db import init_db, upsert_sync, get_sync, mark_failed, get_status_summary, DEFAULT_DB_PATH
from library_setup import setup_library, create_wiki_index_pages

VAULT_ROOT = Path(__file__).parents[2] / "vault"
CONFIG_PATH = Path(__file__).parent / "config.yaml"


# ── 설정 로드 ──────────────────────────────────────────────────────────────────

def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


# ── vault 파일 수집 ────────────────────────────────────────────────────────────

def collect_vault_files(changed_only: bool = False,
                        doc_id: str = None,
                        type_filter: str = None,
                        scope_filter: str = None) -> list[Path]:
    """동기화 대상 .md 파일 목록 반환."""
    if doc_id:
        matches = list(VAULT_ROOT.rglob(f"*{doc_id}*.md"))
        return matches

    if changed_only:
        result = subprocess.run(
            ["git", "diff", "HEAD~1", "HEAD", "--name-only", "--diff-filter=ACM"],
            capture_output=True, text=True,
            cwd=VAULT_ROOT.parent,
        )
        paths = [VAULT_ROOT.parent / p for p in result.stdout.splitlines()
                 if p.startswith("vault/") and p.endswith(".md")]
    else:
        paths = list(VAULT_ROOT.rglob("*.md"))

    # README, template 제외
    paths = [p for p in paths
             if p.name != "README.md"
             and "99_템플릿" not in str(p)
             and ".obsidian" not in str(p)]

    if type_filter:
        paths = [p for p in paths if _get_meta(p).get("type", "").upper() == type_filter.upper()]
    if scope_filter:
        paths = [p for p in paths
                 if scope_filter.upper() in str(_get_meta(p).get("standards", [])
                                                + [_get_meta(p).get("scope_code", "")])]
    return paths


def _get_meta(path: Path) -> dict:
    try:
        post = frontmatter.load(path)
        return post.metadata
    except Exception:
        return {}


# ── 라우팅 ────────────────────────────────────────────────────────────────────

def resolve_redmine_project(meta: dict, cfg: dict) -> str | None:
    """doc_id 또는 scope_code로 Redmine 프로젝트 identifier 결정."""
    doc_id = meta.get("doc_id", "")
    by_pro = cfg["project_mapping"].get("by_pro", {})
    by_scope = cfg["project_mapping"].get("by_scope_code", {})

    # PRO doc_id 직접 매핑
    if doc_id in by_pro:
        return by_pro[doc_id]

    # WI/TMP/EX는 parent_pro로 매핑
    parent_pro = meta.get("parent_pro", "")
    if isinstance(parent_pro, str):
        parent_pro = parent_pro.strip("[]").replace("[[", "").replace("]]", "").split("_")[0]
    if parent_pro in by_pro:
        return by_pro[parent_pro]

    # scope_code 또는 standards[0] → 상위 프로젝트
    scope_code = meta.get("scope_code") or (meta.get("standards") or [None])[0]
    if scope_code and scope_code in by_scope:
        return by_scope[scope_code]

    return None


def is_issue_type(doc_type: str, cfg: dict) -> bool:
    return doc_type.upper() in [t.upper() for t in cfg["sync_rules"]["issue_types"]]


def should_skip(meta: dict, cfg: dict) -> bool:
    status = meta.get("status", "draft")
    return status in cfg["sync_rules"]["skip_status"]


# ── 동기화 실행 ───────────────────────────────────────────────────────────────

def sync_file(path: Path, client: RedmineClient, cfg: dict,
              dry_run: bool = False) -> dict:
    """파일 1개 동기화. 결과 dict 반환."""
    try:
        post = frontmatter.load(path)
    except Exception as e:
        return {"path": str(path), "status": "error", "reason": f"parse error: {e}"}

    meta = post.metadata
    doc_id = meta.get("doc_id", path.stem)
    doc_type = meta.get("type", "")
    vault_path = str(path.relative_to(VAULT_ROOT.parent))

    if should_skip(meta, cfg):
        return {"doc_id": doc_id, "status": "skipped", "reason": "draft"}

    project_id = resolve_redmine_project(meta, cfg)
    if not project_id:
        return {"doc_id": doc_id, "status": "skipped", "reason": "no project mapping"}

    now = datetime.now(timezone.utc).isoformat()

    if is_issue_type(doc_type, cfg):
        result = _sync_as_issue(doc_id, post, meta, project_id, vault_path,
                                client, cfg, dry_run, now)
    else:
        result = _sync_as_wiki(doc_id, post, meta, project_id, vault_path,
                               client, cfg, dry_run, now)

    if not dry_run and result["status"] in ("created", "updated"):
        upsert_sync(
            vault_doc_id=doc_id,
            vault_path=vault_path,
            redmine_type=result["redmine_type"],
            redmine_project_id=project_id,
            redmine_resource=result["redmine_resource"],
            vault_version=str(meta.get("version", "")),
            synced_at=now,
        )

    return result


def _sync_as_wiki(doc_id, post, meta, project_id, vault_path,
                  client, cfg, dry_run, now) -> dict:
    doc_type = meta.get("type", "")
    wiki_title = doc_id.replace(" ", "-")
    parent_map = {"WI": "WI", "TMP": "TMP", "EX": "EX", "PRO": "PRO", "POL": "POL", "MAT": "MAT"}
    parent_title = parent_map.get(doc_type.upper())

    body = transform(post.content, meta, vault_path)

    if dry_run:
        return {
            "doc_id": doc_id, "status": "dry-run",
            "redmine_type": "wiki",
            "redmine_project": project_id,
            "redmine_resource": wiki_title,
            "parent": parent_title,
        }

    existing = get_sync(doc_id)
    client.upsert_wiki_page(project_id, wiki_title, body, parent_title)
    action = "updated" if existing else "created"
    return {
        "doc_id": doc_id, "status": action,
        "redmine_type": "wiki",
        "redmine_project": project_id,
        "redmine_resource": wiki_title,
    }


def _sync_as_issue(doc_id, post, meta, project_id, vault_path,
                   client, cfg, dry_run, now) -> dict:
    doc_type = meta.get("type", "").upper()
    tracker_name = cfg["issue_trackers"].get(doc_type, cfg["issue_trackers"].get("REC"))
    subject = f"[{doc_id}] {meta.get('title', doc_id)}"
    body = transform(post.content, meta, vault_path)

    if dry_run:
        return {
            "doc_id": doc_id, "status": "dry-run",
            "redmine_type": "issue",
            "redmine_project": project_id,
            "tracker": tracker_name,
        }

    tracker_id = client.get_tracker_id(project_id, tracker_name)
    if not tracker_id:
        return {"doc_id": doc_id, "status": "error", "reason": f"tracker '{tracker_name}' not found"}

    existing = get_sync(doc_id)
    if existing and existing["redmine_type"] == "issue":
        client.update_issue(int(existing["redmine_resource"]), subject=subject, description=body)
        return {"doc_id": doc_id, "status": "updated",
                "redmine_type": "issue", "redmine_project": project_id,
                "redmine_resource": existing["redmine_resource"]}
    else:
        issue = client.create_issue(project_id, subject, tracker_id, description=body)
        return {"doc_id": doc_id, "status": "created",
                "redmine_type": "issue", "redmine_project": project_id,
                "redmine_resource": str(issue["id"])}


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="vault → Redmine Library 동기화")
    parser.add_argument("doc_id", nargs="?", help="특정 doc_id 1건만 동기화")
    parser.add_argument("--changed", action="store_true", help="git diff 변경분만")
    parser.add_argument("--type", dest="type_filter", help="문서 유형 필터 (예: WI)")
    parser.add_argument("--scope", dest="scope_filter", help="scope_code 필터 (예: ISO27001)")
    parser.add_argument("--dry-run", action="store_true", help="실제 전송 없이 미리보기")
    parser.add_argument("--status", action="store_true", help="마지막 동기화 상태 출력")
    parser.add_argument("--setup", action="store_true",
                        help="Redmine Library 프로젝트 계층 자동 생성 + config.yaml by_pro 갱신")
    args = parser.parse_args()

    cfg = load_config()
    init_db()

    if args.status:
        summary = get_status_summary()
        print("\n[ Sync Map 현황 ]")
        for k, v in summary.items():
            print(f"  {k:12s}: {v}건")
        return

    client = client_from_config(cfg)

    if not args.dry_run:
        if not client.ping():
            print("❌ Redmine 접속 실패. URL/API KEY를 확인하세요.", file=sys.stderr)
            sys.exit(1)

    # --setup: 프로젝트 계층 생성 + config.yaml by_pro 갱신
    if args.setup:
        mode = "[DRY-RUN]" if args.dry_run else "[SETUP]"
        print(f"\n{mode} Library 프로젝트 계층 생성\n")
        result = setup_library(client, cfg, dry_run=args.dry_run)
        print(f"\n{mode} Wiki 인덱스 페이지 생성\n")
        create_wiki_index_pages(client, cfg, dry_run=args.dry_run)
        print(f"\n완료: 신규 {len(result['created'])} / "
              f"기존 {len(result['existing'])} / 건너뜀 {len(result['skipped'])}")
        return

    files = collect_vault_files(
        changed_only=args.changed,
        doc_id=args.doc_id,
        type_filter=args.type_filter,
        scope_filter=args.scope_filter,
    )

    if not files:
        print("동기화 대상 파일 없음.")
        return

    mode = "[DRY-RUN]" if args.dry_run else "[SYNC]"
    print(f"\n{mode} 대상 {len(files)}건\n")

    results = {"created": 0, "updated": 0, "skipped": 0, "error": 0, "dry-run": 0}
    for f in files:
        r = sync_file(f, client, cfg, dry_run=args.dry_run)
        status = r.get("status", "error")
        results[status] = results.get(status, 0) + 1
        icon = {"created": "✅", "updated": "🔄", "skipped": "⏭", "error": "❌", "dry-run": "👁"}.get(status, "?")
        doc = r.get("doc_id", str(f.name))
        detail = r.get("redmine_project", r.get("reason", ""))
        print(f"  {icon} {status:8s}  {doc}  →  {detail}")

    print(f"\n완료: 생성 {results['created']} / 갱신 {results['updated']} / "
          f"건너뜀 {results['skipped']} / 오류 {results['error']}")


if __name__ == "__main__":
    main()
