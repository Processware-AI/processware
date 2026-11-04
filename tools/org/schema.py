"""org.yaml 스키마 (org-layer.md §2 — 조직 루트 설정 파일)."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

ORG_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{1,31}$")

# .claude/rbac/policy.yaml 의 6 역할 (단계 4 에서 policy.yaml 을 직접 읽도록 교체 예정)
RBAC_ROLES = ("auditor", "executor", "process_owner", "qmr", "admin", "viewer")

REQUIRED_KEYS = ("org_id", "name")
KNOWN_KEYS = {
    "org_id", "name", "created", "platform_version",
    "scopes", "rbac", "redmine", "description",
}


def load_org_yaml(path: "Path | str") -> dict:
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: 최상위가 매핑이 아닙니다")
    return data


def _known_scopes() -> set:
    try:
        from tools.vault_rules.rules import SCOPE_CODES
        return set(SCOPE_CODES)
    except Exception:  # vault_rules 가 없는 환경 (조직 repo 단독 실행 등)
        return set()


def validate_org(data: dict) -> "tuple[list[str], list[str]]":
    """(errors, warnings) 를 돌려준다. errors 가 비어 있으면 유효."""
    errors: list = []
    warnings: list = []

    for k in REQUIRED_KEYS:
        if k not in data or data[k] in (None, ""):
            errors.append(f"필수 키 누락: {k}")

    oid = data.get("org_id")
    if oid is not None and not (isinstance(oid, str) and ORG_ID_RE.match(oid)):
        errors.append(f"org_id 형식 오류: {oid!r} (소문자·숫자·하이픈, 2~32자, 소문자/숫자로 시작)")

    name = data.get("name")
    if name is not None and not isinstance(name, str):
        errors.append("name 은 문자열이어야 합니다")

    scopes = data.get("scopes")
    if scopes is not None:
        if not isinstance(scopes, list) or not all(isinstance(s, str) for s in scopes):
            errors.append("scopes 는 문자열 목록이어야 합니다")
        else:
            known = _known_scopes()
            if known:
                for s in scopes:
                    if s not in known:
                        warnings.append(f"scopes: 레지스트리에 없는 영역코드 {s!r} (07_표준분류레지스트리 확인)")

    rbac = data.get("rbac")
    if rbac is not None:
        if not isinstance(rbac, dict):
            errors.append("rbac 는 매핑이어야 합니다")
        else:
            users = rbac.get("users") or {}
            if not isinstance(users, dict):
                errors.append("rbac.users 는 매핑(사용자 → 역할 목록)이어야 합니다")
            else:
                for user, roles in users.items():
                    if not isinstance(roles, list):
                        errors.append(f"rbac.users.{user}: 역할 목록이 아닙니다")
                        continue
                    for r in roles:
                        if r not in RBAC_ROLES:
                            errors.append(
                                f"rbac.users.{user}: 알 수 없는 역할 {r!r} (허용: {', '.join(RBAC_ROLES)})"
                            )

    redmine = data.get("redmine")
    if redmine is not None:
        if not isinstance(redmine, dict):
            errors.append("redmine 은 매핑이어야 합니다")
        elif "project_prefix" in redmine and not isinstance(redmine["project_prefix"], str):
            errors.append("redmine.project_prefix 는 문자열이어야 합니다")

    for k in data:
        if k not in KNOWN_KEYS:
            warnings.append(f"알 수 없는 키 {k!r} (무시됨)")

    return errors, warnings
