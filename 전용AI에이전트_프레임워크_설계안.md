# 전용 AI Agent 프레임워크 설계 제안

> 현재 Claude Code 하네스로 검증된 개념을 **독립 실행 프레임워크**로 승격시키는 방향 설계안.
> 작성일: 2026-04-17 · 최종 갱신: 2026-05-02 · 상태: 하네스 검증 완료 · Python 포팅 설계 진행 중
> 관련: [[표준프로세스_구성원칙]], 현 하네스(`.claude/agents/`, `.claude/commands/`)

> **하네스 현황 (2026-05-02)**: **4차원 PDCA 폐쇄 루프 PoC 완료** — 차원 1~4 전체 구현·통합 완료(main 머지, commit be900cc). 총 23 에이전트 / 4 슬래시 커맨드 운영 중. 주요 구현 기능 — 계층적 문서 번호 체계(POL→PRO→WI 계보 추적), 표준 분류 레지스트리(Layer/Structure/Integration Mode 3축), 자동차 4종·의료기기 4종 도메인 지원, MAT 9종(001~009) 운영, WI 이중 포맷(MD+steps.yaml), HITL 다단계 승인·타임아웃·에스컬레이션, 심사 9 에이전트 + RBAC 6 역할 + NCR + KPI 대시보드, RCA·PCB quorum·폐쇄 루프 Act→Plan' 재트리거, Phase 4.5 외부 인프라 연동 명세(OIDC·Slack·Jira·한국 영업일·Mermaid 자동 트렌드). 포팅 범위 및 구현 패턴 모두 명확히 정립됨.

---

## 0. 전체 프레임워크 범위 — 4차원 PDCA

표준 프로세스 관리는 4개 차원이 순환하는 PDCA 구조다. 상세 개념: `표준프로세스_AI관리체계_4차원PDCA.md`

| 차원 | PDCA | 슬래시 | 에이전트 | 핵심 산출물 | 현황 |
|---|---|---|---|---|---|
| 1 자산 구축 | Plan | `/build-standard` | 5종 (analyzer·designer·wi-writer·mapper·qa) | POL/PRO/WI/TMP/EX/MAT/REF | **구현됨** |
| 2 이행·관리 | Do | `/do` | 5종 (router·executor·hitl·rec-writer·escalation) | REC + MAT-005/007 | **구현됨** |
| 3 심사·평가 | Check | `/audit` | 9종 (planner·collector·checker·reporter·ncr·kpi×2·independence·trigger) | REC-AUDIT/NCR + MAT-008/009 + act queue | **구현됨** |
| 4 제개정 | Act | `/act` | 4종 (rca·planner·pcb·coordinator) | As-Is 입력 + MAT-001 §개정이력 + 차원 1 재트리거 | **구현됨** |

> **이 설계안의 범위**: 4차원 PDCA 전체가 Claude Code 하네스에서 검증 완료됨. 다음 단계는 **하네스 → 독립 실행 Python 프레임워크 포팅**. 차원 2~4 구현 패턴이 정립되어 포팅 설계 범위도 함께 갱신됨.

---

## 1. 전략 결정

### 1-A. 선택지 맵

| 축 | 옵션 A | 옵션 B | 옵션 C | **결정** |
|---|---|---|---|---|
| **사용자 범위** | 내부 컨설팅 툴 | 컨설팅 펌 B2B | 멀티테넌트 SaaS | 내부 툴 → B2B → SaaS (단계적) |
| **배포 형태** | CLI / 데스크탑 | 온프렘 서버 | 클라우드 | 단계적 |
| **데이터 저장** | 로컬 Vault만 | Vault + 서버 DB | 클라우드 DB + Git | 단계적 |
| **진입 UI** | CLI | 웹 대시보드 | Obsidian 플러그인 | 단계적 |
| **LLM 모델** | Claude 전용 | **멀티 프로바이더** | BYO Key | **멀티 프로바이더** ✅ |

