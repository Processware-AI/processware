---
type: folder-readme
folder: 03_POL_정책
title: 03_POL_정책 — 정책서(POL) 산출물
updated: 2026-04-17
tags: [folder-readme, POL]
---

# 03_POL_정책 — 정책서(POL)

## 역할
조직이 **무엇을 원칙으로 삼고 어떤 책임체계로 운영할지** 를 정의하는 상위 문서.

## 특징
- 방향성 중심
- "무엇을 해야 하는가" 중심
- 세부 수행 방법은 여기 없음 (→ PRO/WI)
- 경영책임·적용범위·준수 원칙 포함

## 파일명 규칙
```
POL-{영역}-{###}_{이름}_v{버전}.md
```
예: `POL-QMS-001_품질방침_v1.0.md`

영역 코드 (QMS/ISMS/PIMS 등): [[02_문서번호체계]] §영역 코드 표

## Frontmatter 필수 필드
`type`, `doc_id`, `title`, `version`, `owner`, `reviewer`, `approver`, `scope`, `child_pro`, `standards`, `status`

## 필수 섹션 (골든샘플 준수)
목적 / 범위 / 정책 원칙(5개 이내) / 역할과 책임 / 준수 기준 / 관련 하위 PRO / 표준 매핑 / 출처 / 개정 이력

참조: [[GS-POL-QMS-002_문서화된정보_관리_정책]]

## 생성 담당
Agent `process-designer` — `/build-process` 파이프라인의 Design phase

## 판단 기준
> "이 문서를 읽고 **우리 조직은 어떤 원칙으로 관리하는가** 가 보이면 POL"

## 무엇이 들어가지 않나
- 세부 수행 절차 → `04_PRO_절차/`
- 실무 단계 → `05_WI_업무지침/`
- 양식 → `06_TMP_템플릿/`

## 관련 규약
- [[01_문서체계]] §8종 유형
- [[표준프로세스_구성원칙]]
