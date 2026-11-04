"""CLI: python -m tools.org <command> [options]

  context     활성 조직 컨텍스트 출력 (env | json | table)
  validate    org.yaml 검증
  init        조직 루트 생성 (org.yaml + 폴더 + sync-core)
  sync-core   플랫폼 core/ → 조직 루트 동기화 (managed 덮어쓰기 · seed 보존)
  register    조직 루트를 레지스트리(~/.processware/orgs.yaml)에 등록
  unregister  레지스트리에서 제거
  list        레지스트리 목록
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import sys
from pathlib import Path

from . import registry
from .context import ENV_ORG_ROOT, ORG_YAML, OrgContextError, find_platform_root, resolve
from .schema import ORG_ID_RE, load_org_yaml, validate_org
from .sync import SyncError, platform_version, sync_core

ORG_SKELETON = (
    "sources",
    "inputs/01_표준원문",
    "inputs/02_법규",
    "inputs/03_해설서",
    "inputs/04_AsIs",
    "inputs/05_산업가이드",
    "inputs/06_목표흐름",
    "vault",
    ".processware/runs",
    ".processware/queues/process-act",
    ".processware/states",
)


def _ctx(args):
    try:
        return resolve(org=args.org, org_root=args.org_root, strict=not args.lenient)
    except OrgContextError as e:
        _die(str(e))


# ── commands ──────────────────────────────────────────────────────────────

def cmd_context(args):
    ctx = _ctx(args)
    if args.format == "json":
        print(json.dumps(ctx.as_dict(), ensure_ascii=False, indent=2))
    elif args.format == "table":
        for k, v in ctx.as_dict().items():
            print(f"{k:<16} {v}")
    else:  # env
        for k, v in ctx.as_env().items():
            print(f"{k}={v}")


def cmd_validate(args):
    if args.file:
        y = Path(args.file)
    else:
        try:
            ctx = resolve(org=args.org, org_root=args.org_root, strict=False)
        except OrgContextError as e:
            _die(str(e))
        y = ctx.org_yaml
    data = load_org_yaml(y)
    errors, warnings = validate_org(data)
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    if errors:
        sys.exit(1)
    print(f"OK {y}")


def cmd_init(args):
    root = Path(args.path).expanduser().resolve()
    if not ORG_ID_RE.match(args.org_id):
        _die(f"org_id 형식 오류: {args.org_id!r} (소문자·숫자·하이픈, 2~32자)")
    y = root / ORG_YAML
    if y.exists():
        _die(f"이미 조직 루트입니다: {y}")

    tmpl = (Path(__file__).parent / "templates" / "org.yaml").read_text(encoding="utf-8")
    content = (
        tmpl.replace("{org_id}", args.org_id)
            .replace("{name}", args.name.replace('"', '\\"'))
            .replace("{created}", _dt.date.today().isoformat())
            .replace("{platform_version}", platform_version(find_platform_root()))
    )

    if args.dry_run:
        print(f"[dry-run] 생성 예정: {root}")
        for d in ORG_SKELETON:
            print(f"  {d}/")
        print(f"  {ORG_YAML}")
        return

    root.mkdir(parents=True, exist_ok=True)
    for d in ORG_SKELETON:
        (root / d).mkdir(parents=True, exist_ok=True)
        (root / d / ".gitkeep").touch()
    y.write_text(content, encoding="utf-8")
    print(f"조직 루트 생성: {root}")
    print(f"  org_id={args.org_id}  name={args.name}")
    if not args.no_sync:
        ctx = resolve(org_root=root)
        try:
            rep = sync_core(ctx)
        except SyncError as e:
            _die(str(e))
        print("  " + rep.summary().replace("\n", "\n  "))
        if not rep.ok:
            sys.exit(1)
    if args.register:
        oid, _ = registry.register(root)
        print(f"  레지스트리 등록: {oid} → {root}")
    print(f"\n활성화: export {ENV_ORG_ROOT}={root}")


def cmd_sync_core(args):
    ctx = _ctx(args)
    try:
        rep = sync_core(ctx, dry_run=args.dry_run, force=args.force)
    except (SyncError, OrgContextError) as e:
        _die(str(e))
    print(rep.summary())
    if args.verbose:
        for label, items in (("created", rep.created), ("updated", rep.updated),
                             ("seed-kept", rep.skipped_seed), ("org created", rep.org_base_created)):
            for it in items:
                print(f"  {label:<11} {it}")
    if not rep.ok:
        sys.exit(1)


def cmd_register(args):
    try:
        oid, root = registry.register(args.path)
    except OrgContextError as e:
        _die(str(e))
    print(f"등록: {oid} → {root}  ({registry.registry_path()})")


def cmd_unregister(args):
    if registry.unregister(args.org_id):
        print(f"제거: {args.org_id}")
    else:
        _die(f"레지스트리에 없음: {args.org_id}")


def cmd_list(args):
    orgs = registry.load()
    if not orgs:
        print(f"(등록된 조직 없음 — {registry.registry_path()})")
        return
    for oid, root in orgs.items():
        mark = "" if Path(root, ORG_YAML).is_file() else "  (org.yaml 없음!)"
        print(f"{oid:<20} {root}{mark}")


def _die(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


# ── main ──────────────────────────────────────────────────────────────────

def _utf8_stdio():
    """Windows 콘솔(cp949)에서도 한글·기호 출력이 깨지지 않도록."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass


