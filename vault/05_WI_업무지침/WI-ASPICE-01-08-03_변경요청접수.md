---
type: WI
doc_id: "WI-ASPICE-01-08-03"
title: "변경 요청 접수 및 등록 (SUP.10.BP1)"
version: "0.1"
owner: "Process Owner"
reviewer: "QA / 요청자"
approver: "Change Control Board Chair"
scope: "변경 요청 채널 정의 → CR 등록 → 분류·우선순위 예비 판정 → CR 관리대장 등록"
parent_pro: "[[PRO-ASPICE-01-08_문제및변경관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-08-03-01_변경요청서]]"]
related_rec: []
standards: ["Automotive SPICE 4.0"]
aspice_processes: ["SUP.10"]
entry_gate: null
scope_type: "common"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SUP.10, ChangeRequest]
---

# 변경 요청 접수 및 등록 업무지침 (WI-ASPICE-01-08-03)

> 상위 절차: [[PRO-ASPICE-01-08_문제및변경관리프로세스]] §5 단계 4
> ASPICE 매핑: SUP.10.BP1 (Identify changes)

## 1. 업무 목적

산출물(요구사항·설계·코드·HW·ML 모델·문서) 의 변경 필요성을 식별·접수하여 **고유 ID 가 부여된 Change Request(CR)** 로 등록한다. 통제되지 않은 임의 변경을 방지하고 모든 변경의 가시성을 확보한다.

## 2. 수행 주체
- **주 수행자**: Process Owner (해당 산출물의 도메인 책임자)
- **검토자**: 요청자, QA
- **승인자**: CCB Chair (CR 등록 단계는 접수만 — 본 승인은 WI-08-05)

## 3. 범위
**VWAY Motors** 의 모든 베이스라인된 산출물의 변경 요청에 적용. 단, 미베이스라인 작업 산출물의 일상적 수정은 본 절차 대상이 아니다(개발 중 자유 수정 영역).

## 4. 입력 자료 / 산출물
- **Input**: 변경 필요성 (RCA 결과·고객 요구·결함 수정·기능 개선·법규 대응 등)
- **Output**: Change Request Record (TMP-ASPICE-01-08-03-01), CR 관리대장 등록 row

## 5. 수행 절차

### 5.1 사전 준비
1. CR 접수 채널 확인 (Jira CR Issue Type / 사내 Polarion ALM / 이메일).
2. 영향 받을 베이스라인 산출물 ID 확인 (CM 시스템 조회).
3. 요청자의 RFQ §·결함 ID·RCA Report ID 등 출처 자료 수집.

### 5.2 수행 단계

1. **CR 접수**
   - 채널: 정식 CR Tool (Jira/Polarion) 우선, 긴급 시 이메일+사후 등록.
   - 접수 시 자동 timestamp 및 요청자 ID 기록.

2. **CR 고유 ID 부여**
   - 형식: `CR-{YYYY}-{NNNN}` (연도 4자리 + 일련번호 4자리).
   - CR 관리대장 (Jira/Polarion 자동) 에서 충돌 방지.

3. **변경 유형 분류**
   - 결함 수정 (Defect Fix) / 기능 개선 (Enhancement) / 법규 대응 (Regulatory) / 기타.
   - 부수 분류: SW / HW / ML / 문서 / 인프라.

4. **우선순위 예비 판정**
   - Critical (안전·법규·양산 차단) / High / Medium / Low.
   - 기준 표 (WI 본문 §7.1 참조) 적용.

5. **변경 사항 기술**
   - 현재 상태 (As-Is) → 변경 후 상태 (To-Be) 명확 기재.
   - 변경 사유, 영향 받을 베이스라인 ID 목록 첨부.

6. **CR 관리대장 등록**
   - CR Tool 자동 등록 + 수동 검증 (필드 누락 점검).
   - 영향 평가 단계(WI-08-04) 로 자동 워크플로 전환.

### 5.3 완료 조건 체크리스트
- [ ] CR 고유 ID `CR-YYYY-NNNN` 형식 부여
- [ ] 변경 유형 4개 중 1개 분류 완료
- [ ] As-Is / To-Be 명확 기술
- [ ] 영향 받을 베이스라인 ID ≥ 1건 첨부
- [ ] 우선순위 예비 판정 완료
- [ ] 요청자 ID·접수일 timestamp 기록
- [ ] CR 관리대장 등록 후 영향평가(WI-08-04) 자동 워크플로 전환
- [ ] [[MAT-001_문서관리대장]] CR 항목 갱신

## 6. 인터페이스 부서
- **요청자 (전 부서)**: 변경 사유·증적 제공
- **CM Team (SUP.8)**: 영향 받을 베이스라인 ID 식별 지원
- **PMO ([[PRO-ASPICE-01-09]])**: 일정·자원 영향 사전 협의
- **Safety Engineer**: ASIL 영향 사전 검토

## 7. 주의사항 / 예외 처리

### 7.1 우선순위 판정 기준 표
| 등급 | 기준 |
|---|---|
| Critical | 안전성 영향 / 양산 라인 정지 / 규제 위반 / 보안 취약 |
| High | 핵심 기능 미동작 / OEM PPAP 영향 / 일정 critical path |
| Medium | 보조 기능 / 사용성 / 일정 여유 있음 |
| Low | 문서 오탈자 / 코드 정리 / 비기능 minor |

### 7.2 긴급 변경 (Hot Fix) 접수
- 양산·고객사 운영 중 Critical 결함:
  - 우선 이메일+전화 접수 → 4 시간 내 정식 CR 등록.
  - WI-08-05 CCB 운영의 긴급 의사결정 절차 적용.

### 7.3 중복·유사 CR
- 신규 CR 등록 전 기존 CR 검색 (CR Tool 검색 기능).
- 중복 발견 시 신규 CR 을 기존 CR 의 sub-issue 로 연결, 별도 등록 금지.

### 7.4 OEM 요청 변경 (External CR)
- ABC Motors 등 OEM 발 변경 요청:
  - OEM 공문 또는 합의 회신 ID 첨부 의무.
  - 우선순위 ≥ High 자동 부여.
  - 계약·일정·비용 영향 PMO 협의 의무.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-08-03-01_변경요청서]]
- 작성예시: [[EX-ASPICE-01-08-03-01_변경요청서_작성예시]]
- 기록 폴더: `vault/08_REC_기록/SUP10/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SUP.10-BP1"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SUP.10.BP1 변경 요청 접수 절차 정의 | (대기) |
