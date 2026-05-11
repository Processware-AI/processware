---
type: WI
doc_id: WI-CMMI-04-01-01
title: "베이스라인 수립 — CI 식별·CM 시스템·릴리즈 (SP1.1~1.3)"
version: "0.1"
status: draft
owner: "Configuration Manager"
reviewer: "CCB Chair / QA Director"
approver: "CCB / CEO/CTO"
scope: "형상항목 식별 → CM 시스템(저장소·CCB) 수립 → 베이스라인 수립·릴리즈"
scope_code: CMMI
parent_pro: "[[PRO-CMMI-04-01_형상_관리_절차]]"
parent_pol: "[[POL-CMMI-04_지원_품질보증_정책]]"
related_tmp:
  - "[[TMP-CMMI-04-01-01-01_형상항목_CI_목록]]"
  - "[[TMP-CMMI-04-01-01-02_형상관리시스템_운영규정]]"
  - "[[TMP-CMMI-04-01-01-03_베이스라인_기술서]]"
related_rec: []
standards: [CMMI-DEV-ML3-V1.3]
standards_meta:
  publisher: "Software Engineering Institute (CMU/SEI)"
  year: 2010
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_acronym: CM
sg_sp_refs:
  - "CMMIDEV-CM-SP1.1-REQ-001"
  - "CMMIDEV-CM-SP1.2-REQ-001"
  - "CMMIDEV-CM-SP1.3-REQ-001"
entry_gate: null
scope_type: project
created: 2026-05-11
updated: 2026-05-11
tags: [WI, CMMI, CM, Support, ML2]
---

# 베이스라인 수립 — CI 식별·CM 시스템·릴리즈 (WI-CMMI-04-01-01)

> 상위 절차: [[PRO-CMMI-04-01_형상_관리_절차]] · 표준: CMMI-DEV V1.3 CM SG1

## 1. 업무 목적
프로젝트·조직 산출물 중 통제 대상 형상항목(CI)을 식별하고, CM 시스템(저장소·CCB·접근통제)을 수립하며, 합의된 CI 집합을 베이스라인으로 수립·릴리즈하여 변경 통제의 기준선을 확립한다.

## 2. 수행 주체
- **주 수행자**: Configuration Manager
- **검토자**: CCB, Project Manager
- **승인자**: CCB (베이스라인 릴리즈 승인)

## 3. 범위
PRO-CMMI-04-01 §5 의 **SP1.1(CI 식별) ~ SP1.3(베이스라인 수립·릴리즈)** 적용. 변경 추적·통제는 [[WI-CMMI-04-01-02]] 참조.

## 4. 입력 자료 / 산출물
- **Input**
  - 프로젝트 산출물 목록 (PP SP2.3 산출물)
  - 조직 CM 정책 ([[POL-CMMI-04]])
  - 기존 CM 시스템 운영 자산 (있을 경우)
- **Output**
  - [[TMP-CMMI-04-01-01-01_형상항목_CI_목록]] (작성본)
  - [[TMP-CMMI-04-01-01-02_형상관리시스템_운영규정]] (작성본, CCB 헌장 포함)
  - [[TMP-CMMI-04-01-01-03_베이스라인_기술서]] (릴리즈본)

## 5. 수행 절차

### 5.1 사전 준비
1. 프로젝트 산출물 목록(PP SP2.3) 확보 및 CI 후보 추출.
2. 조직 CM 정책·기존 CM 시스템 자산 조회.
3. CCB 위원 구성(Sponsor, CM, QA, 개발 대표 등) 후보 명단 확정.

### 5.2 수행 단계
1. **CI 식별 (SP1.1)**
   - CI 식별 기준 정의: 영향도·재사용·계약 인도물 여부 등.
   - 후보 산출물 → CI/비CI 분류 → 명명규칙(ID·버전) 부여.
   - 각 CI 의 책임자(Owner) 지정.
