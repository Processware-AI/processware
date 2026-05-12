---
type: inputs-category
category: "04_AsIs"
title: 기존 조직 표준 자산 + 개정 큐
updated: 2026-05-13
---
# 04_AsIs — 기존 조직 표준 자산

> ⚠️ **본 카테고리에 들어가지 않는 것**: RFP·발주문서·SoW 등 외부에서 받은 1회성 사업 명세서.
> 이런 자료는 파생 프로덕트 `subproducts/rfp-to-proposal/inputs/` 로 가야 한다.

## 조직 기존 자산
조직이 **현재 사용 중이거나 과거에 사용한 표준 자산** — 새 표준 빌드 시 baseline 또는 보완 컨텍스트로 활용.

예시:
- 현_품질매뉴얼_v3.pdf, 조직도_2026.png, 기존_문서관리규정.docx
- 과거 심사 리포트, 내부 감사 보고서
- 기존 운영 절차서, 점검 체크리스트

## 개정 큐 파일
차원 4 (Act) 가 작성한 개정 지시 파일.
파일명: `queue-q{hex}.md`
`/process-plan` 재빌드 시 자동 참조.

## 부적합 자료 — 파생 프로덕트로 분리

| 자료 유형 | 본 카테고리? | 정상 위치 |
|---|---|---|
| 현 품질매뉴얼·기존 절차서 (조직 영속 자산) | ✅ Yes | `inputs/04_AsIs/{name}/` (여기) |
| 발주처 RFP (Request for Proposal) | ❌ No | `subproducts/rfp-to-proposal/sources/` |
| 사업별 SoW (Statement of Work) | ❌ No | `subproducts/rfp-to-proposal/sources/` |
| 고객 입찰 명세서·검수 체크리스트 | ❌ No | `subproducts/rfp-to-proposal/sources/` |

근거: 본 카테고리는 **"조직이 항상 따르는 영속 기준"** 만 받는다. RFP/SoW 는 1회성 사업 컨텍스트이므로 vault 의 표준 자산이 되어선 안 됨.
상세: `../../docs/architecture/derivative-products.md` §6

## 기밀 주의
내부 자산 — 외부 공개 금지. 개인정보·계약가 마스킹 필수.
