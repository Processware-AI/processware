---
type: WI
doc_id: WI-CMMI-02-05-01
title: "프로젝트 정의 프로세스 수립 + OPA 활용 (SG1: SP1.1~1.3)"
version: "0.1"
status: draft
owner: "Project Manager"
reviewer: "EPG Lead"
approver: "PMO Director"
scope: "OSSP 테일러링 → 프로젝트 정의 프로세스 수립 + OPA 활용 + 작업환경 수립"
scope_code: CMMI
parent_pro: "[[PRO-CMMI-02-05_통합_프로젝트_관리_절차]]"
parent_pol: "[[POL-CMMI-02_프로젝트_관리_정책]]"
related_tmp:
  - "[[TMP-CMMI-02-05-01-01_프로젝트_정의_프로세스_기술서]]"
  - "[[TMP-CMMI-02-05-01-02_OPA_활용_계획서]]"
  - "[[TMP-CMMI-02-05-01-03_프로젝트_작업환경_정의서]]"
related_rec: []
standards: [CMMI-DEV-ML3-V1.3]
standards_meta:
  publisher: "Software Engineering Institute (CMU/SEI)"
  year: 2010
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_acronym: IPM
sg_sp_refs:
  - "CMMIDEV-IPM-SP1.1-REQ-001"
  - "CMMIDEV-IPM-SP1.2-REQ-001"
  - "CMMIDEV-IPM-SP1.3-REQ-001"
entry_gate: null
scope_type: project
created: 2026-05-11
updated: 2026-05-11
tags: [WI, CMMI, IPM, ML3]
---

# 프로젝트 정의 프로세스 수립 + OPA 활용 (WI-CMMI-02-05-01)

> 상위 절차: [[PRO-CMMI-02-05_통합_프로젝트_관리_절차]]

## 1. 업무 목적
OSSP 를 테일러링하여 프로젝트의 정의된 프로세스(Project's Defined Process)를 수립하고, OPA(Organizational Process Assets)를 활용 계획에 통합하며, 프로젝트 작업환경을 수립한다. GG3 제도화의 프로젝트 측 구현 핵심.

## 2. 수행 주체
- **주 수행자**: Project Manager (EPG 자문)
- **검토자**: EPG Lead, Senior Management
- **승인자**: PMO Director

## 3. 범위
PRO-CMMI-02-05 §5 의 **SG1 SP1.1~1.3**.

## 4. 입력 자료 / 산출물
- **Input**
  - OSSP ([[WI-CMMI-01-01-01]] 산출)
  - 테일러링 가이드 ([[WI-CMMI-01-01-02]] 산출)
  - PAL/측정저장소 ([[WI-CMMI-01-01-03]])
  - 조직 표준 작업환경 (OPD SP1.6)
- **Output**
  - [[TMP-CMMI-02-05-01-01_프로젝트_정의_프로세스_기술서]]
  - [[TMP-CMMI-02-05-01-02_OPA_활용_계획서]]
  - [[TMP-CMMI-02-05-01-03_프로젝트_작업환경_정의서]]

## 5. 수행 절차

### 5.1 사전 준비
1. OSSP·테일러링 가이드 입수.
2. PAL 접근 권한 확보.
3. EPG 자문 일정 confirm.

### 5.2 수행 단계
1. **정의 프로세스 수립 (SP1.1)**
   - OSSP 의 컴포넌트 프로세스 (18 PA) 중 본 프로젝트 적용 대상 선택
   - 테일러링 가이드의 규칙 (필수/선택/제외) 적용
   - 테일러링 사유 기록 (단순화·강화·조합 등)
2. **OPA 활용 계획 (SP1.2)**
   - PAL 조회로 활용할 자산 (측정값·교훈·재사용 컴포넌트) 식별
   - 본 프로젝트에서 기여할 자산 후보 정의 (종료 시 OPA 기여)
3. **작업환경 수립 (SP1.3)**
   - 조직 표준 작업환경 (Tool stack, 환경) 기반 프로젝트 환경 설계
   - 환경 차이 명시 (도구 추가·제외 등)
4. **검토 + 승인**
   - EPG 자문 → PMO Director 결재

### 5.3 완료 조건
- [ ] 정의 프로세스 기술서 작성 (테일러링 결정 + 근거)
- [ ] OPA 활용 계획서 (활용 자산 + 기여 후보)
- [ ] 작업환경 정의서 (도구·환경 list)
- [ ] EPG 자문 의견 반영
- [ ] PMO Director 결재
- [ ] CM 등록

## 6. 인터페이스 부서
- **EPG**: OSSP·테일러링 자문, OPA 운영 ([[PRO-CMMI-01-01]])
- **PAL 운영자**: 자산 조회 지원 ([[WI-CMMI-01-01-03]])
- **CM**: 정의 프로세스 베이스라인 등록
- **MA**: 측정 항목 매핑

## 7. 주의사항 / 예외 처리

### 7.1 OSSP 미적용 영역 (커스텀 프로세스 필요)
- OSSP 카탈로그 외 프로세스 필요 시 EPG 임시 승인 → 6개월 내 OSSP 등재 의무.

### 7.2 테일러링 가이드 충돌
- 가이드 규칙간 충돌 발견 시 EPG 결정 요청 (Conditional 적용 가능).

### 7.3 PAL 자산 부재
- 신규 도메인으로 PAL 자산 0건인 경우: 외부 벤치마크 활용 + 본 프로젝트 종료 후 PAL 기여 약속.

## 8. 연계 템플릿 / 기록
- 템플릿:
  - [[TMP-CMMI-02-05-01-01_프로젝트_정의_프로세스_기술서]]
  - [[TMP-CMMI-02-05-01-02_OPA_활용_계획서]]
  - [[TMP-CMMI-02-05-01-03_프로젝트_작업환경_정의서]]
- 작성예시:
  - [[EX-CMMI-02-05-01-01_프로젝트_정의_프로세스_기술서_작성예시]]
  - [[EX-CMMI-02-05-01-02_OPA_활용_계획서_작성예시]]
  - [[EX-CMMI-02-05-01-03_프로젝트_작업환경_정의서_작성예시]]

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-IPM-SP1.1~1.3-REQ-001 (p.159-162)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (wi-tmp-writer) | - |
