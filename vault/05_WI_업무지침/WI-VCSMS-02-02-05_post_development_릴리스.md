---
type: WI
doc_id: "WI-VCSMS-02-02-05"
title: "post-development 릴리스"
version: "0.1"
owner: "Cybersecurity Manager (CSM)"
reviewer: "Project CS Lead"
approver: "Top Management (경영진)"
scope: "릴리스 전 케이스·평가보고서·post-dev 요구 가용화 및 릴리스 조건 충족 (§6.4.9 [RQ-06-33,34])"
parent_pro: "[[PRO-VCSMS-02-02_사이버보안_케이스_평가_및_릴리스_절차]]"
parent_pol: "[[POL-VCSMS-02_차량_사이버보안_엔지니어링_정책]]"
entry_gate: "WI-VCSMS-02-02-04.status == done"
scope_type: project
related_tmp:
  - "[[TMP-VCSMS-02-02-05-01_릴리스_체크리스트_및_릴리스보고서]]"
related_rec: []
standards: ["ISO/SAE 21434"]
status: draft
created: 2026-06-14
updated: 2026-06-14
tags: [WI, VCSMS, ISO21434, release, post-development, interface_only]
---

# post-development 릴리스 (WI-VCSMS-02-02-05)

> 상위 절차: [[PRO-VCSMS-02-02_사이버보안_케이스_평가_및_릴리스_절차]] · 정책: [[POL-VCSMS-02_차량_사이버보안_엔지니어링_정책]]

## 1. 업무 목적
릴리스 전에 사이버보안 케이스·(해당 시)평가 보고서·post-development 사이버보안 요구를 가용화하고, 릴리스 조건(케이스 논거 충족·평가 확인·요구 수용)이 모두 충족되었는지 게이트로 검증하여 post-development 릴리스를 결정·기록한다. (§6.4.9 [RQ-06-33,34])

## 2. 수행 주체
- **주 수행자**: Cybersecurity Manager (CSM)
- **검토자**: Project CS Lead
- **승인자**: Top Management (경영진) — 릴리스 결정

## 3. 범위
본 지침은 PRO-VCSMS-02-02 §5 단계 6(릴리스)에 적용한다. 평가 미수행 결정 시에도 케이스·post-dev 요구 충족 검증은 수행한다. 릴리스 후 운영·생산 단계는 후속 절차(PRO-VCSMS-02-07 생산, PRO-VCSMS-02-09 운영)로 연결된다.

## 4. 입력 자료 / 산출물
- **Input**
  - [[TMP-VCSMS-02-02-01-01_사이버보안_케이스]] (승인, open 0)
  - [[TMP-VCSMS-02-02-04-01_사이버보안_평가보고서]] (해당 시, 조건 종결)
  - post-development 사이버보안 요구 (WP-10-02)
- **Output**
  - [[TMP-VCSMS-02-02-05-01_릴리스_체크리스트_및_릴리스보고서]] 작성분 (WP-06-04)

## 5. 수행 절차 (단계별)

### 5.1 사전 준비
1. 평가 보고서가 완료되었는지(또는 평가 미수행 결정인지) 확인한다(entry_gate).
2. 케이스의 open 논거와 평가 보고서의 조건부 조건 종결 상태를 확인한다.

### 5.2 수행 단계
1. **릴리스 산출물 가용화**
   - 케이스·(해당 시)평가 보고서·post-dev 요구를 릴리스 결정자에게 가용화한다([RQ-06-33]).
2. **릴리스 조건 게이트 점검**
   - (a) 케이스 논거 충족(open 0), (b) 평가 확인(수용 또는 조건 종결), (c) post-dev 요구 수용을 각각 점검한다([RQ-06-34]).
   - 하나라도 미충족이면 릴리스 차단(§7.1).
3. **릴리스 결정·승인**
   - 모든 조건 충족 시 경영진이 릴리스를 승인한다.
4. **릴리스 보고서 작성·기록**
   - 릴리스 결정·근거·충족 증적을 릴리스 보고서에 기록하고 형상관리에 등록한다.

### 5.3 완료 조건
- [ ] 케이스·평가보고서·post-dev 요구 가용화
- [ ] 케이스 논거 충족(open 0) 확인
- [ ] 평가 확인(수용/조건 종결) 확인
- [ ] post-development 요구 수용 확인
- [ ] 경영진 릴리스 승인 + 릴리스 보고서 형상 등록

## 6. 인터페이스 부서
- **경영진**: 릴리스 결정·승인
- **생산/운영팀**: post-dev 요구 인수 (PRO-02-07, 02-09)
- **품질(QMS)**: 릴리스 보고서 형상·문서 관리 (§5.4.4 경계면)

## 7. 주의사항 / 예외 처리

### 7.1 조건 미충족 릴리스 시도
- 릴리스 조건 중 하나라도 미충족인 상태로 릴리스를 시도하는 경우:
  - 릴리스 게이트를 차단하고 미충족 항목을 명시.
  - KPI(조건 미충족 릴리스 0건) 위반 — 강행 불가.

### 7.2 조건부 수용 조건 미종결
- 평가 보고서의 조건부 수용 조건이 기한 내 종결되지 않은 경우:
  - 릴리스를 보류하고 조건 종결 계획을 재수립.
  - 종결 불가 시 거부로 전환·재작업.

### 7.3 릴리스 후 결함 발견
- 릴리스 후 사이버보안 결함·취약점이 발견된 경우:
  - 지속활동(PRO-VCSMS-01-03)·사고대응(PRO-VCSMS-01-04)으로 연계.
  - 필요 시 업데이트(PRO-VCSMS-02-09) 또는 리콜 절차 가동.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-VCSMS-02-02-05-01_릴리스_체크리스트_및_릴리스보고서]]
- 작성예시: [[EX-VCSMS-02-02-05-01_릴리스_체크리스트_및_릴리스보고서_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. 출처 (source_citation)
```yaml
- type: standard_original
  file: "inputs/01_표준원문/AutoCyberSec/requirements.yaml"
  locator: "ISO/SAE 21434:2021 §6.4.9 [RQ-06-33,34]"
  retrieved_at: "2026-06-14"
  license: "ISO/SAE copyright"
  paraphrase_only: true
- type: business_flow
  file: "inputs/06_목표흐름/business_flow.yaml"
  locator: "SC-007"
  retrieved_at: "2026-06-14"
  license: "내부 자산"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-06-14 | 최초 초안 — §6.4.9 post-development 릴리스 | (미승인) |
