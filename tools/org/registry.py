"""조직 레지스트리 — ~/.processware/orgs.yaml (org_id → org_root).

플랫폼 체크아웃 1개로 여러 조직 루트(별도 repo)를 `--org <id>` 로 전환하기 위한 로컬 매핑.
위치는 환경변수 PROCESSWARE_HOME 으로 바꿀 수 있다.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

import yaml

ENV_HOME = "PROCESSWARE_HOME"
REGISTRY_FILE = "orgs.yaml"


def home() -> Path:
    return Path(os.environ.get(ENV_HOME) or (Path.home() / ".processware")).expanduser()


def registry_path() -> Path:
    return home() / REGISTRY_FILE


def load() -> dict:
    p = registry_path()
    if not p.is_file():
        return {}
    with open(p, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    orgs = data.get("orgs") or {}
    return {str(k): str(v) for k, v in orgs.items()}


def save(orgs: dict) -> Path:
    p = registry_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        yaml.safe_dump({"orgs": dict(sorted(orgs.items()))}, f, allow_unicode=True, sort_keys=False)
    return p


def lookup(org_id: str) -> Optional[Path]:
    v = load().get(org_id)
    return Path(v).expanduser() if v else None


def register(org_root: "Path | str") -> "tuple[str, Path]":
    """org_root 의 org.yaml 을 읽어 org_id 로 등록한다. (org_id, root) 반환."""
    from .context import ORG_YAML, OrgContextError
    from .schema import load_org_yaml, validate_org

    root = Path(org_root).expanduser().resolve()
    y = root / ORG_YAML
    if not y.is_file():
        raise OrgContextError(f"{ORG_YAML} 이 없습니다: {root}")
    data = load_org_yaml(y)
    errors, _ = validate_org(data)
    if errors:
        raise OrgContextError(f"{y} 검증 실패:\n  - " + "\n  - ".join(errors))
    oid = str(data["org_id"])
    orgs = load()
    orgs[oid] = str(root)
    save(orgs)
    return oid, root


def unregister(org_id: str) -> bool:
    orgs = load()
    if org_id not in orgs:
        return False
    del orgs[org_id]
    save(orgs)
    return True
