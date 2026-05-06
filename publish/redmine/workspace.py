"""
Workspace 생성·동기화·목록 조회.

Workspace = 현업 업무 단위를 묶은 가상 업무공간.
  ws-{slug}               : 상위 Redmine 프로젝트
  ws-{slug}-{pro_slug}    : PRO 단위 서브프로젝트 (Library Module 복사본)

CLI:
  python3 workspace.py create --name "..." --slug "..." --modules PRO-XXX,PRO-YYY
  python3 workspace.py sync   --workspace ws-{slug} --module lib-{scope}-{pro_slug}
  python3 workspace.py list
  python3 workspace.py status --workspace ws-{slug}
  (모든 subcommand에 --dry-run 지원)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import yaml

from redmine_client import RedmineClient, client_from_config
from db import init_db, upsert_workspace, list_workspaces, get_conn

CONFIG_PATH = Path(__file__).parent / "config.yaml"

_IDENT_RE = re.compile(r"[^a-z0-9\-]")

WORKSPACE_HEADER = """\
> **[워크스페이스 복사본]** 이 문서는 `{source_module}` Library Module에서 복사되었습니다.
> 복사 일시: {copied_at} | 이후 편집은 팀 자율.
> Library 최신 버전으로 업데이트하려면: `python3 workspace.py sync --workspace {ws_slug} --module {source_module}`

---

