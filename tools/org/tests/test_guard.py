"""python -m unittest tools.org.tests.test_guard"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.org import resolve
from tools.org.guard import Guard
from tools.org.sync import sync_core

PLATFORM = Path(__file__).resolve().parents[3]
PY = sys.executable
ORG_ENV_KEYS = ("PROCESSWARE_ORG_ROOT", "PROCESSWARE_ORG", "PROCESSWARE_HOME", "PROCESSWARE_PLATFORM_ROOT")


class Base(unittest.TestCase):
    def setUp(self):
        self._saved = {k: os.environ.pop(k, None) for k in ORG_ENV_KEYS}
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "acme"
        self.root.mkdir()
        (self.root / "org.yaml").write_text('org_id: acme\nname: "ACME"\n', encoding="utf-8")
        self.ctx = resolve(org_root=self.root, cwd=PLATFORM)
        sync_core(self.ctx)
        self.guard = Guard(self.ctx)

    def tearDown(self):
        for k in ORG_ENV_KEYS:
            os.environ.pop(k, None)
        for k, v in self._saved.items():
            if v is not None:
                os.environ[k] = v
        self.tmp.cleanup()


class TestGuard(Base):
    def test_zones(self):
        self.assertEqual(self.guard.zone(self.root / "vault" / "x.md")[0], "org")
        self.assertEqual(self.guard.zone(PLATFORM / "tools" / "org" / "guard.py")[0], "platform")
        self.assertEqual(self.guard.zone(Path(self.tmp.name) / "elsewhere.md")[0], "outside")

    def test_write_org_ok_and_managed_denied(self):
        ok = self.guard.check(self.root / "vault" / "03_POL_정책" / "POL-QMS-01_x_v1.0.md")
        self.assertTrue(ok.ok)
        rec = self.guard.check(self.root / ".processware" / "runs" / "run-x" / "trace.jsonl")
        self.assertTrue(rec.ok)
        seed = self.guard.check(self.root / "vault" / "90_MAT_통합매핑" / "MAT-001_문서관리대장.md")
        self.assertTrue(seed.ok)                       # seed 는 조직 소유 → 쓰기 허용
        managed = self.guard.check(self.root / "vault" / "01_구성원칙" / "표준프로세스_구성원칙.md")
        self.assertFalse(managed.ok)
        self.assertTrue(managed.managed)
        self.assertIn("sync-core", managed.reason)
        readme = self.guard.check(self.root / "vault" / "03_POL_정책" / "README.md")
        self.assertFalse(readme.ok)                    # 폴더 README 도 managed

    def test_write_platform_and_outside(self):
        plat = self.guard.check(PLATFORM / "docs" / "x.md")
        self.assertFalse(plat.ok)
        self.assertTrue(self.guard.check(PLATFORM / "docs" / "x.md", allow_platform=True).ok)
        legacy = self.guard.check(PLATFORM / "vault" / "03_POL_정책" / "x.md", allow_platform=True)
        self.assertFalse(legacy.ok)
        self.assertIn("조직 데이터 위치가 아니다", legacy.reason)
        out = self.guard.check(Path(self.tmp.name) / "elsewhere.md", allow_platform=True)
        self.assertFalse(out.ok)
        self.assertEqual(out.zone, "outside")

    def test_read(self):
        self.assertTrue(self.guard.check(PLATFORM / ".claude" / "rbac" / "policy.yaml", mode="read").ok)
        self.assertTrue(self.guard.check(self.root / "vault" / "01_구성원칙" / "표준프로세스_구성원칙.md", mode="read").ok)
        self.assertFalse(self.guard.check(Path(self.tmp.name) / "x.md", mode="read").ok)


class TestCli(Base):
    def _env(self, with_org=True):
        env = dict(os.environ)
        for k in ORG_ENV_KEYS:
            env.pop(k, None)
        env["PROCESSWARE_HOME"] = str(Path(self.tmp.name) / "home")
        if with_org:
            env["PROCESSWARE_ORG_ROOT"] = str(self.root)
        return env

    def test_guard_cli(self):
        r = subprocess.run(
            [PY, "-m", "tools.org", "guard", "--mode", "write",
             "--path", str(self.root / "vault" / "03_POL_정책" / "a.md"),
             "--path", str(self.root / "vault" / "01_구성원칙" / "표준프로세스_구성원칙.md"),
             "--format", "json"],
            cwd=PLATFORM, env=self._env(), capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 2, r.stderr)
        rows = json.loads(r.stdout)
        self.assertEqual([x["ok"] for x in rows], [True, False])

    def test_vault_rules_validate_rejects_outside_and_managed(self):
        env = self._env()
        # 조직 vault 안의 정상 파일
        good = self.root / "vault" / "03_POL_정책" / "POL-QMS-01_품질정책_v1.0.md"
        good.write_text("---\ndoc_id: POL-QMS-01\ntitle: 품질정책\nversion: \"1.0\"\nstatus: draft\n---\n# x\n", encoding="utf-8")
        r = subprocess.run([PY, "-m", "tools.vault_rules", "validate", "--file", str(good)],
                           cwd=PLATFORM, env=env, capture_output=True, text=True, encoding="utf-8")
        self.assertNotIn("격리", r.stderr)
        # 조직 밖 파일
        bad = Path(self.tmp.name) / "POL-QMS-01_품질정책_v1.0.md"
        bad.write_text("x", encoding="utf-8")
        r = subprocess.run([PY, "-m", "tools.vault_rules", "validate", "--file", str(bad)],
                           cwd=PLATFORM, env=env, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 1)
        self.assertIn("격리", r.stderr)

    def _hook(self, path, with_org=True):
        payload = json.dumps({"tool_name": "Write", "tool_input": {"file_path": str(path)}})
        return subprocess.run([PY, "-m", "tools.org.hook_guard"], input=payload, cwd=PLATFORM,
                              env=self._env(with_org), capture_output=True, text=True, encoding="utf-8")

    def test_hook(self):
        self.assertEqual(self._hook(self.root / "vault" / "03_POL_정책" / "a.md").returncode, 0)
        self.assertEqual(self._hook(PLATFORM / "docs" / "x.md").returncode, 0)                 # 플랫폼 개발은 허용
        r = self._hook(self.root / "vault" / "01_구성원칙" / "표준프로세스_구성원칙.md")
        self.assertEqual(r.returncode, 2)
        self.assertIn("org-guard", r.stderr)
        self.assertEqual(self._hook(PLATFORM / "vault" / "x.md").returncode, 2)                # 제거된 플랫폼 vault
        self.assertEqual(self._hook(Path(self.tmp.name) / "x.md").returncode, 2)               # outside
        self.assertEqual(self._hook(Path(self.tmp.name) / "x.md", with_org=False).returncode, 0)  # 컨텍스트 없음 → 생략


if __name__ == "__main__":
    unittest.main()
