"""Redmine REST API 래퍼 — Project / Wiki / Issue CRUD."""

from __future__ import annotations

import os
import time
import requests
from typing import Optional


class RedmineClient:
    def __init__(self, url: str, api_key: str):
        self.base = url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "X-Redmine-API-Key": api_key,
            "Content-Type": "application/json",
        })

    # ── 프로젝트 ──────────────────────────────────────────────

    def get_project(self, identifier: str) -> Optional[dict]:
        r = self.session.get(f"{self.base}/projects/{identifier}.json")
        if r.status_code == 404:
            return None
        r.raise_for_status()
        return r.json()["project"]

    def create_project(self, identifier: str, name: str,
                       parent_id: Optional[int] = None,
                       description: str = "") -> dict:
        payload = {"project": {
            "identifier": identifier,
            "name": name,
            "description": description,
            "is_public": False,
        }}
        if parent_id:
            payload["project"]["parent_id"] = parent_id
        r = self.session.post(f"{self.base}/projects.json", json=payload)
        r.raise_for_status()
        return r.json()["project"]

    def get_or_create_project(self, identifier: str, name: str,
                               parent_id: Optional[int] = None,
                               description: str = "") -> tuple[dict, bool]:
        """(project_dict, created) 반환. created=True면 신규 생성."""
        existing = self.get_project(identifier)
        if existing:
            return existing, False
        return self.create_project(identifier, name, parent_id, description), True

    # ── Wiki ──────────────────────────────────────────────────

    def get_wiki_page(self, project_id: str, title: str) -> Optional[dict]:
        r = self.session.get(
            f"{self.base}/projects/{project_id}/wiki/{title}.json"
        )
        if r.status_code == 404:
            return None
        r.raise_for_status()
        return r.json()["wiki_page"]

    def upsert_wiki_page(self, project_id: str, title: str,
                         text: str, parent_title: Optional[str] = None) -> dict:
        """페이지가 없으면 생성, 있으면 업데이트 (PUT은 양쪽 모두 처리)."""
        payload: dict = {"wiki_page": {"text": text}}
        if parent_title:
            payload["wiki_page"]["parent_title"] = parent_title
        r = self.session.put(
            f"{self.base}/projects/{project_id}/wiki/{title}.json",
            json=payload,
        )
        r.raise_for_status()
        # PUT /wiki/:title 은 200(update) 또는 201(create) 반환
        return {"project_id": project_id, "title": title, "status": r.status_code}

    def list_wiki_pages(self, project_id: str) -> list[dict]:
        r = self.session.get(f"{self.base}/projects/{project_id}/wiki/index.json")
        r.raise_for_status()
        return r.json().get("wiki_pages", [])

    # ── Issue ─────────────────────────────────────────────────

    def get_tracker_id(self, project_id: str, tracker_name: str) -> Optional[int]:
        r = self.session.get(f"{self.base}/trackers.json")
        r.raise_for_status()
        for t in r.json().get("trackers", []):
            if t["name"] == tracker_name:
                return t["id"]
        return None

    def get_issue_status_id(self, status_name: str) -> Optional[int]:
        r = self.session.get(f"{self.base}/issue_statuses.json")
        r.raise_for_status()
        for s in r.json().get("issue_statuses", []):
            if s["name"] == status_name:
                return s["id"]
        return None

    def find_issue_by_custom_field(self, project_id: str,
                                   field_id: int, value: str) -> Optional[dict]:
        r = self.session.get(
            f"{self.base}/issues.json",
            params={"project_id": project_id, "cf_{field_id}": value, "limit": 1},
        )
        r.raise_for_status()
        issues = r.json().get("issues", [])
        return issues[0] if issues else None

    def create_issue(self, project_id: str, subject: str, tracker_id: int,
                     description: str = "", status_id: Optional[int] = None,
                     custom_fields: Optional[list] = None) -> dict:
        payload: dict = {"issue": {
            "project_id": project_id,
            "subject": subject,
            "tracker_id": tracker_id,
            "description": description,
        }}
        if status_id:
            payload["issue"]["status_id"] = status_id
        if custom_fields:
            payload["issue"]["custom_fields"] = custom_fields
        r = self.session.post(f"{self.base}/issues.json", json=payload)
        r.raise_for_status()
        return r.json()["issue"]

    def update_issue(self, issue_id: int, subject: Optional[str] = None,
                     description: Optional[str] = None,
                     status_id: Optional[int] = None,
                     custom_fields: Optional[list] = None) -> None:
        payload: dict = {"issue": {}}
        if subject:
            payload["issue"]["subject"] = subject
        if description is not None:
            payload["issue"]["description"] = description
        if status_id:
            payload["issue"]["status_id"] = status_id
        if custom_fields:
            payload["issue"]["custom_fields"] = custom_fields
        r = self.session.put(f"{self.base}/issues/{issue_id}.json", json=payload)
        r.raise_for_status()

    # ── 유틸 ──────────────────────────────────────────────────

    def ping(self) -> bool:
        """접속 확인. True = 성공."""
        try:
            r = self.session.get(f"{self.base}/users/current.json", timeout=5)
            return r.status_code == 200
        except requests.RequestException:
            return False

    def _retry(self, fn, retries: int = 3, delay: float = 2.0):
        for attempt in range(retries):
            try:
                return fn()
            except requests.HTTPError as e:
                if attempt == retries - 1 or e.response.status_code < 500:
                    raise
                time.sleep(delay)


def client_from_config(cfg: dict) -> RedmineClient:
    url = cfg["redmine"]["url"]
    api_key = cfg["redmine"]["api_key"]
    if api_key.startswith("${") and api_key.endswith("}"):
        env_var = api_key[2:-1]
        api_key = os.environ.get(env_var, "")
    return RedmineClient(url, api_key)
