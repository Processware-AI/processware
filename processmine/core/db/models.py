from datetime import datetime
from typing import Any

from sqlalchemy import (
    Column, DateTime, ForeignKey, Integer, JSON, String, Text,
    func, UniqueConstraint,
)
from sqlalchemy.orm import DeclarativeBase, relationship, backref


class Base(DeclarativeBase):
    pass


class Document(Base):
    """POL / PRO / WI / TMP / EX / MAT / REF 문서."""
    __tablename__ = "documents"

    id          = Column(Integer, primary_key=True)
    doc_id      = Column(String, unique=True, index=True, nullable=False)  # POL-QMS-01
    doc_type    = Column(String, nullable=False)   # POL/PRO/WI/TMP/EX/MAT/REF
    scope_code  = Column(String, index=True)       # QMS/ISMS/...
    title       = Column(String, nullable=False)
    version     = Column(String, default="0.1")
    status      = Column(String, default="draft")  # draft/active/deprecated
    content     = Column(Text)                     # 전체 MD 텍스트
    meta        = Column(JSON, default=dict)       # frontmatter 파싱 결과
    parent_doc_id = Column(String, ForeignKey("documents.doc_id"), nullable=True)
    run_id      = Column(String, ForeignKey("runs.run_id"), nullable=True)
    created_at  = Column(DateTime, default=func.now())
    updated_at  = Column(DateTime, default=func.now(), onupdate=func.now())

    children = relationship(
        "Document",
        foreign_keys=[parent_doc_id],
        backref=backref("parent", remote_side="Document.doc_id"),
    )


class Record(Base):
    """REC / REC-NCR / REC-AUDIT / REC-GAP 기록."""
    __tablename__ = "records"

    id          = Column(Integer, primary_key=True)
    rec_id      = Column(String, unique=True, index=True, nullable=False)
    rec_type    = Column(String, nullable=False)   # REC/NCR/AUDIT/GAP
    wi_id       = Column(String, nullable=True)
    tmp_id      = Column(String, nullable=True)
    status      = Column(String, default="open")
    content     = Column(Text)
    meta        = Column(JSON, default=dict)
    run_id      = Column(String, ForeignKey("runs.run_id"), nullable=True)
    created_at  = Column(DateTime, default=func.now())
    updated_at  = Column(DateTime, default=func.now(), onupdate=func.now())


class Run(Base):
    """파이프라인 실행 단위. 체크포인트·재개 지원."""
    __tablename__ = "runs"

    id          = Column(Integer, primary_key=True)
    run_id      = Column(String, unique=True, nullable=False)  # UUID
    command     = Column(String, nullable=False)   # build-process / do / check / act
    args        = Column(JSON, default=dict)       # {"standard": "ISO9001"}
    status      = Column(String, default="running")  # running/completed/failed/paused
    checkpoint  = Column(JSON, default=dict)       # 현재 단계 상태
    created_at  = Column(DateTime, default=func.now())
    updated_at  = Column(DateTime, default=func.now(), onupdate=func.now())

    documents = relationship("Document", backref="run",
                             foreign_keys=[Document.run_id])
    records   = relationship("Record", backref="run",
                             foreign_keys=[Record.run_id])
