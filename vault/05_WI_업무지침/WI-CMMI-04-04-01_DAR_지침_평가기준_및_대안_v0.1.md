---
type: WI
doc_id: WI-CMMI-04-04-01
title: "DAR 적용 지침·평가기준·대안 (SP1.1~1.3)"
version: "0.1"
status: draft
owner: "Decision Facilitator"
reviewer: "Decision Owner"
approver: "Approver (사안별 위임 권한자)"
scope: "DAR 적용 지침 적용 → 평가 기준 수립(가중치) → 대안 식별"
scope_code: CMMI
parent_pro: "[[PRO-CMMI-04-04_의사결정_분석_결정_절차]]"
parent_pol: "[[POL-CMMI-04_지원_품질보증_정책]]"
related_tmp:
  - "[[TMP-CMMI-04-04-01-01_DAR_적용지침_적용결과서]]"
  - "[[TMP-CMMI-04-04-01-02_평가기준_정의서]]"
  - "[[TMP-CMMI-04-04-01-03_대안_목록]]"
related_rec: []
standards: [CMMI-DEV-ML3-V1.3]
standards_meta:
  publisher: "Software Engineering Institute (CMU/SEI)"
  year: 2010
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_acronym: DAR
sg_sp_refs:
  - "CMMIDEV-DAR-SP1.1-REQ-001"
  - "CMMIDEV-DAR-SP1.2-REQ-001"
  - "CMMIDEV-DAR-SP1.3-REQ-001"
entry_gate: null
scope_type: organization_project
created: 2026-05-11
updated: 2026-05-11
tags: [WI, CMMI, DAR, Support, ML3]
---

# DAR 적용 지침·평가기준·대안 (WI-CMMI-04-04-01)

> 상위 절차: [[PRO-CMMI-04-04_의사결정_분석_결정_절차]] · 표준: CMMI-DEV V1.3 DAR SG1 (전반)

## 1. 업무 목적
의사결정 사안에 대해 DAR(형식 평가 프로세스) 적용 여부를 객관 지침으로 판정하고, 적용 대상에 대해 평가 기준(가중치 포함)·대안 목록을 정의한다.

## 2. 수행 주체
- **주 수행자**: Decision Facilitator
- **검토자**: Decision Owner, 이해관계자
- **승인자**: Approver (TS·SAM·OPF 등 호출 영역별 위임권자)

## 3. 범위
PRO-CMMI-04-04 §5 의 **SP1.1(적용 지침) ~ SP1.3(대안 식별)** 적용. 평가 방법·평가는 [[WI-CMMI-04-04-02]] 참조.

## 4. 입력 자료 / 산출물
- **Input**
  - 의사결정 사안 (TS SP1.1, TS SP2.4, SAM SP1.2, OPF SP1.3 등에서 호출)
  - 조직 DAR 적용 지침
  - 사안 관련 정보(요구사항·제약·이해관계자 요구)
- **Output**
  - [[TMP-CMMI-04-04-01-01_DAR_적용지침_적용결과서]] (적용 여부 판정)
  - [[TMP-CMMI-04-04-01-02_평가기준_정의서]] (가중치 포함)
  - [[TMP-CMMI-04-04-01-03_대안_목록]]

## 5. 수행 절차

### 5.1 사전 준비
1. 의사결정 사안의 트리거 PA·SP 확인 (예: TS SP1.1 솔루션 선정).
2. 조직 DAR 적용 지침 최신 버전 확인.
3. 이해관계자·평가 패널 후보 검토.

### 5.2 수행 단계
1. **DAR 적용 지침 적용 (SP1.1)**
   - 사안의 영향도(비용·가역성·이해관계자 다양성·리스크) 평가.
   - 지침 항목별 판정 → DAR 적용 여부 결정.
   - 미적용 결정 시 일반 결정 절차 안내 → 본 WI 종료.
2. **평가 기준 수립 (SP1.2)**
   - 평가 기준 후보 도출 (성능·비용·일정·리스크·확장성·운영성 등).
   - 각 기준의 가중치(합=100% 또는 1.0) 부여.
   - 기준별 측정 방법·임계값 명시.
3. **이해관계자 검토**
   - 기준·가중치를 이해관계자와 검토 → 합의.
4. **대안 식별 (SP1.3)**
   - 사안에 대한 가능한 대안을 광범위하게 도출 (브레인스토밍·문헌·시장조사).
   - 명백히 부적합한 대안은 사유와 함께 조기 탈락.
   - 최종 후보 2~5개 권장.
5. **결과 정리·결재**
   - 적용 결과서·기준 정의서·대안 목록을 결재.

### 5.3 완료 조건
- [ ] DAR 적용 여부 판정 근거 명기
- [ ] 평가 기준 가중치 합 = 100% 또는 1.0
- [ ] 각 기준의 측정 방법·임계값 명시
- [ ] 이해관계자 검토 합의
- [ ] 대안 2~5개 식별 (조기 탈락 사유 포함)
- [ ] 결재 완료

## 6. 인터페이스 부서
- **DAR Facilitator**: 본 지침 주 수행
- **Decision Owner**: 사안 책임자 (R)
- **TS/SAM/OPF/IPM 등**: DAR 호출 영역
- **이해관계자**: 기준·대안 검토

## 7. 주의사항 / 예외 처리

### 7.1 DAR 적용 의무 사안 (조직 지침 트리거)
- 조직 지침이 명시한 의무 적용 사안(예: 5천만원 이상 외주, 핵심 아키텍처 결정 등):
  - "적용 여부" 판정 단계 생략 가능 — 직접 SP1.2 진입.

### 7.2 평가 기준 합의 실패
- 이해관계자 간 가중치 합의 실패 시:
  - Approver 가 중재 → 최종 결정.
  - 중재 불가 시 Senior Mgmt 에스컬레이션.

### 7.3 대안 부족 (1개 이하)
- 대안이 1개 이하인 경우 DAR 절차 자체가 무의미:
  - 대안 도출 재시도 (외부 자문·시장조사 확대).
  - 그래도 1개면 일반 결정 절차로 전환.

## 8. 연계 템플릿 / 기록
- 템플릿:
  - [[TMP-CMMI-04-04-01-01_DAR_적용지침_적용결과서]]
  - [[TMP-CMMI-04-04-01-02_평가기준_정의서]]
  - [[TMP-CMMI-04-04-01-03_대안_목록]]
- 작성예시:
  - [[EX-CMMI-04-04-01-01_DAR_적용지침_적용결과서_작성예시]]
  - [[EX-CMMI-04-04-01-02_평가기준_정의서_작성예시]]
  - [[EX-CMMI-04-04-01-03_대안_목록_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-DAR-SP1.1-REQ-001 (p.151)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-DAR-SP1.2-REQ-001 (p.152)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-DAR-SP1.3-REQ-001 (p.153)"
  retrieved_at: "2026-05-11"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (wi-tmp-writer) | - |
