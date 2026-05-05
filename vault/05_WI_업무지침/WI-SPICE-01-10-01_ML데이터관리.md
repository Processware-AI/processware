---
type: WI
doc_id: "WI-SPICE-01-10-01"
title: "ML 데이터 관리 통합 (SUP.11)"
version: "0.1"
owner: "Data Engineer"
reviewer: "Data Engineering Lead / Privacy Officer / Safety Engineer"
approver: "Data Engineering Lead"
scope: "데이터 수집·라벨링·라이선스·품질·버전·베이스라인 관리"
parent_pro: "[[PRO-SPICE-01-10_데이터및머신러닝지원프로세스]]"
related_tmp: []
related_rec: []
standards: ["Automotive SPICE 4.0", "ISO/IEC 5259", "GDPR", "PIPA"]
aspice_processes: ["SUP.11"]
entry_gate: null
scope_type: "common"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SUP.11, Data, MLOps, Privacy]
---

# ML 데이터 관리 업무지침 (WI-SPICE-01-10-01)

> 상위 절차: [[PRO-SPICE-01-10_데이터및머신러닝지원프로세스]]
> ASPICE 매핑: SUP.11 (Machine Learning Data Management) — BP1~BP6

## 1. 업무 목적

ML 학습·검증 데이터의 수집·라벨링·품질·라이선스·개인정보·버전을 관리하여 PRO-04 ML 모델 개발의 신뢰할 수 있는 입력을 제공하고 재현성을 보장한다.

## 2. 수행 주체
- **주 수행자**: Data Engineer
- **검토자**: Data Lead, Privacy Officer (개인정보), Safety Engineer (Edge Case)
- **승인자**: Data Engineering Lead

## 3. 범위
프로젝트 데이터 요구 식별 시점부터 ML 모델 학습 베이스라인 데이터 v{n} 인계까지 적용한다.

## 4. 입력 자료 / 산출물
- **Input**: 데이터 수집 계획, 차량 센서 로그, 외부 데이터셋
- **Output**: Labeled Dataset v{n}, 라이선스 명세, 개인정보 검토서, 데이터 품질 보고서, Dataset Hash

## 5. 수행 절차

### 5.1 사전 준비
1. 데이터 저장소(Object Storage) + DVC/MLflow 환경 구성.
2. 라벨링 도구(CVAT, LabelStudio) 라이선스 확인.

### 5.2 수행 단계

1. **데이터 수집** (SUP.11.BP1)
   - 차량 센서 로깅 + 외부 데이터셋 다운로드.
   - 수집 메타(시간·장소·차량·날씨) 기록.

2. **라벨링** (SUP.11.BP2)
   - 라벨링 가이드라인 + 검수자 교차 검증.
   - Inter-annotator Agreement (Kappa) ≥ 0.8.

3. **라이선스·개인정보 검증** (SUP.11.BP3)
   - 외부 데이터셋의 라이선스 (상업 사용·재배포) 확인.
   - 영상 내 개인정보(번호판·얼굴) 마스킹 강제.
   - 개인정보 처리 동의서 확보 (수집 시).

4. **데이터 품질 평가** (SUP.11.BP4)
   - 결측·중복·노이즈·클래스 불균형 분석.
   - Edge Case 커버리지 (악천후·역광·OOD).

5. **데이터 버전·베이스라인** (SUP.11.BP5)
   - DVC 로 버전 관리 + Hash 등록.
   - 베이스라인 v{n} → CM 등록.

6. **PRO-04 인계** (SUP.11.BP6)
   - 데이터셋 + 메타 + 라이선스 + 품질 보고서 인계.

### 5.3 완료 조건 체크리스트
- [ ] 모든 데이터 수집 메타(시간·장소·차량·날씨) 보존
- [ ] 라벨링 IAA Kappa ≥ 0.8
- [ ] 외부 데이터셋 라이선스 명세 첨부
- [ ] 개인정보 마스킹 100% 검증
- [ ] 데이터 품질 보고서 (결측·중복·불균형) 작성
- [ ] DVC 버전 + Hash 등록 + CM 베이스라인
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **ML Engineering ([[PRO-SPICE-01-04]])**: 데이터 인계
- **Privacy/Legal**: 개인정보·라이선스 검토
- **Safety**: Edge Case 검토
- **CM (SUP.8)**: 베이스라인

## 7. 주의사항 / 예외 처리

### 7.1 개인정보 노출 (마스킹 누락)
- 데이터셋에서 마스킹 누락 발견:
  - 즉시 데이터셋 사용 중단 + 재마스킹.
  - Privacy Officer 보고 + 위반 사유 분석.

### 7.2 라이선스 위반 의심
- 외부 데이터셋 라이선스 조건 불명:
  - 즉시 사용 중단 + 법무 검토.
  - 합법 대안 데이터로 교체.

### 7.3 클래스 심각 불균형
- 특정 클래스 < 1% 등 학습 곤란:
  - 데이터 보강(추가 수집·합성·증강) 요청.
  - 미해결 시 ML 모델 측 클래스 가중치 조정 협의.

### 7.4 데이터 누수 (Train/Val 중복)
- 동일 차량/시간대 샘플이 Train·Val 중복:
  - 즉시 분할 재실시 + 학습 결과 무효화.
  - 분할 정책 RCA + 자동 검증 도구 도입.

## 8. 연계 템플릿 / 기록
- 기록 폴더: `vault/08_REC_기록/SUP.11/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SUP.11-PURPOSE-001 / VWAY-SUP.11-BP1~BP6"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SUP.11 BP1~BP6 + 개인정보·재현성 | (대기) |
