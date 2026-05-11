"""
D-1 merge script: consolidate 4 batch YAML files + existing GG/GP/SP samples
into a new requirements.yaml. Normalizes schema variations across batches.
"""

import sys
import yaml
import re
from pathlib import Path

# Force UTF-8 stdout on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(r"C:\MyProjects\processware\inputs\01_표준원문\CMMI-DEV")
BATCH_DIR = ROOT / "_d1_batch"
ORIG_BACKUP = BATCH_DIR / "requirements_backup_pre_d1.yaml"
TARGET = ROOT / "requirements.yaml"


def parse_pa_from_id(rid: str) -> str:
    """CMMIDEV-PI-SG1-REQ-001 → PI"""
    parts = rid.split("-")
    if len(parts) >= 3:
        return parts[1]
    return ""


def normalize_entry(r: dict) -> dict:
    """Normalize a requirement entry to canonical schema."""
    n = dict(r)  # copy
    rid = n.get("id", "")

    # 1) Add process_area if missing
    if "process_area" not in n:
        pa = parse_pa_from_id(rid)
        # Skip for GG/GP (no PA)
        if pa not in ("GG1", "GG2", "GG3", "GP1.1", "GP2.1", "GP2.2", "GP2.3",
                       "GP2.4", "GP2.5", "GP2.6", "GP2.7", "GP2.8", "GP2.9",
                       "GP2.10", "GP3.1", "GP3.2"):
            if not pa.startswith("GG") and not pa.startswith("GP"):
                n["process_area"] = pa

    # 2) Map batch4 fields: title → clause_title, statement → text
    if "title" in n and "clause_title" not in n:
        n["clause_title"] = n.pop("title")
    if "statement" in n and "text" not in n:
        n["text"] = n.pop("statement")

    # 3) Map batch4 type=specific_goal/specific_practice/purpose → component + type
    t = n.get("type", "")
    if t == "specific_goal":
        n["component"] = "required"
        n["type"] = "normative"
        n["obligation"] = n.get("obligation", "shall")
        n["classification"] = n.get("classification", "process_requirement")
    elif t == "specific_practice":
        n["component"] = "expected"
        n["type"] = "normative"
        n["obligation"] = n.get("obligation", "shall")
        n["classification"] = n.get("classification", "process_requirement")
    elif t == "purpose":
        n["component"] = "informative"
        n["type"] = "purpose_statement"
        # Purpose statements don't have obligation
        n.pop("obligation", None)

    # 4) Ensure obligation exists for SG/SP (normative)
    if "component" in n and n["component"] in ("required", "expected"):
        if "obligation" not in n:
            n["obligation"] = "shall"
        if "type" not in n:
            n["type"] = "normative"

    # 5) Default status if missing
    if "status" not in n:
        n["status"] = "active_verbatim"

    # 6) parent_goal for SP entries (e.g., CMMIDEV-PI-SP1.1-REQ-001 → PI SG 1)
    if "parent_goal" not in n:
        m = re.match(r"CMMIDEV-(\w+)-SP(\d+)\.\d+-REQ-\d+", rid)
        if m:
            pa = m.group(1)
            sg_num = m.group(2)
            n["parent_goal"] = f"{pa} SG {sg_num}"

    return n


# 1) Load existing requirements.yaml (it's been overwritten — load backup if exists, else current)
if ORIG_BACKUP.exists():
    orig_file = ORIG_BACKUP
    print(f"Using backup: {orig_file}")
else:
    orig_file = TARGET
    print(f"Using current: {orig_file}")

with open(orig_file, "r", encoding="utf-8") as f:
    orig = yaml.safe_load(f)
orig_requirements = orig.get("requirements", [])
print(f"Original requirements count: {len(orig_requirements)}")

# 2) Filter: keep GG, GP, and 5 pre-extracted SP samples
preserve_prefixes = ("CMMIDEV-GG", "CMMIDEV-GP")
preserve_specific = {
    "CMMIDEV-REQM-SP1.5-REQ-001",
    "CMMIDEV-RSKM-SP1.1-REQ-001",
    "CMMIDEV-RSKM-SP1.2-REQ-001",
    "CMMIDEV-RSKM-SP1.3-REQ-001",
    "CMMIDEV-RSKM-SP2.1-REQ-001",
}

preserved = [r for r in orig_requirements
             if r.get("id", "").startswith(preserve_prefixes)
             or r.get("id", "") in preserve_specific]
print(f"Preserved from original: {len(preserved)}")

# 3) Load 4 batch files
batches = ["batch1_support", "batch2_pm", "batch3_engineering", "batch4_processmgmt"]
batch_entries = []
for bname in batches:
    bpath = BATCH_DIR / f"{bname}.yaml"
    with open(bpath, "r", encoding="utf-8") as f:
        bdata = yaml.safe_load(f)
    entries = bdata.get("requirements", [])
    print(f"  {bname}: {len(entries)} entries (raw)")
    batch_entries.extend(entries)

print(f"Total batch entries (raw): {len(batch_entries)}")

