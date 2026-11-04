"""tools.org — 조직 컨텍스트 (org-layer.md §3 단계 1).

활성 조직 루트를 해석하여 vault / inputs / sources / runs / queues / states 경로를 제공한다.
사용: python -m tools.org context [--format env|json|table] [--org <id> | --org-root <path>]
"""

from .context import OrgContext, OrgContextError, resolve, find_platform_root

__all__ = ["OrgContext", "OrgContextError", "resolve", "find_platform_root"]
