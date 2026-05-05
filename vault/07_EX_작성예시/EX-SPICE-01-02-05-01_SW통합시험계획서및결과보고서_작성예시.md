---
type: EX
doc_id: "EX-SPICE-01-02-05-01"
title: "SW 컴포넌트/통합 시험 계획서 및 결과 보고서 작성예시"
version: "0.1"
owner: ""
parent_tmp: "[[TMP-SPICE-01-02-05-01_SW통합시험계획서및결과보고서]]"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [EX, sample, ASPICE, SWE.5]
---

# SW 통합 시험 계획서 및 결과 보고서 작성예시 (EX-SPICE-01-02-05-01)

> 원본 양식: [[TMP-SPICE-01-02-05-01_SW통합시험계획서및결과보고서]]

## 작성 정보 (예시)
| 항목 | 내용 |
|---|---|
| 빌드 ID | build-2026-06-25-1830 |
| Stage | Stage 2 (Decision + Perception) |
| 작성자 | 한소프 |

## 1. 통합 전략 (예시)
| Stage | SWC | 종료 기준 |
|---|---|---|
| 1 | Decision (단독) | Unit Coverage 100% + Lint Pass |
| 2 | Decision + Perception | Port-OBJ-001 시험 100% Pass |
| 3 | + OTA Manager | OTA flashing 시뮬 100% Pass |

## 2. 시험 케이스 (예시)
| TC | Stage | Port | 입력 | 기대 | 합격 |
|---|---|---|---|---|---|
| TC-INT-AEB-001 | 2 | Port-OBJ-001 | ObjectList[정지차량 50m] | BrakeReq sent | 80ms 이내 |
| TC-INT-AEB-002 | 2 | Port-OBJ-001 | ObjectList[빈 도로] x1000 | BrakeReq=0 | FP < 0.1% |

## 3. 실행 결과 (예시)
| TC | P/F | 측정 | 결함 |
|---|---|---|---|
| TC-INT-AEB-001 | Pass | 65ms | - |
| TC-INT-AEB-002 | Pass | FP=0.0% (0/1000) | - |

## 4. 회귀 (예시)
| 변경 | 영향 | 케이스 | 결과 |
|---|---|---|---|
| AEB 알고리즘 patch v2 | TC-INT-AEB-001~005 | 5 | All Pass |

## 작성 시 유의사항
- 빌드 ID 는 immutable + Hash 첨부
- 회귀 케이스는 자동 식별 (영향 분석 도구)

## 잘못된 작성 사례
> 빌드 ID 누락 → 결과 재현 불가
