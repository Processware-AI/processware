---
type: architecture
title: 조직 계층 도입 설계 방향 — 플랫폼 1 + 조직 루트 N
version: "0.7"
status: draft
updated: 2026-11-04
decided:
  - "2026-11-04: 조직 루트는 플랫폼 repo 밖 별도 repo 로 둔다"
  - "2026-11-04: 공개 표준 ingest 산출물은 조직 루트에 둔다 (조직 간 공유 지식 팩 없음)"
  - "2026-11-04: 파생 프로덕트(파생 ②)에도 조직 컨텍스트를 같은 환경변수 PROCESSWARE_ORG_ROOT 로 전달한다"
  - "2026-11-04: default 조직 fallback 은 마이그레이션(단계 3) 완료 후 제거한다"
tags: [architecture, multi-tenant, org-layer, vault-isolation]
related:
  - derivative-products.md
  - ../표준프로세스_AI관리체계_4차원PDCA.md
  - ../전용AI에이전트_프레임워크_설계안.md
---

# 조직 계층 도입 설계 방향

## 0. 배경 — 현재 구조 진단

현재 repo 는 **단일 조직 전용(single-tenant)** 이다. 분리 축은 **표준(standard)** 이지 **조직(tenant)** 이 아니다.

| 구분 | 현재 상태 |
|---|---|
| 표준 단위 분리 | ✅ 영역코드 22종(QMS·ISMS·CMMI·VCSMS …) + MAT-011~ 표준별 추적성 + Redmine `lib-{scope}` |
| 조직 단위 분리 | ❌ 없음. `02_적용요건/` 폴더명을 조직 이름으로 짓도록 안내할 뿐, 상위에 조직 계층이 없다 |
| repo 당 하나인 것 | MAT-001~010 전사 공통 매핑표, `.claude/rbac/policy.yaml`, 문서 번호 체계, `.claude/runs|queues|states`, `publish/redmine/config.yaml` |
| 설계 문서의 입장 | 멀티테넌트는 4차원 PDCA 설계서 Phase 5 "SaaS 멀티테넌트" 와 독립 프레임워크 설계안의 "내부 툴 → B2B → SaaS" 마지막 단계에만 등장 |

즉 현재 운영 모델은 **"조직 하나당 repo(vault) 하나를 복제해서 쓰는 방식"** 이다. 컨설팅 펌처럼 여러 고객사를 다루려면 조직 계층이 필요하다.

**결론**: **플랫폼(에이전트·규칙·템플릿) 1개 + 조직 루트 N개** 로 분리하고, 모든 커맨드가 **활성 조직 컨텍스트** 를 통해 경로를 해석하도록 바꾼다. 문서 ID 체계는 건드리지 않는다.

---

## 1. 공유 / 조직별 분리 기준

현재 repo 를 두 층으로 가른다.

| 층 | 내용 | 현재 위치 |
|---|---|---|
| **플랫폼 (공유)** | 에이전트 29 · 커맨드 9 · utils, `tools/vault_rules`, 구성원칙 · 문서체계 · 번호체계 · 표준분류레지스트리, 99_템플릿 · 골든샘플 | `.claude/`, `tools/`, `vault/00_공통관리` · `01_구성원칙` · `99_템플릿` |
| **조직 (격리)** | 원본 소스 · ingest 산출물 전체(공개 표준 포함), 적용요건, POL~REF, MAT-001~, AsIs, 실행 trace · act queue · 체크포인트, RBAC 사용자 배정, Redmine 매핑 | `sources/`, `inputs/01~05`, `vault/02~09`, `vault/90_MAT`, `.claude/runs|queues|states`, `.claude/rbac/`, `publish/*/config.yaml` |

핵심 관찰 두 가지:

1. **입력은 전부 조직 루트에 둔다.** 공개 표준의 requirements.yaml 은 내용상 조직과 무관하지만, 표준 원문 저작권과 조직별 ingest 버전 · delta 이력이 달라질 수 있으므로 조직 간 공유 지식 팩을 두지 않는다 (2026-11-04 결정). 같은 표준을 여러 조직에서 쓰면 조직마다 `/process-ingest` 를 다시 돌린다.
2. **MAT · trace · queue · RBAC 가 repo 당 하나라는 점이 격리의 본체다.** 이들을 조직 루트 아래로 내리는 것이 설계 변경의 핵심이다.

---

## 2. 목표 구조

