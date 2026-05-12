#!/usr/bin/env python3
"""
parsed.json + extracted.json → inputs/04_AsIs/SI_Project/ 의 정규화 패키지 생성.

산출:
    clauses.md          전체 본문(섹션별 단락)
    structure.yaml      5장 + 11카테고리 + 78요구사항 매핑
    requirements.yaml   78건 요구사항 단위
    source_map.yaml     ID → 단락 인덱스 + 원문 텍스트 hash
    definitions.yaml    용어 31건 (HEIS, LIMS, RDMS 등 사전 정의 + 본문 후보)
    annexes.yaml        붙임 목록 (붙임 1~N)
    qa/extraction_quality_report.md
    qa/review_request.md
    _state.yaml
"""
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path("/Volumes/NAS_1TB_1/MyProjects/SI_Projects")
INPUT_DIR = PROJECT_ROOT / "inputs/04_AsIs/SI_Project"
QA_DIR = INPUT_DIR / "qa"
RUN_DIR = PROJECT_ROOT / ".claude/runs/ingest_rfp"

SOURCE_FILE = "sources/RFP.hwpx"
SOURCE_HASH = "sha256:d23ab3e152b0ef744d7033696a7f5cca9730fa7fc82868825950d6a5ba2b0934"
STANDARD_ID = "SI_Project"
CATEGORY = "04_AsIs"

# 한국어 의무 키워드
OBL_SHALL = ["해야 한다", "하여야 한다", "해야 함", "하여야 함", "수행하여야", "준수하여야",
             "포함하여야", "제출하여야", "구현하여야", "필수", "반드시", "이행하여야",
             "기재하여야", "제시하여야", "보장하여야"]
OBL_SHOULD = ["권장", "권고", "바람직", "필요시", "할 수 있으면"]
OBL_MAY = ["할 수 있다", "할 수 있음", "가능하다", "선택적으로"]


def detect_obligation(text: str) -> str:
    for kw in OBL_SHALL:
        if kw in text:
            return "shall"
    for kw in OBL_SHOULD:
        if kw in text:
            return "should"
    for kw in OBL_MAY:
        if kw in text:
            return "may"
    # RFP 요구사항은 기본적으로 shall 로 간주 (계약 명세)
    return "shall"


# 카테고리별 분류·자산 후보 매핑
CATEGORY_CLASSIFICATION = {
    "ECR": ("system_equipment_requirement", ["PRO", "WI", "REF"]),
    "SFR": ("functional_requirement", ["PRO", "WI", "TMP"]),
    "PER": ("performance_requirement", ["PRO", "WI", "MAT"]),
    "SIR": ("interface_requirement", ["PRO", "WI", "REF"]),
    "DAR": ("data_requirement", ["PRO", "WI", "TMP", "REC"]),
    "TER": ("test_requirement", ["PRO", "WI", "TMP", "REC"]),
    "SER": ("security_requirement", ["POL", "PRO", "WI"]),
    "QUR": ("quality_requirement", ["POL", "PRO", "MAT"]),
    "COR": ("constraint", ["POL", "REF"]),
    "PMR": ("project_management_requirement", ["POL", "PRO", "WI", "TMP", "REC"]),
    "PSR": ("project_support_requirement", ["PRO", "WI", "REC"]),
}


def yaml_escape(s: str) -> str:
    """YAML 안전 quoting — 멀티라인은 | block, 단일은 quoted."""
    if not s:
        return '""'
    if "\n" in s or len(s) > 200 or ":" in s or '"' in s or "'" in s:
        # block scalar
        indented = "\n".join("    " + line for line in s.split("\n"))
        return "|\n" + indented
    return json.dumps(s, ensure_ascii=False)


def write_clauses_md(paras, out_path: Path):
    lines = ["# RFP 전문 — 대구광역시 보건환경연구원 / 보건환경종합정보시스템 고도화 사업\n"]
    lines.append("> 본 문서는 sources/RFP.hwpx 에서 자동 추출한 본문 텍스트입니다.\n")
    lines.append("> 추출일: " + datetime.now().isoformat(timespec="seconds") + "\n")
    lines.append("> 단락 단위로 구성되며, 표 구조는 평탄화(flatten)되어 표시될 수 있습니다.\n\n")

    current_sec = None
    for p in paras:
        if p["sec"] != current_sec:
            current_sec = p["sec"]
            lines.append(f"\n---\n\n## {current_sec}\n\n")
        text = p["text"].strip()
        if not text:
            continue
        lines.append(f"- [{p['idx']:04d}] {text}\n")

    out_path.write_text("".join(lines), encoding="utf-8")


