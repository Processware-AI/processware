"""vault Markdown → Redmine Markdown 변환."""

import re
from datetime import datetime


HEADER_TEMPLATE = """\
> **[자동생성]** 이 문서는 processware vault에서 자동 배포됩니다. 직접 편집하지 마세요.
> 원본: `{vault_path}` | 버전: {version} | 최종갱신: {updated}

---

"""


def transform(content: str, metadata: dict, vault_path: str) -> str:
    """frontmatter 제거 → 자동 헤더 삽입 → wikilink 변환."""
    body = _strip_frontmatter(content)
    header = HEADER_TEMPLATE.format(
        vault_path=vault_path,
        version=metadata.get("version", "-"),
        updated=metadata.get("updated", datetime.now().strftime("%Y-%m-%d")),
    )
    body = _convert_wikilinks(body)
    return header + body


def _strip_frontmatter(content: str) -> str:
    """--- ... --- 블록 제거."""
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            return content[end + 4:].lstrip("\n")
    return content


def _convert_wikilinks(text: str) -> str:
    """[[WI-XXX_제목]] → [[WI-XXX 제목]] (Redmine wiki 링크 포맷)."""
    def replacer(m):
        inner = m.group(1)
        # 별칭 링크 [[target|alias]] 처리
        if "|" in inner:
            target, alias = inner.split("|", 1)
            slug = _to_redmine_title(target.strip())
            return f"[[{slug}|{alias.strip()}]]"
        slug = _to_redmine_title(inner.strip())
        return f"[[{slug}]]"

    return re.sub(r"\[\[([^\]]+)\]\]", replacer, text)


def _to_redmine_title(obsidian_title: str) -> str:
    """Obsidian 파일명 스타일 → Redmine wiki 페이지 제목 (밑줄 → 공백)."""
    # 파일 확장자 제거
    title = re.sub(r"\.md$", "", obsidian_title)
    # 첫 번째 밑줄 이후를 공백으로 (doc_id_제목 → doc_id 제목)
    title = title.replace("_", " ", 1)
    return title