```
processware/                        ← 플랫폼 repo (공유)
├── .claude/
│   ├── agents/                     ← 29 에이전트 (경로는 {VAULT} 등 변수로 참조)
│   ├── commands/                   ← 9 커맨드 (--org 옵션 공통)
│   ├── utils/
│   └── rbac/policy.yaml            ← 역할 정의 템플릿 (사용자 배정 없음)
├── tools/
│   ├── vault_rules/                ← 기존 (--vault 루트 인자 그대로 사용)
│   └── org/                        ← context / validate / init / sync-core / register / list
└── core/
    ├── vault_base/                 ← vault 템플릿 전체 + _manifest.yaml (managed: 00_공통관리 · 01_구성원칙 · 99_템플릿 · 폴더 README · 가이드 / seed: MOC · MAT-001~009)
    └── org_base/                   ← 조직 루트 템플릿 (README · .gitignore · inputs/·sources/ README) — 없을 때만 복사

{ORG_ROOT}/                         ← 조직 루트 (조직별 별도 git repo — 결정)
├── org.yaml                        ← org_id · 명칭 · 사용 영역코드 · rbac 사용자 배정 · redmine 매핑
├── sources/                        ← 조직이 투하한 원본 파일 (표준 PDF · 법규 · AsIs, 저작권 · 기밀)
├── inputs/                         ← /process-ingest 산출물 전체 (공개 표준 포함, 조직 루트에 둠 — 결정)
│   ├── 01_표준원문 · 02_법규 · 03_해설서 · 05_산업가이드
│   ├── 04_AsIs/                    ← 조직 내부 자산 (기밀)
│   └── 06_목표흐름/                ← business_flow.yaml / .md
├── vault/                          ← Obsidian vault — 자기완결
│   ├── 00_공통관리 · 01_구성원칙 · 99_템플릿   ← managed: sync-core 가 덮어씀 (직접 수정 금지)
│   ├── 00_MOC · 90_MAT_통합매핑               ← seed: 최초 1회 복사 후 조직 소유
│   ├── 02_적용요건 · 03_POL ~ 09_REF · 90_MAT ← 조직 산출물
│   └── 99_폐기_보관
└── .processware/
    ├── runs/                       ← 실행 trace (run-*)
    ├── queues/process-act/         ← 차원 4 인계 큐 (queue-q*)
    ├── states/                     ← 차원 1 체크포인트 (_state.yaml)
    └── sync_map.sqlite             ← Redmine 등 외부 연동 매핑
```

### 2.1 조직 루트를 플랫폼 repo 밖 별도 repo 로 둔다 (결정)

컨설팅 상황의 **NDA** 때문이다. 한 repo 안에 `orgs/A`, `orgs/B` 를 두면:

- 커밋 한 번에 고객 자산이 섞인다.
- 브랜치 · 히스토리 단위 격리가 불가능하다.
- 고객에게 repo 접근 권한을 줄 수 없다.

조직 루트가 별도 repo 이면 `PROCESSWARE_ORG_ROOT` 로 가리키기만 하면 되고, 플랫폼 체크아웃 1개로 N 개 조직을 운영할 수 있다.

### 2.2 공유 폴더는 심볼릭 링크가 아니라 복사

Obsidian 은 vault 가 자기완결적이어야 wikilink 가 동작한다. 따라서 `00_공통관리` · `01_구성원칙` · `99_템플릿` 은 `tools/org sync-core` 가 `core/vault_base` 에서 **복사** 해 넣는다. 플랫폼이 갱신되면 sync-core 를 다시 실행하고, 조직별 오버라이드(예: 용어집 추가 항목) 는 별도 파일로 두어 덮어쓰지 않는다.

---

## 3. 변경 단계

