"""Static rule definitions — single source of truth for vault structure."""

from typing import Dict, List

# 8종 문서 유형
DOC_TYPES = ["POL", "PRO", "WI", "TMP", "EX", "REC", "MAT", "REF"]

# 유형 → 폴더 이름
FOLDER_MAP: Dict[str, str] = {
    "POL": "03_POL_정책",
    "PRO": "04_PRO_절차",
    "WI":  "05_WI_업무지침",
    "TMP": "06_TMP_템플릿",
    "EX":  "07_EX_작성예시",
    "REC": "08_REC_기록",
    "MAT": "90_MAT_통합매핑",
    "REF": "09_REF_참고자료",
}

# 유형 → 계층 깊이 (POL=1, PRO=2, WI=3, TMP/EX=4, REC=5)
HIERARCHY_DEPTH: Dict[str, int] = {
    "POL": 1,
    "PRO": 2,
    "WI":  3,
    "TMP": 4,
    "EX":  4,
    "REC": 5,
    "MAT": 0,  # 별도 축
    "REF": 0,  # 별도 축
}

# 유형 → 부모 유형
PARENT_TYPE: Dict[str, str] = {
    "PRO": "POL",
    "WI":  "PRO",
    "TMP": "WI",
    "EX":  "WI",
    "REC": "TMP",
}

# 유형별 frontmatter 필수 필드
FRONTMATTER_SCHEMA: Dict[str, List[str]] = {
    "POL": ["type", "doc_id", "title", "version", "status", "owner", "scope_code"],
    "PRO": ["type", "doc_id", "title", "version", "status", "owner", "scope_code", "parent_pol"],
    "WI":  ["type", "doc_id", "title", "version", "status", "owner", "scope_code", "parent_pro"],
    "TMP": ["type", "doc_id", "title", "version", "parent_wi"],
    "EX":  ["type", "doc_id", "title", "version", "parent_tmp"],
    "REC": ["type", "doc_id", "title", "wi_id", "tmp_id", "created_at", "status"],
    "MAT": ["type", "doc_id", "title", "version"],
    "REF": ["type", "doc_id", "title", "version"],
}

# MAT 전사 공통 예약 구역 (001~010)
MAT_COMMON_MAX = 10
MAT_STANDARD_START = 11

# 영역 코드 등록 목록
SCOPE_CODES = [
    "QMS", "ISMS", "PIMS", "EMS", "OHSMS", "ITSM", "BCMS", "RM", "AIMS",
    "SWLC", "SYSLC", "IR", "VUL",
    "AUTO", "SPICE", "FUSA", "VCSMS",
    "MDQMS", "MDRM", "MDSW", "MDCS",
    "CMMI",
]

# 분리 원칙 — 같은 폴더 금지 쌍
SEPARATION_RULES = [
    ("TMP", "REC"),
]
