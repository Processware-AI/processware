"""traceability-mapper — 추적성 매트릭스 생성 에이전트."""

from ..base import BaseAgent

_SYSTEM = """당신은 컴플라이언스 추적성 분석가다.
생성된 POL/PRO/WI/TMP 문서 목록과 요구사항 목록을 받아 추적성 매트릭스를 생성한다.

출력 형식 (JSON):
{
  "traceability": [
    {
      "req_id": "REQ-001",
      "clause": "4.1",
      "statement": "...",
      "pol_id": "POL-QMS-01",
      "pro_ids": ["PRO-QMS-01-01"],
      "wi_ids": ["WI-QMS-01-01-01"],
      "tmp_ids": ["TMP-QMS-01-01-01-01"],
      "coverage": "full"
    }
  ],
  "summary": {
    "total_requirements": 25,
    "full_coverage": 20,
    "partial_coverage": 3,
    "no_coverage": 2
  }
}

coverage 값: full / partial / none
반드시 유효한 JSON만 출력.
"""


class TraceabilityMapperAgent(BaseAgent):
    name = "traceability-mapper"

    def execute(self, inputs: dict, run_id: str = None) -> dict:
        standard = inputs.get("standard", "")
        scope_code = inputs.get("scope_code", "GEN")
        requirements = inputs.get("requirements", [])
        designed_docs = inputs.get("designed_documents", [])
        wi_docs = inputs.get("wi_documents", [])
        tmp_docs = inputs.get("tmp_documents", [])

        all_docs = designed_docs + wi_docs + tmp_docs
        doc_summary = "\n".join(
            f"- {d['doc_id']} ({d['doc_type']}): {d['title']}"
            for d in all_docs
        )
        req_summary = "\n".join(
            f"- {r.get('req_id', '')}: [{r.get('clause', '')}] {r.get('statement', '')[:100]}"
            for r in requirements[:30]
        )

        raw = self.call_llm(
            _SYSTEM,
            f"""표준: {standard}
영역: {scope_code}

생성된 문서 목록:
{doc_summary}

요구사항 목록:
{req_summary}

각 요구사항이 어느 POL/PRO/WI/TMP에 의해 충족되는지 매핑하라.""",
            max_tokens=8096,
        )

        import json, re
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            m = re.search(r'\{.*\}', raw, re.DOTALL)
            data = json.loads(m.group()) if m else {"traceability": [], "summary": {}}

        traceability = data.get("traceability", [])
        summary = data.get("summary", {})

        lines = [f"# {standard} 추적성 매트릭스\n"]
        lines.append(f"표준: {standard} | 영역: {scope_code}\n")
        lines.append(f"## 커버리지 요약\n")
        lines.append(f"- 전체 요구사항: {summary.get('total_requirements', len(requirements))}")
        lines.append(f"- 완전 충족: {summary.get('full_coverage', 0)}")
        lines.append(f"- 부분 충족: {summary.get('partial_coverage', 0)}")
        lines.append(f"- 미충족: {summary.get('no_coverage', 0)}\n")
        lines.append("## 요구사항별 추적성\n")
        lines.append("| REQ-ID | 조항 | POL | PRO | WI | TMP | 충족도 |")
        lines.append("|--------|------|-----|-----|----|-----|--------|")
        for t in traceability:
            pro_str = ", ".join(t.get("pro_ids", []))
            wi_str = ", ".join(t.get("wi_ids", []))
            tmp_str = ", ".join(t.get("tmp_ids", []))
            cov = {"full": "✅", "partial": "🟡", "none": "⛔"}.get(t.get("coverage", "none"), "⛔")
            lines.append(f"| {t.get('req_id','')} | {t.get('clause','')} | {t.get('pol_id','')} | {pro_str} | {wi_str} | {tmp_str} | {cov} |")

        content = "\n".join(lines)

        from tools.vault_rules import next_seq, generate_filename
        seq = next_seq("MAT", scope_code, None)
        doc_id = f"MAT-{seq:03d}"
        slug = standard.replace(" ", "").replace("/", "").replace(":", "").lower()
        filename = generate_filename(doc_id, f"{slug}_추적성", "0.1")

        self.save_document(
            run_id=run_id,
            doc_id=doc_id,
            doc_type="MAT",
            scope_code=scope_code,
            title=f"{standard} 추적성 매트릭스",
            content=content,
            meta={
                "doc_id": doc_id,
                "filename": filename,
                "standard": standard,
                "coverage_summary": summary,
            },
        )

        return {
            "traceability_matrix": traceability,
            "coverage_summary": summary,
            "mat_doc_id": doc_id,
        }
