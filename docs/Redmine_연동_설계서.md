---
type: design
title: "vault → Redmine 단방향 연동 설계서"
version: "0.2"
created: 2026-05-06
updated: 2026-05-06
status: draft
tags: [redmine, integration, vault-push, workspace, process-library]
---

# vault → Redmine 단방향 연동 설계서

## 1. 핵심 원칙

- **단방향 Push**: vault → Redmine. 역방향 없음 (vault SSoT 보호)
- **Library = READ ONLY**: Process Library는 vault가 관리. 팀 직접 편집 금지.
- **Workspace = 자율**: 생성 후 팀이 소유. vault와 독립.

---

## 2. 개념 체계

### 용어 정의

| 용어 | 정의 | Redmine 구현 |
|---|---|---|
| **Process Library** | vault가 push한 표준 프로세스 저장소 | `lib-{scope_code}` 프로젝트 |
| **Library Module** | PRO 단위 라이브러리 컨테이너 | `lib-{scope_code}-{pro_slug}` 서브프로젝트 |
| **Workspace** | 현업 업무 단위를 묶은 가상 업무공간 | `ws-{name}` 프로젝트 + 서브프로젝트 N개 |
| **Workspace Module** | Workspace 내 PRO 단위 실행 공간 | `ws-{name}-{pro_slug}` 서브프로젝트 |

### 관계

```
현업 Workspace 1개  :  Redmine Project N개  (1:N)
Library Module 1개  :  Workspace Module N개 (1:N, 복사 관계)
```

---

## 3. Redmine 구조 전체도

```
[Process Library]                         vault 관리, READ ONLY
lib-iso27001
├── lib-iso27001-riskmanagement           (PRO-ISO27001-001-001)
├── lib-iso27001-accesscontrol            (PRO-ISO27001-001-002)
└── lib-iso27001-incidentmgmt             (PRO-ISO27001-001-003)

lib-cmmi
├── lib-cmmi-projectplanning              (PRO-CMMI-001-001)
└── lib-cmmi-requirements                 (PRO-CMMI-001-002)

         ↓ /workspace-create (필요한 Library Module 선택)

[Workspace: 제품Alpha 개발]               팀 관리, 자율 편집
ws-product-alpha
├── ws-product-alpha-riskmanagement       ← lib-iso27001-riskmanagement 복사
└── ws-product-alpha-accesscontrol        ← lib-iso27001-accesscontrol 복사

[Workspace: 고객사B 납품]
ws-client-b
├── ws-client-b-riskmanagement            ← lib-iso27001-riskmanagement 복사
└── ws-client-b-projectplanning           ← lib-cmmi-projectplanning 복사
```

---

## 4. vault 문서 유형별 Redmine 매핑

### Library Module 내 배치

| vault type | status 조건 | Redmine 리소스 |
|---|---|---|
| POL | final | scope_code 레벨 wiki (`POL/{doc_id}`) |
| PRO | final | Library Module wiki 메인 페이지 |
| WI | final | Library Module wiki (`WI/{doc_id}`) |
| TMP / EX | final | Library Module wiki (`TMP/{doc_id}`) |
| MAT (공통) | — | scope_code 레벨 wiki (`MAT/{doc_id}`) |
| REC (일반) | final | Issue — Tracker: 프로세스기록, 상태: Closed |
| REC-NCR | open/진행 | Issue — Tracker: NCR, 상태: 진행중 |
| REC-NCR | closed | Issue — Tracker: NCR, 상태: 종결 |
| draft 전체 | draft | **skip** (미동기화) |

---

## 5. 콘텐츠 변환 규칙

```
변환 전 (vault)                변환 후 (Redmine)
────────────────────────────────────────────────
frontmatter YAML 블록          제거
[[wikilink]]                   [[Redmine wiki 링크]] 포맷 변환
# 제목                         자동생성 헤더 추가 후 본문
```

**자동생성 헤더 (모든 push 문서에 삽입):**
```
> **[자동생성]** 이 문서는 processware vault에서 자동 배포됩니다.
> 직접 편집하지 마세요. 원본: vault/{경로}
> 버전: {version} | 최종갱신: {updated}
---
```

---

## 6. config.yaml 구조

