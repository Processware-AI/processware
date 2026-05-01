---
type: asis-feedback
source: act-cycle
queue_id: queue-qa1b2c3d4
trace_id: run-c4f8a1b2
generated_at: "2026-05-02T14:25:14+09:00"
generated_by: "act-coordinator (claude-opus-4-7)"
priority: critical
related_audit_trace: run-a1c2d3e4
related_kpi_trace:   run-k4f8d2a1
related_ncr: REC-NCR-04-01-2026-001
pcb_approved_at: "2026-05-02T14:15:01+09:00"
pcb_approver: "(auto-approved Phase1 PoC)"
target_asset: PRO-CMMI-04-01
target_sections: ["§5-6 종결 추적", "§7 KPI"]
rebuild_command: "/build-standard CMMI-DEV-ML3 --from write --target PRO-CMMI-04-01"
expected_next_version: "1.1"
tags: [asis-feedback, act-cycle, NCR-001, F-001, critical]
---

# As-Is 피드백 — queue-qa1b2c3d4 (NCR-001 critical)

> 본 파일은 차원 4 (Act) 사이클이 차원 1 (Plan) 빌드에 인계하는 **개정 입력**입니다.
> `/build-standard CMMI-DEV-ML3 --from write --target PRO-CMMI-04-01` 실행 시 process-designer / wi-tmp-writer 가 본 파일을 읽고 개정에 반영합니다.

## 1. 모(母) 사이클 추적성

| 단계 | 식별자 | 결과 |
|---|---|---|
| 차원 3 audit | [[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]] | finding F-001 critical (REQ-005 PRO §5-6) |
| 차원 3 NCR | [[REC-NCR-04-01-2026-001_REQ-005_critical_종결추적]] | status: open / SLA 2026-05-30 |
| 차원 3 KPI | run-k4f8d2a1 | KPI-04-01-02 / META-FINDINGS-DENSITY / META-NCR-CLOSURE 통합 (root cause 동일) |
| 차원 4 큐 | [[queue-qa1b2c3d4]] | priority: critical / status: in_progress → done |
| 차원 4 trace | run-c4f8a1b2 | status: completed |
| PCB 승인 | (auto-approved Phase1 PoC) | 2026-05-02 14:15 KST |

## 2. 근본 원인 (RCA 요약)

PRO-CMMI-04-01 §5-6 의 "종결 추적" 절차에 종결 기한 SLA 가 정의되지 않아, 부적합 발견 시 "추적" 의 종결 시점이 운영 자율에 맡겨지고 있음. 그 결과 REC-04-01-03-001 / REC-04-01-04-002 두 trace 모두 재점검·재실행이 지연되어 KPI '부적합 종결율 ≥ 95%' 와 '평균 종결 기간 ≤ 20영업일' 이 동시 미달. 5-Why depth 5 — high confidence.

**Primary**: method — PRO §5-6 SLA 미정의 (종결 시점·책임자 일정 관리 책임 분리 부재)
**Secondary** (통합 후보): measurement — KPI 측정 기준 시점과 절차 시점의 분리

## 3. 개정 요청 (구체 사항)

### 3-1. PRO-CMMI-04-01 §5-6 종결 추적 — 개정 요구

**현재 (v1.0)** — `vault/04_PRO_절차/PRO-CMMI-04-01_*.md` §5 단계별 상세 6번 행:

> "6 | 종결 추적 | 시정조치 종결까지 추적 | QA | 시정조치 | 종결 기록"

**개정 요구 (process-designer 가 차원 1 빌드 시 결정)**:
1. **종결 시점 SLA 명시** — 등급별 (critical 20영업일 / major 60일 / minor 90일) — `/audit ncr-drafter` 의 SLA 휴리스틱과 정합.
2. **종결 책임자 (R) 와 일정 관리 책임자 (A) 분리** — RACI 표 §3 와 정합 (현재 R: QA / A: PCB 인데, 일정 관리 A 는 PM 권장).
3. **종결 기한 경과 시 에스컬레이션 트리거** — SLA 50% 경과 시 PM 자동 알림, 100% 경과 시 PCB 보고.

**예상 v1.1 §5 표 6번 행 (process-designer 최종 결정)**:

> "6 | 종결 추적 | QA(R) 가 부적합 등급별 SLA (critical 20영업일/major 60일/minor 90일) 안에 종결 추적. 일정 관리 PM(A). SLA 50% 경과 시 PM 자동 알림, 100% 경과 시 PCB 보고. | QA, PM | 시정조치 + SLA | 종결 기록 + SLA 준수 표기"

### 3-2. PRO-CMMI-04-01 §7 KPI — 정합 갱신

**현재 (v1.0)** — §7 표 3번째 행:

