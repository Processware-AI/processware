"""Base agent class — wraps Claude API for all processmine agents."""

from abc import ABC, abstractmethod
from typing import Any

import anthropic

from ..config import settings
from ..core.db import session_scope


class BaseAgent(ABC):
    """
    All processmine agents inherit from this.
    Each agent:
      1. Receives structured input (dict)
      2. Calls Claude API (one or more turns)
      3. Writes results to DB
      4. Returns structured output (dict)
    """

    name: str = "base"
    model: str = settings.model

    def __init__(self):
        self._client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

    # ── Public ────────────────────────────────────────────────────────────────

    def run(self, inputs: dict, run_id: str = None) -> dict:
        return self.execute(inputs, run_id=run_id)

    @abstractmethod
    def execute(self, inputs: dict, run_id: str = None) -> dict:
        """Subclasses implement the agent logic here."""

    # ── Claude API helpers ────────────────────────────────────────────────────

    def call_llm(self, system: str, user: str,
                 max_tokens: int = 8096) -> str:
        response = self._client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return response.content[0].text

    def call_llm_with_tools(self, system: str, messages: list,
                            tools: list, max_tokens: int = 8096) -> dict:
        response = self._client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            tools=tools,
            messages=messages,
        )
        return response

    # ── DB helpers ────────────────────────────────────────────────────────────

    def save_document(self, run_id: str, doc_id: str, doc_type: str,
                      scope_code: str, title: str, content: str,
                      meta: dict, parent_doc_id: str = None,
                      version: str = "0.1", status: str = "draft"):
        from ..core.db import upsert_document
        with session_scope() as session:
            return upsert_document(
                session,
                doc_id=doc_id,
                doc_type=doc_type,
                scope_code=scope_code,
                title=title,
                version=version,
                status=status,
                content=content,
                meta=meta,
                parent_doc_id=parent_doc_id,
                run_id=run_id,
            )
