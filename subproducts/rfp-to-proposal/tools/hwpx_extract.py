#!/usr/bin/env python3
"""
hwpx 추출기 — Hancom HWPX (zip+XML) 에서 텍스트와 단락 구조를 뽑는다.

용도: /process-ingest 파이프라인의 Phase 2 텍스트 추출.
사용:
    python3 tools/hwpx_extract.py <unzipped_contents_dir> <output_path>
    예) python3 tools/hwpx_extract.py .claude/runs/ingest_rfp/Contents \
            .claude/runs/ingest_rfp/extracted.json

산출 JSON 스키마:
    {
      "sections": [
        {"file": "section0.xml", "paragraphs": [{"idx": 0, "text": "...", "style": "..."}]}
      ],
      "stats": {"section0_chars": N, "section1_chars": M, "total_paragraphs": K}
    }
"""
import json
import os
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

HP_NS = "http://www.hancom.co.kr/hwpml/2011/paragraph"


def extract_paragraphs(xml_path: Path):
    """단락 단위로 텍스트를 뽑는다. <hp:p> 가 하나의 단락."""
    tree = ET.parse(xml_path)
    root = tree.getroot()
    paragraphs = []
    # <hp:p> 단락 — 그 안의 모든 <hp:t> 텍스트를 이어붙임
    for idx, p in enumerate(root.iter(f"{{{HP_NS}}}p")):
        texts = []
        for t in p.iter(f"{{{HP_NS}}}t"):
            if t.text:
                texts.append(t.text)
        merged = "".join(texts).strip()
        if not merged:
            continue
        # paraPrIDRef 로 스타일 추정 가능 (헤더/본문 구분에 활용)
        style_id = p.get("paraPrIDRef", "")
        paragraphs.append({"idx": idx, "text": merged, "style": style_id})
    return paragraphs


def main():
    if len(sys.argv) != 3:
        print("usage: hwpx_extract.py <contents_dir> <output_json>", file=sys.stderr)
        sys.exit(2)
    contents_dir = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    section_files = sorted(contents_dir.glob("section*.xml"))
    if not section_files:
        print(f"no section*.xml in {contents_dir}", file=sys.stderr)
        sys.exit(1)

    sections = []
    stats = {"total_paragraphs": 0}
    for sf in section_files:
        paragraphs = extract_paragraphs(sf)
        sections.append({"file": sf.name, "paragraphs": paragraphs})
        char_count = sum(len(p["text"]) for p in paragraphs)
        stats[f"{sf.stem}_chars"] = char_count
        stats[f"{sf.stem}_paragraphs"] = len(paragraphs)
        stats["total_paragraphs"] += len(paragraphs)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump({"sections": sections, "stats": stats}, f, ensure_ascii=False, indent=2)
    print(json.dumps(stats, ensure_ascii=False))


if __name__ == "__main__":
    main()
