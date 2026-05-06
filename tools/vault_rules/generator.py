"""Deterministic generation of doc IDs, filenames, and vault paths."""

import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional

from .rules import FOLDER_MAP, HIERARCHY_DEPTH


@dataclass
class DocId:
    """Parsed representation of a document identifier."""
    doc_type: str
    scope: str
    pol_seq: Optional[str] = None   # 2-digit, e.g. "01"
    pro_seq: Optional[str] = None   # 2-digit
    wi_seq:  Optional[str] = None   # 2-digit
    tmp_seq: Optional[str] = None   # 2-digit
    year:    Optional[str] = None   # 4-digit (REC only)
    rec_seq: Optional[str] = None   # 3-digit (REC only)
    mat_seq: Optional[str] = None   # 3-digit (MAT/REF only)

    def __str__(self) -> str:
        return build_doc_id(self)


# ── Parsing ──────────────────────────────────────────────────────────────────

_PATTERNS = {
    # REC-QMS-01-01-02-01-2026-001
    "REC": re.compile(
        r"^REC-(?P<scope>[A-Z]+)-(?P<pol>\d{2})-(?P<pro>\d{2})-(?P<wi>\d{2})-(?P<tmp>\d{2})-(?P<year>\d{4})-(?P<rec>\d{3})$"
    ),
    # TMP-QMS-01-01-02-01 / EX-QMS-01-01-02-01
    "TMP": re.compile(
        r"^(?P<type>TMP|EX)-(?P<scope>[A-Z]+)-(?P<pol>\d{2})-(?P<pro>\d{2})-(?P<wi>\d{2})-(?P<tmp>\d{2})$"
    ),
    # WI-QMS-01-01-02
    "WI": re.compile(
        r"^WI-(?P<scope>[A-Z]+)-(?P<pol>\d{2})-(?P<pro>\d{2})-(?P<wi>\d{2})$"
    ),
    # PRO-QMS-01-01
    "PRO": re.compile(
        r"^PRO-(?P<scope>[A-Z]+)-(?P<pol>\d{2})-(?P<pro>\d{2})$"
    ),
    # POL-QMS-01
    "POL": re.compile(
        r"^POL-(?P<scope>[A-Z]+)-(?P<pol>\d{2})$"
    ),
    # MAT-001 / REF-001
    "MAT": re.compile(
        r"^(?P<type>MAT|REF)-(?P<seq>\d{3})$"
    ),
}


def parse_doc_id(raw: str) -> DocId:
    """Parse a doc ID string into a DocId dataclass. Raises ValueError on failure."""
    raw = raw.strip()

    # REC first (most specific)
    m = _PATTERNS["REC"].match(raw)
    if m:
        return DocId(doc_type="REC", scope=m["scope"],
                     pol_seq=m["pol"], pro_seq=m["pro"], wi_seq=m["wi"],
                     tmp_seq=m["tmp"], year=m["year"], rec_seq=m["rec"])

    # TMP / EX
    m = _PATTERNS["TMP"].match(raw)
    if m:
        return DocId(doc_type=m["type"], scope=m["scope"],
                     pol_seq=m["pol"], pro_seq=m["pro"],
                     wi_seq=m["wi"], tmp_seq=m["tmp"])

    # WI
    m = _PATTERNS["WI"].match(raw)
    if m:
        return DocId(doc_type="WI", scope=m["scope"],
                     pol_seq=m["pol"], pro_seq=m["pro"], wi_seq=m["wi"])

    # PRO
    m = _PATTERNS["PRO"].match(raw)
    if m:
        return DocId(doc_type="PRO", scope=m["scope"],
                     pol_seq=m["pol"], pro_seq=m["pro"])

    # POL
    m = _PATTERNS["POL"].match(raw)
    if m:
        return DocId(doc_type="POL", scope=m["scope"], pol_seq=m["pol"])

    # MAT / REF
    m = _PATTERNS["MAT"].match(raw)
    if m:
        return DocId(doc_type=m["type"], scope="", mat_seq=m["seq"])

    raise ValueError(f"Cannot parse doc ID: {raw!r}")


# ── Building ──────────────────────────────────────────────────────────────────

