#!/usr/bin/env python3
"""
RFP 파서 — extracted.json 을 받아 RFP 의 요구사항 목록표 + 상세 요구사항을 구조화한다.

산출:
    .claude/runs/ingest_rfp/parsed.json
        {
          "categories": [{"code":"ECR","name":"시스템 장비 구성 요구사항"}, ...],
          "requirements": [
            {"id":"ECR-001","category":"ECR","name":"DBMS 구축",
             "definition":"...", "details":"...", "outputs":"...",
             "start_idx": 504, "end_idx": 528, "section":"section0.xml"}
          ],
          "chapter_structure": [...],
          "list_table_only": ["XYZ-NNN", ...]  # 목록표에만 있고 상세 누락
        }
"""
import json
import re
import sys
from pathlib import Path

ID_PAT = re.compile(r"^(ECR|SFR|PER|SIR|DAR|TER|SER|QUR|COR|PMR|PSR)-(\d{3})$")

CATEGORY_NAMES = {
    "ECR": "시스템 장비 구성 요구사항",
    "SFR": "기능 요구사항",
    "PER": "성능 요구사항",
    "SIR": "인터페이스 요구사항",
    "DAR": "데이터 요구사항",
    "TER": "테스트 요구사항",
    "SER": "보안 요구사항",
    "QUR": "품질 요구사항",
    "COR": "제약사항",
    "PMR": "프로젝트 관리 요구사항",
    "PSR": "프로젝트 지원 요구사항",
}


def flatten_paragraphs(data):
    paras = []
    for s in data["sections"]:
        for p in s["paragraphs"]:
            paras.append({"sec": s["file"], **p})
    return paras


def find_requirement_anchors(paras):
    """ID 단락 위치를 식별. 요구사항 목록표 영역(317~497)은 제외하고 상세 영역만."""
    anchors = []
    for i, p in enumerate(paras):
        if i < 498:  # 목록표 영역 스킵
            continue
        m = ID_PAT.match(p["text"].strip())
        if m:
            anchors.append({"idx": i, "id": p["text"].strip(), "category": m.group(1)})
    return anchors


def collect_list_table_ids(paras):
    """목록표 영역(317-497)에 등장한 모든 ID 수집."""
    ids = []
    for i in range(317, 498):
        if i >= len(paras):
            break
        t = paras[i]["text"].strip()
        if ID_PAT.match(t):
            ids.append(t)
    return ids


def extract_requirement_block(paras, start_idx, end_idx):
    """anchor 사이 단락들에서 명칭/정의/세부내용/산출정보 추출."""
    block = [paras[i]["text"].strip() for i in range(start_idx, end_idx) if paras[i]["text"].strip()]

    name = ""
    definition_parts = []
    details_parts = []
    outputs_parts = []

    # 라벨 인덱스 찾기 — 단락 단위 (조각 라벨 합치기)
    label_positions = {}  # label_name -> position in block
    i = 0
    while i < len(block):
        t = block[i]
        # 명칭 라벨 직후
        if t == "요구사항 명칭" and i + 1 < len(block):
            label_positions["name"] = i + 1
            i += 2
            continue
        # 라벨 조각 패턴
        # "요구사항" + "상세" + "설명" + "정의" — 다음 단락부터 정의
        # 또는 한 줄로 "정의" 등장
        if t == "정의":
            label_positions["definition"] = i + 1
        elif t == "세부" and i + 1 < len(block) and block[i + 1] == "내용":
            label_positions["details"] = i + 2
        elif t == "세부내용":
            label_positions["details"] = i + 1
        elif t == "산출정보" or t == "산출 정보":
            label_positions["outputs"] = i + 1
        elif t == "산출" and i + 1 < len(block) and block[i + 1] == "정보":
            label_positions["outputs"] = i + 2
        elif t == "관련 요구사항":
            label_positions["related"] = i + 1
        i += 1

    # name 추출
    if "name" in label_positions:
        name = block[label_positions["name"]] if label_positions["name"] < len(block) else ""

    # 슬라이스: definition → 다음 라벨까지
    def slice_until(start, next_keys):
        if start is None or start >= len(block):
            return []
        next_starts = [label_positions[k] for k in next_keys if k in label_positions and label_positions[k] > start]
        # 라벨 자체 단락은 슬라이스에 포함되면 안 됨 — start+0 부터 next_start-1 (그 라벨 단어의 위치 -1)
        next_label_word_positions = []
        for k in next_keys:
            if k in label_positions:
                # label_positions 는 라벨 다음 단락 idx. 라벨 단어 자체는 그 -1 또는 그 라벨 단어 길이만큼 앞.
                # 정의: 라벨 단어 1개 ("정의")
                # 세부내용: 라벨 단어 2개 ("세부", "내용") → 시작 -2
                # 산출정보: 라벨 단어 2개 → 시작 -2 (또는 1)
                if k == "definition":
                    next_label_word_positions.append(label_positions[k] - 1)
                elif k == "details":
                    next_label_word_positions.append(label_positions[k] - 2)
                elif k == "outputs":
                    next_label_word_positions.append(label_positions[k] - 2)
                elif k == "related":
                    next_label_word_positions.append(label_positions[k] - 1)
        cut_points = [p for p in next_label_word_positions if p > start]
        end = min(cut_points) if cut_points else len(block)
        return block[start:end]

    if "definition" in label_positions:
        definition_parts = slice_until(label_positions["definition"], ["details", "outputs", "related"])
    if "details" in label_positions:
        details_parts = slice_until(label_positions["details"], ["outputs", "related"])
    if "outputs" in label_positions:
        outputs_parts = slice_until(label_positions["outputs"], ["related"])

    return {
        "name": name,
        "definition": " ".join(definition_parts).strip(),
        "details": "\n".join(details_parts).strip(),
        "outputs": " ".join(outputs_parts).strip(),
    }


