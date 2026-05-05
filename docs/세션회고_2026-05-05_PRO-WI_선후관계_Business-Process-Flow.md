---
type: session-recap
date: 2026-05-05
title: "PRO/WI 선후 관계 + Business Flow / Process Flow 이중 레이어 설계"
participants: ["dongseok"]
commits:
  - 2266325  # feat: PRO/WI 선후 관계 + Business/Process Flow 이중 레이어 설계
tags: [session, flow, sequencing, business-flow, process-flow, PRO, WI, ingest, plan]
---

# 세션 회고 — 2026-05-05 (2)

## 1. 출발점

미결 항목 4가지 중 **WI 시간적 선후 관계**를 먼저 논의하기로 했다.

논의 초반 핵심 전환: "WI만 보면 반쪽짜리"  
→ WI 간 선후 관계뿐 아니라 **PRO 간 선후 관계**까지 동시에 설계해야 함.

---

## 2. 핵심 논의 흐름

### 2-1. 선후 관계의 두 계층

```
Level 1: PRO 간 선후 관계 (macro)
  PRO-001 → PRO-002 → PRO-003

Level 2: PRO 내 WI 시퀀스 (micro)
  PRO-002 안에서: WI-010 → WI-011 → WI-012
```

**결론**: 두 계층 모두 **설계 시점(process-plan)** 에 문서에 박아야 한다. 런타임 상태가 아님.

### 2-2. 선후 관계 정의 위치

PRO 내 WI 시퀀스는 PRO 생성 시점에 결정 가능.  
PRO 간 선후 관계는 모든 PRO가 만들어진 후에야 전체 그림이 보임.

**결론**:
- PRO 내 WI 시퀀스 → `process-designer` 확장 (PRO 생성 시 `wi_sequence[]` 포함)
- PRO 간 선후 관계 → `flow-mapper` 에이전트 신설 (plan 파이프라인 phase 3.5)

### 2-3. flow-mapper 단독 실행 가능성

사용자: "flow-mapper만 따로 실행시킬 수 있나?"

에이전트는 직접 호출 불가. 해결:  
→ `/process-plan --flow` 서브모드 신설 (새 최상위 커맨드 없이 단독 실행 가능)

### 2-4. Business Flow / Process Flow 구분 (핵심 결정)

사용자가 두 레이어를 명확히 분리:

| | Business Flow | Process Flow |
|---|---|---|
| **단계** | Ingest (차원 0) | Plan (차원 1) |
| **관점** | 업무 경로 — 조직이 실제로 하는 일 | 절차 — 표준을 충족하는 방법 |
| **특성** | 핵심 업무 중심, 지원(QA/CM) 생략 가능 | 핵심 PRO + 지원 PRO 연계 포함 |
| **저장** | `inputs/06_목표흐름/business_flow.yaml` | MAT-010 + PRO frontmatter |
| **생성** | flow-proposer + HITL | flow-mapper (파생) |

**연결 고리**: process-designer가 business_flow.yaml을 읽어 PRO를 설계 → flow-mapper가 PRO frontmatter를 읽어 MAT-010 생성.

### 2-5. inputs/06_목표흐름/ 신설

기존 `04_AsIs/`(현재 상태) 와 분리 이유:  
→ "표준 프로세스를 만든다는 건 현재 상태가 아니라 미래 상태를 계획하는 것"

**결론**: `inputs/06_목표흐름/business_flow.yaml` 신설. 사람이 직접 수정 가능.

### 2-6. 시나리오 기반 도출

단순히 "표준 구조 관점 3~5개"가 아니라, **표준이 적용되는 조직에서 발생하는 업무 시나리오를 최대한 시뮬레이션**해서 도출.

**표준 구조 기반 이유**: 산업 특성 판단은 사람의 영역. 시스템은 표준 구조 하에서 가능한 흐름을 제시하면 됨.

**HITL 방식**: 2~3레벨 그룹핑 목록 제시 (Level 1: 업무 성격 / Level 2: 도메인 묶음 / Level 3: 개별 시나리오)  
→ 번호·그룹 단위 포함/제외 + 추가 시나리오 요구 가능.

### 2-7. Actor 제외 결정

사용자: "ingest 단계에서 actor가 도출될 수 있을까?"

→ ingest 시점에는 조직 구조를 알 수 없음. 표준은 역할을 추상적으로만 정의.  
**결론**: actor는 business_flow에서 제외. RACI는 process-designer가 PRO 생성 시 결정.

역할 분리:
```
business_flow: WHAT + 어떤 순서로 + core/support 구분
PRO/RACI:      WHO (실제 조직 역할)
WI steps:      HOW (세부 절차)
```

