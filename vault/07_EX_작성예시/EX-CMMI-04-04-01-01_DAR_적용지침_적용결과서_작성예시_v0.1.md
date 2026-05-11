---
type: EX
doc_id: EX-CMMI-04-04-01-01
title: "DAR 적용 지침 적용 결과서 작성예시"
version: "0.1"
owner: "Decision Facilitator"
parent_tmp: "[[TMP-CMMI-04-04-01-01_DAR_적용지침_적용결과서]]"
standards: [CMMI-DEV-ML3-V1.3]
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
status: draft
created: 2026-05-11
updated: 2026-05-11
tags: [EX, CMMI, DAR, sample]
---

# DAR 적용 지침 적용 결과서 작성예시 (EX-CMMI-04-04-01-01)

> 원본 양식: [[TMP-CMMI-04-04-01-01_DAR_적용지침_적용결과서]]

> ⚠️ 본 문서는 **교육·가이드용 샘플**.

## 샘플 컨텍스트
"**NEXT 플랫폼 v3.0 메시지 브로커 솔루션 선정**" (TS SP1.1 트리거).

## 1. 사안 정보 (샘플)
| 항목 | 내용 |
|---|---|
| 사안 ID | DAR-2026-007 |
| 사안 명·요약 | NEXT3 메시지 브로커 솔루션 선정 — 신규 도입 |
| 트리거 PA·SP | TS SP1.1 (솔루션 선정) |
| 식별 일자 | 2026-04-10 |
| Decision Owner | 정OO (Lead Architect) |
| Decision Facilitator | 한OO (EPG Lead) |

## 2. 영향도 평가 (샘플)
| 요인 | 수준 | 사유 |
|---|---|---|
| 비용 | H | 3년 TCO 5억원 추정 |
| 가역성 | L | 한번 채택 시 마이그레이션 비용 큼 |
| 이해관계자 다양성 | H | 개발·운영·SRE·보안·고객 |
| 리스크 | M | 신기술 채택 가능성 |

## 3. DAR 적용 결정 (샘플)
| 항목 | 내용 |
|---|---|
| 결정 | 적용 |
| 근거 | 비용 H + 가역성 L + 이해관계자 H → 영향도 임계값 초과. 조직 지침 "5천만원 이상 + 비가역 결정" 의무 적용 트리거 부합 |
| 결정자 | 한OO (Facilitator) + 정OO (Owner) |

## 4. 결재 (샘플)
| 검토 | 승인 | 일자 |
|---|---|---|
| 정OO (Decision Owner) | 최OO (CTO — Approver) | 2026-04-11 |

## 작성 시 유의사항
- 영향도는 정성 평가지만 근거는 정량 또는 비교 가능한 형태로.
- 조직 지침이 명시한 의무 적용 사안은 결정 단계 생략 가능 — 근거 명기.

## 잘못된 작성 사례
> ❌ "큰 의사결정이라 DAR 적용" 식 모호한 근거
> ✅ "TCO ≥5억, 가역성 L" 등 정량·지침 부합 명시
