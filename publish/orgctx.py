"""publish/ 공통 — 활성 조직 컨텍스트 (org-layer.md §3 단계 6).

publish/* 는 플랫폼 repo 의 코드지만 데이터(vault · 설정 · sync_map DB · 로그)는 모두 **조직 루트** 에 있다.

  {ORG_ROOT}/vault/                              ← 동기화 대상
  {ORG_ROOT}/publish/{target}/config.yaml         ← 연동 설정 (core/org_base 에서 시드, 조직이 편집)
  {ORG_ROOT}/.processware/publish/{target}_sync.db ← sync_map · workspace_map
  {ORG_ROOT}/.processware/publish/{target}_sync.log
  {ORG_ROOT}/org.yaml → redmine.enabled · redmine.project_prefix (기본 org_id)

Redmine 식별자: lib-{prefix}-{scope}  /  lib-{prefix}-{scope}-{pro_slug}  /  ws-{prefix}-{slug}
"""

from __future__ import annotations

import sys
from pathlib import Path

PLATFORM_ROOT = Path(__file__).resolve().parents[1]
if str(PLATFORM_ROOT) not in sys.path:
    sys.path.insert(0, str(PLATFORM_ROOT))

# Windows 콘솔(cp949)에서도 한글·기호가 깨지지 않도록 — publish/* 전부 이 모듈을 import 한다
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        try:
            _s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

from tools.org import OrgContextError, resolve          # noqa: E402
from tools.org.schema import load_org_yaml              # noqa: E402

_ctx = None
_org = None


def ctx():
    """활성 조직 컨텍스트 (1회 해석, 실패 시 메시지 출력 후 exit 1)."""
    global _ctx, _org
    if _ctx is None:
        try:
            _ctx = resolve()
        except OrgContextError as e:
            print(f"❌ {e}", file=sys.stderr)
            sys.exit(1)
        _org = load_org_yaml(_ctx.org_yaml)
    return _ctx


def org_yaml() -> dict:
    ctx()
    return _org


def org_root() -> Path:
    return ctx().org_root


def vault_root() -> Path:
    return ctx().vault


def org_id() -> str:
    return ctx().org_id


def project_prefix() -> str:
    """Redmine 프로젝트 식별자 접두어 — org.yaml redmine.project_prefix, 기본 org_id."""
    rd = org_yaml().get("redmine") or {}
    return str(rd.get("project_prefix") or org_id()).lower()


def redmine_enabled() -> bool:
    rd = org_yaml().get("redmine") or {}
    return bool(rd.get("enabled", False))


def ensure_enabled(target: str = "redmine") -> None:
    if target == "redmine" and not redmine_enabled():
        print(
            f"❌ 조직 '{org_id()}' 의 org.yaml 에서 redmine.enabled 가 false 입니다. "
            f"연동을 켜려면 {ctx().org_yaml} 의 redmine.enabled: true 로 바꾸고 "
            f"{config_path(target)} 에 접속 정보를 넣으세요.",
            file=sys.stderr,
        )
        sys.exit(1)


def config_path(target: str = "redmine") -> Path:
    return org_root() / "publish" / target / "config.yaml"


def state_dir() -> Path:
    d = org_root() / ".processware" / "publish"
    d.mkdir(parents=True, exist_ok=True)
    return d


def db_path(target: str = "redmine") -> Path:
    return state_dir() / f"{target}_sync.db"


def log_path(target: str = "redmine") -> Path:
    return state_dir() / f"{target}_sync.log"


def banner() -> str:
    c = ctx()
    return f"조직: {c.org_id} · vault: {c.vault} · prefix: {project_prefix()}"
