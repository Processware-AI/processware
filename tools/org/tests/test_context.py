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
from tools.org.sync import Manifest, sync_core, _glob_to_re

PLATFORM = Path(__file__).resolve().parents[3]
VAULT_BASE = PLATFORM / "core" / "vault_base"
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
        f"org_id: {org_id}\nname: \"{name}\"\nplatform_version: \"x\"\n{extra}", encoding="utf-8"
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
    def test_no_org_raises(self):
        with self.assertRaises(OrgContextError):
            resolve(cwd=PLATFORM)

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
        self.assertFalse(ctx.contains(PLATFORM / "core" / "x.md"))

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


class TestSync(EnvIsolation):
    def test_glob(self):
        self.assertTrue(_glob_to_re("00_공통관리/**").match("00_공통관리/a/b.md"))
        self.assertTrue(_glob_to_re("*/README.md").match("00_MOC/README.md"))
        self.assertFalse(_glob_to_re("*/README.md").match("a/b/README.md"))
        self.assertTrue(_glob_to_re("90_MAT_통합매핑/MAT-*.md").match("90_MAT_통합매핑/MAT-001_x.md"))
        self.assertTrue(_glob_to_re(".obsidian/**").match(".obsidian/app.json"))

    def test_manifest_covers_every_vault_base_file(self):
        m = Manifest.load(VAULT_BASE)
        missing = [
            p.relative_to(VAULT_BASE).as_posix()
            for p in VAULT_BASE.rglob("*")
            if p.is_file() and p.name != "_manifest.yaml"
            and m.classify(p.relative_to(VAULT_BASE).as_posix()) is None
        ]
        self.assertEqual(missing, [])
        self.assertEqual(m.classify("00_공통관리/01_문서체계.md"), "managed")
        self.assertEqual(m.classify("00_MOC/README.md"), "managed")
        self.assertEqual(m.classify("00_MOC/MOC_전체표준.md"), "seed")
        self.assertEqual(m.classify("90_MAT_통합매핑/MAT-001_문서관리대장.md"), "seed")
        self.assertEqual(m.classify("00_공통관리/07_표준분류레지스트리_조직추가.md"), "org")   # 조직 소유 예외
        self.assertEqual(m.classify("00_공통관리/07_표준분류레지스트리.md"), "managed")

    def test_sync_create_update_preserve(self):
        root = Path(self.tmp.name) / "acme"
        _write_org(root)
        ctx = resolve(org_root=root, cwd=PLATFORM)

        rep = sync_core(ctx)
        self.assertTrue(rep.ok, rep.unclassified)
        self.assertGreater(len(rep.created), 50)
        self.assertEqual(rep.updated, [])
        self.assertTrue((ctx.vault / "01_구성원칙" / "표준프로세스_구성원칙.md").is_file())
        self.assertTrue((ctx.vault / "90_MAT_통합매핑" / "MAT-001_문서관리대장.md").is_file())
        self.assertTrue((root / "inputs" / "README.md").is_file())       # org_base
        self.assertTrue((root / ".gitignore").is_file())
        self.assertTrue((root / ".processware" / "sync-core.yaml").is_file())
        self.assertNotIn('platform_version: "x"', (root / "org.yaml").read_text(encoding="utf-8"))

        # managed 는 덮어쓰고, seed 는 보존
        managed = ctx.vault / "01_구성원칙" / "표준프로세스_구성원칙.md"
        seed = ctx.vault / "90_MAT_통합매핑" / "MAT-001_문서관리대장.md"
        managed.write_text("tampered", encoding="utf-8")
        seed.write_text("org-owned", encoding="utf-8")
        rep2 = sync_core(ctx)
        self.assertIn("01_구성원칙/표준프로세스_구성원칙.md", rep2.updated)
        self.assertIn("90_MAT_통합매핑/MAT-001_문서관리대장.md", rep2.skipped_seed)
        self.assertNotEqual(managed.read_text(encoding="utf-8"), "tampered")
        self.assertEqual(seed.read_text(encoding="utf-8"), "org-owned")

        # --force 는 seed 도 재시드, dry-run 은 쓰지 않음
        rep3 = sync_core(ctx, dry_run=True, force=True)
        self.assertIn("90_MAT_통합매핑/MAT-001_문서관리대장.md", rep3.updated)
        self.assertEqual(seed.read_text(encoding="utf-8"), "org-owned")
        rep4 = sync_core(ctx, force=True)
        self.assertNotEqual(seed.read_text(encoding="utf-8"), "org-owned")
        self.assertEqual(len(rep4.updated), 1)


class TestCli(EnvIsolation):
    def _run(self, *argv, env=None, cwd=PLATFORM):
        e = _clean_env()
        e["PROCESSWARE_HOME"] = os.environ["PROCESSWARE_HOME"]
        if env:
            e.update(env)
        return subprocess.run(
            [PY, "-m", *argv], cwd=cwd, env=e, capture_output=True, text=True, encoding="utf-8"
        )

    def test_init_syncs_then_context_and_vault_rules(self):
        root = Path(self.tmp.name) / "acme"
        r = self._run("tools.org", "init", str(root), "--org-id", "acme", "--name", "ACME", "--register")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue((root / "org.yaml").is_file())
        self.assertTrue((root / ".processware" / "queues" / "process-act").is_dir())
        self.assertTrue((root / "vault" / "00_공통관리" / "01_문서체계.md").is_file())
        self.assertIn("sync-core", r.stdout)

        r = self._run("tools.org", "validate", "--org-root", str(root))
        self.assertEqual(r.returncode, 0, r.stderr)

        r = self._run("tools.org", "context", "--org", "acme")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("PROCESSWARE_ORG_ID=acme", r.stdout)
        self.assertIn(f"PROCESSWARE_VAULT={root.resolve() / 'vault'}", r.stdout)

        r = self._run("tools.org", "sync-core", "--org-root", str(root), "--dry-run")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("[dry-run]", r.stdout)

        # vault_rules 가 조직 vault 를 기본 루트로 쓰는지 (REC 폴더 + MAT 다음 번호)
        env = {"PROCESSWARE_ORG_ROOT": str(root)}
        r = self._run("tools.vault_rules", "folder", "--type", "POL", env=env)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(r.stdout.strip().startswith(str(root.resolve())), r.stdout)
        r = self._run("tools.vault_rules", "next-id", "--type", "MAT", env=env)
        self.assertTrue(r.stdout.strip().startswith("MAT-0"), r.stdout + r.stderr)

        r = self._run("tools.org", "list")
        self.assertIn("acme", r.stdout)

    def test_no_org_fails_clearly(self):
        r = self._run("tools.org", "context")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("PROCESSWARE_ORG_ROOT", r.stderr)
        r = self._run("tools.vault_rules", "folder", "--type", "POL")
        self.assertNotEqual(r.returncode, 0)

    def test_context_bad_root_fails(self):
        r = self._run("tools.org", "context", "--org-root", str(Path(self.tmp.name) / "nope"))
        self.assertNotEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
