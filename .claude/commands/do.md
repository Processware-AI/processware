---
description: 표준 프로세스 실행 (차원 2 Do) — WI 1건을 대화식으로 이행하고 REC(기록)를 자동 작성. 사용: /do <WI번호 또는 자연어>
argument-hint: "<WI번호 | 자연어 키워드> [--dry-run] [--executor <이름>] [--auto-approve]"
---

# 표준 프로세스 실행 하네스 (차원 2 Do)

대상 입력: **$ARGUMENTS**

본 커맨드는 `/build-standard` 가 만들어 놓은 자산(WI/TMP/EX/PRO/POL)을 **계약서**로 삼아, AI Agent 가 사람과 대화하며 절차를 이행하고 REC(기록본)를 자동 작성한다.

상위 설계: `표준프로세스_AI관리체계_4차원PDCA.md` §3 "차원 2 — DO" / §5.3 "WI 이중 포맷"

---

## 0. 실행 원칙

- **자산은 읽기 전용**: POL/PRO/WI/TMP/EX 는 본 커맨드가 절대 수정하지 않는다 (개정은 차원 4·1의 책임).
- **REC 만 신규 생성**: 산출물은 `vault/08_REC_기록/` 에만 쓴다.
- **MAT-005 만 갱신**: 추적성은 MAT-005 의 `## 실행 기록 (운영 인스턴스)` 섹션에 1행 append.
- **모든 입력·LLM 출력 전수 로그**: `.claude/runs/{trace_id}/trace.jsonl` (심사 증적).
- **환각 방지**: TMP 필드에 직접 매핑 가능한 값만 REC 에 기록한다. 매핑 불가능한 자유 서술이 필요하면 사람에게 추가 질문.
- **HITL 강제 정지**: WI §5.3 "완료 조건" 에 "승인" 표현이 있거나, WI §2 "수행 주체" 의 "승인자" 역할이 있으면 반드시 사람 승인 게이트 발동 (Phase 1 에서는 게이트 검출만, 승인은 모킹).

---

## 1. 인자 파싱

### 1-1. 직접 지정 (Phase 1 권장)
```
/do WI-CMMI-04-01-03
/do WI-CMMI-04-01-03_작업산출물_평가_v1.0
```
→ 정확 매칭으로 WI 파일 1건 결정.

### 1-2. 자연어 (Phase 3 에서 확장)
```
/do 작업산출물 평가
/do 산출물 검토 시작
```
→ Phase 1 단계에서는 **자연어가 들어오면 후보 WI 목록을 보여주고 사용자에게 선택을 요청** 한다 (process-router 미구현 상태이므로).

### 1-3. 옵션
| 플래그 | 효과 |
|---|---|
| `--dry-run` | 대화는 진행하되 REC 파일은 쓰지 않고 미리보기만 출력 |
| `--executor <이름>` | 실행자(작성자) 명시. 미지정 시 시스템 사용자명 자동 인식 시도 |
| `--auto-approve` | HITL 게이트를 자동 승인으로 모킹 (Phase 1 PoC 검증용 — 실운영 금지) |
| `--resume <trace_id>` | 이전 실행을 이어서 재개 (Phase 2 에서 정식 지원, Phase 1 은 검출만) |

---

## 2. 실행 시퀀스

### Phase A. 사전 점검
A-1. 인자에서 WI 식별. 매칭 실패 시 후보 목록 출력 후 종료.
A-2. WI 파일 Read 성공 확인. frontmatter 의 다음 필드 추출:
   - `doc_id`, `parent_pro`, `parent_pol`, `related_tmp[]`, `related_ex[]`, `owner`, `reviewer`, `approver`, `standards`, `scope_code`
A-3. **TMP 필수 확인**: `related_tmp[]` 가 비어 있으면 실행 중단 (REC 산출 불가 — TMP 부재).
A-4. trace_id 생성 (예: `run-` + 8자 hex).
A-5. `.claude/runs/{trace_id}/` 디렉터리 생성 + `state.yaml` 초기화.

### Phase B. process-executor 위임
B-1. 서브에이전트 `process-executor` 를 다음 컨텍스트로 호출:
```
[입력]
- wi_path:   vault/05_WI_업무지침/{WI파일}
- tmp_path:  vault/06_TMP_템플릿/{TMP파일}
- ex_path:   vault/07_EX_작성예시/{EX파일}  (있으면)
- pro_path:  vault/04_PRO_절차/{PRO파일}    (있으면)
- trace_id:  run-xxxxxxxx
- executor:  {사용자명}
- options:   {dry_run, auto_approve}

[출력]
- step 별 대화 진행
- state.yaml 갱신
- trace.jsonl 1라인/이벤트
- 모든 step 완료 시 .claude/runs/{trace_id}/rec_payload.yaml 생성
```

B-2. process-executor 가 모든 step 을 처리하고 `state.status: ready_to_finalize` 로 만들면 Phase C 로.
B-3. HITL 게이트 만나면 `state.status: pending_approval` + 사용자에게 안내 후 종료(Phase 2 에서 재개 메커니즘 정식화).

