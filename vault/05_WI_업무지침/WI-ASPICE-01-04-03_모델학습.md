---
doc_id: "WI-ASPICE-01-04-03"
title: "모델 학습 (MLE.3)"
type: WI
version: "0.1"
status: draft
owner: "ML Engineer"
reviewer: "ML Architect / Data Engineer / QA"
approver: "SW Lead"
scope: "승인된 데이터셋 → 모델 학습·하이퍼파라미터 튜닝 → 재현성 확보 → 학습 완료 모델 CM 등록"
scope_type: project
scope_code: ASPICE
domain: ASPICE
parent_pro: "[[PRO-ASPICE-01-04_머신러닝공학프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-04-03-01_모델학습결과보고서]]"]
aspice_processes: ["MLE.3"]
entry_gate: "WI-ASPICE-01-04-02.status == done AND PRO-ASPICE-01-10.dataset_baseline == ready"
standards: ["Automotive SPICE 4.0"]
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, MLE.3, ModelTraining, ADAS, AI]
---

# WI-ASPICE-01-04-03 — 모델 학습 (MLE.3)

## 1. 업무 목적
승인된 ML 아키텍처(ML-AD)와 데이터셋 베이스라인을 기반으로 모델을 학습·튜닝하여 후속 테스트(MLE.4)에 투입할 학습 완료 모델(가중치)을 산출한다. 재현성·실험 추적·CM 등록을 통해 ASPICE 4.0 MLE.3 활동을 충족한다.

## 2. 수행 주체
- **주 수행자**: ML Engineer
- **검토자**: ML Architect / Data Engineer / QA
- **승인자**: SW Lead

## 3. 범위
- 대상: ML-AD 에 명세된 모델 가중치 학습 활동 전체
- 포함: 데이터 분할, 학습 실행, 하이퍼파라미터 튜닝, 가중치 CM 등록
- 제외: 독립 테스트셋 평가(MLE.4) 는 별도 WI

## 4. 입력 자료 / 산출물
**입력 자료**
- ML 아키텍처 기술서(ML-AD)
- 데이터셋 베이스라인(DVC tag, 라벨 검증 완료)
- HW/GPU 자원 가용성
- 학습 실행 계획(epoch·batch·lr 초기값)

**산출물**
- 모델 학습 결과 보고서(TMP-ASPICE-01-04-03-01)
- 학습 가중치 파일(.pt/.onnx) — CM 등록
- 학습 로그·MLflow run id
- Docker 이미지 / requirements.lock

## 5. 수행 절차

### 5.1 사전 준비
1. 데이터셋 베이스라인 hash 와 DVC tag 일치 확인.
2. GPU 자원·사용 일정 예약(예: A100 x4, 72시간).
3. MLflow tracking 서버·아티팩트 저장소 가용성 확인.
4. 학습 환경 Docker 이미지·random seed·CUDA 버전 고정.

### 5.2 수행 단계
1. **데이터 분할** (MLE.3 BP1) — train/val/test 비율을 ML-AD 에 따라 결정하고 stratified split 수행.
2. **베이스라인 학습** (MLE.3 BP2) — 초기 하이퍼파라미터로 학습을 실행하고 epoch 별 loss/accuracy 를 MLflow 에 기록한다.
3. **하이퍼파라미터 튜닝** (MLE.3 BP3) — Bayesian/Grid 등 사전 합의된 방식으로 튜닝하고 결과 비교 표를 작성한다.
4. **재현성 검증** — 동일 seed·환경에서 재실행 시 결과가 허용 오차 내인지 확인한다.
5. **과적합·편향 점검** — train/val gap, confusion matrix, slice metric 으로 과적합 여부와 편향을 확인한다.
6. **최종 가중치 선정** — 검증 성능과 안정성 기준으로 가중치 후보 1개를 선정한다.
7. **CM 등록** — 가중치·환경 docker tag·dataset tag 를 묶어 CM 베이스라인으로 등록한다.
8. **결과 보고서 작성·승인** — 검토자 회람 후 SW Lead 결재.

### 5.3 완료 조건 체크리스트
- [ ] 데이터 분할 비율과 결과가 기록되었다.
- [ ] 학습 곡선(epoch loss/accuracy) 가 MLflow 에 보존되었다.
- [ ] 하이퍼파라미터 비교 표가 첨부되었다.
- [ ] seed·docker·CUDA 버전이 고정·기록되었다.
- [ ] 과적합·편향 점검이 완료되었다.
- [ ] 최종 가중치가 CM 등록되었다(태그·hash 명시).
- [ ] 결과 보고서가 결재 완료되었다.
- [ ] [[MAT-001_문서관리대장]] 갱신 완료.

## 6. 인터페이스 부서
- 데이터팀: 데이터셋 베이스라인 발행·라벨 품질 보증
- HW/IT: GPU 자원 운영, MLflow 인프라
- 기능안전팀: 학습 결과의 안전 기준 사전 협의
- CM: 모델·환경 베이스라인 등록
- QA: 재현성·실험 추적 감사

## 7. 주의사항 / 예외 처리

### 7.1 학습 실패 또는 발산
loss 가 발산하거나 NaN 이 발생하면 로그·hyperparameter snapshot 보존 후 lr 조정·gradient clipping 적용으로 재학습한다. 3회 연속 실패 시 ML Architect 에 에스컬레이션.

### 7.2 데이터 라벨 결함 발견
학습 중 라벨 노이즈가 의심되면 학습을 중단하고 데이터팀에 라벨 재검토를 요청한다. 라벨 변경 시 데이터셋 새 베이스라인을 발행하고 학습을 재개한다.

### 7.3 GPU/하드웨어 장애
학습 중단 시 마지막 checkpoint 에서 재개하되, 환경 동등성(동일 GPU 모델·드라이버) 을 확인한다. 이종 GPU 혼용 학습은 금지한다.

### 7.4 라이선스/PII 위반
데이터셋에 PII 또는 라이선스 위반 자료가 포함된 사실이 사후 발견되면 학습을 중단하고 해당 데이터·모델을 격리·삭제한다. 법무·CISO 통보 후 새 베이스라인으로 재학습.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-04-03-01_모델학습결과보고서]]
- 작성예시: [[EX-ASPICE-01-04-03-01_모델학습결과보고서_작성예시]]
- 상위 절차: [[PRO-ASPICE-01-04_머신러닝공학프로세스]]
- 추적성: [[MAT-007_요구사항추적매트릭스]]

## 9. 출처
```yaml
source_citation:
  - file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    section: "MLE.3 / ASPICE 4.0"
    accessed: "2026-05-06"
standards:
  - "Automotive SPICE 4.0 — MLE.3 Machine Learning Training"
```

## 10. 개정 이력
| 버전 | 일자 | 변경 내용 | 승인자 |
|------|------|-----------|--------|
| 0.1 | 2026-05-06 | 최초 작성 (Draft) | SW Lead |
