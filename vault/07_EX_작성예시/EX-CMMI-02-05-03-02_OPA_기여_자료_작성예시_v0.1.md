---
type: EX
doc_id: EX-CMMI-02-05-03-02
title: "OPA 기여 자료 작성예시"
version: "0.1"
owner: "Project Manager"
parent_tmp: "[[TMP-CMMI-02-05-03-02_OPA_기여_자료]]"
standards: [CMMI-DEV-ML3-V1.3]
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
status: draft
created: 2026-05-11
updated: 2026-05-11
tags: [EX, CMMI, IPM, OPA, sample]
---

# OPA 기여 자료 작성예시

> 원본: [[TMP-CMMI-02-05-03-02_OPA_기여_자료]]

## 1. 문서 정보 (샘플)
| 항목 | 예시값 |
|---|---|
| 프로젝트명 | 모바일 헬스케어 앱 v2.0 |
| 종료일 | 2026-11-30 |
| 작성자 | 김OO (PM) |

## 2. 측정값 기여 (샘플)
| 측정 항목 | 값 | 단위 | PAL 등록 ID |
|---|---|---|---|
| 총 effort | 13.2 | person-month | PAL-MEAS-2026-HCA-001 |
| Defect rate (Beta 기준) | 2.8 | per 1000 LOC | PAL-MEAS-2026-HCA-002 |
| HealthKit 통합 effort | 1.4 | person-month | PAL-MEAS-2026-HCA-003 |
| SUS 점수 | 84 | score | PAL-MEAS-2026-HCA-004 |

## 3. 교훈 (샘플)
| 교훈 ID | 카테고리 | 내용 | 적용 도메인 |
|---|---|---|---|
| LL-001 | 잘된 점 | UI/UX 외주 + 사내 디자이너 페어링으로 도메인 fit + 생산성 둘 다 확보 | 모바일, 도메인 신규 |
| LL-002 | 개선점 | HealthKit API 변경 모니터링이 늦었음 — 분기 Apple Dev Beta 추적 권장 | iOS, 외부 의존성 |
| LL-003 | 잘된 점 | 격주 Try/Continue/Stop 회고가 빠른 개선 사이클 만듦 | Agile, 모든 도메인 |

## 4. 개선 제안 (OPF SP1.1 입력) (샘플)
| 제안 ID | 영역 | 내용 | 예상 효과 |
|---|---|---|---|
| IS-001 | 프로세스 | 자원 계획서에 휴가 캘린더 통합 항목 추가 (ISS-005 RCA) | 일정 지연 방지 |
| IS-002 | 도구 | HealthKit-like 외부 API breaking change 자동 알림 도구 도입 | API 위험 감소 |
| IS-003 | 조직 | 모바일 도메인 자문 풀 (헬스/금융/리테일) 구축 | 신규 도메인 입장 시간 단축 |

## 5. EPG 인계 (샘플)
| 항목 | 내용 |
|---|---|
| 인계일 | 2026-12-05 |
| 인계자 | 김OO (PM) |
| EPG 수신자 | 김OO (EPG Lead) |
| PAL 등록 ID | PAL-BATCH-2026-HCA-001 (4 측정 + 3 교훈 + 3 개선) |

## 6. 결재 (샘플)
| 검토 | 승인 | 일자 |
|---|---|---|
| 김OO (EPG Lead) | 이OO (PMO Director) | 2026-12-06 |

## 작성 시 유의사항
- IPM KPI = OPA 기여 ≥ 3건. 본 EX 는 10건 (4+3+3) — 잘된 수준.
- 교훈 카테고리는 "잘된/개선" 페어로 균형 잡힐 것 권장.

## 잘못된 작성 사례
> ❌ "특별한 측정값 없음" 으로 측정값 항목 0건
> ✅ 최소 1건 — 작은 프로젝트라도 effort/duration 은 기록 가능
