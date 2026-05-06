---
doc_id: "EX-ASPICE-01-08-05-01"
title: "CCB 회의록 작성예시"
type: EX
version: "0.1"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
scope_code: "ASPICE"
domain: "ASPICE"
parent_tmp: "[[TMP-ASPICE-01-08-05-01_CCB회의록]]"
aspice_processes: ["SUP.10"]
standards: ["Automotive SPICE 4.0"]
tags: [EX, sample, ASPICE, SUP.10, CCB]
---

# CCB 회의록 작성예시

> 본 문서는 작성 요령 학습용 예시입니다. 가상의 ABC Motors Co., Ltd. ADAS DCU V2 프로젝트(ABC-ADAS-2026-001) 데이터를 사용합니다.

## 작성정보
| 항목 | 내용 |
|---|---|
| 회의 ID | CCB-ABC-ADAS-2026-003 |
| 회의 차수 | 2026년 정기 CCB 18차 |
| 회의 유형 | 정기 |
| 일시 | 2026-05-06 14:00 ~ 15:30 KST |
| 장소 | 대면 (ABC Motors HQ 회의실 7F-301) + 원격 (Webex) 병행 |
| 작성자 (CCB 간사) | 김프로젝트 (Project Manager) |
| 검토자 | CCB Members 전원 |
| 승인자 (CCB Chair) | 윤시비 (Program Director) |

## 참석자 및 정족수
| 역할 | 성명 | 참석 여부 | 비고 |
|---|---|---|---|
| CCB Chair | 윤시비 | 참석 (대면) | — |
| Project Manager | 김프로젝트 | 참석 (대면) | — |
| Technical Lead | 이아키 | 참석 (대면) | — |
| QA | 박품질 | 참석 (대면) | — |
| Safety Engineer | 최세이프 | 참석 (원격, Webex) | — |
| Cybersecurity Engineer | 한사이버 | 참석 (대면) | — |
| CM Manager | 송형상 | 참석 (대면) | — |
| (기타 초청자) | 임변경 (Change Control Eng) | 참석 (대면) | CR 발표 |

| 정족수 | 충족 여부 |
|---|---|
| 필요 정원 / 실제 참석 | 7명 중 7명 참석 (100%) |
| 필수 분야 참석 (안전·보안 CR 시) | Safety / Cybersecurity 모두 참석 — 충족 |

## 1. 검토 CR 목록
| CR-ID | 제목 | 영향 평가 ID | 변경 유형 | CCB 권고안 |
|---|---|---|---|---|
| CR-007 | CAN-FD 메시지 ID 변경 (0x101 → 0x201) | IA-ABC-ADAS-2026-001-CR-007 | Minor | 조건부 승인 |
| CR-008 | 자율긴급제동(AEB) 알고리즘 임계값 완화 | IA-ABC-ADAS-2026-001-CR-008 | Major | 반려 |

## 2. CR 별 논의 요약
| CR-ID | 주요 논의 내용 | 질의·답변 요약 |
|---|---|---|
| CR-007 | OEM 게이트웨이 정합 시급. 페이로드 불변, ASIL 영향 없음. 작업량 2.5 MD, 일정 +2일. | Q(QA) 인접 메시지 충돌 가능성? A(Tech Lead) TC-COMM-013 으로 검증 예정. Q(Safety) ASIL 변동 진짜 없음? A(Safety) 페이로드·신뢰성 메커니즘 동일, 영향 없음 확인. |
| CR-008 | AEB 30 km/h 미만 정지 요건을 25 km/h 로 완화 요청 (HW 응답속도 한계). | Q(Safety) ASIL D 안전목표 직접 영향. 잔존 위험 수용 불가. A(요청자) 인정. Q(QA) Safety Case 재작성 부담. 결론: 반려, HW 개선으로 재추진 권고. |

## 3. 의결 결과
| CR-ID | 결정 (Approved / Conditional / Rejected / Deferred) | 조건 (조건부 시) | 반려 사유 | 의결 정족수 |
|---|---|---|---|---|
| CR-007 | Conditional Approved | (1) SWE.5 통합 시험 TC-COMM-012, TC-COMM-013, TC-COMM-012-A 모두 Pass, (2) 신규 베이스라인 BL-REL-v1.0.1 발행 | — | 7/7 찬성 |
| CR-008 | Rejected | — | ASIL D 안전목표 직접 위배. 잔존 위험 수용 불가. HW 개선 후 재상정 권고. | 7/7 반려 |

## 4. CR 상태 갱신 확인
| CR-ID | SUP.10 시스템 갱신 상태 | 갱신 일시 | 갱신자 |
|---|---|---|---|
| CR-007 | Conditional Approved | 2026-05-06 15:35 KST | 임변경 |
| CR-008 | Rejected | 2026-05-06 15:35 KST | 임변경 |

## 5. 차기 CCB 예정
| 항목 | 내용 |
|---|---|
| 차기 회의 일시 | 2026-05-13 14:00 KST (정기 19차) |
| 차기 의제 (보류 CR 포함) | (1) CR-007 구현 결과 보고, (2) CR-009 (UI 다국어 지원) 영향 평가 결과 검토, (3) CR-010 후보 사전 검토 |

## 6. 서명
| 역할 | 성명 | 서명 | 일자 |
|---|---|---|---|
| 작성 (CCB 간사 / PM) | 김프로젝트 | (서명) | 2026-05-06 |
| 승인 (CCB Chair) | 윤시비 | (서명) | 2026-05-06 |

---

## 작성 요령
- **정족수와 필수 분야 분리 기록**: 단순 과반뿐 아니라 안전·보안 CR 시 Safety/Cybersecurity 참석 필수 — 별도 칸으로 가시화.
- **질의·답변 요약 필수**: 단순 결정만 적으면 사후 추적 시 의사결정 근거가 사라짐. 핵심 질의 1~2개라도 기록.
- **조건은 측정 가능하게**: "잘 검증할 것" 같은 모호한 조건 금지. "TC-XXX 모두 Pass" 처럼 기준 명시.
- **CR 상태 즉시 갱신**: 회의 종료 즉시(권장 15분 내) SUP.10 시스템에 반영. 갱신자·일시 기록.

## 잘못된 사례
- 정족수 미달인데 결정 진행 — 결정 무효 + ASPICE 평가 시 GP 2.1 미흡.
- 반려 사유 "검토 부족" 만 기재 — 요청자가 보완 방향을 알 수 없음.
- 회의록을 일주일 후 작성·배포 — 구현 결정 지연, 추적성 약화.
- 이해 충돌 표기 누락 — CR 작성자가 본인 CR 의결에 참여한 사실이 가려짐.
