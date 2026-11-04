"""python -m unittest tools.org.tests.test_context  (pytest 불필요)"""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.org import OrgContextError, resolve, find_platform_root
from tools.org import registry
from tools.org.schema import validate_org

PLATFORM = Path(__file__).resolve().parents[3]
PY = sys.executable

ORG_ENV_KEYS = ("PROCESSWARE_ORG_ROOT", "PROCESSWARE_ORG", "PROCESSWARE_HOME", "PROCESSWARE_PLATFORM_ROOT")


def _clean_env():
    env = dict(os.environ)
    for k in ORG_ENV_KEYS:
        env.pop(k, None)
    return env


def _write_org(root: Path, org_id="acme", name="ACME Corp", extra=""):
    root.mkdir(parents=True, exist_ok=True)
    (root / "org.yaml").write_text(
        f"org_id: {org_id}\nname: \"{name}\"\n{extra}", encoding="utf-8"
    )


class EnvIsolation(unittest.TestCase):
    def setUp(self):
        self._saved = {k: os.environ.pop(k, None) for k in ORG_ENV_KEYS}
        self.tmp = tempfile.TemporaryDirectory()
        os.environ["PROCESSWARE_HOME"] = str(Path(self.tmp.name) / "home")

    def tearDown(self):
        for k in ORG_ENV_KEYS:
            os.environ.pop(k, None)
        for k, v in self._saved.items():
            if v is not None:
                os.environ[k] = v
        self.tmp.cleanup()


class TestResolve(EnvIsolation):
    def test_fallback_default_uses_platform_vault(self):
        ctx = resolve(cwd=PLATFORM)
        self.assertEqual(ctx.mode, "default")
        self.assertEqual(ctx.org_id, "default")
        self.assertEqual(ctx.vault, PLATFORM / "vault")
        self.assertEqual(ctx.runs, PLATFORM / ".claude" / "runs")
        self.assertIsNone(ctx.org_yaml)

    def test_allow_default_false_raises(self):
        with self.assertRaises(OrgContextError):
            resolve(cwd=PLATFORM, allow_default=False)

    def test_org_root_arg(self):
        root = Path(self.tmp.name) / "acme"
        _write_org(root)
        ctx = resolve(org_root=root, cwd=PLATFORM)
        self.assertEqual(ctx.mode, "org")
        self.assertEqual(ctx.org_id, "acme")
        self.assertEqual(ctx.source, "arg:org-root")
        self.assertEqual(ctx.vault, root.resolve() / "vault")
        self.assertEqual(ctx.runs, root.resolve() / ".processware" / "runs")
        self.assertEqual(ctx.queues, root.resolve() / ".processware" / "queues")
        self.assertEqual(ctx.platform_root, PLATFORM)

    def test_env_org_root(self):
        root = Path(self.tmp.name) / "acme"
        _write_org(root)
        os.environ["PROCESSWARE_ORG_ROOT"] = str(root)
        ctx = resolve(cwd=PLATFORM)
        self.assertEqual(ctx.source, "env:PROCESSWARE_ORG_ROOT")
        self.assertEqual(ctx.org_id, "acme")

    def test_missing_org_yaml(self):
        root = Path(self.tmp.name) / "empty"
        root.mkdir()
        with self.assertRaises(OrgContextError):
            resolve(org_root=root, cwd=PLATFORM)

    def test_invalid_org_id_strict(self):
        root = Path(self.tmp.name) / "bad"
        _write_org(root, org_id="Bad_ID")
        with self.assertRaises(OrgContextError):
            resolve(org_root=root, cwd=PLATFORM)
        ctx = resolve(org_root=root, cwd=PLATFORM, strict=False)
        self.assertEqual(ctx.org_id, "Bad_ID")

    def test_registry_and_org_arg(self):
        root = Path(self.tmp.name) / "acme"
        _write_org(root)
        oid, _ = registry.register(root)
        self.assertEqual(oid, "acme")
        ctx = resolve(org="acme", cwd=PLATFORM)
        self.assertEqual(ctx.source, "arg:org")
        os.environ["PROCESSWARE_ORG"] = "acme"
        self.assertEqual(resolve(cwd=PLATFORM).source, "env:PROCESSWARE_ORG")
        with self.assertRaises(OrgContextError):
            resolve(org="nope", cwd=PLATFORM)
        self.assertTrue(registry.unregister("acme"))
        self.assertFalse(registry.unregister("acme"))

    def test_contains(self):
        root = Path(self.tmp.name) / "acme"
        _write_org(root)
        ctx = resolve(org_root=root, cwd=PLATFORM)
        self.assertTrue(ctx.contains(root / "vault" / "x.md"))
        self.assertFalse(ctx.contains(PLATFORM / "vault" / "x.md"))

    def test_find_platform_root(self):
        self.assertEqual(find_platform_root(PLATFORM / "tools" / "org"), PLATFORM)


class TestSchema(unittest.TestCase):
    def test_valid(self):
        errors, warnings = validate_org({"org_id": "acme", "name": "A", "scopes": ["QMS"]})
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_errors(self):
        errors, _ = validate_org({"org_id": "A B", "rbac": {"users": {"x": ["king"]}}})
        self.assertTrue(any("필수 키 누락: name" in e for e in errors))
        self.assertTrue(any("org_id 형식 오류" in e for e in errors))
        self.assertTrue(any("알 수 없는 역할" in e for e in errors))

    def test_warnings(self):
        _, warnings = validate_org({"org_id": "acme", "name": "A", "scopes": ["ZZZ"], "foo": 1})
        self.assertTrue(any("ZZZ" in w for w in warnings))
        self.assertTrue(any("foo" in w for w in warnings))


class TestCli(EnvIsolation):
    def _run(self, *argv, env=None, cwd=PLATFORM):
        e = _clean_env()
        e["PROCESSWARE_HOME"] = os.environ["PROCESSWARE_HOME"]
        if env:
            e.update(env)
        return subprocess.run(
            [PY, "-m", *argv], cwd=cwd, env=e, capture_output=True, text=True, encoding="utf-8"
        )

    def test_init_then_context_and_vault_rules(self):
        root = Path(self.tmp.name) / "acme"
        r = self._run("tools.org", "init", str(root), "--org-id", "acme", "--name", "ACME", "--register")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue((root / "org.yaml").is_file())
        self.assertTrue((root / ".processware" / "queues" / "process-act").is_dir())

        r = self._run("tools.org", "validate", "--org-root", str(root))
        self.assertEqual(r.returncode, 0, r.stderr)

        r = self._run("tools.org", "context", "--org", "acme")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("PROCESSWARE_ORG_ID=acme", r.stdout)
        self.assertIn(f"PROCESSWARE_VAULT={root.resolve() / 'vault'}", r.stdout)

        # vault_rules 가 조직 vault 를 기본 루트로 쓰는지
        r = self._run("tools.vault_rules", "folder", "--type", "POL",
                      env={"PROCESSWARE_ORG_ROOT": str(root)})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(r.stdout.strip().startswith(str(root.resolve())), r.stdout)

        r = self._run("tools.org", "list")
        self.assertIn("acme", r.stdout)

    def test_context_default_warns(self):
        r = self._run("tools.org", "context")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("PROCESSWARE_ORG_MODE=default", r.stdout)
        self.assertIn("fallback", r.stderr)

    def test_context_bad_root_fails(self):
        r = self._run("tools.org", "context", "--org-root", str(Path(self.tmp.name) / "nope"))
        self.assertNotEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
