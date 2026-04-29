# 전용 AI Agent 프레임워크 설계 제안

> 현재 Claude Code 하네스로 검증된 개념을 **독립 실행 프레임워크**로 승격시키는 방향 설계안.
> 작성일: 2026-04-17 · 최종 갱신: 2026-04-23 · 상태: draft (depth 검토 예정)
> 관련: [[표준프로세스_구성원칙]], 현 하네스(`.claude/agents/`, `.claude/commands/`)

> **하네스 현황 (2026-04-23)**: 작성 이후 추가 검증된 핵심 기능 — 계층적 문서 번호 체계(POL→PRO→WI 계보 추적), 표준 분류 레지스트리(Layer/Structure/Integration Mode 3축), 자동차 4종·의료기기 4종 도메인 지원, MAT-006 문서계층추적매트릭스, MAT 번호 구역 체계(001~010 전사공통 / 011~099 표준별 / 100+ 예약), WI/TMP/EX 전수 생성 강제. 포팅 범위가 초기 예상보다 넓어졌으나 각 기능의 구현 패턴이 명확히 정립됨.

---

## 0. 전체 프레임워크 범위 — 4차원 PDCA

표준 프로세스 관리는 4개 차원이 순환하는 PDCA 구조다. 상세 개념: `표준프로세스_AI관리체계_4차원PDCA.md`

| 차원 | PDCA | 핵심 산출물 | 현황 |
|---|---|---|---|
| 1 자산 구축 | Plan | POL/PRO/WI/TMP/EX/MAT/REF | **구현됨** (현 하네스) |
| 2 이행·관리 | Do | REC (기록본) | 미설계 |
| 3 심사·평가 | Check | 심사 보고서·NCR | 미설계 |
| 4 제개정 | Act | 개정 POL/PRO/WI | 미설계 |

> **이 설계안의 범위**: 차원 1 독립 제품화. 차원 2~4는 차원 1 검증 이후 단계적 확장 대상.

---

## 1. 먼저 확정할 선택지

| 축 | 옵션 A | 옵션 B | 옵션 C |
|---|---|---|---|
| **사용자 범위** | 내부 컨설팅 툴 | 컨설팅 펌 B2B | 멀티테넌트 SaaS |
| **배포 형태** | CLI / 데스크탑 | 온프렘 서버 | 클라우드 |
| **데이터 저장** | 로컬 Vault만 | Vault + 서버 DB | 클라우드 DB + Git |
| **진입 UI** | CLI | 웹 대시보드 | Obsidian 플러그인 |
| **LLM 모델** | Claude 전용 | 멀티 프로바이더 | BYO Key |

어느 조합을 노리냐에 따라 프레임워크 규모가 3배 이상 달라짐.
**추천 진화 경로**: 내부 툴 → B2B 온프렘 → SaaS (단계적)

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
| **Claude Agent SDK** | 현 하네스 개념 그대로 이식. 서브에이전트·MCP 네이티브 | Claude 종속 | ★★★★★ (1순위) |
| **LangGraph** | 그래프 기반 상태머신·재개·HITL 강력 | 학습곡선·상태모델 복잡 | ★★★★ (복잡 워크플로우면) |
| **CrewAI** | 역할 기반 다중에이전트 직관적 | 프로덕션 성숙도 부족 | ★★ |
| **AutoGen** | 대화형 에이전트 강점 | 구조적 파이프라인엔 과잉 | ★★ |
| **직접 구축** | 최대 자유도 | 6개월+ 재발명 | ★ (비추) |

**추천: Claude Agent SDK + LangGraph 하이브리드**
- 에이전트 실행: Claude Agent SDK (서브에이전트/MCP 패턴 그대로)
- 파이프라인 오케스트레이션: LangGraph (체크포인트·재개·HITL)

MVP 단계는 **Claude Agent SDK 전용**도 충분함.

---

## 4. 제안 아키텍처 (Python 기준)