> "부적합 평균 종결 기간 | 발견→종결 | ≤ 20 영업일 | 분기"

**개정 요구**:
1. "**발견**" 기준 시점을 §5-6 의 "**부적합 식별 (WI-04-01-01) 시점**" 으로 명시.
2. "**종결**" 기준 시점을 §5-6 의 "**종결 합의 (capa_rec 발행) 시점**" 으로 명시.
3. **측정 보고서 산출물 (TMP) 정의** — 별도 큐 (queue-qe5f6a7b8 / queue-q9d8c7b6a) 와 통합 처리 권장.

## 4. 영향 자산 (정합 검증 필요)

| 자산 | 관계 | 영향 | qa-reviewer 검증 |
|---|---|---|---|
| WI-CMMI-04-01-03 | child_of_pro | DoD 의 종결 시점이 PRO §5-6 SLA 와 정합 | §11-A WI ↔ steps.yaml + §11-D 개정 정합 (Phase 4.5) |
| WI-CMMI-04-01-04 | child_of_pro | 다단계 승인 SLA 와 정합 (queue-qf1e2d3c4 와 통합 후보) | 동일 |

## 5. Not Affected 자산

| 자산 | 이유 |
|---|---|
| WI-CMMI-04-01-01 | 본 root cause 와 무관 — 별도 큐 (queue-q5a6b7c8d META-COVERAGE) 처리 |
| WI-CMMI-04-01-05 | 본 root cause 와 무관 — 별도 큐 처리 |
| POL-CMMI-04 | POL 변경 불필요 — PRO 수준 SLA 정의로 충분 |

## 6. 기존 운영 trace (As-Is 인용)

본 PRO 의 v1.0 운영 결과 — 차원 1 빌드가 이 데이터를 read-only 로 참조:

- run-b7d4e3c5 (WI-04-01-03 / 2026-05-01) — final, DoD 부적합 종결 ❌ (재점검 약속만 있고 미수행)
- run-c5f8a9d2 (WI-04-01-04 / 2026-05-01) — final, 다단계 승인 정상 (대조 사례)
- run-d8a3f6b7 (WI-04-01-04 / 2026-05-01) — rejected, Sponsor 미참석 (NCR-004)

> 위 trace 들은 v1.0 기준이며 개정 후 v1.1 부터 신규 trace 가 누적됩니다. **MAT-005 §실행기록의 "적용 표준 버전" 컬럼 신설 권장** (차원 1 빌드 시 검토).

## 7. 위험 요인

- **정합성 위험**: PRO §5-6 개정이 자식 WI (-03/-04) 의 DoD 와 충돌 가능 — qa-reviewer §11-A 검증 필수.
- **기존 운영 영향**: MAT-005 §실행기록 trace 3건이 v1.0 기준 — 개정 후 trace 의 "적용 표준 버전" 명시 필요.
- **다중 큐 통합 미수행**: 본 As-Is 는 단일 큐 PoC. queue-qe5f6a7b8 / q9d8c7b6a / qf1e2d3c4 의 root cause 와 일부 겹침 — Phase 2 다중 큐 일괄 처리 후속 사이클로 분리.

## 8. 권장 단계 (사이클 진행 상황)

1. ✅ **backup** (사용자 작업) — `git tag pre-revision/PRO-CMMI-04-01-v1.0`
2. ▶ **rebuild** (사용자 차원 1 실행) — `/build-standard CMMI-DEV-ML3 --from write --target PRO-CMMI-04-01`
3. ▶ **validate** (자동 — qa-reviewer)
4. ✅ **register** (완료 — 본 시점) — MAT-001 §개정 이력 1행 추가
5. ▶ **close_ncr** (사용자) — `/audit --close-ncr REC-NCR-04-01-2026-001 --capa <개정판 PRO 의 후속 REC>`
6. ▶ **re_kpi** (qmr) — `/audit --kpi start CMMI-DEV-ML3 --period 2026-04-01..2026-06-30` (회차 2 baseline 비교 자동)

## 9. 구성원칙 §8 준수

본 개정은 **기존 PRO-CMMI-04-01 의 §5-6 / §7 확장** 이며 신규 PRO 생성이 아닙니다.
표준프로세스_구성원칙.md §8 ("동일 목적 기존 PRO 있으면 기존 확장 우선") 에 부합.

---

> 본 As-Is 파일은 차원 4 사이클의 산출물이며 차원 1 빌드의 입력입니다.
> 직접 수정 금지 — 추가 피드백은 새 act 사이클 (`/act start <queue_id>`).
> 본 파일이 지운 후 재작성되면 차원 1 빌드는 새 입력으로 인식 (단, queue_id 는 1회만 처리되도록 act-coordinator 가 충돌 검사).