"""


# ── 유틸 ──────────────────────────────────────────────────────────────────────

def _slugify(text: str) -> str:
    return _IDENT_RE.sub("-", text.lower()).strip("-")


def _pro_slug_from_identifier(identifier: str) -> str:
    """
    lib-iso27001-p001-001 → iso27001-p001-001
    lib-cmmi-p001-001     → cmmi-p001-001
    scope + pro번호 조합으로 멀티 표준 혼합 시 충돌 방지.
    """
    # "lib-" 접두어 제거
    without_lib = identifier.removeprefix("lib-")
    return without_lib   # e.g., iso27001-p001-001


def _load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


# ── Wiki 복사 ─────────────────────────────────────────────────────────────────

def _copy_wiki_pages(client: Optional[RedmineClient],
                     src_project: str, dst_project: str,
                     ws_slug: str, dry_run: bool = False) -> list[str]:
    """src_project의 모든 wiki 페이지를 dst_project에 복사."""
    if dry_run:
        print(f"    👁  wiki 복사 예정: {src_project} → {dst_project}")
        return ["(dry-run)"]

    try:
        pages = client.list_wiki_pages(src_project)
    except Exception as e:
        print(f"    ⚠️  wiki 목록 조회 실패 ({src_project}): {e}")
        return []

    copied = []
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")

    for page_meta in pages:
        title = page_meta["title"]
        try:
            page = client.get_wiki_page(src_project, title)
            if not page:
                continue
            original_text = page.get("text", "")
        except Exception as e:
            print(f"    ⚠️  {title} 조회 실패: {e}")
            continue

        # Library 자동생성 헤더 제거 → 워크스페이스 헤더로 교체
        text = _replace_library_header(original_text, src_project, ws_slug, now_str)

        if dry_run:
            print(f"    👁  copy wiki  {src_project}/{title} → {dst_project}/{title}")
            copied.append(title)
            continue

        try:
            client.upsert_wiki_page(dst_project, title, text,
                                     parent_title=page_meta.get("parent", {}).get("title"))
            copied.append(title)
        except Exception as e:
            print(f"    ⚠️  {title} 복사 실패: {e}")

    return copied


def _replace_library_header(text: str, source_module: str,
                              ws_slug: str, copied_at: str) -> str:
    """Library 자동생성 헤더 블록을 워크스페이스 헤더로 교체."""
    ws_header = WORKSPACE_HEADER.format(
        source_module=source_module,
        copied_at=copied_at,
        ws_slug=ws_slug,
    )
    # "**[자동생성]**" 헤더 블록 제거 ("> ... \n---\n" 패턴)
    cleaned = re.sub(
        r"^(>.*\n)+---\n\n?",
        "",
        text,
        flags=re.MULTILINE,
    )
    return ws_header + cleaned


# ── create ────────────────────────────────────────────────────────────────────

def cmd_create(client: RedmineClient, cfg: dict, args) -> int:
    slug = _slugify(args.slug)
    ws_identifier = f"ws-{slug}"
    by_pro = cfg["project_mapping"].get("by_pro") or {}
    module_ids = [m.strip() for m in args.modules.split(",") if m.strip()]

    if not module_ids:
        print("❌ --modules 에 PRO doc_id를 하나 이상 지정하세요.", file=sys.stderr)
        return 1

    # 각 PRO → Library Module identifier 확인
    resolved: list[tuple[str, str]] = []   # (pro_doc_id, lib_identifier)
    for pro_id in module_ids:
        lib_id = by_pro.get(pro_id)
        if not lib_id:
            print(f"  ⚠️  '{pro_id}' 에 대한 Library Module 매핑 없음."
                  f" config.yaml by_pro 또는 --setup 실행 확인.", file=sys.stderr)
            continue
        resolved.append((pro_id, lib_id))

    if not resolved:
        print("❌ 유효한 Library Module이 없습니다.", file=sys.stderr)
        return 1

    mode = "[DRY-RUN]" if args.dry_run else "[CREATE]"
    print(f"\n{mode} Workspace: {args.name}  ({ws_identifier})\n")

    # 상위 프로젝트 생성
    if args.dry_run:
        print(f"  👁  parent project  {ws_identifier}  '{args.name}'")
        parent_id = None
    else:
        parent_proj, created = client.get_or_create_project(
            identifier=ws_identifier,
            name=args.name,
            description=getattr(args, "description", ""),
        )
        parent_id = parent_proj["id"]
        icon = "✅" if created else "·"
        print(f"  {icon}  {'created' if created else 'existing'}  {ws_identifier}")

    # PRO별 서브프로젝트 생성 + wiki 복사
    source_modules = []
    for pro_id, lib_id in resolved:
        pro_slug = _pro_slug_from_identifier(lib_id)
        sub_identifier = f"ws-{slug}-{pro_slug}"
        sub_name = f"[{pro_id}] {sub_identifier}"

        source_modules.append(lib_id)

        if args.dry_run:
            print(f"\n  👁  sub-project  {sub_identifier}  ← {lib_id}")
            _copy_wiki_pages(client, lib_id, sub_identifier, ws_identifier,
                             dry_run=True)
            continue

        sub_proj, sub_created = client.get_or_create_project(
            identifier=sub_identifier,
            name=sub_name,
            parent_id=parent_id,
            description=f"Workspace Module: {pro_id} (from {lib_id})",
        )
        icon = "✅" if sub_created else "·"
        print(f"\n  {icon}  {'created' if sub_created else 'existing'}  {sub_identifier}")

        # wiki 복사
        print(f"    → wiki 복사 중: {lib_id} → {sub_identifier}")
        copied = _copy_wiki_pages(client, lib_id, sub_identifier, ws_identifier)
        print(f"    → {len(copied)}개 페이지 복사 완료")

    # workspace_map DB 등록
    if not args.dry_run:
        now = datetime.now(timezone.utc).isoformat()
        upsert_workspace(slug, args.name, ws_identifier, source_modules, now)
        print(f"\n  📋 workspace_map 등록 완료: {ws_identifier}")

    print(f"\n{mode} 완료: {ws_identifier} ({len(resolved)}개 모듈)")
    return 0


# ── sync ──────────────────────────────────────────────────────────────────────

def cmd_sync(client: RedmineClient, cfg: dict, args) -> int:
    """특정 Library Module의 최신 내용을 Workspace Module에 반영."""
    ws_slug = args.workspace.removeprefix("ws-")
    lib_module = args.module   # e.g., lib-iso27001-p001-001

    pro_slug = _pro_slug_from_identifier(lib_module)
    dst_project = f"ws-{ws_slug}-{pro_slug}"

    mode = "[DRY-RUN]" if args.dry_run else "[SYNC]"
    print(f"\n{mode} {lib_module} → {dst_project}\n")

    # 대상 워크스페이스 모듈 존재 확인
    if not args.dry_run:
        if not client.get_project(dst_project):
            print(f"❌ '{dst_project}' 프로젝트가 Redmine에 없습니다.", file=sys.stderr)
            return 1

    copied = _copy_wiki_pages(client, lib_module, dst_project,
                               f"ws-{ws_slug}", dry_run=args.dry_run)
    print(f"\n{mode} 완료: {len(copied)}개 페이지 반영")
    return 0


# ── list ──────────────────────────────────────────────────────────────────────

def cmd_list(args) -> int:
    rows = list_workspaces()
    if not rows:
        print("등록된 Workspace 없음.")
        return 0

    print(f"\n{'슬러그':<25} {'이름':<30} {'모듈 수':>6}  {'생성일'}")
    print("-" * 80)
    for row in rows:
        modules = json.loads(row["source_modules"])
        created = row["created_at"][:10]
        print(f"{row['workspace_slug']:<25} {row['workspace_name']:<30} "
              f"{len(modules):>6}  {created}")
    return 0


# ── status ────────────────────────────────────────────────────────────────────

def cmd_status(args) -> int:
    ws_slug = args.workspace.removeprefix("ws-")
    rows = list_workspaces()
    found = [r for r in rows if r["workspace_slug"] == ws_slug]
    if not found:
        print(f"Workspace '{ws_slug}' 를 찾을 수 없습니다.")
        return 1
    row = found[0]
    modules = json.loads(row["source_modules"])
    print(f"\nWorkspace: {row['workspace_name']}")
    print(f"  slug:     ws-{row['workspace_slug']}")
    print(f"  project:  {row['redmine_project_id']}")
    print(f"  created:  {row['created_at'][:10]}")
    print(f"  modules ({len(modules)}):")
    for m in modules:
        print(f"    - {m}")
    return 0


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Workspace 관리")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # create
    p_create = sub.add_parser("create", help="Workspace 생성")
    p_create.add_argument("--name",        required=True, help="워크스페이스 표시 이름")
    p_create.add_argument("--slug",        required=True, help="URL-safe 식별자 (ws-{slug})")
    p_create.add_argument("--modules",     required=True,
                          help="쉼표 구분 PRO doc_id 목록 (예: PRO-ISO27001-001-001,PRO-CMMI-001-001)")
    p_create.add_argument("--description", default="", help="워크스페이스 설명")
    p_create.add_argument("--dry-run",     action="store_true")

    # sync
    p_sync = sub.add_parser("sync", help="Library Module → Workspace Module 최신화")
    p_sync.add_argument("--workspace", required=True, help="ws-{slug} 또는 {slug}")
    p_sync.add_argument("--module",    required=True, help="lib-{scope}-{pro_slug}")
    p_sync.add_argument("--dry-run",   action="store_true")

    # list
    sub.add_parser("list", help="전체 Workspace 목록")

    # status
    p_status = sub.add_parser("status", help="특정 Workspace 상세")
    p_status.add_argument("--workspace", required=True)

    args = parser.parse_args()
    init_db()
    cfg = _load_config()

    if args.cmd == "list":
        return cmd_list(args)
    if args.cmd == "status":
        return cmd_status(args)

    client = client_from_config(cfg)
    if not getattr(args, "dry_run", False):
        if not client.ping():
            print("❌ Redmine 접속 실패. URL/API KEY를 확인하세요.", file=sys.stderr)
            return 1

    if args.cmd == "create":
        return cmd_create(client, cfg, args)
    if args.cmd == "sync":
        return cmd_sync(client, cfg, args)

    return 0


if __name__ == "__main__":
    sys.exit(main())
