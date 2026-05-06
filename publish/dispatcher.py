"""
vault 외부 시스템 연동 디스패처.

사용:
  python3 publish/dispatcher.py push   [--target <backend>] [push 옵션...]
  python3 publish/dispatcher.py workspace [--target <backend>] create|sync|list|status [옵션...]

지원 backend:
  redmine (기본값) — publish/redmine/adapter.py
  future: confluence, notion, ...
"""

from __future__ import annotations

import argparse
import importlib
import sys
from pathlib import Path

import yaml

_HERE = Path(__file__).parent
_TOP_CONFIG = _HERE / "config.yaml"


def _load_top_config() -> dict:
    if _TOP_CONFIG.exists():
        with open(_TOP_CONFIG) as f:
            return yaml.safe_load(f) or {}
    return {}


def _load_adapter(target: str):
    """publish/{target}/adapter.py 의 {Target}Adapter 클래스를 반환."""
    adapter_path = _HERE / target / "adapter.py"
    if not adapter_path.exists():
        print(f"❌ 어댑터 없음: publish/{target}/adapter.py", file=sys.stderr)
        sys.exit(1)

    # 어댑터 모듈 동적 로드
    spec_loader = importlib.util.spec_from_file_location(f"{target}_adapter", adapter_path)
    mod = importlib.util.module_from_spec(spec_loader)
    spec_loader.loader.exec_module(mod)

    class_name = target.capitalize() + "Adapter"
    if not hasattr(mod, class_name):
        print(f"❌ {class_name} 클래스를 {adapter_path}에서 찾을 수 없음.", file=sys.stderr)
        sys.exit(1)
    return getattr(mod, class_name)


def _load_adapter_config(target: str) -> dict:
    """publish/{target}/config.yaml 로드."""
    cfg_path = _HERE / target / "config.yaml"
    if not cfg_path.exists():
        print(f"⚠️  {cfg_path} 없음. 빈 설정으로 진행.", file=sys.stderr)
        return {}
    with open(cfg_path) as f:
        return yaml.safe_load(f) or {}


# ── push 서브커맨드 ────────────────────────────────────────────────────────────

def cmd_push(adapter, args) -> int:
    if args.status:
        return adapter.status()
    if args.setup:
        return adapter.setup(dry_run=args.dry_run)
    return adapter.push(
        doc_id=args.doc_id,
        changed_only=args.changed,
        type_filter=args.type_filter,
        scope_filter=args.scope_filter,
        dry_run=args.dry_run,
    )


def build_push_parser(sub):
    p = sub.add_parser("push", help="vault → Library 동기화")
    p.add_argument("doc_id", nargs="?", help="특정 doc_id 1건")
    p.add_argument("--changed",  action="store_true", help="git diff 변경분만")
    p.add_argument("--type",     dest="type_filter",  help="문서 유형 필터 (예: WI)")
    p.add_argument("--scope",    dest="scope_filter", help="scope_code 필터 (예: ISO27001)")
    p.add_argument("--dry-run",  action="store_true")
    p.add_argument("--status",   action="store_true", help="마지막 동기화 상태 출력")
    p.add_argument("--setup",    action="store_true", help="Library 프로젝트 계층 초기화")
    return p


# ── workspace 서브커맨드 ───────────────────────────────────────────────────────

def cmd_workspace(adapter, args) -> int:
    if args.ws_cmd == "create":
        return adapter.workspace_create(
            name=args.name,
            slug=args.slug,
            modules=args.modules,
            description=getattr(args, "description", ""),
            dry_run=getattr(args, "dry_run", False),
        )
    if args.ws_cmd == "sync":
        return adapter.workspace_sync(
            workspace_slug=args.workspace,
            module=args.module,
            dry_run=getattr(args, "dry_run", False),
        )
    if args.ws_cmd == "list":
        return adapter.workspace_list()
    if args.ws_cmd == "status":
        return adapter.workspace_status(workspace_slug=args.workspace)
    return 1


def build_workspace_parser(sub):
    p = sub.add_parser("workspace", help="Workspace 관리")
    ws_sub = p.add_subparsers(dest="ws_cmd", required=True)

    pc = ws_sub.add_parser("create")
    pc.add_argument("--name",        required=True)
    pc.add_argument("--slug",        required=True)
    pc.add_argument("--modules",     required=True)
    pc.add_argument("--description", default="")
    pc.add_argument("--dry-run",     action="store_true")

    ps = ws_sub.add_parser("sync")
    ps.add_argument("--workspace", required=True)
    ps.add_argument("--module",    required=True)
    ps.add_argument("--dry-run",   action="store_true")

    ws_sub.add_parser("list")

    pst = ws_sub.add_parser("status")
    pst.add_argument("--workspace", required=True)

    return p


# ── 메인 ──────────────────────────────────────────────────────────────────────

def main() -> int:
    top_cfg = _load_top_config()
    default_target = top_cfg.get("default_target", "redmine")

    parser = argparse.ArgumentParser(description="vault 외부 시스템 연동 디스패처")
    parser.add_argument("--target", default=default_target,
                        help=f"연동 대상 백엔드 (기본값: {default_target})")
    sub = parser.add_subparsers(dest="cmd", required=True)
    build_push_parser(sub)
    build_workspace_parser(sub)

    args = parser.parse_args()

    AdapterClass = _load_adapter(args.target)
    adapter_cfg = _load_adapter_config(args.target)
    adapter = AdapterClass(adapter_cfg)

    if args.cmd == "push":
        return cmd_push(adapter, args)
    if args.cmd == "workspace":
        return cmd_workspace(adapter, args)

    return 1


if __name__ == "__main__":
    sys.exit(main())
