---
doc_id: "EX-ASPICE-01-04-02-01"
title: "ML 아키텍처 기술서 작성예시"
type: EX
version: "0.1"
status: draft
parent_tmp: "[[TMP-ASPICE-01-04-02-01_ML아키텍처기술서]]"
scope_type: project
scope_code: ASPICE
domain: ASPICE
created: "2026-05-06"
updated: "2026-05-06"
tags: [EX, sample, ASPICE, MLE.2, MLArchitecture]
---

# ML 아키텍처 기술서 (작성예시)

> 본 문서는 작성예시입니다. 가공의 회사·프로젝트 정보를 사용합니다.

## 작성 정보
| 항목 | 내용 |
|------|------|
| 프로젝트명 | ABC Motors Co., Ltd. — ADAS Domain Controller 개발 |
| ML 컴포넌트명 | ADAS-DCU-V2 / Object Detection (Front Camera) |
| 문서 번호 | ABC-ADAS-2026-001-ML-AD-001 |
| 작성자 | 박ML (ML Engineer) |
| 검토자 | 이아키 (ML Architect), 최안전 (Safety), 정품질 (QA) |
| 승인자 | 김SW (SW Lead) |
| 작성일자 | 2026-05-06 |

## 1. ML 요구사항(ML-RS) 참조
| ML-RS-ID | 요구사항 요약 | ASIL | 참조 문서/버전 |
|----------|---------------|------|----------------|
| ML-RS-001 | 차량/보행자/신호등 검출 mAP@50 ≥ 0.85 | B(D) | ML-RS-ADAS-DCU-V2-v1.0 |
| ML-RS-002 | 추론 레이턴시 ≤ 50ms (NXP S32G274A) | B(D) | ML-RS-ADAS-DCU-V2-v1.0 |
| ML-RS-003 | False Positive Rate ≤ 0.005 | B(D) | ML-RS-ADAS-DCU-V2-v1.0 |

## 2. 모델 유형 및 알고리즘 선정
| 후보 모델 | 과업 적합성 | 정확도 (벤치) | 레이턴시 | 메모리 | 채택 여부 | 사유 |
|-----------|-------------|---------------|----------|--------|-----------|------|
| YOLOv8-m | 검출 우수 | mAP@50 0.89 | 42ms | 320MB | **채택** | 정확도·속도 균형 |
| YOLOv5-s | 경량 | mAP@50 0.81 | 28ms | 180MB | 비채택 | 정확도 미달 |
| DETR-R50 | 검출 우수 | mAP@50 0.88 | 95ms | 720MB | 비채택 | 레이턴시 초과 |

## 3. 입출력 인터페이스 정의
| 인터페이스 | 사양 |
|------------|------|
| 입력 텐서(shape/dtype) | (1, 3, 640, 640) FP16 |
| 입력 전처리 | YUV→RGB 변환, 0~1 정규화, 리사이즈(LetterBox) |
| 출력 포맷 | List[BBox(x1,y1,x2,y2,score,class_id)] |
| 출력 후처리 | NMS(IoU=0.5), score≥0.4 필터 |
| 시간 제약 (ms) | ≤ 50 (end-to-end) |

## 4. 데이터 파이프라인 구조
| 단계 | 책임자 | 도구 | 산출물 |
|------|--------|------|--------|
| 수집 | 데이터팀 | 차량 로깅 시스템(8대) | raw mp4 + GPS |
| 라벨링 | 외주(LabelCo) | CVAT | COCO format json |
| 증강 | ML팀 | Albumentations | augmented npz |
| 전처리 | ML팀 | PyTorch Dataset | tensor cache |
| 배포(베이스라인) | CM팀 | DVC + S3 | dataset-v1.2 tag |

## 5. 추론 엔진 및 HW 타겟
| 항목 | 내용 |
|------|------|
| 학습 프레임워크 | PyTorch 2.1 |
| 추론 런타임 | TensorRT 8.6 (FP16) |
| 모델 변환 경로 | PyTorch → ONNX 1.15 → TensorRT engine |
| 타겟 HW (SoC/가속기) | NXP S32G274A + dedicated NPU 4 TOPS |
| 양자화·최적화 | FP16 양자화, 레이어 퓨전, 동적 배치 비활성 |

## 6. 안전 제약 (ASIL 상속)
| 안전 메커니즘 | 설명 | 담당 컴포넌트 |
|---------------|------|----------------|
| 입력 유효성 검사 | 카메라 신호 손실/포화 검출 | ImageQualityMonitor |
| 출력 신뢰도 모니터 | score 분포 이상 탐지 | InferenceMonitor |
| 폴백 전략 | 신뢰도 저하 시 ADAS 기능 점진적 다운그레이드 | SafetyController(ASIL D) |
| 이중화/투표 | 카메라 + 레이더 센서 퓨전 | SensorFusion(ASIL D) |
| Safety Cage | 비물리적 BBox 출력 거부 | OutputValidator |

## 7. Bias·공정성 고려
| 위험 시나리오 | 발생 가능성 | 영향 | 완화 방안 |
|---------------|--------------|------|------------|
| 야간 검출률 저하 | 중 | 보행자 미검출 | 야간 데이터 30% 비중 증강 + IR 카메라 보강 |
| 우천 시 레이턴시 증가 | 중 | 반응 지연 | 우천 데이터 15% 추가, 도메인 적응 학습 |
| 어린이/휠체어 검출 편차 | 저 | 취약 보행자 미검출 | 클래스 균형 재가중, 합성 데이터 보강 |

## 8. 추적성 (ML-RS ↔ 아키텍처)
| ML-RS-ID | ML-AD 항목 | 검증 방법 |
|----------|-------------|------------|
| ML-RS-001 | §2 모델 선정 (YOLOv8-m) | MLE.4 모델 테스트 (mAP) |
| ML-RS-002 | §5 추론 환경 (TRT FP16) | MLE.4 타겟 HW 레이턴시 측정 |
| ML-RS-003 | §6 출력 신뢰도 모니터 | MLE.4 FPR 측정 + Safety Case 검토 |

## 9. 승인
| 역할 | 성명 | 서명 | 일자 |
|------|------|------|------|
| 작성자 | 박ML | (서명) | 2026-05-06 |
| 검토자(ML Architect) | 이아키 | (서명) | 2026-05-06 |
| 검토자(Safety) | 최안전 | (서명) | 2026-05-06 |
| 검토자(QA) | 정품질 | (서명) | 2026-05-06 |
| 승인자(SW Lead) | 김SW | (서명) | 2026-05-06 |

## 작성 요령
- 모델 후보는 최소 3개를 객관적 벤치마크로 비교한다.
- ASIL 분해(B(D))는 안전 분석 보고서를 명시 인용한다.
- Bias 시나리오는 실제 ODD 와 일치시켜야 한다.

## 잘못된 사례
- "PyTorch 사용" 만 적고 추론 런타임·변환 경로 누락 → 양산 통합 단계에서 차질.
- 안전 메커니즘을 "필요시 검토" 로 회피 → ASIL 매핑 부적합 판정.
- 데이터 편향을 "없음" 으로 기재 → SOTIF 평가 거부.
