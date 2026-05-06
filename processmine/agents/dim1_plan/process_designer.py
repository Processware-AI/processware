"""process-designer — POL/PRO 생성 에이전트 (Python 포팅)."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from tools.vault_rules import new_child_id, generate_filename, next_seq

from ..base import BaseAgent

_SYSTEM = """당신은 프로세스 아키텍트(SEPG)다.
표준 요구사항 목록(REQ)을 받아 정책(POL)과 절차(PRO)를 설계한다.

출력 형식 (JSON):
{
  "documents": [
    {
      "doc_type": "POL",
      "scope_code": "...",
      "title": "...",
      "content": "# 제목\\n\\n[전체 마크다운 본문]",
      "meta": {
        "type": "POL",
        "version": "0.1",
        "status": "draft",
        "owner": "...",
        "standards": ["..."]
      }
    }
  ]
}

규칙:
- 하나의 표준에 POL 1~3개, 각 POL 하위에 PRO 2~5개
- POL: 방향성·원칙·책임만. 세부 절차 금지.
- PRO: Mermaid flowchart + RACI 표 + KPI 5개 이내 필수
- 반드시 유효한 JSON만 출력. 다른 텍스트 없음.
"""


class ProcessDesignerAgent(BaseAgent):
    name = "process-designer"

    def execute(self, inputs: dict, run_id: str = None) -> dict:
        requirements = inputs.get("requirements", [])
        scope_code = inputs.get("scope_code", "GEN")
        standard = inputs.get("standard", "")

        user_prompt = f"""표준: {standard}
영역코드: {scope_code}

요구사항 목록:
{self._format_reqs(requirements)}

위 요구사항을 커버하는 POL/PRO 문서 세트를 JSON으로 생성하라."""

        raw = self.call_llm(_SYSTEM, user_prompt, max_tokens=16000)

        import json
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            import re
            m = re.search(r'\{.*\}', raw, re.DOTALL)
            data = json.loads(m.group()) if m else {"documents": []}

        saved = []
        pol_id = None

        for doc in data.get("documents", []):
            doc_type = doc["doc_type"]
            scope = doc.get("scope_code", scope_code)

            if doc_type == "POL":
                seq = next_seq("POL", scope, None)
                doc_id = f"POL-{scope}-{seq:02d}"
                parent = None
                pol_id = doc_id
            elif doc_type == "PRO" and pol_id:
                seq = next_seq("PRO", scope, pol_id)
                doc_id = new_child_id(pol_id, "PRO", seq)
                parent = pol_id
            else:
                continue

            filename = generate_filename(doc_id, doc["title"], "0.1")
            meta = {**doc.get("meta", {}), "doc_id": doc_id, "filename": filename}

            self.save_document(
                run_id=run_id,
                doc_id=doc_id,
                doc_type=doc_type,
                scope_code=scope,
                title=doc["title"],
                content=doc["content"],
                meta=meta,
                parent_doc_id=parent,
            )
            saved.append({"doc_id": doc_id, "doc_type": doc_type, "title": doc["title"]})

        return {"designed_documents": saved, "pol_id": pol_id}

    def _format_reqs(self, reqs: list) -> str:
        if not reqs:
            return "(요구사항 없음)"
        return "\n".join(
            f"- {r.get('req_id', '')}: {r.get('statement', r)}"
            for r in reqs
        )
