"""CRUD operations for processmine models."""

from typing import Optional
from sqlalchemy.orm import Session

from .models import Document, Record, Run


# ── Document ──────────────────────────────────────────────────────────────────

def upsert_document(session: Session, **kwargs) -> Document:
    doc = session.query(Document).filter_by(doc_id=kwargs["doc_id"]).first()
    if doc:
        for k, v in kwargs.items():
            setattr(doc, k, v)
    else:
        doc = Document(**kwargs)
        session.add(doc)
    session.flush()
    return doc


def get_document(session: Session, doc_id: str) -> Optional[Document]:
    return session.query(Document).filter_by(doc_id=doc_id).first()


def list_documents(session: Session, doc_type: str = None,
                   scope_code: str = None) -> list[Document]:
    q = session.query(Document)
    if doc_type:
        q = q.filter_by(doc_type=doc_type)
    if scope_code:
        q = q.filter_by(scope_code=scope_code)
    return q.all()


def next_seq_for_type(session: Session, doc_type: str,
                      scope_code: str, parent_doc_id: str = None) -> int:
    """DB 기반 다음 일련번호 조회 (scanner.py 의 DB 버전)."""
    q = session.query(Document).filter_by(doc_type=doc_type, scope_code=scope_code)
    if parent_doc_id:
        q = q.filter_by(parent_doc_id=parent_doc_id)
    count = q.count()
    return count + 1


# ── Record ────────────────────────────────────────────────────────────────────

def upsert_record(session: Session, **kwargs) -> Record:
    rec = session.query(Record).filter_by(rec_id=kwargs["rec_id"]).first()
    if rec:
        for k, v in kwargs.items():
            setattr(rec, k, v)
    else:
        rec = Record(**kwargs)
        session.add(rec)
    session.flush()
    return rec


# ── Run ───────────────────────────────────────────────────────────────────────

def create_run(session: Session, run_id: str, command: str, args: dict) -> Run:
    run = Run(run_id=run_id, command=command, args=args)
    session.add(run)
    session.flush()
    return run


def get_run(session: Session, run_id: str) -> Optional[Run]:
    return session.query(Run).filter_by(run_id=run_id).first()


def update_run_checkpoint(session: Session, run_id: str,
                          checkpoint: dict, status: str = None):
    run = session.query(Run).filter_by(run_id=run_id).first()
    if run:
        run.checkpoint = checkpoint
        if status:
            run.status = status
        session.flush()
