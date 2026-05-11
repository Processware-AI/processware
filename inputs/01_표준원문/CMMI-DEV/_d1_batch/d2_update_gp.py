"""
D-2 update: replace canonical GG3, GP 2.4-2.10, GP 3.1-3.2 entries
with verbatim text from PDF p.82-119.
"""

import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

REQ_YAML = Path(r"C:\MyProjects\processware\inputs\01_표준원문\CMMI-DEV\requirements.yaml")

# Verbatim D-2 extracts
D2_UPDATES = {
    "CMMIDEV-GG3-REQ-001": {
        "clause": "GG 3",
        "clause_title": "Institutionalize a Defined Process",
        "text": "The process is institutionalized as a defined process.",
        "obligation": "shall",
        "type": "normative",
        "classification": "process_requirement",
        "component": "required",
        "target_asset_candidates": ["POL", "PRO", "MAT"],
        "evidence_candidates": [
            "tailored project-defined process from OSSP",
            "process related experiences contributed to OPA",
        ],
        "applies_to_levels": ["ML3", "CL3"],
        "applies_to": ["all 22 process areas (at ML3 and above)"],
        "status": "active_verbatim",
        "source_page": 115,
    },
    "CMMIDEV-GP2.4-REQ-001": {
        "clause": "GP 2.4",
        "clause_title": "Assign Responsibility",
        "text": "Assign responsibility and authority for performing the process, developing the work products, and providing the services of the process.",
        "obligation": "shall",
        "type": "normative",
        "classification": "role_requirement",
        "component": "expected",
        "target_asset_candidates": ["POL", "PRO", "MAT"],
        "parent_goal": "GG2",
        "subpractices": [
            "Assign overall responsibility and authority for performing the process.",
            "Assign responsibility and authority for performing the specific tasks of the process.",
            "Confirm that the people assigned to the responsibilities and authorities understand and accept them.",
        ],
        "status": "active_verbatim",
        "source_page": 82,
    },
    "CMMIDEV-GP2.5-REQ-001": {
        "clause": "GP 2.5",
        "clause_title": "Train People",
        "text": "Train the people performing or supporting the process as needed.",
        "obligation": "shall",
        "type": "normative",
        "classification": "process_requirement",
        "component": "expected",
        "target_asset_candidates": ["PRO", "REC"],
        "parent_goal": "GG2",
        "status": "active_verbatim",
        "source_page": 83,
    },
    "CMMIDEV-GP2.6-REQ-001": {
        "clause": "GP 2.6",
        "clause_title": "Control Work Products",
        "text": "Place selected work products of the process under appropriate levels of control.",
        "obligation": "shall",
        "type": "normative",
        "classification": "evidence_requirement",
        "component": "expected",
        "target_asset_candidates": ["PRO", "REC"],
        "parent_goal": "GG2",
        "status": "active_verbatim",
        "source_page": 88,
    },
    "CMMIDEV-GP2.7-REQ-001": {
        "clause": "GP 2.7",
        "clause_title": "Identify and Involve Relevant Stakeholders",
        "text": "Identify and involve the relevant stakeholders of the process as planned.",
        "obligation": "shall",
        "type": "normative",
        "classification": "process_requirement",
        "component": "expected",
        "target_asset_candidates": ["PRO", "MAT", "REC"],
        "parent_goal": "GG2",
        "subpractices": [
            "Identify stakeholders relevant to this process and their appropriate involvement.",
            "Share these identifications with project planners or other planners as appropriate.",
            "Involve relevant stakeholders as planned.",
        ],
        "status": "active_verbatim",
        "source_page": 93,
    },
    "CMMIDEV-GP2.8-REQ-001": {
        "clause": "GP 2.8",
        "clause_title": "Monitor and Control the Process",
        "text": "Monitor and control the process against the plan for performing the process and take appropriate corrective action.",
        "obligation": "shall",
        "type": "normative",
        "classification": "process_requirement",
        "component": "expected",
        "target_asset_candidates": ["PRO", "REC"],
        "parent_goal": "GG2",
        "subpractices": [
            "Evaluate actual progress and performance against the plan for performing the process.",
            "Review accomplishments and results of the process against the plan for performing the process.",
            "Review activities, status, and results of the process with the immediate level of management responsible for the process and identify issues.",
            "Identify and evaluate the effects of significant deviations from the plan for performing the process.",
            "Identify problems in the plan for performing the process and in the execution of the process.",
            "Take corrective action when requirements and objectives are not being satisfied, when issues are identified, or when progress differs significantly from the plan for performing the process.",
            "Track corrective action to closure.",
        ],
        "status": "active_verbatim",
        "source_page": 100,
    },
    "CMMIDEV-GP2.9-REQ-001": {
        "clause": "GP 2.9",
        "clause_title": "Objectively Evaluate Adherence",
        "text": "Objectively evaluate adherence of the process and selected work products against the process description, standards, and procedures, and address noncompliance.",
        "obligation": "shall",
        "type": "normative",
        "classification": "process_requirement",
        "component": "expected",
        "target_asset_candidates": ["PRO", "REC", "MAT"],
        "parent_goal": "GG2",
        "status": "active_verbatim",
        "source_page": 106,
    },
    "CMMIDEV-GP2.10-REQ-001": {
        "clause": "GP 2.10",
        "clause_title": "Review Status with Higher Level Management",
        "text": "Review the activities, status, and results of the process with higher level management and resolve issues.",
        "obligation": "shall",
        "type": "normative",
        "classification": "role_requirement",
        "component": "expected",
        "target_asset_candidates": ["PRO", "REC"],
        "parent_goal": "GG2",
        "status": "active_verbatim",
        "source_page": 113,
    },
    "CMMIDEV-GP3.1-REQ-001": {
        "clause": "GP 3.1",
        "clause_title": "Establish a Defined Process",
        "text": "Establish and maintain the description of a defined process.",
        "obligation": "shall",
        "type": "normative",
        "classification": "process_requirement",
        "component": "expected",
        "target_asset_candidates": ["PRO", "MAT"],
        "parent_goal": "GG3",
        "subpractices": [
            "Select from the organization's set of standard processes those processes that cover the process area and best meet the needs of the project or organizational function.",
            "Establish the defined process by tailoring the selected processes according to the organization's tailoring guidelines.",
            "Ensure that the organization's process objectives are appropriately addressed in the defined process.",
            "Document the defined process and the records of the tailoring.",
            "Revise the description of the defined process as necessary.",
        ],
        "status": "active_verbatim",
        "source_page": 115,
    },
    "CMMIDEV-GP3.2-REQ-001": {
        "clause": "GP 3.2",
        "clause_title": "Collect Process Related Experiences",
        "text": "Collect process related experiences derived from planning and performing the process to support the future use and improvement of the organization's processes and process assets.",
        "obligation": "shall",
        "type": "normative",
        "classification": "evidence_requirement",
        "component": "expected",
        "target_asset_candidates": ["REC", "MAT"],
        "parent_goal": "GG3",
        "subpractices": [
            "Store process and product measures in the organization's measurement repository.",
            "Submit documentation for inclusion in the organization's process asset library.",
            "Document lessons learned from the process for inclusion in the organization's process asset library.",
            "Propose improvements to the organizational process assets.",
        ],
        "status": "active_verbatim",
        "source_page": 115,
    },
}

