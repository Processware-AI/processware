"""RBAC — 역할 정의는 플랫폼, 사용자 배정은 조직 (org-layer.md §3 단계 4).

플랫폼 `.claude/rbac/policy.yaml`  : roles[].allow / deny / target_constraints (조직 공통, 읽기 전용)
조직   `org.yaml` → rbac             : enforce · users{name: roles|{roles,aliases,owns_pro}} · delegations[]
조직   `.processware/rbac_audit.jsonl`: 거부 · 민감 작업 허용 · 독립성 판정 로그 (append-only)

판정은 결정론적이다 — 문자열 · glob 매칭만 쓰고 추론하지 않는다.
"""

from __future__ import annotations

import datetime as _dt
import fnmatch
import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional

import yaml

from .context import OrgContext
from .schema import RBAC_ROLES, load_org_yaml

POLICY_PATH = ".claude/rbac/policy.yaml"
AUDIT_LOG = ".processware/rbac_audit.jsonl"

# 허용돼도 로그를 남기는 민감 작업 (policy.yaml extensions.audit_log.events_logged 와 동형)
SENSITIVE_ACTIONS = (
    "audit.confirm", "audit.close-ncr", "audit.act-queue.dispatch",
    "act.start", "act.approve", "act.reject", "act.trigger-rebuild",
    "build-process.start", "rbac.*",
)


class RbacError(Exception):
    pass


# ── 모델 ──────────────────────────────────────────────────────────────────

@dataclass
class User:
    name: str
    roles: list
    aliases: list = field(default_factory=list)
    owns_pro: list = field(default_factory=list)


@dataclass
class Delegation:
    from_user: str
    to_user: str
    roles: list
    until: Optional[_dt.date] = None
    reason: str = ""

    def active(self, today: _dt.date) -> bool:
        return self.until is None or today <= self.until


@dataclass
class Decision:
    verdict: str                      # allowed | denied | unknown_user | bypass_disabled
    user: str
    action: str
    canonical_user: Optional[str] = None
    target: Optional[str] = None
    roles: list = field(default_factory=list)          # 유효 역할 (위임 포함) — "role" 또는 "role (delegated from X)"
    matched_rule: Optional[str] = None
    denied_reason: Optional[str] = None
    requires_independence: bool = False
    checked_at: str = ""

    @property
    def ok(self) -> bool:
        return self.verdict in ("allowed", "bypass_disabled")

    def as_dict(self) -> dict:
        return asdict(self)


@dataclass
class IndependenceResult:
    verdict: str                      # passed | failed
    auditor: str
    canonical_auditor: Optional[str]
    violations: list                  # 이행자 이름 중 심사원과 동일인으로 판정된 것
    checked: int
    checked_at: str = ""

    def as_dict(self) -> dict:
        return asdict(self)


# ── 로드 ──────────────────────────────────────────────────────────────────

