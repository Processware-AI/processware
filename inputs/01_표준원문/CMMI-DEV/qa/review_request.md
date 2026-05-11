---
standard_id: CMMI-DEV
version: "1.3"
extraction_mode: backbone_first_pass
generated_at: "2026-05-11T00:00:00+09:00"
status: pending_review
---

# CMMI-DEV V1.3 인제스트 검토 요청 — Backbone Pass

## 📋 요약

- **표준**: CMMI for Development, Version 1.3 (CMU/SEI-2010-TR-033, 2010-11)
- **추출 범위**: Backbone 단일 패스 — 22 PA 구조 + GG/GP 골격 + 2 PA 샘플 verbatim
- **요건 수**: **62건의 backbone 요건** (3 GG + 12 GP + 47 SG) + 5건의 SP 샘플
- **PDF-verbatim 비율**: 15 / 67 = 22%
- **다음 명령**: `/process-ingest --confirm CMMI-DEV`

---

## ✅ 검증된 사실 (PDF verbatim 확보)

검토자가 그대로 신뢰해도 좋은 항목:

- [x] **22 Process Areas 모두 식별** (Table 3.2, p.33 verbatim)
- [x] **카테고리 분류** (Process Mgmt 5 / Project Mgmt 7 / Engineering 5 / Support 5)
- [x] **Maturity Level 매핑** (ML2 7개 / ML3 11개 / ML4 2개 / ML5 2개)
- [x] **GG 1, GG 2 statements** (p.68 verbatim)
- [x] **GP 1.1, GP 2.1, GP 2.2, GP 2.3 statements** (p.68-76 verbatim)
- [x] **REQM SP 1.5 statement + Example Work Products + 4 Subpractices** (p.346 verbatim)
- [x] **RSKM PA Purpose, Intro, SG/SP Summary, SG 1, SP 1.1-1.3, SG 2, SP 2.1** (p.349-354 verbatim)
- [x] **Component classification 3-tier** (required / expected / informative — p.9-10 verbatim)
- [x] **Numbering scheme** (SG/GG/SP/GP — p.15 verbatim)

---

## ⚠️ 의도된 한계 — 검토자가 결정해야 할 항목

다음 6개 영역은 **backbone 패스에서 의도적으로 deferred**. 각 항목을 확인하고 우선순위를 정해 주세요.

### [ ] D-1. SP verbatim 추출 (20 PAs)

CAR, CM, DAR, IPM, MA, OPD, OPF, OPM, OPP, OT, PI, PMC, PP, PPQA, QPM, RD, SAM, TS, VAL, VER 20개 PA의 SP (Specific Practice) 본문이 canonical structure 기준이며 PDF verbatim 인용이 없음.

- **영향**: SP-level 감사 증적이 필요한 경우 verbatim 보강 필요
- **추정 작업량**: PA당 평균 10-15 페이지 × 20 PA ≈ 220 페이지 (PDF Read ~12 회)
- **권고 결정**:
  - [ ] D-1-a. 모든 20 PA SP verbatim 보강
  - [ ] D-1-b. ML2 PA(CM, MA, PMC, PP, PPQA, SAM)만 우선 보강 (6 PA)
  - [ ] D-1-c. Engineering PA(PI, RD, TS, VAL, VER)만 우선 보강 (5 PA)
  - [ ] D-1-d. 보류 — 현재 backbone 으로 차원 1 (Plan) 진행

### [ ] D-2. GP 2.4 ~ 3.2 verbatim 추출 (9 GP)

`GP 2.4 Assign Responsibility`, `GP 2.5 Train People`, ... `GP 3.2 Collect Process Related Experiences` statement 가 canonical-derived. PDF verbatim 인용 없음.

- **영향**: GP-level 정책/절차 매핑 시 출처 인용 불가
- **추정 작업량**: p.82-126 (~45 페이지, PDF Read 3 회)
- **권고 결정**:
  - [ ] D-2-a. 9개 GP verbatim 보강 (권장 — 작업량 적음)
  - [ ] D-2-b. 보류

### [ ] D-3. Appendix D Glossary 전체 추출

핵심 17건 용어만 `definitions.yaml` 에 등재. CMMI 공식 Glossary 약 100여건이 추가로 존재.

- **영향**: 용어 정의 인용 시 일부 항목은 직접 추출 필요
- **추정 작업량**: p.433-end (~30 페이지, PDF Read 2 회)
- **권고 결정**:
  - [ ] D-3-a. 전체 Glossary 보강
  - [ ] D-3-b. on-demand (요청 시 개별 보강)

### [ ] D-4. Part One Ch 4-5 본문 추출

Ch 4 "Relationships Among Process Areas" + Ch 5 "Using CMMI Models" 본문 미추출 (TOC structure 만 캡처).

