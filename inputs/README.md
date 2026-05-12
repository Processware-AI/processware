---
type: inputs-root
title: 전사 입력자료 — 코어 vault 용
updated: 2026-05-13
tags: [inputs]
---

# 입력자료 (inputs/) — 코어 vault 전용

**코어 Processware vault** 구축을 위한 표준/법규/가이드 원본 자료. vault 밖에서 관리되며 클라이언트에게 제공되지 않는다.

> ⚠️ **본 디렉토리에 들어가지 않는 것**: RFP·발주문서·SoW 같은 1회성 사업 명세서. 이런 자료는 본 메인 repo 가 아니라 파생 프로덕트 `subproducts/rfp-to-proposal/inputs/` 영역으로 가야 한다.
> 상세: `../docs/architecture/derivative-products.md`

## 구조
```
inputs/
├── 01_표준원문/   ← ISO/IEC/KS 표준 원문 (조직이 항상 따르는 영속 기준)
├── 02_법규/       ← 관련 법령·고시·규정
├── 03_해설서/     ← 해설서·가이드·주석
├── 04_AsIs/       ← 기존 조직 내부 표준 자산 (현 품질매뉴얼·기존 절차서 등) + 차원 4 개정 큐 파일
└── 05_산업가이드/ ← 업종 공통 프레임워크 (NIST CSF·CIS Controls·OWASP 등)
```

## 본 입력자료의 본질

본 메인 repo 의 입력은 **조직이 모든 사업에서 항상 준수하는 영속 기준** 만 받는다:

| 적합 ✅ | 부적합 ❌ |
|---|---|
| 국제표준 (ISO 9001, ISO 27001, CMMI 등) | 발주처 RFP / 제안요청서 |
| 국내 법규 (개인정보보호법, 전자금융감독규정) | 1회성 사업 SoW (Statement of Work) |
| 기존 조직 자산 (품질매뉴얼, 기존 절차서) | 고객 입찰 명세서 |
| 산업 가이드 (NIST CSF, COBIT) | 1회 컨설팅 보고서 |

부적합 자료는 파생 ① (`subproducts/rfp-to-proposal/`) 의 입력 영역으로 분리한다.

## 참조 우선순위
`standard-analyzer` 스캔 순서: 01 → 02 → 05 → 03 → 04 (AsIs 마지막, 맥락 보완)

## 저작권·기밀
- 표준 원문: 저작권 주의, git 제외
- AsIs: 조직 내부 자산, 외부 공개 금지
- 개인정보·계약가·고객 목록 마스킹 필수

## git 정책
실제 파일은 .gitignore 제외, README 와 ingest 정규화 산출물(YAML/MD) 만 추적.
