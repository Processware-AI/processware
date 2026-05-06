"""Pipeline orchestrator — runs agent sequences with checkpoint/resume."""

import uuid
from dataclasses import dataclass, field
from typing import Callable

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from .db import create_run, get_run, update_run_checkpoint, session_scope
from ..config import settings

console = Console()


@dataclass
class PipelineStep:
    name: str
    agent_fn: Callable[[dict, str], dict]
    description: str = ""


class Pipeline:
    """Ordered sequence of agent steps with checkpoint/resume support."""

    def __init__(self, name: str, steps: list[PipelineStep]):
        self.name = name
        self.steps = steps

    def run(self, inputs: dict, resume_run_id: str = None) -> dict:
        run_id = resume_run_id or str(uuid.uuid4())[:8]

        with session_scope() as session:
            run = get_run(session, run_id)
            if run is None:
                run = create_run(session, run_id=run_id,
                                 command=self.name, args=inputs)
                start_step = 0
            else:
                start_step = run.checkpoint.get("completed_steps", 0)
                console.print(f"[yellow]Resuming run {run_id} from step {start_step}[/yellow]")

        context = {**inputs, "_run_id": run_id}

        with Progress(SpinnerColumn(), TextColumn("{task.description}"),
                      console=console) as progress:
            for i, step in enumerate(self.steps):
                if i < start_step:
                    continue

                task = progress.add_task(
                    f"[cyan]{step.name}[/cyan] — {step.description}", total=None
                )
                try:
                    result = step.agent_fn(context, run_id)
                    context.update(result or {})
                    progress.update(task, description=f"[green]✓ {step.name}[/green]")
                except Exception as e:
                    progress.stop()
                    console.print(f"[red]✗ {step.name} failed: {e}[/red]")
                    with session_scope() as session:
                        update_run_checkpoint(
                            session, run_id,
                            checkpoint={"completed_steps": i, "error": str(e)},
                            status="failed",
                        )
                    raise

                with session_scope() as session:
                    update_run_checkpoint(
                        session, run_id,
                        checkpoint={"completed_steps": i + 1},
                        status="running",
                    )

        with session_scope() as session:
            update_run_checkpoint(session, run_id,
                                  checkpoint={"completed_steps": len(self.steps)},
                                  status="completed")

        console.print(f"\n[bold green]✓ Pipeline complete[/bold green] (run_id: {run_id})")
        return context