### 1-B. 결정 완료 항목

| # | 항목 | 결정 |
|---|---|---|
| 1 | **패키지명** | `processmine` (PyPI 등록 예정) |
| 2 | **LLM 모델** | 멀티 프로바이더 지향 — Claude 우선 구현 후 OpenAI·Gemini·온프렘 LLM 추상화 레이어 추가 |
| 3 | **언어** | Python (미결 → 섹션 1-C 참조) |
| 4 | **오픈소스/상용** | 미결 |
| 5 | **Obsidian 유지 여부** | 미결 |

### 1-C. 미결 결정 항목

1. **언어**: Python 전용 vs TypeScript vs 양쪽?
2. **타겟 고객 최소단위**: 1인 컨설턴트 vs 10인 펌 vs 100인 기업
3. **Obsidian 유지 여부**: 계속 핵심 UI로 / 웹 UI 대체 / 둘 다
4. **오픈소스/상용**: 코어 OSS + 상용 부가기능(멀티테넌트·지식팩) 여부
5. **프레임워크**: Claude Agent SDK 단독 vs SDK + LangGraph 하이브리드

---

## 2. 필수 구성 요소 (프레임워크 무관)

```
┌──────────────────────────────────────────────────────────┐
│                   Entry Points                            │
│    CLI   │   HTTP API   │   Web UI   │  Obsidian Plugin  │
└────────────────────────┬─────────────────────────────────┘
                         │
┌────────────────────────▼─────────────────────────────────┐
│                 Orchestrator (Graph/Plan)                 │
│   · Pipeline DSL (analyze→design→write→trace→QA)         │
│   · Human-in-the-Loop 게이트 (심사원 검수)                │
│   · Retry / Backoff / Partial resume                      │
└────────────────────────┬─────────────────────────────────┘
                         │
      ┌──────────────────┼──────────────────┐
      │                  │                  │
┌─────▼──────┐   ┌──────▼──────┐   ┌───────▼────────┐
│   Agent    │   │    Tool     │   │    Memory      │
│  Registry  │   │  Registry   │   │   / RAG        │
│            │   │  (MCP 호환) │   │                │
│ analyzer   │   │ vault-fs    │   │ 표준 카탈로그  │
│ designer   │   │ obsidian    │   │ 요구사항 DB    │
│ wi-writer  │   │ web-search  │   │ 과거 산출물    │
│ mapper     │   │ git-commit  │   │ 조직별 테일러링│
│ qa-review  │   │ legal-db    │   │ (pgvector)     │
└────────────┘   └─────────────┘   └────────────────┘
                         │
┌────────────────────────▼─────────────────────────────────┐
│               Cross-Cutting Services                      │
│  Audit Log · Tracing(OTel) · RBAC · Secrets · Billing    │
└──────────────────────────────────────────────────────────┘
                         │
┌────────────────────────▼─────────────────────────────────┐
│                    Storage                                │
│  Vault(MD) │ Postgres │ Object(S3) │ Git │ Vector(pgv)   │
└──────────────────────────────────────────────────────────┘
```

**핵심 포인트**
- **MCP 호환 Tool 레지스트리** — Obsidian, GitHub, 법령DB, ISO.org 같은 외부소스 플러그인으로
- **Audit Log는 필수** — 심사증적으로 직접 쓰일 수 있어야 함(MAT-005와 연동)
- **Human-in-the-Loop** — 심사원/Process Owner 가 승인해야 다음 단계 진행
- **Vault를 Git + DB 이중 저장** — 버전 추적(Git) + 쿼리(DB)

---

## 3. 프레임워크 비교

