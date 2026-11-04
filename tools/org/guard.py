"""격리 가드 — 활성 조직 루트 밖 · 플랫폼 관리 파일에 대한 쓰기 차단 (org-layer.md §3 단계 5).

영역(zone)
  org      : 활성 조직 루트 안 ({ORG_ROOT}/**)
  platform : 플랫폼 repo 안 (.claude/ tools/ docs/ core/ …)
  outside  : 둘 다 아님

규칙
  read  : org · platform 허용, outside 거부
  write : org 허용 — 단 core/vault_base/_manifest.yaml 의 managed 파일(00_공통관리 · 01_구성원칙 · 99_템플릿 · 폴더 README …)은 거부
          platform 거부 (allow_platform=True 일 때만 허용 — 플랫폼 개발 작업)
          outside 거부
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional

from .context import OrgContext

# 플랫폼 repo 안에서 "조직 데이터처럼 보이는" 위치 — 단계 3 이후 플랫폼에는 존재하지 않아야 한다
LEGACY_PLATFORM_DATA_DIRS = ("vault", "inputs", "sources", ".processware")


@dataclass
class GuardResult:
    path: str
    resolved: str
    mode: str                 # read | write
    zone: str                 # org | platform | outside
    rel: Optional[str]        # zone 기준 상대경로
    managed: bool
    ok: bool
    reason: Optional[str] = None

    def as_dict(self) -> dict:
        return asdict(self)


class Guard:
    def __init__(self, ctx: OrgContext):
        self.ctx = ctx
        self._manifest = None

    # ── manifest (지연 로드) ──
    @property
    def manifest(self):
        if self._manifest is None:
            from .sync import VAULT_BASE, Manifest, SyncError
            base = self.ctx.platform_root / VAULT_BASE
            try:
                self._manifest = Manifest.load(base)
            except SyncError:
                self._manifest = False
        return self._manifest or None

    # ── 영역 판정 ──
    def zone(self, path) -> tuple:
        p = Path(path).expanduser()
        if not p.is_absolute():
            p = Path.cwd() / p
        p = p.resolve()
        org = self.ctx.org_root.resolve()
        plat = self.ctx.platform_root.resolve()
        try:
            return "org", p.relative_to(org).as_posix(), p
        except ValueError:
            pass
        try:
            return "platform", p.relative_to(plat).as_posix(), p
        except ValueError:
            pass
        return "outside", None, p

    def is_managed(self, resolved: Path) -> bool:
        """{ORG_ROOT}/vault 아래의 플랫폼 관리 파일인가 (manifest managed)."""
        try:
            rel = resolved.relative_to(self.ctx.vault.resolve()).as_posix()
        except ValueError:
            return False
        m = self.manifest
        return bool(m) and m.classify(rel) == "managed"

    def legacy_platform_data(self, rel: Optional[str]) -> bool:
        return bool(rel) and rel.split("/", 1)[0] in LEGACY_PLATFORM_DATA_DIRS

    # ── 판정 ──
    def check(self, path, mode: str = "write", allow_platform: bool = False) -> GuardResult:
        zone, rel, resolved = self.zone(path)
        managed = zone == "org" and self.is_managed(resolved)
        res = GuardResult(path=str(path), resolved=str(resolved), mode=mode, zone=zone, rel=rel, managed=managed, ok=False)

        if mode == "read":
            if zone in ("org", "platform"):
                res.ok = True
            else:
                res.reason = f"활성 조직 루트({self.ctx.org_root}) 와 플랫폼 밖의 경로는 읽지 않는다"
            return res

        # write
        if zone == "org":
            if managed:
                res.reason = (
                    f"플랫폼 관리 파일 (core/vault_base managed): {rel} — 직접 수정 금지. "
                    "플랫폼 repo 의 core/vault_base 를 고치고 `python3 -m tools.org sync-core` 로 반영한다. "
                    "조직별 추가는 별도 파일로."
                )
            else:
                res.ok = True
        elif zone == "platform":
            if self.legacy_platform_data(rel):
                res.reason = (
                    f"플랫폼 repo 안의 '{rel.split('/', 1)[0]}/' 은 더 이상 조직 데이터 위치가 아니다 — "
                    f"활성 조직 루트 {self.ctx.org_root} 아래에 써야 한다"
                )
            elif allow_platform:
                res.ok = True
            else:
                res.reason = "플랫폼 자산(.claude/ tools/ docs/ core/)은 커맨드 실행 중 읽기 전용 — 플랫폼 개발 작업에서만 수정"
        else:
            res.reason = f"활성 조직 루트({self.ctx.org_root}) 밖의 경로에는 쓰지 않는다"
        return res

    def check_many(self, paths, mode: str = "write", allow_platform: bool = False) -> list:
        return [self.check(p, mode, allow_platform) for p in paths]
