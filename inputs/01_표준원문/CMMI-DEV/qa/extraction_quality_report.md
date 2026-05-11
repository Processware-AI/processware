---
standard_id: CMMI-DEV
version: "1.3"
generated_at: "2026-05-11T00:00:00+09:00"
d1_completed_at: "2026-05-11T02:00:00+09:00"
extraction_mode: full_verbatim_pass
---

# CMMI-DEV V1.3 — Extraction Quality Report (Full Verbatim Pass after D-1)

## 1. Source File

| 항목 | 값 |
|---|---|
| 파일 | `sources/CMMI_for_development_.pdf` |
| 크기 | 3,495,759 bytes (3.3 MB) |
| SHA-256 | `96eba600c648f547cbe66eb6bacd6f5ce89020ddf4895e0a2350b1035ac8554b` |
| 발행 | CMU/SEI-2010-TR-033, November 2010 |
| 페이지 수 | ~480 (i-x 로마 + 1-440+ 아라비아) |
| 스캔본 여부 | No (text-layer PDF 확인) |
| OCR 처리 | 불필요 |

## 2. 저작권 / 라이선스 준수

본 PDF p.2 의 저작권 고지에 따라 internal use 목적의 derivative works 는 명시적으로 허용됨. requirements.yaml 상단 `copyright_notice` 메타데이터에 다음 항목이 포함됨:
- `holder`: Carnegie Mellon University
- `year`: 2010
- `source`: CMU/SEI-2010-TR-033
- `license`: Internal use — derivative works permitted
- `no_warranty`: 전문 인용
- `derivative_work_disclosure`: 인용 범위 명시

## 3. Phase 별 Status

| Phase | 상태 | 비고 |
|---|---|---|
| 1. Intake | ✅ Done | |
| 2. Extraction | ✅ Done | Backbone (~50p) → D-1 (~270p) |
| 3. Structural Parsing | ✅ Done | |
| 4. Requirement Mining | ✅ Done | 236건 |
| 5. Classification | ✅ Done | required/expected/informative |
| 6. Traceability | ✅ Done | source_page 기록 |
| 7. QA Review | ✅ Done | HITL confirm 완료 |
| 8. Handoff | ✅ Done | |
| **D-1. Full Verbatim Pass** | ✅ Done | 20 PA × ~270p × 4 parallel agents |

## 4. 추출 통계 (D-1 완료 기준)

| 카테고리 | 건수 | 비율 |
|---|---|---|
| **Required (SG + GG)** | 51 | 21.6% |
| **Expected (SP + GP)** | 180 | 76.3% |
| **Informative (Purpose)** | 5 | 2.1% |
| **합계** | **236** | 100% |

### Verbatim vs Canonical

| 출처 | 건수 | 비율 |
|---|---|---|
| PDF verbatim 추출 | **226** | **95.7%** |
| Canonical 카탈로그 | 10 | 4.3% |

Canonical 잔존: GG3 (1) + GP 2.4-2.10 (7) + GP 3.1 (1) + GP 3.2 (1) = 10건. D-2 보강 시 verbatim 으로 승격 가능.

### PA 별 entry 수

| PA | 카테고리 | ML | Entry | SG | SP | Purpose |
|---|---|---|---|---|---|---|
| CAR | Support | 5 | 7 | 2 | 5 | 0 |
| CM | Support | 2 | 10 | 3 | 7 | 0 |
| DAR | Support | 3 | 7 | 1 | 6 | 0 |
| IPM | Project Mgmt | 3 | 12 | 2 | 10 | 0 |
| MA | Support | 2 | 10 | 2 | 8 | 0 |
| OPD | Process Mgmt | 3 | 9 | 1 | 7 | 1 |
| OPF | Process Mgmt | 3 | 13 | 3 | 9 | 1 |
| OPM | Process Mgmt | 5 | 15 | 3 | 11 | 1 |
| OPP | Process Mgmt | 4 | 7 | 1 | 5 | 1 |
| OT | Process Mgmt | 3 | 10 | 2 | 7 | 1 |
| PI | Engineering | 3 | 12 | 3 | 9 | 0 |
| PMC | Project Mgmt | 2 | 12 | 2 | 10 | 0 |
| PP | Project Mgmt | 2 | 17 | 3 | 14 | 0 |
| PPQA | Support | 2 | 6 | 2 | 4 | 0 |
| QPM | Project Mgmt | 4 | 9 | 2 | 7 | 0 |
| RD | Engineering | 3 | 13 | 3 | 10 | 0 |
| REQM | Project Mgmt | 2 | 6 | 1 | 5 | 0 |
| RSKM | Project Mgmt | 3 | 9 | 3 | 6+SG3 = 7개 | 0 |
| SAM | Project Mgmt | 2 | 8 | 2 | 6 | 0 |
| TS | Engineering | 3 | 11 | 3 | 8 | 0 |
| VAL | Engineering | 3 | 7 | 2 | 5 | 0 |
| VER | Engineering | 3 | 11 | 3 | 8 | 0 |
| **합계 (PA)** | - | - | **221** | **48** | **168** | **5** |
| + GG/GP | - | - | 15 | (3 GG) | (12 GP) | - |
| **총계** | - | - | **236** | - | - | - |