| 프레임워크 | 장점 | 단점 | 적합도 |
|---|---|---|---|
| **Claude Agent SDK** | 현 하네스 개념 그대로 이식. 서브에이전트·MCP 네이티브 | Claude 종속 — 멀티 프로바이더 지향 시 추상화 레이어 필요 | ★★★★★ (1순위, MVP) |
| **LangGraph** | 그래프 기반 상태머신·재개·HITL 강력. 멀티 프로바이더 LLM 지원 | 학습곡선·상태모델 복잡 | ★★★★ (오케스트레이션 레이어) |
| **CrewAI** | 역할 기반 다중에이전트 직관적 | 프로덕션 성숙도 부족 | ★★ |
| **AutoGen** | 대화형 에이전트 강점 | 구조적 파이프라인엔 과잉 | ★★ |
| **직접 구축** | 최대 자유도 | 6개월+ 재발명 | ★ (비추) |

**결정: Claude Agent SDK + LangGraph 하이브리드**
- 에이전트 실행: Claude Agent SDK (서브에이전트/MCP 패턴 그대로, MVP 우선)
- 파이프라인 오케스트레이션: LangGraph (체크포인트·재개·HITL)
- **멀티 프로바이더 전략**: `LLMProvider` 추상화 인터페이스 → Claude / OpenAI / Gemini / 온프렘(Ollama 등) 교체 가능하도록 설계. MVP는 Claude 전용으로 시작 후 인터페이스 분리.

MVP 단계는 **Claude Agent SDK 전용**으로 시작해 LLM 추상화 레이어를 이후 적용.

---

## 4. 제안 아키텍처 (Python 기준)

```
processmine/                              ← 프레임워크 패키지명 예시 (processmine — Process + Mine (내 프로세스를 채굴·정제))
├── core/
│   ├── orchestrator.py          ← 파이프라인 엔진 (4차원 PDCA 폐쇄 루프 포함)
│   ├── agent_registry.py
│   ├── tool_registry.py         ← MCP 서버 로더
│   └── state.py                 ← 체크포인트 (_state.yaml → Python State 객체)
├── agents/
│   ├── dim1_plan/               ← 차원 1 (5종) — .claude/agents/ 포팅
│   │   ├── standard_analyzer.py
│   │   ├── process_designer.py
│   │   ├── wi_tmp_writer.py
│   │   ├── traceability_mapper.py
│   │   └── qa_reviewer.py
│   ├── dim2_do/                 ← 차원 2 (5종) — /do 하네스 포팅
│   │   ├── process_router.py    ← MAT-007 자연어 라우팅
│   │   ├── process_executor.py  ← steps.yaml 로드·멀티턴 실행
│   │   ├── hitl_gatekeeper.py   ← 다단계 승인·타임아웃·에스컬레이션
│   │   ├── rec_writer.py        ← REC 생성 + MAT-005 기록
│   │   └── escalation_coordinator.py
│   ├── dim3_check/              ← 차원 3 (9종) — /audit 하네스 포팅
│   │   ├── audit_planner.py
│   │   ├── evidence_collector.py
│   │   ├── compliance_checker.py ← 4-tier verdict
│   │   ├── audit_reporter.py
│   │   ├── ncr_drafter.py       ← SLA 휴리스틱 + R/A 추정
│   │   ├── kpi_collector.py
│   │   ├── kpi_analyzer.py      ← 회귀 탐지 + Mermaid 트렌드
│   │   ├── independence_guard.py ← auditor ≠ executor 검증
│   │   └── act_trigger.py       ← act queue 자동 발행
│   └── dim4_act/                ← 차원 4 (4종) — /act 하네스 포팅
│       ├── rca_analyzer.py      ← 5-Why / Fishbone
│       ├── revision_planner.py  ← 5종 rebuild_mode 결정
│       ├── pcb_gatekeeper.py    ← quorum 4 모드
│       └── act_coordinator.py   ← As-Is 생성 + 차원 1 재트리거
├── queues/                      ← 차원 3→4 폐쇄 루프 큐
│   └── act/                     ← queue-q*.yaml (NCR/KPI→Act 인계)
├── tools/                       ← MCP 서버들
│   ├── vault_fs/                ← Obsidian vault 읽기/쓰기
│   ├── standards_catalog/       ← ISO/IEC/KS 메타DB
│   ├── legal_kr/                ← 국가법령정보센터 API
│   └── git_sync/                ← vault ↔ Git
├── standards/                   ← 표준별 지식팩 (현 하네스의 표준분류레지스트리 패턴 이식)
│   ├── registry.yaml            ← Layer/Structure/Integration Mode 3축 메타
│   ├── iso9001/
│   │   ├── meta.yaml            ← layer/structure/integration_mode/scope_codes
│   │   └── _inputs/             ← 표준원문·법규·해설서·As-Is
│   ├── iso27001/
│   └── ...                      ← L1 9종 + L2 8종 + L3 1종 (총 18종)
├── templates/                   ← T03~T15 템플릿 (현 vault/99_템플릿/)
│   └── wi_steps_schema.yaml     ← steps.yaml Pydantic 스키마
├── utils/                       ← Phase 4.5 유틸리티
│   ├── business_days_kr.py      ← 한국 영업일 계산기
│   ├── pcb_quorum.py            ← quorum 4 모드
│   └── auto_trend_mermaid.py    ← Mermaid 자동 트렌드
├── api/                         ← FastAPI 엔드포인트
├── cli/                         ← typer CLI (processmine build-standard ISO9001)
├── web/                         ← Next.js 대시보드 (선택)
└── audit/                       ← 감사증적 로거 (OTel)
```

