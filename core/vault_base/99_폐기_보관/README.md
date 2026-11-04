---
type: folder-readme
folder: 99_폐기_보관
title: 99_폐기_보관 — 만료·폐지 문서 아카이브
updated: 2026-04-17
tags: [folder-readme, archive]
---

# 99_폐기_보관 — 아카이브

## 역할
만료·폐지·superseded 된 문서의 **보존 공간**. 이력·감사 대응 목적.

## 이동 규칙
다음 상태의 문서를 이 폴더로 이동:
- `status: superseded` — 신규 문서로 대체됨
- `status: obsolete` — 더 이상 사용하지 않음
- `status: expired` — 보관기간 경과 (폐기 예정)

## 이동 방법
**개정**(경미/중대)은 이동하지 않음. 버전만 증분.
**전면 재작성 또는 폐지** 시에만 이동.

상세 절차: [[GS-WI-102-04_개정_및_버전관리]] §7.2

## 파일명
이동 후 원본 파일명 유지 + 이동일 suffix:
```
{원본파일명}_archived_{YYYYMMDD}.md
```
예: `POL-QMS-002_문서관리_정책_v1.0_archived_20260417.md`

## Frontmatter 갱신
이동 시 frontmatter 수정:
- `status: archived`
- `archived_at: <YYYYMMDD>`
- `superseded_by: [[신규문서]]` (있으면)
- `retention_end: <YYYYMMDD>` (있으면)

## 보관 기간
각 문서의 `retention` 필드 준수. 일반적으로:
- 정책/절차/업무지침: 최종 사용 후 5년
- 기록(REC): 법정 보존기간 (3~10년, 유형별)
- 참고자료(REF): 보관 의무 없음 (자유)

## 폐기 (최종)
보관기간 종료 후 `PRO-QMS-103_문서_폐기_관리_절차` 에 따라 폐기. 폐기 기록은 MAT-001 에 남김.

## 주의
- 개인정보·기밀 포함 문서는 별도 보안 아카이브 (EDMS)
- git 에 포함되어 공개 가능성이 있다면 **마스킹 후 이동**
