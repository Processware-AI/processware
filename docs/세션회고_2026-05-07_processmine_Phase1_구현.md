---
type: session-recap
date: 2026-05-07
title: "processmine Phase 1 구현 — 독립 실행형 Python 패키지 스캐폴드"
participants: ["dongseok"]
commits:
  - b1ec32a  # feat(processmine): Phase 1 scaffold — 5-agent dim1_plan pipeline
tags: [session, processmine, python, db, sqlite, pipeline, agents, dim1]
---

# 세션 회고 — 2026-05-07 (processmine Phase 1)

## 1. 출발점

이전 세션의 processmine 아키텍처 설계 결정에 따라 실제 코드 구현 착수.
핵심 결정사항:
- Obsidian 버림 → DBMS (SQLite → PostgreSQL 확장)
- Claude Code 하네스와 독립 실행형 2개 병행
- DB에 전체 MD 내용 저장 (Option A)
- 1인 컨설턴트 대상 상용 제품

## 2. 구현 내용

### 2-1. pyproject.toml
- setuptools.build_meta (setuptools.backends.legacy:build → 오류 수정)
- 엔트리포인트: `processmine = "processmine.cli.main:app"`
- Python 3.11+ 필수 (가상환경 venv/로 격리)

### 2-2. processmine/core/db/
- **models.py**: Document / Record / Run 3개 테이블
  - Document: 자기참조 FK (parent_doc_id → doc_id). SQLAlchemy backref + remote_side 설정 필요
  - Run: 파이프라인 실행 단위, checkpoint JSON으로 체크포인트/재개 지원
- **engine.py**: get_engine() lazy singleton, init_db(), session_scope() 컨텍스트 매니저
- **repository.py**: upsert_document, list_documents, create_run, update_run_checkpoint 등

### 2-3. processmine/core/orchestrator.py
- PipelineStep(name, agent_fn, description) 데이터클래스
- Pipeline.run(inputs, resume_run_id) — Rich 진행바 + 체크포인트 저장/재개

### 2-4. processmine/agents/base.py
- BaseAgent 추상 클래스
- call_llm() / call_llm_with_tools() — Anthropic SDK 래핑
- save_document() — DB 저장 헬퍼

### 2-5. processmine/agents/dim1_plan/ — 5개 에이전트
| 에이전트 | 역할 | 출력 |
|---|---|---|
| standard-analyzer | 표준 요구사항 분해 | REF 문서 + requirements 목록 |
| process-designer | POL/PRO 설계 | POL/PRO DB 저장 |
| wi-tmp-writer | WI/TMP/EX 생성 | WI/TMP/EX DB 저장 |
| traceability-mapper | 추적성 매트릭스 | MAT 문서 |
| qa-reviewer | 품질 검토 | REF QA 보고서 |

### 2-6. processmine/cli/main.py
- `processmine init [path]` — DB 초기화
- `processmine build-process <standard> [--scope] [--resume] [--reqs]` — 5단계 파이프라인
- `processmine list [--type] [--scope]` — DB 문서 목록
- `processmine export [--out] [--scope] [--type]` — DB → .md 파일 내보내기

## 3. 발생한 이슈 & 해결

| 이슈 | 원인 | 해결 |
|---|---|---|
| `BackendUnavailable: setuptools.backends` | pyproject.toml build-backend 오타 | `setuptools.build_meta` 로 수정 |
| `sqlalchemy ArgumentError: same direction ONETOMANY` | 자기참조 FK에 remote_side 없음 | `backref=backref("parent", remote_side="Document.doc_id")` |
| pip 21.2.4 editable mode 실패 | macOS 기본 Python 3.9 | Python 3.11 venv 생성 후 재설치 |

## 4. 현재 상태

- [x] 패키지 설치 (`pip install -e ".[dev]"`)
- [x] `processmine init` — DB 생성 확인
- [x] `processmine build-process --help` — CLI 정상 작동
- [x] 5개 에이전트 import 및 파이프라인 wiring 확인
- [ ] 실제 API 키로 end-to-end 테스트 (미실행)
- [ ] `processmine export` 실제 파일 출력 테스트

## 5. 다음 단계

1. **end-to-end 실행 테스트** — 실제 ANTHROPIC_API_KEY 환경에서 `processmine build-process ISO9001`
2. **dim2 agents 포팅** — process-do (do), process-check, process-act 파이프라인
3. **export 검증** — `processmine export` → vault 폴더 구조와 동일한 .md 생성 확인
4. **PostgreSQL 전환** — sqlite URL → pg URL 설정 테스트

## 6. 아키텍처 메모

- `tools/vault_rules` 는 processmine과 Claude Code 하네스가 공유. 동일 패키지 경로 사용.
- DB 내 content 필드 = 전체 MD 텍스트. export 시 폴더/파일명은 meta.filename 으로 결정.
- 파이프라인 컨텍스트(ctx dict)가 스텝 간 결과를 전달. 체크포인트는 Run.checkpoint JSON에 저장.