**데이터 레이어**
- **Postgres**: 테넌트·프로젝트·표준 카탈로그·실행 이력
- **Git (서버사이드 Gitea 등)**: 각 테넌트의 vault 버전 관리
- **pgvector**: 표준 조항·법령·과거 산출물 RAG
- **S3 호환**: 첨부증적·대용량 REC

---

## 5. MVP 로드맵 (4단계)

> **현황 요약**: 하네스에서 차원 1~4 전체가 PoC 검증 완료됨. 아래 Phase 1~2 에서 "하네스 검증됨" 표기된 항목은 Python 포팅 시 구현 패턴이 명확히 정립된 상태.

### Phase 1. 코어 포팅 — 차원 1 (핵심 기능 확보)
- 현 `.claude/agents/*.md` → Python 에이전트 클래스로 이식 (5종) ← *하네스 검증됨*
- Claude Agent SDK로 서브에이전트 호출 재현
- CLI 1개: `processmine build-standard ISO9001 --vault ./vault`
- Obsidian vault 쓰기 기능 검증
- **체크포인트·자가수정 루프** 이식 (`_state.yaml` 패턴 → Python State 객체) ← *하네스 검증됨*
- **표준 분류 레지스트리** 이식 (`registry.yaml` + Layer/Structure/Integration Mode 분기 로직) ← *하네스 검증됨*
- **계층적 문서 번호 생성기** (POL→PRO→WI 번호 계승 규칙) 구현 ← *하네스 검증됨*
- **멀티도메인 지원**: hls_merge / quasi_hls_merge / interface_only / reference_only 4가지 Integration Mode 분기 ← *하네스 검증됨*
- 현재 지원 표준 범위 재현: L1 9종 + L2 8종 + L3 1종 (총 18종) ← *하네스 검증됨*
- **WI 이중 포맷 출력**: `wi-tmp-writer`가 WI-*.md (사람용) + WI-*.steps.yaml (Agent 실행용) 동시 생성 ← *하네스 검증됨*

