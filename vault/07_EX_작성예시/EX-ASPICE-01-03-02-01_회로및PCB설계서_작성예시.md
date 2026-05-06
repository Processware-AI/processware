---
type: EX
doc_id: "EX-ASPICE-01-03-02-01"
title: "회로 및 PCB 설계서 작성예시"
version: "0.1"
owner: ""
parent_tmp: "[[TMP-ASPICE-01-03-02-01_회로및PCB설계서]]"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [EX, sample, ASPICE, HWE.2]
---

# 회로 및 PCB 설계서 작성예시 (EX-ASPICE-01-03-02-01)

> 원본 양식: [[TMP-ASPICE-01-03-02-01_회로및PCB설계서]]

> 이 파일은 교육·가이드용 샘플입니다. 실제 기록으로 사용하지 마세요. 실제 기록은 `08_REC_기록/` 에 REC 로 생성.

## 작성 정보 (예시)
| 항목 | 내용 |
|---|---|
| 프로젝트 코드 | VW-ADAS-2026-001 |
| ECU/PCB 식별자 | ADAS-DCU-V2-MAINBOARD |
| 보드 Revision | Rev. A |
| 작성자 | 박회로 (HW Engineering Team) |
| 검토자 | 김아키 (HW Architect), 이시그 (SI/PI Engineer), 최이엠 (EMC Engineer) |
| 승인자 | 정에이치 (HW Lead) |
| 작성일 | 2026-05-06 |
| 베이스라인 버전 | v1.0 |

## 1. 개요 (예시)
| 항목 | 내용 |
|---|---|
| 적용 HwRS 베이스라인 | HwRS-VW-ADAS-2026-001-v1.0 |
| 보드 기능 요약 | ADAS Domain Controller — Camera/Radar 입력 → 인지 처리 → CAN-FD 출력 |
| 핵심 IC | NXP S32G274A (MCU+SoC), TI TPS65981 (PMIC), Marvell 88Q2112 (1000BASE-T1 PHY) |
| 동작 전압 / 소비전류 | 12V (8~16V tolerant) / 평균 8.5W, peak 14W |
| 동작 온도 범위 | -40°C ~ +85°C (AEC-Q100 Grade 2) |

## 2. 회로 블록도 (예시)
| # | 블록 명 | 기능 | 입력 | 출력 | 핵심 IC |
|---|---|---|---|---|---|
| B1 | Power Mgmt | 12V → 5V/3.3V/1.8V/1.0V | VBAT | DC rails | TPS65981 |
| B2 | MCU Cluster | 인지 알고리즘 실행 | DDR4, Flash | CAN-FD, Ethernet | S32G274A |
| B3 | CAN-FD I/F | 차량 CAN 통신 | MCU TX/RX | CAN_H/L | TJA1463 |
| B4 | Ethernet PHY | 카메라/레이더 데이터 수신 | RGMII | 1000BASE-T1 | 88Q2112 |
| B5 | Camera GMSL2 | 4채널 카메라 입력 | GMSL2 | CSI-2 | MAX9296A |

## 3. 핵심 IC 부품 선정 (예시)
| # | 카테고리 | P/N | Vendor | AEC-Q100 | Lifetime | EoL Risk |
|---|---|---|---|---|---|---|
| 1 | MCU+SoC | S32G274AAVPHST | NXP | Grade 2 | 15+ years | Low |
| 2 | PMIC | TPS65981PNPR | TI | Grade 2 | 10+ years | Low |
| 3 | CAN-FD | TJA1463BTKZ | NXP | Grade 1 | 12+ years | Low |
| 4 | Eth PHY | 88Q2112-A2-NNP2C000 | Marvell | Grade 2 | 10+ years | Medium (관찰) |
| 5 | GMSL2 Deserializer | MAX9296AGTN/V+ | ADI(Maxim) | Grade 2 | 10+ years | Low |

## 4. PCB Stack-up (예시 — 8 layer)
| Layer # | 종류 | 두께 (mil) | 임피던스 | 비고 |
|---|---|---|---|---|
| L1 | Signal (Top) | 1.4 | 50Ω SE / 100Ω diff | High-speed (CAN-FD, Ethernet) |
| L2 | GND | 1.4 | — | Reference plane |
| L3 | Signal | 0.7 | 50Ω SE | Camera GMSL2 |
| L4 | Power (3.3V) | 1.4 | — |  |
| L5 | Power (1.0V/1.8V) | 1.4 | — |  |
| L6 | Signal | 0.7 | 50Ω SE | DDR4 |
| L7 | GND | 1.4 | — | Reference plane |
| L8 | Signal (Bot) | 1.4 | 50Ω SE | Low-speed I/O |

