---
type: inputs-category
category: "05_산업가이드"
title: 05_산업가이드 — 업종·국제 모범사례
updated: 2026-04-17
tags: [inputs, category, industry]
---

# 05_산업가이드

## 들어가는 것
- NIST (SP 800-53, CSF 2.0 등) — 미국 국립표준
- ENISA — EU 사이버보안 가이드
- ISACA (CISA·COBIT) — IT 거버넌스
- OECD·ITU 가이드
- **업종별 best practice** 문서 (의료기기·금융·AI 등)
- GDPR, HIPAA 등 해외 규제 참고

## 예시
```
05_산업가이드/
├── NIST_SP_800-53_rev5.pdf
├── NIST_CSF_2.0.pdf
├── NIST_CSF_2.0/              ← MD 변환 (공개자료)
│   ├── MOC_CSF.md
│   └── 5_functions.md
├── ENISA_cybersecurity_guide_2025.pdf
├── GDPR_한글_요약.md
└── AI_거버넌스_OECD.pdf
```

## 들어가지 않는 것
- 국내 법규 → `02_법규/`
- 인증기관 해설 (KFQ·BSI 등 국내) → `03_해설서/`
- 고객사 내부 문서 → `04_AsIs/`

## 저작권 (주로 유리)
- **NIST·ENISA·OECD**: 대부분 공개 배포 허용 (저작권 표기 필요)
- **ISACA 등 회원제**: 라이선스 확인 필요
- **해외 표준 원본**: ISO 와 동일 유료 취급 가능

## 활용 가치
- 국내 표준·법규에 없는 **심화 통제** 보완
- 글로벌 고객 대응 시 **해외 규제 매핑**
- AI·보안 등 **빠르게 진화하는 영역**의 최신 모범사례
- 업종 특화 요구(의료기기 SW, 금융 API, AI 거버넌스)

## 주요 출처
| 소스 | URL |
|---|---|
| NIST | [nvlpubs.nist.gov](https://nvlpubs.nist.gov) |
| ENISA | [enisa.europa.eu](https://www.enisa.europa.eu) |
| ISO/IEC JTC 1 | [jtc1info.org](https://www.jtc1info.org) |
| CIS Controls | [cisecurity.org](https://www.cisecurity.org) |

## 변환 권장
- 공개 자료는 `pandoc`/`marker` 로 verbatim MD 허용
- 핵심만 paraphrase summary 도 OK
- 큰 문서는 조항별 분할

## 에이전트 참조 우선순위
`03_해설서` 수준. **IMS 통합(multi-standard)** 시 교차 참조용으로 유용.

## 관련 규약
- [[05_입력자료_규칙]] §5 출처 우선순위
