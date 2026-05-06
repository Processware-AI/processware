---
type: EX
doc_id: "EX-ASPICE-01-03-03-01"
title: "BOM 작성예시"
version: "0.1"
owner: ""
parent_tmp: "[[TMP-ASPICE-01-03-03-01_BOM]]"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [EX, sample, ASPICE, HWE.2, BOM]
---

# BOM 작성예시 (EX-ASPICE-01-03-03-01)

> 원본 양식: [[TMP-ASPICE-01-03-03-01_BOM]]

> 이 파일은 교육·가이드용 샘플입니다. 실제 기록으로 사용하지 마세요. 실제 기록은 `08_REC_기록/` 에 REC 로 생성.

## 작성 정보 (예시)
| 항목 | 내용 |
|---|---|
| 프로젝트 코드 | VW-ADAS-2026-001 |
| ECU/PCB 식별자 | ADAS-DCU-V2-MAINBOARD |
| 보드 Revision | Rev. A |
| BOM 버전 | v1.0 |
| 작성자 | 박회로 (HW Engineering Team) |
| 검토자 | 송구매 (Procurement), 한큐엠 (QA), 류세이프 (Safety Engineer) |
| 승인자 | 정에이치 (HW Lead), 강시엠 (CM Manager) |
| 작성일 | 2026-05-06 |

## 1. BOM 본표 (예시 — 일부 발췌)
| Item # | Ref Des | Qty | Value | Footprint | Manufacturer | P/N | Vendor | Vendor P/N | AEC-Q | Lifetime | EoL | Lead | Price (USD) | 특수특성 | 비고 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | U1 | 1 | MCU+SoC | BGA-525 | NXP | S32G274AAVPHST | Avnet | S32G274AAVPHST | Q100 G2 | 15+ | L | 16 | 285.50 | ♦§ | ASIL D Lockstep |
| 2 | U2 | 1 | PMIC | QFN-48 | TI | TPS65981PNPR | Digikey | 296-TPS65981PNPRCT-ND | Q100 G2 | 10+ | L | 12 | 8.45 | ♦ | ASIL B 전원 |
| 3 | U3 | 1 | CAN-FD Tx | SOIC-14 | NXP | TJA1463BTKZ | Mouser | 771-TJA1463BTKZ | Q100 G1 | 12+ | L | 10 | 2.85 | ♦ | ASIL B |
| 4 | U4 | 1 | Eth PHY | QFN-56 | Marvell | 88Q2112-A2-NNP2C000 | Avnet | 88Q2112-A2 | Q100 G2 | 10+ | M | 14 | 12.30 | § | Cybersec MAC sec |
| 5 | U5 | 1 | GMSL2 Des | TQFN-56 | ADI | MAX9296AGTN/V+ | Mouser | 700-MAX9296AGTNV | Q100 G2 | 10+ | L | 10 | 18.20 | ¤ | EMC critical |
| 6 | C1~C12 | 12 | 100nF/50V | 0402 | Murata | GRM155R71H104KE14D | Digikey | 490-1532-1-ND | Q200 | 10+ | L | 4 | 0.012 |  |  |
| 7 | R1~R8 | 8 | 10kΩ 1% | 0402 | Yageo | RC0402FR-0710KL | Digikey | 311-10.0KLRCT-ND | Q200 | 10+ | L | 4 | 0.008 |  |  |

(실제 BOM 은 약 220 행)

## 2. 특수특성 부품 요약 (예시)
| Item # | P/N | 분류 | 등급 | 변경 시 시험 요구 |
|---|---|---|---|---|
| 1 | S32G274AAVPHST | Safety + Cyber | ASIL D + CAL 4 | 회귀 + Safety Re-cert + Pen Test |
| 2 | TPS65981PNPR | Safety | ASIL B | FMEA 재수행 + 전원 회귀 |
| 3 | TJA1463BTKZ | Safety | ASIL B | CAN 통신 회귀 |
| 4 | 88Q2112-A2 | Cyber | CAL 3 | TARA 재수행 + Pen Test |
| 5 | MAX9296AGTN/V+ | EMC | — | EMC Pre-comp + 시제 EMC 재시험 |

