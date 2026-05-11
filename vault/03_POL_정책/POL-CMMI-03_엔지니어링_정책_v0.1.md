---
type: POL
doc_id: POL-CMMI-03
title: "엔지니어링 정책"
version: "0.1"
status: draft
owner: "Chief Engineer / Engineering Director"
reviewer: "Senior Management Steering Group"
approver: "CEO/CTO"
scope_code: CMMI
scope: "요구사항 개발·기술 솔루션·제품 통합·검증·확인의 엔지니어링 전 흐름"
standards: [CMMI-DEV-ML3-V1.3]
standards_meta:
  publisher: "Software Engineering Institute (CMU/SEI)"
  year: 2010
  publication_report: "CMU/SEI-2010-TR-033"
  license: "internal_use_derivative_work"
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_coverage: [RD, TS, PI, VER, VAL]
category: "Engineering"
child_pro:
  - "[[PRO-CMMI-03-01_요구사항_개발_절차]]"
  - "[[PRO-CMMI-03-02_기술_솔루션_설계_절차]]"
  - "[[PRO-CMMI-03-03_제품_통합_절차]]"
  - "[[PRO-CMMI-03-04_검증_절차]]"
  - "[[PRO-CMMI-03-05_확인_절차]]"
created: 2026-05-11
updated: 2026-05-11
retention: "상시"
tags: [POL, CMMI, Engineering, RD, TS, PI, VER, VAL]
related:
  - "[[적용요건]]"
  - "[[POL-CMMI-02_프로젝트_관리_정책]]"
---

# 엔지니어링 정책 (POL-CMMI-03)

## 1. 목적
본 정책은 CMMI-DEV-ML3 Engineering 카테고리(RD, TS, PI, VER, VAL)의 요구를 충족하기 위해, 모든 개발 활동이 **요구사항 → 설계 → 통합 → 검증 → 확인**의 통제된 엔지니어링 흐름을 따르도록 방향을 정의한다.

## 2. 적용 범위
조직이 개발·공급하는 모든 제품·제품컴포넌트·서비스의 엔지니어링 활동에 적용한다. 단순 운영·유지보수(설계 변경이 없는 작업)는 [[PRO-CMMI-04-01_형상_관리_절차]] 만 적용한다.

## 3. 정의
- **Customer Requirements** (RD SG1): 이해관계자 니즈에서 도출·우선순위화된 고객 요구사항.
- **Product Requirements** (RD SG2): 고객 요구사항에서 도출·할당된 제품·컴포넌트·인터페이스 요구사항.
- **TDP** (Technical Data Package, TS SP2.2): 제품 설계의 기술자료 집합.
- **ICD** (Interface Control Document, TS SP2.3 / PI SP2.2): 인터페이스 설계 명세서.
- **Peer Review** (VER SG2): 정의된 기준에 따라 동료가 산출물을 검토하여 결함을 식별·제거하는 활동.

## 4. 역할과 책임 (RACI 요지)
| 역할 | 책임 |
|---|---|
| **CEO/CTO** | 정책 승인, 엔지니어링 게이트(요구 베이스라인·설계 베이스라인·릴리즈) 최종 승인 |
| **Chief Engineer** | 본 정책 유지, 엔지니어링 표준·기술 의사결정 |
| **Project Manager** | RD/TS/PI/VER/VAL 스케줄·자원 통합 (POL-CMMI-02 위임) |
| **Engineer / Architect** | RD/TS/PI/VER/VAL 실행 책임 |
| **Test Lead** | VER/VAL 환경·절차·실행 책임 |
| **Customer Representative** | RD SG1 (Elicit Needs), VAL 수락 |

## 5. 정책 원칙
1. **요구사항 우선** — 모든 설계·구현·통합·검증·확인은 베이스라인 요구사항(RD 산출)에 추적되어야 한다. 베이스라인되지 않은 요구사항으로 후속 활동을 시작할 수 없다.
2. **VER 먼저, VAL 다음** — 산출물은 먼저 "올바르게 만들었는가"를 VER로, 그 다음 "올바른 것을 만들었는가"를 VAL로 평가한다 (VER-before-VAL).
3. **인터페이스 우선 관리** — RD SP2.3에서 인터페이스 요구사항을 식별하고, TS SP2.3 ICD로 설계하며, PI SG2에서 호환성·완전성을 보장한다.
4. **공식적 의사결정 적용** — TS SP1.1 대안 평가·Make/Buy/Reuse (TS SP2.4) 등 영향 큰 결정은 [[PRO-CMMI-04-04_의사결정_분석_결정_절차]] (DAR)을 적용한다.
5. **Peer Review 의무** — VER SG2에 따라 주요 산출물(요구사항·설계·코드·테스트)은 정의된 피어리뷰 프로세스를 거친다.
6. **재귀·반복 허용** — RD ↔ TS는 새 정보 발견 시 반복하며, VER은 시스템·서브시스템·컴포넌트 레벨 모두에 재귀 적용한다 (recursion & iteration, p.50).

## 6. 준수 기준
- 모든 제품에 베이스라인 요구사항·설계·통합 산출물이 CM 베이스라인으로 등록.
- 요구사항 양방향 추적성(RTM): 고객 요구 ↔ 제품 요구 ↔ 설계 ↔ 코드 ↔ 검증·확인 결과 100%.
- 피어리뷰 결함 밀도 측정, 검증 결과 분석(VER SP3.2) 후 RD/TS/PI에 피드백.
- VAL 결과는 RD/TS/PI에 customer needs feedback으로 환류.

## 7. 관련 하위 절차 (PRO)
- [[PRO-CMMI-03-01_요구사항_개발_절차]] — RD
- [[PRO-CMMI-03-02_기술_솔루션_설계_절차]] — TS
- [[PRO-CMMI-03-03_제품_통합_절차]] — PI
- [[PRO-CMMI-03-04_검증_절차]] — VER
- [[PRO-CMMI-03-05_확인_절차]] — VAL

## 8. 표준 매핑 (Traceability)
| CMMI 조항 | Req-ID | 반영 |
|---|---|---|
| RD SG1~SG3 | CMMIDEV-RD-SG1~SG3-REQ-001 | §5-1, §7 PRO-CMMI-03-01 |
| TS SG1~SG3 | CMMIDEV-TS-SG1~SG3-REQ-001 | §5-3,4, §7 PRO-CMMI-03-02 |
| PI SG1~SG3 | CMMIDEV-PI-SG1~SG3-REQ-001 | §5-3, §7 PRO-CMMI-03-03 |
| VER SG1~SG3 | CMMIDEV-VER-SG1~SG3-REQ-001 | §5-2,5, §7 PRO-CMMI-03-04 |
| VAL SG1~SG2 | CMMIDEV-VAL-SG1~SG2-REQ-001 | §5-2, §7 PRO-CMMI-03-05 |
| Engineering Flow | pa_relationships.yaml — RD→TS→PI, VER feeds back to RD/TS/PI, VAL feedback (p.47-49) | §5-6 재귀·반복 |
| Cross-cutting | VER-before-VAL (p.49) | §5-2 |

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-RD-SG1~SG3 (p.328-340)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-TS-SG1~SG3 (p.375-390)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-PI-SG1~SG3 (p.259-268)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-VER-SG1~SG3 (p.403-410)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-VAL-SG1~SG2 (p.394-399)"
  retrieved_at: "2026-05-11"
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/pa_relationships.yaml"
  locator: "engineering_process_flow + VER-before-VAL (p.47-49)"
  retrieved_at: "2026-05-11"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (process-designer 생성) | - |
