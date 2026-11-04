"""교차 조직 뷰 — 레지스트리의 모든 조직 루트를 읽기 전용으로 집계 (org-layer.md §3 단계 7).

컨설팅 펌 관점의 통합 대시보드. 조직 데이터를 복제하지 않고 각 루트를 읽어 수치만 모은다.
어떤 조직 루트에도 쓰지 않는다 (sync-core 기록 · 감사 로그 포함).

수집 항목 (조직당):
  설정    org_id · name · root · platform_version(조직) vs 플랫폼 현재 · rbac.enforce · 사용자 수 · redmine.enabled
  자산    POL / PRO / WI / TMP / EX / REC / REF / MAT 파일 수, 적용요건 모듈 수, 영역코드
  실행    trace 수 (run-* 접두어별) · 진행 중 trace · act queue (pending / in_progress / done)
  심사    NCR open / closed (REC-NCR frontmatter status) · REC-AUDIT · REC-GAP 수
  거버넌스 rbac_audit 거부 건수 · 최근 sync-core · 최근 활동(git HEAD 날짜 또는 vault mtime)
"""

from __future__ import annotations

import datetime as _dt
import json
import re
import subprocess
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional

import yaml

from . import registry
from .context import OrgContext, OrgContextError, resolve, find_platform_root
from .sync import SYNC_RECORD, platform_version

DOC_FOLDERS = {
    "POL": "03_POL_정책",
    "PRO": "04_PRO_절차",
    "WI": "05_WI_업무지침",
    "TMP": "06_TMP_템플릿",
    "EX": "07_EX_작성예시",
    "REC": "08_REC_기록",
    "REF": "09_REF_참고자료",
    "MAT": "90_MAT_통합매핑",
}
RUN_PREFIX = {"a": "audit", "k": "kpi", "g": "gap", "c": "act", "b": "backfill"}


@dataclass
class OrgSummary:
    org_id: str
    name: str = ""
    root: str = ""
    ok: bool = True
    error: Optional[str] = None
    platform_version: str = ""
    platform_drift: bool = False
    rbac_enforce: Optional[bool] = None
    users: int = 0
    redmine_enabled: bool = False
    scopes: list = field(default_factory=list)
    modules: int = 0                               # 02_적용요건/{명칭}/
    docs: dict = field(default_factory=dict)       # {POL: n, PRO: n, ...}
    traces: dict = field(default_factory=dict)     # {do: n, audit: n, ...}
    traces_running: int = 0
    queues: dict = field(default_factory=dict)     # {pending: n, in_progress: n, done: n}
    ncr_open: int = 0
    ncr_closed: int = 0
    audits: int = 0
    gaps: int = 0
    rbac_denied: int = 0
    last_sync: str = ""
    last_activity: str = ""

    def as_dict(self) -> dict:
        return asdict(self)


# ── 파서 (읽기 전용) ───────────────────────────────────────────────────────

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)


def _frontmatter(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}
    m = _FM_RE.match(text)
    if not m:
        return {}
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def _is_doc(p: Path) -> bool:
    return p.suffix == ".md" and p.name != "README.md" and not p.name.startswith("_")


def _count_docs(vault: Path) -> dict:
    out = {}
    for t, folder in DOC_FOLDERS.items():
        d = vault / folder
        out[t] = sum(1 for p in d.rglob("*.md") if _is_doc(p)) if d.is_dir() else 0
    return out


def _modules(vault: Path) -> int:
    d = vault / "02_적용요건"
    return sum(1 for p in d.iterdir() if p.is_dir() and not p.name.startswith(("_", "."))) if d.is_dir() else 0


def _traces(runs: Path) -> tuple:
    counts: dict = {}
    running = 0
    if not runs.is_dir():
        return counts, running
    for d in runs.iterdir():
        if not d.is_dir() or not d.name.startswith("run-"):
            continue
        kind = RUN_PREFIX.get(d.name[4:5], "do")
        counts[kind] = counts.get(kind, 0) + 1
        st = d / "state.yaml"
        if st.is_file():
            try:
                data = yaml.safe_load(st.read_text(encoding="utf-8", errors="replace")) or {}
            except yaml.YAMLError:
                data = {}
            status = str(data.get("status") or data.get("overall_status") or "")
            if status in ("running", "pending_approval", "paused", "in_progress"):
                running += 1
    return counts, running


