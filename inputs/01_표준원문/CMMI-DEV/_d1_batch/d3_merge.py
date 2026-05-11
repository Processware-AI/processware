"""
D-3 merge: assemble Glossary parts → definitions.yaml (consolidated)
"""

import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, str(Path(__file__).parent))

from d3_glossary_data import GLOSSARY_PART1
from d3_glossary_data2 import GLOSSARY_PART2
from d3_glossary_data3 import GLOSSARY_PART3

TARGET = Path(r"C:\MyProjects\processware\inputs\01_표준원문\CMMI-DEV\definitions.yaml")

all_terms = GLOSSARY_PART1 + GLOSSARY_PART2 + GLOSSARY_PART3

# Sort alphabetically by term
all_terms.sort(key=lambda t: t["term"].lower())

# Normalize entry structure
normalized = []
for t in all_terms:
    entry = {
        "term": t["term"],
        "definition": t["definition"],
        "source_page": t["page"],
        "status": "active_verbatim",
    }
    if "abbreviation" in t:
        entry["abbreviation"] = t["abbreviation"]
    if "cross_references" in t:
        entry["cross_references"] = t["cross_references"]
    if "notes" in t:
        entry["notes"] = t["notes"]
    normalized.append(entry)

doc = {
    "standard_id": "CMMI-DEV",
    "version": "1.3",
    "section": "Appendix D — Glossary",
    "extraction_mode": "full_verbatim_pass_d3",
    "generated_at": "2026-05-11T04:00:00+09:00",
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
            "Verbatim Appendix D Glossary reproduced for internal compliance management."
        ),
    },
    "definitions": normalized,
    "summary": {
        "total_terms": len(normalized),
        "with_abbreviation": sum(1 for e in normalized if "abbreviation" in e),
        "with_cross_references": sum(1 for e in normalized if "cross_references" in e),
        "with_notes": sum(1 for e in normalized if "notes" in e),
        "page_range": "433-468 (physical)",
        "extraction_passes": {
            "backbone_pass_v1": "17 핵심 용어만 (Preface + Part One + Part Two 기반)",
            "d3_pass": "Appendix D 전체 verbatim (이 파일)",
        },
    },
}

with open(TARGET, "w", encoding="utf-8") as f:
    yaml.dump(doc, f, sort_keys=False, allow_unicode=True,
              default_flow_style=False, width=1000)

print(f"[DONE] Written: {TARGET}")
print(f"   Total terms: {len(normalized)}")
print(f"   With abbreviation: {doc['summary']['with_abbreviation']}")
print(f"   With cross_references: {doc['summary']['with_cross_references']}")
print(f"   With notes: {doc['summary']['with_notes']}")
