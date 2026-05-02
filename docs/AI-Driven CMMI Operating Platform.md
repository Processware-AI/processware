---
type: vision
title: "AI-Driven CMMI Operating Platform"
version: "0.1"
status: draft
created: 2026-05-01
updated: 2026-05-01
tags: [vision, CMMI, AI-Agent, automation, ML4, ML5]
---

# AI-Driven CMMI Operating Platform

> 본 문서는 CMMI 의 ML3 표준 자동 생성을 넘어, ML4(정량 관리)·ML5(최적화) 까지 **AI Agent 가 운영을 직접 수행**하는 플랫폼 비전을 정리한다.

상위 문서: [[표준프로세스_구성원칙]] · [[표준프로세스_AI관리체계_4차원PDCA]] · [[전용AI에이전트_프레임워크_설계안]]

---

## 1. 문제 의식

ML 단계가 올라갈수록 **사람이 부담해야 하는 정량·통계·분석 작업**이 폭증한다. 전통적으로 이는 SEPG·PMO·통계 전문가의 수작업으로 처리되어 왔고, 그 결과:

- ML3 도달도 12~24개월 소요
- ML4 도달은 대기업·전담 조직 한정
- ML5 운영은 극소수 글로벌 기업만 가능
- 인증 후 **회귀(degradation)**가 심각 — 심사 통과 후 6개월 내 KPI 추락 사례 다수

**핵심 통찰**: ML 단계가 올라갈수록 요구되는 작업의 본질이 **"데이터 기반 정량 관리 + 최적화"** 이며, 이는 LLM/AI Agent 가 가장 잘 수행하는 영역과 정확히 정합한다.

---

## 2. ML 단계별 본질 ↔ AI 자동화 적합성

| ML | 본질 | 사람 부담 | AI 자동화 적합성 |
|---|---|---|---|
| ML2 | 관리 (Managed) | 반복적 기록·보고서 | 중 (RPA 수준) |
| ML3 | 정의·일관성 (Defined) | 표준 문서화·교육 | **고** — 본 프로젝트의 `/plan-process` 하네스가 이미 처리 |
| **ML4** | **정량 관리 (Quantitatively Managed)** | **통계 분석·SPC·baseline** | **매우 고** — AI 가 가장 강한 영역 |
| **ML5** | **최적화 (Optimizing)** | **RCA·혁신 발굴·예측** | **매우 고** — LLM 추론·생성 영역 |

ML 이 올라갈수록 **AI 우위**가 극대화된다.

---

## 3. CMMI Practice ↔ AI Agent 매핑

| CMMI Practice (PG4/PG5) | 사람 수행 시 부담 | AI Agent 자동화 |
|---|---|---|
| MPM PG4 — 측정 데이터 수집 | 매월 수동 집계 | `metric-collector` agent (CI/CD·이슈트래커·코드품질 도구에서 자동 수집) |
| MPM PG4 — Process Performance Baseline | 통계학 전공 필요 | `baseline-analyzer` agent (시계열 분석·outlier 탐지) |
| MPM PG4 — SPC (Statistical Process Control) | 컨트롤 차트 수동 작성 | `spc-monitor` agent (실시간 control limit 알림) |
| MPM PG5 — 사업 KPI 연계 | 임원 대시보드 manual | `bizkpi-aligner` agent (OKR ↔ 프로세스 KPI 매핑) |
| **CAR PG4** — 통계적 근본원인분석 | 5Why·Fishbone 수작업 | `rca-agent` (인시던트 로그 → LLM 인과 추론 + 통계 검정) |
| **CAR PG5** — 공통 원인 식별 | 데이터 마이닝 전문가 | `common-cause-detector` agent (군집 분석·상관관계) |
| **OT PG5** — 학습조직 | HR 담당자 manual | `learning-recommender` agent (역량 gap → 교육 추천) |
| **PCM PG5** — 프로세스 혁신 | SEPG manual | `process-innovator` agent (외부 best practice 학습 → 제안) |
| QPM (Quantitative Project Management) | PMO 통계 분석 | `qpm-agent` (프로젝트 데이터 → 예측 모델) |

---

## 4. 제안 아키텍처 — 3-Layer Operating Platform

본 프로젝트의 `build-process` 하네스 위에 운영 레이어를 적층한다.