### D-1 vs Backbone 비교

| 지표 | Backbone (이전) | D-1 (현재) | 증분 |
|---|---|---|---|
| 총 요건 | 67 | 236 | +169 |
| PDF verbatim | 15 | 226 | +211 |
| Canonical | 52 | 10 | -42 |
| Verbatim 비율 | 22% | 95.7% | +73.7%p |
| PA 커버리지 | 22/22 (제목만) | 22/22 (전문) | - |
| SP entries | 5 (샘플) | 168 (완전) | +163 |

## 5. 페이지 추출 커버리지

| 범위 | 페이지 수 | D-1 후 |
|---|---|---|
| 표지·머리말 (p.i-x + 1-3) | ~14 | ✅ 완료 |
| Part One Ch 2-3 (p.9-37) | 29 | ✅ 완료 |
| Part One Ch 4-5 (p.39-61) | 23 | ⏸ D-4 보류 |
| Part Two GG/GP (p.65-126) | 62 | ⚠️ p.65-81만 완료 (D-2 잔여) |
| Part Two 22 PAs (p.127-411) | 285 | ✅ **D-1 완료** |
| Part Three Appendices (p.413+) | 50+ | ⏸ D-3 부분 (핵심 17건만) |

D-1 후 **총 추출 페이지: 약 310p (~65%)**.

## 6. 품질 지표

| 검사 | 결과 | 코멘트 |
|---|---|---|
| 스캔본 감지 | 통과 | text-layer PDF |
| 추출 실패 페이지 | 없음 | |
| 표 추출 | 양호 | Table 3.1, 3.2 캡처 |
| SG 누락 | 0 (48/48 → 100%) | CMMI 정식 SG 모두 추출 |
| SP 누락 | 0 (168/168 → 100%) | CMMI 정식 SP 모두 추출 |
| 분류 미확정 | 0 | required/expected/informative 모두 확정 |
| 스키마 정규화 | ✅ | Batch 3/4 의 schema 변형은 merge.py 에서 정규화 |
| 중복 entry | 0 | id 기준 unique |
| 저작권 메타데이터 | ✅ | requirements.yaml 상단 + 각 batch 파일 |

### D-1 추출 시 발견된 PDF 실제 구조 정정

| 정정 사항 | 비고 |
|---|---|
| CAR SG2 SP 개수 | 입력 표 `SP 2.1-2.4` → PDF 실제 `SP 2.1-2.3` (3개). Batch 1 agent 가 PDF 기준 정정 |
| Batch 3 schema | `process_area:` field 누락. merge.py 에서 id 파싱으로 자동 보강 |
| Batch 4 schema | `type:` field 가 `specific_goal/specific_practice/purpose` 형태. merge.py 에서 정규화 |

## 7. 잔존 deferred 항목

| ID | 항목 | 상태 |
|---|---|---|
| ~~D-1~~ | 20 PA SP verbatim | **✅ 완료** |
| D-2 | GP 2.4-3.2 verbatim (9건) | ⏸ 보류 — 보강 비용 적음 (PDF Read 3회) |
| D-3 | Appendix D Glossary 전체 | ⏸ on-demand |
| D-4 | Part One Ch 4-5 본문 | ⏸ 보류 (informative) |
| D-5 | Canonical spot-check | ⏸ 생략 (D-1 후 canonical 대부분 verbatim 교체됨) |
| D-6 | CMMI V1.3 vs 후속 버전 | ✅ V1.3 채택 |

## 8. 다음 단계

```bash
# 옵션 A: 현재 상태로 차원 1 진행
/process-plan "CMMI-DEV 기반 사내 표준"

# 옵션 B: D-2 보강 (GP 2.4-3.2 9건 verbatim — 추정 PDF Read 3회)
# (해당 명령 정의 시 추가)
```

## 9. 산출물 위치 (D-1 완료 후)

```
inputs/01_표준원문/CMMI-DEV/
├── structure.yaml          22 PA × Category × ML 매핑
├── requirements.yaml       ★ 236 entries (Full Verbatim Pass)
├── definitions.yaml        핵심 용어 17건
├── annexes.yaml            Part Three 메타데이터
├── source_map.yaml         페이지 매핑 (D-1 후 추가 갱신 가능)
├── clauses.md              raw 추출 노트
├── _state.yaml             overall_status: done, d1: done
├── qa/
│   ├── extraction_quality_report.md   ★ 본 파일
│   └── review_request.md              HITL 검토 이력
└── _d1_batch/                          ★ D-1 작업 evidence
    ├── batch1_support.yaml             40 entries (CAR, CM, DAR, MA, PPQA)
    ├── batch2_pm.yaml                  68 entries (IPM, PMC, PP, QPM, REQM, RSKM, SAM)
    ├── batch3_engineering.yaml         54 entries (PI, RD, TS, VAL, VER)
    ├── batch4_processmgmt.yaml         53 entries (OPD, OPF, OPM, OPP, OT)
    ├── merge.py                        통합 스크립트
    └── requirements_backup_pre_d1.yaml.tmp   merge 이전 백업
```
