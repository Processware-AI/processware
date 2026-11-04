---
type: golden-sample-index
title: 골든 샘플 (Golden Samples)
updated: 2026-04-17
tags: [golden-sample, reference]
---

# 골든 샘플 — 품질 하한선 참조

이 폴더의 문서는 **실제 산출물이 아님**. 각 유형별 "이 정도 수준으로 써야 한다" 는 기준 예시.

## 용도
1. 에이전트가 POL/PRO/WI 생성 시 **구조·깊이·문체의 기준선**으로 참조
2. 사용자 검토 시 **"좋은 결과물이란 무엇인가"** 합의 기준
3. QA 에이전트의 **골든샘플 정합성** 점검 기준

## 수록 목록

| 파일 | 유형 | 축(앵커) | 비고 |
|---|---|---|---|
| [[GS-POL-QMS-002_문서화된정보_관리_정책]] | POL | ISO 9001 §7.5 | 방향성·원칙·책임만 |
| [[GS-PRO-QMS-102_문서_개정_관리_절차]] | PRO | §7.5.3 문서 통제 | Mermaid·RACI·KPI 모범 |
| [[GS-WI-102-04_개정_및_버전관리]] | WI | PRO-QMS-102 하위 | 단계·I/O·예외처리 모범 |

## 선택 기준
- **ISO 9001 §7.5 (문서화된 정보)** 를 축으로 선정 — HLS 공통 조항이라 모든 표준에서 재활용 가능
- POL→PRO→WI 가 실제로 **체인으로 이어지는 완결 세트**

## 운영 규칙
- 파일명 접두어 `GS-` (Golden Sample)
- frontmatter `type: golden_sample`, `models: <POL|PRO|WI>`
- MAT-001 문서관리대장에 **등록 금지** (실 산출물 아님)
- 골든샘플 자체 개정은 구성원칙 개정과 같은 수준의 중대 변경 취급

## 에이전트 참조 규약
- `process-designer` : POL/PRO 생성 전 GS-POL-*, GS-PRO-* 를 먼저 읽음
- `wi-tmp-writer`   : WI 생성 전 GS-WI-* 를 먼저 읽음
- `qa-reviewer`     : 각 산출물이 동일 유형 GS 의 **필수 섹션 구조**를 포함하는지 점검

## 신규 골든샘플 추가 시
1. 본 폴더에 `GS-{유형}-{ID}_{이름}.md` 로 생성
2. 이 README 의 수록 목록에 Row 추가
3. PCB(Process Control Board) 준하는 검토 후 반영
