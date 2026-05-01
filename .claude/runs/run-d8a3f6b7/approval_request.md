---
type: approval_request
trace_id: run-d8a3f6b7
wi_id: WI-CMMI-04-01-04
step_id: step-08
approver_role: Sponsor
requested_at: 2026-05-01T16:48:00+09:00
status: rejected
approver_name: "박상무 (Sponsor)"
responded_at: 2026-05-01T16:53:00+09:00
reason: "임계 기준(SLA) 미정의 + Sponsor 회의 미참석 — WI §7.1 결정 지연 분기 적용. SLA 정식 정의 후 재실행 필요."
input_source: "/do --reject"
---

# 승인 요청 — 품질이슈 에스컬레이션 및 종결 (반려됨)

> 본 파일은 외부 알림 채널의 drop-out 모킹입니다.

## 요약
- WI: [[WI-CMMI-04-01-04_품질이슈_에스컬레이션_및_종결_v1.0]]
- 결정 사항: NCR-2026-077 (Major, 12일) — 임계 기준 미정의 상태에서 종결 시도
- 추적: run-d8a3f6b7

## 응답 결과
**❌ 반려** — Sponsor 박상무
사유: 임계 기준(SLA) 미정의 + Sponsor 회의 미참석. WI §7.1 결정 지연 분기 적용. SLA 정식 정의 후 재실행 필요.
응답 시각: 2026-05-01T16:53:00+09:00
응답 채널: `/do --reject`

## 후속 조치
1. SLA 정식 정의 (§5.1.1) — 임계 기간 표준화
2. Sponsor 결정 회의 정식 개최
3. 시정조치 후 신규 REC 발행: `/do WI-CMMI-04-01-04`
