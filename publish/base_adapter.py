"""vault 외부 시스템 연동 어댑터 추상 인터페이스."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class BaseAdapter(ABC):
    """각 외부 시스템 어댑터가 구현해야 하는 인터페이스."""

    # ── Library 동기화 ────────────────────────────────────────────────────────

    @abstractmethod
    def push(
        self,
        doc_id: str | None = None,
        changed_only: bool = False,
        type_filter: str | None = None,
        scope_filter: str | None = None,
        dry_run: bool = False,
    ) -> int:
        """vault → 외부 시스템 Library 동기화. 종료 코드 반환."""

    @abstractmethod
    def setup(self, dry_run: bool = False) -> int:
        """외부 시스템 Library 프로젝트 계층 초기화. 종료 코드 반환."""

    @abstractmethod
    def status(self) -> int:
        """마지막 동기화 상태 출력. 종료 코드 반환."""

    # ── Workspace ─────────────────────────────────────────────────────────────

    @abstractmethod
    def workspace_create(
        self,
        name: str,
        slug: str,
        modules: list[str],
        description: str = "",
        dry_run: bool = False,
    ) -> int:
        """Workspace 생성. 종료 코드 반환."""

    @abstractmethod
    def workspace_sync(
        self,
        workspace_slug: str,
        module: str,
        dry_run: bool = False,
    ) -> int:
        """Library Module → Workspace Module 최신화. 종료 코드 반환."""

    @abstractmethod
    def workspace_list(self) -> int:
        """전체 Workspace 목록 출력. 종료 코드 반환."""

    @abstractmethod
    def workspace_status(self, workspace_slug: str) -> int:
        """특정 Workspace 상세 출력. 종료 코드 반환."""