- **영향**: PA 간 의존성 (Process Management 군 등) 정보가 informative
- **추정 작업량**: p.39-61 (~23 페이지, PDF Read 2 회)
- **권고 결정**:
  - [ ] D-4-a. 보강 (PA 간 관계도 informative reference 로 유용)
  - [ ] D-4-b. 보류

### [ ] D-5. SP 분류 검증 (canonical vs verbatim)

`requirements.yaml` 에서 `status: active_canonical` 으로 표시된 39건의 SG/GP statements 는 CMMI-DEV V1.3 공식 카탈로그 기준 인용이지만 본 PDF 에서 직접 추출하지 않음. 카탈로그와 본 PDF 가 일치한다는 사용자 확인이 필요.

- **검증 방법**: 무작위 5건 spot-check → PDF Read 1-2 회
- **권고 결정**:
  - [ ] D-5-a. spot-check 수행 (random 5 SG verbatim 비교)
  - [ ] D-5-b. spot-check 생략 (canonical 카탈로그 신뢰)

### [ ] D-6. CMMI-DEV 사용 의도 확인

CMMI-DEV V1.3 의 발행일은 2010-11. 후속 버전 V2.0, V2.2, V3.0 이 존재 (CMMI Institute / ISACA 관리).

- **권고 결정**:
  - [ ] D-6-a. V1.3 그대로 사용 (예: 사내 적합성 검증, 과거 인증 기반)
  - [ ] D-6-b. 최신 버전(V3.0 등) 으로 업그레이드 후 재투입 — 본 ingest 무효화

---

## 📊 추출 결과 — 본문 요건 (확인 권장)

| ID | Clause | Title | Component | Status |
|---|---|---|---|---|
| CMMIDEV-GG1-REQ-001 | GG 1 | Achieve Specific Goals | required | ✅ verbatim |
| CMMIDEV-GG2-REQ-001 | GG 2 | Institutionalize a Managed Process | required | ✅ verbatim |
| CMMIDEV-GG3-REQ-001 | GG 3 | Institutionalize a Defined Process | required | canonical |
| CMMIDEV-GP1.1-REQ-001 | GP 1.1 | Perform Specific Practices | expected | ✅ verbatim |
| CMMIDEV-GP2.1-REQ-001 | GP 2.1 | Establish an Organizational Policy | expected | ✅ verbatim |
| CMMIDEV-GP2.2-REQ-001 | GP 2.2 | Plan the Process | expected | ✅ verbatim |
| CMMIDEV-GP2.3-REQ-001 | GP 2.3 | Provide Resources | expected | ✅ verbatim |
| CMMIDEV-GP2.4~2.10 | GP 2.4-2.10 | (7 GPs) | expected | canonical |
| CMMIDEV-GP3.1, 3.2 | GP 3.1, 3.2 | (2 GPs) | expected | canonical |
| CMMIDEV-CAR-SG1 | CAR SG 1 | Determine Causes of Selected Outcomes | required | canonical |
| ... (생략, 총 SG 47건) | ... | ... | ... | ... |
| CMMIDEV-REQM-SP1.5 | REQM SP 1.5 | Ensure Alignment Between Project Work and Requirements | expected | ✅ verbatim |
| CMMIDEV-RSKM-SP1.1~2.1 | RSKM SP 1.1-2.1 | (4 SPs) | expected | ✅ verbatim |

**전체 목록**: `requirements.yaml` 참조

---

## 🔧 수정 방법

`requirements.yaml`, `structure.yaml`, `definitions.yaml` 을 직접 편집할 수 있습니다.

- 잘못된 요건 statement → `text` 필드 수정 + `status: active_verbatim` 변경
- 누락된 요건 → 새 entry 추가 + `source_map.yaml` 에 page 정보 등재
- 불필요한 요건 → 해당 entry 의 `status: deprecated` 로 표시

---

## ▶️ 다음 단계

검토 완료 후 다음 명령으로 진행:

```bash
# 옵션 1: 현재 backbone 으로 차원 1 (Plan) 진행
/process-ingest --confirm CMMI-DEV
/process-plan "CMMI-DEV ML3 기반 사내 표준 프로세스"

# 옵션 2: deeper pass 보강 후 확정
#   (이 review 파일에 [ ] 체크박스 표시 후 처리 요청)
```

---

## 📁 산출물 위치

```
inputs/01_표준원문/CMMI-DEV/
├── structure.yaml          # 표준 구조 (TOC + 22 PA + GG/GP)
├── requirements.yaml       # 요건 67건 (62 backbone + 5 SP 샘플)
├── definitions.yaml        # 핵심 용어 17건
├── annexes.yaml            # Part Three Appendix 메타데이터
├── source_map.yaml         # 페이지 매핑 33건
├── clauses.md              # raw 추출 노트
├── _state.yaml             # ingest 상태 (overall_status: pending_review)
└── qa/
    ├── extraction_quality_report.md   # 품질 보고서
    └── review_request.md              # 본 파일
```