## 5. SI/PI 시뮬레이션 결과 (예시)
| 신호명 | 도구 | 측정 항목 | 측정값 | 기준 | Pass/Fail |
|---|---|---|---|---|---|
| CAN-FD (5Mbps) | HyperLynx | Eye height | 1.85V | ≥ 1.5V | Pass |
| 1000BASE-T1 | HyperLynx | Eye width | 0.78 UI | ≥ 0.65 UI | Pass |
| DDR4-2400 | SIwave | Eye width | 0.62 UI | ≥ 0.55 UI | Pass |
| 1.0V Core PDN | SIwave | Z @ 1MHz | 8 mΩ | ≤ 10 mΩ | Pass |

## 6. EMC Pre-compliance (예시)
| 항목 | 도구 | 주파수 | 측정값 | 기준 (CISPR 25 Cl.5) | Margin |
|---|---|---|---|---|---|
| 방사 EMI (Vertical) | EMC Studio | 30~200 MHz | 28 dBμV/m | 36 dBμV/m | 8 dB |
| 방사 EMI (Vertical) | EMC Studio | 200~1000 MHz | 32 dBμV/m | 40 dBμV/m | 8 dB |
| 전도 EMI (BCI) | CST | 1~108 MHz | 22 dBμA | 30 dBμA | 8 dB |

## 7. DRC 결과 (예시)
| 항목 | 위반 건수 | 조치 | 최종 |
|---|---|---|---|
| Clearance violation | 12 → 0 | Trace re-route + spacing 조정 | Pass |
| Drill-to-copper | 3 → 0 | Pad size 확대 | Pass |
| Acid trap | 5 → 0 | 90° 코너 → 45° 변경 | Pass |
| 총계 | 20 → 0 |  | Pass |

## 8. HwRS ↔ Schematic 추적성 (예시)
| HwRS ID | 회로 블록 # | Sheet # | 비고 |
|---|---|---|---|
| HWR-VW-ADAS-2026-001-001 (CAN-FD I/F) | B3 | Sheet-04 |  |
| HWR-VW-ADAS-2026-001-002 (Camera 4ch) | B5 | Sheet-06 |  |
| HWR-VW-ADAS-2026-001-101 (전원 8.5W typ) | B1 | Sheet-02 |  |
| 추적성 커버리지 | — | — | 96.4% (53/55) |

## 9. 설계 검토 결과 (예시)
| 일자 | 참석자 | 주요 지적 | 조치 | 승인 |
|---|---|---|---|---|
| 2026-05-04 | 김아키, 이시그, 최이엠, 정에이치 | DDR4 length matching ±5mil → ±2mil 강화 | 라우팅 재작업 완료 | Pending |
| 2026-05-06 | 동일 | 모든 지적 해소 확인 | — | Approved (정에이치) |

## 10. 베이스라인 등록 (예시)
| 항목 | 내용 |
|---|---|
| CM 시스템 | Polarion ALM + Git LFS |
| Schematic Tag | SCH-VW-ADAS-2026-001-RevA-v1.0 |
| PCB Layout Tag | PCB-VW-ADAS-2026-001-RevA-v1.0 |
| 등록일 | 2026-05-06 |
| 등록자 | 박회로 |

## 작성 시 유의사항
- Schematic 의 모든 부품에 AEC-Q100/Q200 Grade 명시 — Grade 미달 부품 사용 시 Safety 검토 의무.
- SI/PI 시뮬 측정값은 정량 수치 + 단위 + 기준 함께 기록 (Pass/Fail 단독 기재 금지).
- EMC Margin 은 최소 6 dB 이상 확보 권고 (시제 단계 변동 흡수).
- DRC 위반은 Patch 식 수정 금지 — 위반 패턴 분석 후 재라우팅 원칙.
- HwRS↔Schematic 추적성이 95% 미달 시 누락 ID 사유 기록.

## 잘못된 작성 사례
> "PCB Stack-up: 일반적 4-layer" — 임피던스·두께 누락. → Layer별 종류·두께·임피던스 표 작성.
> "EMC OK" — 정량값 없음. → 실측 dBμV/m + 기준 + Margin 함께 기록.
> "DRC 통과" — 위반 → 조치 이력 누락. → 위반 카테고리별 건수 변화 기록.
