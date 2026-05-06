---
type: WI
doc_id: "WI-ASPICE-01-11-05"
title: "재사용 자산 유지 및 검색성 (REU.2)"
version: "0.1"
owner: "Process Engineer"
reviewer: "Tech Lead / CM Engineer"
approver: "Reuse Asset Review Board"
scope: "등록된 재사용 자산 → 정기 갱신·폐기 관리 → 검색 인덱스 유지 → 엔지니어 재사용 지원"
parent_pro: "[[PRO-ASPICE-01-11_프로세스개선및재사용]]"
related_tmp: ["[[TMP-ASPICE-01-11-05-01_재사용자산유지보고서]]"]
related_rec: []
aspice_processes: ["REU.2"]
entry_gate: "WI-ASPICE-01-11-04.status == done"
scope_type: "common"
standards: ["Automotive SPICE 4.0"]
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, REU.2, ReuseAsset, Maintenance, Searchability]
---

# 재사용 자산 유지 및 검색성 (WI-ASPICE-01-11-05)

> 상위 절차: [[PRO-ASPICE-01-11_프로세스개선및재사용]]
> ASPICE 4.0 REU.2.BP4 — 재사용 자산 유지·검색성 보장

## 1. 업무 목적

본 지침은 [[WI-ASPICE-01-11-04_재사용자산등록및인증]] 으로 등록·인증된 재사용 자산에 대해 **분기별 정기 검토를 통해 갱신·폐기·재인증을 운영**하고, 검색 카탈로그(태그·키워드·도메인·성숙도) 의 인덱스를 최신 상태로 유지하며, 사용자(엔지니어) 의 검색·재사용을 지원하여 [[WI-ASPICE-01-11-03_재사용전략수립]] 의 재사용율 목표 달성을 뒷받침하는 데 목적이 있다.

## 2. 수행 주체

| 역할 | 담당 |
|---|---|
| 주수행자 | Process Engineer (또는 Reuse Asset Owner) |
| 검토자 | Tech Lead / CM Engineer |
| 승인자 | Reuse Asset Review Board |

## 3. 범위

[[WI-ASPICE-01-11-04_재사용자산등록및인증]] 으로 인증·등록된 모든 재사용 자산의 분기별 유지 활동에 적용한다. 등록 후 30일 미만 경과 자산은 첫 분기 점검에서 제외(다음 분기부터 포함).

## 4. 입력 자료 / 산출물

- **Input**:
  - 등록된 재사용 자산 목록 (Artifactory / Polarion / Confluence / ML Registry)
  - 자산별 사용 통계 (download / copy / reference 카운트)
  - 사용자 피드백 (Confluence 페이지 코멘트, 사내 설문, JIRA RA-FEEDBACK 채널)
  - 자산 갱신 PR 또는 폐기 요청
- **Output**:
  - [[TMP-ASPICE-01-11-05-01_재사용자산유지보고서]] 분기별 작성 산출물
  - 갱신·폐기 처리 결과 (저장소 메타데이터 갱신, 카탈로그 동기화)
  - 검색 카탈로그 인덱스 갱신 (Confluence 태그·키워드)
  - MAN.6 측정 연계 재사용율 보고

## 5. 수행 절차

### 5.1 사전 준비

1. 분기 시작 시 등록된 전체 자산 목록과 메타데이터를 추출한다.
2. 자산별 사용 통계(분기 download/copy/reference 수, 최근 사용일) 를 자동 수집 스크립트로 집계한다.
3. 사용자 피드백 채널(Confluence 코멘트, JIRA RA-FEEDBACK, 사내 설문) 의 신규 항목을 수집한다.
4. 자산 책임자 현황(퇴사·이동 여부) 을 점검한다.
5. Reuse Asset Review Board 분기 회의 일정을 확보한다.

### 5.2 수행 단계 (ASPICE REU.2.BP4 참조)

