---
type: WI
doc_id: "WI-SPICE-01-02-05"
title: "SW 컴포넌트/통합 검증 (SWE.5)"
version: "0.1"
owner: "SW Engineer"
reviewer: "QA / SW Architect"
approver: "SW Lead"
scope: "SW 유닛 → 컴포넌트/통합 시험 (Bottom-up) + SwAD↔통합 추적성"
parent_pro: "[[PRO-SPICE-01-02_소프트웨어공학프로세스]]"
related_tmp:
  - "[[TMP-SPICE-01-02-05-01_SW통합시험계획서및결과보고서]]"
related_rec: []
standards: ["Automotive SPICE 4.0"]
aspice_processes: ["SWE.5"]
entry_gate: "WI-SPICE-01-02-04.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SWE.5, Integration]
---

# SW 컴포넌트/통합 검증 업무지침 (WI-SPICE-01-02-05)

> 상위 절차: [[PRO-SPICE-01-02_소프트웨어공학프로세스]] §5 단계 10
> ASPICE 매핑: SWE.5 (Software Component Verification and Integration Verification) — BP1~BP5

## 1. 업무 목적

검증된 SW 유닛을 SwAD 의 통합 전략에 따라 단계적으로 통합하고, 컴포넌트·통합 인터페이스의 동작이 SwAD 사양을 충족함을 입증한다.

## 2. 수행 주체
- **주 수행자**: SW Engineer
- **검토자**: SW Architect, QA
- **승인자**: SW Lead

## 3. 범위
WI-SPICE-01-02-04 의 유닛 검증 통과 후부터 통합 빌드 + 시험 결과 보고서 등록까지 적용한다.

## 4. 입력 자료 / 산출물
- **Input**: Verified Units, SwAD, Integration Strategy
- **Output**: Integration Test Spec, Integration Test Report, Integrated SW Build

## 5. 수행 절차

### 5.1 사전 준비
1. 통합 시험 환경(Test Bench, Simulation) + CI 파이프라인 점검.
2. 통합 순서·단계(Stage) 결정.

### 5.2 수행 단계
1. **통합 전략 정의** (SWE.5.BP1)
   - Bottom-up 우선, 필요 시 Top-down 혼용.
   - 단계별 통합 범위·종료 기준 명시.

2. **통합 시험 케이스 설계** (SWE.5.BP2)
   - SwAD 인터페이스별 정상·경계·예외 케이스.
   - ASIL D 인터페이스는 강건성·결함 주입 시험 강제.

3. **단계적 통합·시험 실행** (SWE.5.BP3/4)
   - CI 파이프라인 자동 실행.
   - Fail 결함은 [[WI-SPICE-01-08-01_문제등록및분류]] 등록.

4. **회귀 시험** (SWE.5.BP4 후속)
   - 변경 발생 시 영향 범위 회귀 시험 자동 실행.

5. **결과 보고** (SWE.5.BP5)
   - 통합 빌드 + 보고서 → SWE.6 인계.

### 5.3 완료 조건 체크리스트
- [ ] 통합 전략에 단계·종료 기준 명시
- [ ] SwAD 의 모든 인터페이스에 대한 시험 케이스 존재
- [ ] ASIL D 인터페이스 결함 주입 시험 100% 실행
- [ ] 모든 Fail 결함 SUP.9 등록
- [ ] 회귀 시험 결과 무결성 확인
- [ ] CI 파이프라인 자동 빌드 + 시험 Pass
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **CM (SUP.8)**: 통합 빌드 형상관리
- **QA (SUP.1)**: 검토 게이트
- **System Engineering ([[PRO-SPICE-01-01]])**: SYS.4 통합 인계

## 7. 주의사항 / 예외 처리

### 7.1 인터페이스 모호성 발견
- 통합 시 SwAD 인터페이스 명세 모호 발견:
  - SWE.2 단계 회귀 → SwAD 보완.
  - 임시 가정 사용 금지.

### 7.2 통합 결함 폭증
- 단일 단계에서 다수 Fail:
  - 통합 중단 + 변경 롤백.
  - RCA 후 재개.

### 7.3 빌드 환경 변경
- Toolchain·라이브러리 버전 변경 시:
  - 변경 영향 분석 + 회귀 시험 전수 실행.
  - 결과 무결성 확인 후 진행.

### 7.4 결함 누설
- 유닛 시험 통과한 모듈에서 통합 시험 결함 발견:
  - 즉시 SWE.4 케이스 보완 + 재실행.
  - 결함 누설율 KPI 갱신 (분기 보고).

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-SPICE-01-02-05-01_SW통합시험계획서및결과보고서]]
- 작성예시: [[EX-SPICE-01-02-05-01_SW통합시험계획서및결과보고서_작성예시]]
- 기록 폴더: `vault/08_REC_기록/SWE.5/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SWE.5-PURPOSE-001 / VWAY-SWE.5-BP1~BP5"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SWE.5 BP1~BP5 + 회귀·결함 누설 관리 | (대기) |
