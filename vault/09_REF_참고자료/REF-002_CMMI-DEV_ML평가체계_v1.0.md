---
type: REF
doc_id: "REF-002"
title: "CMMI Maturity Level 평가체계 — ML3 인증 가이드"
version: "1.0"
source: "ISACA / CMMI Institute, CMMI Appraisal Method (SCAMPI/Benchmark)"
source_date: "2023"
author: "ISACA / CMMI Institute"
status: draft
created: 2026-04-29
updated: 2026-04-29
tags: [REF, CMMI, appraisal, ML3, paraphrase]
---

# CMMI Maturity Level 평가체계 — ML3 인증 가이드 (REF-002)

> 원문 출처: ISACA / CMMI Institute, *CMMI Appraisal Method* (구 SCAMPI → 현 Benchmark Appraisal)
> 라이선스: ISACA — paraphrase only
> 최종 확인일: 2026-04-29

## 요약

CMMI v3.0 의 ML 평가는 **Benchmark Appraisal** 방식으로 수행되며, ML3 통과 조건은 다음과 같다.

## 핵심 평가 방식

### 1. Appraisal 종류 (CMMI v3.0)
- **Benchmark Appraisal**: 공식 ML 인증 (3년 유효)
- **Sustainment Appraisal**: 인증 갱신 (2년차)
- **Action Plan Reappraisal**: 미충족 항목 재평가
- **Evaluation Appraisal**: 비공식 사전 진단

### 2. 평가 범위
- **Organizational Unit (OU)**: 평가 대상 조직 단위 (사업부·부서)
- **Sample Size**: OU 내 프로젝트·작업 그룹 중 표본 추출
- **Practice Coverage**: 모든 Required Practice 의 충족 증거 확인

### 3. ML3 평가 통과 조건
1. **ML2 PA 9개의 PG2 까지 모든 Practice 충족**
   - CM, MC, MPM, PAD, PLAN, PQA, RDM, RSK, SAM
2. **ML3 PA 11개의 PG3 까지 모든 Practice 충족**
   - CAR, DAR, EST, GOV, II, OT, PCM, PR, VV, PI, TS
   - (단, GOV·II 는 ML2 PG2 부터 평가 시작)
3. **조직 표준 프로세스 집합(OSSP) 의 운영 증거**
4. **프로세스 자산 라이브러리(PAL) 운영 증거**
5. **측정 저장소(Measurement Repository) 운영 증거**
6. **각 Practice 의 일관된 수행 증거** — 표본 프로젝트·표본 작업 그룹 전체에서 동일하게 수행

### 4. 평가 단계
1. **Readiness Review (준비 검토)**: 사전 자가진단
2. **Plan & Prepare**: 평가 일정·범위·증거 수집 계획
3. **Conduct Appraisal**: 인터뷰·문서 검토·증거 매핑
4. **Report Results**: ML 인증 발행 또는 시정 권고

### 5. 증거 유형
각 Practice Statement 충족 증거는 다음 중 1개 이상 필요:
- **Direct Artifact**: Practice 수행의 직접 산출물(예: CM-2.3 의 기준선 릴리스 노트)
- **Indirect Artifact**: 간접 증거(예: 회의록·이메일·추적도구 로그)
- **Affirmation**: 인터뷰 답변

## 핵심 조항 / 요구사항

| 평가 요소 | 요지 | 본 체계 적용 영향 |
|---|---|---|
| Required Practice 충족 | 모든 Practice Statement 가 OU 내에서 일관되게 수행 | 모든 Req-ID 가 POL/PRO/WI 와 매핑 필수 |
| OSSP 운영 | 조직 표준 프로세스 집합 + Tailoring 지침 보유 | PAD-3.1, PAD-3.2 → POL-CMMI-01 영역 |
| PAL 운영 | 프로세스 자산 라이브러리 (도구·템플릿·예시) | PAD-3.3 → 본 체계의 99_템플릿/ + 09_REF 와 매핑 |
| 측정 저장소 | 조직 차원의 측정 데이터 누적 | MPM-3.2, EST-3.1 → 단일 측정저장소 인스턴스 |
| Tailoring | 프로젝트가 OSSP 를 테일러링하여 사용 | 본 체계의 테일러링 가이드 작성 필수 |
| 내부 평가자 | OU 외부 또는 독립 평가자 권장 | 자체 사전진단 시 SEPG·QA 역할 |

## 적용 영향

### 본 체계(CMMI-DEV-ML3 편입) 에 미치는 영향
- **추적성 매트릭스(MAT-011) 필수**: 모든 Practice → POL/PRO/WI/TMP/REC 매핑
- **REC(기록) 보존 정책**: 평가 시 표본 프로젝트의 REC 증거 필요 → REC 보관기간 정책화
- **테일러링 가이드 필수**: PAD-3.2 충족 위해 OSSP 테일러링 절차 문서화 필요
- **PG2/PG3 표시**: WI 단위에서 어떤 Practice·Practice Group 을 충족하는지 frontmatter 표시 권장

## 관련 내부 문서

- [[00_CMMI-DEV-ML3_표준개요]]
- [[01_CMMI-DEV-ML3_요구사항분해]]
- [[REF-001_CMMI-DEV-v3.0_모델구조_v1.0]]

## 원문 인용

> 본 REF 는 paraphrase 만 포함. 원문 인용은 ISACA 라이선스에 따라 금지.

## 변경 알림

- 외부 원문 개정(평가 방법 변경) 시: 본 REF 버전 업 + MAT-002 동기화
