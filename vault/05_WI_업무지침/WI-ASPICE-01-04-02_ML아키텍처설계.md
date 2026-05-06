---
doc_id: "WI-ASPICE-01-04-02"
title: "ML 아키텍처 설계 (MLE.2)"
type: WI
version: "0.1"
status: draft
owner: "ML Engineer"
reviewer: "ML Architect / Safety Engineer / QA"
approver: "SW Lead"
scope: "ML 요구사항(ML-RS) 기반 → 아키텍처·프레임워크·데이터 파이프라인 설계 → ML-AD 발행"
scope_type: project
scope_code: ASPICE
domain: ASPICE
parent_pro: "[[PRO-ASPICE-01-04_머신러닝공학프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-04-02-01_ML아키텍처기술서]]"]
aspice_processes: ["MLE.2"]
entry_gate: "WI-ASPICE-01-04-01.status == done"
standards: ["Automotive SPICE 4.0"]
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, MLE.2, MLArchitecture, ADAS, AI]
---

# WI-ASPICE-01-04-02 — ML 아키텍처 설계 (MLE.2)

## 1. 업무 목적
승인된 ML 요구사항(ML-RS)을 기반으로 ML 모델 아키텍처·프레임워크·데이터 파이프라인·추론 환경을 설계하고, ML 아키텍처 기술서(ML-AD)를 발행하여 후속 학습(MLE.3) 단계의 입력으로 제공한다. ASPICE 4.0 MLE.2 활동을 수행한다.

## 2. 수행 주체
- **주 수행자**: ML Engineer
- **검토자**: ML Architect / Safety Engineer / QA
- **승인자**: SW Lead

## 3. 범위
- 대상: ADAS·자율주행 ML 컴포넌트(인지·예측·제어 보조)
- 적용 기술: 학습 프레임워크(PyTorch/TensorFlow), 추론 런타임(TensorRT/ONNX-RT), HW 가속기
- 제외: 모델 학습·평가 자체는 후속 WI 적용
- 적용 표준: Automotive SPICE 4.0 MLE.2, ISO 21448 (SOTIF) 관련 사항

## 4. 입력 자료 / 산출물
**입력 자료**
- ML 요구사항 명세서(ML-RS) — WI-ASPICE-01-04-01 산출물
- 시스템 아키텍처(SyAD) 중 AI 컴포넌트 인터페이스
- HW 타겟 사양(연산성능·메모리·전력)
- ASIL 분류 결과(안전 제약)
- 데이터셋 가용성 정보

**산출물**
- ML 아키텍처 기술서(TMP-ASPICE-01-04-02-01)
- 추론 파이프라인 다이어그램(C4·UML)
- ASIL-AI 안전 제약 매핑표
- 데이터셋 요구 명세

## 5. 수행 절차

### 5.1 사전 준비
1. ML-RS 베이스라인 확정 및 변경 동결.
2. 타겟 HW 의 추론 성능 벤치마크 자료 확보.
3. 후보 프레임워크·런타임 라이선스·자동차 등급 인증 여부 확인.
4. 안전 등급(ASIL) 별 격리(partitioning) 방침 합의.

### 5.2 수행 단계
1. **모델 유형 선정** (MLE.2 BP1) — 과업(분류/검출/세그멘테이션)에 적합한 모델 패밀리(YOLO·DETR·UNet 등)를 후보 비교 후 선정한다.
2. **프레임워크·런타임 결정** (MLE.2 BP2) — 학습(PyTorch 등)과 추론(TensorRT/ONNX-RT)을 분리 결정하고 변환 경로를 명세한다.
3. **데이터 파이프라인 설계** (MLE.2 BP3) — 수집·라벨링·증강·전처리·배포 단계 및 책임자를 명세한다.
4. **인터페이스 정의** (MLE.2 BP4) — 입력 텐서 사양(해상도/포맷)·출력 사양(BBox/score 형식)·시간 제약을 정의한다.
5. **안전 제약 상속** (MLE.2 BP5) — 상위 ASIL 등급을 ML 컴포넌트에 매핑하고 모니터(Safety Cage)·폴백 전략을 정의한다.
6. **공정성·편향 분석** (MLE.2 BP6) — 데이터 분포 편향 가능성과 완화 방안(증강·재가중)을 명세한다.
7. **추적성 구축** — ML-RS ↔ ML-AD 양방향 추적성 확보.
8. **검토 및 승인** — 검토자 회람 후 SW Lead 결재.

### 5.3 완료 조건 체크리스트
- [ ] ML-RS 모든 항목이 ML-AD 에 매핑되었다.
- [ ] 학습·추론 프레임워크와 변환 경로가 명세되었다.
- [ ] 데이터 파이프라인이 단계별로 정의되었다.
- [ ] ASIL 안전 제약과 폴백 전략이 매핑되었다.
- [ ] 공정성·편향 완화 방안이 기록되었다.
- [ ] 양방향 추적성이 확보되었다.
- [ ] 검토자·승인자 결재가 완료되었다.
- [ ] [[MAT-001_문서관리대장]] 갱신 완료.

## 6. 인터페이스 부서
- 시스템 엔지니어링: 상위 아키텍처와 인터페이스 일관성
- 기능안전팀: ASIL 매핑 및 안전 케이스 검토
- 데이터팀: 데이터셋 가용성·라벨링 품질 협의
- HW팀: 타겟 HW 추론 성능·전력 검증 협업
- QA: 설계 검토 독립성 확보

## 7. 주의사항 / 예외 처리

### 7.1 타겟 HW 성능 미달
선정 모델이 타겟 HW 의 레이턴시·메모리 한도를 초과하면 모델 경량화(양자화·프루닝)·HW 업그레이드·요구사항 완화 중 하나로 대안 결정 후 ML-RS 변경 절차를 거친다.

### 7.2 데이터 편향 위험 식별
특정 시나리오(야간·악천후·소수 인구 집단)에서 데이터 편중이 확인되면 추가 수집 계획을 수립하고 안전 케이스에 잔여 리스크로 명시한다.

### 7.3 프레임워크 라이선스 충돌
오픈소스 라이선스(GPL 등)가 양산 코드 통합에 제약을 주는 경우 법무 검토 후 대체 프레임워크로 전환한다.

### 7.4 ASIL D 매핑 회피
ML 모델은 본질적 비결정성으로 ASIL D 직접 할당이 어려우므로 안전 모니터·이중화로 ASIL D 시스템 안에서 ASIL B(D) 분해를 적용한다.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-04-02-01_ML아키텍처기술서]]
- 작성예시: [[EX-ASPICE-01-04-02-01_ML아키텍처기술서_작성예시]]
- 상위 절차: [[PRO-ASPICE-01-04_머신러닝공학프로세스]]
- 추적성: [[MAT-007_요구사항추적매트릭스]]

## 9. 출처
```yaml
source_citation:
  - file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    section: "MLE.2 / ASPICE 4.0"
    accessed: "2026-05-06"
standards:
  - "Automotive SPICE 4.0 — MLE.2 Machine Learning Architecture"
  - "ISO 21448:2022 — SOTIF"
```

## 10. 개정 이력
| 버전 | 일자 | 변경 내용 | 승인자 |
|------|------|-----------|--------|
| 0.1 | 2026-05-06 | 최초 작성 (Draft) | SW Lead |
