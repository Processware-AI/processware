---
type: folder-readme
folder: 02_표준
title: 02_표준 — 표준별 작업 공간
updated: 2026-04-17
tags: [folder-readme, workspace]
---

# 02_표준 — 표준별 작업 공간

## 역할
각 표준 편입 시 **분석·작업·입력자료를 모으는 워크스페이스**. 확정 산출물(POL/PRO/WI 등)은 여기에 두지 않고 각 유형 폴더로 발행.

## 서브폴더 패턴
표준 1건 = 폴더 1개. 폴더명 = 표준 코드.

```
02_표준/
├── _scaffold/                        ← 새 표준 편입용 템플릿 (복사하여 사용)
│   ├── README.md
│   └── _inputs/
│       ├── README.md
│       ├── 01_표준원문/README.md
│       ├── 02_법규/README.md
│       ├── 03_해설서/README.md
│       ├── 04_AsIs/README.md
│       └── 05_산업가이드/README.md
├── ISO9001/                          ← scaffold 복사해서 시작
│   ├── 00_ISO9001_표준개요.md       ← standard-analyzer 생성
│   ├── 01_ISO9001_요구사항분해.md   ← standard-analyzer 생성
│   ├── 02_작업노트.md                ← 인간 가독 체크리스트
│   ├── _state.yaml                   ← 파이프라인 상태 (gitignored)
│   ├── 99_QA리포트_*.md              ← qa-reviewer 생성 (gitignored)
│   └── _inputs/
│       ├── 01_표준원문/
│       ├── 02_법규/
│       ├── 03_해설서/
│       ├── 04_AsIs/
│       ├── 05_산업가이드/
│       └── README.md
├── ISO27001/
│   └── ...
```

## 빠른 시작 (새 표준 편입)
```bash
cd vault/02_표준/
cp -R _scaffold ISO27001        # 5개 카테고리 폴더 + README 즉시 복사
# 그 다음 각 카테고리에 파일 투하
claude
> /build-standard ISO27001
```
또는 `_scaffold/` 없이 바로 `/build-standard` 실행하면 `standard-analyzer` 가 자동 복사.

## 무엇이 들어가나
- 표준 개요 (00_*)
- 요구사항 분해 (01_*)
- 작업노트 (02_*)
- 실행 상태 (_state.yaml)
- QA 리포트 (99_QA리포트_*)
- 고객/표준 입력자료 (_inputs/)

## 무엇이 들어가지 않나
- 확정 POL/PRO/WI/TMP/EX 등 — 각 유형 폴더로
- 통합 관리대장 — `90_MAT_통합매핑/` 로

## 사용 흐름
```
1. 수동: mkdir 02_표준/{표준코드}/_inputs + 입력자료 배치
2. 자동: /build-standard {표준코드} 실행
3. 결과: 00_*, 01_*, 02_* 자동 생성 + 유형 폴더에 산출물 발행
```

## git 제외 (`.gitignore`)
- `_inputs/` 실파일 (README.md 만 추적)
- `_state*.yaml` (실행 인스턴스)
- `99_QA리포트_*.md` (실행 인스턴스)
- `02_작업노트.md` (인스턴스별 로그)

## 관련 규약
- 입력자료: [[05_입력자료_규칙]]
- 상태 관리: [[06_파이프라인_상태규약]]
- 문서 번호: [[02_문서번호체계]]
