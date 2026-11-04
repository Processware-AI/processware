"""python -m unittest tools.org.tests.test_overview"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.org import registry, resolve
from tools.org.overview import collect, render_markdown, render_table
from tools.org.sync import sync_core

PLATFORM = Path(__file__).resolve().parents[3]
PY = sys.executable
ORG_ENV_KEYS = ("PROCESSWARE_ORG_ROOT", "PROCESSWARE_ORG", "PROCESSWARE_HOME", "PROCESSWARE_PLATFORM_ROOT")


def _snapshot(root: Path) -> set:
    return {(p.relative_to(root).as_posix(), p.stat().st_mtime_ns) for p in root.rglob("*") if p.is_file()}


class TestOverview(unittest.TestCase):
    def setUp(self):
        self._saved = {k: os.environ.pop(k, None) for k in ORG_ENV_KEYS}
        self.tmp = tempfile.TemporaryDirectory()
        os.environ["PROCESSWARE_HOME"] = str(Path(self.tmp.name) / "home")

        # acme: 자산 · NCR · trace · queue 가 있는 조직
        self.acme = Path(self.tmp.name) / "acme"
        self.acme.mkdir()
        (self.acme / "org.yaml").write_text(
            'org_id: acme\nname: "ACME"\nscopes: [QMS]\nplatform_version: "old"\n'
            'rbac:\n  enforce: true\n  users:\n    "a": [auditor]\n    "b": [executor]\n', encoding="utf-8")
        ctx = resolve(org_root=self.acme, cwd=PLATFORM)
        sync_core(ctx)                                      # platform_version 갱신됨
        v = ctx.vault
        (v / "02_적용요건" / "품질경영").mkdir(parents=True)
        (v / "03_POL_정책" / "POL-QMS-01_품질정책_v1.0.md").write_text("---\ndoc_id: POL-QMS-01\n---\n", encoding="utf-8")
        (v / "04_PRO_절차" / "PRO-QMS-01-01_x_v1.0.md").write_text("---\ndoc_id: PRO-QMS-01-01\n---\n", encoding="utf-8")
        for i in (1, 2, 3):
            (v / "05_WI_업무지침" / f"WI-QMS-01-01-0{i}_x_v1.0.md").write_text("---\n---\n", encoding="utf-8")
        audit = v / "08_REC_기록" / "AUDIT"
        audit.mkdir(parents=True)
        (audit / "REC-NCR-01-01-2026-001_x.md").write_text("---\nstatus: open\nseverity: major\n---\n", encoding="utf-8")
        (audit / "REC-NCR-01-01-2026-002_x.md").write_text("---\nstatus: closed\n---\n", encoding="utf-8")
        (audit / "REC-AUDIT-01-01-2026-001_x.md").write_text("---\n---\n", encoding="utf-8")
        (v / "08_REC_기록" / "REC-QMS-01-01-01-01-2026-001_x.md").write_text("---\n---\n", encoding="utf-8")
        for name, status in (("run-a1b2c3d4", "done"), ("run-1234abcd", "running"), ("run-c0ffee00", "done")):
            d = ctx.runs / name
            d.mkdir(parents=True)
            (d / "state.yaml").write_text(f"status: {status}\n", encoding="utf-8")
        q = ctx.queues / "process-act"
        q.mkdir(parents=True)
        (q / "queue-q1.yaml").write_text("status: pending\n", encoding="utf-8")
        (q / "queue-q2.yaml").write_text("status: done\n", encoding="utf-8")
        (self.acme / ".processware" / "rbac_audit.jsonl").write_text(
            '{"event": "rbac_denied"}\n{"event": "rbac_allowed"}\n{"event": "rbac_denied"}\n', encoding="utf-8")
        registry.register(self.acme)

        # beta: 빈 조직 (platform_version 일치), redmine on
        self.beta = Path(self.tmp.name) / "beta"
        self.beta.mkdir()
        (self.beta / "org.yaml").write_text('org_id: beta\nname: "Beta"\nredmine:\n  enabled: true\n', encoding="utf-8")
        sync_core(resolve(org_root=self.beta, cwd=PLATFORM))
        registry.register(self.beta)

        # broken: 레지스트리에는 있지만 org.yaml 이 사라진 조직
        self.broken = Path(self.tmp.name) / "broken"
        self.broken.mkdir()
        (self.broken / "org.yaml").write_text('org_id: broken\nname: "B"\n', encoding="utf-8")
        registry.register(self.broken)
        (self.broken / "org.yaml").unlink()

    def tearDown(self):
        for k in ORG_ENV_KEYS:
            os.environ.pop(k, None)
        for k, v in self._saved.items():
            if v is not None:
                os.environ[k] = v
        self.tmp.cleanup()

    def test_collect_counts_and_read_only(self):
        before = _snapshot(self.acme) | _snapshot(self.beta)
        rows = {s.org_id: s for s in collect()}
        self.assertEqual(before, _snapshot(self.acme) | _snapshot(self.beta))   # 아무것도 쓰지 않음

        a = rows["acme"]
        self.assertTrue(a.ok)
        self.assertEqual(a.docs["POL"], 1)
        self.assertEqual(a.docs["PRO"], 1)
        self.assertEqual(a.docs["WI"], 3)
        self.assertEqual(a.docs["REC"], 4)          # REC 1 + AUDIT 폴더 3 (하위 포함)
        self.assertGreaterEqual(a.docs["MAT"], 9)   # 시드된 MAT-001~009
        self.assertEqual(a.modules, 1)
        self.assertEqual((a.ncr_open, a.ncr_closed, a.audits, a.gaps), (1, 1, 1, 0))
        self.assertEqual(a.traces, {"audit": 1, "do": 1, "act": 1})
        self.assertEqual(a.traces_running, 1)
        self.assertEqual(a.queues, {"pending": 1, "done": 1})
        self.assertEqual(a.rbac_denied, 2)
        self.assertTrue(a.rbac_enforce)
        self.assertEqual(a.users, 2)
        self.assertEqual(a.scopes, ["QMS"])
        self.assertFalse(a.platform_drift)          # sync_core 가 현재 버전으로 갱신
        self.assertTrue(a.last_sync)

        b = rows["beta"]
        self.assertTrue(b.redmine_enabled)
        self.assertEqual(b.docs["POL"], 0)
        self.assertEqual(b.ncr_open, 0)

        self.assertFalse(rows["broken"].ok)
        self.assertIn("org.yaml", rows["broken"].error)

    def test_drift_and_filter(self):
        (self.beta / "org.yaml").write_text('org_id: beta\nname: "Beta"\nplatform_version: "deadbeef"\n', encoding="utf-8")
        rows = collect(org_ids=["beta"])
        self.assertEqual([s.org_id for s in rows], ["beta"])
        self.assertTrue(rows[0].platform_drift)

    def test_renderers(self):
        rows = collect()
        md = render_markdown(rows, "abc1234")
        self.assertIn("| `acme` |", md)
        self.assertIn("미종결 NCR: acme 1건", md)
        self.assertIn("대기 중 act queue: acme 1건", md)
        self.assertIn("해석 실패 조직: broken", md)
        tb = render_table(rows, "abc1234")
        self.assertIn("acme", tb)
        self.assertIn("❌", tb)

    def test_cli(self):
        env = dict(os.environ)
        for k in ORG_ENV_KEYS:
            env.pop(k, None)
        env["PROCESSWARE_HOME"] = os.environ["PROCESSWARE_HOME"]
        r = subprocess.run([PY, "-m", "tools.org", "overview", "--format", "json"], cwd=PLATFORM, env=env,
                           capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 3, r.stderr)          # broken 조직 포함 → exit 3 (결과는 출력됨)
        data = json.loads(r.stdout)
        self.assertEqual({o["org_id"] for o in data["orgs"]}, {"acme", "beta", "broken"})
        out = Path(self.tmp.name) / "report.md"
        r = subprocess.run([PY, "-m", "tools.org", "overview", "--format", "md", "--out", str(out)], cwd=PLATFORM, env=env,
                           capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 3, r.stderr)
        self.assertIn("교차 조직 뷰", out.read_text(encoding="utf-8"))
        self.assertIn("해석 실패 조직: broken", out.read_text(encoding="utf-8"))
        # --org-root 로 미등록 조직 추가
        extra = Path(self.tmp.name) / "gamma"
        extra.mkdir()
        (extra / "org.yaml").write_text('org_id: gamma\nname: "G"\n', encoding="utf-8")
        r = subprocess.run([PY, "-m", "tools.org", "overview", "--format", "json", "--org", "beta", "--root", str(extra)],
                           cwd=PLATFORM, env=env, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual([o["org_id"] for o in json.loads(r.stdout)["orgs"]], ["beta", "gamma"])


if __name__ == "__main__":
    unittest.main()
