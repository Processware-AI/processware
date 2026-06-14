---
type: WI
doc_id: "WI-VCSMS-02-01-02"
title: "사이버보안 관련성·신규/재사용 분석"
version: "0.1"
owner: "Project CS Lead"
reviewer: "Cybersecurity Manager (CSM)"
approver: "Cybersecurity Manager (CSM)"
scope: "item/component 사이버보안 관련성·신규/재사용·테일러링 적용 여부 결정 (§6.4.2 [RQ-06-02])"
parent_pro: "[[PRO-VCSMS-02-01_프로젝트_사이버보안_관리_절차]]"
parent_pol: "[[POL-VCSMS-02_차량_사이버보안_엔지니어링_정책]]"
entry_gate: "WI-VCSMS-02-01-01.status == done"
scope_type: project
related_tmp:
  - "[[TMP-VCSMS-02-01-02-01_사이버보안_관련성_판정서]]"
related_rec: []
standards: ["ISO/SAE 21434"]
status: draft
created: 2026-06-14
updated: 2026-06-14
tags: [WI, VCSMS, ISO21434, relevance, reuse, interface_only]
---

# 사이버보안 관련성·신규/재사용 분석 (WI-VCSMS-02-01-02)

> 상위 절차: [[PRO-VCSMS-02-01_프로젝트_사이버보안_관리_절차]] · 정책: [[POL-VCSMS-02_차량_사이버보안_엔지니어링_정책]]

## 1. 업무 목적
대상 item/component 를 분석하여 (1) 사이버보안 관련성 여부, (2) 신규 개발/재사용/수정 구분, (3) 테일러링 적용 여부를 판정함으로써, 이후 계획 수립의 범위와 깊이를 결정한다. (§6.4.2 [RQ-06-02])

## 2. 수행 주체
- **주 수행자**: Project CS Lead
- **검토자**: TARA 분석가 / 보안 설계자
- **승인자**: Cybersecurity Manager (CSM)

## 3. 범위
본 지침은 PRO-VCSMS-02-01 §5 단계 2(관련성 분석)에 적용한다. 사이버보안 무관 판정 시 근거를 기록하고 절차를 종료한다. 재사용·OTS·OOC 의 상세 분석은 WI-VCSMS-02-01-05 로 이어진다.

## 4. 입력 자료 / 산출물
- **Input**
  - [[TMP-VCSMS-02-01-01-01_프로젝트_사이버보안_책임배정표]] (확정)
  - item/component 정의·아키텍처 개요
  - 기존 유사 제품/컴포넌트 이력(재사용 후보)
- **Output**
  - [[TMP-VCSMS-02-01-02-01_사이버보안_관련성_판정서]] 작성분 (관련성·신규/재사용·테일러링 판정)

## 5. 수행 절차 (단계별)

### 5.1 사전 준비
1. 책임배정표가 확정·승인되었는지 확인한다(entry_gate).
2. item/component 정의서와 아키텍처 개요를 수집한다.
3. 재사용 후보(기존 제품·플랫폼·OTS·OOC)를 식별한다.

### 5.2 수행 단계
1. **관련성 판정**
   - item/component 가 E/E 시스템으로서 사이버보안 자산·공격면을 갖는지 분석한다.
   - 외부 인터페이스·통신·데이터·업데이트 역량 유무로 관련성을 판정한다.
   - **무관 판정 시**: 근거를 명시 기록하고 CSM 승인 후 절차 종료(§7.1).
2. **신규/재사용 구분**
   - 각 component 를 신규 개발 / 재사용(무수정) / 수정 재사용 / OTS / OOC 로 분류한다.
   - 재사용·OTS·OOC 분류 항목은 WI-VCSMS-02-01-05 상세 분석 대상으로 표기한다.
3. **테일러링 적용 여부 예비 판단**
   - 리스크값 1 수준 등 활동 축소 근거가 예상되는 항목을 테일러링 후보로 표기한다([PM-06-13]). 실제 근거 검토는 WI-VCSMS-02-01-04.
4. **검토·승인**
   - TARA 분석가·보안 설계자 검토 후 CSM 이 판정서를 승인한다.

### 5.3 완료 조건
- [ ] 모든 item/component 의 관련성 판정 완료
- [ ] 무관 판정 항목은 근거 기록 + 승인
- [ ] 관련 항목의 신규/재사용/OTS/OOC 분류 완료
- [ ] 테일러링 후보 표기
- [ ] CSM 승인 획득

## 6. 인터페이스 부서
- **E/E 설계팀**: 아키텍처·인터페이스 정보 제공
- **구매/SCM**: OTS·OOC 컴포넌트 출처 정보
- **품질(QMS)**: 판정서 형상·문서 관리 (§5.4.4 경계면)

## 7. 주의사항 / 예외 처리

### 7.1 사이버보안 무관 판정
- 무관으로 판정 시:
  - 근거(자산·공격면 부재 등)를 구체적으로 기록.
  - CSM 승인 후 후속 계획 수립 단계를 생략하되, 판정서는 형상관리 대상으로 보존.
  - 차후 설계 변경으로 인터페이스 추가 시 관련성 재판정.

### 7.2 관련성 경계 모호
- 관련성 판단이 모호한 경우:
  - 보수적으로 "관련"으로 판정하고 컨셉 단계 TARA(§9.4)에서 재확인.
  - 판단 근거와 가정을 명시.

### 7.3 재사용 이력 불충분
- 재사용 후보의 사이버보안 문서·이력이 불충분한 경우:
  - OTS/OOC 절차(WI-VCSMS-02-01-05)로 회부하여 문서 충분성 평가([RQ-06-17] [RQ-06-22]).
  - 불충분 시 추가 활동 식별을 계획에 반영.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-VCSMS-02-01-02-01_사이버보안_관련성_판정서]]
- 작성예시: [[EX-VCSMS-02-01-02-01_사이버보안_관련성_판정서_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. 출처 (source_citation)
```yaml
- type: standard_original
  file: "inputs/01_표준원문/AutoCyberSec/requirements.yaml"
  locator: "ISO/SAE 21434:2021 §6.4.2 [RQ-06-02], [PM-06-13]"
  retrieved_at: "2026-06-14"
  license: "ISO/SAE copyright"
  paraphrase_only: true
- type: business_flow
  file: "inputs/06_목표흐름/business_flow.yaml"
  locator: "SC-005, SC-006"
  retrieved_at: "2026-06-14"
  license: "내부 자산"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-06-14 | 최초 초안 — §6.4.2 관련성·신규/재사용 분석 | (미승인) |
