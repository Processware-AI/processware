---
type: WI
doc_id: WI-CMMI-01-01-03
title: "측정저장소 및 PAL 구축·운영 (SP1.4~1.5)"
version: "0.1"
status: draft
owner: "Measurement Analyst"
reviewer: "EPG Lead"
approver: "CEO/CTO"
scope: "조직 측정저장소 구조 정의 및 PAL 카탈로그 등록·운영"
scope_code: CMMI
parent_pro: "[[PRO-CMMI-01-01_조직_표준프로세스_수립_유지_절차]]"
parent_pol: "[[POL-CMMI-01_조직_프로세스_거버넌스_정책]]"
related_tmp:
  - "[[TMP-CMMI-01-01-03-01_측정저장소_PAL_운영서]]"
standards: [CMMI-DEV-ML3-V1.3]
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_acronym: OPD
sg_sp_refs: ["CMMIDEV-OPD-SP1.4-REQ-001", "CMMIDEV-OPD-SP1.5-REQ-001"]
entry_gate: "WI-CMMI-01-01-01.status == done"
scope_type: organization
created: 2026-05-11
updated: 2026-05-11
tags: [WI, CMMI, OPD, ML3]
---

# 측정저장소·PAL 구축·운영 (WI-CMMI-01-01-03)

> 상위 절차: [[PRO-CMMI-01-01_조직_표준프로세스_수립_유지_절차]]

## 1. 업무 목적
조직 측정 데이터를 통합 저장·조회 가능한 측정저장소를 구축하고, OSSP·라이프사이클 모델·테일러링 가이드 등 OPA를 PAL 에 카탈로그 등록하여 전 프로젝트가 접근 가능하도록 한다.

## 2. 수행 주체
- **주 수행자**: Measurement Analyst (저장소), CM (PAL)
- **검토자**: EPG Lead
- **승인자**: CEO/CTO

## 3. 범위
PRO-CMMI-01-01 §5 의 SP1.4·SP1.5 단계. 운영 단계의 데이터 등록·조회는 PMC/MA 절차로 위임.

## 4. 입력 자료 / 산출물
- **Input**: OSSP, MA 측정 명세, OPA 자산 목록
- **Output**: [[TMP-CMMI-01-01-03-01_측정저장소_PAL_운영서]], 저장소 스키마, PAL 인덱스

## 5. 수행 절차

### 5.1 사전 준비
1. MA SP1.1~1.4 산출 측정 명세 확보.
2. 저장소 도구·DB 후보 선정.

### 5.2 수행 단계
1. **측정저장소 구조 설계** — 측정 도메인·메트릭·단위·메타데이터 스키마 정의
2. **PAL 카탈로그 구조 설계** — 자산 분류·메타·접근권한 정의
3. **초기 데이터 등록** — 기존 측정값·OPA 자산 마이그레이션
4. **접근 정책 수립** — 역할별 권한 매트릭스
5. **사용 가이드 작성** — 등록·조회 절차서
6. **운영 점검 주기 정의** — 분기 무결성·접근로그 감사
7. **승인 + CM 베이스라인 등록**

### 5.3 완료 조건
- [ ] 저장소 스키마 승인 + 운영 환경 가동
- [ ] PAL 인덱스 작성 + OPA 자산 100% 등록
- [ ] 사용 가이드 배포 + 교육 완료
- [ ] 접근 권한 매트릭스 적용
- [ ] CM 베이스라인 + MAT-001 등록

## 6. 인터페이스 부서
- **MA**: 측정 명세 공급 ([[PRO-CMMI-04-02]])
- **CM**: PAL 자산 베이스라인 통제
- **IT**: 저장소 인프라 운영

## 7. 주의사항 / 예외 처리

### 7.1 저장소 장애
- 24시간 초과 장애 시 OPF 평가 일시 중단 + 백업 데이터로 복구.

### 7.2 데이터 품질 이슈
- 측정 단위 불일치 발견 시 MA SP1.3 재검토 → 일괄 정규화.

### 7.3 자산 중복 등록
- PAL 자산 중복 발견 시 CM 마스터로 통합 + alias 매핑.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-CMMI-01-01-03-01_측정저장소_PAL_운영서]]
- 작성예시: [[EX-CMMI-01-01-03-01_측정저장소_PAL_운영서_작성예시]]

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-OPD-SP1.4-REQ-001 (p.197)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-OPD-SP1.5-REQ-001 (p.199)"
  retrieved_at: "2026-05-11"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 | - |