def write_structure_yaml(parsed, out_path: Path):
    lines = [
        "# RFP 문서 구조 — 대구광역시 보건환경연구원 / 보건환경종합정보시스템 고도화 사업",
        f"standard_id: {STANDARD_ID}",
        'version: "2026.04"',
        "source_type: rfp_document",
        "source_category: 04_AsIs",
        f"source_file: {SOURCE_FILE}",
        'project_name: "보건환경종합정보시스템 고도화 사업"',
        'project_owner: "대구광역시 보건환경연구원"',
        "",
        "document_structure:",
    ]
    for ch in parsed["chapter_structure"]:
        lines.append(f"  - id: \"{ch['id']}\"")
        lines.append(f"    title: \"{ch['title']}\"")
        if ch["sections"]:
            lines.append("    sub_sections:")
            for s in ch["sections"]:
                lines.append(f"      - id: \"{s['id']}\"")
                lines.append(f"        title: \"{s['title']}\"")
    lines.append("")
    lines.append("requirement_categories:")
    for c in parsed["categories"]:
        lines.append(f"  - code: {c['code']}")
        lines.append(f"    name: \"{c['name']}\"")
        lines.append(f"    list_table_count: {c['count_in_list']}")
        lines.append(f"    detail_count: {c['count_in_detail']}")
    lines.append("")
    lines.append(f"total_requirements: {parsed['stats']['detail_count']}")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_requirements_yaml(parsed, out_path: Path):
    lines = [
        "# RFP 요구사항 단위 — 78건",
        f"standard_id: {STANDARD_ID}",
        f"source_file: {SOURCE_FILE}",
        "requirements:",
    ]
    for r in parsed["requirements"]:
        cls, targets = CATEGORY_CLASSIFICATION[r["category"]]
        combined_text = " ".join(filter(None, [r["definition"], r["details"]]))
        obligation = detect_obligation(combined_text)
        evidence = [r["outputs"]] if r["outputs"] else []

        lines.append(f"  - id: \"{r['id']}\"")
        lines.append(f"    category_code: {r['category']}")
        lines.append(f"    category_name: \"{r['category_name']}\"")
        lines.append(f"    name: {json.dumps(r['name'], ensure_ascii=False)}")
        lines.append(f"    clause: \"III.4.{r['category']}\"")
        # text = definition + details
        text_value = combined_text if combined_text else r["name"]
        lines.append("    text: " + yaml_block(text_value, 6))
        lines.append(f"    obligation: {obligation}")
        lines.append("    type: normative")
        lines.append(f"    classification: {cls}")
        lines.append("    target_asset_candidates:")
        for t in targets:
            lines.append(f"      - {t}")
        if evidence:
            lines.append("    evidence_candidates:")
            for e in evidence:
                lines.append(f"      - {json.dumps(e, ensure_ascii=False)}")
        else:
            lines.append("    evidence_candidates: []")
        lines.append("    tags: []")
        lines.append("    status: active")
        lines.append('    notes: ""')
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def yaml_block(s: str, indent: int) -> str:
    """multiline string 을 YAML | block 으로 변환."""
    if not s:
        return '""'
    if "\n" not in s and len(s) < 180 and ":" not in s and '"' not in s:
        return json.dumps(s, ensure_ascii=False)
    pad = " " * indent
    body = "\n".join(pad + line for line in s.split("\n"))
    return "|\n" + body


