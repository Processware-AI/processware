"""vault_rules — deterministic vault structure rules for processware."""

from .generator import (
    DocId,
    parse_doc_id,
    build_doc_id,
    new_child_id,
    new_mat_id,
    new_ref_id,
    generate_filename,
    get_folder_path,
    increment_version,
    cascade_ids,
)
from .scanner import next_seq
from .validator import validate_file, validate_frontmatter
from .rules import FOLDER_MAP, FRONTMATTER_SCHEMA, SCOPE_CODES, DOC_TYPES

__all__ = [
    "DocId",
    "parse_doc_id", "build_doc_id", "new_child_id",
    "new_mat_id", "new_ref_id",
    "generate_filename", "get_folder_path", "increment_version", "cascade_ids",
    "next_seq",
    "validate_file", "validate_frontmatter",
    "FOLDER_MAP", "FRONTMATTER_SCHEMA", "SCOPE_CODES", "DOC_TYPES",
]
