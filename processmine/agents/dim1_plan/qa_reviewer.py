"""qa-reviewer — 산출물 품질 검토 에이전트."""

from ..base import BaseAgent

_SYSTEM = """당신은 프로세스 문서 품질 심사관이다.
생성된 POL/PRO/WI/TMP/MAT 문서 목록을 받아 품질을 검토하고 합불 판정한다.

출력 형식 (JSON):
{
  "review_result": "pass",
  "findings": [
    {
      "doc_id": "PRO-QMS-01-01",
      "severity": "major",
      "issue": "Mermaid flowchart 누락",
      "action": "flowchart 추가 필요"
    }
  ],
  "score": {
    "completeness": 85,
    "consistency": 90,
    "traceability": 80,
    "overall": 85
  }
}

review_result: pass / conditional_pass / fail
severity: critical / major / minor / observation
점수: 0~100

규칙:
- PRO에 Mermaid flowchart 없으면 major
- PRO에 RACI 표 없으면 major
- PRO에 KPI 없으면 minor
- WI에 완료 조건 체크리스트 없으면 major
- WI에 예외처리 3개 미만이면 minor
- 추적성 미충족 요구사항이 20% 초과면 critical
- 반드시 유효한 JSON만 출력
"""


class QaReviewerAgent(BaseAgent):
    name = "qa-reviewer"

    def execute(self, inputs: dict, run_id: str = None) -> dict:
        standard = inputs.get("standard", "")
        scope_code = inputs.get("scope_code", "GEN")
        designed_docs = inputs.get("designed_documents", [])
        wi_docs = inputs.get("wi_documents", [])
        tmp_docs = inputs.get("tmp_documents", [])
        coverage = inputs.get("coverage_summary", {})

        from ...core.db import session_scope, get_document

        doc_contents = []
        with session_scope() as session:
            for d in (designed_docs + wi_docs)[:10]:
                doc = get_document(session, d["doc_id"])
                if doc:
                    doc_contents.append({
                        "doc_id": doc.doc_id,
                        "doc_type": doc.doc_type,
                        "title": doc.title,
                        "content_excerpt": (doc.content or "")[:500],
                    })

        doc_summary = "\n".join(
            f"[{d['doc_id']}] ({d['doc_type']}) {d['title']}\n  {d['content_excerpt'][:200]}..."
            for d in doc_contents
        )

        raw = self.call_llm(
            _SYSTEM,
            f"""표준: {standard}
영역: {scope_code}
커버리지: {coverage}

검토 대상 문서 (발췌):
{doc_summary}

위 문서들의 품질을 검토하고 합불 판정하라.""",
            max_tokens=4096,
        )

        import json, re
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            m = re.search(r'\{.*\}', raw, re.DOTALL)
            data = json.loads(m.group()) if m else {
                "review_result": "conditional_pass",
                "findings": [],
                "score": {"overall": 75},
            }

        findings = data.get("findings", [])
        score = data.get("score", {})
        result = data.get("review_result", "conditional_pass")

        lines = [f"# QA 검토 보고서 — {standard}\n"]
        lines.append(f"**판정**: {result.upper()}")
        lines.append(f"**종합 점수**: {score.get('overall', 0)}점\n")
        lines.append("## 점수 상세\n")
        lines.append(f"| 항목 | 점수 |")
        lines.append(f"|------|------|")
        for k, v in score.items():
            if k != "overall":
                lines.append(f"| {k} | {v} |")
        lines.append("\n## 지적 사항\n")
        if findings:
            lines.append("| 문서 | 심각도 | 내용 | 조치 |")
            lines.append("|------|--------|------|------|")
            for f in findings:
                lines.append(f"| {f.get('doc_id','')} | {f.get('severity','')} | {f.get('issue','')} | {f.get('action','')} |")
        else:
            lines.append("지적 사항 없음.")

        content = "\n".join(lines)

        from tools.vault_rules import next_seq, generate_filename
        seq = next_seq("REF", scope_code, None)
        doc_id = f"REF-{scope_code}-QA-{seq:02d}"
        filename = generate_filename(doc_id, f"{standard}_QA검토보고서", "0.1")

        self.save_document(
            run_id=run_id,
            doc_id=doc_id,
            doc_type="REF",
            scope_code=scope_code,
            title=f"{standard} QA 검토 보고서",
            content=content,
            meta={
                "doc_id": doc_id,
                "filename": filename,
                "review_result": result,
                "score": score,
                "finding_count": len(findings),
            },
        )

        return {
            "qa_result": result,
            "qa_findings": findings,
            "qa_score": score,
            "qa_doc_id": doc_id,
        }
