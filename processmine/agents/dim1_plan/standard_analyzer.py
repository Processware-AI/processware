"""standard-analyzer — 표준 요구사항 분해 에이전트."""

from ..base import BaseAgent

_SYSTEM = """당신은 ISO/IEC·KS 표준 분석 전문 컨설턴트다.
표준명을 입력받아 요구사항 목록을 추출한다.

출력 형식 (JSON):
{
  "standard_name": "ISO 9001:2015",
  "scope_code": "QMS",
  "layer": "L1_management",
  "structure": "HLS",
  "requirements": [
    {
      "req_id": "REQ-001",
      "clause": "4.1",
      "statement": "조직은 조직의 목적과 전략적 방향에 관련 있는 외부 및 내부 이슈를 결정해야 한다.",
      "level": "shall",
      "category": "context"
    }
  ]
}

규칙:
- req_id: REQ-{NNN} (001부터 순번)
- clause: 표준 조항 번호 (4.1, 5.1.1 등)
- level: shall / should / may 중 하나
- category: context / leadership / planning / support / operation / performance / improvement 중 하나
- 반드시 유효한 JSON만 출력. 다른 텍스트 없음.
- requirements 는 최소 20개 이상 추출
"""


class StandardAnalyzerAgent(BaseAgent):
    name = "standard-analyzer"

    def execute(self, inputs: dict, run_id: str = None) -> dict:
        standard = inputs.get("standard", "")
        scope_code = inputs.get("scope_code", "GEN")

        user_prompt = f"""표준: {standard}
영역코드: {scope_code}

이 표준의 주요 요구사항을 JSON 형식으로 추출하라.
shall 요건을 우선 포함하고, 실무적으로 중요한 조항을 빠짐없이 포함하라."""

        raw = self.call_llm(_SYSTEM, user_prompt, max_tokens=8096)

        import json, re
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            m = re.search(r'\{.*\}', raw, re.DOTALL)
            data = json.loads(m.group()) if m else {"requirements": []}

        requirements = data.get("requirements", [])

        import yaml
        content = f"""# {standard} 요구사항 분석

표준: {data.get('standard_name', standard)}
영역: {data.get('scope_code', scope_code)}
계층: {data.get('layer', 'L1_management')}
구조: {data.get('structure', 'HLS')}

## 요구사항 목록

{yaml.dump(requirements, allow_unicode=True, default_flow_style=False)}
"""

        from tools.vault_rules import next_seq, generate_filename
        scope = data.get("scope_code", scope_code)
        seq = next_seq("REF", scope, None)
        doc_id = f"REF-{scope}-{seq:02d}"
        filename = generate_filename(doc_id, f"{standard}_요구사항분석", "0.1")

        self.save_document(
            run_id=run_id,
            doc_id=doc_id,
            doc_type="REF",
            scope_code=scope,
            title=f"{standard} 요구사항 분석",
            content=content,
            meta={
                "doc_id": doc_id,
                "filename": filename,
                "standard": standard,
                "layer": data.get("layer"),
                "structure": data.get("structure"),
                "req_count": len(requirements),
            },
        )

        return {
            "requirements": requirements,
            "scope_code": scope,
            "standard_meta": {
                "layer": data.get("layer"),
                "structure": data.get("structure"),
            },
            "ref_doc_id": doc_id,
        }