def build_doc_id(d: DocId) -> str:
    """Reconstruct a doc ID string from a DocId dataclass."""
    t = d.doc_type
    if t == "POL":
        return f"POL-{d.scope}-{d.pol_seq}"
    if t == "PRO":
        return f"PRO-{d.scope}-{d.pol_seq}-{d.pro_seq}"
    if t == "WI":
        return f"WI-{d.scope}-{d.pol_seq}-{d.pro_seq}-{d.wi_seq}"
    if t in ("TMP", "EX"):
        return f"{t}-{d.scope}-{d.pol_seq}-{d.pro_seq}-{d.wi_seq}-{d.tmp_seq}"
    if t == "REC":
        return f"REC-{d.scope}-{d.pol_seq}-{d.pro_seq}-{d.wi_seq}-{d.tmp_seq}-{d.year}-{d.rec_seq}"
    if t in ("MAT", "REF"):
        return f"{t}-{d.mat_seq}"
    raise ValueError(f"Unknown doc_type: {t!r}")


def new_child_id(parent_id: str, child_type: str, seq: int) -> str:
    """
    Create a child doc ID given a parent ID and the next sequence number.

    parent POL-QMS-01 + child PRO + seq 2  →  PRO-QMS-01-02
    parent PRO-QMS-01-01 + child WI + seq 3  →  WI-QMS-01-01-03
    """
    p = parse_doc_id(parent_id)
    seq_str = f"{seq:02d}"

    if child_type == "PRO" and p.doc_type == "POL":
        return f"PRO-{p.scope}-{p.pol_seq}-{seq_str}"
    if child_type == "WI" and p.doc_type == "PRO":
        return f"WI-{p.scope}-{p.pol_seq}-{p.pro_seq}-{seq_str}"
    if child_type in ("TMP", "EX") and p.doc_type == "WI":
        return f"{child_type}-{p.scope}-{p.pol_seq}-{p.pro_seq}-{p.wi_seq}-{seq_str}"
    if child_type == "REC" and p.doc_type in ("TMP", "EX"):
        year = date.today().year
        rec_seq = f"{seq:03d}"
        return (f"REC-{p.scope}-{p.pol_seq}-{p.pro_seq}-{p.wi_seq}"
                f"-{p.tmp_seq}-{year}-{rec_seq}")

    raise ValueError(
        f"Cannot create child {child_type!r} under parent {parent_id!r} ({p.doc_type})"
    )


def new_mat_id(seq: int) -> str:
    return f"MAT-{seq:03d}"


def new_ref_id(seq: int) -> str:
    return f"REF-{seq:03d}"


# ── Filename & path ───────────────────────────────────────────────────────────

def generate_filename(doc_id: str, name: str, version: str) -> str:
    """
    Build canonical filename.
    name spaces → underscores; version has no 'v' prefix needed.
    Example: PRO-QMS-01-02_접근통제_절차_v1.0.md
    """
    slug = name.strip().replace(" ", "_")
    ver = version.lstrip("v")
    return f"{doc_id}_{slug}_v{ver}.md"


def get_folder_path(doc_type: str, vault_root: str = "vault") -> Path:
    folder = FOLDER_MAP.get(doc_type)
    if not folder:
        raise ValueError(f"Unknown doc_type: {doc_type!r}")
    return Path(vault_root) / folder


def increment_version(current: str, change: str = "minor") -> str:
    """
    Increment a version string.
    change='major' → x+1.0,  change='minor' → x.y+1
    """
    ver = current.lstrip("v")
    parts = ver.split(".")
    major, minor = int(parts[0]), int(parts[1]) if len(parts) > 1 else 0

    if change == "major":
        return f"{major + 1}.0"
    return f"{major}.{minor + 1}"


# ── Cascade rename ────────────────────────────────────────────────────────────

def cascade_ids(old_pol_id: str, new_pol_id: str, affected_ids: list[str]) -> dict[str, str]:
    """
    Given a POL rename, return a mapping {old_id: new_id} for all affected child IDs.
    affected_ids: list of raw doc ID strings that descend from old_pol_id.
    """
    old = parse_doc_id(old_pol_id)
    new = parse_doc_id(new_pol_id)
    if old.doc_type != "POL" or new.doc_type != "POL":
        raise ValueError("Both IDs must be POL type")

    mapping: dict[str, str] = {}
    for raw in affected_ids:
        try:
            d = parse_doc_id(raw)
        except ValueError:
            continue
        if d.pol_seq != old.pol_seq or d.scope != old.scope:
            continue
        d.pol_seq = new.pol_seq
        d.scope = new.scope
        mapping[raw] = build_doc_id(d)
    return mapping
