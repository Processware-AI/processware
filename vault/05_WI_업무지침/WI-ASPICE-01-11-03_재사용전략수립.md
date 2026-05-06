---
type: WI
doc_id: "WI-ASPICE-01-11-03"
title: "재사용 전략 수립 (REU.2)"
version: "0.1"
owner: "Process Engineer"
reviewer: "Tech Lead / SW Architect"
approver: "Process Improvement Board"
scope: "조직 수준 재사용 전략 수립 → 재사용 자산 분류 체계 정의 → 재사용률 목표 설정 → 인프라 결정"
parent_pro: "[[PRO-ASPICE-01-11_프로세스개선및재사용]]"
related_tmp: ["[[TMP-ASPICE-01-11-03-01_재사용전략서]]"]
related_rec: []
aspice_processes: ["REU.2"]
entry_gate: null
scope_type: "common"
standards: ["Automotive SPICE 4.0"]
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, REU.2, Reuse, ReuseStrategy]
---

# 재사용 전략 수립 (WI-ASPICE-01-11-03)

> 상위 절차: [[PRO-ASPICE-01-11_프로세스개선및재사용]]
> ASPICE 4.0 REU.2.BP1 — 재사용 전략 정의

## 1. 업무 목적

본 지침은 VWAY Motors 의 **조직 수준 재사용 전략을 수립**하여 재사용 가능한 작업 산출물(SW 라이브러리·시험 케이스·설계 템플릿·요구사항 카탈로그) 의 식별 범위, 분류 체계, 재사용률 목표, 인프라(저장소·도구), 거버넌스, 교육 계획을 명문화한다. 본 전략은 [[WI-ASPICE-01-11-04_재사용자산등록및인증]] 과 [[WI-ASPICE-01-11-05_재사용자산유지및검색성]] 의 운영 기준이 된다.

## 2. 수행 주체

| 역할 | 담당 |
|---|---|
| 주수행자 | Process Engineer |
| 검토자 | Tech Lead / SW Architect |
| 승인자 | Process Improvement Board |

## 3. 범위

VWAY Motors 의 조직 차원 모든 재사용 가능 자산(SW 컴포넌트·HW 모듈·ML 모델·문서 템플릿) 의 전략 수립에 적용한다. 단일 프로젝트 내부 공통 모듈은 본 전략의 분류 체계 적용은 권장하되 등록 의무 대상은 아니다.

## 4. 입력 자료 / 산출물

- **Input**:
  - 조직 비즈니스 전략 (CTO 방향성)
  - [[POL-ASPICE-01_ASPICE역량거버넌스정책]] §3 원칙 2 (Generic Practice 제도화)
  - 기존 재사용 자산 인벤토리 (현황 분석)
  - 경쟁사·업계 재사용 사례 벤치마크
  - 인프라 도구 현황 (Artifactory, Confluence, Git 등)
- **Output**:
  - [[TMP-ASPICE-01-11-03-01_재사용전략서]] 작성 산출물
  - 재사용 자산 분류 체계(taxonomy)
  - 재사용률 목표 KPI (연도별)
  - 재사용 거버넌스 모델 (심의위원회·승인 절차)

## 5. 수행 절차

### 5.1 사전 준비

1. 조직 차원 재사용 현황을 인벤토리화한다 (현재 등록·운영 중인 라이브러리·템플릿 목록).
2. 도메인 분류(차량 SW: Powertrain / Chassis / Body / Infotainment / ADAS) 를 확정한다.
3. 자산 유형 분류(SW 라이브러리 / 시험 케이스 / 설계 템플릿 / 요구사항 카탈로그 / ML 모델) 를 확정한다.
4. 인프라 도구 옵션(Artifactory, Nexus, Confluence, Git submodule, 사내 Wiki)을 비교한다.
5. 경쟁사·업계 재사용률 벤치마크 자료를 수집한다.

### 5.2 수행 단계 (ASPICE REU.2.BP1 참조)

