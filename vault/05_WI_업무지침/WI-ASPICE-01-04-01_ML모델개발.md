---
type: WI
doc_id: "WI-ASPICE-01-04-01"
title: "ML 모델 개발 통합 (MLE.1~MLE.4)"
version: "0.1"
owner: "ML Engineer"
reviewer: "ML Architect / Safety Engineer / Data Engineering Lead"
approver: "ML Lead"
scope: "ML 요구사항 → 아키텍처 → 학습 → 모델 테스트 통합 절차"
parent_pro: "[[PRO-ASPICE-01-04_머신러닝공학프로세스]]"
related_tmp: []
related_rec: []
standards: ["Automotive SPICE 4.0", "ISO 26262", "ISO/IEC 5259", "ISO/IEC 23894"]
aspice_processes: ["MLE.1", "MLE.2", "MLE.3", "MLE.4"]
entry_gate: null
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, MLE, ADAS, AI, MLOps]
---

# ML 모델 개발 통합 업무지침 (WI-ASPICE-01-04-01)

> 상위 절차: [[PRO-ASPICE-01-04_머신러닝공학프로세스]]
> ASPICE 매핑: MLE.1~MLE.4 (ML Requirements / Architecture / Training / Testing)

## 1. 업무 목적

ADAS·자율주행에 적용되는 ML 모델의 요구사항 분석부터 아키텍처·학습·테스트까지 일관된 절차로 수행하여, 데이터 의존성·모델 신뢰성을 검증한다.

## 2. 수행 주체
- **주 수행자**: ML Engineer
- **검토자**: ML Architect, Safety Engineer (ASIL ML 분배), Data Lead
- **승인자**: ML Lead

## 3. 범위
SAD 의 ML 분배분 인계 + [[PRO-ASPICE-01-10_ML데이터관리]] 의 데이터 베이스라인 준비 완료 후부터 모델 v1.0 인계까지 적용한다.

## 4. 입력 자료 / 산출물
- **Input**: SyRS (ML 분배분), ML 학습 데이터셋 (베이스라인), HW 추론 환경 사양
- **Output**: ML Requirements Spec, ML Architecture, Trained Model (with Hash), Model Test Report

## 5. 수행 절차

### 5.1 사전 준비
1. 학습 환경(GPU 클러스터, 라이선스) + MLOps 도구(MLflow, DVC) 점검.
2. 데이터 버전 v{n} CM 등록 확인 (PRO-10).
3. 모델 ID 체계(`MDL-{프로젝트코드}-{NNN}`) 정의.

### 5.2 수행 단계

1. **ML 요구사항 분석** (MLE.1)
   - 기능: 입력(센서 데이터) · 출력(클래스/Bbox/세그먼트) · 정확도 목표(mAP, Recall).
   - 비기능: 추론 시간(ms), 메모리(MB), 전력(W).
   - 안전성: ASIL 상속 + 안전 마진(예: False Negative 한계).

2. **ML 아키텍처 설계** (MLE.2)
   - 모델 구조(Backbone + Head), 입력 전처리·후처리.
   - 추론 환경 적합성(양자화·Pruning·TensorRT 등).

3. **모델 학습** (MLE.3)
   - 데이터 분할(Train/Val/Test) — 누수(leakage) 방지.
   - 하이퍼파라미터·실험 추적 (MLflow).
   - 학습 결과(가중치) Hash + 데이터 버전 + 환경 메타 보존 (재현성).

4. **모델 테스트** (MLE.4)
   - Val/Test set 성능 측정.
   - Edge Case 시험 (조도·날씨·OOD).
   - Fairness/Bias 검증 (필요 시).
   - Adversarial Robustness 시험 (보안 관련 시).

5. **결과 인계**
   - 모델 + 메타 + 테스트 보고서 → SYS.4 통합 인계.

### 5.3 완료 조건 체크리스트
- [ ] ML 요구사항에 정확도·추론시간·ASIL 명시
- [ ] 데이터셋 베이스라인 v{n} 명시 + Hash 일치
- [ ] 학습 재현 가능 (시드·환경·코드 commit hash 보존)
- [ ] Val/Test 성능 목표 달성 또는 사유 기록
- [ ] Edge Case 시험 결과 첨부
- [ ] 모델 가중치 Hash + 메타 보존
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **Data Engineering ([[PRO-ASPICE-01-10]])**: 데이터셋 인계
- **HW Lead**: 추론 환경 합의
- **System/SW Engineering**: 통합 인계
- **Safety Engineering**: ASIL ML 검토

## 7. 주의사항 / 예외 처리

### 7.1 데이터 누수 (Leakage)
- Train/Val/Test 분할에서 동일 차량·동일 시나리오 혼입 발견 시:
  - 즉시 학습 결과 무효 처리 + 데이터 재분할.
  - 책임 분석 및 RCA → 데이터 관리 프로세스 개선.

### 7.2 재현성 결여
- 동일 시드·환경·데이터로 학습 재현 불가:
  - 환경 차이 분석 (CUDA/Driver/Library 버전).
  - 비결정적 연산(예: cuDNN benchmark) 비활성화.
  - 재현성 보장 후 정식 학습 재실행.

### 7.3 Edge Case 성능 미달
- 특정 시나리오(악천후·역광) 에서 정확도 급락:
  - 데이터 보강(추가 수집 또는 합성) 요청.
  - 모델 구조 변경 또는 앙상블 검토.
  - 미해결 시 ODD (Operational Design Domain) 명시적 제한.

### 7.4 OEM 데이터 정책 위반
- OEM 가 학습 데이터의 외부 사용·재배포 제한:
  - 데이터 격리 환경(VWAY 사내 GPU, 외부 API 금지) 강제.
  - 위반 시 즉시 학습 중단 + 법무 보고.

## 8. 연계 템플릿 / 기록
- 기록 폴더: `vault/08_REC_기록/MLE/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-MLE.1-* / VWAY-MLE.2-* / VWAY-MLE.3-* / VWAY-MLE.4-*"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — MLE.1~4 통합 + MLOps 재현성 | (대기) |
