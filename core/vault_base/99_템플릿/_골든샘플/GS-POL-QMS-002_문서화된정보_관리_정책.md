---
type: golden_sample
models: POL
doc_id: "GS-POL-QMS-002"
title: "문서화된 정보 관리 정책 (골든 샘플)"
version: "1.0"
owner: "Quality Management Representative"
reviewer: "Process Control Board"
approver: "CEO"
scope: "전사 품질경영시스템 내 모든 문서화된 정보(Documented Information)"
child_pro:
  - "[[GS-PRO-QMS-102_문서_개정_관리_절차]]"
  - "[[PRO-QMS-101_문서_생성_관리_절차]]"
  - "[[PRO-QMS-103_문서_폐기_관리_절차]]"
standards: ["ISO 9001", "ISO/IEC 27001", "ISO 14001"]
status: approved
created: 2026-04-17
updated: 2026-04-17
retention: "상시"
tags: [POL, QMS, golden-sample]
---

# 문서화된 정보 관리 정책 (GS-POL-QMS-002)

> **[골든 샘플]** 이 문서는 `POL` 유형의 품질 하한선 참조용입니다. 실제 산출물 아님.
> 상위 기준: [[표준프로세스_구성원칙]] · 문서체계: [[01_문서체계]]

## 1. 목적
본 정책은 당사의 품질경영시스템(QMS)에서 생성·유지·활용되는 모든 **문서화된 정보**가 요구되는 시점·장소에서 **이용 가능하고, 적절하게 보호**되도록 관리 방향을 정의한다.

## 2. 적용 범위
전사 모든 조직에서 생성하는 8종 문서(POL/PRO/WI/TMP/EX/REC/MAT/REF) 및 외부 기원 문서(법규·표준·고객 요구문서)에 적용한다. 개인 업무 노트·임시 초안은 제외한다.

## 3. 정책 원칙
1. **단일 출처(Single Source of Truth)** — 동일 주제에 대해 상충되는 복수 문서를 두지 않는다.
2. **최신성 유지** — 모든 사용자는 최신 승인판만 참조·활용한다. 구판 접근은 이력 추적 목적에 한정한다.
3. **접근 통제** — 기밀 등급(공개·내부·제한·극비)에 따라 열람·편집 권한을 부여한다.
4. **이력 추적성** — 모든 개정·승인·배포 이력은 [[MAT-001_문서관리대장]] 에 기록한다.
5. **폐기 규율** — 보존기간 경과 시 정해진 절차로 폐기하며, 법적 보존 의무 문서는 별도 관리한다.

## 4. 역할과 책임
| 역할 | 책임 |
|---|---|
| **CEO** | 정책 승인, 자원 배정 |
| **Quality Management Representative (QMR)** | 정책 유지·유효성 검토 (연 1회) |
| **Process Control Board (PCB)** | 신규·개정 심의, 영향평가 승인 |
| **Process Owner** | 담당 영역 문서의 최신성·정확성 유지 |
| **모든 임직원** | 최신 승인판 사용, 미승인 초안 배포 금지 |

## 5. 준수 기준
- 모든 문서는 `[유형]-[식별번호]_[이름]_v[버전].md` 파일명 규칙 준수 ([[02_문서번호체계]])
- 필수 frontmatter 메타 충족 ([[01_문서체계]] §필수 메타 표)
- 개정 시 [[GS-PRO-QMS-102_문서_개정_관리_절차]] 준수
- 보관기간 종료 시 `PRO-QMS-103` 폐기 절차 준수

## 6. 관련 하위 절차 (PRO)
- [[GS-PRO-QMS-102_문서_개정_관리_절차]] — 개정·버전관리
- [[PRO-QMS-101_문서_생성_관리_절차]] — 신규 생성·승인
- [[PRO-QMS-103_문서_폐기_관리_절차]] — 보존·폐기

## 7. 표준 매핑 (Traceability)
| 표준 조항 | Req-ID | 반영 |
|---|---|---|
| ISO 9001 §7.5.1 | ISO9001-R-030 | §3 정책 원칙 1~5 |
| ISO 9001 §7.5.2 | ISO9001-R-031 | §5 준수 기준 (식별·설명) |
| ISO 9001 §7.5.3 | ISO9001-R-032 | §6 관련 하위 절차 (통제) |
| ISO 27001 §7.5 | ISO27001-R-030 | 공통 적용(IMS) |

## 8. 출처 (source_citation)
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/ISO9001_2015.pdf"
  locator: "§7.5.1 Documented Information — General"
  retrieved_at: "2026-04-17"
  license: "ISO copyright — paraphrase only"
  paraphrase_only: true
- type: standard_original
  file: "_inputs/01_표준원문/ISO27001_2022.pdf"
  locator: "§7.5"
  retrieved_at: "2026-04-17"
  license: "ISO copyright — paraphrase only"
  paraphrase_only: true
```

## 9. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 1.0 | 2026-04-17 | 최초 승인 | CEO |

---

## 🎯 이 샘플에서 본받을 포인트 (에이전트 학습 포인트)
- **분량**: A4 1~2장 내. 세부 절차를 끌어오지 않음.
- **§3 정책 원칙**: 행동이 아니라 **원칙**을 5개 이내로. "~한다" 어조.
- **§4 역할**: 승인자는 1인(CEO), 유지자(QMR)·심의체(PCB)·실행자(Owner) 분리.
- **§7 표준 매핑**: 정책에도 Req-ID 역추적이 반드시 있어야 함.
- **§8 source_citation**: 모든 주장을 `_inputs/` 근거와 연결. paraphrase_only 플래그 명시.