### Phase 2. 프레임워크화 — 차원 2~4 포팅
- Orchestrator 서버 + MCP 기반 Tool Registry
- 감사증적 (JSONL + OTel)
- 표준 카탈로그 DB (ISO/IEC/KS 메타 — Phase 1의 `registry.yaml` DB 승격)
- **Process Execution Agent (차원 2)**: steps.yaml 로드 → 대화식 이행 → REC 생성 → HITL 다단계 승인·타임아웃·에스컬레이션 ← *하네스 검증됨 (8 진입 모드, MAT-007 자연어 라우팅)*
- **Audit Agent (차원 3)**: REC↔PRO/WI 대조 + NCR 발행 + KPI 대시보드 + RBAC 6 역할 + act queue 발행 ← *하네스 검증됨 (9 에이전트)*
- **Act Agent (차원 4)**: RCA + PCB quorum + As-Is 생성 + 차원 1 재트리거 ← *하네스 검증됨 (4 에이전트 + 폐쇄 루프 PoC)*
- **Phase 4.5 외부 연동 명세** 이식: OIDC·Slack·Jira·한국 영업일·Mermaid 자동 트렌드 ← *하네스 명세 완료*

### Phase 3. B2B 배포 가능한 상태
- HTTP API + 인증(RBAC)
- Docker Compose 온프렘 배포 키트
- 웹 대시보드 (실행 상태·산출물 브라우저·심사증적)
- Human-in-the-Loop 승인 UI

### Phase 4. SaaS화
- 멀티테넌트·결제·Git 분리
- RAG 지식팩 마켓플레이스(표준별 프리셋 판매)

---

## 6. 기술적 도전 포인트 (미리 알아야 할 것)

| 이슈 | 대응 |
|---|---|
| LLM 비환각 보장 | 각 에이전트 출력을 **스키마 검증** + RAG 근거 링크 강제 |
| 대용량 표준 원문 | 조항 단위 청크 + hybrid search (BM25 + vector) |
| 개정판 추적 | 표준 카탈로그에 `version`·`effective_date`·`superseded_by` |
| 고객 데이터 격리 | 테넌트별 vault·DB 스키마 분리, 키 BYO 옵션 |
| 심사 증적 무결성 | Git hash + 서명(sigstore) 로 추적증적 |
| AI 결과 책임 | 모든 산출물 `generated_by: claude-sonnet-4-6`, `reviewed_by: human` 필드 |
| **계층 번호 무결성** | POL 번호 변경 시 하위 PRO·WI 번호 연쇄 갱신 — 번호 생성기에 cascading update 로직 필수 *(하네스 패턴 확립됨)* |
| **Integration Mode 혼재 방지** | interface_only 표준이 HLS 영역코드 문서에 섞이는 레이어 혼재 → QA 체크 + 자동 분리 규칙 *(하네스 패턴 확립됨)* |
| **WI 이중 포맷 동기화** | MD(서술형)와 steps.yaml(구조화)이 항상 동일 버전을 유지해야 함 — 개정 시 둘 다 갱신, 버전 불일치는 차원 3 QA에서 부적합 처리 *(하네스 검증됨)* |
| **steps.yaml 완전성 보장** | `wi-tmp-writer`가 LLM으로 steps.yaml 생성 시 모든 TMP 필드가 outputs에 매핑되었는지 스키마 검증 필수 *(하네스 검증됨)* |
| **HITL 다단계·타임아웃 이식** | review→approve→final chain + SLA 만료 시 escalate_to[] 자동 발송 — 차원 2 하네스의 8 진입 모드 패턴 Python 재현 *(하네스 검증됨)* |
| **심사 독립성 강제** | auditor ≠ trace.executed_by 검증 + RBAC 6 역할 — independence-guard 패턴 Python 재현 *(하네스 검증됨)* |
| **폐쇄 루프 act queue 자동 발행** | 차원 3 NCR/KPI → `.claude/queues/act/` 자동 push → 차원 4 RCA → PCB → 차원 1 재트리거 — 전체 루프 패턴 *(하네스 PoC 실증됨)* |
| **PCB quorum 다단계** | simple_majority / supermajority / unanimous / chair_veto 4 모드 — Phase 4.5 명세 완료 *(Python 이식 대상)* |
| **LLM API 운영 비용** | 23 에이전트 자동 실행 시 대용량 컨텍스트 → per-run 토큰 비용이 제품 단가 설계에 직결. 표준 분석 1회 예상 토큰량 측정 후 과금 모델 설계 필요 — **검토 필요** |

