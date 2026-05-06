"""wi-tmp-writer — WI/TMP/EX 생성 에이전트."""

from ..base import BaseAgent

_SYSTEM_WI = """당신은 품질문서 작성 전문가다.
PRO(절차서) 정보를 받아 업무지침서(WI)를 생성한다.

출력 형식 (JSON):
{
  "wi_documents": [
    {
      "pro_id": "PRO-QMS-01-01",
      "title": "...",
      "content": "# 제목\\n\\n[전체 마크다운 본문]",
      "meta": {
        "type": "WI",
        "version": "0.1",
        "status": "draft",
        "owner": "..."
      }
    }
  ]
}

WI 구조:
1. 목적 및 적용범위
2. 참조문서
3. 용어 정의
4. 역할 및 책임
5. 절차 (단계별 상세)
   5.1 입력 조건
   5.2 처리 단계 (번호 매긴 상세 지침)
   5.3 완료 조건 체크리스트
6. 예외 처리 (3개 이상)
7. 기록 및 증적
8. 연계 템플릿
9. 개정 이력

규칙:
- 능동형 문체 사용 ("한다", "확인한다", "기록한다")
- 각 단계는 구체적이고 실행 가능한 지침
- 반드시 유효한 JSON만 출력
"""

_SYSTEM_TMP = """당신은 품질문서 양식 설계 전문가다.
WI(업무지침서)의 §8 연계 템플릿 정보를 받아 TMP(빈 양식)와 EX(작성 예시)를 생성한다.

출력 형식 (JSON):
{
  "tmp_documents": [
    {
      "wi_id": "WI-QMS-01-01-01",
      "tmp_title": "...",
      "tmp_content": "# 양식명\\n\\n[빈 양식 마크다운]",
      "ex_content": "# 작성예시: 양식명\\n\\n[실제 데이터로 채운 예시]"
    }
  ]
}

규칙:
- TMP: 필드명만 있는 빈 양식 (실제 데이터 없음)
- EX: TMP를 실제 데이터로 채운 예시
- 반드시 유효한 JSON만 출력
"""


class WiTmpWriterAgent(BaseAgent):
    name = "wi-tmp-writer"

    def execute(self, inputs: dict, run_id: str = None) -> dict:
        scope_code = inputs.get("scope_code", "GEN")
        designed_docs = inputs.get("designed_documents", [])

        from ...core.db import session_scope, get_document

        pro_docs = []
        with session_scope() as session:
            for d in designed_docs:
                if d["doc_type"] == "PRO":
                    doc = get_document(session, d["doc_id"])
                    if doc:
                        pro_docs.append({
                            "doc_id": doc.doc_id,
                            "title": doc.title,
                            "content": (doc.content or "")[:2000],
                        })

        if not pro_docs:
            return {"wi_documents": [], "tmp_documents": []}

        pro_summary = "\n".join(
            f"- {d['doc_id']}: {d['title']}\n  내용 요약: {d['content'][:300]}..."
            for d in pro_docs
        )

        wi_raw = self.call_llm(
            _SYSTEM_WI,
            f"영역코드: {scope_code}\n\n대상 PRO 목록:\n{pro_summary}\n\n각 PRO에 대한 WI를 생성하라.",
            max_tokens=16000,
        )

        import json, re
        try:
            wi_data = json.loads(wi_raw)
        except json.JSONDecodeError:
            m = re.search(r'\{.*\}', wi_raw, re.DOTALL)
            wi_data = json.loads(m.group()) if m else {"wi_documents": []}

        from tools.vault_rules import next_seq, new_child_id, generate_filename

        saved_wi = []
        pol_id_cache = {}

        for wi in wi_data.get("wi_documents", []):
            pro_id = wi.get("pro_id", "")
            if not pro_id:
                continue

            parts = pro_id.split("-")
            if len(parts) >= 4:
                pol_id = f"{parts[0]}-{parts[1]}-{parts[2]}"
            else:
                continue

            seq = next_seq("WI", scope_code, pro_id)
            doc_id = new_child_id(pro_id, "WI", seq)
            filename = generate_filename(doc_id, wi["title"], "0.1")
            meta = {**wi.get("meta", {}), "doc_id": doc_id, "filename": filename, "parent_pro": pro_id}

            self.save_document(
                run_id=run_id,
                doc_id=doc_id,
                doc_type="WI",
                scope_code=scope_code,
                title=wi["title"],
                content=wi["content"],
                meta=meta,
                parent_doc_id=pro_id,
            )
            saved_wi.append({"doc_id": doc_id, "doc_type": "WI", "title": wi["title"], "pro_id": pro_id})

        tmp_raw = self.call_llm(
            _SYSTEM_TMP,
            f"영역코드: {scope_code}\n\n생성된 WI 목록:\n" +
            "\n".join(f"- {w['doc_id']}: {w['title']}" for w in saved_wi) +
            "\n\n각 WI에 대한 TMP와 EX를 생성하라.",
            max_tokens=16000,
        )

        try:
            tmp_data = json.loads(tmp_raw)
        except json.JSONDecodeError:
            m = re.search(r'\{.*\}', tmp_raw, re.DOTALL)
            tmp_data = json.loads(m.group()) if m else {"tmp_documents": []}

        saved_tmp = []
        for tmp in tmp_data.get("tmp_documents", []):
            wi_id = tmp.get("wi_id", "")
            if not wi_id:
                continue

            tmp_seq = next_seq("TMP", scope_code, wi_id)
            tmp_id = new_child_id(wi_id, "TMP", tmp_seq)
            tmp_filename = generate_filename(tmp_id, tmp["tmp_title"], "0.1")

            self.save_document(
                run_id=run_id,
                doc_id=tmp_id,
                doc_type="TMP",
                scope_code=scope_code,
                title=tmp["tmp_title"],
                content=tmp["tmp_content"],
                meta={"doc_id": tmp_id, "filename": tmp_filename, "parent_wi": wi_id},
                parent_doc_id=wi_id,
            )
            saved_tmp.append({"doc_id": tmp_id, "doc_type": "TMP", "title": tmp["tmp_title"]})

            if tmp.get("ex_content"):
                ex_seq = next_seq("EX", scope_code, tmp_id)
                ex_id = new_child_id(tmp_id, "EX", ex_seq)
                ex_filename = generate_filename(ex_id, f"{tmp['tmp_title']}_예시", "0.1")
                self.save_document(
                    run_id=run_id,
                    doc_id=ex_id,
                    doc_type="EX",
                    scope_code=scope_code,
                    title=f"{tmp['tmp_title']} 작성예시",
                    content=tmp["ex_content"],
                    meta={"doc_id": ex_id, "filename": ex_filename, "parent_tmp": tmp_id},
                    parent_doc_id=tmp_id,
                )
                saved_tmp.append({"doc_id": ex_id, "doc_type": "EX", "title": f"{tmp['tmp_title']} 작성예시"})

        return {"wi_documents": saved_wi, "tmp_documents": saved_tmp}
