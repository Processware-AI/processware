"""Vault filesystem scanning — determine next available sequence numbers."""

import re
from pathlib import Path
from typing import Optional

from .rules import FOLDER_MAP, MAT_COMMON_MAX, MAT_STANDARD_START
from .generator import parse_doc_id


def _vault_path(vault_root: str, doc_type: str) -> Path:
    folder = FOLDER_MAP.get(doc_type, "")
    return Path(vault_root) / folder


# ── Sequence extraction helpers ───────────────────────────────────────────────

def _extract_seq(filename: str, position: int) -> Optional[int]:
    """Extract numeric segment at given dash-split position (0-based after type)."""
    stem = Path(filename).stem  # strip .md
    # filename like PRO-QMS-01-02_절차명_v1.0 → split on first '_' then split on '-'
    id_part = stem.split("_")[0]
    parts = id_part.split("-")
    try:
        return int(parts[position])
    except (IndexError, ValueError):
        return None


# ── Public API ────────────────────────────────────────────────────────────────

def next_seq(
    doc_type: str,
    scope: str,
    parent_id: Optional[str],
    vault_root: str = "vault",
    year: Optional[int] = None,
) -> int:
    """
    Return the next available integer sequence number for a new child document.

    For REC: year-scoped 3-digit seq within (parent TMP + year).
    For MAT/REF: global 3-digit, MAT standard range starts at MAT_STANDARD_START.
    For others: 2-digit seq within the parent scope.
    """
    if doc_type in ("MAT", "REF"):
        return _next_mat_ref_seq(doc_type, vault_root)

    if doc_type == "REC":
        return _next_rec_seq(parent_id, year, vault_root)

    return _next_hierarchical_seq(doc_type, scope, parent_id, vault_root)


def _next_hierarchical_seq(
    doc_type: str, scope: str, parent_id: Optional[str], vault_root: str
) -> int:
    folder = _vault_path(vault_root, doc_type)
    if not folder.exists():
        return 1

    # Position of the sequence segment depends on doc_type
    # POL-QMS-{pol}  → position 2
    # PRO-QMS-{pol}-{pro} → position 3
    # WI-QMS-{pol}-{pro}-{wi} → position 4
    # TMP/EX-QMS-{pol}-{pro}-{wi}-{tmp} → position 5
    pos_map = {"POL": 2, "PRO": 3, "WI": 4, "TMP": 5, "EX": 5}
    pos = pos_map.get(doc_type, 2)

    # Build prefix to filter matching files
    prefix = _build_prefix(doc_type, scope, parent_id)

    seqs = []
    for f in folder.glob("*.md"):
        name = f.name
        if not name.startswith(prefix):
            continue
        seq = _extract_seq(name, pos)
        if seq is not None:
            seqs.append(seq)

    return max(seqs, default=0) + 1


def _build_prefix(doc_type: str, scope: str, parent_id: Optional[str]) -> str:
    """Build the filename prefix to filter candidate files in a folder."""
    if doc_type == "POL" or parent_id is None:
        return f"{doc_type}-{scope}-"

    try:
        p = parse_doc_id(parent_id)
    except ValueError:
        return f"{doc_type}-{scope}-"

    if doc_type == "PRO":
        return f"PRO-{scope}-{p.pol_seq}-"
    if doc_type == "WI":
        return f"WI-{scope}-{p.pol_seq}-{p.pro_seq}-"
    if doc_type in ("TMP", "EX"):
        return f"{doc_type}-{scope}-{p.pol_seq}-{p.pro_seq}-{p.wi_seq}-"

    return f"{doc_type}-{scope}-"


def _next_rec_seq(parent_id: Optional[str], year: Optional[int], vault_root: str) -> int:
    from datetime import date as _date
    yr = year or _date.today().year

    folder = _vault_path(vault_root, "REC")
    if not folder.exists():
        return 1

    # REC-QMS-01-01-02-01-2026-001
    prefix = ""
    if parent_id:
        try:
            p = parse_doc_id(parent_id)
            prefix = (f"REC-{p.scope}-{p.pol_seq}-{p.pro_seq}"
                      f"-{p.wi_seq}-{p.tmp_seq}-{yr}-")
        except ValueError:
            pass

    pattern = re.compile(r"-(\d{3})\.md$")
    seqs = []
    for f in folder.glob("*.md"):
        if prefix and not f.name.startswith(prefix):
            continue
        m = pattern.search(f.name)
        if m:
            seqs.append(int(m.group(1)))

    return max(seqs, default=0) + 1


def _next_mat_ref_seq(doc_type: str, vault_root: str) -> int:
    folder = _vault_path(vault_root, doc_type)
    if not folder.exists():
        start = MAT_STANDARD_START if doc_type == "MAT" else 1
        return start

    pattern = re.compile(rf"^{doc_type}-(\d{{3}})")
    seqs = []
    for f in folder.glob("*.md"):
        m = pattern.match(f.name)
        if m:
            seqs.append(int(m.group(1)))

    if doc_type == "MAT":
        # Skip reserved common range (001~010)
        standard_seqs = [s for s in seqs if s >= MAT_STANDARD_START]
        return max(standard_seqs, default=MAT_STANDARD_START - 1) + 1

    return max(seqs, default=0) + 1
