---
type: session-recap
date: 2026-05-07
title: "vault 구조 규칙 Python 코드화 + 에이전트 프롬프트 정리"
participants: ["dongseok"]
commits:
  - dc64b45  # feat(tools): vault_rules CLI — vault 구조 규칙 Python 코드화
  - 897eb56  # refactor(agents): vault 구조 규칙 텍스트 → vault_rules CLI 호출로 교체
tags: [session, architecture, vault-rules, python, cli, agents, deterministic]
---

# 세션 회고 — 2026-05-07

## 1. 출발점

전 세션의 Document·Record 레이어 분리 논의를 이어받아 재검토.

---

## 2. Document·Record 레이어 분리 — 보류 결정

전 세션 결론("마크다운 source of truth + SQLite 읽기 캐시")을 재검토한 결과:

- Document Layer = 사람에게 제시하는 규범 (vault .md)
- Record Layer DB = AI 에이전트 자동화 기반 (SQL 집계·조인)
- 현재 REC 수가 적어 grep으로 충분 — 아직 가상의 문제
- .md ↔ DB 동기화 자체가 복잡도를 추가

**결론: Record Layer DB 구현 보류. 트리거는 실제 운영에서 REC가 대량 누적될 때.**

---

## 3. vault 구조 규칙 Python 코드화 (핵심 작업)

### 배경

`process-plan`이 vault를 생성할 때, 파일명·번호 체계·폴더 배치·frontmatter 규칙이
`.claude/agents/*.md` 프롬프트 텍스트로만 존재 → LLM이 읽고 따르지만 일관성 보장 안 됨.

### 설계 결정

**분리 원칙**: 구조 = Python (deterministic), 내용 = LLM

| 역할 | 담당 |
|------|------|
| 파일명, 폴더, 번호 생성, frontmatter 스키마 | Python CLI |
| 문서 내용 (RACI, KPI, 절차 텍스트 등) | LLM |

옵션 A (CLI 도구) / 옵션 B (MCP 서버) 중 **옵션 A** 선택 — 하네스에 즉시 붙고 단순.

### 구현: `tools/vault_rules/` 패키지

```
tools/vault_rules/
  rules.py       # 상수 (폴더맵, 스키마, 영역코드)
  generator.py   # ID 생성·파싱·파일명·cascade — pure functions
  scanner.py     # vault 스캔 → 다음 seq 번호
  validator.py   # 규칙 위반 검사
  __main__.py    # CLI 진입점
```

**CLI 커맨드:**
```bash
python3 -m tools.vault_rules next-id   --type PRO --scope QMS --parent POL-QMS-01
python3 -m tools.vault_rules filename  --id PRO-QMS-01-02 --name "접근통제 절차" --version 1.0
python3 -m tools.vault_rules folder    --type PRO
python3 -m tools.vault_rules schema    --type WI
python3 -m tools.vault_rules version   --current 1.0 --change minor
python3 -m tools.vault_rules validate  --file vault/04_PRO_절차/PRO-...md
python3 -m tools.vault_rules cascade   --old POL-QMS-01 --new POL-QMS-02 --dry-run
python3 -m tools.vault_rules next-seq  --glob "vault/08_REC_기록/AUDIT/REC-NCR-04-01-2026-*.md" --digits 3
```

**주요 구현 특성:**
- MAT `next-id` 호출 시 MAT-001~010 전사공통 예약 구간 자동 스킵 (MAT-011부터 반환)
- `next-seq --glob` — NCR/AUDIT/GAP 같은 특수 패턴에 범용 적용
- `validate` — 파일명 형식, 폴더 배치, frontmatter 필수 필드, doc_id 일치 검사
- `cascade` — POL ID 변경 시 하위 PRO/WI/TMP/EX/REC 연쇄 rename 목록 산출

---

## 4. 에이전트 프롬프트 정리 (8개)

하드코딩된 규칙 텍스트를 CLI 호출로 교체:

| 에이전트 | 제거된 것 | 교체 |
|---------|----------|------|
| process-designer | POL/PRO/WI 번호 규칙 텍스트 | `next-id` |
| wi-tmp-writer | WI/TMP/EX 경로 패턴 | `next-id` + `filename` + `folder` |
| rec-writer | REC 번호 산출 Glob 로직 | `next-id` + `filename` |
| qa-reviewer | 폴더/파일명/자릿수 수동 체크리스트 | `validate` |
| traceability-mapper | MAT 번호 스캔 규칙 | `next-id --type MAT` |
| ncr-drafter | NCR Glob 스캔 로직 | `next-seq --glob` |
| audit-reporter | AUDIT 회차·일련번호 로직 | `next-seq --glob` |
| gap-reporter | GAP Glob 스캔 로직 | `next-seq --glob` |

---

## 5. LLM 의존 감소 범위 정리

**줄어든 것** — 번호·파일명·폴더의 결과값 결정 (CLI가 보장)

**줄어들지 않은 것** — CLI를 언제·어떻게 호출할지, 올바른 인수 전달, 문서 내용 생성

→ "LLM이 틀릴 수 있는 영역을 코드로 보호"한 것이지, LLM 자체를 줄인 건 아님.
완전한 의존 감소는 Python 포팅(processmine) 단계에서 가능 — 에이전트 출력을 Python이 받아 구조 규칙 강제 적용.

---

## 6. 핵심 결정 요약

- **vault 구조 규칙은 Python 코드(tools/vault_rules)가 단일 소스로 관리**
- **에이전트는 구조 결정을 추론하지 않고 CLI에 위임**
- **processmine 포팅 시 이 모듈이 그대로 core 레이어로 이동**
