---
type: REF
doc_id: "REF-002"
title: "EU MDR 사이버보안 요구 요약 (Regulation (EU) 2017/745 Annex I)"
version: "0.1"
source: "Regulation (EU) 2017/745 (MDR) Annex I §17 + MDCG 2019-16 (Guidance on Cybersecurity for medical devices)"
source_date: "MDR 2017-05-05 / MDCG 2019-16 rev.1 2020-07"
author: "European Commission / Medical Device Coordination Group (MDCG)"
status: draft
related_standard: "IEC 81001-5-1:2021 (MDCS)"
created: 2026-06-18
updated: 2026-06-18
tags: [REF, MDCS, EU_MDR, cybersecurity, regulatory]
source_citation:
  - type: llm_inference
    locator: "MDR Annex I §17.2, §17.4 / MDCG 2019-16 — 도메인 지식 기반 요지"
    retrieved_at: "2026-06-18"
    license: "EU 공식 규정·가이던스. 원문 미투입 — 요지만 정리, 인용 시 EUR-Lex/MDCG 원문 대조 권장"
    paraphrase_only: true
---

# EU MDR 사이버보안 요구 요약 (REF-002)

> 원문 출처: Regulation (EU) 2017/745 (Medical Device Regulation) Annex I, 일반 안전·성능 요구사항(GSPR) §17; MDCG 2019-16 Guidance on Cybersecurity
> 최종 확인일: 2026-06-18
> ⚠️ **inputs 미제공 — LLM 추정 기반 요지**. 실제 EUR-Lex 원문·MDCG 가이던스 미투입. 인용 전 원문 대조 필수.

## 요약
EU MDR Annex I GSPR §17(전자 프로그래밍 시스템·SW) 은 SW 를 포함하는 기기가 최신 기술 수준(state of the art)에 따라 신뢰성·반복성·성능을 보장하도록 요구하며, §17.2/§17.4 는 IT 환경 보안·접근통제·정보보안 위험 최소화를 명시한다. MDCG 2019-16 은 이를 보안 설계·검증·시판후 관리로 구체화한다.

## 핵심 요구사항 (요지)
| MDR/MDCG 영역 | 요지 | IEC 81001-5-1 정합 |
|---|---|---|
| Annex I §17.2 | IT 환경·플랫폼 보안, 위험 최소화 설계 | §5.1.2, §5.3, §7.x |
| Annex I §17.4 | 무단접근 방지 위한 최소 IT/IT보안 요건 명시 | §5.4.3, §7.1.2 (보안 맥락) |
| MDCG 2019-16 시판전 | 보안 위험관리·위협 모델·보안 검증 | §4.2, §7.2, §5.7 |
| MDCG 2019-16 시판후 | 취약점 처리·조정 공개·정보 제공 | §4.1.7, Clause 6, §9.x |
| 보안 by design | 방어심층화·최소권한 | §5.3.1, §5.3.2 |

## 적용 영향
- IEC 81001-5-1 적용([[적용요건]])은 MDCG 2019-16 이 기대하는 "secure lifecycle" 의 인정 표준으로 활용 가능.
- IEC 62443-4-1 과 함께 EU 조화규격 후보로 논의되는 표준이며, CE 적합성 평가 시 보조 증적으로 사용 가능 `[확인 필요]`.

## 관련 내부 문서
- [[적용요건]] (REQ-iec81001-5-1)
- [[MAT-002_규제요구사항_대조표]]

## 변경 알림
- MDR/MDCG 개정 시 본 REF 버전 업 + MAT-002 동기화.