def parse_chapter_structure(paras):
    """대단원 구조 — 목차 기반."""
    chapters = [
        {"id": "I", "title": "사업안내", "sections": [
            {"id": "I.1", "title": "사업개요"},
            {"id": "I.2", "title": "추진목표"},
            {"id": "I.3", "title": "추진방침"},
            {"id": "I.4", "title": "사업범위"},
            {"id": "I.5", "title": "추진계획"},
        ]},
        {"id": "II", "title": "현황", "sections": [
            {"id": "II.1", "title": "현 보건환경종합정보시스템(HEIS)"},
            {"id": "II.2", "title": "HEIS 시스템 구성"},
            {"id": "II.3", "title": "고도화대상(HEIS) 프로그램 프로세스"},
        ]},
        {"id": "III", "title": "제안 요청사항", "sections": [
            {"id": "III.1", "title": "제안요청 개요"},
            {"id": "III.2", "title": "과업 주요내용"},
            {"id": "III.3", "title": "요구사항 목록"},
            {"id": "III.4", "title": "상세 요구사항"},
        ]},
        {"id": "IV", "title": "제안안내", "sections": [
            {"id": "IV.1", "title": "사업자 선정방식"},
            {"id": "IV.2", "title": "제안서 평가 방법"},
            {"id": "IV.3", "title": "제안 안내 사항"},
            {"id": "IV.4", "title": "기타사항"},
        ]},
        {"id": "V", "title": "제안서 작성요령", "sections": [
            {"id": "V.1", "title": "제안서의 효력"},
            {"id": "V.2", "title": "제안서 작성지침 및 유의사항"},
        ]},
    ]
    return chapters


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".claude/runs/ingest_rfp/extracted.json")
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(".claude/runs/ingest_rfp/parsed.json")

    with src.open(encoding="utf-8") as f:
        data = json.load(f)
    paras = flatten_paragraphs(data)
    anchors = find_requirement_anchors(paras)
    list_ids = collect_list_table_ids(paras)

    # 각 anchor 의 종료 = 다음 anchor 시작
    requirements = []
    for i, a in enumerate(anchors):
        end = anchors[i + 1]["idx"] if i + 1 < len(anchors) else len(paras)
        block_info = extract_requirement_block(paras, a["idx"], end)
        # section 식별
        section = paras[a["idx"]]["sec"]
        requirements.append({
            "id": a["id"],
            "category": a["category"],
            "category_name": CATEGORY_NAMES.get(a["category"], ""),
            "name": block_info["name"],
            "definition": block_info["definition"],
            "details": block_info["details"],
            "outputs": block_info["outputs"],
            "start_idx": a["idx"],
            "end_idx": end - 1,
            "section": section,
        })

    detail_ids = {r["id"] for r in requirements}
    list_only = [x for x in list_ids if x not in detail_ids]
    detail_only = [r["id"] for r in requirements if r["id"] not in set(list_ids)]

    categories = [
        {"code": c, "name": CATEGORY_NAMES[c],
         "count_in_list": sum(1 for x in list_ids if x.startswith(c)),
         "count_in_detail": sum(1 for r in requirements if r["category"] == c)}
        for c in CATEGORY_NAMES
    ]

    result = {
        "categories": categories,
        "requirements": requirements,
        "chapter_structure": parse_chapter_structure(paras),
        "list_table_ids": list_ids,
        "list_only": list_only,
        "detail_only": detail_only,
        "stats": {
            "total_paragraphs": len(paras),
            "list_table_count": len(list_ids),
            "detail_count": len(requirements),
        },
    }

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(json.dumps(result["stats"], ensure_ascii=False))
    print("list_only:", list_only)
    print("detail_only:", detail_only)


if __name__ == "__main__":
    main()