1. **자산 현황 집계** — 총 등록 / 활성 / 갱신중 / 폐기 / 폐기예정 의 5개 상태별 자산 수를 집계한다.
2. **자산별 상태 평가** — 자산별 (a) 최근 사용일, (b) 사용 프로젝트 수, (c) 결함 보고 건수, (d) 책임자 부재 여부 를 평가하여 상태 분류 (활성 유지 / 갱신 필요 / 폐기 예정 / 즉시 폐기) 한다.
3. **갱신 필요 자산 처리** — Major 변경 시 신규 버전 등록 및 [[WI-ASPICE-01-11-04_재사용자산등록및인증]] 재인증. Minor/Patch 는 책임자 자체 갱신 후 메타데이터만 갱신.
4. **폐기 후보 검토** — 12개월 미사용 또는 상위 호환 신규 자산 등장 시 폐기 후보로 분류하고, 책임자에게 통보 후 60일 유예 기간 부여.
5. **폐기 실행** — 유예 기간 내 활용 의견 미수렴 시 자산을 deprecated 표시 → 6개월 후 카탈로그에서 제거 (저장소는 archive 폴더로 이동, 형상 추적 보존).
6. **검색 인덱스 갱신** — Confluence 태그·키워드·도메인·성숙도 메타데이터를 갱신 및 검색 API 인덱스 재구축 트리거.
7. **사용자 피드백 분석** — 피드백 카테고리 분류(검색 어려움 / API 개선 / 문서 부족 / 결함 보고) 후 개선 항목을 OPP 백로그(WI-ASPICE-01-11-02) 로 이관.
8. **재사용율 산출 및 보고** — 분기 재사용율을 산출하여 [[WI-ASPICE-01-11-03_재사용전략수립]] 목표 대비 달성도를 보고. MAN.6 측정 시스템에 자동 연계.
9. **분기 보고 결재 및 공지** — Reuse Asset Review Board 결재 후 사내 공지(폐기 자산·신규 갱신 자산 안내).

### 5.3 완료 조건 체크리스트

- [ ] 분기 자산 현황 집계가 완료되었다 (총/활성/갱신중/폐기/폐기예정).
- [ ] 자산별 사용 통계가 수집되었다.
- [ ] 갱신 필요 자산이 처리되었다 (Major: 재인증, Minor/Patch: 메타데이터 갱신).
- [ ] 폐기 후보 자산에 60일 유예 통보가 발송되었다.
- [ ] 유예 만료 자산은 deprecated 표시 또는 카탈로그 제거가 완료되었다.
- [ ] 검색 인덱스가 갱신되고 검색 API 가 정상 동작한다.
- [ ] 사용자 피드백이 분류되고 개선 항목이 OPP 백로그로 이관되었다.
- [ ] 분기 재사용율이 산출되어 목표 대비 비교되었다.
- [ ] Reuse Asset Review Board 결재가 완료되었다.
- [ ] [[TMP-ASPICE-01-11-05-01_재사용자산유지보고서]] 가 결재 완료되어 `08_REC_기록/` 에 보관되었다.
- [ ] [[MAT-001_문서관리대장]] 에 본 산출물이 등록되었다.

## 6. 인터페이스 부서

| 부서 | 인터페이스 내용 |
|---|---|
| Reuse Asset Owner (자산 책임자) | 갱신·폐기 의견 제출, 책임자 인계 |
| Tech Lead | 자산 상태 평가 협력 |
| CM Engineer | 폐기 자산 archive 이동, 형상 추적 |
| Infrastructure | 저장소 용량·검색 API 운영 |
| 자산 사용 부서 (도메인 팀) | 활용 사례 제공, 폐기 의견 회신 |
| MAN.6 측정팀 | 재사용율 자동 연계, 분기 KPI 보고 |
| Process Improvement Board | 개선 항목 OPP 인계 |

## 7. 주의사항 / 예외 처리

1. **책임자 부재 자산** — 자산 책임자가 퇴사·이동하여 30일 이상 후임 미지정 시 임시 PQO 가 인계받고 60일 내 정식 후임 지정. 미지정 시 자산은 deprecated 처리 후 폐기 절차 진입.
2. **폐기 유예 기간 내 활용 부활** — 60일 유예 기간 중 활용 부서가 새로 등장하면 폐기 보류하고 재평가. 12개월 후 재검토.
3. **검색 API 장애** — 검색 API 가 24시간 이상 장애 시 카탈로그 페이지의 수동 검색(Confluence 기본) 으로 임시 대체하고 Infrastructure 와 즉시 협력.
4. **재사용율 목표 미달 지속** — 2분기 연속 목표 미달 시 [[WI-ASPICE-01-11-02_개선기회식별및실행]] 에 OPP 등록하고 원인 분석(검색 어려움·인지 부족·자산 부적합 등) 후 개선 과제 실행.

## 8. 연계 템플릿 / 기록

- 템플릿: [[TMP-ASPICE-01-11-05-01_재사용자산유지보고서]]
- 작성예시: [[EX-ASPICE-01-11-05-01_재사용자산유지보고서_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. 출처 (source_citation)

```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-REU.2-BP4"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력

| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — REU.2.BP4 자산 유지·검색성 정의 | (대기) |
