"""processmine CLI — typer 기반."""

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="processmine",
    help="AI-driven process standard management",
    add_completion=False,
)
console = Console()


# ── init ──────────────────────────────────────────────────────────────────────

@app.command()
def init(
    path: str = typer.Argument(".", help="Project directory"),
):
    """Initialize a new processmine project (creates DB + config)."""
    import os
    from pathlib import Path
    from ..core.db import init_db
    from ..config import settings

    project_dir = Path(path).resolve()
    project_dir.mkdir(parents=True, exist_ok=True)
    os.chdir(project_dir)

    init_db()
    console.print(f"[green]✓[/green] processmine initialized at [bold]{project_dir}[/bold]")
    console.print(f"  DB: [dim]{settings.db_url}[/dim]")


# ── build-process ─────────────────────────────────────────────────────────────

@app.command("build-process")
def build_process(
    standard: str = typer.Argument(..., help="Standard code or name (e.g. ISO9001)"),
    scope_code: str = typer.Option("", "--scope", help="Scope code override (e.g. QMS)"),
    resume: str = typer.Option(None, "--resume", help="Resume a previous run_id"),
    requirements_file: str = typer.Option(None, "--reqs", help="Path to requirements YAML/MD"),
):
    """Run dimension-1 (Plan) pipeline — generate POL/PRO/WI/TMP/EX for a standard."""
    from ..core.db import init_db
    from ..core.orchestrator import Pipeline, PipelineStep
    from ..agents.dim1_plan import (
        StandardAnalyzerAgent,
        ProcessDesignerAgent,
        WiTmpWriterAgent,
        TraceabilityMapperAgent,
        QaReviewerAgent,
    )

    init_db()

    reqs = _load_requirements(requirements_file)
    resolved_scope = scope_code or _infer_scope(standard)

    analyzer  = StandardAnalyzerAgent()
    designer  = ProcessDesignerAgent()
    wi_writer = WiTmpWriterAgent()
    tracer    = TraceabilityMapperAgent()
    reviewer  = QaReviewerAgent()

    pipeline = Pipeline(
        name="build-process",
        steps=[
            PipelineStep(
                name="standard-analyzer",
                description="표준 요구사항 분해",
                agent_fn=lambda ctx, rid: analyzer.run(ctx, run_id=rid),
            ),
            PipelineStep(
                name="process-designer",
                description="POL/PRO 설계",
                agent_fn=lambda ctx, rid: designer.run(ctx, run_id=rid),
            ),
            PipelineStep(
                name="wi-tmp-writer",
                description="WI/TMP/EX 생성",
                agent_fn=lambda ctx, rid: wi_writer.run(ctx, run_id=rid),
            ),
            PipelineStep(
                name="traceability-mapper",
                description="추적성 매트릭스 생성",
                agent_fn=lambda ctx, rid: tracer.run(ctx, run_id=rid),
            ),
            PipelineStep(
                name="qa-reviewer",
                description="품질 검토",
                agent_fn=lambda ctx, rid: reviewer.run(ctx, run_id=rid),
            ),
        ],
    )

    inputs = {
        "standard": standard,
        "scope_code": resolved_scope,
        "requirements": reqs,
    }

    result = pipeline.run(inputs, resume_run_id=resume)
    _print_summary(result)


# ── list ──────────────────────────────────────────────────────────────────────

@app.command("list")
def list_documents(
    doc_type: str = typer.Option(None, "--type", help="Filter by doc type"),
    scope_code: str = typer.Option(None, "--scope", help="Filter by scope code"),
):
    """List documents stored in the DB."""
    from ..core.db import list_documents as db_list, session_scope

    with session_scope() as session:
        docs = db_list(session, doc_type=doc_type, scope_code=scope_code)

    table = Table(title="Documents", show_lines=False)
    table.add_column("doc_id", style="cyan")
    table.add_column("type")
    table.add_column("scope")
    table.add_column("title")
    table.add_column("version")
    table.add_column("status")

    for d in docs:
        table.add_row(d.doc_id, d.doc_type, d.scope_code or "",
                      d.title, d.version, d.status)

    console.print(table)


# ── export ────────────────────────────────────────────────────────────────────

@app.command()
def export(
    output_dir: str = typer.Option("./export", "--out", help="Output directory"),
    scope_code: str = typer.Option(None, "--scope", help="Filter by scope code"),
    doc_type: str = typer.Option(None, "--type", help="Filter by doc type"),
):
    """Export documents from DB to .md files."""
    from pathlib import Path
    from ..core.db import list_documents as db_list, session_scope
    from tools.vault_rules import FOLDER_MAP

    out = Path(output_dir)

    with session_scope() as session:
        docs = db_list(session, doc_type=doc_type, scope_code=scope_code)

    count = 0
    for doc in docs:
        folder_name = FOLDER_MAP.get(doc.doc_type, "misc")
        folder = out / folder_name
        folder.mkdir(parents=True, exist_ok=True)

        filename = doc.meta.get("filename") or f"{doc.doc_id}_{doc.title}_v{doc.version}.md"
        path = folder / filename
        path.write_text(doc.content or "", encoding="utf-8")
        count += 1

    console.print(f"[green]✓[/green] Exported {count} documents to [bold]{out}[/bold]")


# ── Helpers ───────────────────────────────────────────────────────────────────

def _load_requirements(path: str | None) -> list:
    if not path:
        return []
    import yaml
    from pathlib import Path
    text = Path(path).read_text(encoding="utf-8")
    data = yaml.safe_load(text)
    if isinstance(data, list):
        return data
    return data.get("requirements", [])


def _infer_scope(standard: str) -> str:
    mapping = {
        "ISO9001": "QMS", "ISO 9001": "QMS",
        "ISO27001": "ISMS", "ISO/IEC 27001": "ISMS",
        "ISO27701": "PIMS",
        "ISO14001": "EMS",
        "ISO45001": "OHSMS",
        "ISO20000": "ITSM",
        "ISO22301": "BCMS",
        "ISO42001": "AIMS",
        "CMMI": "CMMI",
        "IATF16949": "AUTO",
        "ISO13485": "MDQMS",
    }
    for key, scope in mapping.items():
        if key.replace(" ", "").upper() in standard.replace(" ", "").upper():
            return scope
    return "GEN"


def _print_summary(result: dict):
    all_docs = (
        result.get("designed_documents", [])
        + result.get("wi_documents", [])
        + result.get("tmp_documents", [])
    )
    if not all_docs:
        return
    table = Table(title="Generated Documents")
    table.add_column("doc_id", style="cyan")
    table.add_column("type")
    table.add_column("title")
    for d in all_docs:
        table.add_row(d["doc_id"], d["doc_type"], d["title"])

    qa_result = result.get("qa_result", "")
    score = result.get("qa_score", {}).get("overall", "")
    mat_id = result.get("mat_doc_id", "")
    console.print(table)
    if qa_result:
        color = "green" if qa_result == "pass" else "yellow" if "conditional" in qa_result else "red"
        console.print(f"\n[{color}]QA: {qa_result.upper()}[/{color}]"
                      + (f"  (score: {score})" if score else "")
                      + (f"  traceability: {mat_id}" if mat_id else ""))


if __name__ == "__main__":
    app()
