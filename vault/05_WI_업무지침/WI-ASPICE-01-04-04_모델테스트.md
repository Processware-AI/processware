---
doc_id: "WI-ASPICE-01-04-04"
title: "모델 테스트 (MLE.4)"
type: WI
version: "0.1"
status: draft
owner: "ML Test Engineer"
reviewer: "ML Architect / Safety Engineer / QA"
approver: "SW Lead"
scope: "학습 완료 모델 → 독립 테스트셋 평가 → ODD(Operational Design Domain) 커버리지 → 배포 판정"
scope_type: project
scope_code: ASPICE
domain: ASPICE
parent_pro: "[[PRO-ASPICE-01-04_머신러닝공학프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-04-04-01_모델테스트보고서]]"]
aspice_processes: ["MLE.4"]
entry_gate: "WI-ASPICE-01-04-03.status == done"
standards: ["Automotive SPICE 4.0"]
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, MLE.4, ModelTest, ODD, ADAS, AI]
---

# WI-ASPICE-01-04-04 — 모델 테스트 (MLE.4)

## 1. 업무 목적
학습 완료 모델을 독립 테스트셋과 ODD(Operational Design Domain) 시나리오 전반에 걸쳐 평가하여 양산 배포 가능 여부를 판정한다. ASPICE 4.0 MLE.4 활동을 수행하며 ISO 21448 SOTIF 안전 케이스 입력을 제공한다.

## 2. 수행 주체
- **주 수행자**: ML Test Engineer
- **검토자**: ML Architect / Safety Engineer / QA
- **승인자**: SW Lead

## 3. 범위
- 대상: MLE.3 산출 학습 가중치(CM 등록본)
- 평가: 독립 테스트셋 + ODD 시나리오 + 타겟 HW 추론 시험
- 제외: 차량 통합 시험은 SYS.4·VAL 단계 적용

## 4. 입력 자료 / 산출물
**입력 자료**
- 학습 가중치 (CM 등록본)
- 독립 테스트셋(학습·검증과 분리)
- ODD 정의서 + 시나리오 카탈로그
- ML-RS / ML-AD / 안전 요구
- 타겟 HW (NXP S32G274A 등) 보드

**산출물**
- 모델 테스트 보고서(TMP-ASPICE-01-04-04-01)
- 결함 등록(SUP.9 연계)
- 안전 케이스 갱신 입력
- 배포 판정서

## 5. 수행 절차

### 5.1 사전 준비
1. 학습/검증 데이터와 독립적인 테스트셋 확인 및 정합성 검증.
2. ODD 시나리오 카탈로그(날씨·조도·도로·교통) 확정.
3. 타겟 HW 추론 환경(드라이버·런타임 버전) 점검.
4. 합격 기준(KPI) 사전 합의 및 문서화.

### 5.2 수행 단계
1. **독립 테스트셋 평가** (MLE.4 BP1) — 정확도·정밀도·재현율·mAP 측정 후 합격 기준 대비 판정.
2. **ODD 커버리지 평가** (MLE.4 BP2) — 시나리오별 성능을 측정하고 미커버 영역을 식별한다.
3. **타겟 HW 추론 시험** (MLE.4 BP3) — 레이턴시·메모리·전력·온도 한도 내 동작 확인.
4. **안전 요구 충족 검증** (MLE.4 BP4) — 안전 모니터·폴백 동작이 시나리오별로 정상 트리거되는지 확인.
5. **결함 등록** — 합격 기준 미달 또는 안전 위반은 SUP.9 결함관리에 등록.
6. **종합 판정** — Pass / Conditional Pass / Fail 판정 후 배포 결정 입력 제출.
7. **보고서 작성·승인** — 검토자 회람 후 SW Lead 결재.

### 5.3 완료 조건 체크리스트
- [ ] 독립 테스트셋의 학습/검증 분리가 입증되었다.
- [ ] 모든 KPI 가 측정되고 합격 기준 대비 판정되었다.
- [ ] ODD 시나리오 커버리지가 표로 정리되었다.
- [ ] 타겟 HW 추론 시험 결과(레이턴시/메모리)가 기록되었다.
- [ ] 안전 모니터·폴백 동작이 검증되었다.
- [ ] 결함이 SUP.9 에 등록되고 처리 계획이 수립되었다.
- [ ] 보고서가 결재 완료되었다.
- [ ] [[MAT-001_문서관리대장]] 갱신 완료.

## 6. 인터페이스 부서
- 기능안전팀: 안전 케이스 갱신·SOTIF 평가
- 시스템 엔지니어링: ODD·차량 시나리오 일관성
- HW팀: 타겟 보드 가용성·계측 협업
- CM: 테스트 결과 베이스라인 관리
- QA: 독립성·재현성 감사

## 7. 주의사항 / 예외 처리

### 7.1 데이터 누설(Train/Test Leakage)
독립 테스트셋이 학습/검증 데이터와 hash·메타 중복이 발견되면 즉시 시험을 중단하고 데이터팀에 분리 재구성을 요청한다.

### 7.2 KPI 미달
KPI 미달 시 원인 분석 후 ML-AD/ML-RS 변경 또는 추가 학습으로 회귀한다. 안전 KPI(FPR 등)는 미달 시 배포 불가.

### 7.3 타겟 HW 자원 초과
레이턴시/메모리 한도 초과 시 모델 경량화·HW 변경·요구 완화 중 1택 결정 후 ML-AD 변경 절차로 회귀한다.

### 7.4 ODD 외 시나리오 검출
시험 중 ODD 정의 밖이지만 안전 영향이 큰 시나리오가 식별되면 ODD 확장 또는 잔여 리스크로 안전 케이스에 명시한다.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-04-04-01_모델테스트보고서]]
- 작성예시: [[EX-ASPICE-01-04-04-01_모델테스트보고서_작성예시]]
- 상위 절차: [[PRO-ASPICE-01-04_머신러닝공학프로세스]]
- 결함관리: SUP.9 결함관리 프로세스
- 추적성: [[MAT-007_요구사항추적매트릭스]]

## 9. 출처
```yaml
source_citation:
  - file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    section: "MLE.4 / ASPICE 4.0"
    accessed: "2026-05-06"
standards:
  - "Automotive SPICE 4.0 — MLE.4 Machine Learning Testing"
  - "ISO 21448:2022 — SOTIF"
```

## 10. 개정 이력
| 버전 | 일자 | 변경 내용 | 승인자 |
|------|------|-----------|--------|
| 0.1 | 2026-05-06 | 최초 작성 (Draft) | SW Lead |
