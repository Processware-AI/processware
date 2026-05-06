---
type: EX
doc_id: "EX-ASPICE-01-03-04-01"
title: "HW 설계 검증 보고서 작성예시"
version: "0.1"
owner: ""
parent_tmp: "[[TMP-ASPICE-01-03-04-01_HW설계검증보고서]]"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [EX, sample, ASPICE, HWE.3, DesignVerification]
---

# HW 설계 검증 보고서 작성예시 (EX-ASPICE-01-03-04-01)

> 원본 양식: [[TMP-ASPICE-01-03-04-01_HW설계검증보고서]]

> 이 파일은 교육·가이드용 샘플입니다. 실제 기록으로 사용하지 마세요. 실제 기록은 `08_REC_기록/` 에 REC 로 생성.

## 작성 정보 (예시)
| 항목 | 내용 |
|---|---|
| 프로젝트 코드 | ABC-ADAS-2026-001 |
| ECU/PCB 식별자 | ADAS-DCU-V2-MAINBOARD |
| 시제 Lot # | LOT-ADAS-2026-001-A |
| 보드 Revision | Rev. A |
| 작성자 | 이시그 (SI/PI Engineer) |
| 검토자 | 박에이치더블유 (HW Architect), 최이엠 (EMC Engineer), 김큐에이 (QA) |
| 승인자 | 정에이치 (HW Lead) |
| 작성일 | 2026-05-06 |
| 보고서 버전 | v1.0 |

## 1. 검증 계획 요약 (예시)
| 항목 | 내용 |
|---|---|
| 검증 범위 | SI (Eye diagram, Jitter, Crosstalk), PI (PDN 임피던스), EMC (방사·전도), 기능 동작 |
| 시뮬↔측정 비교 항목 | CAN-FD SI Eye diagram, 1000BASE-T1 Eye diagram, PDN 임피던스, CISPR 25 방사 EMI |
| 합격 기준 | 시뮬 대비 측정값 편차 ≤ 20%; EMC CISPR 25 Class 5 충족 |
| 측정 시작일 | 2026-04-28 |
| 측정 종료일 | 2026-05-05 |
| 측정 장비 (모델·교정일) | Tektronix DPO72004C (교정 2026-03-01), Rohde & Schwarz FSW26 (교정 2026-02-15), VNA ZNB20 (교정 2026-02-15) |

## 2. 시제 PCB ↔ 설계 일치성 검증 (예시)

### 2.1 Visual / 외관 검사 (IPC-A-610)
| 검사 항목 | 결과 (Pass/Fail) | 비고 |
|---|---|---|
| 부품 실장 상태 (납땜 품질) | Pass | IPC-A-610 Class 2 기준 충족 |
| PCB 외관 (스크래치·오염) | Pass | 이상 없음 |
| 커넥터 실장 방향 | Pass | J1~J8 전항목 정방향 |
| LED 극성 | Pass | D1~D4 정방향 실장 |

### 2.2 Stack-up 마이크로섹션 분석
| Layer # | 설계값 (mil) | 실측값 (mil) | 편차 (%) | Pass/Fail |
|---|---|---|---|---|
| L1 (Top Cu) | 1.4 | 1.38 | -1.4% | Pass |
| Prepreg (L1-L2) | 3.5 | 3.52 | +0.6% | Pass |
| L2 (GND) | 1.4 | 1.41 | +0.7% | Pass |
| Core (L2-L3) | 4.7 | 4.68 | -0.4% | Pass |
| 총 판두께 | 62 | 62.4 | +0.6% | Pass |

### 2.3 ICT (Net 연결성)
| 항목 | 설계 | 측정 | 일치 |
|---|---|---|---|
| Total Net 수 | 1,842 | 1,842 | ✓ |
| 단선 | 0 | 0 | ✓ |
| 단락 | 0 | 0 | ✓ |

### 2.4 BOM ↔ 실장 일치
| Item # | Ref Des | 설계 P/N | 실장 P/N | 일치 |
|---|---|---|---|---|
| 1 | U1 | S32G274AAVPHST | S32G274AAVPHST | ✓ |
| 2 | U2 | TPS65981PNPR | TPS65981PNPR | ✓ |
| 3 | U3 | TJA1463BTKZ | TJA1463BTKZ | ✓ |
| 4 | U4 | 88Q2112-A2-NNP2C000 | 88Q2112-A2-NNP2C000 | ✓ |
| 5 | U5 | MAX9296AGTN/V+ | MAX9296AGTN/V+ | ✓ |