```
spx/                              ← 프레임워크 패키지명 예시 (SPX=Standard Process eXpert)
├── core/
│   ├── orchestrator.py          ← 파이프라인 엔진
│   ├── agent_registry.py
│   ├── tool_registry.py         ← MCP 서버 로더
│   └── state.py                 ← 체크포인트
├── agents/                      ← 현 .claude/agents/ 포팅
│   ├── standard_analyzer.py
│   ├── process_designer.py
│   ├── wi_tmp_writer.py
│   ├── traceability_mapper.py
│   └── qa_reviewer.py
├── tools/                       ← MCP 서버들
│   ├── vault_fs/                ← Obsidian vault 읽기/쓰기
│   ├── standards_catalog/       ← ISO/IEC/KS 메타DB
│   ├── legal_kr/                ← 국가법령정보센터 API
│   └── git_sync/                ← vault ↔ Git
├── standards/                   ← 표준별 지식팩 (현 하네스의 표준분류레지스트리 패턴 이식)
│   ├── registry.yaml            ← Layer/Structure/Integration Mode 3축 메타 (현 07_표준분류레지스트리.md 정형화)
│   ├── iso9001/
│   │   ├── meta.yaml            ← layer/structure/integration_mode/scope_codes
│   │   └── _inputs/             ← 표준원문·법규·해설서·As-Is (현 _inputs/ 패턴)
│   ├── iso27001/
│   └── ...                      ← 현재 L1 9종 + L2 8종 + L3 1종 지원
├── templates/                   ← T03~T15 템플릿 (현 vault/99_템플릿/)
│   └── wi_steps_schema.yaml     ← steps.yaml 생성 스키마 (차원 2 Agent 실행 정의)
├── api/                         ← FastAPI 엔드포인트
├── cli/                         ← typer CLI (spx build-standard ISO9001)
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

### Phase 1. 코어 포팅 (핵심 기능 확보)
- 현 `.claude/agents/*.md` → Python 에이전트 클래스로 이식 (5종)
- Claude Agent SDK로 서브에이전트 호출 재현
- CLI 1개: `spx build-standard ISO9001 --vault ./vault`
- Obsidian vault 쓰기 기능 검증
- **체크포인트·자가수정 루프** 이식 (`_state.yaml` 패턴 → Python State 객체)
- **표준 분류 레지스트리** 이식 (`registry.yaml` + Layer/Structure/Integration Mode 분기 로직)
- **계층적 문서 번호 생성기** (POL→PRO→WI 번호 계승 규칙) 구현
- **멀티도메인 지원**: hls_merge / quasi_hls_merge / interface_only / reference_only 4가지 Integration Mode 분기
- 현재 지원 표준 범위 재현: L1 9종 + L2 8종 + L3 1종 (총 18종)
- **WI 이중 포맷 출력**: `wi-tmp-writer`가 WI-*.md (사람용) + WI-*.steps.yaml (Agent 실행용) 동시 생성

### Phase 2. 프레임워크화
- Orchestrator 서버 + MCP 기반 Tool Registry
- 감사증적 (JSONL + OTel)
- 표준 카탈로그 DB (ISO/IEC/KS 메타 — Phase 1의 `registry.yaml` DB 승격)
- **Process Execution Agent (차원 2 MVP)**: steps.yaml 로드 → 대화식 이행 → REC 생성 → HITL 승인 라우팅

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
| **계층 번호 무결성** | POL 번호 변경 시 하위 PRO·WI 번호 연쇄 갱신 — 번호 생성기에 cascading update 로직 필수 |
| **Integration Mode 혼재 방지** | interface_only 표준이 HLS 영역코드 문서에 섞이는 레이어 혼재 → QA 체크 + 자동 분리 규칙 |
| **WI 이중 포맷 동기화** | MD(서술형)와 steps.yaml(구조화)이 항상 동일 버전을 유지해야 함 — 개정 시 둘 다 갱신, 버전 불일치는 차원 3 QA에서 부적합 처리 |
| **steps.yaml 완전성 보장** | `wi-tmp-writer`가 LLM으로 steps.yaml 생성 시 모든 TMP 필드가 outputs에 매핑되었는지 스키마 검증 필수 |

---

## 7. 즉시 결정 필요한 항목

1. **언어**: Python(SDK 1순위) vs TypeScript vs 양쪽?
2. **타겟 고객 최소단위**: 1인 컨설턴트 vs 10인 펌 vs 100인 기업
3. **Obsidian 유지 여부**: 계속 핵심 UI로 쓸지, 웹 UI로 대체할지, 둘 다 지원할지
4. **오픈소스 / 상용**: 코어는 OSS 두고 상용 부가기능(멀티테넌트·지식팩)만 판매할지
5. **단독 빌드 vs 파운데이션 활용**: 완전 자체 구현 vs Claude Agent SDK + LangGraph 조합

---

## 8. 결론 및 첫 수

**가능하다.** 현재 하네스는 이미 "설계 수준"에서 프레임워크의 씨앗이 거의 다 들어가 있음. 남은 것은 **실행 엔진을 Claude Code CLI 에서 떼어내는 것**. Claude Agent SDK 가 그 용도로 만들어진 도구이므로 포팅 비용은 예상보다 작음.

**가장 현실적인 첫 수**:
> "Python + Claude Agent SDK 로 현 `.claude/agents/*` 를 포팅 → CLI 1개로 ISO 9001 구축 재현 → 거기서부터 기능 확장"

→ Phase 1 MVP 예상 소요: **4~6주** (초기 예상 2~4주에서 상향 조정 — 계층 번호 생성기·표준 분류 레지스트리·멀티도메인 Integration Mode 분기가 추가 포팅 범위에 포함).

---

## 9. 후속 심화 검토 주제 (다음 세션 용)

- [ ] (A) Phase 1 MVP 코드베이스 골격 생성 (디렉터리·주요 파일 스캐폴딩)
- [ ] (B) Claude Agent SDK vs LangGraph 상세 비교 + 의사결정
- [ ] (C) 멀티테넌트 SaaS 아키텍처 상세 (DB 스키마·격리 전략)
- [ ] (D) 지식팩(표준 카탈로그·RAG) 구조 설계 — 현 `07_표준분류레지스트리.md` + `_inputs/` 패턴을 YAML 스키마로 정형화하는 것이 출발점
- [ ] (E) 감사증적 + HITL 워크플로우 상세
- [ ] (F) 사업화 연계 (사업 모델 문서와 이 설계안의 접점)
- [ ] (G) 계층 번호 생성기 설계 — POL 번호 변경 시 cascading update 로직, 번호 충돌 탐지, REC 버전 예외 처리
- [ ] (H) Integration Mode 별 테스트 케이스 정의 — hls_merge/quasi_hls_merge/interface_only/reference_only 각 1종 이상 E2E 검증
- [ ] (I) WI steps.yaml 스키마 정의 — field types(text/enum/person/date/boolean), required_if 조건식, HITL approver_role 목록, TMP 필드 매핑 규칙
- [ ] (J) Process Execution Agent 설계 — steps.yaml 로드 → 대화 세션 관리 → 컨텍스트 유지 → 멀티턴 완료 시 REC 생성 흐름

---

## 참고 관련 문서 (프로젝트 내)
- 전체 구성원칙: `vault/01_구성원칙/표준프로세스_구성원칙.md`
- 현 하네스 README: `README.md`
- 현 에이전트 정의: `.claude/agents/*.md`
- 문서체계·번호체계: `vault/00_공통관리/01_문서체계.md`, `02_문서번호체계.md`
- 표준 분류 레지스트리: `vault/00_공통관리/07_표준분류레지스트리.md`
