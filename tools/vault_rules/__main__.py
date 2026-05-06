"""CLI entry point: python -m tools.vault_rules <command> [options]"""

import argparse
import json
import sys
from pathlib import Path

from .rules import FOLDER_MAP, FRONTMATTER_SCHEMA, SCOPE_CODES
from .generator import (
    generate_filename,
    get_folder_path,
    increment_version,
    new_child_id,
    new_mat_id,
    new_ref_id,
    cascade_ids,
    parse_doc_id,
)
from .scanner import next_seq
from .validator import validate_file


def cmd_next_id(args):
    """Next available doc ID."""
    t = args.type.upper()
    vault = args.vault

    if t == "MAT":
        seq = next_seq("MAT", "", None, vault)
        print(new_mat_id(seq))
    elif t == "REF":
        seq = next_seq("REF", "", None, vault)
        print(new_ref_id(seq))
    elif t == "POL":
        scope = _require(args, "scope")
        seq = next_seq("POL", scope, None, vault)
        print(f"POL-{scope}-{seq:02d}")
    else:
        scope = _require(args, "scope")
        parent = _require(args, "parent")
        year = getattr(args, "year", None)
        seq = next_seq(t, scope, parent, vault, year)
        print(new_child_id(parent, t, seq))


def cmd_filename(args):
    """Generate canonical filename."""
    print(generate_filename(args.id, args.name, args.version))


def cmd_folder(args):
    """Get folder path for doc type."""
    p = get_folder_path(args.type.upper(), args.vault)
    print(str(p))


def cmd_schema(args):
    """Print required frontmatter fields (JSON array)."""
    t = args.type.upper()
    fields = FRONTMATTER_SCHEMA.get(t)
    if fields is None:
        _die(f"Unknown doc type: {t!r}")
    print(json.dumps(fields))


def cmd_version(args):
    """Increment version string."""
    change = getattr(args, "change", "minor") or "minor"
    print(increment_version(args.current, change))


def cmd_validate(args):
    """Validate a vault document file. Exits 0=OK, 1=errors."""
    errors = validate_file(args.file, args.vault)
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    print("OK")


def cmd_cascade(args):
    """List files to rename when a POL ID changes."""
    vault_root = Path(args.vault)
    old_parsed = parse_doc_id(args.old)
    if old_parsed.doc_type != "POL":
        _die("--old must be a POL ID")

    # Collect all vault .md file stems
    all_ids = []
    for md in vault_root.rglob("*.md"):
        stem = md.stem.split("_")[0]
        try:
            parse_doc_id(stem)
            all_ids.append(stem)
        except ValueError:
            pass

    mapping = cascade_ids(args.old, args.new, all_ids)
    if not mapping:
        print("No files affected.")
        return

    for old_id, new_id in sorted(mapping.items()):
        print(f"{old_id}  →  {new_id}")

    if not args.dry_run:
        print("\n(pass --dry-run to preview only; actual rename not implemented in CLI)")


# ── Helpers ───────────────────────────────────────────────────────────────────

def _require(args, attr):
    val = getattr(args, attr, None)
    if not val:
        _die(f"--{attr} is required for this command")
    return val


def _die(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog="python -m tools.vault_rules",
        description="Deterministic vault structure rules for processware",
    )
    parser.add_argument("--vault", default="vault", help="Vault root directory (default: vault)")
    sub = parser.add_subparsers(dest="command", required=True)

    # next-id
    p = sub.add_parser("next-id", help="Get next available doc ID")
    p.add_argument("--type", required=True, help="Doc type (POL/PRO/WI/TMP/EX/REC/MAT/REF)")
    p.add_argument("--scope", help="Scope code (e.g. QMS)")
    p.add_argument("--parent", help="Parent doc ID")
    p.add_argument("--year", type=int, help="Year for REC IDs (default: current year)")

    # filename
    p = sub.add_parser("filename", help="Generate canonical filename")
    p.add_argument("--id", required=True, help="Doc ID (e.g. PRO-QMS-01-02)")
    p.add_argument("--name", required=True, help="Document name (spaces OK)")
    p.add_argument("--version", required=True, help="Version (e.g. 1.0)")

    # folder
    p = sub.add_parser("folder", help="Get folder path for a doc type")
    p.add_argument("--type", required=True, help="Doc type")

    # schema
    p = sub.add_parser("schema", help="Print required frontmatter fields as JSON")
    p.add_argument("--type", required=True, help="Doc type")

    # version
    p = sub.add_parser("version", help="Increment a version string")
    p.add_argument("--current", required=True, help="Current version (e.g. 1.0)")
    p.add_argument("--change", choices=["major", "minor"], default="minor")

    # validate
    p = sub.add_parser("validate", help="Validate a vault document file")
    p.add_argument("--file", required=True, help="Path to .md file")

    # cascade
    p = sub.add_parser("cascade", help="Preview rename cascade for a POL ID change")
    p.add_argument("--old", required=True, help="Old POL ID (e.g. POL-QMS-01)")
    p.add_argument("--new", required=True, help="New POL ID (e.g. POL-QMS-02)")
    p.add_argument("--dry-run", action="store_true", help="Preview only, no changes")

    args = parser.parse_args()

    dispatch = {
        "next-id":  cmd_next_id,
        "filename": cmd_filename,
        "folder":   cmd_folder,
        "schema":   cmd_schema,
        "version":  cmd_version,
        "validate": cmd_validate,
        "cascade":  cmd_cascade,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
