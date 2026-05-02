---
type: scaffold
title: _scaffold — 새 표준 편입용 템플릿
updated: 2026-04-17
tags: [scaffold, template]
---

# _scaffold — 새 표준 편입 스캐폴드

## 역할
새 표준을 편입할 때 **복사해서 시작하는 템플릿 폴더**. 매번 `_inputs/` 하위 5개 카테고리 폴더를 수동으로 만들 필요 없음.

## 사용법

### 방법 A: 수동 복사 (권장 — 빠름)
```bash
cd /Users/dongseok/MyProjects/Standard_Process/vault/02_표준/
cp -R _scaffold ISO27001
# → ISO27001/_inputs/ 아래 5개 카테고리 폴더가 즉시 생성됨
```

이후 각 카테고리 폴더에 파일을 투하하고:
```
claude
> /plan-process ISO27001
```

### 방법 B: 자동 (에이전트에 위임)
```
/plan-process ISO27001
```
`standard-analyzer` 가 `_inputs/` 없음을 감지하면 이 scaffold 를 자동 복사.

## 포함 구조
```
_scaffold/
├── README.md                       ← 이 문서
└── _inputs/
    ├── README.md                   ← 입력자료 인벤토리 템플릿
    ├── 01_표준원문/README.md      ← 표준 원본 안내
    ├── 02_법규/README.md           ← 법규 안내
    ├── 03_해설서/README.md         ← 해설서 안내
    ├── 04_AsIs/README.md           ← 고객사 As-Is 안내
    └── 05_산업가이드/README.md    ← 산업 가이드 안내
```

## 커스터마이즈
- 조직 특성에 맞게 이 scaffold 를 수정해도 OK (예: 업종 특화 카테고리 추가)
- scaffold 변경은 **이후 복사되는 모든 표준에 영향**
- 기존 표준 폴더(ISO9001 등)에는 소급 적용되지 않음

## 업데이트 시 주의
scaffold 를 크게 바꿀 때:
1. 기존 편입된 표준 폴더들도 같이 마이그레이션할지 결정
2. `05_입력자료_규칙.md` 와 정합성 확인
3. `standard-analyzer` 프롬프트의 자동 복사 로직이 깨지지 않는지 확인

## 관련 규약
- [[05_입력자료_규칙]] §2 폴더 구조, §10 하이브리드 구조
- [[02_표준/README]] — 표준별 작업 공간 사용법