def main():
    _utf8_stdio()
    parser = argparse.ArgumentParser(
        prog="python -m tools.org",
        description="Processware 조직 컨텍스트 (org-layer §3 단계 1)",
    )
    # 공통 옵션 — 서브커맨드 앞/뒤 어느 위치에서나 허용
    #   python -m tools.org --org-root X context   /   python -m tools.org context --org-root X
    parser.add_argument("--org", default=None, help="레지스트리의 조직 id")
    parser.add_argument("--org-root", default=None, help="조직 루트 경로 (--org 보다 우선)")
    parser.add_argument("--lenient", action="store_true", default=False,
                        help="org.yaml 검증 오류가 있어도 계속")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--org", default=argparse.SUPPRESS)
    common.add_argument("--org-root", default=argparse.SUPPRESS)
    common.add_argument("--lenient", action="store_true", default=argparse.SUPPRESS)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("context", parents=[common], help="활성 조직 컨텍스트 출력")
    p.add_argument("--format", choices=["env", "json", "table"], default="env")

    p = sub.add_parser("validate", parents=[common], help="org.yaml 검증")
    p.add_argument("--file", help="org.yaml 경로 직접 지정")

    p = sub.add_parser("init", help="조직 루트 뼈대 생성")
    p.add_argument("path", help="조직 루트 경로 (별도 git repo 권장)")
    p.add_argument("--org-id", required=True)
    p.add_argument("--name", required=True)
    p.add_argument("--register", action="store_true", help="생성 후 레지스트리에 등록")
    p.add_argument("--no-sync", action="store_true", help="sync-core 를 실행하지 않음 (vault 비움)")
    p.add_argument("--dry-run", action="store_true")

    p = sub.add_parser("sync-core", parents=[common], help="플랫폼 core/ → 조직 루트 동기화")
    p.add_argument("--dry-run", action="store_true", help="변경 미리보기")
    p.add_argument("--force", action="store_true", help="seed 파일도 덮어쓴다 (재시드)")
    p.add_argument("--verbose", "-v", action="store_true", help="파일 단위 목록 출력")

    p = sub.add_parser("register", help="조직 루트를 레지스트리에 등록")
    p.add_argument("path")

    p = sub.add_parser("unregister", help="레지스트리에서 제거")
    p.add_argument("org_id")

    sub.add_parser("list", help="레지스트리 목록")

    args = parser.parse_args()
    {
        "context": cmd_context,
        "validate": cmd_validate,
        "init": cmd_init,
        "sync-core": cmd_sync_core,
        "register": cmd_register,
        "unregister": cmd_unregister,
        "list": cmd_list,
    }[args.command](args)


if __name__ == "__main__":
    main()