def load_policy(platform_root: Path) -> dict:
    p = platform_root / POLICY_PATH
    if not p.is_file():
        raise RbacError(f"플랫폼 RBAC 정책 없음: {p}")
    with open(p, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    roles = data.get("roles") or {}
    if not isinstance(roles, dict) or not roles:
        raise RbacError(f"{p}: roles 가 비어 있습니다")
    return data


def normalize_users(raw: dict) -> dict:
    """org.yaml rbac.users → {name: User}. 값은 역할 목록(단축) 또는 {roles, aliases, owns_pro}."""
    users: dict = {}
    for name, spec in (raw or {}).items():
        name = str(name)
        if isinstance(spec, list):
            users[name] = User(name=name, roles=[str(r) for r in spec])
        elif isinstance(spec, dict):
            users[name] = User(
                name=name,
                roles=[str(r) for r in (spec.get("roles") or [])],
                aliases=[str(a) for a in (spec.get("aliases") or [])],
                owns_pro=[str(p) for p in (spec.get("owns_pro") or [])],
            )
        else:
            raise RbacError(f"rbac.users.{name}: 역할 목록 또는 매핑이어야 합니다")
    return users


def normalize_delegations(raw: list) -> list:
    out = []
    for i, d in enumerate(raw or []):
        if not isinstance(d, dict):
            raise RbacError(f"rbac.delegations[{i}]: 매핑이어야 합니다")
        until = d.get("until")
        if isinstance(until, _dt.datetime):
            until = until.date()
        elif isinstance(until, str):
            until = _dt.date.fromisoformat(until)
        elif until is not None and not isinstance(until, _dt.date):
            raise RbacError(f"rbac.delegations[{i}].until: 날짜(YYYY-MM-DD)여야 합니다")
        out.append(Delegation(
            from_user=str(d.get("from", "")),
            to_user=str(d.get("to", "")),
            roles=[str(r) for r in (d.get("roles") or [])],
            until=until,
            reason=str(d.get("reason", "")),
        ))
    return out


def _norm(name: str) -> str:
    return " ".join(str(name).split()).strip().lower()


def _match(pattern: str, action: str) -> bool:
    return fnmatch.fnmatchcase(action, str(pattern))


def _now() -> str:
    return _dt.datetime.now().astimezone().isoformat(timespec="seconds")


# ── 엔진 ──────────────────────────────────────────────────────────────────

class Rbac:
    def __init__(self, ctx: OrgContext, today: Optional[_dt.date] = None):
        self.ctx = ctx
        self.policy = load_policy(ctx.platform_root)
        self.roles_def: dict = self.policy["roles"]
        data = load_org_yaml(ctx.org_yaml)
        rb = data.get("rbac") or {}
        self.enforce = bool(rb.get("enforce", True))
        self.users = normalize_users(rb.get("users") or {})
        self.delegations = normalize_delegations(rb.get("delegations") or [])
        self.today = today or _dt.date.today()
        self.audit_log = ctx.org_root / str(rb.get("audit_log") or AUDIT_LOG)

    # ── 사용자 ──
    def resolve_user(self, name: str) -> Optional[User]:
        key = _norm(name)
        for u in self.users.values():
            if _norm(u.name) == key or any(_norm(a) == key for a in u.aliases):
                return u
        return None

    def same_person(self, a: str, b: str) -> bool:
        ua, ub = self.resolve_user(a), self.resolve_user(b)
        if ua and ub:
            return ua.name == ub.name
        return _norm(a) == _norm(b)

    def effective_roles(self, user: User) -> list:
        """[(role, source)] — 본인 역할 + 활성 위임."""
        out = [(r, "own") for r in user.roles]
        for d in self.delegations:
            if not d.active(self.today):
                continue
            if self.same_person(d.to_user, user.name):
                for r in d.roles:
                    if r not in [x for x, _ in out]:
                        out.append((r, f"delegated from {d.from_user}"))
        return out

    # ── 권한 판정 ──
    def check(self, name: str, action: str, target: Optional[str] = None, log: bool = True) -> Decision:
        dec = Decision(verdict="denied", user=name, action=action, target=target, checked_at=_now())
        user = self.resolve_user(name)

        if user is None:
            if self.enforce:
                dec.verdict = "unknown_user"
                dec.denied_reason = (
                    f"'{name}' 은 org.yaml rbac.users 에 없습니다 (enforce: true). "
                    "admin 이 org.yaml 에 사용자와 역할을 등록해야 합니다."
                )
            else:
                dec.verdict = "bypass_disabled"
                dec.matched_rule = "org.yaml rbac.enforce: false"
            self._log(dec, log)
            return dec

        dec.canonical_user = user.name
        eff = self.effective_roles(user)
        dec.roles = [r if src == "own" else f"{r} ({src})" for r, src in eff]
        if not self.enforce:
            dec.verdict = "bypass_disabled"
            dec.matched_rule = "org.yaml rbac.enforce: false"
            self._log(dec, log)
            return dec

        denies: list = []
        for role, _src in eff:
            rdef = self.roles_def.get(role)
            if not rdef:
                denies.append(f"{role}: 플랫폼 policy.yaml 에 정의되지 않은 역할")
                continue
            deny_hit = next((p for p in (rdef.get("deny") or []) if _match(p, action)), None)
            if deny_hit is not None:
                denies.append(f"{role}.deny = {deny_hit}")
                continue
            allow_hit = next((p for p in (rdef.get("allow") or []) if _match(p, action)), None)
            if allow_hit is None:
                continue
            # target 제약
            tc = rdef.get("target_constraints") or {}
            if tc.get("owns_pro_required") and target and str(target).startswith("PRO-"):
                if target not in user.owns_pro:
                    denies.append(f"{role}.target_constraints.owns_pro_required — {target} 은 {user.name} 의 owns_pro 에 없음")
                    continue
            dec.verdict = "allowed"
            dec.matched_rule = f"{role}.allow = {allow_hit}"
            dec.requires_independence = bool(tc.get("independence_required"))
            break

        if dec.verdict != "allowed":
            dec.denied_reason = (
                "; ".join(denies) if denies
                else f"역할 {[r for r, _ in eff]} 의 allow 에 '{action}' 과 일치하는 규칙 없음 (거부가 기본)"
            )
        self._log(dec, log)
        return dec

    def allowed_actions(self, name: str) -> list:
        user = self.resolve_user(name)
        if not user:
            return []
        pats = []
        for role, _ in self.effective_roles(user):
            pats += [str(p) for p in (self.roles_def.get(role, {}).get("allow") or [])]
        return sorted(set(pats))

    # ── 독립성 (ISO §9.2) ──
    def independence(self, auditor: str, executors: list, log: bool = True) -> IndependenceResult:
        ua = self.resolve_user(auditor)
        violations = [e for e in executors if self.same_person(auditor, e)]
        res = IndependenceResult(
            verdict="failed" if violations else "passed",
            auditor=auditor,
            canonical_auditor=ua.name if ua else None,
            violations=violations,
            checked=len(executors),
            checked_at=_now(),
        )
        if log:
            self._append({
                "ts": res.checked_at,
                "event": "independence_passed" if not violations else "independence_failed",
                "auditor": auditor, "canonical_auditor": res.canonical_auditor,
                "checked": len(executors), "violations": violations,
            })
        return res

    # ── 로그 ──
    def _log(self, dec: Decision, enabled: bool):
        if not enabled:
            return
        if dec.verdict in ("denied", "unknown_user"):
            event = "rbac_denied"
        elif dec.verdict == "bypass_disabled":
            event = "rbac_bypass"
        elif any(_match(p, dec.action) for p in SENSITIVE_ACTIONS):
            event = "rbac_allowed"
        else:
            return
        self._append({
            "ts": dec.checked_at, "event": event,
            "user": dec.user, "canonical_user": dec.canonical_user,
            "action": dec.action, "target": dec.target,
            "verdict": dec.verdict, "roles": dec.roles,
            "matched_rule": dec.matched_rule, "denied_reason": dec.denied_reason,
        })

    def _append(self, record: dict):
        self.audit_log.parent.mkdir(parents=True, exist_ok=True)
        with open(self.audit_log, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def read_log(self, limit: int = 50, event: Optional[str] = None) -> list:
        if not self.audit_log.is_file():
            return []
        rows = []
        with open(self.audit_log, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if event and rec.get("event") != event:
                    continue
                rows.append(rec)
        return rows[-limit:]
