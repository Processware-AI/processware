---
type: inputs-category
category: "02_법규"
title: 02_법규 — 국내 법령·규제
updated: 2026-04-17
tags: [inputs, category, law]
---

# 02_법규

## 들어가는 것
- 개인정보보호법, 산업안전보건법, 전자금융감독규정 등 **한국 법령**
- 금감원·식약처·KISA 등 **공공기관 고시·가이드라인**
- ISMS-P 인증기준, 디지털의료제품법 등 **인증 관련 공공 문서**

## 예시
```
02_법규/
├── 개인정보보호법.pdf
├── 개인정보보호법_조항별/         ← MD 변환본 (권장)
│   ├── MOC_PIPA.md
│   ├── 제1장_총칙.md
│   └── 제3장_개인정보의_처리.md
├── 산업안전보건법_발췌.md
└── ISMS-P_인증기준_2024.pdf
```

## 들어가지 않는 것
- 해외 규제 (GDPR 등) → `05_산업가이드/`
- 인증기관 해설 → `03_해설서/`
- 국제 표준 → `01_표준원문/`

## 저작권 (유리함)
- **한국 법령은 공공저작물** → 원문 그대로 인용 가능
- 공공기관 가이드라인도 대부분 공개 허용 (발행처 라이선스 확인)
- `content_mode: verbatim` MD 변환도 OK

## 주요 출처
| 유형 | 출처 |
|---|---|
| 법령 전문 | [법제처 law.go.kr](https://www.law.go.kr) |
| 개인정보 | [개인정보보호위원회](https://www.pipc.go.kr) |
| 정보보호 | [KISA](https://www.kisa.or.kr), [ISMS-P](https://isms.kisa.or.kr) |
| 금융 | [금감원](https://www.fss.or.kr) |
| 의료기기 | [식약처](https://www.mfds.go.kr) |

## 변환 방법
- `pandoc input.pdf -o output.md` (공공저작물이라 verbatim OK)
- [marker](https://github.com/VikParuchuri/marker) — 표·레이아웃 보존 우수
- 수동 발췌 — 핵심 조항만 선별

## 에이전트 참조 우선순위
**최상위**. 의무(shall) 도출의 1차 근거. 법규 없으면 LLM 추정에 의존하므로 반드시 배치 권장.

## 관련 규약
- [[05_입력자료_규칙]] §5 출처 우선순위