1. **재사용 비전·목표 정의** — CTO 방향성과 정렬된 재사용 비전을 정의하고, 연도별 재사용률 목표(예: Year1 30%, Year3 50%) 를 수립한다.
2. **재사용 범위 정의** — 재사용 대상 자산 유형(코드 라이브러리·시험 케이스·설계 템플릿·요구사항 카탈로그·ML 모델) 과 적용 도메인을 명시한다.
3. **분류 체계(taxonomy) 설계** — 도메인 × 자산 유형 × 성숙도(Experimental / Validated / Certified) 의 3차원 분류 체계를 설계한다.
4. **인프라 결정** — 저장소(SW: Artifactory, 문서: Confluence, ML 모델: ABC ML Registry), 검색 도구(Confluence + 태그 + 검색 API), 접근 권한 모델(부서별 Read/Write) 을 결정한다.
5. **거버넌스 정의** — 자산 심의위원회 구성(SW Architect + Tech Lead + QA + Safety Engineer), 인증 기준, 승인 절차, 정기 리뷰 주기(분기 1회)를 정의한다.
6. **측정 지표 정의** — 재사용률 측정 방법(분자: 재사용 컴포넌트 수, 분모: 신규 프로젝트 컴포넌트 총수), 분기 보고 양식, MAN.6 측정 연계를 정의한다.
7. **교육·전파 계획 수립** — 신규 입사자 온보딩 모듈, 분기 재사용 사례 발표회, 사내 카탈로그 사용 가이드 작성 계획을 수립한다.
8. **리스크·예외 정의** — 라이선스 충돌·안전 등급 불일치·도메인 격차 등의 리스크 시나리오와 대응 정책을 명시한다.
9. **결재 및 배포** — Process Improvement Board 승인 후 사내 게시·전파한다.

### 5.3 완료 조건 체크리스트

- [ ] 연도별 재사용률 목표가 수치로 정의되었다.
- [ ] 재사용 범위(자산 유형 + 도메인)가 명시되었다.
- [ ] 3차원 분류 체계(도메인 × 유형 × 성숙도)가 설계되었다.
- [ ] 저장소·검색 도구·권한 모델이 결정되었다.
- [ ] 자산 심의위원회 구성과 승인 절차가 정의되었다.
- [ ] 재사용률 측정 방법과 보고 주기가 정의되었다.
- [ ] 교육·전파 계획이 수립되었다.
- [ ] 리스크·예외 대응 정책이 명시되었다.
- [ ] Process Improvement Board 결재가 완료되었다.
- [ ] [[TMP-ASPICE-01-11-03-01_재사용전략서]] 가 결재 완료되어 `08_REC_기록/` 에 보관되었다.
- [ ] [[MAT-001_문서관리대장]] 에 본 산출물이 등록되었다.

## 6. 인터페이스 부서

| 부서 | 인터페이스 내용 |
|---|---|
| CTO Office | 재사용 비전·목표 승인 |
| SW Architecture Team | 분류 체계·인프라 검토 |
| Tech Leads | 도메인별 자산 식별 협력 |
| QA (SUP.1) | 인증 기준 검토 |
| Safety / Security | 안전·보안 등급 정책 검토 |
| Infrastructure | 저장소·도구 운영 책임 |
| HR / 교육팀 | 신규 입사자 온보딩 모듈 통합 |

## 7. 주의사항 / 예외 처리

1. **재사용률 목표의 무리한 상향** — Year1 50% 등 비현실적 목표 설정 시 형식적 등록 유발 위험. 첫해는 30% 이내로 보수적 설정 권고.
2. **라이선스 호환성 충돌** — 재사용 자산이 GPL/AGPL 등 copyleft 라이선스를 포함하면 양산 제품 통합 시 라이선스 위반. 자산 등록 단계에서 라이선스 화이트리스트 적용.
3. **안전 등급 불일치** — ASIL D 시스템에 ASIL QM 등급 자산을 재사용할 경우 안전 분석 필요. 분류 체계의 성숙도 차원에 안전 등급(ASIL) 메타데이터 포함.
4. **도메인 격차로 인한 부적합** — 다른 도메인(예: Infotainment 라이브러리를 ADAS 에 재사용) 적용 시 비기능 요구사항(실시간성·결정성) 차이로 부적합 가능. 분류 체계의 도메인 차원 + Tech Lead 검토 의무화.

## 8. 연계 템플릿 / 기록

- 템플릿: [[TMP-ASPICE-01-11-03-01_재사용전략서]]
- 작성예시: [[EX-ASPICE-01-11-03-01_재사용전략서_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. 출처 (source_citation)

```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-REU.2-BP1"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력

| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — REU.2.BP1 재사용 전략 정의 | (대기) |
