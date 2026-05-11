"""
D-5 retroactive spot-check:
backbone canonical statements (from conversation memory) vs current verbatim.
"""

import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

REQ = Path(r"C:\MyProjects\processware\inputs\01_표준원문\CMMI-DEV\requirements.yaml")

# Backbone canonical statements that I authored during the original ingest
# (from this conversation's history — exact text as written in backbone pass)
BACKBONE_CANONICAL = {
    "CMMIDEV-CAR-SG1-REQ-001":
        "Root causes of selected outcomes are systematically determined.",
    "CMMIDEV-DAR-SG1-REQ-001":
        "Decisions are based on an evaluation of alternatives using established criteria.",
    "CMMIDEV-MA-SG2-REQ-001":
        "Measurement results, which address identified information needs and objectives, are provided.",
    "CMMIDEV-PP-SG2-REQ-001":
        "A project plan is established and maintained as the basis for managing the project.",
    "CMMIDEV-VER-SG1-REQ-001":
        "Preparation for verification is conducted.",
    # Two more as bonus
    "CMMIDEV-CM-SG2-REQ-001":
        "Changes to the work products under configuration management are tracked and controlled.",
    "CMMIDEV-PPQA-SG1-REQ-001":
        "Adherence of the performed process and associated work products to applicable process descriptions, standards, and procedures is objectively evaluated.",
}

with open(REQ, "r", encoding="utf-8") as f:
    doc = yaml.safe_load(f)

current_by_id = {r["id"]: r for r in doc["requirements"]}

print("=" * 80)
print("D-5 SPOT-CHECK — Backbone canonical vs current verbatim")
print("=" * 80)

results = []
for rid, canon in BACKBONE_CANONICAL.items():
    if rid not in current_by_id:
        results.append((rid, "MISSING", canon, ""))
        continue

    current = current_by_id[rid]
    cur_text = current.get("text", "").strip()
    canon_norm = canon.strip()

    if cur_text == canon_norm:
        verdict = "EXACT MATCH"
    elif cur_text.lower() == canon_norm.lower():
        verdict = "MATCH (case diff)"
    elif canon_norm.replace(",", "") == cur_text.replace(",", ""):
        verdict = "MATCH (punctuation diff)"
    else:
        verdict = "DIFF"

    results.append((rid, verdict, canon_norm, cur_text))

# Print results
for rid, verdict, canon, cur in results:
    print(f"\n[{verdict}] {rid}")
    if verdict == "DIFF":
        print(f"  Canonical : {canon}")
        print(f"  Verbatim  : {cur}")
    else:
        print(f"  Text     : {canon[:100]}{'...' if len(canon) > 100 else ''}")

# Summary
print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
match_count = sum(1 for _, v, _, _ in results if "MATCH" in v)
diff_count = sum(1 for _, v, _, _ in results if v == "DIFF")
miss_count = sum(1 for _, v, _, _ in results if v == "MISSING")
print(f"Total: {len(results)}")
print(f"  Exact/near-match: {match_count}")
print(f"  Differences: {diff_count}")
print(f"  Missing: {miss_count}")
print(f"  Match rate: {match_count}/{len(results)} = {100*match_count/len(results):.0f}%")