def _queues(queues: Path) -> dict:
    out: dict = {}
    d = queues / "process-act"
    if not d.is_dir():
        return out
    for p in d.glob("queue-q*.yaml"):
        try:
            data = yaml.safe_load(p.read_text(encoding="utf-8", errors="replace")) or {}
        except yaml.YAMLError:
            data = {}
        status = str(data.get("status") or "unknown")
        out[status] = out.get(status, 0) + 1
    return out


def _audit_docs(vault: Path) -> tuple:
    d = vault / "08_REC_기록" / "AUDIT"
    ncr_open = ncr_closed = audits = gaps = 0
    if not d.is_dir():
        return ncr_open, ncr_closed, audits, gaps
    for p in d.glob("*.md"):
        n = p.name
        if n.startswith("REC-NCR"):
            fm = _frontmatter(p)
            if str(fm.get("status", "open")).lower() in ("closed", "done", "verified"):
                ncr_closed += 1
            else:
                ncr_open += 1
        elif n.startswith("REC-AUDIT"):
            audits += 1
        elif n.startswith("REC-GAP"):
            gaps += 1
    return ncr_open, ncr_closed, audits, gaps


def _rbac_denied(org_root: Path, org: dict) -> int:
    rel = ((org.get("rbac") or {}).get("audit_log")) or ".processware/rbac_audit.jsonl"
    p = org_root / rel
    if not p.is_file():
        return 0
    n = 0
    with open(p, encoding="utf-8", errors="replace") as f:
        for line in f:
            if '"event": "rbac_denied"' in line or '"event":"rbac_denied"' in line:
                n += 1
    return n


def _last_sync(org_root: Path) -> str:
    p = org_root / SYNC_RECORD
    if not p.is_file():
        return ""
    try:
        data = yaml.safe_load(p.read_text(encoding="utf-8", errors="replace")) or {}
    except yaml.YAMLError:
        return ""
    return str(data.get("last_sync") or "")[:19]


def _last_activity(org_root: Path, vault: Path) -> str:
    try:
        r = subprocess.run(["git", "-C", str(org_root), "log", "-1", "--format=%cI"],
                           capture_output=True, text=True, timeout=5)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()[:19]
    except Exception:
        pass
    latest = 0.0
    if vault.is_dir():
        for p in vault.rglob("*.md"):
            try:
                latest = max(latest, p.stat().st_mtime)
            except OSError:
                pass
    return _dt.datetime.fromtimestamp(latest).isoformat(timespec="seconds") if latest else ""


# ── 집계 ──────────────────────────────────────────────────────────────────

def summarize(ctx: OrgContext, current_platform: str) -> OrgSummary:
    from .schema import load_org_yaml
    org = load_org_yaml(ctx.org_yaml)
    s = OrgSummary(org_id=ctx.org_id, name=str(org.get("name", "")), root=str(ctx.org_root))
    s.platform_version = str(org.get("platform_version") or "")
    s.platform_drift = bool(s.platform_version and current_platform not in ("", "unknown") and s.platform_version != current_platform)
    rb = org.get("rbac") or {}
    s.rbac_enforce = bool(rb.get("enforce", True)) if rb else None
    s.users = len(rb.get("users") or {})
    s.redmine_enabled = bool((org.get("redmine") or {}).get("enabled", False))
    s.scopes = [str(x) for x in (org.get("scopes") or [])]
    s.modules = _modules(ctx.vault)
    s.docs = _count_docs(ctx.vault)
    s.traces, s.traces_running = _traces(ctx.runs)
    s.queues = _queues(ctx.queues)
    s.ncr_open, s.ncr_closed, s.audits, s.gaps = _audit_docs(ctx.vault)
    s.rbac_denied = _rbac_denied(ctx.org_root, org)
    s.last_sync = _last_sync(ctx.org_root)
    s.last_activity = _last_activity(ctx.org_root, ctx.vault)
    return s


def collect(org_ids: Optional[list] = None, extra_roots: Optional[list] = None) -> list:
    """레지스트리(+ 추가 루트)의 조직을 집계. 해석 실패한 조직은 ok=False 로 포함."""
    current = platform_version(find_platform_root())
    targets: list = []
    reg = registry.load()
    for oid, root in reg.items():
        if org_ids and oid not in org_ids:
            continue
        targets.append((oid, root))
    for r in extra_roots or []:
        targets.append((Path(r).name, str(r)))

    out = []
    for oid, root in targets:
        try:
            ctx = resolve(org_root=root, strict=False)
            out.append(summarize(ctx, current))
        except (OrgContextError, Exception) as e:  # 한 조직의 문제가 전체 뷰를 막지 않게
            out.append(OrgSummary(org_id=oid, root=str(root), ok=False, error=str(e)))
    return out