## 3. SI 측정 결과 (예시)
| 신호명 | 측정 항목 | 시뮬값 | 측정값 | 편차 (%) | 기준 | Pass/Fail |
|---|---|---|---|---|---|---|
| CAN-FD (5Mbps) | Eye Height | 1.42 V | 1.38 V | -2.8% | ≤20% | Pass |
| CAN-FD (5Mbps) | Eye Width | 165 ps | 158 ps | -4.2% | ≤20% | Pass |
| 1000BASE-T1 | Eye Height | 0.82 V | 0.79 V | -3.7% | ≤20% | Pass |
| DDR4 | Jitter (Tj) | 48 ps | 52 ps | +8.3% | ≤20% | Pass |
| DDR4 | Crosstalk | -32 dB | -29 dB | +3 dB | ≤20% | Pass |

## 4. PI 측정 결과 (예시)
| Power Rail | 측정 항목 | 시뮬값 | 측정값 | 편차 (%) | 기준 | Pass/Fail |
|---|---|---|---|---|---|---|
| VCC_3V3 | PDN 임피던스 (10MHz) | 18 mΩ | 20 mΩ | +11.1% | ≤20% | Pass |
| VCC_1V8 | 부하변동 전압강하 | 42 mV | 47 mV | +11.9% | ≤20% | Pass |
| VCC_1V0 (Core) | Ripple (full load) | 18 mV | 21 mV | +16.7% | ≤20% | Pass |

## 5. EMC 측정 결과 (예시)
| 시험 종류 | 시험 표준 | 측정 주파수/조건 | 측정값 | 기준 | Margin | Pass/Fail |
|---|---|---|---|---|---|---|
| 방사 EMI (협대역) | CISPR 25 Class 5 | 30MHz~1GHz | 최대 38 dBμV/m @156MHz | 40 dBμV/m | +2 dB | Pass |
| 방사 EMI (광대역) | CISPR 25 Class 5 | 30MHz~1GHz | 최대 52 dBμV/m @312MHz | 57 dBμV/m | +5 dB | Pass |
| 전도 EMI | CISPR 25 Class 5 | 0.15MHz~108MHz | 최대 62 dBμV @AM대역 | 66 dBμV | +4 dB | Pass |
| BCI 면역 | ISO 11452-4 | 1MHz~400MHz | 최소 여유 6 dB @CAN-FD 무결성 | — | 6 dB | Pass |

## 6. 시뮬↔측정 모델 타당성 평가 (예시)
| 항목 | 시뮬 모델 | 측정 일치도 | 모델 갱신 필요 |
|---|---|---|---|
| CAN-FD SI | Mentor HyperLynx v16, IBIS v5.1 | 95% (편차 ≤5%) | 불필요 |
| DDR4 SI | Ansys SIwave + IBIS-AMI | 91% (Jitter +8.3%) | 권고 (IBIS-AMI 파라미터 미세조정) |
| PDN (PI) | Ansys SIwave PDN | 88% (VCC_1V0 +16.7%) | 불필요 (허용 범위 내) |
| 방사 EMI | CST Studio Suite 2025 | 94% | 불필요 |

## 7. 결함 / SUP.9 등록 (예시)
| 결함 ID | 카테고리 | 설명 | 심각도 | 조치 상태 |
|---|---|---|---|---|
| — | — | 결함 없음 | — | — |

## 8. 측정 Raw Data 보관 (예시)
| 데이터 종류 | 파일명 | 크기 | CM Tag | 보관 위치 |
|---|---|---|---|---|
| SI Raw (Oscilloscope) | ABC-ADAS-HWE3-SI-raw.zip | 2.4 GB | BL-HWE3-SIraw-v1.0 | Artifactory/HWE/ABC-ADAS-2026-001 |
| EMC Raw (EMI Receiver) | ABC-ADAS-HWE3-EMC-raw.zip | 890 MB | BL-HWE3-EMCraw-v1.0 | Artifactory/HWE/ABC-ADAS-2026-001 |
| PI Raw (VNA) | ABC-ADAS-HWE3-PI-raw.zip | 120 MB | BL-HWE3-PIraw-v1.0 | Artifactory/HWE/ABC-ADAS-2026-001 |

## 9. 종합 판정 (예시)
| 항목 | 결과 |
|---|---|
| PCB↔설계 일치 | Pass (ICT, BOM, Stack-up 전항목 일치) |
| SI 검증 | Pass (편차 최대 8.3%, 기준 20% 이내) |
| PI 검증 | Pass (편차 최대 16.7%, 기준 20% 이내) |
| EMC 검증 | Pass (CISPR 25 Class 5 충족, 최소 여유 2 dB) |
| 종합 결정 (Pass/Conditional/Fail) | **Pass** |
| 후속 HWE.4 진행 가능 여부 | **가능** |

## 10. 승인 (예시)
| 역할 | 성명 | 서명/결재 ID | 일자 |
|---|---|---|---|
| 작성자 | 이시그 | APPR-2026-HWE3-001 | 2026-05-06 |
| 검토자 | 박에이치더블유 | APPR-2026-HWE3-002 | 2026-05-06 |
| 승인자 (HW Lead) | 정에이치 | APPR-2026-HWE3-003 | 2026-05-06 |
