---
type: WI
doc_id: "WI-ASPICE-01-10-04"
title: "데이터 버전 및 베이스라인 (SUP.11)"
version: "0.1"
owner: "Data Engineer"
reviewer: "ML Engineer / CM Engineer"
approver: "Data Manager"
scope: "품질 승인 데이터 → DVC/Git LFS 버전 등록 → 베이스라인 태그 → 모델 학습 입력 고정 → 재현성 보장"
parent_pro: "[[PRO-ASPICE-01-10_ML데이터관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-10-04-01_데이터베이스라인등록서]]"]
related_rec: []
aspice_processes: ["SUP.11"]
entry_gate: "WI-ASPICE-01-10-03.status == done"
scope_type: "common"
standards: ["Automotive SPICE 4.0"]
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SUP.11, MLData, DataVersioning, Baseline, DVC]
---

# 데이터 버전 및 베이스라인 (WI-ASPICE-01-10-04)

> 상위 절차: [[PRO-ASPICE-01-10_ML데이터관리프로세스]]
> ASPICE 4.0 SUP.11.BP4 — 데이터 버전·베이스라인 등록·재현성 확보

## 1. 업무 목적

본 지침은 [[WI-ASPICE-01-10-03_데이터품질평가]] 를 통과한 데이터셋을 **DVC(Data Version Control) 와 Git LFS 로 버전 관리**하고, 학습용 베이스라인 태그를 등록하여, ML 모델 학습 입력의 동결과 재현성을 보장하는 데 목적이 있다. [[PRO-ASPICE-01-04_머신러닝공학프로세스]] 의 학습 단계 입력 인계 직전 단계로서, 모든 학습 실험은 본 베이스라인을 입력으로 사용해야 한다.

## 2. 수행 주체

| 역할 | 담당 |
|---|---|
| 주수행자 | Data Engineer |
| 검토자 | ML Engineer / CM Engineer |
| 승인자 | Data Manager |

## 3. 범위

품질 평가를 통과한 모든 학습·검증·테스트 데이터셋의 버전 관리·베이스라인 등록에 적용한다. 임시 실험용 데이터(EDA 단계, 일회성 시각화) 는 본 절차 대상이 아니나, 정식 학습에 사용되는 시점부터는 본 지침을 적용한다.

## 4. 입력 자료 / 산출물

- **Input**:
  - [[WI-ASPICE-01-10-03_데이터품질평가]] 승인 데이터셋
  - 데이터셋 분할 정의(Train/Val/Test 비율, split seed)
  - 전처리 파이프라인 코드·버전
  - DVC 저장소 설정 + 원격 저장소(S3/GCS) 접속 정보
- **Output**:
  - [[TMP-ASPICE-01-10-04-01_데이터베이스라인등록서]] 작성 산출물
  - DVC 베이스라인 태그(예: `ds-adas-v1.0`)
  - 분할별 SHA-256 해시
  - 학습 실험 ID(MLE 연계)

## 4-bis. 인계 대상

- [[PRO-ASPICE-01-04_머신러닝공학프로세스]] 학습 단계 (MLE.3 학습 인계)
- [[PRO-ASPICE-01-08_형상관리프로세스]] (SUP.8) — 베이스라인 형상 등록 연계

## 5. 수행 절차

### 5.1 사전 준비

1. DVC 저장소 초기화 상태와 원격 저장소(S3 버킷 또는 GCS 버킷) 권한을 확인한다.
2. 데이터셋의 Train/Val/Test 분할 비율과 split seed 를 ML Engineer 와 합의·기록한다.
3. 전처리 파이프라인 코드의 Git 커밋 해시를 확보한다.
4. 베이스라인 명명 규칙(`ds-{도메인}-v{Major}.{Minor}-BL`)을 확인한다.
5. CM Engineer 와 형상관리 베이스라인 등록 일정을 협의한다.

### 5.2 수행 단계 (ASPICE SUP.11.BP4 참조)