### 2-8. MAT-010 파생 문서 원칙 유지

기존 MAT-001~009와 동일하게 파생 문서로 유지.  
사람이 흐름을 수정하고 싶으면 → `business_flow.yaml` 수정 → `/process-plan --flow` 재실행.  
MAT-010 직접 수정은 의미 없음 (다음 실행 시 덮어씌워짐).

---

## 3. 확정된 스키마

### business_flow.yaml

```yaml
standard_basis: [ISO-27001]
generated_at: "ISO8601"
confirmed_at: "ISO8601"

scenario_groups:
  - id: SG-1
    name: 핵심 운영 프로세스
    sub_groups:
      - id: SG-1-1
        name: 시스템·서비스 관리
        scenarios: [SC-001, SC-002]

scenarios:
  - id: SC-001
    name: 신규 시스템 도입 시 보안 흐름
    type: main          # main | exception | support
    standard_clauses: ["ISO 27001 §8.1"]
    nodes:
      - id: 보안요구분석
        label: 보안 요구사항 분석
        type: core       # core | support (actor 없음)
        standard_clause: "ISO 27001 §8.1"
    edges:
      - from: 보안요구분석
        to: 위험평가
    mermaid: |
      flowchart LR
        A[보안요구분석] --> B[위험평가]
```

### PRO frontmatter 추가 필드

```yaml
pro_type: core              # core | support
source_scenarios: [SC-001]  # 추적성
follows: [PRO-001]          # PRO 간 선후관계
precedes: [PRO-003]
wi_sequence:                # child_wi[] 대체
  - wi_id: WI-001
    mandatory: true
    entry_condition: null
  - wi_id: WI-002
    mandatory: true
    entry_condition: "WI-001.status == done"
```

### WI frontmatter 추가 필드

```yaml
entry_gate: "WI-001.status == done"   # null이면 즉시 시작 가능 (soft warning)
```

---

## 4. 구현 내용

**신규 에이전트 2개:**
- `flow-proposer.md`: process-ingest Phase 9 — 표준 분석 → 시나리오 도출 → HITL → business_flow.yaml 저장
- `flow-mapper.md`: process-plan Phase 3.5 — PRO frontmatter 읽어 MAT-010 생성 (파생 문서)

**수정 파일 5개:**

| 파일 | 주요 변경 |
|---|---|
| `process-designer.md` | `child_wi[]` → `wi_sequence[]`, `pro_type`/`source_scenarios`/`follows`/`precedes` 추가, business_flow.yaml 읽기 단계(Phase 0-3) 신설 |
| `wi-tmp-writer.md` | `wi_sequence` 기준으로 전환, WI `entry_gate` 필드 추가, L-4 검증에 entry_gate 교차 확인 추가 |
| `process-executor.md` | `entry_gate` soft warning 체크(A-1-gate), PRO `wi_sequence` 위치 파악 추가 |
| `process-plan.md` | Phase 3.5 Flow(flow-mapper) 추가, `--flow` 플래그 신설 |
| `process-ingest.md` | `inputs/06_목표흐름/` 폴더 추가, Phase 9(flow-proposer 자동 호출) 추가 |

---

## 5. 미결 항목 현황

| 항목 | 상태 |
|---|---|
| PRO/WI 선후 관계 | ✅ 구현 완료 |
| REC 백필 (기존 문서 → REC 변환) | 미구현 |
| process-audit → process-act 자동 트리거 | 미구현 |
| 외부 인증기관 보고서 포맷 (XLSX/PDF) | 미구현 |

---

## 6. 핵심 결정 요약

**"WI만 보면 반쪽짜리 — PRO 간 선후 관계도 함께"**  
두 계층(PRO 간 / PRO 내 WI 시퀀스) 모두 설계 시점에 문서화.

**"Business Flow와 Process Flow는 다른 레이어"**  
ingest(업무 경로, 핵심 중심) vs plan(핵심+지원 PRO 연계). process-designer가 변환 담당.

**"MAT-010은 파생 문서, inputs/06_목표흐름/이 진실의 원천"**  
사람이 흐름을 수정하는 인터페이스는 business_flow.yaml. MAT-010 직접 수정 안 함.

**"Actor는 business_flow에서 제외"**  
ingest 시점에 조직 구조 알 수 없음. RACI는 process-designer가 PRO 생성 시 결정.

**"시나리오는 몇 가지 관점이 아니라 업무 케이스 시뮬레이션"**  
표준 구조 기반으로 실제 발생 가능한 업무 케이스를 최대한 도출. 2~3레벨 그룹핑 후 HITL 선택.
