---
type: EX
doc_id: "EX-SPICE-01-02-06-01"
title: "SW 검증 보고서 작성예시"
version: "0.1"
owner: ""
parent_tmp: "[[TMP-SPICE-01-02-06-01_SW검증보고서]]"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [EX, sample, ASPICE, SWE.6]
---

# SW 검증 보고서 작성예시 (EX-SPICE-01-02-06-01)

> 원본 양식: [[TMP-SPICE-01-02-06-01_SW검증보고서]]

## 작성 정보 (예시)
| 항목 | 내용 |
|---|---|
| 빌드 ID | build-2026-06-30-0900 |
| 검증 사이클 | Cycle 1 |
| 작성자 | 한소프 |
| QA Lead 승인 | 윤큐엘 / 2026-07-02 |

## 1. 검증 환경 (예시)
| 환경 | 버전 | 캘리브레이션 |
|---|---|---|
| SIL Simulink R2025b | (no HW) | N/A |
| PIL TC397 EVM #3 | F/W loader v1.4 | 2026-06-25 |

## 2. 검증 케이스 (예시)
| VER-SW | SWR-ID | 시나리오 | 합격 |
|---|---|---|---|
| VER-SW-001 | SWR-...-AEB-001 | 정지 차량 50m | BrakeReq 200ms 이내, decel=0.6g |
| VER-SW-002 | SWR-...-AEB-002 | 빈 도로 1000회 | FP < 0.1% |
| VER-SW-003 | SWR-...-OTA-001 | 변조 펌웨어 100건 | 100% 거부 |

## 3. 결과 (예시)
| VER-SW | P/F | 측정 | 결함 |
|---|---|---|---|
| VER-SW-001 | Pass | 178ms / 0.6g | - |
| VER-SW-002 | Pass | FP=0.0% | - |
| VER-SW-003 | Pass | 100/100 거부 | - |

## 4. 추적성 (예시)
| SWR-ID | VER-SW-ID | 결과 |
|---|---|---|
| SWR-...-AEB-001 | VER-SW-001 | Pass |
| SWR-...-AEB-002 | VER-SW-002 | Pass |
| SWR-...-OTA-001 | VER-SW-003 | Pass |

## 5. 잔여 / 인계 (예시)
- 잔여: 0
- SYS.4 인계: Yes
- QA Lead 서명: 윤큐엘 / 2026-07-02

## 작성 시 유의사항
- 모든 SWR 의 검증 결과 첨부 (미검증 0건)
- 측정 raw 데이터 보존
- QA Lead 의 독립 승인 필수

## 잘못된 작성 사례
> 미검증 SWR 보고 누락 → 추적성 부적합
> 개발 라인 인원이 승인 → 독립성 위반
