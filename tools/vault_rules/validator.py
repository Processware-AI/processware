"""Validate vault documents against structural rules."""

import re
from pathlib import Path
from typing import List

try:
    import yaml
    _HAS_YAML = True
except ImportError:
    _HAS_YAML = False

from .rules import FOLDER_MAP, FRONTMATTER_SCHEMA, SEPARATION_RULES
from .generator import parse_doc_id, generate_filename


def validate_file(file_path: str, vault_root: str = "vault") -> List[str]:
    """
    Check a single vault document file for rule violations.
    Returns a list of error strings (empty = OK).
    """
    errors: List[str] = []
    p = Path(file_path)

    if not p.exists():
        return [f"File not found: {file_path}"]

    # ── 1. Filename format ────────────────────────────────────────────────────
    stem = p.stem  # e.g. PRO-QMS-01-02_접근통제_절차_v1.0
    id_part = stem.split("_")[0]
    try:
        parsed = parse_doc_id(id_part)
    except ValueError as e:
        errors.append(f"Invalid doc ID in filename: {e}")
        return errors  # can't continue without a valid ID

    # ── 2. Correct folder ─────────────────────────────────────────────────────
    expected_folder = FOLDER_MAP.get(parsed.doc_type, "")
    if expected_folder and expected_folder not in str(p.parent):
        errors.append(
            f"Wrong folder: '{p.parent.name}' (expected '{expected_folder}')"
        )

    # ── 3. Version suffix present ─────────────────────────────────────────────
    if parsed.doc_type not in ("REC",) and not re.search(r"_v\d+\.\d+$", stem):
        errors.append("Filename missing version suffix (e.g. _v1.0)")

    # ── 4. Frontmatter required fields ────────────────────────────────────────
    if _HAS_YAML:
        fm_errors = _validate_frontmatter_from_file(p, parsed.doc_type)
        errors.extend(fm_errors)

    # ── 5. doc_id in frontmatter matches filename ─────────────────────────────
    if _HAS_YAML:
        fm = _read_frontmatter(p)
        if fm:
            fm_id = fm.get("doc_id", "")
            if fm_id and fm_id != id_part:
                errors.append(
                    f"doc_id mismatch: frontmatter='{fm_id}', filename='{id_part}'"
                )

    return errors


def validate_frontmatter(doc_type: str, frontmatter: dict) -> List[str]:
    """Check that a frontmatter dict has all required fields for the given doc type."""
    required = FRONTMATTER_SCHEMA.get(doc_type, [])
    missing = [f for f in required if f not in frontmatter or frontmatter[f] in (None, "")]
    return [f"Missing required frontmatter field: '{f}'" for f in missing]


# ── Internal helpers ──────────────────────────────────────────────────────────

def _read_frontmatter(path: Path) -> dict:
    if not _HAS_YAML:
        return {}
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def _validate_frontmatter_from_file(path: Path, doc_type: str) -> List[str]:
    fm = _read_frontmatter(path)
    if not fm:
        return ["No frontmatter found (expected YAML between --- delimiters)"]
    return validate_frontmatter(doc_type, fm)
