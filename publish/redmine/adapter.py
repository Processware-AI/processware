"""Redmine 어댑터 — 기존 sync.py / workspace.py 를 BaseAdapter 인터페이스로 래핑."""

from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace

# 기존 모듈을 직접 임포트 (파일 경로 기준)
_HERE = Path(__file__).parent
sys.path.insert(0, str(_HERE))

import sync as _sync
import workspace as _ws
from db import init_db
from redmine_client import client_from_config

sys.path.pop(0)

# 상위 패키지의 BaseAdapter
sys.path.insert(0, str(_HERE.parent))
from base_adapter import BaseAdapter
sys.path.pop(0)


class RedmineAdapter(BaseAdapter):

    def __init__(self, cfg: dict):
        self._cfg = cfg
        init_db()

    # ── Library 동기화 ────────────────────────────────────────────────────────

    def push(
        self,
        doc_id=None,
        changed_only=False,
        type_filter=None,
        scope_filter=None,
        dry_run=False,
    ) -> int:
        cfg = self._cfg
        client = client_from_config(cfg)
        if not dry_run and not client.ping():
            print("❌ Redmine 접속 실패. URL/API KEY를 확인하세요.", file=sys.stderr)
            return 1

        files = _sync.collect_vault_files(
            changed_only=changed_only,
            doc_id=doc_id,
            type_filter=type_filter,
            scope_filter=scope_filter,
        )
        if not files:
            print("동기화 대상 파일 없음.")
            return 0

        mode = "[DRY-RUN]" if dry_run else "[SYNC]"
        print(f"\n{mode} 대상 {len(files)}건\n")

        results: dict[str, int] = {}
        for f in files:
            r = _sync.sync_file(f, client, cfg, dry_run=dry_run)
            st = r.get("status", "error")
            results[st] = results.get(st, 0) + 1
            icon = {"created": "✅", "updated": "🔄", "skipped": "⏭",
                    "error": "❌", "dry-run": "👁"}.get(st, "?")
            print(f"  {icon} {st:8s}  {r.get('doc_id', f.name)}  →  "
                  f"{r.get('redmine_project', r.get('reason', ''))}")

        print(f"\n완료: 생성 {results.get('created',0)} / "
              f"갱신 {results.get('updated',0)} / "
              f"건너뜀 {results.get('skipped',0)} / "
              f"오류 {results.get('error',0)}")
        return 0

    def setup(self, dry_run=False) -> int:
        from library_setup import setup_library, create_wiki_index_pages
        cfg = self._cfg
        client = client_from_config(cfg)
        if not dry_run and not client.ping():
            print("❌ Redmine 접속 실패.", file=sys.stderr)
            return 1
        mode = "[DRY-RUN]" if dry_run else "[SETUP]"
        print(f"\n{mode} Library 프로젝트 계층 생성\n")
        result = setup_library(client, cfg, dry_run=dry_run)
        print(f"\n{mode} Wiki 인덱스 페이지 생성\n")
        create_wiki_index_pages(client, cfg, dry_run=dry_run)
        print(f"\n완료: 신규 {len(result['created'])} / "
              f"기존 {len(result['existing'])} / 건너뜀 {len(result['skipped'])}")
        return 0

    def status(self) -> int:
        from db import get_status_summary
        summary = get_status_summary()
        print("\n[ Sync Map 현황 ]")
        for k, v in summary.items():
            print(f"  {k:12s}: {v}건")
        return 0

    # ── Workspace ─────────────────────────────────────────────────────────────

    def workspace_create(self, name, slug, modules, description="", dry_run=False) -> int:
        cfg = self._cfg
        client = client_from_config(cfg)
        if not dry_run and not client.ping():
            print("❌ Redmine 접속 실패.", file=sys.stderr)
            return 1
        args = SimpleNamespace(
            name=name, slug=slug,
            modules=",".join(modules) if isinstance(modules, list) else modules,
            description=description, dry_run=dry_run,
        )
        return _ws.cmd_create(client, cfg, args)

    def workspace_sync(self, workspace_slug, module, dry_run=False) -> int:
        cfg = self._cfg
        client = client_from_config(cfg)
        if not dry_run and not client.ping():
            print("❌ Redmine 접속 실패.", file=sys.stderr)
            return 1
        args = SimpleNamespace(workspace=workspace_slug, module=module, dry_run=dry_run)
        return _ws.cmd_sync(client, cfg, args)

    def workspace_list(self) -> int:
        return _ws.cmd_list(SimpleNamespace())

    def workspace_status(self, workspace_slug) -> int:
        return _ws.cmd_status(SimpleNamespace(workspace=workspace_slug))