| 단계 | 내용 | 영향 범위 |
|---|---|---|
| **1. 조직 컨텍스트 도입** ✅ 구현 (2026-11-04) | `PROCESSWARE_ORG_ROOT` 환경변수 또는 모든 커맨드의 `--org <id>` / `--org-root <path>` 옵션으로 활성 조직을 정한다. 미지정 시 현재 `vault/` 를 `default` 조직으로 취급해 하위 호환을 유지한다 (단계 3 완료 시 이 fallback 은 제거). 구현: `tools/org/` (context · schema · registry · CLI) + `.claude/utils/org_context.md` 규약 + 커맨드 9개 공통 절 + `tools/vault_rules` 기본 vault 연동. §6 참조. | 커맨드 9 · tools |
| **2. 경로 추상화** ✅ 구현 (2026-11-04) | 에이전트 29 · 커맨드 9 · utils 1 의 리터럴 경로 574건을 `{VAULT}` `{INPUTS}` `{SOURCES}` `{RUNS}` `{QUEUES}` `{STATES}` 로 치환. frontmatter(description · argument-hint)는 사용자 입력 예시라 리터럴 유지. 커맨드 공통 절이 변수 바인딩·에이전트 전달을 규정, 에이전트마다 변수 안내 1줄. 단계 1 의 임시 치환 브리지 삭제. | 에이전트 29 · 커맨드 9 |
| **3. 스캐폴드 도구** ✅ 구현 (2026-11-05) | `python -m tools.org init {path}` 가 조직 루트(org.yaml · 폴더)를 만들고 `sync-core` 를 실행한다. `core/vault_base/_manifest.yaml` 의 managed(덮어쓰기)/seed(없을 때만) 규칙으로 `{ORG_ROOT}/vault` 를 채우고, `core/org_base` 로 조직 README · .gitignore 를 시드한다. 플랫폼 repo 의 `vault/` · `inputs/` · `sources/` 는 `core/` 로 이동(git mv)했고 default fallback 은 제거했다. | `tools/org/sync.py` · `core/` |
| **4. RBAC 조직화** ✅ 구현 (2026-11-05) | 역할 정의는 플랫폼 `policy.yaml` (v0.2), 사용자→역할 배정 · alias · owns_pro · 위임 · enforce 는 `org.yaml` → `rbac`. 판정은 `python3 -m tools.org rbac` (결정론적) 이 하고 감사 로그를 조직 루트 `.processware/rbac_audit.jsonl` 에 남긴다. independence-guard 는 CLI 결과만 전달. | `tools/org/rbac.py` · independence-guard · policy.yaml |
| **5. 격리 가드** | 에이전트가 활성 조직 루트 밖의 vault 경로에 쓰려 하면 거부하는 검증을 qa-reviewer 와 `vault_rules validate` 에 추가한다. | qa-reviewer · vault_rules |
| **6. 외부 연동** | Redmine 프로젝트 이름을 `lib-{org}-{scope}` · `ws-{org}-{slug}` 로 바꾸고, sync_map DB 와 config 를 조직 루트로 옮긴다. GitHub Actions 는 **조직 repo 쪽에서 플랫폼을 체크아웃해 실행** 하는 구조로 뒤집는다. | publish/redmine · vault-push.yml |
| **7. 교차 조직 뷰 (선택)** | 컨설팅 펌 관점의 읽기 전용 통합 대시보드. 조직 데이터를 복제하지 않고 각 루트를 읽어 생성한다. 마지막에 한다. | 신규 |

---

## 4. 의도적으로 바꾸지 않는 것

- **문서 ID**: `POL-QMS-01` 에 조직 코드를 넣지 않는다. 조직은 루트 경로로 이미 구분되고, ID 를 바꾸면 계보 추적 · wikilink · 추적성 매트릭스가 전부 깨진다. 대신 frontmatter 에 `org:` 필드만 추가한다.
- **MAT 번호**: 조직마다 MAT-001 부터 다시 시작한다. 전사 공통 10종 + 표준별 011~ 규칙은 조직 안에서 그대로 유효하다.
- **4차원 PDCA 파이프라인 로직**: 경로만 바뀌고 Phase 구성 · 에이전트 역할 · HITL 게이트는 동일하다.
- **8종 문서 유형 체계 · 폴더 배치 · 분리 원칙**: `표준프로세스_구성원칙.md` 의 프레임은 조직 vault 안에서 그대로 적용된다.

---

## 5. 먼저 결정할 사항

| # | 결정 | 선택지 | 권장 |
|---|---|---|---|
| 1 | 조직 루트 위치 | (a) 플랫폼 repo 밖 별도 repo / (b) 플랫폼 repo 안 `orgs/{org}/` | ✅ **(a) 결정 (2026-11-04)** — NDA 격리 |
| 2 | 공개 표준 ingest 산출물 공유 | (a) `knowledge/standards/` 지식 팩으로 조직 간 공유 / (b) 조직 루트에 둠 | ✅ **(b) 결정 (2026-11-04)** — 저작권 · 조직별 ingest 버전 분리. 플랫폼 repo 에 `knowledge/` 없음 |
| 3 | 3-Vault 파생 프로덕트와의 관계 | 파생 ②(Project Asset Generator) 는 "조직의 코어 vault" 를 입력으로 받음 | ✅ **결정 (2026-11-04)** — 조직 컨텍스트를 파생 프로덕트에도 같은 환경변수 `PROCESSWARE_ORG_ROOT` 로 전달. 파생 ① 은 코어 vault 를 입력으로 받지 않으므로 해당 없음 |
| 4 | 하위 호환 기간 | `default` 조직 fallback 을 언제까지 유지할지 | ✅ **결정 (2026-11-04)** — 단계 3 마이그레이션 완료 후 제거. 이후 `PROCESSWARE_ORG_ROOT` 미설정 시 커맨드는 즉시 실패 → **단계 3 에서 실행 완료 (2026-11-05)** |

선결 결정 4건 모두 확정 (2026-11-04). 다음 단계는 §3 의 1단계(조직 컨텍스트 도입)부터 구현 착수.

---

## 6. 구현 현황

