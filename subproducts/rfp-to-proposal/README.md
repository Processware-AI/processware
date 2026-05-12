---
type: subproduct-root
title: RFP-to-Proposal — 파생 프로덕트 ① (Prototype)
status: prototype
parent_repo: Processware
updated: 2026-05-13
tags: [subproduct, rfp, proposal, derivative]
---

# RFP-to-Proposal — 파생 프로덕트 ① (Prototype)

발주처 RFP(제안요청서)를 분석하여 응시자 **제안서(Proposal)** 초안을 자동 작성하는 파생 프로덕트의 prototype.

> ⚠️ **현재 상태**: prototype — 분석·정규화 단계만 구현, 제안서 작문 엔진 미구현.
> ⚠️ **위치**: 본 메인 Processware repo 안의 `subproducts/` 격리 영역. 향후 별도 repo (`processware-rfp-to-proposal`) 로 분리 예정.

---

## 1. 본 sub-product 의 위치 (3-Vault 생태계)

상세: `../../docs/architecture/derivative-products.md`

```
┌─ 📦 코어 vault — Processware (메인 repo)  ─┐
│   국제표준 / 법규 → POL/PRO/WI 등          │
└────────────────────────────────────────────┘
                                              ┌─ 🤖 파생 ① — 본 sub-product ────┐
                                              │   RFP → 제안서 (Proposal)        │
                                              │   (별도 vault, 코어 와 결합 안함)│
                                              └──────────────────────────────────┘
                                                              ↓
                                              ┌─ 🛠 파생 ② — Project Asset Gen  ─┐
                                              │   제안서 + 코어 vault           │
                                              │   → 사업 산출물                  │
                                              └──────────────────────────────────┘
```

## 2. 디렉토리

```
subproducts/rfp-to-proposal/
├── README.md                      ← 본 문서
├── docs/                          ← sub-product 설계·아키텍처
├── sources/                       ← RFP 원본 (PDF/DOCX/HWPX)
│   └── RFP.hwpx                   ← 1차 검증 케이스 (대구광역시 보건환경연구원)
├── inputs/                        ← RFP 분석 결과 (정규화 패키지)
│   ├── SI_Project/                ← 케이스 1: 보건환경종합정보시스템 고도화
│   │   ├── _state.yaml
│   │   ├── structure.yaml
│   │   ├── requirements.yaml      ← 78건 정규화 요구사항
│   │   ├── clauses.md
│   │   ├── definitions.yaml
│   │   ├── annexes.yaml
│   │   ├── source_map.yaml
│   │   └── qa/
│   └── 06_목표흐름/
│       ├── business_flow.yaml     ← 17 시나리오 / 6 그룹 (제안서 §사업수행방안 골격)
│       └── business_flow.md       ← Mermaid 시각화 동반본
└── tools/                         ← 분석 엔진 prototype
    ├── hwpx_extract.py            ← Hancom HWPX → 단락 단위 텍스트 추출
    ├── rfp_parser.py              ← RFP 목록표 + 상세 요구사항 구조화
    └── rfp_to_inputs.py           ← inputs/ 패키지 생성 (YAML·MD)
```

## 3. 현재 구현 범위

### ✅ 구현됨 (prototype)
- **RFP 추출** — `.hwpx` (Hancom Office) ZIP 아카이브 → XML 단락 단위 텍스트
- **구조 파싱** — 요구사항 목록표 + 상세 요구사항 영역 자동 식별
- **요구사항 정규화** — ID 패턴(`{prefix}-{NNN}`) 기반 78건 자동 추출 + name/definition/details/outputs 분리
- **카테고리 분류** — 11종 (ECR/SFR/PER/SIR/DAR/TER/SER/QUR/COR/PMR/PSR)
- **업무 시나리오 도출** — `flow-proposer` agent 가 정규화 요구사항 → 17 시나리오 / 6 그룹 매핑
- **Mermaid 시각화 동반본** — `business_flow.md` 자동 생성

### ❌ 미구현 (향후)
- **제안서 작문 엔진** — 정규화 요구사항 + 코어 vault 참조 → 제안서 섹션 본문 자동 작성
- **제안서 vault 구조** — 입찰사례별 누적 + 추적성 매트릭스
- **다른 형식 지원** — PDF / DOCX RFP 입력
- **CLI/SaaS UX** — 현재는 Python 스크립트 직접 실행

## 4. 검증 결과 (1차 케이스)

| 항목 | 값 |
|---|---|
| 대상 RFP | 대구광역시 보건환경연구원 — 보건환경종합정보시스템 고도화 사업 |
| 원본 형식 | HWPX (Hancom Office) |
| 원본 단락 | 4,285개 |
| 추출 글자 수 | 136,737자 |
| 추출 요구사항 | 78건 / 11카테고리 |
| 자동 정규화 정확도 | 양호 (name·definition·outputs 100% / details 8건 short — 표 평탄화 손실) |
| 업무 시나리오 도출 | 17 시나리오 / 6 그룹 |

## 5. 사용법 (prototype)

```bash
# 1. RFP 원본을 sources/ 에 배치
cp ~/Downloads/some_rfp.hwpx subproducts/rfp-to-proposal/sources/

# 2. hwpx 추출 (XML 단락 → JSON)
python3 subproducts/rfp-to-proposal/tools/hwpx_extract.py \
        <unzipped_contents_dir> \
        .claude/runs/ingest_rfp/extracted.json

# 3. RFP 파싱 (요구사항 ID·카테고리 구조화)
python3 subproducts/rfp-to-proposal/tools/rfp_parser.py

# 4. inputs/ 패키지 생성 (YAML·MD)
python3 subproducts/rfp-to-proposal/tools/rfp_to_inputs.py
```

> 현재는 `tools/rfp_to_inputs.py` 안에 경로가 메인 repo 기준으로 하드코딩됨. 별도 repo 분리 시 일반화 필요.

## 6. 메인 repo 와의 관계

- **코어 vault 자산 참조 없음** — 본 sub-product 는 코어 `vault/` 를 읽지 않는다.
- **공통 인프라 일부 사용** — `flow-proposer` agent 정의(`.claude/agents/flow-proposer.md`) 는 코어 harness 의 일부지만, 본 sub-product 의 시나리오 도출에도 사용됨.
- **별도 repo 분리 시점**: sub-product 의 코드·자산이 충분히 성숙하고, 코어 harness 의존성을 줄이면 분리.

## 7. 로드맵

- **[현재]** Prototype — 본 sub-folder
- **[다음]** 제안서 작문 엔진 prototype 추가 (LLM + section template)
- **[향후]** 별도 repo 분리 (`processware-rfp-to-proposal`)
- **[장기]** SaaS 제품화

## 8. 관련 문서

- `../../docs/architecture/derivative-products.md` — 3-Vault 생태계 아키텍처
- `../../docs/architecture/` — 메인 repo 아키텍처 문서 트리
- `../../README.md` — 메인 Processware repo
