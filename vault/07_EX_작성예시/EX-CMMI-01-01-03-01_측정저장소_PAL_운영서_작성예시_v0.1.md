---
type: EX
doc_id: EX-CMMI-01-01-03-01
title: "측정저장소 및 PAL 운영서 작성예시"
version: "0.1"
owner: "Measurement Analyst"
parent_tmp: "[[TMP-CMMI-01-01-03-01_측정저장소_PAL_운영서]]"
standards: [CMMI-DEV-ML3-V1.3]
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
status: draft
created: 2026-05-11
updated: 2026-05-11
tags: [EX, CMMI, OPD, sample]
---

# 측정저장소 및 PAL 운영서 작성예시 (EX-CMMI-01-01-03-01)

> 원본: [[TMP-CMMI-01-01-03-01_측정저장소_PAL_운영서]]

## 샘플 컨텍스트
"**알파소프트(주)**" 측정저장소·PAL 운영 예시.

## 1. 문서 정보
| 항목 | 예시값 |
|---|---|
| 문서번호 | MR-PAL-2026-001 |
| 버전 | 1.0 |
| 작성자 | 이OO (MA) |
| 작성일 | 2026-04-25 |

## 2. 스키마 (샘플)
| 도메인 | 메트릭명 | 단위 | 타입 | 메타 |
|---|---|---|---|---|
| 일정 | schedule_variance | % | float | proj_id, period |
| 노력 | effort_actual_hr | hour | float | proj_id, role |
| 결함 | defect_density | defects/KLOC | float | proj_id, phase |
| 리뷰 | review_yield | % | float | proj_id, artifact |

## 3. PAL 카탈로그 (샘플)
| 분류 | 예시 자산 | 메타 | 접근 URL |
|---|---|---|---|
| OSSP | OSSP-2026-001 | v1.0, EPG | wiki/OSSP/2026-001 |
| LCM | LCM-Waterfall | v1.0, EPG | wiki/LCM/Waterfall |
| 가이드 | TG-2026-001 | v1.0, EPG | wiki/Guide/TG-2026-001 |
| 측정 | MA Plan ML3 | v1.0, MA | wiki/Plan/MA-ML3 |

## 4. 권한 매트릭스 (샘플)
| 역할 | 조회 | 등록 | 수정 | 삭제 |
|---|---|---|---|---|
| 전 임직원 | O | X | X | X |
| 프로젝트 PM | O | O | X | X |
| EPG | O | O | O | X |
| CM Manager | O | O | O | O |

## 5. 운영 점검 (샘플)
| 주기 | 점검 항목 | 책임 |
|---|---|---|
| 분기 | 무결성 검증 (체크섬) | MA |
| 분기 | 접근 로그 감사 | CM, 보안 |
| 반기 | 자산 사용도 분석 | EPG |

## 작성 시 유의사항
- 메트릭 단위는 ISO 단위(시간·% 등)로 통일.
- 권한은 최소권한 원칙.

## 잘못된 작성 사례
> ❌ 전 인원에게 등록·수정 권한 부여 — 데이터 품질 저하
> ✅ 등록은 PM 이상으로 제한 + 변경 이력 자동 기록