### Phase C. rec-writer 위임
C-1. 서브에이전트 `rec-writer` 호출:
```
[입력]
- trace_id: run-xxxxxxxx
- rec_payload: .claude/runs/{trace_id}/rec_payload.yaml
- options: {dry_run}

[작업]
- REC 파일명 결정 (다음 일련번호 자동 산출)
- TMP 양식 구조에 payload 매핑 → REC 파일 생성
- MAT-005 §"실행 기록" 섹션에 1행 append
- state.yaml 의 final_rec_path 갱신
- trace.jsonl 마감 이벤트 기록
```

C-2. dry-run 인 경우 REC 미리보기만 출력하고 저장하지 않는다.

### Phase D. 종결 보고
- ✅ 생성된 REC 파일 경로
- 📍 MAT-005 갱신 행 인용
- 🔍 trace_id (감사증적)
- ⏸ HITL 미해결 시: 승인자·승인 게이트 정보
- ⚠ 부분 실패 시: 실패 step·복구 방법

---

## 3. trace_id·state·로그 규약

### 3-1. 디렉터리 구조
```
.claude/runs/{trace_id}/
├── state.yaml          ← 실행 상태 (재개·HITL 대기)
├── trace.jsonl         ← 입력·LLM 출력·승인 전수 로그
└── rec_payload.yaml    ← process-executor → rec-writer 인계용
```

### 3-2. `state.yaml` 스키마
```yaml
trace_id: run-a3f9c2b1
wi_id: WI-CMMI-04-01-03
wi_path: vault/05_WI_업무지침/WI-CMMI-04-01-03_...md
tmp_path: vault/06_TMP_템플릿/TMP-CMMI-04-01-03-01_...md
ex_path:  vault/07_EX_작성예시/EX-CMMI-04-01-03-01_...md
pro_path: vault/04_PRO_절차/PRO-CMMI-04-01_...md
status: running | pending_approval | ready_to_finalize | completed | aborted
started_at: "ISO8601"
executed_by: "{사용자명}"
options:
  dry_run: false
  auto_approve: false
current_step: step-04
steps:
  - id: step-01
    name: 표본 선정
    status: done
    answers:
      sample_items: ["요구사항 등록부", "설계서"]
hitl:
  required: true
  approver_role: "PM"
  approver_name: null         # 응답 후 채워짐
  decision: null              # approved | rejected
  requested_at: null
  responded_at: null
final_rec_path: null
finalized_at: null
```

### 3-3. `trace.jsonl` 이벤트 종류
- `start` — 실행 시작
- `step_enter` — step 진입
- `question` — Agent → 사람 질문 (step / field / prompt)
- `answer` — 사람 → Agent 응답 (값 + 검증 결과)
- `derivation` — 처리 규칙 자동 적용 (예: 점수 합산 → 등급)
- `step_done` — step 종료
- `hitl_request` — 승인 요청 발송
- `hitl_response` — 승인 응답 수신
- `rec_drafted` — REC 초안 작성 완료
- `rec_finalized` — REC 파일 저장 완료
- `mat005_updated` — MAT-005 행 추가
- `aborted` — 중단 사유 기록

---

## 4. Phase 1 범위 명시 (현 단계)

본 커맨드는 다음 4 Phase 로 점진 구축된다. 현재는 **Phase 1**.

| Phase | 포함 | 제외 |
|---|---|---|
| **1 (지금)** | 직접 WI 지정 / 단일 step 대화 / TMP 매핑 / REC 1건 생성 / MAT-005 1행 / trace 로그 | 자연어 라우팅 / HITL 정식 / 멀티턴 재개 |
| 2 | HITL 게이트 정지·재개 / `--resume` / state 영속 | 자연어 라우팅 / 외부 알림 채널 |
| 3 | process-router / MAT-007 카탈로그 / 자연어 매칭 | 외부 시스템 연동 |
| 4 | wi-tmp-writer 확장 (steps.yaml 정식 출력) / steps.yaml ↔ MD 동기화 | — |

---

## 5. 안전 가드

- 본 커맨드 실행 중 `vault/03~07_*` (자산 영역) 의 어떤 파일도 **수정하지 않는다**. 검증 위반 즉시 중단.
- `vault/08_REC_기록/` 와 `vault/90_MAT_통합매핑/MAT-005_*.md` 만 쓰기 허용.
- main / feat 브랜치에 직접 push 금지. 커밋은 사용자가 명시 요청 시에만.
- `--dry-run` 외 모드에서 REC 파일을 동일 경로로 덮어쓰는 것은 금지 (일련번호 충돌 시 다음 번호로 진행).

---

## 6. 최종 보고 양식

```
✅ 실행 완료 — WI-CMMI-04-01-03 작업산출물 평가
📁 REC: vault/08_REC_기록/REC-CMMI-04-01-03-01-2026-001_작업산출물_평가서.md
📋 MAT-005 갱신: 실행 기록 섹션 1행 append
🔍 trace_id: run-a3f9c2b1  (.claude/runs/run-a3f9c2b1/)
👤 실행자: {사용자명}
⏸ HITL: required=true / approver=PM / decision=approved (mock)
⏱ 소요 시간: 4분 12초
```
