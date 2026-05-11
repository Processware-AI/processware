---
type: WI
doc_id: WI-CMMI-03-02-02
title: "제품/컴포넌트 설계 + TDP (SG2: SP2.1~2.2)"
version: "0.1"
status: draft
owner: "Lead Architect"
reviewer: "Chief Engineer / Engineering Director"
approver: "Project Manager"
scope: "제품·컴포넌트 설계 → 기술자료패키지(TDP) 수립"
scope_code: CMMI
parent_pro: "[[PRO-CMMI-03-02_기술_솔루션_설계_절차]]"
parent_pol: "[[POL-CMMI-03_엔지니어링_정책]]"
related_tmp:
  - "[[TMP-CMMI-03-02-02-01_제품_컴포넌트_설계서]]"
  - "[[TMP-CMMI-03-02-02-02_기술자료패키지_TDP]]"
related_rec: []
standards: [CMMI-DEV-ML3-V1.3]
standards_meta:
  publisher: "Software Engineering Institute (CMU/SEI)"
  year: 2010
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_acronym: TS
sg_sp_refs:
  - "CMMIDEV-TS-SG2-REQ-001"
  - "CMMIDEV-TS-SP2.1-REQ-001"
  - "CMMIDEV-TS-SP2.2-REQ-001"
entry_gate: "WI-CMMI-03-02-01.status == done"
scope_type: project
created: 2026-05-11
updated: 2026-05-11
tags: [WI, CMMI, TS, Engineering, ML3]
---

# 제품/컴포넌트 설계 + TDP (WI-CMMI-03-02-02)

> 상위 절차: [[PRO-CMMI-03-02_기술_솔루션_설계_절차]]

## 1. 업무 목적
선정된 솔루션을 바탕으로 제품 아키텍처·컴포넌트 설계를 작성하고, 후속 단계(구현·검증·통합·운영)가 사용할 기술자료패키지(TDP) 를 수립한다.

## 2. 수행 주체
- **주 수행자**: Lead Architect, Domain Engineer
- **검토자**: Chief Engineer, VER Lead, PI Lead, CM
- **승인자**: Project Manager

## 3. 범위
PRO-CMMI-03-02 §5 의 **SP2.1 (Design the Product or Product Component) ~ SP2.2 (Establish a Technical Data Package)**.

## 4. 입력 자료 / 산출물
- **Input**
  - 선정된 솔루션 (WI-CMMI-03-02-01 산출물)
  - 요구사항 베이스라인 (RD/REQM)
  - 표준 / 패턴 카탈로그
- **Output**
  - [[TMP-CMMI-03-02-02-01_제품_컴포넌트_설계서]]
  - [[TMP-CMMI-03-02-02-02_기술자료패키지_TDP]] (CM 베이스라인)

## 5. 수행 절차

### 5.1 사전 준비
1. 선정 솔루션 결정 보고서 확보.
2. 적용 표준·패턴(예: 12-factor, OWASP ASVS, ISO 26262 등) 정리.
3. 설계 워크숍 일정 확정.

### 5.2 수행 단계
1. **제품 아키텍처 설계**
   - 컴포넌트 분해·역할·책임 (CRC) 명세.
   - 데이터 / 통신 / 보안 아키텍처 분리 작성.
   - 비기능 요구(품질 8축)와 아키텍처 매핑.
2. **컴포넌트 상세 설계**
   - 각 컴포넌트별 구조·인터페이스·상태기계·핵심 알고리즘 작성.
   - 의존성·재사용 자산 명시.
3. **설계 결정 기록(ADR)**
   - 영향 큰 결정마다 ADR (Architecture Decision Record) 생성.
   - DAR 적용 결정은 DAR ID 인용.
4. **설계 리뷰**
   - VER Lead + PI Lead + 도메인 SME 참여.
   - 리뷰 결함 정리·해소.
5. **TDP 수립 (SP2.2)**
   - 설계서·인터페이스·재료/부품·시험 명세·운영 한계·사용 매뉴얼 골격·검증 결과 인덱스를 1개 패키지로 묶음.
   - TDP 항목 체크리스트로 완전성 검증.
6. **CM 베이스라인**
   - TDP 를 CM 베이스라인으로 등록 ([[PRO-CMMI-04-01]]).
7. **PM 승인**

### 5.3 완료 조건 체크리스트
- [ ] 아키텍처: 데이터/통신/보안 3축 모두 작성
- [ ] 모든 컴포넌트(WI-CMMI-03-01-02 식별)에 상세 설계 존재
- [ ] 품질 8축 ↔ 아키텍처 매핑 표 작성
- [ ] 영향 큰 결정 ADR 발행
- [ ] 설계 리뷰 결함 0건 또는 해소
- [ ] TDP 체크리스트 100% 충족
- [ ] CM 베이스라인 등록
- [ ] PM 승인 결재

## 6. 인터페이스 부서
- **Architect / Engineer**: 주 수행
- **VER Lead**: 설계 시점 검증 요건 사전 점검 ([[PRO-CMMI-03-04]])
- **PI Lead**: 통합 가능성 사전 점검 ([[PRO-CMMI-03-03]])
- **CM**: TDP 베이스라인 등록 ([[PRO-CMMI-04-01]])
- **EPG**: 표준·패턴 자산 공급

## 7. 주의사항 / 예외 처리

### 7.1 요구사항 변경 (베이스라인 갱신)
- 본 WI 중에 RD 베이스라인 변경 발생:
  - 영향 평가 후 설계 부분 갱신 — 전체 재작성 금지.
  - 변경 로그 별도 시트 기록.

### 7.2 기술 성숙도 미흡
- 신규 기술 적용 부분이 검증되지 않음:
  - 별도 PoC + 학습 시간 일정 반영.
  - PoC 미통과 시 대안으로 변경 결정 — WI-CMMI-03-02-01 재실시.

### 7.3 TDP 항목 일부 누락
- 표준 TDP 항목 일부가 본 제품에 비적용(예: HW 부재로 재료/부품 N/A):
  - 명시적 N/A 표기 + 사유 + CM 검토 의견.
  - 묵시적 누락 금지 — 항상 항목별 상태(작성/N/A/연기) 기재.

## 8. 연계 템플릿 / 기록
- 템플릿:
  - [[TMP-CMMI-03-02-02-01_제품_컴포넌트_설계서]]
  - [[TMP-CMMI-03-02-02-02_기술자료패키지_TDP]]
- 작성예시:
  - [[EX-CMMI-03-02-02-01_제품_컴포넌트_설계서_작성예시]]
  - [[EX-CMMI-03-02-02-02_기술자료패키지_TDP_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-TS-SP2.1-REQ-001 (p.380)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-TS-SP2.2-REQ-001 (p.381)"
  retrieved_at: "2026-05-11"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (wi-tmp-writer) | - |
