"""sync-core — 플랫폼 core/ 를 조직 루트에 동기화 (org-layer.md §3 단계 3).

core/vault_base/  → {ORG_ROOT}/vault/   (_manifest.yaml 의 managed / seed 규칙)
core/org_base/    → {ORG_ROOT}/         (없을 때만 복사 — README · .gitignore 등 조직이 소유)

managed : 플랫폼 관리 파일. sync 마다 덮어쓴다 (00_공통관리 · 01_구성원칙 · 99_템플릿 · 폴더 README …).
seed    : 조직 시드 파일. 없을 때만 복사하고 이후 조직이 소유한다 (MAT-001~009 · MOC …). --force 로 재시드.
"""

from __future__ import annotations

import datetime as _dt
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import yaml

from .context import OrgContext, OrgContextError

VAULT_BASE = "core/vault_base"
ORG_BASE = "core/org_base"
MANIFEST = "_manifest.yaml"
SYNC_RECORD = ".processware/sync-core.yaml"


class SyncError(Exception):
    pass


@dataclass
class SyncReport:
    created: list = field(default_factory=list)
    updated: list = field(default_factory=list)
    unchanged: list = field(default_factory=list)
    skipped_seed: list = field(default_factory=list)   # seed 가 이미 존재 → 보존
    unclassified: list = field(default_factory=list)   # manifest 에 없는 파일 (오류)
    org_base_created: list = field(default_factory=list)
    org_base_skipped: list = field(default_factory=list)
    platform_version: str = "unknown"
    dry_run: bool = False

    @property
    def ok(self) -> bool:
        return not self.unclassified

    def summary(self) -> str:
        tag = "[dry-run] " if self.dry_run else ""
        lines = [
            f"{tag}sync-core  platform={self.platform_version}",
            f"  vault  created={len(self.created)} updated={len(self.updated)} "
            f"unchanged={len(self.unchanged)} seed-kept={len(self.skipped_seed)}",
            f"  org    created={len(self.org_base_created)} kept={len(self.org_base_skipped)}",
        ]
        if self.unclassified:
            lines.append(f"  ERROR  manifest 에 분류되지 않은 파일 {len(self.unclassified)}건:")
            lines += [f"    - {p}" for p in self.unclassified]
        return "\n".join(lines)


# ── glob ──────────────────────────────────────────────────────────────────

def _glob_to_re(pattern: str) -> "re.Pattern[str]":
    """'**/' '**' '*' '?' 를 지원하는 경로 glob → 정규식 (POSIX 구분자, 전체 일치)."""
    out = []
    i = 0
    while i < len(pattern):
        c = pattern[i]
        if pattern.startswith("**/", i):
            out.append("(?:.*/)?")
            i += 3
        elif pattern.startswith("**", i):
            out.append(".*")
            i += 2
        elif c == "*":
            out.append("[^/]*")
            i += 1
        elif c == "?":
            out.append("[^/]")
            i += 1
        else:
            out.append(re.escape(c))
            i += 1
    return re.compile("^" + "".join(out) + "$")


@dataclass
class Manifest:
    managed: list
    seed: list

    @classmethod
    def load(cls, base: Path) -> "Manifest":
        p = base / MANIFEST
        if not p.is_file():
            raise SyncError(f"manifest 없음: {p}")
        with open(p, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        return cls(
            managed=[_glob_to_re(g) for g in data.get("managed") or []],
            seed=[_glob_to_re(g) for g in data.get("seed") or []],
        )

    def classify(self, rel: str) -> Optional[str]:
        if any(r.match(rel) for r in self.managed):
            return "managed"
        if any(r.match(rel) for r in self.seed):
            return "seed"
        return None


# ── helpers ───────────────────────────────────────────────────────────────

def platform_version(platform_root: Path) -> str:
    try:
        out = subprocess.run(
            ["git", "-C", str(platform_root), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, timeout=5,
        )
        return out.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def _iter_files(base: Path):
    for p in sorted(base.rglob("*")):
        if p.is_file():
            rel = p.relative_to(base).as_posix()
            if rel == MANIFEST or "/__pycache__/" in f"/{rel}":
                continue
            yield rel, p


def _same(a: Path, b: Path) -> bool:
    return a.read_bytes() == b.read_bytes()


def _copy(src: Path, dst: Path, dry_run: bool):
    if dry_run:
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def _set_platform_version(org_yaml: Path, version: str, dry_run: bool):
    """org.yaml 의 platform_version 줄만 교체 (주석 보존)."""
    if dry_run:
        return
    text = org_yaml.read_text(encoding="utf-8")
    new_line = f'platform_version: "{version}"'
    if re.search(r"^platform_version:.*$", text, flags=re.M):
        text = re.sub(r'^platform_version:\s*"?[^"\n#]*"?', new_line, text, count=1, flags=re.M)
    else:
        text = text.rstrip("\n") + "\n" + new_line + "\n"
    org_yaml.write_text(text, encoding="utf-8")


# ── main entry ────────────────────────────────────────────────────────────

def sync_core(ctx: OrgContext, dry_run: bool = False, force: bool = False) -> SyncReport:
    """core/ → 조직 루트 동기화. 반환된 report.ok 가 False 면 manifest 누락 (파일은 그래도 처리됨)."""
    if ctx.org_yaml is None:
        raise OrgContextError("조직 모드가 아닙니다 — sync-core 는 조직 루트가 필요합니다.")

    vault_base = ctx.platform_root / VAULT_BASE
    org_base = ctx.platform_root / ORG_BASE
    if not vault_base.is_dir():
        raise SyncError(f"플랫폼 vault 템플릿 없음: {vault_base}")

    manifest = Manifest.load(vault_base)
    rep = SyncReport(dry_run=dry_run, platform_version=platform_version(ctx.platform_root))

    # 1) vault_base → {ORG_ROOT}/vault
    for rel, src in _iter_files(vault_base):
        kind = manifest.classify(rel)
        dst = ctx.vault / rel
        if kind is None:
            rep.unclassified.append(rel)
            continue
        if not dst.exists():
            _copy(src, dst, dry_run)
            rep.created.append(rel)
        elif kind == "managed" or force:
            if _same(src, dst):
                rep.unchanged.append(rel)
            else:
                _copy(src, dst, dry_run)
                rep.updated.append(rel)
        else:  # seed & exists
            rep.skipped_seed.append(rel)

    # 2) org_base → {ORG_ROOT}  (없을 때만)
    if org_base.is_dir():
        for rel, src in _iter_files(org_base):
            dst = ctx.org_root / rel
            if dst.exists():
                rep.org_base_skipped.append(rel)
            else:
                _copy(src, dst, dry_run)
                rep.org_base_created.append(rel)

    # 3) 기록
    _set_platform_version(ctx.org_yaml, rep.platform_version, dry_run)
    if not dry_run:
        rec = ctx.org_root / SYNC_RECORD
        rec.parent.mkdir(parents=True, exist_ok=True)
        with open(rec, "w", encoding="utf-8") as f:
            yaml.safe_dump(
                {
                    "last_sync": _dt.datetime.now().isoformat(timespec="seconds"),
                    "platform_version": rep.platform_version,
                    "created": len(rep.created),
                    "updated": len(rep.updated),
                    "seed_kept": len(rep.skipped_seed),
                    "unclassified": rep.unclassified,
                },
                f, allow_unicode=True, sort_keys=False,
            )
    return rep