```yaml
redmine:
  url: "https://redmine.yourorg.com"
  api_key: "${REDMINE_API_KEY}"

project_mapping:
  by_scope_code:
    ISO27001: "lib-iso27001"
    CMMI:     "lib-cmmi"
    ISO9001:  "lib-iso9001"
  by_pro:
    PRO-ISO27001-001-001: "lib-iso27001-riskmanagement"
    PRO-ISO27001-001-002: "lib-iso27001-accesscontrol"
    PRO-CMMI-001-001:     "lib-cmmi-projectplanning"

sync_rules:
  skip_status: [draft]
  wiki_types:  [POL, PRO, WI, TMP, EX, MAT, REC-AUDIT, REC-GAP]
  issue_types: [REC, REC-NCR]

issue_trackers:
  REC:     "프로세스기록"
  REC-NCR: "NCR"

redmine_custom_fields:
  doc_id:    10
  version:   11
  standards: 12
  retention: 13
```

---

## 7. 스킬 인터페이스

### /vault-push (Library 동기화)

```
/vault-push                         전체 vault → Library 동기화
/vault-push --changed               git diff 기준 변경분만
/vault-push WI-ISO27001-001-001-001 특정 문서 1건
/vault-push --type WI               WI 전체
/vault-push --scope ISO27001        특정 표준 전체
/vault-push --dry-run               실제 전송 없이 미리보기
/vault-push --status                마지막 동기화 상태
```

### /workspace-create (Workspace 생성)

```
/workspace-create \
  --name "제품Alpha 개발" \
  --slug product-alpha \
  --modules PRO-ISO27001-001-001,PRO-ISO27001-001-002 \
  --description "ISO27001 기반 제품Alpha 개발 프로세스 공간"
```

동작:
1. 지정된 Library Module 존재 확인
2. `ws-{slug}` 상위 프로젝트 생성
3. 각 PRO → `ws-{slug}-{pro_slug}` 서브프로젝트 생성
4. wiki 페이지·Issue 트래커 복사
5. sync_map에 `workspace_instance: true` 플래그 등록

### /workspace-sync (선택적 버전 업데이트)

```
/workspace-sync \
  --workspace ws-product-alpha \
  --module lib-iso27001-riskmanagement
```

동작: 해당 Library Module의 최신 버전을 Workspace Module에 반영 (팀 확인 후 진행).

---

## 8. Sync Map DB 스키마 (.claude/states/redmine_sync.db)

```sql
CREATE TABLE sync_map (
    vault_doc_id       TEXT PRIMARY KEY,
    vault_path         TEXT NOT NULL,
    redmine_type       TEXT NOT NULL,   -- 'wiki' | 'issue'
    redmine_project_id INTEGER NOT NULL,
    redmine_resource   TEXT NOT NULL,   -- wiki title or issue id
    vault_version      TEXT,
    last_synced_at     TEXT,
    status             TEXT,            -- 'synced' | 'failed' | 'pending'
    workspace_instance INTEGER DEFAULT 0  -- 1이면 Workspace 복사본
);

CREATE TABLE workspace_map (
    workspace_slug     TEXT NOT NULL,
    workspace_name     TEXT NOT NULL,
    redmine_project_id INTEGER NOT NULL,
    source_modules     TEXT NOT NULL,   -- JSON array of Library Module ids
    created_at         TEXT NOT NULL
);
```

---

## 9. 구현 파일 구성

```
processware/
└── publish/
    └── redmine/
        ├── config.yaml          접속 정보 + 매핑 룰
        ├── sync.py              /vault-push 메인 로직
        ├── workspace.py         /workspace-create, /workspace-sync
        ├── transformer.py       vault MD → Redmine 포맷 변환
        ├── redmine_client.py    Redmine REST API 래퍼
        └── requirements.txt     python-frontmatter, requests
.claude/
├── commands/
│   ├── vault-push.md            스킬 정의
│   └── workspace-create.md      스킬 정의
└── states/
    └── redmine_sync.db          Sync Map (git 제외)
```

---

## 10. 구현 Phase

```
Phase 1 — 기반 (1~2일)
  config.yaml + redmine_client.py + SQLite 스키마 + dry-run

Phase 2 — Library Push (2~3일)
  transformer.py + WI/PRO/POL → Library Module wiki push
  /vault-push 스킬 등록

Phase 3 — Issue 동기화 (1~2일)
  REC → Issue (Closed) + NCR → Issue (Open/종결)

Phase 4 — Workspace (2~3일)
  workspace.py + /workspace-create 스킬 등록

Phase 5 — 자동화 (1일)
  git post-commit hook + GitHub Actions 연결
```
