---
type: REF
doc_id: "REF-001"
title: "FDA Premarket Cybersecurity 가이던스 요약 (의료기기 사이버보안)"
version: "0.1"
source: "US FDA — Cybersecurity in Medical Devices: Quality System Considerations and Content of Premarket Submissions (Guidance for Industry and FDA Staff)"
source_date: "2023-09 (final guidance)"
author: "U.S. Food and Drug Administration (CDRH)"
status: draft
related_standard: "IEC 81001-5-1:2021 (MDCS)"
created: 2026-06-18
updated: 2026-06-18
tags: [REF, MDCS, FDA, cybersecurity, regulatory]
source_citation:
  - type: llm_inference
    locator: "FDA Premarket Cybersecurity Guidance (2023) — 도메인 지식 기반 요지 정리"
    retrieved_at: "2026-06-18"
    license: "공공기관 발행 가이던스(미국). 원문 미투입 — 요지만 정리, 인용 시 원문 대조 권장"
    paraphrase_only: true
---

# FDA Premarket Cybersecurity 가이던스 요약 (REF-001)

> 원문 출처: US FDA, "Cybersecurity in Medical Devices: Quality System Considerations and Content of Premarket Submissions" (2023)
> 최종 확인일: 2026-06-18
> ⚠️ **inputs 미제공 — LLM 추정 기반 요지**. `inputs/02_법규` 및 `inputs/05_산업가이드` 에 실제 가이던스 원문이 없어 도메인 지식으로 보완함. 인용·근거 채택 전 FDA 원문(공식 PDF) 대조 필수.

## 요약
FDA 는 2023 년 식약 현대화법(FD&C Act §524B, Omnibus 2023)에 근거하여 "사이버보안 기기(cyber device)" 의 시판전 제출 시 사이버보안 정보를 의무화했다. 핵심은 **Secure Product Development Framework(SPDF)** 채택, **SBOM** 제출, 취약점 관리·패치 계획 수립이다. IEC 81001-5-1 의 제품 수명주기 보안 활동은 FDA 가 기대하는 SPDF 의 인정 가능한 구현 방안 중 하나로 정합된다.

## 핵심 요구사항 (요지)
| 영역 | 요지 | IEC 81001-5-1 정합 |
|---|---|---|
| SPDF | 설계 단계부터 보안 내재화한 개발 프레임워크 | Clause 5 전반 (개발 보안 활동) |
| 위협 모델링 | 시스템 수준 위협 모델 제출 | §7.2 (위협 모델) |
| SBOM | SW 구성요소 목록 제출 + 취약점 관리 | §4.3, §8-REQ-002 (SBOM/구성요소) |
| 보안 시험 | 취약점·침투 시험 증적 | §5.7.3, §5.7.4 |
| 시판후 관리 | 취약점 모니터링·조정 공개·패치 계획 | Clause 6, §4.1.7, §9.x |
| 라벨링 | 사용자 대상 보안 문서 | §5.8.2 동반문서 |

## 적용 영향
- IEC 81001-5-1 적용요건([[적용요건]])이 충족되면 FDA SPDF 기대치 상당 부분을 커버할 수 있음(완전 일치 아님 — FDA 고유 제출 양식·라벨링 별도).
- §524B "cyber device" 해당 여부는 제품별 판정 필요 `[확인 필요]`.

## 관련 내부 문서
- [[적용요건]] (REQ-iec81001-5-1)
- [[MAT-002_규제요구사항_대조표]]

## 변경 알림
- FDA 가이던스 개정 시 본 REF 버전 업 + MAT-002 동기화.
