---
type: EX
doc_id: "EX-SPICE-01-02-01-01"
title: "SW 요구사항 명세서 작성예시"
version: "0.1"
owner: ""
parent_tmp: "[[TMP-SPICE-01-02-01-01_SW요구사항명세서]]"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [EX, sample, ASPICE, SWE.1]
---

# SW 요구사항 명세서 작성예시 (EX-SPICE-01-02-01-01)

> 원본 양식: [[TMP-SPICE-01-02-01-01_SW요구사항명세서]]

## 작성 정보 (예시)
| 항목 | 내용 |
|---|---|
| 프로젝트 코드 | VW-ADAS-2026-001 |
| SwRS 버전 | v1.0 |
| AUTOSAR 환경 | Classic + Adaptive (혼합) |
| 작성자 | 한소프 |

## 2. SW 기능 요구사항 (예시)
| SWR-ID | 요구사항 | 컴포넌트 | 입력 | 출력 | 시험가능성 |
|---|---|---|---|---|---|
| SWR-...-AEB-001 | 정지 차량 50m 내 감지 시 0.6g 감속 신호 송출 | Decision SWC | ObjectList (struct) | BrakeRequest (CAN signal) | Unit: stub 입력 → CAN 신호 검증 |
| SWR-...-AEB-002 | False Positive < 0.1% (빈 도로 1000회) | Decision SWC | ObjectList | (no signal) | Unit: 1000회 빈 도로 시뮬 |
| SWR-...-LKA-001 | 차선 인식 후 EPS 토크 명령 ±5Nm 산출 | Decision SWC | LaneInfo | EPS_Torque | Unit: 곡률별 토크 곡선 검증 |

## 3. 비기능 요구사항 (예시)
| ID | 카테고리 | 요구사항 | 정량 |
|---|---|---|---|
| SWR-...-NF-001 | 성능 | Decision Loop 주기 | ≤ 50ms |
| SWR-...-NF-002 | 메모리 | Decision SWC RAM | ≤ 256KB |
| SWR-...-NF-003 | 메모리 | Flash | ≤ 1MB |

## 4. ASIL 상속·분리 (예시)
| SWR-ID | 상속 | 분리 | 사유 |
|---|---|---|---|
| SWR-...-AEB-001 | ASIL D | 분리 안함 | 단일 SWC 책임 |
| SWR-...-AEB-002 | ASIL D | B(D) + B(D) Decomposition | False Positive 검증 + 시뮬 검증 분리 (ISO 26262-9 Clause 5) |

## 5. 자원 분석 (예시)
| 항목 | 예산 | 추정 | Margin |
|---|---|---|---|
| RAM | 256KB | 198KB | 23% |
| Flash | 1MB | 740KB | 26% |
| CPU 점유 | 40% | 32% | 8%p |

## 6. 추적성 (예시)
| SyRS-ID | SWR-ID | 관계 |
|---|---|---|
| SYS-...-002 | SWR-...-AEB-001, SWR-...-AEB-002 | 1:N |
| SYS-...-001 | SWR-...-LKA-001 | 1:1 |

## 7. 베이스라인 (예시)
| CM Tag | SwRS-VW-ADAS-2026-001-v1.0 |
| 등록일 | 2026-06-01 |

## 작성 시 유의사항
- ASIL Decomposition 은 ISO 26262-9 Clause 5 규칙 인용 + Safety Engineer 결재
- 자원 Margin ≥ 20% 권장 (변경 buffer)

## 잘못된 작성 사례
> SWR 에 시험가능성 미기재 → SWE.4 케이스 작성 불가
> ASIL 분리에 사유·승인 없음 → 안전 부적합
