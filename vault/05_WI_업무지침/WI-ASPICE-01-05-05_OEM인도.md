---
doc_id: "WI-ASPICE-01-05-05"
title: "OEM 인도 (SPL.2)"
type: WI
version: "0.1"
status: draft
owner: "Project Manager"
reviewer: "QA / Legal / CM"
approver: "Program Director"
scope: "릴리즈 패키지 완성 후 → OEM 전달 → 인도 확인서 수령 → 인도 완료 기록"
scope_type: project
scope_code: ASPICE
domain: ASPICE
parent_pro: "[[PRO-ASPICE-01-05_검증및인도프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-05-05-01_OEM인도확인서]]"]
aspice_processes: ["SPL.2"]
entry_gate: "WI-ASPICE-01-05-04.status == done"
standards: ["Automotive SPICE 4.0"]
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SPL.2, OEM, Delivery]
---

# WI-ASPICE-01-05-05 — OEM 인도 (SPL.2)

## 1. 업무 목적
릴리즈 패키지(WI-ASPICE-01-05-04 산출)를 OEM 에 안전하게 전달하고 수령 확인서를 수령·보존하여 계약상 인도 의무 이행을 입증한다. ASPICE 4.0 SPL.2 활동을 완결한다.

## 2. 수행 주체
- **주 수행자**: Project Manager
- **검토자**: QA / Legal / CM
- **승인자**: Program Director

## 3. 범위
- 대상: 릴리즈 패키지 전체(바이너리·문서·체크섬·서명)
- 활동: 안전한 전달, 수령 확인 수령, 인도 후 지원 약정 확정
- 제외: 인도 후 변경 관리는 SUP.10 적용

## 4. 입력 자료 / 산출물
**입력 자료**
- 릴리즈 패키지 (CM tag: REL-...)
- 릴리즈 패키지 명세서 (TMP-ASPICE-01-05-04-01)
- OEM 수령 담당자 연락처
- 계약서상 인도 조건 / 채널 / 인도 일정
- 수출통제 검토 결과

**산출물**
- OEM 인도 확인서(TMP-ASPICE-01-05-05-01)
- 전달 채널 로그 (SFTP/Portal 전송 기록)
- 수령 확인 회신 (서명/이메일)
- 인도 완료 선언서

## 5. 수행 절차

### 5.1 사전 준비
1. 릴리즈 패키지 무결성 재검증(체크섬·서명).
2. OEM 수령 담당자·채널·일정 최종 확인.
3. 수출통제 분류 재확인(EAR/ITAR/EAR99).
4. 인도 후 지원 SLA(기간·연락 채널) 합의 사항 점검.

### 5.2 수행 단계
1. **전달 채널 가동** (SPL.2 BP6) — 합의된 채널(암호화 SFTP, OEM Portal)로 패키지를 업로드한다.
2. **전달 완료 통지** — OEM 담당자에게 전달 완료 통지문을 발송하고 수령 확인을 요청한다.
3. **수령 확인 수령** — OEM 으로부터 수령 확인 (서명 또는 회신 이메일)을 받아 보관한다.
4. **인도 후 지원 약정 확정** — SLA·연락 채널·이슈 채널을 OEM 과 합의 문서화한다.
5. **인도 완료 선언** — 사내 PM·Program Director 결재로 인도 완료를 선언한다.
6. **레슨드런 캡처** — 인도 과정의 이슈·교훈을 SUP.7 lessons learned 로 기록한다.
7. **CM 인도 기록 갱신** — CM 시스템에 인도 일자·수령자·tag 를 기록한다.

### 5.3 완료 조건 체크리스트
- [ ] 패키지 무결성(체크섬·서명) 이 재검증되었다.
- [ ] 수출통제 분류가 확인되고 위반이 없다.
- [ ] 합의 채널로 전달이 완료되었다.
- [ ] OEM 수령 확인이 수령·보존되었다.
- [ ] 인도 후 지원 SLA 가 문서화되었다.
- [ ] 인도 완료 선언이 결재 완료되었다.
- [ ] CM 인도 기록이 갱신되었다.
- [ ] [[MAT-001_문서관리대장]] 갱신 완료.

## 6. 인터페이스 부서
- 법무팀: 수출통제·계약 의무 준수 검토
- 보안팀: 전송 채널 암호화·접근 통제
- QA: 인도 활동 무결성 감사
- CM: 인도 기록·아카이브 보존
- 고객 지원팀: 인도 후 SLA 운영 인수인계

## 7. 주의사항 / 예외 처리

### 7.1 전송 실패 또는 채널 장애
SFTP/Portal 장애 시 대체 채널(암호화 USB 직배송 등)을 법무·보안 검토 후 가동한다. 평문 이메일 첨부는 금지.

### 7.2 OEM 수령 거부
OEM 이 패키지 결함 또는 문서 미비를 사유로 수령을 거부하면 즉시 시정 후 재인도한다. 거부 사유와 시정 내역을 인도 확인서에 부기한다.

### 7.3 수출통제 위반 사후 검출
인도 후 EAR/ITAR 위반이 의심되면 즉시 OEM 에 통보 후 사용 중단 요청, 법무·CISO 보고 및 당국 신고 절차를 따른다.

### 7.4 SLA 합의 미타결
인도 후 지원 SLA 가 합의되지 않은 채 인도가 진행되면 잠정 SLA(30일)를 적용하고 30일 이내 정식 합의를 강제한다.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-05-05-01_OEM인도확인서]]
- 작성예시: [[EX-ASPICE-01-05-05-01_OEM인도확인서_작성예시]]
- 상위 절차: [[PRO-ASPICE-01-05_검증및인도프로세스]]
- 추적성: [[MAT-007_요구사항추적매트릭스]]

## 9. 출처
```yaml
source_citation:
  - file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    section: "SPL.2 / ASPICE 4.0"
    accessed: "2026-05-06"
standards:
  - "Automotive SPICE 4.0 — SPL.2 Product Release"
```

## 10. 개정 이력
| 버전 | 일자 | 변경 내용 | 승인자 |
|------|------|-----------|--------|
| 0.1 | 2026-05-06 | 최초 작성 (Draft) | Program Director |