```
┌──────────────────────────────────────────────────────────────────┐
│  Layer 3: 자동 최적화 (ML5)                                       │
│  ─────────────────────────                                        │
│  • process-innovator         외부 best practice 학습 → 제안          │
│  • common-cause-detector     공통 원인 변동 식별                    │
│  • improvement-orchestrator  PDCA 사이클 자동 운영                  │
├──────────────────────────────────────────────────────────────────┤
│  Layer 2: 정량 관리 (ML4)                                         │
│  ───────────────────────                                          │
│  • metric-collector          CI/CD·도구 연동, 자동 수집              │
│  • baseline-analyzer         Process Performance Baseline 산출      │
│  • spc-monitor               Control Chart·Outlier 알림             │
│  • rca-agent                 LLM 인과 추론 + 통계 검정              │
│  • qpm-agent                 정량 프로젝트 관리·예측                │
├──────────────────────────────────────────────────────────────────┤
│  Layer 1: 정의·일관성 (ML3) — ✅ 본 프로젝트가 이미 보유            │
│  ────────────────────────────────────────────                     │
│  • standard-analyzer    표준 요구사항 분해                          │
│  • process-designer     POL/PRO 설계                              │
│  • wi-tmp-writer        WI/TMP/EX 생성                            │
│  • traceability-mapper  추적성 매트릭스                            │
│  • qa-reviewer          전수 QA 감사                              │
├──────────────────────────────────────────────────────────────────┤
│  Layer 0: 데이터 기반                                              │
│  ──────────────                                                    │
│  vault/ + 측정저장소(MR) + PAL + 인시던트 DB + CI/CD 파이프라인       │
└──────────────────────────────────────────────────────────────────┘
```

**핵심 원리**: 상위 Layer 의 Agent 는 하위 Layer 의 산출물을 입력으로 사용한다.
- Layer 1 의 POL/PRO/WI/TMP → Layer 2 Agent 의 **행동 명세서**
- Layer 2 의 측정 데이터·baseline → Layer 3 Agent 의 **분석 입력**

---

## 5. 단계적 로드맵

### Phase 1 (현재 완료) — Layer 1 ML3
- `/plan-process` 하네스 + 5개 핵심 에이전트
- CMMI-DEV-ML3 산출물 459건 생성 사례 보유
- branch-per-standard 운영 정책 확립

### Phase 2 (단기 4~8주) — Layer 2 PoC
- `metric-collector` 시범 — CMMI 측정저장소(MR)에 CI/CD 데이터 자동 적재
- `rca-agent` 시범 — 인시던트 발생 시 자동 RCA 초안 생성
- 측정 대상: PRO-CMMI-204 (MPM) / PRO-CMMI-403 (CAR) 의 KPI 5개 이상

### Phase 3 (중기 3~6개월) — Layer 2 풀 패키지
- SPC·baseline 자동화 + QPM 연계
- ML4 산출물 신규 빌드: `/plan-process CMMI-DEV-ML4`
- PRO/WI 의 KPI·예외 처리 분기가 Agent 호출로 실행

### Phase 4 (장기 6~12개월) — Layer 3 ML5 자동화
- 공통 원인 탐지·혁신 제안·학습조직 자동화
- "AI 가 지속 개선 사이클을 운영하는 조직" 모델 검증
- ML5 산출물 빌드: `/plan-process CMMI-DEV-ML5`

---

## 6. 본 vault 와의 결정적 연결

기존에 만든 산출물이 운영 자동화의 **계약서** 역할을 한다:

| 본 프로젝트 산출물 | Agent 운영 시 역할 |
|---|---|
| POL/PRO/WI 의 입력·출력 정의 | Agent 의 input/output 스펙 |
| TMP 양식 | Agent 출력 schema (JSON Schema 변환 가능) |
| MAT-011 추적성 매트릭스 | Agent 실행 추적·증적 |
| WI §5.3 Definition of Done | Agent 종료 조건 |
| WI §7 예외 처리 | Agent 의 error handling 분기 |
| KPI | Agent 자기 평가 기준 (self-evaluation) |

즉 **`/plan-process` 가 만든 문서가 AI Agent 의 행동 명세서로 직결**된다. 이는 일반 표준 도입과의 본질적 차이이며, 차별화의 핵심이다.

