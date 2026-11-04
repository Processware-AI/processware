"""org.yaml 스키마 (org-layer.md §2 — 조직 루트 설정 파일)."""

from __future__ import annotations

import datetime as _dt
import re
from pathlib import Path
from typing import Any

import yaml

ORG_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{1,31}$")

# 플랫폼 .claude/rbac/policy.yaml 의 6 역할 (정의는 플랫폼, 배정은 조직)
RBAC_ROLES = ("auditor", "executor", "process_owner", "qmr", "admin", "viewer")

REQUIRED_KEYS = ("org_id", "name")
KNOWN_KEYS = {
    "org_id", "name", "created", "platform_version",
    "scopes", "rbac", "redmine", "description",
}
RBAC_KEYS = {"enforce", "users", "delegations", "audit_log"}


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


def _check_roles(where: str, roles, errors: list):
    if not isinstance(roles, list):
        errors.append(f"{where}: 역할 목록이 아닙니다")
        return
    for r in roles:
        if r not in RBAC_ROLES:
            errors.append(f"{where}: 알 수 없는 역할 {r!r} (허용: {', '.join(RBAC_ROLES)})")


def _validate_rbac(rbac: Any, errors: list, warnings: list):
    if not isinstance(rbac, dict):
        errors.append("rbac 는 매핑이어야 합니다")
        return
    for k in rbac:
        if k not in RBAC_KEYS:
            warnings.append(f"rbac: 알 수 없는 키 {k!r} (무시됨)")

    enforce = rbac.get("enforce", True)
    if not isinstance(enforce, bool):
        errors.append("rbac.enforce 는 true/false 여야 합니다")

    users = rbac.get("users") or {}
    if not isinstance(users, dict):
        errors.append("rbac.users 는 매핑(사용자 → 역할 목록 또는 {roles, aliases, owns_pro})이어야 합니다")
        users = {}
    else:
        for user, spec in users.items():
            where = f"rbac.users.{user}"
            if isinstance(spec, list):
                _check_roles(where, spec, errors)
            elif isinstance(spec, dict):
                for k in spec:
                    if k not in ("roles", "aliases", "owns_pro"):
                        warnings.append(f"{where}: 알 수 없는 키 {k!r} (무시됨)")
                _check_roles(f"{where}.roles", spec.get("roles") or [], errors)
                for k in ("aliases", "owns_pro"):
                    v = spec.get(k)
                    if v is not None and not (isinstance(v, list) and all(isinstance(x, str) for x in v)):
                        errors.append(f"{where}.{k}: 문자열 목록이어야 합니다")
            else:
                errors.append(f"{where}: 역할 목록 또는 매핑이어야 합니다")

    if enforce is True and not users:
        warnings.append("rbac.enforce: true 인데 users 가 비어 있음 — 모든 작업이 거부됩니다")

    dels = rbac.get("delegations")
    if dels is not None:
        if not isinstance(dels, list):
            errors.append("rbac.delegations 는 목록이어야 합니다")
        else:
            for i, d in enumerate(dels):
                where = f"rbac.delegations[{i}]"
                if not isinstance(d, dict):
                    errors.append(f"{where}: 매핑이어야 합니다")
                    continue
                for k in ("from", "to"):
                    if not d.get(k):
                        errors.append(f"{where}.{k}: 필수")
                _check_roles(f"{where}.roles", d.get("roles") or [], errors)
                if not d.get("roles"):
                    errors.append(f"{where}.roles: 비어 있음")
                until = d.get("until")
                if isinstance(until, str):
                    try:
                        _dt.date.fromisoformat(until)
                    except ValueError:
                        errors.append(f"{where}.until: YYYY-MM-DD 형식이어야 합니다")
                elif until is not None and not isinstance(until, (_dt.date, _dt.datetime)):
                    errors.append(f"{where}.until: 날짜여야 합니다")
                to = d.get("to")
                if to and isinstance(users, dict) and to not in users:
                    warnings.append(f"{where}.to: '{to}' 가 rbac.users 에 없음 (위임 수신자도 사용자로 등록 권장)")

    al = rbac.get("audit_log")
    if al is not None and not isinstance(al, str):
        errors.append("rbac.audit_log 는 경로 문자열이어야 합니다")


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

    if data.get("rbac") is not None:
        _validate_rbac(data["rbac"], errors, warnings)

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