# ── 렌더링 ────────────────────────────────────────────────────────────────

def _q(s: OrgSummary, k: str) -> int:
    return int(s.queues.get(k, 0))


def render_table(rows: list, current_platform: str) -> str:
    hdr = f"{'org':<12} {'name':<18} {'POL/PRO/WI':<12} {'REC':>5} {'NCR o/c':<8} {'queue p/i/d':<12} {'trace(run)':<11} {'rbac':<9} {'redmine':<8} {'platform':<9} {'last activity'}"
    lines = [f"platform={current_platform}", hdr, "-" * len(hdr)]
    for s in rows:
        if not s.ok:
            lines.append(f"{s.org_id:<12} ❌ {s.error}")
            continue
        d = s.docs
        tr = sum(s.traces.values())
        rbac = ("enforce" if s.rbac_enforce else "off") + f"/{s.users}"
        plat = s.platform_version + ("⚠" if s.platform_drift else "")
        lines.append(
            f"{s.org_id:<12} {s.name[:18]:<18} {d.get('POL',0)}/{d.get('PRO',0)}/{d.get('WI',0):<7} {d.get('REC',0):>5} "
            f"{s.ncr_open}/{s.ncr_closed:<6} {_q(s,'pending')}/{_q(s,'in_progress')}/{_q(s,'done'):<8} "
            f"{tr}({s.traces_running}){'':<6} {rbac:<9} {('on' if s.redmine_enabled else 'off'):<8} {plat:<9} {s.last_activity[:10]}"
        )
    return "\n".join(lines)


def render_markdown(rows: list, current_platform: str) -> str:
    now = _dt.datetime.now().isoformat(timespec="minutes")
    out = [f"# Processware 교차 조직 뷰", "",
           f"> 생성: {now} · 플랫폼: `{current_platform}` · 조직 {len(rows)}개 · 읽기 전용 집계 (조직 데이터 복제 없음)", "",
           "| 조직 | 명칭 | 영역코드 | 모듈 | POL / PRO / WI | TMP / EX | REC | NCR open / closed | 심사 / GAP | act queue p / i / d | trace (진행) | RBAC | Redmine | platform | 최근 sync-core | 최근 활동 |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in rows:
        if not s.ok:
            out.append(f"| `{s.org_id}` | ❌ {s.error} |" + " |" * 14)
            continue
        d = s.docs
        plat = f"`{s.platform_version}`" + (" ⚠ drift" if s.platform_drift else "")
        rbac = ("enforce" if s.rbac_enforce else "off") + f" · {s.users}명" + (f" · 거부 {s.rbac_denied}" if s.rbac_denied else "")
        out.append(
            f"| `{s.org_id}` | {s.name} | {', '.join(s.scopes) or '—'} | {s.modules} | {d.get('POL',0)} / {d.get('PRO',0)} / {d.get('WI',0)} "
            f"| {d.get('TMP',0)} / {d.get('EX',0)} | {d.get('REC',0)} | {s.ncr_open} / {s.ncr_closed} | {s.audits} / {s.gaps} "
            f"| {_q(s,'pending')} / {_q(s,'in_progress')} / {_q(s,'done')} | {sum(s.traces.values())} ({s.traces_running}) "
            f"| {rbac} | {'on' if s.redmine_enabled else 'off'} | {plat} | {s.last_sync or '—'} | {s.last_activity or '—'} |"
        )
    drift = [s.org_id for s in rows if s.ok and s.platform_drift]
    open_ncr = [(s.org_id, s.ncr_open) for s in rows if s.ok and s.ncr_open]
    pending = [(s.org_id, _q(s, "pending")) for s in rows if s.ok and _q(s, "pending")]
    out += ["", "## 주의 항목", ""]
    out.append(f"- 플랫폼 버전 불일치 (sync-core 필요): {', '.join(drift) if drift else '없음'}")
    out.append("- 미종결 NCR: " + (", ".join(f"{o} {n}건" for o, n in open_ncr) if open_ncr else "없음"))
    out.append("- 대기 중 act queue: " + (", ".join(f"{o} {n}건" for o, n in pending) if pending else "없음"))
    broken = [s.org_id for s in rows if not s.ok]
    out.append(f"- 해석 실패 조직: {', '.join(broken) if broken else '없음'}")
    return "\n".join(out) + "\n"


def render_json(rows: list, current_platform: str) -> str:
    return json.dumps({"platform_version": current_platform,
                       "generated_at": _dt.datetime.now().isoformat(timespec="seconds"),
                       "orgs": [s.as_dict() for s in rows]}, ensure_ascii=False, indent=2)
