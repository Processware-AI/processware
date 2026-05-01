---
type: inputs-category
category: "01_표준원문"
title: 01_표준원문 — 표준 원본 자료
updated: 2026-04-17
tags: [inputs, category, standard-original]
---

# 01_표준원문

## 들어가는 것
- ISO / IEC 표준 원본 PDF (라이선스 보유 시)
- KS 표준 국문본 (한국표준협회 구매)
- 표준 원본을 MD 로 변환한 서브볼트 (같은 이름 폴더)

## 예시
```
01_표준원문/
├── ISO9001_2015.pdf              ← 원본 (대조용)
└── ISO9001_2015/                  ← MD 변환 서브볼트 (권장)
    ├── MOC_ISO9001.md
    ├── 04_조직_상황.md
    ├── 07_지원/
    │   └── 07.5_문서화된_정보.md
    └── ...
```

## 들어가지 않는 것
- 공공 법규 → `02_법규/`
- 인증기관 해설서 → `03_해설서/`
- 고객사 내부 문서 → `04_AsIs/`

## 저작권 주의 (CRITICAL)
- **ISO/IEC 원본은 유료·저작권 보호**. 공개 repo 에 업로드 금지
- `.gitignore` 에 의해 이 폴더 자체는 git 추적 제외됨 (README 만 추적)
- 고객에게 납품하는 산출물에 **원문 직접 복사 금지** (paraphrase 만)
- MD 변환 시 frontmatter `content_mode`:
  - `verbatim` — 원문 그대로 추출 → PDF 와 동일 저작권 취급
  - `paraphrase` — 요지 재작성 → 조항번호와 함께 인용 가능
  - `summary` — 핵심 1~2줄 요약 → 가장 안전

## 변환 방법
| 대상 | 권장 |
|---|---|
| ISO/IEC 원문 | 수동 `paraphrase/summary` MD (시간 투자 1회) |
| KS 표준 | pandoc 또는 marker 로 변환 후 라이선스 확인 |

## 에이전트 참조 우선순위
`02_법규` 다음, `03_해설서` 이전. 변환 MD 가 있으면 **PDF 원본보다 우선**.

## 관련 규약
- [[05_입력자료_규칙]] §10 하이브리드 구조
- [[T15_입력문서_INP]] — 변환 MD frontmatter 템플릿