1. **데이터 분할 실행** — 정의된 비율과 seed 로 Train/Val/Test 를 분할하고, 분할 매니페스트(파일 목록 + 해시)를 생성한다.
2. **분할별 SHA-256 해시 계산** — 각 분할(Train/Val/Test) 의 통합 해시를 계산하여 변경 감지 기준으로 사용한다.
3. **DVC add 및 push** — `dvc add` 로 데이터셋을 DVC 추적에 등록하고, 원격 저장소(S3/GCS) 로 `dvc push` 한다.
4. **DVC 태그 생성** — `dvc tag` 또는 Git tag 로 베이스라인 태그(예: `ds-adas-v1.0`)를 생성한다.
5. **메타데이터 기록** — 데이터 출처(소스 데이터셋 ID), 전처리 파이프라인 버전(Git 커밋 해시), 분할 seed, 환경 정보(Python·라이브러리 버전)를 메타 파일로 기록한다.
6. **베이스라인 잠금(Lock)** — 학습 진행 중 베이스라인 변경을 차단하기 위해 DVC 저장소에 readonly 정책을 적용하거나 별도 잠금 마커 파일을 생성한다.
7. **학습 실험 ID 연결** — 베이스라인을 사용하는 학습 실험(Experiment ID, 예: ML-EXP-042) 과의 연계를 등록한다.
8. **CM 형상관리 등록** — [[PRO-ASPICE-01-08_형상관리프로세스]] 에 본 베이스라인을 등록하여 SW 빌드 산출물과 동일 수준의 형상 통제를 받도록 한다.
9. **인계 통보** — 등록 완료 사실과 베이스라인 ID 를 ML Engineering 팀에 전달하여 학습 단계 진입을 승인한다.

### 5.3 완료 조건 체크리스트

- [ ] Train/Val/Test 분할이 정의된 비율·seed 로 실행되었다.
- [ ] 분할별 SHA-256 해시가 계산되어 등록서에 기록되었다.
- [ ] `dvc push` 로 원격 저장소에 데이터가 업로드되었다.
- [ ] 베이스라인 태그(`ds-{도메인}-v{Major}.{Minor}-BL`)가 생성되었다.
- [ ] 메타데이터(출처·파이프라인 버전·환경 정보)가 기록되었다.
- [ ] 베이스라인 잠금 처리(readonly 또는 lock 마커)가 적용되었다.
- [ ] 연계 학습 실험 ID 가 등록되었다.
- [ ] [[PRO-ASPICE-01-08_형상관리프로세스]] 형상관리 등록이 완료되었다.
- [ ] Data Manager 승인 결재가 완료되었다.
- [ ] [[TMP-ASPICE-01-10-04-01_데이터베이스라인등록서]] 가 결재 완료되어 `08_REC_기록/` 에 보관되었다.
- [ ] [[MAT-001_문서관리대장]] 에 본 산출물이 등록되었다.

## 6. 인터페이스 부서

| 부서 | 인터페이스 내용 |
|---|---|
| ML Engineering | 학습 실험 ID 연계, 베이스라인 인계 |
| CM Engineering | 형상관리 베이스라인 동시 등록 |
| Infrastructure | DVC 원격 저장소(S3/GCS) 권한·용량 관리 |
| QA (SUP.1) | 등록 절차·재현성 감사 |
| Data Engineering | 후속 데이터셋 갱신 시 신규 베이스라인 등록 |

## 7. 주의사항 / 예외 처리

1. **베이스라인 잠금 위반 시도** — 학습 진행 중 데이터셋 수정 PR 이 발생하면 자동 차단(CI 가드) 하고, 긴급 수정이 필요하면 신규 베이스라인(v1.0 → v1.1)으로 분리 등록한다.
2. **원격 저장소 push 실패** — 네트워크·용량 문제로 push 가 실패하면 학습 실험 진입을 보류하고 Infrastructure 팀과 즉시 협력한다. 부분 push 상태로 학습 진입 금지.
3. **DVC 태그 충돌** — 동일 베이스라인 ID 가 이미 존재하면 자동 거부. 강제 덮어쓰기는 금지하고 Minor 버전 증분(v1.0 → v1.0.1)으로 신규 등록.
4. **데이터셋 사후 추가/삭제 발견** — 등록 후 누락 또는 추가 샘플이 발견되면 신규 베이스라인을 발행하고, 기존 베이스라인을 사용한 학습 실험은 [[PRO-ASPICE-01-04_머신러닝공학프로세스]] 에서 재학습 여부를 결정한다.

## 8. 연계 템플릿 / 기록

- 템플릿: [[TMP-ASPICE-01-10-04-01_데이터베이스라인등록서]]
- 작성예시: [[EX-ASPICE-01-10-04-01_데이터베이스라인등록서_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. 출처 (source_citation)

```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SUP.11-BP4"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력

| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SUP.11.BP4 데이터 버전·베이스라인 정의 | (대기) |
