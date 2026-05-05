---
type: EX
doc_id: "EX-ASPICE-01-02-02-01"
title: "SW 아키텍처 기술서 작성예시"
version: "0.1"
owner: ""
parent_tmp: "[[TMP-ASPICE-01-02-02-01_SW아키텍처기술서]]"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [EX, sample, ASPICE, SWE.2]
---

# SW 아키텍처 기술서 작성예시 (EX-ASPICE-01-02-02-01)

> 원본 양식: [[TMP-ASPICE-01-02-02-01_SW아키텍처기술서]]

## 1. SWC 구조 (예시)
| SWC-ID | 명 | 책임 | 부모 |
|---|---|---|---|
| SWC-DEC-001 | Decision SWC | LKA/AEB 결정 로직 | ADAS_Composition |
| SWC-PER-001 | Perception Adapter | ML 모델 결과 후처리 | ADAS_Composition |
| SWC-OTA-001 | OTA Manager | 펌웨어 검증·flashing | ADAS_Composition |

## 2. 인터페이스 (예시)
| Port-ID | 종류 | 송신 | 수신 | 데이터 | QoS |
|---|---|---|---|---|---|
| Port-OBJ-001 | Sender/Receiver | SWC-PER-001 | SWC-DEC-001 | struct ObjectList[16] | 33ms cyclic |
| Port-BRK-001 | Sender/Receiver | SWC-DEC-001 | RTE→CAN | struct BrakeReq | 10ms cyclic, E2E CRC |
| Port-OTA-001 | Client/Server | SWC-OTA-001 | NVM Service | binary blob | request-response |

## 3. 자원·타이밍 (예시)
| 항목 | 예산 | 추정 |
|---|---|---|
| Decision Task 주기 | 50ms | 50ms |
| Decision WCET | 20ms | 12ms (실측 platform = TC397) |
| RAM | 256KB | 198KB |

## 4. 동적 거동 (예시)
| Runnable | Trigger | Task | 우선순위 | WCET |
|---|---|---|---|---|
| Decision_Run | 50ms cyclic | Task_50ms | 5 (high) | 12ms |
| OTA_Verify | Event | Task_OTA | 1 (low) | 200ms |

## 5. 추적성 (예시)
| SWR-ID | SWC/Port | 관계 |
|---|---|---|
| SWR-...-AEB-001 | SWC-DEC-001 + Port-BRK-001 | 1:N |
| SWR-...-OTA-001 | SWC-OTA-001 | 1:1 |

## 6. 베이스라인 (예시)
| CM Tag | SwAD-VW-ADAS-2026-001-v1.0 |
| 등록일 | 2026-06-08 |

## 작성 시 유의사항
- WCET 는 실측 플랫폼 명시 (예: Infineon AURIX TC397)
- ASIL D Port 는 E2E Protection 필수
- Resource Margin ≥ 20%

## 잘못된 작성 사례
> WCET 추정만 있고 실측 없음 → 안전 분석 부족
> Port 의 QoS (주기·CRC) 누락 → 통합 시 결함 위험
