---
type: WI
doc_id: "WI-ASPICE-01-11-04"
title: "재사용 자산 등록 및 인증 (REU.2)"
version: "0.1"
owner: "Process Engineer"
reviewer: "Tech Lead / QA / Safety Engineer"
approver: "Reuse Asset Review Board"
scope: "재사용 후보 자산 → 품질·완전성 검토 → 인증 → 재사용 라이브러리 등록 → 메타데이터 관리"
parent_pro: "[[PRO-ASPICE-01-11_프로세스개선및재사용]]"
related_tmp: ["[[TMP-ASPICE-01-11-04-01_재사용자산등록서]]"]
related_rec: []
aspice_processes: ["REU.2"]
entry_gate: "WI-ASPICE-01-11-03.status == done"
scope_type: "common"
standards: ["Automotive SPICE 4.0"]
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, REU.2, ReuseAsset, Certification]
---

# 재사용 자산 등록 및 인증 (WI-ASPICE-01-11-04)

> 상위 절차: [[PRO-ASPICE-01-11_프로세스개선및재사용]]
> ASPICE 4.0 REU.2.BP2/BP3 — 재사용 자산 인증 평가 및 등록

## 1. 업무 목적

본 지침은 [[WI-ASPICE-01-11-03_재사용전략수립]] 에서 정의된 분류 체계와 인증 기준에 따라 **재사용 후보 자산을 품질·완전성·추적성·안전 분류 측면에서 평가**하고, Reuse Asset Review Board 의 인증을 거쳐 재사용 라이브러리(Artifactory / Polarion / Confluence / ML Registry) 에 메타데이터와 함께 등록하는 데 목적이 있다.

## 2. 수행 주체

| 역할 | 담당 |
|---|---|
| 주수행자 | Process Engineer (또는 자산 제안자) |
| 검토자 | Tech Lead / QA / Safety Engineer |
| 승인자 | Reuse Asset Review Board |

## 3. 범위

[[WI-ASPICE-01-11-03_재사용전략수립]] 에서 정의한 5개 자산 유형(SW 라이브러리·시험 케이스·설계 템플릿·요구사항 카탈로그·ML 모델) 의 등록·인증에 적용한다. 단일 프로젝트 내부 공통 모듈은 사내 활용에 한해 등록 의무 면제이나, 인증을 받으면 전사 재사용 자산으로 격상된다.

## 4. 입력 자료 / 산출물

- **Input**:
  - 재사용 후보 자산 (소스 코드·테스트 결과·문서)
  - [[WI-ASPICE-01-11-03_재사용전략수립]] 인증 기준
  - 자산 제안서 (제안자·도메인·예상 활용처)
  - 안전·보안 분류 자료 (해당 시 ASIL/SL 등급)
- **Output**:
  - [[TMP-ASPICE-01-11-04-01_재사용자산등록서]] 작성 산출물
  - 인증 결과 (승인/조건부/반려)
  - 등록된 자산 (Artifactory/Polarion/Confluence/ML Registry)
  - 메타데이터 (자산 ID, 버전, 도메인, 성숙도, 안전 등급, 사용 제약, 책임자)

## 5. 수행 절차

### 5.1 사전 준비

1. 재사용 후보 자산 제안서를 접수하고 [[WI-ASPICE-01-11-03_재사용전략수립]] 의 분류 체계 적합성을 1차 확인한다.
2. 인증 기준 체크리스트를 최신 버전으로 확보한다 (테스트 커버리지, 문서 완전성, 추적성, 안전 분류, 라이선스).
3. Reuse Asset Review Board 정기 회의 일정을 확인한다 (월 1회).
4. 자산 유형별 저장소(Artifactory / Polarion / Confluence / ML Registry) 등록 권한을 확인한다.
5. 라이선스 화이트리스트와 안전 등급 매핑 표를 준비한다.

### 5.2 수행 단계 (ASPICE REU.2.BP2/BP3 참조)

1. **자산 기본 정보 등록** — 자산 ID, 명칭, 유형, 버전, 담당자, 도메인, 인터페이스 명세를 표준 양식에 기록한다.
2. **품질 게이트 평가**
   - **테스트 커버리지** 측정 (단위 테스트 ≥ 80% 등) 및 결과 첨부.
   - **문서 완전성** 검토 (API 문서·사용 예제·제약사항·릴리스 노트).
   - **ASPICE 추적성** 확인 (요구사항·설계·테스트 추적 매트릭스 첨부).
   - **안전 분류** 평가 (해당 시 ASIL 등급, Safety Element out of Context 분석 첨부).
   - **라이선스 화이트리스트** 자동 검사.
