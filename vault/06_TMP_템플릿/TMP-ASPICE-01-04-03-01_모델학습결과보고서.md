---
doc_id: "TMP-ASPICE-01-04-03-01"
title: "모델 학습 결과 보고서"
type: TMP
version: "0.1"
status: draft
parent_wi: "[[WI-ASPICE-01-04-03_모델학습]]"
related_ex: "[[EX-ASPICE-01-04-03-01_모델학습결과보고서_작성예시]]"
scope_type: project
scope_code: ASPICE
domain: ASPICE
created: "2026-05-06"
updated: "2026-05-06"
tags: [TMP, ASPICE, MLE.3, ModelTraining]
---

> 이 파일은 빈 양식입니다. 예시 값을 기입하지 마세요(예시는 EX 로 분리).

# 모델 학습 결과 보고서

## 작성 정보
| 항목 | 내용 |
|------|------|
| 프로젝트명 | |
| 모델명 / 버전 | |
| 문서 번호 | |
| MLflow run id | |
| 작성자 | |
| 검토자 | |
| 승인자 | |
| 작성일자 | |

## 1. 데이터셋 정보
| 항목 | 내용 |
|------|------|
| 데이터셋 베이스라인 (DVC tag) | |
| Train / Val / Test 비율 | |
| Train 샘플 수 | |
| Val 샘플 수 | |
| Test 샘플 수 | |
| 클래스 분포 | |

## 2. 학습 환경
| 항목 | 내용 |
|------|------|
| GPU 모델·수량 | |
| Framework·버전 | |
| CUDA / cuDNN | |
| Docker 이미지 tag | |
| requirements.lock hash | |

## 3. 하이퍼파라미터
| 파라미터 | 값 | 비고 |
|----------|----|----|
| batch size | | |
| learning rate | | |
| optimizer | | |
| epochs | | |
| weight decay | | |
| augmentation | | |

## 4. 학습 곡선 요약
| epoch | train loss | val loss | train acc | val acc |
|-------|------------|----------|-----------|---------|
| | | | | |

## 5. 검증 결과
| 지표 | 값 | 목표 | 판정 |
|------|----|------|------|
| Precision | | | |
| Recall | | | |
| mAP@50 | | | |
| mAP@50:95 | | | |

## 6. 재현성 정보
| 항목 | 내용 |
|------|------|
| random seed | |
| Docker 이미지 | |
| 재실행 결과 일치 여부 | |
| 허용 오차 | |

## 7. Bias 검출 결과
| Slice | 샘플 수 | 성능 지표 | 평균 대비 차이 | 조치 |
|-------|---------|-----------|----------------|------|
| | | | | |

## 8. CM 등록 정보
| 항목 | 내용 |
|------|------|
| 모델 가중치 파일명 | |
| 파일 hash (SHA-256) | |
| CM 베이스라인 tag | |
| 등록 일자 | |

## 9. 종합 판정 / 승인
| 판정 | 사유 |
|------|------|
| Pass / Conditional Pass / Fail | |

| 역할 | 성명 | 서명 | 일자 |
|------|------|------|------|
| 작성자 | | | |
| 검토자(ML Architect) | | | |
| 검토자(Data Engineer) | | | |
| 검토자(QA) | | | |
| 승인자(SW Lead) | | | |
