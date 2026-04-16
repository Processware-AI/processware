---
type: folder-readme
folder: 99_템플릿
title: 99_템플릿 — Obsidian Templates
updated: 2026-04-17
tags: [folder-readme, templates]
---

# 99_템플릿 — Obsidian Templates

## 역할
산출물 생성 시 사용하는 **표준 템플릿 모음**. Obsidian Templates 플러그인에서 이 폴더를 지정하면 메뉴에서 바로 삽입 가능.

## 수록 템플릿

### 8종 유형 템플릿 (T03~T10)
| 파일 | 유형 |
|---|---|
| [[T03_정책서_POL]] | POL |
| [[T04_절차서_PRO]] | PRO |
| [[T05_업무지침_WI]] | WI |
| [[T06_템플릿_TMP]] | TMP |
| [[T07_작성예시_EX]] | EX |
| [[T08_기록본_REC]] | REC |
| [[T09_매핑표_MAT]] | MAT |
| [[T10_참고자료_REF]] | REF |

### 표준 분석용 (T11~T13)
| 파일 | 용도 |
|---|---|
| [[T11_표준개요]] | 표준 편입 시 개요 |
| [[T12_요구사항분해]] | Req-ID 매트릭스 |
| [[T13_표준작업노트]] | 인간 가독 체크리스트 |

### 파이프라인·입력 (T14~T15)
| 파일 | 용도 |
|---|---|
| `T14_파이프라인상태.yaml` | `_state.yaml` 초기 생성용 |
| [[T15_입력문서_INP]] | PDF→MD 변환본 frontmatter |

### 골든 샘플
- [[_골든샘플/README]] — POL/PRO/WI 품질 하한선 참조

## Obsidian 설정
```
Settings → Core plugins → Templates
Templates folder location: 99_템플릿/
```
설정 후 `Cmd+P` → "Insert template" 로 삽입.

## 파일명 규칙
`T{번호}_{유형}.md` (표준 템플릿)
`GS-{유형}-{id}_{이름}.md` (골든 샘플)

## 관리 규칙
- 번호 부여는 한 번, 이후 불변
- 템플릿 변경은 **전 산출물 영향** → PCB 심의
- 새 유형 추가 시 `T{다음번호}_{새유형}.md`

## 관련 규약
- 유형 정의: [[01_문서체계]]
- 번호 규칙: [[02_문서번호체계]]
- 골든샘플 운영: [[_골든샘플/README]]
