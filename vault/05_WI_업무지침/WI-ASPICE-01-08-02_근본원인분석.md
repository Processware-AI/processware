---
type: WI
doc_id: "WI-ASPICE-01-08-02"
title: "근본 원인 분석 (SUP.9.BP3)"
version: "0.1"
owner: "Process Owner"
reviewer: "QA / 발견자 / 관련 도메인 엔지니어"
approver: "Change Control Board Chair"
scope: "Problem Ticket → 5-Why·Fishbone 적용 → 공통 원인 식별 → 해결책 도출 → RCA Report"
parent_pro: "[[PRO-ASPICE-01-08_문제및변경관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-08-02-01_근본원인분석보고서]]"]
related_rec: []
standards: ["Automotive SPICE 4.0"]
aspice_processes: ["SUP.9"]
entry_gate: "WI-ASPICE-01-08-01.status == done"
scope_type: "common"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SUP.9, RCA, 5-Why, Fishbone]
---

# 근본 원인 분석 업무지침 (WI-ASPICE-01-08-02)

> 상위 절차: [[PRO-ASPICE-01-08_문제및변경관리프로세스]] §5 단계 2
> ASPICE 매핑: SUP.9.BP3 (Determine causes and impact of problems)

## 1. 업무 목적

등록·분류된 Problem Ticket 의 **표면 증상이 아닌 근본 원인(Root Cause)** 을 체계적으로 식별하여, 동일 결함의 재발을 예방하는 영구 해결책을 도출한다. 5-Why 와 Fishbone (Ishikawa) 두 기법을 결합 적용한다.

## 2. 수행 주체
- **주 수행자**: Process Owner (해당 결함이 속한 프로세스 책임자)
- **검토자**: QA, 발견자, 관련 도메인 엔지니어 (SW/HW/ML/Test)
- **승인자**: CCB Chair (Major 등급 이상)

## 3. 범위
WI-08-01 에서 등록·분류된 모든 **Major / Critical** 등급 Problem Ticket 에 의무 적용. Minor 등급은 약식 RCA(5-Why 만) 적용 가능. **VWAY Motors** 의 양산·선행 프로젝트 공통 적용.

## 4. 입력 자료 / 산출물
- **Input**: Problem Ticket (WI-08-01 산출물), 결함 재현 절차, 관련 산출물(요구사항·설계·코드·테스트 결과)
- **Output**: RCA Report (TMP-ASPICE-01-08-02-01), 해결책 후보 목록, 재발 방지 조치안

## 5. 수행 절차

### 5.1 사전 준비
1. Problem Ticket 의 분류·증상·재현 절차 재확인.
2. RCA 워크숍 참석자 확정 (Process Owner + 발견자 + 도메인 엔지니어 + QA).
3. 관련 산출물(요구사항 ID·설계 문서·코드 commit·테스트 로그) 사전 수집.
4. 화이트보드/Miro 등 Fishbone 작성 도구 준비.

### 5.2 수행 단계

1. **사실 확인 (Fact-finding)**
   - 결함의 5W1H 정리: 누가·언제·어디서·무엇을·왜·어떻게 발견했는가.
   - 재현 가능성 확인 (재현율 100% / 간헐적 / 1회성).

2. **5-Why 분석 적용**
   - 표면 증상 → "왜?" 5회 반복 → 시스템·프로세스 차원 원인 도달.
   - 각 Why 단계마다 증거(로그·코드·문서) 첨부.

3. **Fishbone 다이어그램 작성**
   - 6M 카테고리: Man(인적), Machine(도구), Material(부품), Method(절차), Measurement(측정), Environment(환경).
   - 각 카테고리별 잠재 원인 brainstorm.

4. **공통 원인 식별 (Common Cause Identification)**
   - 5-Why 결과와 Fishbone 결과의 교집합 도출.
   - 최종 Root Cause 1~3 개 확정.

5. **해결책 후보 도출**
   - Root Cause 별 해결책 제안 (단기 Quick Fix / 장기 영구 조치).
   - 영구 조치는 SUP.10 변경 절차 연계 필요성 판단.

6. **RCA Report 작성 및 검토**
   - TMP-ASPICE-01-08-02-01 양식 사용.
   - QA 독립 검토 → CCB Chair 승인.

### 5.3 완료 조건 체크리스트
- [ ] Problem Ticket ID 와 RCA Report 1:1 매칭
- [ ] 5-Why 5단계 모두 작성 완료
- [ ] Fishbone 6M 카테고리 모두 검토 (해당 없음 표기 가능)
- [ ] Root Cause ≥ 1 건, ≤ 3 건 확정
- [ ] 각 Root Cause 에 대해 단기·장기 해결책 모두 제시
- [ ] QA 독립 검토 sign-off
- [ ] CCB Chair 승인 (Major 이상)
- [ ] 해결책이 SUP.10 변경 필요 시 CR 등록 ID 기재
- [ ] [[MAT-001_문서관리대장]] 등록

## 6. 인터페이스 부서
- **발견자**: 사실 정보 제공
- **QA (SUP.1)**: RCA 절차 적합성 독립 검토
- **CCB**: 영구 조치가 산출물 변경 동반 시 CR 심의
- **SW/HW/ML/Test 도메인**: 기술적 원인 분석 참여
- **PMO ([[PRO-ASPICE-01-09]])**: 일정·자원 영향 협의

## 7. 주의사항 / 예외 처리

### 7.1 5-Why 가 3단계에서 막히는 경우
- 사실 정보 부족 → 추가 조사 (로그 분석·재현 시험·인터뷰) 후 재개.
- 도메인 전문가 부재 → 외부 전문가 자문 요청.
- 무리한 5단계 도달 시도 시 가설로 흐름 → "추가 조사 필요" 표기 후 보류.

### 7.2 Root Cause 가 조직 차원 (절차·문화)인 경우
- 단일 프로젝트 해결 불가 → PIM.3 (PRO-11) 프로세스 개선 기회로 격상.
- 교훈(Lessons Learned) DB 등록 의무.

### 7.3 안전성·규제 영향 결함의 RCA
- ASIL B 이상 안전성 영향 결함 → Safety Manager 공동 검토 필수.
- ISO 26262 §7.4 (FMEDA·DFA) 연계 검토.
- 규제 신고 의무 결함 (UNECE R155/R156) → Cybersecurity Officer 통보.

### 7.4 RCA 결과 Root Cause 다수 (4건 이상)
- 분석 범위가 너무 넓음 → Problem Ticket 을 분할 등록 권고.
- 또는 우선순위 1~3 위만 RCA 처리, 나머지는 후속 RCA 별도 진행.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-08-02-01_근본원인분석보고서]]
- 작성예시: [[EX-ASPICE-01-08-02-01_근본원인분석보고서_작성예시]]
- 기록 폴더: `vault/08_REC_기록/SUP9/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SUP.9-BP3"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SUP.9.BP3 RCA 절차 정의 | (대기) |
