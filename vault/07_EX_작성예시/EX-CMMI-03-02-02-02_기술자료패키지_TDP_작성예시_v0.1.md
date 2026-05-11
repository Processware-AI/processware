---
type: EX
doc_id: EX-CMMI-03-02-02-02
title: "기술자료패키지(TDP) 작성예시"
version: "0.1"
owner: "Lead Architect"
parent_tmp: "[[TMP-CMMI-03-02-02-02_기술자료패키지_TDP]]"
standards: [CMMI-DEV-ML3-V1.3]
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
status: draft
created: 2026-05-11
updated: 2026-05-11
tags: [EX, CMMI, TS, sample]
---

# 기술자료패키지(TDP) 작성예시 (EX-CMMI-03-02-02-02)

> 원본 양식: [[TMP-CMMI-03-02-02-02_기술자료패키지_TDP]]

## 샘플 컨텍스트
"알파-MES v2" Phase 1 TDP — SW only (HW 없음).

## 1. 문서 정보 (샘플)
| 항목 | 예시값 |
|---|---|
| 문서번호 | TDP-2026-007 |
| 버전 | 1.0 |
| 프로젝트 | 알파-MES-v2 Phase 1 |
| TDP 책임자 | 한OO (Architect) |
| 베이스라인 ID | CM-BL-TDP-2026-007 |
| 등록 일자 | 2026-07-01 |
| 승인자 | 정OO (PM) |

## 2. TDP 항목 인덱스 (샘플)
| 항목 | 문서ID | 버전 | 상태 | 사유 | Owner |
|---|---|---|---|---|---|
| 제품·컴포넌트 설계서 | DES-2026-007 | 1.0 | 작성 | - | Architect |
| 인터페이스 명세서 (ICD) | ICD-2026-007 | 1.0 | 작성 (Draft, 다음 WI) | TS WI-03 산출 예정 | Architect |
| 재료·부품 목록 (BOM) | - | - | **N/A** | SW only 프로젝트 (HW 없음) | - |
| 시험 명세 | TEST-2026-007 | 0.9 | 작성 (Draft) | VER WI-01 와 공동 작성 중 | VER Lead |
| 운영 한계·조건 | OPS-2026-007 | 1.0 | 작성 | - | DevOps |
| 사용자/운영/유지보수 매뉴얼 골격 | DOC-2026-007 | 0.5 | 연기 | TS WI-04 산출 (구현 후) | Doc Writer |
| 검증 결과 인덱스 | - | - | 연기 | VER 수행 후 산출 | VER Lead |
| Make/Buy/Reuse 분석서 | MBR-2026-007 | - | 작성 (Draft, 다음 WI) | TS WI-03 산출 예정 | Procurement |

## 3. CM 베이스라인 등록 (샘플)
| 항목 | 내용 |
|---|---|
| CM 시스템 | GitLab + DOORS Next |
| Baseline ID | CM-BL-TDP-2026-007 |
| 등록 일자 | 2026-07-01 |
| CM Manager | 박OO |

## 4. 변경 관리 규칙 (샘플)
| 항목 | 규칙 |
|---|---|
| 변경 신청 방법 | GitLab MR + CM 변경요청 CR 동시 |
| 영향 평가 책임 | TS Lead + 영향 받는 컴포넌트 Owner |
| 승인자 (소규모) | TS Lead |
| 승인자 (대규모) | PM (정OO) — 일정·비용 ±5% 초과 |

## 5. 결재 (샘플)
| 검토 | 승인 | 일자 |
|---|---|---|
| 박OO (CM), 이OO (Chief Eng) | 정OO (PM) | 2026-07-01 |

## 작성 시 유의사항
- N/A 항목은 사유 의무 — 묵시 누락 금지.
- 연기 항목은 산출 WI/마일스톤 명시.
- TDP 자체는 인덱스 — 본문은 각 문서ID 참조.

## 잘못된 작성 사례
> ❌ HW 없는데 BOM 빈칸 (사유 미상)
> ✅ "N/A — SW only" 명시

> ❌ TDP 본문에 설계 내용 통째로 복사
> ✅ 인덱스 형식만 유지 (단일 출처 원칙)
