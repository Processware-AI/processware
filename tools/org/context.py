"""조직 컨텍스트 해석 (org-layer.md §3 단계 1).

해석 우선순위:
  1. 인자 org_root (CLI --org-root)
  2. 인자 org     (CLI --org <id>, 레지스트리 조회)
  3. 환경변수 PROCESSWARE_ORG_ROOT
  4. 환경변수 PROCESSWARE_ORG (레지스트리 조회)
  5. fallback: default 조직 = 플랫폼 repo 의 vault/ (단계 3 마이그레이션 완료 후 제거 예정)

조직 모드 레이아웃 ({ORG_ROOT} 기준):
  vault/  inputs/  sources/  .processware/{runs,queues,states}
default 모드 레이아웃 (플랫폼 repo 기준):
  vault/  inputs/  sources/  .claude/{runs,queues,states}
"""

from __future__ import annotations

import os
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional

ENV_ORG_ROOT = "PROCESSWARE_ORG_ROOT"
ENV_ORG = "PROCESSWARE_ORG"
ENV_PLATFORM_ROOT = "PROCESSWARE_PLATFORM_ROOT"
ORG_YAML = "org.yaml"
DEFAULT_ORG_ID = "default"
MODE_ORG = "org"
MODE_DEFAULT = "default"

# 플랫폼 repo 루트 판별 마커 (하나라도 있으면 플랫폼 루트)
_PLATFORM_MARKERS = ("tools/vault_rules/__init__.py", ".claude/commands")


class OrgContextError(Exception):
    """조직 컨텍스트를 해석할 수 없을 때."""


@dataclass(frozen=True)
class OrgContext:
    org_id: str
    mode: str            # "org" | "default"
    source: str          # 해석 근거 (arg:org-root / arg:org / env:... / fallback:default)
    org_root: Path
    vault: Path
    inputs: Path
    sources: Path
    runs: Path
    queues: Path
    states: Path
    platform_root: Path
    org_yaml: Optional[Path]

    def as_dict(self) -> dict:
        d = asdict(self)
        return {k: (str(v) if isinstance(v, Path) else v) for k, v in d.items()}

    def as_env(self) -> dict[str, str]:
        """에이전트/커맨드가 그대로 export 할 수 있는 환경변수 맵."""
        return {
            "PROCESSWARE_ORG_ID": self.org_id,
            "PROCESSWARE_ORG_MODE": self.mode,
            "PROCESSWARE_ORG_SOURCE": self.source,
            "PROCESSWARE_ORG_ROOT": str(self.org_root),
            "PROCESSWARE_VAULT": str(self.vault),
            "PROCESSWARE_INPUTS": str(self.inputs),
            "PROCESSWARE_SOURCES": str(self.sources),
            "PROCESSWARE_RUNS": str(self.runs),
            "PROCESSWARE_QUEUES": str(self.queues),
            "PROCESSWARE_STATES": str(self.states),
            "PROCESSWARE_PLATFORM_ROOT": str(self.platform_root),
            "PROCESSWARE_ORG_YAML": str(self.org_yaml) if self.org_yaml else "",
        }

    def contains(self, path: "os.PathLike[str] | str") -> bool:
        """주어진 경로가 활성 조직 루트 안에 있는지 (격리 가드, 단계 5 에서 사용)."""
        p = Path(path).resolve()
        try:
            p.relative_to(self.org_root.resolve())
            return True
        except ValueError:
            return False


# ── 플랫폼 루트 ────────────────────────────────────────────────────────────

def find_platform_root(start: "os.PathLike[str] | str | None" = None) -> Path:
    """cwd(또는 start) 에서 위로 올라가며 플랫폼 repo 루트를 찾는다.

    환경변수 PROCESSWARE_PLATFORM_ROOT 가 있으면 그것을 우선한다.
    못 찾으면 start 자체를 반환한다.
    """
    env = os.environ.get(ENV_PLATFORM_ROOT)
    if env:
        return Path(env).resolve()

    here = Path(start or Path.cwd()).resolve()
    for candidate in (here, *here.parents):
        if any((candidate / m).exists() for m in _PLATFORM_MARKERS):
            return candidate
    return here


