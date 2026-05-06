"""Sync Map SQLite DB — vault_doc_id ↔ Redmine 리소스 매핑 관리."""

from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Optional

DEFAULT_DB_PATH = Path(__file__).parents[2] / ".claude" / "states" / "redmine_sync.db"


@contextmanager
def get_conn(db_path: Path = DEFAULT_DB_PATH):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db(db_path: Path = DEFAULT_DB_PATH) -> None:
    """스키마 초기화 (없으면 생성, 있으면 무시)."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with get_conn(db_path) as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS sync_map (
                vault_doc_id        TEXT PRIMARY KEY,
                vault_path          TEXT NOT NULL,
                redmine_type        TEXT NOT NULL,
                redmine_project_id  TEXT NOT NULL,
                redmine_resource    TEXT NOT NULL,
                vault_version       TEXT,
                last_synced_at      TEXT,
                status              TEXT DEFAULT 'pending',
                workspace_instance  INTEGER DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS workspace_map (
                workspace_slug      TEXT NOT NULL,
                workspace_name      TEXT NOT NULL,
                redmine_project_id  TEXT NOT NULL,
                source_modules      TEXT NOT NULL,
                created_at          TEXT NOT NULL,
                PRIMARY KEY (workspace_slug, redmine_project_id)
            );

            CREATE INDEX IF NOT EXISTS idx_sync_status
                ON sync_map (status);
            CREATE INDEX IF NOT EXISTS idx_sync_project
                ON sync_map (redmine_project_id);
        """)


# ── sync_map CRUD ──────────────────────────────────────────────────────────────

def upsert_sync(vault_doc_id: str, vault_path: str,
                redmine_type: str, redmine_project_id: str,
                redmine_resource: str, vault_version: str,
                synced_at: str, status: str = "synced",
                workspace_instance: bool = False,
                db_path: Path = DEFAULT_DB_PATH) -> None:
    with get_conn(db_path) as conn:
        conn.execute("""
            INSERT INTO sync_map
                (vault_doc_id, vault_path, redmine_type, redmine_project_id,
                 redmine_resource, vault_version, last_synced_at, status, workspace_instance)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(vault_doc_id) DO UPDATE SET
                vault_path          = excluded.vault_path,
                redmine_type        = excluded.redmine_type,
                redmine_project_id  = excluded.redmine_project_id,
                redmine_resource    = excluded.redmine_resource,
                vault_version       = excluded.vault_version,
                last_synced_at      = excluded.last_synced_at,
                status              = excluded.status
        """, (vault_doc_id, vault_path, redmine_type, redmine_project_id,
              redmine_resource, vault_version, synced_at, status,
              int(workspace_instance)))


def get_sync(vault_doc_id: str,
             db_path: Path = DEFAULT_DB_PATH) -> Optional[sqlite3.Row]:
    with get_conn(db_path) as conn:
        return conn.execute(
            "SELECT * FROM sync_map WHERE vault_doc_id = ?", (vault_doc_id,)
        ).fetchone()


def mark_failed(vault_doc_id: str,
                db_path: Path = DEFAULT_DB_PATH) -> None:
    with get_conn(db_path) as conn:
        conn.execute(
            "UPDATE sync_map SET status = 'failed' WHERE vault_doc_id = ?",
            (vault_doc_id,)
        )


def get_status_summary(db_path: Path = DEFAULT_DB_PATH) -> dict:
    with get_conn(db_path) as conn:
        rows = conn.execute(
            "SELECT status, COUNT(*) as cnt FROM sync_map GROUP BY status"
        ).fetchall()
    return {row["status"]: row["cnt"] for row in rows}


# ── workspace_map CRUD ─────────────────────────────────────────────────────────

def upsert_workspace(workspace_slug: str, workspace_name: str,
                     redmine_project_id: str, source_modules: list[str],
                     created_at: str,
                     db_path: Path = DEFAULT_DB_PATH) -> None:
    import json
    with get_conn(db_path) as conn:
        conn.execute("""
            INSERT INTO workspace_map
                (workspace_slug, workspace_name, redmine_project_id,
                 source_modules, created_at)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(workspace_slug, redmine_project_id) DO UPDATE SET
                workspace_name     = excluded.workspace_name,
                source_modules     = excluded.source_modules
        """, (workspace_slug, workspace_name, redmine_project_id,
              json.dumps(source_modules, ensure_ascii=False), created_at))


def list_workspaces(db_path: Path = DEFAULT_DB_PATH) -> list[sqlite3.Row]:
    with get_conn(db_path) as conn:
        return conn.execute("SELECT * FROM workspace_map ORDER BY created_at DESC").fetchall()
