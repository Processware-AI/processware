---
type: sources-root
title: 전처리 소스 파일
updated: 2026-05-05
tags: [sources, ingest]
---

# sources/

`/process-ingest` 의 입력 원본 파일 보관 폴더.

## 들어가는 것
- 국제표준 PDF (ISO·IEC·KS·ANSI 등)
- 국내 법령·고시·규정 PDF
- 해설서·가이드라인 DOCX·PDF
- 기존 조직 내부 문서 (DOCX·PPTX·XLSX)
- 표준 개정사항 delta 문서

## 들어가지 않는 것
- 텍스트·YAML·MD 파일 → `inputs/` 에 직접 배치
- ingest 완료된 정규화 파일 → `inputs/` 에 자동 생성됨

## 파일명 권장 규칙
```
{표준ID}_{버전}.pdf          예: ISO9001_2015.pdf
{표준ID}_{버전}_개정사항.pdf  예: ISO9001_2024_개정사항.pdf
{법규명}_{연도}.pdf           예: 개인정보보호법_2024.pdf
현_{문서명}_v{N}.docx        예: 현_품질매뉴얼_v3.docx
```

## 처리 방법
```
/process-ingest sources/ISO9001_2015.pdf --standard ISO9001 --version 2015
```

## 저작권·기밀
- 표준 원문: 저작권 주의 — 구매·라이선스 확인 후 배치
- 내부 문서: 조직 내부 자산 — 외부 공개 금지
- 개인정보·계약가·고객 목록 마스킹 필수

## git 정책
실제 파일은 .gitignore 제외, README 만 추적.
