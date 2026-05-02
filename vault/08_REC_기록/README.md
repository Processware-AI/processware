---
type: folder-readme
folder: 08_REC_기록
title: 08_REC_기록 — 실제 수행 기록(REC)
updated: 2026-04-17
tags: [folder-readme, REC]
---

# 08_REC_기록 — 기록본(REC)

## 역할
업무 수행 결과 실제로 생성된 **증빙 문서**. 심사증적 역할.

## 중요
**이 폴더는 `/plan-process` 파이프라인에서 생성하지 않습니다.**
- 편입 단계(하네스 실행)에는 파일 없음
- **운영 단계** 에서 실무자가 TMP 를 복사해 작성하며 쌓임

## 파일명 규칙
```
REC-{기능}-{YYYY}-{###}_{이름}.md
```
예: `REC-IR-2026-001_침해사고_신고서.md`

## Frontmatter 필수
`type: REC`, `doc_id`, `title`, `source_tmp`, `related_wi`, `event_id`, `event_date`, `author`, `approver`, `retention`, `status`(final/archived)

## 특징
- 특정 사건·활동과 연결 (event_id)
- 날짜·담당자·승인 이력 존재
- **수정 통제 필요** (재발행 시 신규 REC 생성, 기존 유지)
- 보관기간 준수 (frontmatter `retention`)

## 금지사항
- ❌ 이 폴더에 TMP(빈 양식) 두지 않기
- ❌ 이 폴더에 EX(예시) 두지 않기
- ❌ 개인정보·기밀 마스킹 없이 커밋

## git 제외
`.gitignore` 에서 제외 — 운영 데이터는 로컬/EDMS 관리. 필요 시 별도 저장소.

## 판단 기준
> "실제 운영 중 작성된 문서라면 REC"

## 관련 폴더
- 양식: `06_TMP_템플릿/`
- 예시: `07_EX_작성예시/`
- 증적 인덱스: [[MAT-005_심사증적_인덱스]]