| 단계 | 상태 | 산출물 |
|---|---|---|
| 1. 조직 컨텍스트 도입 | ✅ 구현 (2026-11-04) | `tools/org/` — `context.py` (해석 우선순위 5단계 · 레이아웃), `schema.py` (org.yaml 검증), `registry.py` (`~/.processware/orgs.yaml`), `__main__.py` (`context` · `validate` · `init` · `register` · `unregister` · `list`), `templates/org.yaml`, `tests/` (unittest 15건). `.claude/utils/org_context.md` 해석 규약. 커맨드 9개에 "조직 컨텍스트 (공통)" 절 + `argument-hint` 에 `--org` / `--org-root` 추가. `tools/vault_rules` 의 `--vault` 기본값을 활성 조직 vault 로 연동. |
| 2. 경로 추상화 | ✅ 구현 (2026-11-04) | `.claude/agents/*` (29) · `.claude/commands/*` (9) · `.claude/utils/auto_trend_mermaid.md` 본문 리터럴 574건 → 변수 표기. `.claude/utils/org_context.md` §3 이 변수 정의. 커맨드 공통 절 재작성 (변수 표·바인딩·에이전트 전달·하위 호출 export). 에이전트 29개 본문 첫 줄에 경로 변수 안내. |
| 3. 스캐폴드 도구 | ✅ 구현 (2026-11-05) | `core/vault_base/` (구 `vault/` 전체, `_inputs_common` 제거, `.obsidian` 포함) + `_manifest.yaml` · `core/org_base/` (README · .gitignore · inputs/sources README). `tools/org/sync.py` sync-core (managed 덮어쓰기 · seed 보존 · `--force` 재시드 · `--dry-run` · manifest 전수 분류 검사 · org.yaml platform_version 갱신 · `.processware/sync-core.yaml` 기록). `init` 이 sync-core 자동 실행 (`--no-sync` 로 생략). `context.py` default fallback 제거. 테스트 17건. |
| 4. RBAC 조직화 | ✅ 구현 (2026-11-05) | `.claude/rbac/policy.yaml` v0.2 — 역할 6종 정의만 (PoC users 제거, `act.*` action 추가, 판정 규칙 명문화). `org.yaml` → `rbac`: `enforce` · `users` (역할 목록 또는 {roles, aliases, owns_pro}) · `delegations[]` (until 만료 자동 무시) · `audit_log`. `tools/org/rbac.py` 판정 엔진 (glob 매칭 · deny→allow→target_constraints · 위임 · alias · 독립성) + 감사 로그 `.processware/rbac_audit.jsonl`. CLI `tools.org rbac check|independence|roles|users|log`. independence-guard 는 CLI 결과만 사용 (LLM 판정 제거). 테스트 32건. |
| 5~7 | ⏳ 미착수 | — |

**알려진 제한 (단계 3 시점)**
- 플랫폼 repo 에는 더 이상 `vault/` · `inputs/` · `sources/` 가 없다. 모든 커맨드는 `PROCESSWARE_ORG_ROOT` 또는 `--org`/`--org-root` 가 있어야 동작한다.
- `publish/redmine/*` Python 과 `.github/workflows/vault-push.yml` 은 플랫폼 repo 루트의 `vault/` 리터럴을 전제하므로 **현재 동작하지 않는다**. 조직 repo 쪽으로 옮기는 것이 단계 6.
- `/process-plan` Phase −2 (git branch 격리)는 vault 가 있는 repo 에서 branch 를 만든다는 전제다. 조직 루트가 별도 repo 가 되었으므로 git 작업은 `{ORG_ROOT}` 에서 해야 한다 (공통 절에 원칙만 명시, 커맨드 본문 보강은 단계 6~7).
- 사용자 가이드 4종 · 사용자_매뉴얼은 `vault/`, `.claude/runs/` 리터럴로 설명한다. 조직 루트 기준으로 읽는다. 본문 갱신은 후속 과제.
- 에이전트가 호출하는 `python3 -m tools.vault_rules` 는 환경변수 `PROCESSWARE_ORG_ROOT` 를 상속받아야 한다. 커맨드가 `--org-root` 로 받은 값은 하위 호출 전에 export 한다.

---

## 7. 관련 문서

- `derivative-products.md` — 3-Vault 생태계 (코어 + RFP-to-Proposal + Project Asset Generator). 분리 축이 프로덕트인 반면, 본 문서의 분리 축은 조직.
- `../표준프로세스_AI관리체계_4차원PDCA.md` §Phase 5 — SaaS 멀티테넌트 로드맵.
- `../전용AI에이전트_프레임워크_설계안.md` — 내부 툴 → B2B → SaaS 단계, 멀티테넌트 DB 스키마 · 격리 전략 (미결 항목 C).
- `../../vault/00_공통관리/07_표준분류레지스트리.md` — 영역코드 22종 (표준 단위 분리의 현재 기준).
