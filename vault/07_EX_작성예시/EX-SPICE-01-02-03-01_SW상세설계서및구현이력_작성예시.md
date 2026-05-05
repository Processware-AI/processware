---
type: EX
doc_id: "EX-SPICE-01-02-03-01"
title: "SW 상세설계서 및 구현 이력 작성예시"
version: "0.1"
owner: ""
parent_tmp: "[[TMP-SPICE-01-02-03-01_SW상세설계서및구현이력]]"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [EX, sample, ASPICE, SWE.3]
---

# SW 상세설계서 및 구현 이력 작성예시 (EX-SPICE-01-02-03-01)

> 원본 양식: [[TMP-SPICE-01-02-03-01_SW상세설계서및구현이력]]

## 작성 정보 (예시)
| 항목 | 내용 |
|---|---|
| 모듈 | aeb_decision |
| 파일 | aeb_decision.c / aeb_decision.h |
| 작성자 | 한소프 |
| 리뷰어 | 박개발 (동료), 이아키 (Architect) |

## 2. 함수 명세 (예시)
| 함수 | 입력 | 출력 | pre | post | 예외 | CC |
|---|---|---|---|---|---|---|
| aeb_decide | const ObjectList* obj, float speed_kmh | BrakeReq | obj != NULL, 0 ≤ speed ≤ 300 | BrakeReq.valid == 1 if 발동 | NULL → BrakeReq.invalid 반환 | 8 |
| aeb_calc_decel | float ttc_s, float speed_kmh | float decel_g | ttc_s > 0 | 0 ≤ decel_g ≤ 0.6 | ttc_s ≤ 0 → decel_g = 0.6 | 5 |

## 3. 정적분석 (예시)
| 도구 | 룰셋 | Mandatory | Required | Deviation |
|---|---|---|---|---|
| Polyspace 2025 | MISRA-C:2012 | 0 | 2 (Rule 11.3, 21.6) | DEV-001, DEV-002 (HW 레지스터 cast, printf 사용) |

## 4. 리뷰 기록 (예시)
| 일자 | 리뷰어 | 코멘트 | 종결 | 미종결 사유 |
|---|---|---|---|---|
| 2026-06-15 | 박개발 | 5 | 5 | - |
| 2026-06-16 | 이아키 | 3 | 3 | - |

## 5. 추적성 (예시)
| SWC/Port | 모듈/함수 | 관계 |
|---|---|---|
| SWC-DEC-001 / Port-BRK-001 | aeb_decision.c::aeb_decide | 1:1 |

## 6. Commit (예시)
| Commit | 일자 | 작성자 | 요지 |
|---|---|---|---|
| a3f5c12 | 2026-06-17 | 한소프 | [SWR-...-AEB-001] aeb_decide implementation + unit tests |

## 작성 시 유의사항
- Cyclomatic Complexity ≤ 15
- 모든 Required Deviation 은 사유 + Architect 결재
- 함수 시그니처에 const, restrict 적극 활용

## 잘못된 작성 사례
> CC = 25 함수 → 분리 필요
> Deviation 사유 누락 → 안전 부적합