---

## 7. 결론 및 첫 수

**가능하고 준비됐다.** 하네스에서 4차원 PDCA 전체(23 에이전트, 폐쇄 루프 PoC)가 검증 완료됨. 남은 것은 **실행 엔진을 Claude Code CLI 에서 떼어내는 것**. 각 차원의 구현 패턴이 명확히 정립되어 포팅 범위와 비용을 정확히 예측할 수 있는 상태.

**가장 현실적인 첫 수**:
> "Python + Claude Agent SDK 로 현 `.claude/agents/*` 를 포팅 → `processmine build-standard ISO9001` CLI 1개로 차원 1 재현 → `LLMProvider` 추상화 레이어 삽입(멀티 프로바이더 기반 확보) → 차원 2~4 에이전트 순차 포팅 → Phase 3 배포 키트"

→ Phase 1 MVP 예상 소요: **4~6주** (차원 1 코어 — 계층 번호 생성기·표준 분류 레지스트리·멀티도메인 Integration Mode 분기 포함)
→ Phase 2 포팅 소요: **6~8주** (차원 2~4 에이전트 + 폐쇄 루프 Orchestrator + Phase 4.5 외부 연동 기반 구현)
→ **하네스 검증 덕분에 설계 리스크가 기존 예상 대비 크게 감소함.**

---

## 9. 후속 심화 검토 주제

### 9-A. 미착수 — Python 포팅 시 신규 설계 필요

- [ ] (A) Phase 1 MVP 코드베이스 골격 생성 (디렉터리·주요 파일 스캐폴딩)
- [ ] (B) Claude Agent SDK vs LangGraph 상세 비교 + 의사결정
- [ ] (C) 멀티테넌트 SaaS 아키텍처 상세 (DB 스키마·격리 전략)
- [ ] (D) 지식팩(표준 카탈로그·RAG) 구조 설계 — `07_표준분류레지스트리.md` + `_inputs/` 패턴을 YAML 스키마로 정형화하는 것이 출발점
- [ ] (E) 감사증적 + HITL 워크플로우 Python 포팅 상세
- [ ] (F) 사업화 연계 (사업 모델 문서와 이 설계안의 접점)
- [ ] (M) Phase 4.5 외부 연동 Python 구현 — OIDC/SCIM 통합, Slack/Jira webhook, 한국 영업일 라이브러리 선정

### 9-B. 하네스 검증 완료 — 포팅 패턴 확립됨

- ✅ (G) 계층 번호 생성기 — POL→PRO→WI cascading update, 번호 충돌 탐지, REC 버전 예외 처리 → Python 클래스로 이식
- ✅ (H) Integration Mode 별 E2E 검증 — hls_merge/quasi_hls_merge/interface_only/reference_only 18종 표준 커버 → 포팅 시 pytest E2E 정의
- ✅ (I) WI steps.yaml 스키마 — field types, required_if, HITL approver_role, TMP 필드 매핑 → Pydantic 스키마로 정형화
- ✅ (J) Process Execution Agent — steps.yaml 로드·멀티턴·REC 생성 (차원 2 하네스 8 진입 모드 검증)
- ✅ (K) Audit Agent — REC↔PRO/WI 대조·NCR·KPI 대시보드·independence-guard (차원 3 하네스 9 에이전트 검증)
- ✅ (L) Act Agent — RCA·PCB quorum·차원 1 재트리거·폐쇄 루프 (차원 4 하네스 + PoC 실증)

---

## 참고 관련 문서 (프로젝트 내)
- 전체 구성원칙: `vault/01_구성원칙/표준프로세스_구성원칙.md`
- 현 하네스 README: `README.md`
- 현 에이전트 정의: `.claude/agents/*.md`
- 문서체계·번호체계: `vault/00_공통관리/01_문서체계.md`, `02_문서번호체계.md`
- 표준 분류 레지스트리: `vault/00_공통관리/07_표준분류레지스트리.md`
