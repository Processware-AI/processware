---
type: WI
doc_id: WI-CMMI-03-02-03
title: "인터페이스 설계 + Make/Buy/Reuse (SG2: SP2.3~2.4)"
version: "0.1"
status: draft
owner: "Lead Architect / Procurement"
reviewer: "Chief Engineer / PI Lead"
approver: "Project Manager"
scope: "기준에 따른 인터페이스 설계(ICD) + 컴포넌트별 Make/Buy/Reuse 분석"
scope_code: CMMI
parent_pro: "[[PRO-CMMI-03-02_기술_솔루션_설계_절차]]"
parent_pol: "[[POL-CMMI-03_엔지니어링_정책]]"
related_tmp:
  - "[[TMP-CMMI-03-02-03-01_인터페이스_설계_명세서_ICD]]"
  - "[[TMP-CMMI-03-02-03-02_Make_Buy_Reuse_분석서]]"
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
  - "CMMIDEV-TS-SP2.3-REQ-001"
  - "CMMIDEV-TS-SP2.4-REQ-001"
entry_gate: "WI-CMMI-03-02-02.status == done"
scope_type: project
created: 2026-05-11
updated: 2026-05-11
tags: [WI, CMMI, TS, Engineering, ML3]
---

# 인터페이스 설계 + Make/Buy/Reuse (WI-CMMI-03-02-03)

> 상위 절차: [[PRO-CMMI-03-02_기술_솔루션_설계_절차]]

## 1. 업무 목적
조직 / 프로젝트 표준 기준에 따라 모든 인터페이스(내부·외부)를 ICD(Interface Control Document) 로 명세하고, 컴포넌트별 Make/Buy/Reuse 분석을 통해 조달 전략을 확정한다.

## 2. 수행 주체
- **주 수행자**: Lead Architect (ICD), Procurement (MBR)
- **검토자**: Chief Engineer, PI Lead, DAR Owner, Legal
- **승인자**: Project Manager

## 3. 범위
PRO-CMMI-03-02 §5 의 **SP2.3 (Design Interfaces Using Criteria) ~ SP2.4 (Perform Make, Buy, or Reuse Analyses)**.

## 4. 입력 자료 / 산출물
- **Input**
  - 인터페이스 요구사항 정의서 (WI-CMMI-03-01-02 산출)
  - 제품·컴포넌트 설계서 (WI-CMMI-03-02-02)
  - 조달 가이드·승인 공급업체 목록 (SAM)
- **Output**
  - [[TMP-CMMI-03-02-03-01_인터페이스_설계_명세서_ICD]]
  - [[TMP-CMMI-03-02-03-02_Make_Buy_Reuse_분석서]]
  - SAM 인계 정보 (Buy 선정 컴포넌트)

## 5. 수행 절차

### 5.1 사전 준비
1. IR 정의서 + 설계서 베이스라인 확보.
2. 조직 표준 인터페이스 기준(예: REST 가이드라인, 메시지 스키마 표준) 정리.
3. 승인 공급업체 목록(AVL) 최신본 확보.

### 5.2 수행 단계
1. **인터페이스 기준 적용 (SP2.3)**
   - 스키마·프로토콜·SLA·예외 처리·버전 정책·보안 요건 등 조직 기준 적용.
   - 비표준 채택 시 사유·승인 필수.
2. **ICD 작성**
   - 인터페이스별 1개 ICD (또는 묶음별).
   - 양 끝점·데이터 스키마(JSON Schema/Protobuf/XSD)·프로토콜·에러·재시도·SLA·관측가능성 명세.
3. **인터페이스 검토**
   - PI Lead + 양 끝점 컴포넌트 Owner 합동 검토.
4. **Make/Buy/Reuse 분석 (SP2.4)**
   - 컴포넌트별 4축 비교: 비용·일정·역량·리스크.
   - 영향 큰 결정은 DAR 적용.
5. **결정·후속 조치**
   - Make: 내부 개발 일정 반영.
   - Buy: SAM ([[PRO-CMMI-02-04]]) WI-01 입력 송부.
   - Reuse: EPG/PAL 자산 사용 협약.
6. **PI 인계**
   - ICD 를 PI ([[PRO-CMMI-03-03]]) WI-02 입력으로 송부.
7. **PM 승인**

### 5.3 완료 조건 체크리스트
- [ ] 모든 IR 에 1개 이상의 ICD 매핑
- [ ] ICD 항목: 양 끝점·스키마·프로토콜·SLA·에러·재시도·관측 7요소 모두
- [ ] 비표준 채택 사유·승인 첨부 (있는 경우)
- [ ] PI Lead 합동 검토 완료
- [ ] 모든 컴포넌트의 Make/Buy/Reuse 결정 완료
- [ ] Buy 결정에 SAM 인계 송부 기록
- [ ] PM 승인 결재

## 6. 인터페이스 부서
- **Architect / Procurement**: 주 수행
- **PI Lead**: ICD 수신 ([[PRO-CMMI-03-03]] SP2.1)
- **SAM Owner**: Buy 인계 수신 ([[PRO-CMMI-02-04]])
- **DAR Owner**: 영향 큰 결정 적용 ([[PRO-CMMI-04-04]])
- **EPG**: Reuse 자산 PAL 협약 ([[PRO-CMMI-01-01]])
- **Legal**: 외부 공급 계약 검토

## 7. 주의사항 / 예외 처리

### 7.1 표준 미준수 인터페이스
- 외부 시스템이 사내 표준을 따르지 않는 경우:
  - 적응 계층(Adapter) 도입 — 표준 측 인터페이스 노출.
  - 비호환 사유 + 적응 계층 위치를 ICD 에 명시.

### 7.2 공급업체 변경 (Buy)
- 조달 중 공급업체 변경:
  - 영향 평가 + 재DAR + ICD 재검토.
  - 변경 일자·사유·후속 조치를 별도 시트 기록.

### 7.3 Reuse 자산 부합 미흡
- PAL 자산이 70% 미만 부합:
  - Make 또는 Hybrid 로 재결정.
  - 부합도 평가 기준을 첨부.

## 8. 연계 템플릿 / 기록
- 템플릿:
  - [[TMP-CMMI-03-02-03-01_인터페이스_설계_명세서_ICD]]
  - [[TMP-CMMI-03-02-03-02_Make_Buy_Reuse_분석서]]
- 작성예시:
  - [[EX-CMMI-03-02-03-01_인터페이스_설계_명세서_ICD_작성예시]]
  - [[EX-CMMI-03-02-03-02_Make_Buy_Reuse_분석서_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-TS-SP2.3-REQ-001 (p.383)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-TS-SP2.4-REQ-001 (p.385)"
  retrieved_at: "2026-05-11"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (wi-tmp-writer) | - |