# ── 레이아웃 ───────────────────────────────────────────────────────────────

def _org_layout(root: Path) -> dict:
    dot = root / ".processware"
    return {
        "vault": root / "vault",
        "inputs": root / "inputs",
        "sources": root / "sources",
        "runs": dot / "runs",
        "queues": dot / "queues",
        "states": dot / "states",
    }


def _default_layout(platform_root: Path) -> dict:
    dot = platform_root / ".claude"
    return {
        "vault": platform_root / "vault",
        "inputs": platform_root / "inputs",
        "sources": platform_root / "sources",
        "runs": dot / "runs",
        "queues": dot / "queues",
        "states": dot / "states",
    }


# ── 해석 ───────────────────────────────────────────────────────────────────

def resolve(
    org: Optional[str] = None,
    org_root: "os.PathLike[str] | str | None" = None,
    cwd: "os.PathLike[str] | str | None" = None,
    strict: bool = True,
    allow_default: bool = True,
) -> OrgContext:
    """활성 조직 컨텍스트를 해석한다.

    strict=True   : 조직 모드에서 org.yaml 검증 오류가 있으면 OrgContextError.
    allow_default : False 이면 fallback 을 금지하고 OrgContextError (단계 3 완료 후 기본 동작).
    """
    from . import registry  # 지연 import (순환 방지)

    platform_root = find_platform_root(cwd)

    root: Optional[Path] = None
    source = ""

    if org_root:
        root, source = Path(org_root), "arg:org-root"
    elif org:
        found = registry.lookup(org)
        if found is None:
            raise OrgContextError(
                f"조직 '{org}' 이 레지스트리에 없습니다. "
                "`python -m tools.org register <org_root>` 로 등록하거나 --org-root 를 쓰세요."
            )
        root, source = found, "arg:org"
    elif os.environ.get(ENV_ORG_ROOT):
        root, source = Path(os.environ[ENV_ORG_ROOT]), f"env:{ENV_ORG_ROOT}"
    elif os.environ.get(ENV_ORG):
        oid = os.environ[ENV_ORG]
        found = registry.lookup(oid)
        if found is None:
            raise OrgContextError(f"{ENV_ORG}={oid} 가 레지스트리에 없습니다.")
        root, source = found, f"env:{ENV_ORG}"

    if root is None:
        if not allow_default:
            raise OrgContextError(
                f"활성 조직이 없습니다. {ENV_ORG_ROOT} 를 설정하거나 --org/--org-root 를 지정하세요."
            )
        return OrgContext(
            org_id=DEFAULT_ORG_ID,
            mode=MODE_DEFAULT,
            source="fallback:default",
            org_root=platform_root,
            platform_root=platform_root,
            org_yaml=None,
            **_default_layout(platform_root),
        )

    root = root.expanduser().resolve()
    if not root.is_dir():
        raise OrgContextError(f"조직 루트가 디렉토리가 아닙니다: {root} ({source})")

    org_yaml = root / ORG_YAML
    if not org_yaml.is_file():
        raise OrgContextError(
            f"조직 루트에 {ORG_YAML} 이 없습니다: {root} ({source}). "
            f"`python -m tools.org init {root} --org-id <id> --name <명칭>` 으로 생성하세요."
        )

    from .schema import load_org_yaml, validate_org

    data = load_org_yaml(org_yaml)
    errors, _warnings = validate_org(data)
    if errors and strict:
        raise OrgContextError(f"{org_yaml} 검증 실패:\n  - " + "\n  - ".join(errors))

    return OrgContext(
        org_id=str(data.get("org_id", root.name)),
        mode=MODE_ORG,
        source=source,
        org_root=root,
        platform_root=platform_root,
        org_yaml=org_yaml,
        **_org_layout(root),
    )
