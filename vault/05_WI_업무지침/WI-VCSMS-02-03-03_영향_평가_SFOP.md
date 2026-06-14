---
type: WI
doc_id: "WI-VCSMS-02-03-03"
title: "영향 평가 (S/F/O/P 4등급)"
version: "0.1"
owner: "TARA 분석가"
reviewer: "안전 담당 / 보안 설계자"
approver: "Cybersecurity Manager (CSM)"
scope: "피해 시나리오를 S/F/O/P 범주별 severe~negligible 4등급 판정 (§15.5 [RQ-15-04~07][PM-15-07])"
parent_pro: "[[PRO-VCSMS-02-03_위협분석_및_리스크평가_TARA_절차]]"
parent_pol: "[[POL-VCSMS-02_차량_사이버보안_엔지니어링_정책]]"
entry_gate: "WI-VCSMS-02-03-01.status == done"
scope_type: project
related_tmp:
  - "[[TMP-VCSMS-02-03-03-01_영향평가표]]"
related_rec: []
standards: ["ISO/SAE 21434"]
status: draft
created: 2026-06-14
updated: 2026-06-14
tags: [WI, VCSMS, ISO21434, TARA, impact-rating, SFOP, interface_only]
---

# 영향 평가 (S/F/O/P 4등급) (WI-VCSMS-02-03-03)

> 상위 절차: [[PRO-VCSMS-02-03_위협분석_및_리스크평가_TARA_절차]] · 정책: [[POL-VCSMS-02_차량_사이버보안_엔지니어링_정책]]
> **횡단 방법론** — TARA 3단계. 안전 영향등급은 ISO 26262-3 §6.4.3 으로 도출.

## 1. 업무 목적
피해 시나리오를 안전(Safety)·재무(Financial)·운영(Operational)·프라이버시(Privacy) 4개 영향 범주별로 severe/major/moderate/negligible 4등급으로 판정하여, 리스크값 결정의 영향 축을 제공한다. 안전 영향등급은 ISO 26262-3:2018 §6.4.3 에 따라 도출한다. (§15.5 [RQ-15-04~07][PM-15-07])

## 2. 수행 주체
- **주 수행자**: TARA 분석가
- **검토자**: 안전 담당(안전 범주) / 보안 설계자
- **승인자**: Cybersecurity Manager (CSM)

## 3. 범위
본 지침은 PRO-VCSMS-02-03 §5 단계 3(영향 평가)에 적용한다. 자산·피해 시나리오(WI-01)를 입력으로 받아 영향등급(WP-15-04)을 산출한다. 등급 정의표는 ISO 원문 Table 을 직접 전재하지 않고 조직 자체 영향등급표로 재구성하여 사용한다(저작권). [PM-15-07] 에 따라 타 범주가 덜 치명적임을 논증하면 해당 범주 추가 분석을 생략할 수 있다.

## 4. 입력 자료 / 산출물
- **Input**
  - [[TMP-VCSMS-02-03-01-01_자산_및_피해시나리오_목록]] (승인)
  - 조직 자체 영향등급표 (S/F/O/P 4등급 정의, 내부 재구성)
  - 안전 영향: ISO 26262-3 §6.4.3 도출 결과 (안전 담당 제공)
- **Output**
  - [[TMP-VCSMS-02-03-03-01_영향평가표]] 작성분 (WP-15-04)

## 5. 수행 절차 (단계별)

### 5.1 사전 준비
1. 자산·피해 시나리오 목록이 승인되었는지 확인한다(entry_gate).
2. 조직 자체 S/F/O/P 영향등급 정의표(재구성본)를 준비한다.
3. 안전 범주는 안전 담당에게 ISO 26262-3 §6.4.3 기반 영향등급을 요청한다.

### 5.2 수행 단계
1. **범주별 영향 판정**
   - 각 피해 시나리오를 S/F/O/P 4범주에 대해 severe/major/moderate/negligible 로 판정한다([RQ-15-04,05]).
   - 안전(S) 등급은 ISO 26262-3 §6.4.3 도출 결과를 사용한다([RQ-15-06]).
2. **최고 영향등급 결정**
   - 각 피해 시나리오의 범주별 등급 중 최고 등급을 대표 영향으로 기록한다.
3. **생략 논증 (해당 시)**
   - 특정 범주가 타 범주 대비 덜 치명적임을 논증할 수 있으면 해당 범주 추가 분석을 생략하고 근거를 기록한다([PM-15-07]).
4. **검토·승인**
   - 안전 담당이 안전 등급의 ISO 26262 정합성을 확인하고 CSM 이 승인한다.

### 5.3 완료 조건
- [ ] 각 피해 시나리오의 S/F/O/P 4범주 등급 판정
- [ ] 안전(S) 등급 ISO 26262-3 §6.4.3 정합 확인
- [ ] 범주별 최고 영향등급 기록
- [ ] (생략 시) 생략 논증 근거 기록
- [ ] CSM 승인

## 6. 인터페이스 부서
- **안전 담당(ISO 26262)**: 안전 영향등급 도출·정합 확인 (§15.5 [RQ-15-06])
- **법무/프라이버시**: 프라이버시(P) 영향 자문
- **품질(QMS)**: 산출물 형상·문서 관리 (§5.4.4 경계면)

## 7. 주의사항 / 예외 처리

### 7.1 안전 영향등급 불일치
- 안전(S) 등급이 ISO 26262 HARA 결과와 불일치하는 경우:
  - 안전 담당과 정합화하고, 정합 전까지 보수적(상위) 등급을 잠정 적용.
  - KPI(안전 영향등급 ISO 26262 정합율 100%) 준수.

### 7.2 등급표 외 임의 판정
- 조직 등급표 정의에 없는 임의 기준으로 판정하려는 경우:
  - 금지. 반드시 자체 등급표 정의에 따라 판정하고, 정의 보완이 필요하면 등급표를 개정 후 적용.

### 7.3 생략 논증 부실
- [PM-15-07] 생략 논증이 부실한 경우:
  - 생략을 철회하고 해당 범주를 정식 평가.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-VCSMS-02-03-03-01_영향평가표]]
- 작성예시: [[EX-VCSMS-02-03-03-01_영향평가표_작성예시]]
- 기록 폴더: `08_REC_기록/`
- 참고: 조직 자체 S/F/O/P 영향등급 정의표 (REF — ISO 원문 Table 재구성)

## 9. 출처 (source_citation)
```yaml
- type: standard_original
  file: "inputs/01_표준원문/AutoCyberSec/requirements.yaml"
  locator: "ISO/SAE 21434:2021 §15.5 [RQ-15-04~07][PM-15-07] (등급 정의 재구성)"
  retrieved_at: "2026-06-14"
  license: "ISO/SAE copyright"
  paraphrase_only: true
- type: standard_original
  file: "vault/09_REF_참고자료/REF-003_ISO26262_기능안전_경계면.md"
  locator: "ISO 26262-3:2018 §6.4.3 안전 영향등급 도출"
  retrieved_at: "2026-06-14"
  license: "ISO copyright"
  paraphrase_only: true
- type: business_flow
  file: "inputs/06_목표흐름/business_flow.yaml"
  locator: "SC-008"
  retrieved_at: "2026-06-14"
  license: "내부 자산"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-06-14 | 최초 초안 — §15.5 영향 평가(S/F/O/P) | (미승인) |
