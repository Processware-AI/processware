---
type: EX
doc_id: EX-CMMI-03-02-03-02
title: "Make/Buy/Reuse 분석서 작성예시"
version: "0.1"
owner: "Procurement / Chief Engineer"
parent_tmp: "[[TMP-CMMI-03-02-03-02_Make_Buy_Reuse_분석서]]"
standards: [CMMI-DEV-ML3-V1.3]
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
status: draft
created: 2026-05-11
updated: 2026-05-11
tags: [EX, CMMI, TS, sample]
---

# Make/Buy/Reuse 분석서 작성예시 (EX-CMMI-03-02-03-02)

> 원본 양식: [[TMP-CMMI-03-02-03-02_Make_Buy_Reuse_분석서]]

## 샘플 컨텍스트
"알파-MES v2" — 6개 컴포넌트 조달 전략.

## 1. 문서 정보 (샘플)
| 항목 | 예시값 |
|---|---|
| 문서번호 | MBR-2026-007 |
| 버전 | 1.0 |
| 프로젝트 | 알파-MES-v2 |
| 작성자 | 박OO (Procurement) + 이OO (Chief Eng) |
| 작성일 | 2026-07-12 |
| AVL 버전 | 2026-Q2 |
| 승인자 (PM) | 정OO |

## 2. 비교 표 (샘플)
| 컴포넌트 | Make | Buy | Reuse | 비용 | 일정 | 역량 | 리스크 | 결정 | 근거 | DAR ID |
|---|---|---|---|---|---|---|---|---|---|---|
| C-01 Gateway | 7 | 9 | 6 | Buy ↓ | Buy ↑ | Buy ↑ | M | **Buy** | Spring Cloud Gateway 채택 | - |
| C-02 작업지시 | 9 | 5 | 4 | Make ≈ | Make ↑ | Make ↑ | L | **Make** | 도메인 핵심 | - |
| C-03 분석기 | 8 | 6 | 5 | Make ≈ | Make ↑ | Make ↑ | M | **Make** | 도메인 핵심 | - |
| C-04 대시보드 | 7 | 6 | 8 | Reuse ↓ | Hybrid ↑ | Hybrid ↑ | L | **Hybrid (Reuse+Make)** | TS WI-01 ALT-D | DAR-2026-024 |
| C-05 저장소 | 6 | 9 | 5 | Buy ≈ | Buy ↑ | Buy ↑ | L | **Buy** | PG + S3 + HSM 표준 채택 | - |
| C-06 ERP 어댑터 | 8 | 7 | 4 | Make ↑ | Make ↑ | Make ↑ | M | **Make** | EDI 도메인 사내 보유 | - |

## 3. 결정 요약 (샘플)
| 결정 | 컴포넌트 수 | 비율(%) |
|---|---|---|
| Make | 3 (C-02, C-03, C-06) | 50 |
| Buy | 2 (C-01, C-05) | 33 |
| Reuse / Hybrid | 1 (C-04) | 17 |

## 4. 후속 조치 (샘플)
| 컴포넌트 | 결정 | 후속 행위 | 송부 ID | 책임자 | 마감 |
|---|---|---|---|---|---|
| C-01 | Buy | SAM (PRO-CMMI-02-04 WI-01) — Spring Cloud Gateway 라이선스 협상 | SAM-HOI-2026-031 | 박OO | 2026-07-25 |
| C-05 | Buy | SAM — PG·S3·HSM 통합 견적 | SAM-HOI-2026-032 | 박OO | 2026-07-25 |
| C-04 | Reuse | EPG/PAL 프레임워크 v3 사용 협약 | PAL-AGR-2026-014 | EPG | 2026-07-18 |
| C-02 | Make | 내부 일정 등록 (백엔드팀 8주) | - | C-02 Owner | 2026-07-15 |
| C-03 | Make | 내부 일정 등록 (데이터팀 7주) | - | C-03 Owner | 2026-07-15 |
| C-06 | Make | 내부 일정 등록 (통합팀 6주) | - | C-06 Owner | 2026-07-15 |

## 5. 결재 (샘플)
| 검토 | 승인 | 일자 |
|---|---|---|
| 이OO (Chief Eng), Legal 한OO | 정OO (PM) | 2026-07-13 |

## 작성 시 유의사항
- 4축(비용·일정·역량·리스크) 모두 기재 — 단순 점수만 적기 금지.
- Buy 결정은 SAM 인계 송부 ID 의무, Reuse 는 PAL 협약 ID 의무.
- 영향 큰 결정만 DAR — Hybrid 같은 복합 결정은 DAR 의무.

## 잘못된 작성 사례
> ❌ "Make 가 좋다" — 근거 없음
> ✅ "도메인 핵심 + 사내 역량 보유" 등 근거 명시

> ❌ SAM 인계 없이 Buy 진행
> ✅ SAM 송부 ID 명시 후 SAM PRO 진입
