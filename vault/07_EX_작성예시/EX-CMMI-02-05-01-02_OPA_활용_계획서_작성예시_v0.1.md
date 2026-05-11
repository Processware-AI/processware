---
type: EX
doc_id: EX-CMMI-02-05-01-02
title: "OPA 활용 계획서 작성예시"
version: "0.1"
owner: "Project Manager"
parent_tmp: "[[TMP-CMMI-02-05-01-02_OPA_활용_계획서]]"
standards: [CMMI-DEV-ML3-V1.3]
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
status: draft
created: 2026-05-11
updated: 2026-05-11
tags: [EX, CMMI, IPM, sample]
---

# OPA 활용 계획서 작성예시

> 원본: [[TMP-CMMI-02-05-01-02_OPA_활용_계획서]]

## 1. 문서 정보 (샘플)
| 항목 | 예시값 |
|---|---|
| 프로젝트명 | 모바일 헬스케어 앱 v2.0 |
| 작성자 | 김OO (PM) |
| 작성일 | 2026-05-25 |

## 2. 활용할 OPA 자산
| 자산 ID | 유형 | 활용 목적 |
|---|---|---|
| PAL-MEAS-2024-HCM-001 | 측정값 (effort) | WI-01 추정 baseline |
| PAL-LL-2025-FIT-002-003 | 교훈 | iOS 시뮬레이터 다중 디바이스 시험 노하우 |
| PAL-REUSE-AUTH-001 | 재사용 | OAuth 인증 모듈 재사용 |

## 3. 기여 자산 후보 (종료 시)
| 후보 | 유형 | 예상 시점 |
|---|---|---|
| HealthKit 통합 effort 측정 | 측정값 | 2026-12 |
| 모바일 헬스 SUS 평가 노하우 | 교훈 | 2026-12 |
| 디자인 시스템 재사용 컴포넌트 | 재사용 | 2026-12 |

## 4. 결재
| 검토 | 승인 | 일자 |
|---|---|---|
| 김OO (EPG Lead) | 이OO (PMO Director) | 2026-05-26 |

## 작성 시 유의사항
- 활용·기여 둘 다 명시 — 단방향 (활용만/기여만) 은 GG3 GP 3.2 미충족.
- 기여 후보 ≥ 3 권장 (IPM KPI).

## 잘못된 작성 사례
> ❌ 활용 자산만 적고 기여 후보 공란
> ✅ Bidirectional — 활용 + 기여 양쪽 명시
