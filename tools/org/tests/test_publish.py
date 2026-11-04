"""python -m unittest tools.org.tests.test_publish  (python-frontmatter · requests · PyYAML 필요)"""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.org import resolve
from tools.org.sync import sync_core

PLATFORM = Path(__file__).resolve().parents[3]
PUBLISH = PLATFORM / "publish"
PY = sys.executable
ORG_ENV_KEYS = ("PROCESSWARE_ORG_ROOT", "PROCESSWARE_ORG", "PROCESSWARE_HOME", "PROCESSWARE_PLATFORM_ROOT")

PRO_DOC = """---
type: PRO
doc_id: PRO-QMS-01-01
title: 문서관리 절차
version: "1.0"
status: final
scope_code: QMS
standards: [QMS]
---
# PRO-QMS-01-01 문서관리 절차
본문 [[WI-QMS-01-01-01_문서등록]]
"""

try:
    import frontmatter, requests  # noqa: F401
    DEPS = True
except ImportError:
    DEPS = False


@unittest.skipUnless(DEPS, "python-frontmatter / requests 미설치")
class Base(unittest.TestCase):
    def setUp(self):
        self._saved = {k: os.environ.pop(k, None) for k in ORG_ENV_KEYS}
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "acme"
        self.root.mkdir()
        (self.root / "org.yaml").write_text(
            'org_id: acme\nname: "ACME"\nredmine:\n  enabled: false\n  project_prefix: acme\n', encoding="utf-8")
        ctx = resolve(org_root=self.root, cwd=PLATFORM)
        sync_core(ctx)
        pro = self.root / "vault" / "04_PRO_절차" / "PRO-QMS-01-01_문서관리_절차_v1.0.md"
        pro.write_text(PRO_DOC, encoding="utf-8")
        os.environ["PROCESSWARE_ORG_ROOT"] = str(self.root)
        os.environ["PROCESSWARE_HOME"] = str(Path(self.tmp.name) / "home")
        # publish 모듈 로드 (조직 컨텍스트 캐시 초기화)
        for p in (str(PUBLISH), str(PUBLISH / "redmine")):
            if p not in sys.path:
                sys.path.insert(0, p)
        import orgctx
        orgctx._ctx = None
        orgctx._org = None
        self.orgctx = orgctx

    def tearDown(self):
        for k in ORG_ENV_KEYS:
            os.environ.pop(k, None)
        for k, v in self._saved.items():
            if v is not None:
                os.environ[k] = v
        self.orgctx._ctx = None
        self.orgctx._org = None
        self.tmp.cleanup()

    def _env(self):
        env = dict(os.environ)
        env["PROCESSWARE_ORG_ROOT"] = str(self.root)
        return env


class TestOrgCtx(Base):
    def test_paths_and_prefix(self):
        oc = self.orgctx
        self.assertEqual(oc.org_id(), "acme")
        self.assertEqual(oc.project_prefix(), "acme")
        self.assertFalse(oc.redmine_enabled())
        self.assertEqual(oc.vault_root(), self.root.resolve() / "vault")
        self.assertTrue(oc.config_path("redmine").is_file())          # core/org_base 에서 시드됨
        self.assertEqual(oc.db_path("redmine"), self.root.resolve() / ".processware" / "publish" / "redmine_sync.db")

    def test_identifiers(self):
        import library_setup, workspace
        cfg = {"project_mapping": {"by_scope_code": {}, "by_pro": {}}}
        self.assertEqual(library_setup.build_project_identifier("QMS", "PRO-QMS-01-01"), "lib-acme-qms-p01-01")
        self.assertEqual(library_setup.parent_identifier_for("QMS", cfg), "lib-acme-qms")
        cfg["project_mapping"]["by_scope_code"]["QMS"] = "lib-acme-quality"
        self.assertEqual(library_setup.parent_identifier_for("QMS", cfg), "lib-acme-quality")
        self.assertEqual(workspace._pro_slug_from_identifier("lib-acme-qms-p01-01"), "qms-p01-01")
        self.assertEqual(workspace._pro_slug_from_identifier("lib-qms-p01-01"), "qms-p01-01")
        self.assertEqual(workspace._ws_identifier("alpha"), "ws-acme-alpha")
        for arg in ("ws-acme-alpha", "ws-alpha", "alpha"):
            self.assertEqual(workspace._ws_slug(arg), "alpha")

    def test_collect_and_dry_run_sync(self):
        import sync as redmine_sync
        import db
        db.init_db()
        self.assertTrue((self.root / ".processware" / "publish" / "redmine_sync.db").is_file())
        files = redmine_sync.collect_vault_files()
        names = [f.name for f in files]
        self.assertIn("PRO-QMS-01-01_문서관리_절차_v1.0.md", names)
        self.assertFalse(any(n == "README.md" for n in names))
        cfg = redmine_sync.load_config()
        pro = [f for f in files if f.name.startswith("PRO-QMS")][0]
        r = redmine_sync.sync_file(pro, client=None, cfg=cfg, dry_run=True)
        self.assertEqual(r["status"], "dry-run")
        self.assertEqual(r["redmine_project"], "lib-acme-qms")
        # 플랫폼 관리 문서(00_공통관리 등)는 status 가 없어 draft 취급 → skipped
        managed = [f for f in files if "01_문서체계" in f.name][0]
        self.assertEqual(redmine_sync.sync_file(managed, client=None, cfg=cfg, dry_run=True)["status"], "skipped")


class TestDispatcherCli(Base):
    def _run(self, *argv):
        return subprocess.run([PY, str(PUBLISH / "dispatcher.py"), *argv], cwd=PLATFORM, env=self._env(),
                              capture_output=True, text=True, encoding="utf-8")

    def test_push_dry_run_and_enabled_gate(self):
        r = self._run("push", "--dry-run")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("lib-acme-qms", r.stdout)
        self.assertIn("조직: acme", r.stderr)

        r = self._run("push")                       # enabled: false → 전송 전에 중단
        self.assertEqual(r.returncode, 1)
        self.assertIn("redmine.enabled", r.stderr)

        r = self._run("push", "--status")
        self.assertEqual(r.returncode, 0, r.stderr)

        r = self._run("workspace", "list")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("등록된 Workspace 없음", r.stdout)

    def test_missing_org_fails(self):
        env = self._env()
        env.pop("PROCESSWARE_ORG_ROOT")
        r = subprocess.run([PY, str(PUBLISH / "dispatcher.py"), "push", "--dry-run"], cwd=PLATFORM, env=env,
                           capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 1)
        self.assertIn("PROCESSWARE_ORG_ROOT", r.stderr)


if __name__ == "__main__":
    unittest.main()