---

## 7. 차별화 포인트 (전통 컨설팅 대비)

| 차원 | 전통 CMMI 컨설팅 | AI-Driven CMMI Platform |
|---|---|---|
| ML3 도달 시간 | 12~24 개월 | **수일** (`/plan-process`) |
| ML4 도달 가능성 | 대기업 한정 | **모든 조직** (Agent 가 통계 처리) |
| ML5 운영 비용 | 매우 고가 (전문가 다수) | **저비용** (Agent 가 24/7 운영) |
| 회귀(degradation) 방지 | 수동 내부심사 (연 1~2회) | **자동 모니터링** (실시간) |
| 산출물 ↔ 운영 연결 | 종이 문서 → 사람이 해석 | **계약서 직결** (Agent 가 직접 실행) |
| 다중 표준 통합 | 표준별 별도 컨설팅 | **branch-per-standard** + 공통 운영 레이어 |

---

## 8. 기술 스택 후보

| 영역 | 후보 기술 |
|---|---|
| Agent 프레임워크 | Claude Agent SDK / LangGraph / AutoGen |
| 측정 데이터 수집 | OpenTelemetry / Prometheus / GitHub Actions API |
| 통계 분석 | Python (statsmodels·scipy) / R |
| Vector DB (RAG) | Pinecone / Weaviate / Postgres+pgvector |
| 워크플로우 | Temporal / Airflow / Dagster |
| 대시보드 | Grafana / Metabase / Superset |
| 데이터 레이크 | DuckDB / BigQuery / Snowflake |

---

## 9. 위험·고려사항

1. **Agent 환각(hallucination)** — 통계 결과·RCA 결론에 LLM 환각 시 잘못된 의사결정. → 통계 검증 도구를 Tool Use 로 강제 호출, LLM 단독 추론 금지.
2. **데이터 거버넌스** — 측정저장소 접근 권한·개인정보·기밀 데이터. → ISO 27001/27701 통합 운영 필요 (본 하네스로 추가 표준 빌드 가능).
3. **Auditability** — CMMI 평가관이 AI Agent 결과물을 증적으로 수용할지. → MAT-011 처럼 Agent 실행 로그 전수 추적성 확보 필수.
4. **모델 변경 리스크** — LLM 모델 업그레이드 시 동일 입력에 다른 출력. → Agent 별 model version pinning + regression test.
5. **사람 검토 루프** — ML5 혁신 제안은 인간 승인이 최종 단계. → human-in-the-loop 필수 지점 명시 (PCB 승인·경영검토 등).

---

## 10. 다음 행동 옵션

- **A**. ML4 운영 Agent **개념 설계 문서** 작성 — 본 비전을 구체 스펙으로 분해 (Layer 2 5개 Agent)
- **B**. `/plan-process CMMI-DEV-ML4` 로 ML4 산출물 먼저 빌드 → 그 위에 Agent 운영
- **C**. ML4 Agent 1종 PoC 구현 (`rca-agent` 또는 `metric-collector` 권장)
- **D**. 대외 발표·제안용 비전 페이퍼·로드맵 작성

권장 순서: **A → C → B → D**
1. 비전 → 구체 설계 (지금 본 문서가 비전, A 가 설계)
2. PoC 로 가능성 검증
3. 정식 표준 산출물 빌드
4. 사례 확보 후 대외 확장

---

## 11. 결론

본 프로젝트는 시작점부터 단순 "표준 문서 자동 생성"을 목표로 하지 않았다. **"AI 가 표준 자체를 운영하는 살아있는 시스템"** 이 본질적 비전이며, ML4/ML5 자동화는 그 비전의 자연스러운 다음 단계이다.

`/plan-process` 하네스 (Layer 1) 는 운영 자동화 (Layer 2/3) 의 **기반 인프라** 다. 표준 산출물이 Agent 의 명세서로 직결되는 구조는, 전통 컨설팅·일반 RPA·범용 LLM 자동화 모두와 명확히 차별화되는 전략적 자산이다.

**ML5 까지 자동화한 첫 조직** 은 글로벌 시장에서 정의되지 않은 위치에 선다. 이것이 본 비전의 도달 좌표다.
