---
type: WI
doc_id: "WI-VCSMS-02-01-05"
title: "재사용·OTS·out-of-context 컴포넌트 분석"
version: "0.1"
owner: "Project CS Lead"
reviewer: "Cybersecurity Manager (CSM)"
approver: "Cybersecurity Manager (CSM)"
scope: "재사용·OTS·OOC 컴포넌트 변경·영향·누락 WP·가정 검증·충족성 분석 (§6.4.4-6.4.6 [RQ-06-15~22])"
parent_pro: "[[PRO-VCSMS-02-01_프로젝트_사이버보안_관리_절차]]"
parent_pol: "[[POL-VCSMS-02_차량_사이버보안_엔지니어링_정책]]"
entry_gate: "WI-VCSMS-02-01-02.status == done"
scope_type: project
related_tmp:
  - "[[TMP-VCSMS-02-01-05-01_재사용_OTS_OOC_분석서]]"
related_rec: []
standards: ["ISO/SAE 21434"]
status: draft
created: 2026-06-14
updated: 2026-06-14
tags: [WI, VCSMS, ISO21434, reuse, OTS, out-of-context, interface_only]
---

# 재사용·OTS·out-of-context 컴포넌트 분석 (WI-VCSMS-02-01-05)

> 상위 절차: [[PRO-VCSMS-02-01_프로젝트_사이버보안_관리_절차]] · 정책: [[POL-VCSMS-02_차량_사이버보안_엔지니어링_정책]]

## 1. 업무 목적
재사용·OTS(off-the-shelf)·out-of-context(OOC) 컴포넌트에 대해 변경·영향·누락 작업산출물·가정 검증·요구 충족성을 분석하여, 사이버보안 공백 없이 통합 가능한지 판단하고 필요한 추가 활동을 식별한다. (§6.4.4~6.4.6 [RQ-06-15~22])

## 2. 수행 주체
- **주 수행자**: Project CS Lead
- **검토자**: TARA 분석가 / 보안 설계자
- **승인자**: Cybersecurity Manager (CSM)

## 3. 범위
본 지침은 PRO-VCSMS-02-01 §5 단계 5(재사용/OTS/OOC)에 적용한다. 관련성 판정서(WI-02)에서 상세분석 필요(Y)로 표기된 컴포넌트가 대상이다. 세 유형(재사용·OTS·OOC)을 각각의 요구로 분석한다.

## 4. 입력 자료 / 산출물
- **Input**
  - [[TMP-VCSMS-02-01-02-01_사이버보안_관련성_판정서]] (상세분석 대상)
  - 컴포넌트 사이버보안 문서(공급자 제공·기존 이력)
  - OOC 의도된 사용·맥락·외부 인터페이스 가정
- **Output**
  - [[TMP-VCSMS-02-01-05-01_재사용_OTS_OOC_분석서]] 작성분 (WP-06 보강, 누락 활동 식별)

## 5. 수행 절차 (단계별)

### 5.1 사전 준비
1. 관련성 판정에서 상세분석 필요로 표기된 컴포넌트 목록을 확정한다.
2. 각 컴포넌트의 유형(재사용/OTS/OOC)과 가용 문서를 수집한다.

### 5.2 수행 단계
1. **재사용 분석 (§6.4.4)**
   - 변경·환경변화 시 재사용 분석을 수행하고 변경·영향·누락 WP 를 식별한다([RQ-06-15,16]).
   - component 재사용은 요구 충족 능력·문서 충분성을 평가한다([RQ-06-17]).
2. **OOC 분석 (§6.4.5)**
   - 의도된 사용·맥락·외부 인터페이스 가정을 문서화한다([RQ-06-18]).
   - OOC 개발 요구를 가정 기반으로 정의([RQ-06-19])하고, 통합 시 클레임·가정을 검증한다([RQ-06-20]).
3. **OTS 분석 (§6.4.6)**
   - 관련 문서를 수집·분석해 요구 충족·적합성·문서 충분성을 판단한다([RQ-06-21]).
   - 문서 불충분 시 필요한 사이버보안 활동을 식별·수행한다([RQ-06-22]).
4. **누락 활동 반영·승인**
   - 식별된 누락 WP·추가 활동을 사이버보안 계획(WI-03)에 반영하고 CSM 승인을 받는다.

### 5.3 완료 조건
- [ ] 재사용 컴포넌트의 변경·영향·누락 WP 식별
- [ ] component 재사용의 요구 충족·문서 충분성 평가
- [ ] OOC 가정 문서화 + 통합 시 검증 계획
- [ ] OTS 문서 충분성 판단 + 불충분 시 추가 활동 식별
- [ ] 누락 활동을 계획에 반영 + CSM 승인

## 6. 인터페이스 부서
- **구매/SCM**: OTS/OOC 공급자 문서 입수 (Clause 7)
- **E/E 설계팀**: 통합 인터페이스·가정 검증
- **품질(QMS)**: 분석서 형상·문서 관리 (§5.4.4 경계면)

## 7. 주의사항 / 예외 처리

### 7.1 OTS 문서 입수 불가
- 공급자가 사이버보안 문서를 제공하지 못하는 경우:
  - 문서 불충분으로 간주하고 필요한 분석·테스트 활동을 당사가 직접 식별·수행([RQ-06-22]).
  - 입수 불가 사유와 보완 활동을 분석서에 기록.

### 7.2 OOC 가정 위반
- 통합 검증에서 OOC 의 가정·클레임이 위반된 경우:
  - 통합 차단하고 가정 재정의 또는 추가 통제 설계를 요구.
  - TARA 재수행 필요성을 평가.

### 7.3 재사용 환경 변화 미반영
- 재사용 시 운용환경 변화(공격면 추가 등)가 식별된 경우:
  - 무수정 재사용을 보류하고 변경분에 대한 재사용 분석을 수행([RQ-06-15]).

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-VCSMS-02-01-05-01_재사용_OTS_OOC_분석서]]
- 작성예시: [[EX-VCSMS-02-01-05-01_재사용_OTS_OOC_분석서_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. 출처 (source_citation)
```yaml
- type: standard_original
  file: "inputs/01_표준원문/AutoCyberSec/requirements.yaml"
  locator: "ISO/SAE 21434:2021 §6.4.4-6.4.6 [RQ-06-15~22]"
  retrieved_at: "2026-06-14"
  license: "ISO/SAE copyright"
  paraphrase_only: true
- type: business_flow
  file: "inputs/06_목표흐름/business_flow.yaml"
  locator: "SC-006"
  retrieved_at: "2026-06-14"
  license: "내부 자산"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-06-14 | 최초 초안 — §6.4.4-6.4.6 재사용·OTS·OOC 분석 | (미승인) |