# Load
with open(REQ_YAML, "r", encoding="utf-8") as f:
    doc = yaml.safe_load(f)

# Update
updated_ids = []
for r in doc["requirements"]:
    rid = r.get("id", "")
    if rid in D2_UPDATES:
        # Add 'id' field back since we're replacing whole content
        new_entry = {"id": rid, **D2_UPDATES[rid]}
        r.clear()
        r.update(new_entry)
        updated_ids.append(rid)

print(f"Updated {len(updated_ids)} entries:")
for rid in updated_ids:
    print(f"  - {rid}")

# Update extraction_mode label
doc["extraction_mode"] = "full_verbatim_pass_d1_d2"

# Recompute summary
counts_by_status = {}
counts_verbatim = 0
for r in doc["requirements"]:
    st = r.get("status", "unknown")
    counts_by_status[st] = counts_by_status.get(st, 0) + 1
    if "verbatim" in st:
        counts_verbatim += 1

doc["summary"]["by_status"] = counts_by_status
doc["summary"]["pdf_verbatim_count"] = counts_verbatim
doc["summary"]["extraction_passes"]["d2_pass"] = "GP 2.4-2.10, GP 3.1, GP 3.2, GG 3 (10 canonical → verbatim)"

# Write back
with open(REQ_YAML, "w", encoding="utf-8") as f:
    yaml.dump(doc, f, sort_keys=False, allow_unicode=True,
              default_flow_style=False, width=1000)

print(f"\n[DONE] Updated requirements.yaml")
print(f"   Status counts: {counts_by_status}")
print(f"   Verbatim total: {counts_verbatim} / {len(doc['requirements'])}")
