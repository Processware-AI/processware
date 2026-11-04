"""python -m unittest tools.org.tests.test_rbac"""

import datetime as dt
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.org import resolve
from tools.org.rbac import Rbac, RbacError
from tools.org.schema import validate_org

PLATFORM = Path(__file__).resolve().parents[3]
PY = sys.executable
ORG_ENV_KEYS = ("PROCESSWARE_ORG_ROOT", "PROCESSWARE_ORG", "PROCESSWARE_HOME", "PROCESSWARE_PLATFORM_ROOT")

ORG_YAML = """org_id: acme
name: "ACME"
rbac:
  enforce: true
  users:
    "이감사": [auditor]
    "dongseok": [executor]
    "박팀장": { roles: [process_owner], aliases: ["박 팀장"], owns_pro: ["PRO-QMS-01"] }
    "박상무": [qmr]
    "root": [admin]
    "guest": [viewer]
    "김대리": [executor]
  delegations:
    - { from: "박팀장", to: "김대리", roles: [process_owner], until: 2099-12-31, reason: "휴가" }
    - { from: "박상무", to: "guest", roles: [qmr], until: 2000-01-01, reason: "만료됨" }
"""


class Base(unittest.TestCase):
    def setUp(self):
        self._saved = {k: os.environ.pop(k, None) for k in ORG_ENV_KEYS}
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "acme"
        self.root.mkdir()
        (self.root / "org.yaml").write_text(ORG_YAML, encoding="utf-8")
        self.ctx = resolve(org_root=self.root, cwd=PLATFORM)
        self.rbac = Rbac(self.ctx, today=dt.date(2026, 11, 5))

    def tearDown(self):
        for k in ORG_ENV_KEYS:
            os.environ.pop(k, None)
        for k, v in self._saved.items():
            if v is not None:
                os.environ[k] = v
        self.tmp.cleanup()