3. **Tech Lead 검토** — 도메인 적합성, 인터페이스 일관성, 비기능 요구사항 충족 여부 검토.
4. **QA 검토** — 테스트 결과 신뢰성, 결함 미해결 항목 점검.
5. **Safety / Security Engineer 검토** — 안전·보안 등급 적정성 확인.
6. **Reuse Asset Review Board 심의** — 월 1회 정기 회의에서 종합 심의 후 승인/조건부/반려 결정.
7. **저장소 등록** — 승인 시 자산 유형별 저장소(Artifactory `shared-libs`, Polarion `Reuse Test Suites`, Confluence `Reuse Templates`, ML Registry `certified-models`) 에 등록하고 메타데이터를 입력한다.
8. **카탈로그 게시** — Confluence 재사용 카탈로그 페이지에 자산 정보(요약·링크·예제)를 게시한다.
9. **공지** — 사내 채널(메일·슬랙)에 신규 인증 자산을 공지하여 활용을 촉진한다.

### 5.3 완료 조건 체크리스트

- [ ] 자산 기본 정보(ID·명칭·유형·버전·담당자·도메인) 가 등록되었다.
- [ ] 테스트 커버리지가 인증 기준(≥ 80%) 을 충족한다.
- [ ] 문서 완전성(API·예제·제약·릴리스 노트) 이 100% 작성되었다.
- [ ] ASPICE 추적성 매트릭스가 첨부되었다.
- [ ] 안전 분류(해당 시 ASIL·SEooC) 가 명시되었다.
- [ ] 라이선스 화이트리스트 검사를 통과하였다.
- [ ] Tech Lead·QA·Safety/Security 검토가 완료되었다.
- [ ] Reuse Asset Review Board 심의 결과가 결재되었다.
- [ ] 저장소 등록과 카탈로그 게시가 완료되었다.
- [ ] [[TMP-ASPICE-01-11-04-01_재사용자산등록서]] 가 결재 완료되어 `08_REC_기록/` 에 보관되었다.
- [ ] [[MAT-001_문서관리대장]] 에 본 산출물이 등록되었다.

## 6. 인터페이스 부서

| 부서 | 인터페이스 내용 |
|---|---|
| 자산 제안 부서 (도메인 팀) | 자산 제안서 제출, 검토 의견 회신 |
| Tech Lead / SW Architect | 도메인 적합성 검토 |
| QA (SUP.1) | 테스트 결과 신뢰성 검토 |
| Safety Engineer | 안전 등급 검토 (해당 시) |
| Security Engineer | 보안 등급 검토 (해당 시) |
| Infrastructure | 저장소 권한·용량 관리 |
| Process Quality Office | 카탈로그 게시·공지 운영 |

## 7. 주의사항 / 예외 처리

1. **테스트 커버리지 미달** — 80% 미만이지만 도메인 특성상 측정 곤란한 경우(HW 의존 코드 등), Safety Engineer 가 대체 검증 방법(Mock·Stub·HIL 결과) 을 명시한 면제 신청서를 제출한다.
2. **문서 완전성 부분 미달** — 사용 예제 누락 등 경미한 미달은 조건부 승인(30일 내 보완) 으로 처리한다. 30일 미보완 시 등록 취소.
3. **라이선스 화이트리스트 위반** — GPL/AGPL 포함 자산은 자동 거부. 화이트리스트 외 라이선스 추가 요청은 Legal + Process Improvement Board 합동 검토.
4. **안전 등급 불일치 발견** — 인증 후 운영 중 안전 등급 재평가가 필요한 경우(상위 ASIL 시스템 적용 요구), 자산을 임시 deprecated 처리하고 Safety 재인증 후 등급 갱신.

## 8. 연계 템플릿 / 기록

- 템플릿: [[TMP-ASPICE-01-11-04-01_재사용자산등록서]]
- 작성예시: [[EX-ASPICE-01-11-04-01_재사용자산등록서_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. 출처 (source_citation)

```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-REU.2-BP2, VWAY-REU.2-BP3"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력

| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — REU.2.BP2/BP3 자산 등록·인증 정의 | (대기) |
