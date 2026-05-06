"""
REC / REC-NCR → Redmine Issue 동기화 전담 모듈.

REC  (final)    → Tracker: 프로세스기록, Status: 완료(Closed)
REC-NCR (open)  → Tracker: NCR, Status: 진행중, Priority: severity 매핑
REC-NCR (closed)→ Tracker: NCR, Status: 종결
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from redmine_client import RedmineClient
from transformer import transform
from db import upsert_sync, get_sync

# ── 상태 매핑 ────────────────────────────────────────────────────────────────

# vault status → Redmine 상태 이름 (Redmine 관리자가 동일 이름으로 생성해야 함)
STATUS_MAP = {
    # REC
    "final":       "완료",
    "archived":    "완료",
    # NCR
    "open":        "진행중",
    "in_progress": "진행중",
    "closed":      "종결",
}

# NCR severity → Redmine 우선순위 이름
PRIORITY_MAP = {
    "critical": "긴급",
    "major":    "높음",
    "minor":    "보통",
}

DEFAULT_PRIORITY = "보통"


# ── 캐시 (API 반복 호출 방지) ─────────────────────────────────────────────────

_tracker_cache: dict[str, int] = {}
_status_cache: dict[str, int]  = {}
_priority_cache: dict[str, int] = {}


def _get_tracker_id(client: RedmineClient, name: str) -> Optional[int]:
    if name not in _tracker_cache:
        tid = client.get_tracker_id("", name)   # project 무관 전역 조회
        if tid:
            _tracker_cache[name] = tid
    return _tracker_cache.get(name)


def _get_status_id(client: RedmineClient, name: str) -> Optional[int]:
    if name not in _status_cache:
        sid = client.get_issue_status_id(name)
        if sid:
            _status_cache[name] = sid
    return _status_cache.get(name)


def _get_priority_id(client: RedmineClient, name: str) -> Optional[int]:
    if name not in _priority_cache:
        r = client.session.get(f"{client.base}/enumerations/issue_priorities.json")
        r.raise_for_status()
        for p in r.json().get("issue_priorities", []):
            _priority_cache[p["name"]] = p["id"]
    return _priority_cache.get(name)


# ── 필드 빌더 ────────────────────────────────────────────────────────────────

def _build_custom_fields(meta: dict, cfg: dict) -> list[dict]:
    """config의 custom field ID 매핑 기반으로 custom_fields 리스트 생성."""
    cf_cfg = cfg.get("redmine_custom_fields", {})
    fields = []

    def _add(key: str, value):
        fid = cf_cfg.get(key)
        if fid and value is not None:
            fields.append({"id": fid, "value": str(value)})

    _add("doc_id",    meta.get("doc_id"))
    _add("version",   meta.get("version"))
    _add("retention", meta.get("retention"))

    standards = meta.get("standards", [])
    if standards:
        _add("standards", ", ".join(standards))

    return fields


def _build_subject(meta: dict, doc_id: str) -> str:
    title = meta.get("title", doc_id)
    doc_type = meta.get("type", "").upper()

    if "NCR" in doc_id.upper():
        severity = meta.get("severity", "")
        finding  = meta.get("finding_id", "")
        sev_label = {"critical": "[긴급]", "major": "[높음]", "minor": "[보통]"}.get(severity, "")
        return f"{sev_label} [{doc_id}] {title}"

    return f"[{doc_id}] {title}"


def _build_due_date(meta: dict) -> Optional[str]:
    """sla_due_date (NCR) 또는 event_date (REC) → YYYY-MM-DD."""
    for key in ("sla_due_date", "due_date", "event_date"):
        val = meta.get(key)
        if val:
            return str(val)[:10]
    return None


# ── 메인 동기화 함수 ──────────────────────────────────────────────────────────

def sync_issue(doc_id: str, post, meta: dict, project_id: str,
               vault_path: str, client: RedmineClient, cfg: dict,
               dry_run: bool = False) -> dict:
    """REC / REC-NCR 1건을 Redmine Issue로 동기화."""

    is_ncr     = "NCR" in doc_id.upper()
    vault_status = meta.get("status", "open" if is_ncr else "final")
    tracker_name = cfg["issue_trackers"].get(
        "REC-NCR" if is_ncr else "REC",
        "프로세스기록"
    )

    subject    = _build_subject(meta, doc_id)
    body       = transform(post.content, meta, vault_path)
    due_date   = _build_due_date(meta)
    custom_fields = _build_custom_fields(meta, cfg)

    redmine_status_name = STATUS_MAP.get(vault_status, "진행중" if is_ncr else "완료")
    priority_name       = PRIORITY_MAP.get(meta.get("severity", ""), DEFAULT_PRIORITY) if is_ncr else None

    if dry_run:
        return {
            "doc_id": doc_id, "status": "dry-run",
            "redmine_type": "issue",
            "redmine_project": project_id,
            "tracker": tracker_name,
            "redmine_status": redmine_status_name,
            "priority": priority_name,
            "due_date": due_date,
        }

    # 트래커 ID
    tracker_id = _get_tracker_id(client, tracker_name)
    if not tracker_id:
        return {"doc_id": doc_id, "status": "error",
                "reason": f"tracker '{tracker_name}' not found in Redmine"}

    # 상태 ID
    status_id = _get_status_id(client, redmine_status_name)

    # 우선순위 ID
    priority_id = _get_priority_id(client, priority_name) if priority_name else None

    # 기존 Issue 조회 (DB 우선, 없으면 custom field 검색)
    existing = _find_existing_issue(doc_id, project_id, client, cfg)

    if existing:
        _update_existing(client, existing, subject, body, status_id,
                         priority_id, due_date, custom_fields, doc_id)
        action = "updated"
        resource = str(existing["id"])
    else:
        issue = _create_new(client, project_id, subject, tracker_id,
                            body, status_id, priority_id, due_date, custom_fields)
        action = "created"
        resource = str(issue["id"])

    now = datetime.now(timezone.utc).isoformat()
    upsert_sync(
        vault_doc_id=doc_id,
        vault_path=vault_path,
        redmine_type="issue",
        redmine_project_id=project_id,
        redmine_resource=resource,
        vault_version=str(meta.get("version", "")),
        synced_at=now,
    )

    return {
        "doc_id": doc_id, "status": action,
        "redmine_type": "issue",
        "redmine_project": project_id,
        "redmine_resource": resource,
        "tracker": tracker_name,
        "redmine_status": redmine_status_name,
    }


# ── 내부 헬퍼 ─────────────────────────────────────────────────────────────────

def _find_existing_issue(doc_id: str, project_id: str,
                          client: RedmineClient, cfg: dict) -> Optional[dict]:
    """DB sync_map 우선, 없으면 Redmine custom field로 검색."""
    existing_row = get_sync(doc_id)
    if existing_row and existing_row["redmine_type"] == "issue":
        try:
            r = client.session.get(
                f"{client.base}/issues/{existing_row['redmine_resource']}.json"
            )
            if r.status_code == 200:
                return r.json()["issue"]
        except Exception:
            pass

    # fallback: custom field 검색
    cf_id = cfg.get("redmine_custom_fields", {}).get("doc_id")
    if cf_id:
        return client.find_issue_by_custom_field(project_id, cf_id, doc_id)

    return None


def _create_new(client: RedmineClient, project_id: str, subject: str,
                tracker_id: int, description: str,
                status_id: Optional[int], priority_id: Optional[int],
                due_date: Optional[str], custom_fields: list) -> dict:
    payload: dict = {
        "project_id": project_id,
        "subject": subject,
        "tracker_id": tracker_id,
        "description": description,
    }
    if status_id:
        payload["status_id"] = status_id
    if priority_id:
        payload["priority_id"] = priority_id
    if due_date:
        payload["due_date"] = due_date
    if custom_fields:
        payload["custom_fields"] = custom_fields

    r = client.session.post(f"{client.base}/issues.json", json={"issue": payload})
    r.raise_for_status()
    return r.json()["issue"]


def _update_existing(client: RedmineClient, issue: dict, subject: str,
                     description: str, status_id: Optional[int],
                     priority_id: Optional[int], due_date: Optional[str],
                     custom_fields: list, doc_id: str) -> None:
    payload: dict = {
        "subject": subject,
        "description": description,
        "notes": f"processware vault 자동 갱신 — {doc_id} ({datetime.now().strftime('%Y-%m-%d')})",
    }
    if status_id:
        payload["status_id"] = status_id
    if priority_id:
        payload["priority_id"] = priority_id
    if due_date:
        payload["due_date"] = due_date
    if custom_fields:
        payload["custom_fields"] = custom_fields

    r = client.session.put(
        f"{client.base}/issues/{issue['id']}.json",
        json={"issue": payload},
    )
    r.raise_for_status()
