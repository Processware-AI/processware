---
standard_id: AutoCyberSec
full_name: "ISO/SAE 21434:2021 — Road vehicles — Cybersecurity engineering"
version: "2021"
source_file: sources/ISO_SAE_21434_2021(en).pdf
source_hash: "sha256:79d188172b9ba1971f7ac24f79aab2d58617ad28e4ce2f341d0e2dbc43dfe9ef"
generated_at: "2026-06-14"
extraction_tool: "pdftotext -layout (poppler) + pdfplumber"
---

# AutoCyberSec (ISO/SAE 21434:2021) — 추출 품질 보고서

## 1. 원본 개요
- 총 페이지: **88 p**
- 문서 유형: 텍스트 레이어 PDF (스캔본 아님 — 페이지 평균 ~2,553자, 임계 100자 대비 충분)
- OCR: 불필요 (`ocr_processed: false`)
- 추출 방식: 컬럼 인식을 위해 `pdftotext -layout` 사용. 본 표준은 요구사항 ID(`[RQ-..]`)가 좌측 사이드바 박스에 배치되어 일반 추출 시 본문과 글자 단위로 뒤섞임 → layout 모드로 컬럼 분리 후 단락 선두 앵커로 정규화.

## 2. 추출 성공률
| 항목 | 결과 |
|---|---|
| 추출 성공 페이지 | 88 / 88 (100%) |
| 추출 실패 페이지 | 없음 |
| 표 추출 | 본문 표는 텍스트로 평탄화됨(레이아웃 보존 안 됨) — Annex E/F/G/H 의 평가표는 구조 손실 있음 (informative, 요구사항 아님) |
| 그림 추출 | 그림은 캡션만 텍스트로 보존 (informative) |

## 3. 요구사항 마이닝 결과
본 표준은 모든 규범 조항(Clause 5–15)에서 provision 을 명시적 ID 로 자가 번호화한다:
`[RQ-NN-MM]`(requirement/shall), `[RC-NN-MM]`(recommendation/should), `[PM-NN-MM]`(permission/may).
이를 1차 앵커로 사용하여 마이닝 정확도가 매우 높다.

| 유형 | 추출 건수 |
|---|---|
| RQ (normative, shall) | 101 |
| RC (recommendation, should) | 13 |
| PM (permission, may) | 4 |
| **합계** | **118** |

### 분류(content classification)
- process_requirement: 105
- evidence_requirement: 9
- role_requirement: 4

## 4. 완전성 검증 (자동)
| 검사 | 기준 | 결과 |
|---|---|---|
| 규범 조항 커버리지 | Clause 5–15 (11개 그룹) | **11 / 11 모두 요건 보유** ✅ |
| **ID 시퀀스 연속성** | 각 조항 그룹 provision 번호가 1..max 연속 | **누락 0건** (모든 조항 그룹 gap 없음) ✅ |
| 짧은/빈 텍스트 | 25자 미만 | 0건 ✅ |
| NOTE/EXAMPLE/표/참고문헌 누출 | 요건 본문에 informative 텍스트 혼입 | 0건 ✅ |
| 미분리 복합문 | 단일 REQ에 shall 2회 이상 | 0건 ✅ |
| 분류 미확정 | type/classification = unknown | 0건 ✅ |
| 의무 수준 일관성 | RQ⊃shall / RC⊃should / PM⊃may | 100% 일치 ✅ |

> **ID 시퀀스 연속성 0 누락**은 본 표준이 provision 을 1..N 연속 번호화하기 때문에 가능한 강력한 완전성 신호다. 각 조항의 RQ+RC+PM 합집합이 빈틈없이 연속함을 확인 → **누락된 provision 없음**.

## 5. 보조 산출물
| 산출물 | 건수 | 비고 |
|---|---|---|
| 용어 정의 (Clause 3.1) | 40 | `definitions.yaml` |
| 약어 (Clause 3.2) | 12 | CAL, CVSS, E/E, ECU, OBD, OEM, PM, RC, RQ, RASIC, TARA, WP |
| 작업산출물 WP (`[WP-NN-MM]`) | 42 | `annexes.yaml` + 요건 evidence_candidates 연계 |
| Annex | 8 (A–H, 전부 informative) | `annexes.yaml` |
| 구조 노드 | 15 root + 4단계 하위절 | `structure.yaml` |

## 6. 알려진 한계 / 검토 권고 사항
1. **입력 전제(Prerequisites) 미포함 (18건)**: 각 조항의 `X.Y.1.1 Prerequisites` 의 "The following information shall be available:" 블록은 상류 작업산출물(`[WP-..]`)에 대한 **입력 의존성 선언**으로, 독립 요구사항 ID 가 없어 118건에 미포함. 별도 의존성 매핑이 필요하면 검토 요청서 참조.
2. **표 구조 손실 (informative)**: Annex E(CAL), F(impact), G(feasibility), H(TARA 예시)의 평가 매트릭스는 텍스트 평탄화로 셀 정렬이 손실됨. 모두 informative 가이드이며 규범 요건 아님.
3. **RQ-15-10 후미 표 참조 누락**: "…shall be determined as described in" 뒤의 "Table 1" 참조가 표 제거 과정에서 탈락. 의무 내용 자체는 보존. 검토 요청서 §모호 항목 참조.
4. **type 어휘 확장**: PM(permission)을 위해 `type: permission` 을 도입(구성원칙 표준 8종 외 확장). RQ→normative, RC→recommendation 과 정합.

## 7. 종합 판정
**추출 품질: 우수 (Excellent).** 자가 번호화 표준 특성상 시퀀스 연속성으로 완전성이 검증되었고, informative 누출·복합문·분류 미확정 모두 0건. HITL 검토는 위 §6 의 4개 경미 항목에 집중하면 충분하다.