class TestCheck(Base):
    def test_allow_and_independence_flag(self):
        d = self.rbac.check("이감사", "audit.start", "PRO-QMS-01")
        self.assertEqual(d.verdict, "allowed")
        self.assertTrue(d.requires_independence)
        self.assertEqual(d.matched_rule, "auditor.allow = audit.start")

    def test_explicit_deny(self):
        d = self.rbac.check("이감사", "do.start")
        self.assertEqual(d.verdict, "denied")
        self.assertIn("auditor.deny", d.denied_reason)

    def test_default_deny(self):
        d = self.rbac.check("dongseok", "audit.confirm")
        self.assertEqual(d.verdict, "denied")

    def test_glob_rules(self):
        self.assertEqual(self.rbac.check("박상무", "audit.kpi.start").verdict, "allowed")   # audit.*
        self.assertEqual(self.rbac.check("root", "rbac.write").verdict, "allowed")          # *
        self.assertEqual(self.rbac.check("guest", "audit.start").verdict, "denied")         # *.start deny
        self.assertEqual(self.rbac.check("guest", "do.read").verdict, "allowed")

    def test_owns_pro_constraint(self):
        self.assertEqual(self.rbac.check("박팀장", "act.start", "PRO-QMS-01").verdict, "allowed")
        d = self.rbac.check("박팀장", "act.start", "PRO-QMS-02")
        self.assertEqual(d.verdict, "denied")
        self.assertIn("owns_pro", d.denied_reason)
        # PRO 가 아닌 target 은 제약 미적용
        self.assertEqual(self.rbac.check("박팀장", "audit.close-ncr", "REC-NCR-01-01-2026-001").verdict, "allowed")

    def test_alias(self):
        d = self.rbac.check("박 팀장", "act.list")
        self.assertEqual(d.verdict, "allowed")
        self.assertEqual(d.canonical_user, "박팀장")

    def test_delegation_active_and_expired(self):
        d = self.rbac.check("김대리", "audit.close-ncr")
        self.assertEqual(d.verdict, "allowed")
        self.assertTrue(any("delegated from 박팀장" in r for r in d.roles))
        # 위임받은 process_owner 의 owns_pro 는 수신자 기준 (김대리 owns_pro 없음 → PRO target 거부)
        self.assertEqual(self.rbac.check("김대리", "act.start", "PRO-QMS-01").verdict, "denied")
        # 만료된 위임은 무시
        self.assertEqual(self.rbac.check("guest", "audit.confirm").verdict, "denied")
        # 날짜를 과거로 돌리면 만료 위임이 살아남
        past = Rbac(self.ctx, today=dt.date(1999, 1, 1))
        self.assertEqual(past.check("guest", "audit.confirm").verdict, "allowed")

    def test_unknown_user_and_enforce_false(self):
        d = self.rbac.check("nobody", "do.read")
        self.assertEqual(d.verdict, "unknown_user")
        self.assertFalse(d.ok)
        (self.root / "org.yaml").write_text(ORG_YAML.replace("enforce: true", "enforce: false"), encoding="utf-8")
        r2 = Rbac(self.ctx)
        d2 = r2.check("nobody", "audit.confirm")
        self.assertEqual(d2.verdict, "bypass_disabled")
        self.assertTrue(d2.ok)

    def test_independence(self):
        res = self.rbac.independence("이감사", ["dongseok", "박팀장"])
        self.assertEqual(res.verdict, "passed")
        res = self.rbac.independence("박 팀장", ["dongseok", "박팀장"])
        self.assertEqual(res.verdict, "failed")
        self.assertEqual(res.violations, ["박팀장"])
        self.assertEqual(res.canonical_auditor, "박팀장")
        # 미등록 이름끼리는 정규화 문자열 비교
        self.assertEqual(self.rbac.independence("Kim", ["kim ", "lee"]).violations, ["kim "])

    def test_audit_log(self):
        self.rbac.check("dongseok", "audit.confirm")          # denied → 기록
        self.rbac.check("박상무", "audit.confirm")            # 민감 allowed → 기록
        self.rbac.check("dongseok", "do.read")               # 일반 allowed → 기록 안 함
        self.rbac.independence("이감사", ["dongseok"])
        log = self.ctx.org_root / ".processware" / "rbac_audit.jsonl"
        rows = [json.loads(l) for l in log.read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertEqual([r["event"] for r in rows], ["rbac_denied", "rbac_allowed", "independence_passed"])
        self.assertEqual(len(self.rbac.read_log(event="rbac_denied")), 1)

    def test_allowed_actions(self):
        self.assertIn("audit.start", self.rbac.allowed_actions("이감사"))
        self.assertEqual(self.rbac.allowed_actions("nobody"), [])


class TestSchemaRbac(unittest.TestCase):
    def test_valid_shapes(self):
        import yaml
        errors, warnings = validate_org(yaml.safe_load(ORG_YAML))
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_errors(self):
        errors, warnings = validate_org({
            "org_id": "acme", "name": "A",
            "rbac": {"enforce": "yes", "users": {"x": {"roles": ["king"], "owns_pro": "PRO-1"}},
                     "delegations": [{"from": "a", "roles": [], "until": "2026-13-01"}]},
        })
        joined = " | ".join(errors)
        for frag in ("rbac.enforce", "알 수 없는 역할", "owns_pro", "delegations[0].to", "roles: 비어", "until"):
            self.assertIn(frag, joined, joined)

    def test_enforce_without_users_warns(self):
        _, warnings = validate_org({"org_id": "acme", "name": "A", "rbac": {"enforce": True, "users": {}}})
        self.assertTrue(any("users 가 비어" in w for w in warnings))


class TestCli(Base):
    def _run(self, *argv):
        env = dict(os.environ)
        for k in ORG_ENV_KEYS:
            env.pop(k, None)
        env["PROCESSWARE_ORG_ROOT"] = str(self.root)
        env["PROCESSWARE_HOME"] = str(Path(self.tmp.name) / "home")
        return subprocess.run([PY, "-m", "tools.org", *argv], cwd=PLATFORM, env=env,
                              capture_output=True, text=True, encoding="utf-8")

    def test_check_json_and_exit_codes(self):
        r = self._run("rbac", "check", "--user", "이감사", "--action", "audit.start", "--target", "PRO-QMS-01", "--format", "json")
        self.assertEqual(r.returncode, 0, r.stderr)
        d = json.loads(r.stdout)
        self.assertEqual(d["verdict"], "allowed")
        self.assertTrue(d["requires_independence"])

        r = self._run("rbac", "check", "--user", "dongseok", "--action", "audit.confirm", "--format", "json")
        self.assertEqual(r.returncode, 2)
        self.assertEqual(json.loads(r.stdout)["verdict"], "denied")

        r = self._run("rbac", "independence", "--auditor", "박 팀장", "--executors", "dongseok,박팀장", "--format", "json")
        self.assertEqual(r.returncode, 2)
        self.assertEqual(json.loads(r.stdout)["violations"], ["박팀장"])

        r = self._run("rbac", "roles", "--user", "김대리")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("process_owner", r.stdout)

        r = self._run("rbac", "users")
        self.assertIn("이감사", r.stdout)

        r = self._run("rbac", "log", "--limit", "5")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("rbac_denied", r.stdout)


if __name__ == "__main__":
    unittest.main()