# 4) Normalize all entries (preserved + batch)
all_entries = preserved + batch_entries
normalized = [normalize_entry(r) for r in all_entries]

# 5) Sort: GG/GP first, then by PA + SG/SP number
pa_order = ["CAR", "CM", "DAR", "IPM", "MA", "OPD", "OPF", "OPM", "OPP", "OT",
            "PI", "PMC", "PP", "PPQA", "QPM", "RD", "REQM", "RSKM", "SAM", "TS", "VAL", "VER"]


def sort_key(r):
    rid = r.get("id", "")
    parts = rid.split("-")
    if len(parts) < 3:
        return (99, 99, 99, 99, 99)

    second = parts[1]

    # GG/GP entries first
    if second.startswith("GG") or second.startswith("GP"):
        # Order: GG1, GP1.1, GG2, GP2.1, ..., GG3, GP3.1, GP3.2
        if second.startswith("GG"):
            num = int(second[2:]) if second[2:].isdigit() else 0
            return (0, num, 0, 0, 0)
        else:  # GP
            num = second[2:]  # e.g., "1.1"
            major, minor = num.split(".") if "." in num else (num, "0")
            return (0, int(major), 1, int(minor) if minor.isdigit() else 0, 0)

    # SG/SP entries
    pa_idx = pa_order.index(second) + 1 if second in pa_order else 99

    third = parts[2]  # SG1, SP1.1, PURPOSE
    if third == "PURPOSE":
        return (pa_idx, 0, 0, 0, 0)
    elif third.startswith("SG"):
        sg_num = int(third[2:]) if third[2:].isdigit() else 0
        return (pa_idx, sg_num, 0, 0, 0)
    elif third.startswith("SP"):
        sp_num = third[2:]  # "1.1"
        major, minor = sp_num.split(".") if "." in sp_num else (sp_num, "0")
        try:
            return (pa_idx, int(major), 1, int(minor), 0)
        except ValueError:
            return (pa_idx, 99, 1, 99, 0)
    return (pa_idx, 99, 99, 99, 99)


normalized.sort(key=sort_key)
print(f"Normalized + sorted: {len(normalized)} entries")

# 6) Compute statistics
counts_by_component = {}
counts_by_status = {}
counts_by_pa = {}
counts_verbatim = 0
for r in normalized:
    comp = r.get("component", "unknown")
    counts_by_component[comp] = counts_by_component.get(comp, 0) + 1
    st = r.get("status", "unknown")
    counts_by_status[st] = counts_by_status.get(st, 0) + 1
    if "verbatim" in st:
        counts_verbatim += 1
    pa = r.get("process_area", None)
    if pa:
        counts_by_pa[pa] = counts_by_pa.get(pa, 0) + 1

# 7) Build final document
new_doc = {
    "standard_id": "CMMI-DEV",
    "version": "1.3",
    "extraction_mode": "full_verbatim_pass",
    "generated_at": "2026-05-11T02:00:00+09:00",
    "copyright_notice": {
        "holder": "Carnegie Mellon University",
        "year": 2010,
        "source": "CMU/SEI-2010-TR-033 — CMMI for Development, Version 1.3",
        "license": "Internal use — derivative works permitted (per CMU/SEI copyright notice, PDF p.2)",
        "no_warranty": (
            "THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE "
            "MATERIAL IS FURNISHED ON AN 'AS-IS' BASIS. CARNEGIE MELLON UNIVERSITY "
            "MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY "
            "MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR "
            "MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. "
            "CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH "
            "RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT."
        ),
        "derivative_work_disclosure": (
            "Verbatim extracts of normative components (SG/SP statements, "
            "Example Work Products, Subpractices) reproduced for internal "
            "compliance management. Elaborating prose (introductory notes, "
            "practice elaborations, examples in dashed boxes) is NOT reproduced."
        ),
    },
    "requirements": normalized,
    "summary": {
        "total_requirements": len(normalized),
        "by_component": counts_by_component,
        "by_status": counts_by_status,
        "pdf_verbatim_count": counts_verbatim,
        "by_process_area": dict(sorted(counts_by_pa.items())),
        "extraction_passes": {
            "backbone_pass_v1": "GG (3) + GP (12) + 47 SG canonical + 5 SP samples — superseded by D-1",
            "d1_pass": "All 22 PAs verbatim SG + SP + EWP + Subpractices (this file)",
        },
    },
}

# 8) Write target
with open(TARGET, "w", encoding="utf-8") as f:
    yaml.dump(new_doc, f, sort_keys=False, allow_unicode=True,
              default_flow_style=False, width=1000)

print(f"\n[DONE] Written: {TARGET}")
print(f"   Total entries: {len(normalized)}")
print(f"   By component: {counts_by_component}")
print(f"   By status: {counts_by_status}")
print(f"   PDF verbatim: {counts_verbatim}")
print(f"   PA coverage: {len(counts_by_pa)} PAs")
print(f"   PAs: {sorted(counts_by_pa.keys())}")