2. **CM 시스템 수립 (SP1.2)**
   - 저장소 선정·접근 권한 매트릭스 정의(읽기·쓰기·승인).
   - CCB 헌장 작성: 위원 구성·정족수·소집 주기·결정 권한.
   - 백업·복구·아카이브 절차 명시(RTO/RPO 포함).
3. **베이스라인 식별 및 합의 (SP1.3 전반)**
   - 베이스라인 종류 결정(요구사항·설계·제품 베이스라인 등).
   - 각 베이스라인 포함 CI 집합과 릴리즈 시점 정의.
4. **베이스라인 릴리즈 (SP1.3 후반)**
   - CCB 승인 회의 개최 → 의사록 작성.
   - 베이스라인 ID 부여 후 CM 시스템에 라벨링·잠금.
   - 이해관계자 통보(이메일 + PMC 보고서).
5. **형상관리시스템 운영규정 발효**
   - 운영규정 v1.0 승인 → 조직 게시판 공지.
   - OT 와 연계하여 PM/개발자 대상 교육 일정 등록.

### 5.3 완료 조건
- [ ] CI 목록 작성·검토 완료 (모든 CI 에 ID·Owner·분류 부여)
- [ ] CM 시스템 운영규정 승인 (CCB 헌장 포함)
- [ ] 베이스라인 1개 이상 CCB 승인·릴리즈 완료
- [ ] 베이스라인 ID 부여·잠금 확인
- [ ] 이해관계자 통보 기록 보관
- [ ] MAT-001 에 베이스라인 등록 완료

## 6. 인터페이스 부서
- **CM**: 본 지침 주 수행
- **CCB**: 베이스라인 승인 결재 ([[PRO-CMMI-04-01]] §3 RACI)
- **PP**: 산출물 목록·계획 입력 ([[PRO-CMMI-02-01]] SP2.3)
- **OT**: CM 시스템 교육 니즈 입력 ([[PRO-CMMI-01-03]] SP1.1)
- **All PAs**: CM 은 전 PA 의 work product 무결성 지원 (CM-supports-all)

## 7. 주의사항 / 예외 처리

### 7.1 CI 식별 누락 발견 (사후)
- 베이스라인 이후 미식별 CI 발견 시: 즉시 임시 CI 등록 → 차기 CCB 정식 등록.
- 누락 CI 가 베이스라인 결함을 야기했다면 PPQA 부적합 보고서 발행 ([[PRO-CMMI-04-03]]).

### 7.2 CCB 정족수 미달
- CCB 위원 50% 미만 참석 시 회의 연기 (최대 5영업일 이내 재소집).
- 긴급 변경 시 e-CCB(서면 합의) 허용 — 단, 최소 위원장 + 1명 동의 필수.

### 7.3 CM 시스템 장애
- 저장소 장애 발생 시 RTO 4시간 내 복구.
- 4시간 초과 시: 백업 저장소로 임시 전환 + 형상감사([[WI-CMMI-04-01-03]]) 즉시 발동.

## 8. 연계 템플릿 / 기록
- 템플릿:
  - [[TMP-CMMI-04-01-01-01_형상항목_CI_목록]]
  - [[TMP-CMMI-04-01-01-02_형상관리시스템_운영규정]]
  - [[TMP-CMMI-04-01-01-03_베이스라인_기술서]]
- 작성예시:
  - [[EX-CMMI-04-01-01-01_형상항목_CI_목록_작성예시]]
  - [[EX-CMMI-04-01-01-02_형상관리시스템_운영규정_작성예시]]
  - [[EX-CMMI-04-01-01-03_베이스라인_기술서_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-CM-SP1.1-REQ-001 (p.140)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-CM-SP1.2-REQ-001 (p.142)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-CM-SP1.3-REQ-001 (p.143)"
  retrieved_at: "2026-05-11"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (wi-tmp-writer) | - |
