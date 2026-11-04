---
type: architecture
title: 조직 계층 도입 설계 방향 — 플랫폼 1 + 조직 루트 N
version: "0.2"
status: draft
updated: 2026-11-04
decided:
  - "2026-11-04: 조직 루트는 플랫폼 repo 밖 별도 repo 로 둔다"
  - "2026-11-04: 공개 표준 ingest 산출물은 조직 루트에 둔다 (조직 간 공유 지식 팩 없음)"
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
│   └── org/                        ← 신규: init / switch / sync-core / validate
└── core/vault_base/                ← 00_공통관리 · 01_구성원칙 · 99_템플릿 + 폴더 README + MAT-001~009 빈 양식

{ORG_ROOT}/                         ← 조직 루트 (조직별 별도 git repo — 결정)
├── org.yaml                        ← org_id · 명칭 · 사용 영역코드 · rbac 사용자 배정 · redmine 매핑
├── sources/                        ← 조직이 투하한 원본 파일 (표준 PDF · 법규 · AsIs, 저작권 · 기밀)
├── inputs/                         ← /process-ingest 산출물 전체 (공개 표준 포함, 조직 루트에 둠 — 결정)
│   ├── 01_표준원문 · 02_법규 · 03_해설서 · 05_산업가이드
│   ├── 04_AsIs/                    ← 조직 내부 자산 (기밀)
│   └── 06_목표흐름/                ← business_flow.yaml / .md
├── vault/                          ← Obsidian vault — 자기완결
│   ├── 00_공통관리 · 01_구성원칙 · 99_템플릿   ← core/vault_base 에서 sync-core 로 복사된 사본
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
| **1. 조직 컨텍스트 도입** | `PROCESSWARE_ORG_ROOT` 환경변수 또는 모든 커맨드의 `--org` 옵션으로 활성 조직을 정한다. 미지정 시 현재 `vault/` 를 `default` 조직으로 취급해 하위 호환을 유지한다. | 커맨드 9 |
| **2. 경로 추상화** | 에이전트 · 커맨드 38개 중 **30개** 가 `vault/08_REC_기록` 같은 경로를 하드코딩하고 있다 (08_REC 68회 · 90_MAT 38회 · 05_WI 19회 · 02_적용요건 19회 …). 이를 `{VAULT}` · `{RUNS}` · `{QUEUES}` · `{STATES}` 변수로 치환한다. `tools/vault_rules` 는 이미 `--vault` 루트 인자를 받으므로 그대로 쓴다. | 에이전트 · 커맨드 30 |
| **3. 스캐폴드 도구** | `python -m tools.org init {org_id}` 가 조직 루트를 생성하고 `core/vault_base` 를 복사한다. 현재 `vault/` 는 첫 조직(`default`) 으로 마이그레이션한다. | 신규 `tools/org/` |
| **4. RBAC 조직화** | 현재 `policy.yaml` 은 역할 6종 정의만 있고 **사용자 배정이 없다**. 역할 정의는 플랫폼 템플릿으로 남기고, 사용자→역할 배정과 audit_log 는 `org.yaml` 로 내린다. independence-guard 는 활성 조직 파일만 읽는다. | independence-guard · policy.yaml |
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
| 3 | 3-Vault 파생 프로덕트와의 관계 | 파생 ②(Project Asset Generator) 는 "조직의 코어 vault" 를 입력으로 받음 | 조직 컨텍스트(`PROCESSWARE_ORG_ROOT`) 를 파생 프로덕트에도 같은 환경변수로 전달 |
| 4 | 하위 호환 기간 | `default` 조직 fallback 을 언제까지 유지할지 | 단계 3 마이그레이션 완료 후 제거 |

---

## 6. 관련 문서

- `derivative-products.md` — 3-Vault 생태계 (코어 + RFP-to-Proposal + Project Asset Generator). 분리 축이 프로덕트인 반면, 본 문서의 분리 축은 조직.
- `../표준프로세스_AI관리체계_4차원PDCA.md` §Phase 5 — SaaS 멀티테넌트 로드맵.
- `../전용AI에이전트_프레임워크_설계안.md` — 내부 툴 → B2B → SaaS 단계, 멀티테넌트 DB 스키마 · 격리 전략 (미결 항목 C).
- `../../vault/00_공통관리/07_표준분류레지스트리.md` — 영역코드 22종 (표준 단위 분리의 현재 기준).
