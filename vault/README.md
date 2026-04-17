---
type: vault-overview
title: Standard_Process Obsidian Vault
updated: 2026-04-17
tags: [vault, overview]
---

# Standard_Process Obsidian Vault

Obsidian 에서 이 폴더를 **Open folder as vault** 로 열어 사용.

## 폴더 구조
| 경로 | 역할 | 주 내용 |
|---|---|---|
| `00_MOC/` | Map of Content (인덱스) | MOC_전체표준·프로세스맵·추적성 |
| `00_공통관리/` | 체계 기준·규약 | 문서체계·번호체계·용어집·입력자료·파이프라인 상태 |
| `01_구성원칙/` | 최상위 기준 | 표준프로세스_구성원칙.md |
| `02_표준/` | 표준별 작업 공간 | `{표준코드}/` 하위에 개요·요구사항·작업노트·_inputs |
| `03_POL_정책/` | POL 산출물 | 정책서 |
| `04_PRO_절차/` | PRO 산출물 | 절차서 |
| `05_WI_업무지침/` | WI 산출물 | 업무지침서 |
| `06_TMP_템플릿/` | TMP 산출물 | 빈 양식 |
| `07_EX_작성예시/` | EX 산출물 | 작성예시 |
| `08_REC_기록/` | REC (운영 단계) | 실제 수행 기록 |
| `09_REF_참고자료/` | REF 산출물 | 외부 규정·가이드 요약 |
| `90_MAT_통합매핑/` | 매핑·관리대장 | MAT-001~010 (현 6종) + 표준별 추적성 (MAT-011~) |
| `99_템플릿/` | Obsidian Templates | T03~T15 + _골든샘플 |
| `99_폐기_보관/` | 아카이브 | 폐지·superseded 문서 |
| `_inputs_common/` | 전사 공통 입력자료 | 회사 미션·조직도 등 |

## 탐색 시작점
1. [[MOC_전체표준]] — 편입된 표준 전체 상태
2. [[표준프로세스_구성원칙]] — 체계 기준선
3. [[MAT-001_문서관리대장]] — 문서 인벤토리

## 8종 문서 유형
POL / PRO / WI / TMP / EX / REC / MAT / REF
상세: [[01_문서체계]]

## 네이밍 규칙
`[유형]-[식별번호]_[문서명]_v[버전].md`
상세: [[02_문서번호체계]]

## 권장 Obsidian 플러그인
- Templates (코어) — `99_템플릿/` 지정
- Dataview — MAT-001 자동 인벤토리
- Graph view — 프로세스-표준 연결 시각화

## git 제외
`.gitignore` 에서 제외 (로컬 전용):
- `_inputs/` 내 실데이터
- `_state*.yaml`, `99_QA리포트_*`, `02_작업노트.md`
- `.obsidian/workspace*`, `.obsidian/cache/`
