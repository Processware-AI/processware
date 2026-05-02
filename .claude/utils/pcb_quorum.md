---
type: util-spec
title: PCB 다단계 quorum 명세 (Phase 4.5)
version: "0.1"
owner: "QMR"
status: spec
created: 2026-05-16
related_agents: [pcb-gatekeeper]
---

# PCB 다단계 quorum 명세 (Phase 4.5)

> Phase 1~2 의 단일 PCB 승인 (또는 --auto-approve PoC) 을 정식 다단계 quorum 으로 대체.
> 차원 2 의 hitl-gatekeeper Phase 2.5 (다단계 stages chain) 와 동형 — escalation-coordinator 와 통합.

## 1. quorum 정의

| quorum 모드 | 조건 | 적용 시점 |
|---|---|---|
| simple_majority | 위원 N명 중 ⌈N/2⌉ 이상 승인 | 기본값 (default) |
| supermajority | 위원 N명 중 ⌈2N/3⌉ 이상 승인 | critical impact 또는 POL 변경 |
| unanimous | 위원 N명 전원 승인 | 표준 자체 변경 또는 v1.0 → v2.0 (major version bump) |
| chair_veto | 위원장 1명의 거부권 (chair_veto: true) | 부적합 인정 거부 (반대 의견의 안전판) |

## 2. PCB 위원회 구성 (예시)

```yaml
pcb_committee:
  members:
    - name: "박상무 (Sponsor)"
      role: chairperson                # 위원장 (chair_veto 권한)
      idp_user: "park.sangmu@example.com"
    - name: "QMR 김부장"
      role: voting_member
      idp_user: "kim.bujang@example.com"
    - name: "Process Owner 이팀장"
      role: voting_member
      idp_user: "lee.timjang@example.com"
    - name: "외부 컨설턴트 박박사"
      role: voting_member               # 외부 자문 — 정족수 포함
      idp_user: "park.consultant@external.com"
  default_quorum: simple_majority
  override_rules:
    - condition: "revision_plan.estimated_impact == high"
      quorum: supermajority
    - condition: "revision_plan.affects[0].kind == POL"
      quorum: unanimous
    - condition: "revision_plan.scope.expected_next_version starts_with v2"
      quorum: unanimous
```

## 3. pcb-gatekeeper Phase 2.5 동작 (다단계)

```yaml
# Phase 2.5 신규 입력 필드
mode: gate_enter
trace_id: run-cxxxxxxxx
queue_id: queue-qa1b2c3d4
pcb_committee_path: .claude/rbac/pcb_committee.yaml
options:
  quorum_mode: auto                     # auto: revision_plan 으로 결정 / 강제: simple_majority|supermajority|unanimous
  timeout_days: 7                       # quorum 응답 SLA — 외부 알림과 연동
  escalate_after_timeout: true          # 타임아웃 시 escalation-coordinator 트리거
```

## 4. 응답 처리 (gate_response Phase 2.5)

```yaml
# 위원별 응답 — 각 위원의 /act-process --approve / --reject 호출이 누적
pcb_responses:
  - member: "박상무 (Sponsor)"
    decision: approved
    responded_at: "2026-05-16T15:18:00+09:00"
    note: "본 개정 시급 — Sponsor 승인"
  - member: "QMR 김부장"
    decision: approved
    responded_at: "2026-05-17T09:30:00+09:00"
  - member: "Process Owner 이팀장"
    decision: rejected
    responded_at: "2026-05-17T11:00:00+09:00"
    note: "WI-04-01-06 신규 생성보다 기존 WI-04-01-05 (QA 기록 관리) 확장 검토 권고"
  - member: "외부 컨설턴트 박박사"
    decision: pending                    # 미응답 — 타임아웃 후 escalation
quorum_evaluation:
  mode: simple_majority                   # 4명 중 ⌈4/2⌉ = 2명 이상
  approvals: 2                             # 박상무 + 김부장
  rejections: 1                            # 이팀장
  pending: 1                               # 외부 컨설턴트
  result: approved                         # 2 ≥ 2 → 통과 (단 chair_veto 미사용)
  chair_decision: approved                 # 위원장 동의 → veto 없음
final_decision: approved
final_decided_at: "2026-05-17T11:00:00+09:00"
```

## 5. 타임아웃·에스컬레이션 (escalation-coordinator 통합)

- 본 명세는 차원 2 의 escalation-coordinator (Phase 2.5) 를 PCB 에도 적용.
- `timeout_days` (default 7) 경과 시:
   1. 외부 알림 (이메일/Slack — extensions.external_notifications 참조).
   2. 미응답 위원에 1차 에스컬레이션.
   3. 다시 3일 경과 시 chairperson 의 단독 결정 권한 이양 (또는 quorum 미충족 시 자동 abort).

## 6. RBAC 통합

- `policy.yaml` extensions.delegation 활성화 시 — PCB 위원 부재 시 대리 위원 위임 (한시).
- `policy.yaml` extensions.audit_log 활성화 시 — 모든 PCB 응답 / quorum 평가 / 위원장 veto 등이 audit_log 에 기록.

## 7. PoC 적용 시점

- Phase 1~2 의 `--auto-approve` 는 본 명세 도입 시 deprecated.
- Phase 4.5 도입 첫 단계: `pcb_committee.yaml` 작성 + pcb-gatekeeper 가 모드 인식.
- Phase 4.5 두 번째 단계: 외부 알림 (extensions.external_notifications) 으로 위원회 자동 호출.
- Phase 4.5 세 번째 단계: timeout / escalation 동작 검증.
