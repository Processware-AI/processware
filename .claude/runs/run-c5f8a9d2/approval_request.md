---
type: approval_request
trace_id: run-c5f8a9d2
wi_id: WI-CMMI-04-01-04
step_id: step-08
approver_role: Sponsor
requested_at: 2026-05-01T16:18:00+09:00
status: approved
approver_name: "박상무 (Sponsor)"
responded_at: 2026-05-01T16:23:00+09:00
input_source: "/do --approve"
---

# 승인 요청 — 품질이슈 에스컬레이션 및 종결

> 본 파일은 외부 알림 채널(이메일/Slack/Jira) 의 drop-out 모킹입니다.
> 실제 운영 시 이 파일은 외부 시스템으로 라우팅됩니다.

## 요약
- WI: [[WI-CMMI-04-01-04_품질이슈_에스컬레이션_및_종결_v1.0]]
- 결정 사항: NCR-2026-042 (Critical, 21일 경과) — Sponsor 결재로 인력·외주 자원 추가, 종결 합의
- 다음 액션: REC 확정 저장 + MAT-005 갱신
- 추적: run-c5f8a9d2

## 응답 방법
다음 중 하나로 응답:

**승인**:
```
/do --approve run-c5f8a9d2
```

**반려**:
```
/do --reject run-c5f8a9d2 --reason "<사유>"
```

또는 본 파일의 frontmatter `status` 를 `approved` / `rejected` 로 변경하고
`approver_name`, `responded_at`, `reason` 필드를 채워 저장 → `/do --check-approvals`.

## 미리보기

| ID | 등급 | 1차 책임 | 에스컬레이션 |
|---|---|---|---|
| NCR-2026-042 | Critical | Tech Lead | QA Lead → PM (16:05) → Sponsor (16:10) |

**결정 회의 요약**: 참석 PM·Sponsor·QA Lead. 인력 1명 + 외주 검토자 1명 추가, 재점검 1주 후.
**자원 추가**: 내부 1명 (Backend), 외주 검토자 1명 (5월 한정)
**재추적 일자**: 2026-05-08