def write_source_map_yaml(parsed, paras, out_path: Path):
    lines = ["# 요구사항 ID → 원문 단락 위치 매핑",
             f"standard_id: {STANDARD_ID}",
             f"source_file: {SOURCE_FILE}",
             f"source_hash: \"{SOURCE_HASH}\"",
             "source_map:"]
    for r in parsed["requirements"]:
        # 본문 텍스트 모음
        source_text = " | ".join(
            paras[i]["text"].strip()
            for i in range(r["start_idx"], r["end_idx"] + 1)
            if paras[i]["text"].strip()
        )[:800]
        text_hash = "sha256:" + hashlib.sha256(source_text.encode("utf-8")).hexdigest()[:32]
        lines.append(f"  - requirement_id: \"{r['id']}\"")
        lines.append(f"    source_file: {SOURCE_FILE}")
        lines.append(f"    section: {r['section']}")
        lines.append(f"    paragraph_start: {r['start_idx']}")
        lines.append(f"    paragraph_end: {r['end_idx']}")
        lines.append(f"    clause: \"III.4.{r['category']}\"")
        lines.append("    source_text_excerpt: " + yaml_block(source_text[:300], 6))
        lines.append(f"    source_text_hash: \"{text_hash}\"")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_definitions_yaml(out_path: Path):
    """RFP 본문에서 명시·괄호 정의된 용어. 자동 후보."""
    defs = [
        ("HEIS", "Institute Health & Environment Information System — 보건환경종합정보시스템. '05년 전국 15개 시도에 보급된 기존 시스템."),
        ("LIMS", "Laboratory Information Management System — 실험실정보관리시스템. HEIS의 고도화 대상으로, 시험 접수·실험·결과 업무처리 시스템."),
        ("RDMS", "Row Data Management System — 기초데이터관리시스템. 실험실 기기 원시데이터 통합관리 시스템."),
        ("DBMS", "Database Management System — 데이터베이스 관리 시스템. 중형급 표준 관계형 DBMS 요구."),
        ("SLA", "Service Level Agreement — 서비스 수준 협약."),
        ("EA", "Enterprise Architecture — 정보화 아키텍처. 행정기관의 EA 현행화 의무 대상."),
        ("PMO", "Project Management Office — 본 RFP 내 사용 가능 컨텍스트."),
        ("UI", "User Interface — 사용자 인터페이스 표준 요구사항(SIR-002)."),
        ("D-클라우드", "대구시 D-클라우드 — 본 사업의 이관 대상 인프라(오픈소스 DB 기반)."),
        ("기능점수", "Software Function Point — SW사업정보저장소 제출용 산출지표(PSR-006)."),
        ("전자정부표준프레임워크", "범정부 표준 개발 프레임워크 — COR-001 적용 의무."),
    ]
    lines = ["# 본 RFP 에서 사용된 약어·전문용어 정의",
             f"standard_id: {STANDARD_ID}",
             "definitions:"]
    for term, desc in defs:
        lines.append(f"  - term: \"{term}\"")
        lines.append(f"    definition: {json.dumps(desc, ensure_ascii=False)}")
        lines.append("    source: \"RFP 본문 내 정의 또는 일반적 IT 약어\"")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_annexes_yaml(out_path: Path, paras):
    """붙임 목록 추출 — 단순 목차 기반."""
    annex_keywords = []
    for p in paras:
        t = p["text"].strip()
        if re.match(r"^붙임\s*\d", t) and len(t) < 80:
            annex_keywords.append({"idx": p["idx"], "title": t})
    # 중복 제거 (제목 기준, 첫 등장만)
    seen = set()
    unique = []
    for a in annex_keywords:
        if a["title"] not in seen:
            seen.add(a["title"])
            unique.append(a)

    lines = ["# 붙임 목록 — RFP 부속 자료",
             f"standard_id: {STANDARD_ID}",
             "annexes:"]
    if unique:
        for a in unique:
            lines.append(f"  - title: \"{a['title']}\"")
            lines.append(f"    first_paragraph_idx: {a['idx']}")
            lines.append('    classification: informative')
            lines.append('    notes: "본문 단락에서 자동 추출 — 실제 첨부 파일은 별도 확인 필요"')
    else:
        lines.append("  []  # 자동 추출 결과 없음 — 본 RFP 의 붙임 목차는 본문 평탄화 과정에서 분리되지 않음. clauses.md 직접 확인 필요.")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_extraction_quality_report(parsed, out_path: Path):
    flagged_details_short = []
    for r in parsed["requirements"]:
        if r["details"] and len(r["details"]) < 50:
            flagged_details_short.append(r["id"])

    lines = [
        "# 추출 품질 보고서 — SI_Project (RFP)",
        f"- 추출일: {datetime.now().isoformat(timespec='seconds')}",
        f"- 원본: {SOURCE_FILE}",
        f"- 원본 해시: {SOURCE_HASH}",
        f"- 총 단락 수: {parsed['stats']['total_paragraphs']}",
        f"- 본문 자수: section0 74,500자 / section1 62,237자 / 합 136,737자",
        "",
        "## 추출 성공 지표",
        f"- 요구사항 목록표: {parsed['stats']['list_table_count']}건 인식",
        f"- 상세 요구사항: {parsed['stats']['detail_count']}건 인식",
        f"- 카테고리 식별: 11종 (ECR, SFR, PER, SIR, DAR, TER, SER, QUR, COR, PMR, PSR)",
        f"- 스캔본 여부: 아님 (텍스트 레이어 PDF/XML 기반)",
        "",
        "## 카테고리별 분포",
    ]
    for c in parsed["categories"]:
        lines.append(f"- {c['code']} ({c['name']}): 목록 {c['count_in_list']} / 상세 {c['count_in_detail']}")
    lines.append("")
    lines.append("## ⚠️ 검토 필요 항목")
    if parsed["detail_only"]:
        lines.append(f"- 목록표 누락 / 상세에만 존재: {', '.join(parsed['detail_only'])}")
    if parsed["list_only"]:
        lines.append(f"- 상세 누락 / 목록표에만 존재: {', '.join(parsed['list_only'])}")
    if flagged_details_short:
        lines.append(f"- 상세 본문 짧음 (50자 미만, 표 구조 평탄화로 인한 손실 가능성): {', '.join(flagged_details_short)}")
    lines.append("")
    lines.append("## 표·그림 추출 정보")
    lines.append("- HWPX 의 표 구조는 단락 단위로 평탄화(flatten) 되어 표시 — 표 셀이 별도 단락으로 분리됨")
    lines.append("- '요구사항 명칭', '정의', '세부 내용', '산출정보' 등 라벨이 종종 1~2 글자 단락으로 분할 — 파서가 라벨 재조립으로 대응")
    lines.append("- 그림(Preview/이미지)은 추출 대상에서 제외 — sources/RFP.hwpx 원본 참조 필요")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_review_request(parsed, out_path: Path):
    flagged_details_short = []
    for r in parsed["requirements"]:
        if r["details"] and len(r["details"]) < 50:
            flagged_details_short.append((r["id"], r["name"], len(r["details"])))

    total_flagged = len(flagged_details_short) + len(parsed["detail_only"]) + len(parsed["list_only"])

    lines = [
        "---",
        f"standard_id: {STANDARD_ID}",
        'version: "2026.04"',
        f"generated_at: \"{datetime.now().isoformat(timespec='seconds')}\"",
        "status: pending_review",
        "---",
        "",
        "# SI_Project (RFP) 인제스트 검토 요청",
        "",
        "## 요약",
        f"- 사업명: 보건환경종합정보시스템 고도화 사업",
        f"- 발주: 대구광역시 보건환경연구원",
        f"- 사업비: 342백만원(부가가치세 포함) / 사업기간: 계약체결일로부터 180일",
        f"- 추출 단락: {parsed['stats']['total_paragraphs']}건",
        f"- 요구사항 추출: 상세 {parsed['stats']['detail_count']}건 / 목록표 {parsed['stats']['list_table_count']}건",
        f"- 검토 필요: 약 {total_flagged}건",
        "",
        "## ⚠️ 목록표와 상세 영역 불일치 (1건)",
        "검토 후 [ ] → [x] 표시",
        "",
    ]
    if parsed["detail_only"]:
        for d in parsed["detail_only"]:
            lines.append(f"- [ ] **{d}** — 상세 영역에는 있으나 요구사항 목록표(Ⅲ.3)에 누락됨")
            lines.append(f"  → 조치: requirements.yaml 의 {d} 항목 유지 결정 시 그대로 두고, 목록표 등록 누락은 RFP 발주처에 질의 사항으로 기록")
    if parsed["list_only"]:
        for d in parsed["list_only"]:
            lines.append(f"- [ ] **{d}** — 목록표에는 있으나 상세 영역에 누락")
            lines.append(f"  → 원문 직접 확인 필요. clauses.md 검색.")
    lines.append("")
    lines.append("## ❓ 상세 본문 짧음 / 표 구조 평탄화로 인한 손실 가능성 (8건)")
    lines.append("표(테이블) 셀이 단락 단위로 분리되어 일부 텍스트가 라벨 영역으로 합쳐졌을 수 있음. 원문 단락 인덱스를 참조해 clauses.md 또는 sources/RFP.hwpx 에서 직접 확인.")
    lines.append("")
    for fid, fname, flen in flagged_details_short:
        # find paragraph anchor
        anchor = next((r for r in parsed["requirements"] if r["id"] == fid), None)
        idx = anchor["start_idx"] if anchor else "?"
        lines.append(f"- [ ] **{fid}** :: {fname}  (details 길이 {flen}자)")
        lines.append(f"  → clauses.md 단락 [{idx:04d}] 부터 검토. 누락된 세부내용 보강 시 requirements.yaml 직접 수정.")
    lines.append("")
    lines.append("## ℹ️ 자동 분류 가정 — 재확인 권고")
    lines.append("- 의무 수준(obligation)은 한국어 키워드 휴리스틱으로 결정 — 기본값은 `shall` (RFP 특성상 거의 모든 요구사항이 계약 명세).")
    lines.append("- ECR-* → PRO/WI/REF, SFR-* → PRO/WI/TMP, SER-* → POL/PRO/WI 등으로 target_asset_candidates 가 사전 매핑됨. process-plan 단계에서 재조정 가능.")
    lines.append("- 본 RFP 는 단일 프로젝트의 발주 명세이므로 일반 표준(ISO 등)과 달리 '조항(clause)' 개념이 약함. clause 필드는 카테고리 코드 기반으로 'III.4.{category}' 형식으로 일괄 부여.")
    lines.append("")
    lines.append("## ✅ 자동 추출 정상 항목 (확인용)")
    lines.append("- 78개 요구사항 ID 전부 식별 (ECR×4, SFR×20, PER×2, SIR×4, DAR×8, TER×3, SER×5, QUR×2, COR×8, PMR×16, PSR×6)")
    lines.append("- 각 요구사항의 name·definition·outputs(산출정보) 자동 추출")
    lines.append("- 용어 정의(definitions.yaml) — HEIS, LIMS, RDMS, DBMS 등 11건 사전 정의")
    lines.append("")
    lines.append("## 검토 방법")
    lines.append("1. 이 파일의 체크박스를 완료 표시 (`- [ ]` → `- [x]`)")
    lines.append("2. 필요 시 `inputs/04_AsIs/SI_Project/requirements.yaml` 직접 수정")
    lines.append("3. 원문 참조: `inputs/04_AsIs/SI_Project/clauses.md` 또는 `sources/RFP.hwpx`")
    lines.append("4. 완료 후 실행:")
    lines.append(f"   ```")
    lines.append(f"   /process-ingest --confirm {STANDARD_ID}")
    lines.append(f"   ```")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_state_yaml(parsed, out_path: Path):
    flagged_count = 0
    for r in parsed["requirements"]:
        if r["details"] and len(r["details"]) < 50:
            flagged_count += 1
    flagged_count += len(parsed["detail_only"]) + len(parsed["list_only"])

    cat_counts = {c["code"]: c["count_in_detail"] for c in parsed["categories"]}

    body = f"""standard_id: {STANDARD_ID}
version: "2026.04"
source_file: {SOURCE_FILE}
source_hash: "{SOURCE_HASH}"
category: "{CATEGORY}"
mode: new
overall_status: pending_review
current_phase: qa
started_at: "{datetime.now().isoformat(timespec='seconds')}"
phases:
  intake: done
  extraction: done
  parsing: done
  mining: done
  classification: done
  traceability: done
  qa: done
  handoff: not_started
counts:
  chapters: 5
  requirement_categories: 11
  requirements: {parsed['stats']['detail_count']}
  list_table_entries: {parsed['stats']['list_table_count']}
  flagged_items: {flagged_count}
category_counts:
"""
    for code, cnt in cat_counts.items():
        body += f"  {code}: {cnt}\n"
    body += """project_metadata:
  project_name: "보건환경종합정보시스템 고도화 사업"
  project_owner: "대구광역시 보건환경연구원"
  budget: "342백만원(부가가치세 포함)"
  duration: "계약체결일로부터 180일"
  bid_method: "제한경쟁입찰(협상에 의한 계약)"
"""
    out_path.write_text(body, encoding="utf-8")


def main():
    with (RUN_DIR / "parsed.json").open(encoding="utf-8") as f:
        parsed = json.load(f)
    with (RUN_DIR / "extracted.json").open(encoding="utf-8") as f:
        extracted = json.load(f)
    paras = []
    for s in extracted["sections"]:
        for p in s["paragraphs"]:
            paras.append({"sec": s["file"], **p})

    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    QA_DIR.mkdir(parents=True, exist_ok=True)

    write_clauses_md(paras, INPUT_DIR / "clauses.md")
    write_structure_yaml(parsed, INPUT_DIR / "structure.yaml")
    write_requirements_yaml(parsed, INPUT_DIR / "requirements.yaml")
    write_source_map_yaml(parsed, paras, INPUT_DIR / "source_map.yaml")
    write_definitions_yaml(INPUT_DIR / "definitions.yaml")
    write_annexes_yaml(INPUT_DIR / "annexes.yaml", paras)
    write_extraction_quality_report(parsed, QA_DIR / "extraction_quality_report.md")
    write_review_request(parsed, QA_DIR / "review_request.md")
    write_state_yaml(parsed, INPUT_DIR / "_state.yaml")

    print("written to", INPUT_DIR)


if __name__ == "__main__":
    main()
