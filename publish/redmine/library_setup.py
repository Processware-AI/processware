"""
Library 프로젝트 계층 자동 생성 및 config.yaml by_pro 자동 채우기.

vault의 PRO 파일을 스캔 →
  Redmine: lib-{scope} 상위 프로젝트 + lib-{scope}-{pro_slug} 서브프로젝트 생성
  config.yaml: by_pro 섹션 자동 갱신
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Optional

import frontmatter
import yaml

from redmine_client import RedmineClient

# 활성 조직 컨텍스트 (org-layer 단계 6) — vault · 설정 · DB 는 조직 루트에 있다
_PUBLISH_DIR = Path(__file__).resolve().parents[1]
if str(_PUBLISH_DIR) not in sys.path:
    sys.path.insert(0, str(_PUBLISH_DIR))
import orgctx  # noqa: E402

# Redmine identifier는 소문자·숫자·하이픈만 허용, 최대 100자
_IDENT_RE = re.compile(r"[^a-z0-9\-]")


def _slugify(text: str) -> str:
    return _IDENT_RE.sub("-", text.lower()).strip("-")


def _pro_slug(doc_id: str) -> str:
    """PRO-ISO27001-001-002 → p001-002 (scope 제외 숫자 부분)."""
    parts = doc_id.upper().split("-")
    # 형식: PRO-{SCOPE}-{POL번호}-{PRO순번}
    # parts[0]=PRO, parts[1]=scope(여러 토큰 가능), parts[-2]=pol, parts[-1]=pro
    if len(parts) >= 3:
        return f"p{parts[-2]}-{parts[-1]}"
    return _slugify(doc_id)


def scan_pro_files() -> list[dict]:
    """vault 에서 type=PRO 파일 전체 스캔 → 메타 목록 반환."""
    results = []
    for path in orgctx.vault_root().rglob("*.md"):
        if "99_템플릿" in str(path) or "README" in path.name:
            continue
        try:
            post = frontmatter.load(path)
        except Exception:
            continue
        meta = post.metadata
        if meta.get("type", "").upper() != "PRO":
            continue
        doc_id = meta.get("doc_id", "")
        if not doc_id or "{{" in doc_id:
            continue
        scope_code = (meta.get("scope_code")
                      or (meta.get("standards") or [None])[0])
        results.append({
            "doc_id": doc_id,
            "title": meta.get("title", doc_id),
            "scope_code": scope_code,
            "path": path,
        })
    return results


def parent_identifier_for(scope_code: str, cfg: dict) -> str:
    """상위 프로젝트 identifier — config by_scope_code override, 없으면 lib-{prefix}-{scope}."""
    by_scope = (cfg.get("project_mapping") or {}).get("by_scope_code") or {}
    if scope_code in by_scope and by_scope[scope_code]:
        return by_scope[scope_code]
    return f"lib-{orgctx.project_prefix()}-{_slugify(scope_code)}"


def build_project_identifier(scope_code: str, pro_doc_id: str) -> str:
    """lib-{prefix}-iso27001-p001-001 형식 identifier 생성 (조직 접두어 포함)."""
    scope_slug = _slugify(scope_code)
    pro_part = _pro_slug(pro_doc_id)
    return f"lib-{orgctx.project_prefix()}-{scope_slug}-{pro_part}"


def setup_library(client: RedmineClient, cfg: dict,
                  dry_run: bool = False) -> dict:
    """
    1. vault PRO 파일 스캔
    2. 상위 프로젝트(lib-{scope}) 확인/생성
    3. 서브프로젝트(lib-{scope}-{pro_slug}) 확인/생성
    4. config.yaml by_pro 갱신
    반환: {"created": [...], "existing": [...], "skipped": [...]}
    """
    pros = scan_pro_files()
    if not pros:
        print("  vault에 PRO 파일이 없습니다. /process-plan 실행 후 재시도하세요.")
        return {"created": [], "existing": [], "skipped": []}

    by_pro = cfg["project_mapping"].get("by_pro", {}) or {}

    created, existing, skipped = [], [], []

    for pro in pros:
        scope = pro["scope_code"]
        doc_id = pro["doc_id"]

        if not scope:
            skipped.append({"doc_id": doc_id, "reason": "scope_code / standards 없음"})
            continue

        parent_identifier = parent_identifier_for(scope, cfg)
        sub_identifier = build_project_identifier(scope, doc_id)
        sub_name = f"[{doc_id}] {pro['title']}"

        if dry_run:
            status = "exists" if doc_id in by_pro else "would-create"
            print(f"  {'👁':2s} {status:14s}  {sub_identifier}  ←  {doc_id}")
            created.append(sub_identifier)
            continue

        # 상위 프로젝트 확인 / 생성 (lib-{prefix}-{scope})
        parent, parent_new = client.get_or_create_project(
            identifier=parent_identifier,
            name=f"[{orgctx.org_id()}] {scope} Library",
            description=f"processware Library — org {orgctx.org_id()} / scope {scope}",
        )
        if parent_new:
            print(f"  ✅  created     {parent_identifier}  (상위)")

        # 서브프로젝트 확인/생성
        proj, is_new = client.get_or_create_project(
            identifier=sub_identifier,
            name=sub_name,
            parent_id=parent["id"],
            description=f"processware Library Module: {doc_id}",
        )
        action = "created" if is_new else "existing"
        icon = "✅" if is_new else "·"
        print(f"  {icon}  {action:10s}  {sub_identifier}")

        (created if is_new else existing).append(sub_identifier)

        # by_pro 갱신
        if doc_id not in by_pro:
            by_pro[doc_id] = sub_identifier

    # config.yaml by_pro 저장
    if not dry_run and by_pro:
        _update_config_by_pro(by_pro)
        print(f"\n  config.yaml by_pro 갱신: {len(by_pro)}개 항목")

    return {"created": created, "existing": existing, "skipped": skipped}


def create_wiki_index_pages(client: RedmineClient, cfg: dict,
                             dry_run: bool = False) -> None:
    """Library Module마다 WI/ PRO/ TMP/ EX/ 부모 페이지 생성."""
    by_pro = cfg["project_mapping"].get("by_pro") or {}
    if not by_pro:
        return

    INDEX_PAGES = [
        ("POL",   "정책 (POL)"),
        ("PRO",   "절차서 (PRO)"),
        ("WI",    "업무지침 (WI)"),
        ("TMP",   "양식 (TMP)"),
        ("EX",    "작성예시 (EX)"),
        ("MAT",   "매핑매트릭스 (MAT)"),
        ("AUDIT", "심사보고서 (AUDIT)"),
        ("GAP",   "GAP분석 (GAP)"),
    ]

    for doc_id, project_id in by_pro.items():
        for page_title, page_name in INDEX_PAGES:
            body = f"# {page_name}\n\n> 이 페이지는 processware가 자동 관리합니다.\n\n"
            if dry_run:
                print(f"  👁  index page  {project_id}/wiki/{page_title}")
                continue
            try:
                client.upsert_wiki_page(project_id, page_title, body)
            except Exception as e:
                print(f"  ⚠️  {project_id}/wiki/{page_title} 생성 실패: {e}")


def _update_config_by_pro(by_pro: dict) -> None:
    """{ORG_ROOT}/publish/redmine/config.yaml 의 project_mapping.by_pro 섹션만 업데이트."""
    cfg_path = orgctx.config_path("redmine")
    with open(cfg_path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    cfg["project_mapping"]["by_pro"] = by_pro
    with open(cfg_path, "w", encoding="utf-8") as f:
        yaml.dump(cfg, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