## 3. EoL Risk 부품 요약 (예시)
| Item # | P/N | EoL Status | 통지일 | Second Source | 호환성 검토 |
|---|---|---|---|---|---|
| 4 | 88Q2112-A2 | Active (Medium 관찰) | — | Realtek RTL9001E | Pin compatible 미충족 → 회로 변경 필요 (사전 검토 완료) |

## 4. AVL 매칭 결과 (예시)
| Item # | P/N | AVL 등재 | 등록일 | 비고 |
|---|---|---|---|---|
| 1~5 | (위 주요 IC 5종) | 등재 | 2025-11~2026-03 | 정식 등재 |
| 6, 7 | Murata, Yageo Passive | 등재 | 2024-08 | 표준 부품 |
| 매칭률 | — | — | — | 100% (220/220) |

## 5. 생산데이터 패키지 (예시)
| 파일 종류 | 파일명 | 버전 | 발행일 | 발행자 |
|---|---|---|---|---|
| Gerber (RS-274X) | VW-ADAS-2026-001-RevA-Gerber-v1.0.zip | v1.0 | 2026-05-06 | 박회로 |
| Drill (Excellon) | VW-ADAS-2026-001-RevA-Drill-v1.0.txt | v1.0 | 2026-05-06 | 박회로 |
| Pick&Place | VW-ADAS-2026-001-RevA-PickPlace-v1.0.csv | v1.0 | 2026-05-06 | 박회로 |
| Stack-up | VW-ADAS-2026-001-RevA-Stackup-v1.0.pdf | v1.0 | 2026-05-06 | 박회로 |
| Assembly Drawing | VW-ADAS-2026-001-RevA-Assy-v1.0.pdf | v1.0 | 2026-05-06 | 박회로 |

## 6. BOM 검토 결과 (예시)
| 일자 | 검토자 | 주요 지적 | 조치 | 상태 |
|---|---|---|---|---|
| 2026-05-04 | 송구매 | Item #4 Eth PHY EoL Risk Medium → Second Source 승인 필요 | Realtek RTL9001E 호환성 보고서 첨부 | Closed |
| 2026-05-05 | 류세이프 | Item #1 ASIL D — Lockstep 사용 표시 누락 | "ASIL D Lockstep" 비고 추가 | Closed |
| 2026-05-06 | 한큐엠 | 특수특성 컬럼 표기 일관성 (♦§¤ 정의 별첨 필요) | 별첨 범례 추가 | Closed |

## 7. CM 베이스라인 등록 (예시)
| 항목 | 내용 |
|---|---|
| CM 시스템 | Polarion ALM + Git LFS |
| BOM Baseline Tag | BOM-VW-ADAS-2026-001-RevA-v1.0 |
| 생산데이터 Tag | PROD-VW-ADAS-2026-001-RevA-v1.0 |
| 등록일 | 2026-05-06 |
| 등록자 | 박회로 |
| CM Manager 승인 | 강시엠 (전자결재 ID: APPR-CM-2026-0312) |

## 8. 변경 이력 (예시)
| 일자 | 변경 ID | 변경 내용 | 승인자 |
|---|---|---|---|
| 2026-04-28 | CHG-BOM-001 | Item #4 Eth PHY → Marvell 88Q2112 (당초 88Q2110 EoL) | 정에이치 |

## 작성 시 유의사항
- Manufacturer P/N 은 풀네임 (suffix 포함) 명시 — Generic part name 금지.
- AEC-Q Grade 는 Q100 (반도체) / Q200 (수동소자) 모두 명확히 구분.
- EoL Risk 는 단순 부재 표기가 아닌 Vendor 공식 Lifetime 또는 Z2Data/IHS 조회 결과 기반.
- 특수특성 표기 (♦Safety / §Cyber / ¤EMC) 는 별첨 범례와 일관 유지.
- Lead Time 은 양산 시점 기준 — 시제 전용 단납기 부품은 양산 위험으로 별도 표시.
- BOM 변경 시 반드시 SUP.10 변경 절차 + 회귀 시험 강제.

## 잘못된 작성 사례
> "STM32 MCU" — 정확한 P/N 없음. → "STM32H743ZIT6" 풀네임.
> "EoL: 없음" — Vendor 공식 확인 없이 빈칸. → Lifetime 연수 + DB 조회 일자 함께 기록.
> "특수특성: Safety" — 등급 누락. → "♦ Safety / ASIL B" 형식.
