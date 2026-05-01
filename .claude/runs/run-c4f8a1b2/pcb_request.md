---
type: pcb-approval-request
trace_id: run-c4f8a1b2
status: approved
queue_id: queue-qa1b2c3d4
priority: critical
created_at: "2026-05-02T14:15:00+09:00"
sla_due_date: "2026-05-30"
approver_role: PCB
approver_name: "(auto-approved Phase1 PoC)"
decision: approved
responded_at: "2026-05-02T14:15:01+09:00"
rejection_reason: null
note: "PoC 한정 auto_approve — 운영 시 PCB 위원회 정식 검토 후 응답"
---

# PCB 승인 요청 — run-c4f8a1b2

PCB (Process Control Board) 위원회께,

차원 3 (Check) 의 부적합 발견에 따른 표준 자산 개정 제안을 검토 요청드립니다.

## 1. 배경
- 모(母) 큐: [[queue-qa1b2c3d4]] (priority: critical / status: in_progress)
- 모(母) 심사: [[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]] (1회차 2026 — 이감사)
- 관련 NCR: [[REC-NCR-04-01-2026-001_REQ-005_critical_종결추적]] (open / SLA 2026-05-30)
- 관련 KPI 회귀: KPI-CMMI-04-01-02 (부적합 종결율 0%) / META-NCR-CLOSURE (0%) — 본 큐에 통합

## 2. 근본 원인 (RCA 요약)

PRO-CMMI-04-01 §5-6 의 "종결 추적" 절차에 종결 기한 SLA 가 정의되지 않아, 부적합 발견 시 "추적" 의 종결 시점이 운영 자율에 맡겨지고 있음. 그 결과 REC-04-01-03-001 / REC-04-01-04-002 두 trace 모두 재점검·재실행이 지연되어 KPI '부적합 종결율 ≥ 95%' 와 '평균 종결 기간 ≤ 20영업일' 이 동시 미달. 5-Why depth 5 — high confidence.

**Primary**: method — PRO §5-6 SLA 미정의 (종결 시점·책임자 일정 관리 책임 분리 부재)
**Secondary** (통합 후보): measurement — KPI 측정 기준 시점과 절차 시점의 분리 (queue-qe5f6a7b8 / queue-q9d8c7b6a 와 root cause 통합 가능)
**Confidence**: high

## 3. 개정 계획 요약

| 항목 | 값 |
|---|---|
| Primary 자산 | PRO-CMMI-04-01 v1.0 → v1.1 (예정) |
| 영향 섹션 | §5-6 종결 추적 (등급별 SLA 추가) / §7 KPI (정합 갱신) |
| Affected 자산 | WI-04-01-03 (정합 검토), WI-04-01-04 (queue-qf1e2d3c4 와 통합 후보) |
| Not affected | WI-04-01-01, WI-04-01-05, POL-CMMI-04 |
| Rebuild mode | `--from write --target PRO-CMMI-04-01` (process-designer 미재실행) |
| Impact | medium |
| 추정 노력 | 8 시간 |
| Due date | 2026-05-30 (SLA critical) |

## 4. 권장 단계 (PCB 승인 후 실행)

1. backup (`git tag pre-revision/PRO-CMMI-04-01-v1.0`) — admin/process_owner
2. rebuild (`/build-standard CMMI-DEV-ML3 --from write --target PRO-CMMI-04-01`) — admin
3. validate (qa-reviewer 자동 — build-standard 내부) — 자동
4. register (MAT-001 §개정 이력 — act-coordinator 가 본 시점 사전 작성) — 자동
5. close_ncr (`/audit --close-ncr REC-NCR-04-01-2026-001 --capa <후속 REC>`) — process_owner
6. re_kpi (`/audit --kpi start CMMI-DEV-ML3 --period 2026-04-01..2026-06-30`) — qmr

## 5. 위험 요인

- **정합성 위험** — PRO §5-6 개정이 자식 WI DoD 와 충돌 가능 (qa-reviewer §11-A 검증 필수). Mitigation: --from write 모드로 한정.
- **기존 운영 영향** — MAT-005 §실행기록 trace 3건 v1.0 기준 (As-Is 파일에 기존 trace 인용). Mitigation: trace 의 "적용 표준 버전" 컬럼 신설 검토.
- **다중 큐 통합 미수행** — queue-qe5f6a7b8 / q9d8c7b6a / qf1e2d3c4 와 root cause 일부 겹침. Mitigation: Phase 2 다중 큐 일괄 처리 후속 사이클 분리.

## 6. 응답

- 승인: `/act --approve run-c4f8a1b2 [--approver "박상무 (PCB위원장)"]`
- 반려: `/act --reject  run-c4f8a1b2 --reason "..."`

## 7. PCB 응답 (PoC 자동 승인)

본 PoC 는 `--auto-approve` 플래그로 PCB 즉시 승인 처리되었습니다 (Phase 1 한정).

운영 시에는:
- PCB 위원 3명 quorum (Phase 2.5 다단계 승인 도입 예정)
- 정기 PCB 회의 (월 1회 또는 critical 발생 시 7일 이내) 에서 검토
- 외부 채널 알림 (Phase 4.5 — 이메일/Slack)

## 8. 참조 자료

- [[root_cause.yaml]] — 5-Why depth 5 (single method)
- [[revision_plan.yaml]] — 6단계 권장 단계 + 의존성 + 위험 요인
- [[queue-qa1b2c3d4]] — 큐 본문
- [[REC-NCR-04-01-2026-001_REQ-005_critical_종결추적]] — NCR §4 시정조치 권고
- [[REC-AUDIT-04-01-01-2026-001_프로세스_품질보증_심사보고서]] §6 — 차원 4 권고 1번
