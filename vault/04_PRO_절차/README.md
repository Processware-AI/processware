---
type: folder-readme
folder: 04_PRO_절차
title: 04_PRO_절차 — 절차서(PRO) 산출물
updated: 2026-04-17
tags: [folder-readme, PRO]
---

# 04_PRO_절차 — 절차서(PRO)

## 역할
정책(POL)을 실제 **운영 흐름**으로 바꾼 관리 절차 문서.

## 특징
- 단계 중심
- 책임·승인 흐름 포함
- Mermaid flowchart 포함 권장
- 관련 업무지침(WI) 연결

## 파일명 규칙
```
PRO-{영역}-{###}_{이름}_v{버전}.md
```
예: `PRO-QMS-102_문서_개정_관리_절차_v1.0.md`

## Frontmatter 필수
`type`, `doc_id`, `title`, `version`, `owner`, `parent_policy`, `child_wi`, `standards`, `tier`(M|C|S), `status`

## 필수 섹션 (골든샘플 준수)
목적 / 범위 / RACI / Mermaid flowchart / 단계별 I/O / 연계 WI / KPI / 표준 매핑 / 출처 / 개정 이력

참조: [[GS-PRO-QMS-102_문서_개정_관리_절차]]

## 판단 기준
> "이 문서를 읽고 **업무가 어떤 순서로 관리되는가** 가 보이면 PRO"

## 생성 담당
Agent `process-designer`

## 포함 항목 표준
| 항목 | 설명 |
|---|---|
| 목적 | 절차의 존재 이유 |
| 적용 범위 | 포함/제외 경계 |
| RACI | 역할 책임 매트릭스 (Accountable 1인) |
| Mermaid flowchart | 분기·예외 경로 포함 |
| 단계별 I/O 표 | 각 단계 입력·출력 |
| 통제점·KPI | 5개 이내 |
| 표준 매핑 | Req-ID 역추적 |
| source_citation | _inputs 근거 |

## 무엇이 들어가지 않나
- 정책 수준 원칙 → `03_POL_정책/`
- 담당자 수행 상세 → `05_WI_업무지침/` (PRO는 흐름, WI는 실무)

## 관련 규약
- [[01_문서체계]] §2-2 PRO
- 3-Tier 분류: [[MOC_프로세스맵]]
