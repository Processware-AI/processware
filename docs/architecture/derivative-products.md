---
type: architecture
title: 파생 프로덕트 아키텍처 — 3-Vault 생태계
version: "0.1"
status: draft
updated: 2026-05-13
tags: [architecture, derivative-products, vision]
---

# 파생 프로덕트 아키텍처 — Processware 3-Vault 생태계

## 1. 개요

본 문서는 Processware 메인 프로젝트(코어 vault)와 그 위에 파생될 **2개 별도 프로덕트**의 비전·경계·인터페이스를 정의한다.

**핵심 원칙**: 세 vault 는 **각자 독립된 자산 체계**이며, 구조도 내용도 다르다. 결합점은 파생 ② 하나뿐이다.

---

## 2. 3-Tier 비전

```
┌──────────────────────────────────────────────────────────────────────┐
│  📦 코어 vault — Processware                                         │
│  본 repo (이 디렉토리)                                               │
│                                                                      │
│   입력: 국제표준 / 법규 / 산업가이드                                 │
│   출력: POL / PRO / WI / TMP / EX / MAT / REF                        │
│   특징: 조직이 항상 따르는 표준 프로세스 자산                        │
│   영속성: 표준 개정 주기 (수년)                                      │
└──────────────────────────────────────────────────────────────────────┘
              │ 자산 참조
              │ (파생 ② 에서만 결합)
              ↓
┌─────────────────────────────────────┐    ┌──────────────────────────────────────┐
│  🤖 파생 ① — RFP-to-Proposal        │    │  🛠 파생 ② — Project Asset Generator │
│  (별도 repo, 향후 분리 예정)        │    │  (별도 repo, 향후 분리 예정)         │
│                                     │    │                                      │
│   입력: 발주처 RFP                  │    │   입력: 파생 ① vault 의 제안서       │
│         (PDF/DOCX/HWPX 임의 형식)   │    │         + 코어 vault 표준 자산       │
│   출력: 응시자 제안서 (Proposal)    │    │   출력: 사업 산출물                  │
│   vault 구조: 제안서 구성요소       │    │           - 사업수행계획서           │
│           - 사업이해                │    │           - WBS                      │
│           - 수행방안                │    │           - 요구사항정의서           │
│           - 방법론                  │    │           - 설계서                   │
│           - 조직·인력               │    │           - 시험계획서               │
│           - 품질·보안               │    │           - 검수보고서               │
│           - 일정·예산               │    │                                      │
│   영속성: 입찰 사례별 누적          │    │   영속성: 수주 사업별 누적           │
└─────────────────────────────────────┘    └──────────────────────────────────────┘

   ── 입찰 응시 단계 ──                          ── 사업 실행 단계 ──
```

---

## 3. 세 vault 의 비교

| 측면 | 코어 vault | 파생 ① vault | 파생 ② vault |
|---|---|---|---|
| **본질** | 조직의 영속 자산 | 입찰 응시 자산 | 수주 사업 산출물 |
| **주된 자산 단위** | POL · PRO · WI · TMP · EX | 제안서 섹션 모듈 | 산출물 문서 모듈 |
| **추적성 매트릭스** | MAT-001~010 + MAT-011~ 표준별 | 별도 — 입찰사례별 | 별도 — 수주사업별 |
| **영역코드 의미** | 표준 (QMS·ISMS·CMMI·…) | 제안서 도메인 (SI·컨설팅·구축…) | 사업 단계·도메인 |
| **재사용 패턴** | 모든 사업이 항상 참조 | 유사 RFP 끼리 재사용 | 후속 사업에서 부분 재사용 |
| **갱신 빈도** | 표준 개정 시 (수년) | 입찰 시도마다 (주~월) | 사업 수행 중 (일~주) |
| **인스턴스 수 (가정)** | 표준 N건 (소수, 영속) | 입찰 사례 M건 (다수, 누적) | 수주 사업 P건 (다수, 누적) |
| **외부 비공개 자료 정도** | 표준 원문 (저작권) | RFP (저작권·NDA) + 응시 전략 (기밀) | 사업 수행 데이터 (기밀·개인정보) |

---

## 4. 인터페이스 정의

### 4.1 파생 ① → 파생 ② 인터페이스

파생 ① 의 vault 에서 파생 ② 의 입력으로 넘어가는 데이터:

```yaml
# proposal_artifact.yaml (파생 ① 출력 = 파생 ② 입력)
proposal_id: PROP-2026-001
project_name: "보건환경종합정보시스템 고도화 사업"
client: "대구광역시 보건환경연구원"
status: submitted | won | lost
sections:
  - section_id: business_understanding
    content_ref: "...vault/.../section.md"
  - section_id: execution_plan
    content_ref: "..."
  - section_id: methodology
    content_ref: "..."
  # ...
referenced_standards:    # 코어 vault 에서 참조한 표준 (감사 추적)
  - CMMI-DEV-ML3-V1.3
  - ISO9001
mapped_requirements:     # 정규화된 RFP 요구사항 (중간 산출물)
  rfp_normalized_ref: "..."
```

### 4.2 코어 vault → 파생 ② 인터페이스

파생 ② 가 코어 vault 의 표준 자산을 읽어 사업 산출물의 표준 절차 부분을 자동 채움:

```yaml
# project_asset_generation_config.yaml (파생 ② 측 설정)
core_vault_path: "../processware/vault"
referenced_assets:
  - POL-QMS-001
  - PRO-CMMI-04-01
  - WI-CMMI-04-01-03
  - TMP-CMMI-04-01-03-01
mapping_rules:
  사업수행계획서:
    - source: PRO-CMMI-04-01
      target_section: §5 프로젝트 관리
```

### 4.3 코어 vault → 파생 ① (참조 만, 결합 안 함)

파생 ① 은 코어 vault 를 **읽기 전용으로 참조**할 수 있으나(제안서의 "당사 표준 프로세스" 섹션 등), 결합 대상은 아니다. 파생 ① 의 vault 는 독립적으로 구성된다.

---

## 5. 현재 상태 및 분리 로드맵

### 5.1 현재 단계 (2026-05-13 — 모든 분리 단계 완료)

| 구성 요소 | 위치 | 상태 |
|---|---|---|
| 코어 vault | `vault/` (본 repo) | 표준 빌드 미시작 — 인프라·하네스만 운영 |
| 파생 ① | [processware-rfp-to-proposal](https://github.com/Processware-AI/processware-rfp-to-proposal) (별도 repo) | **별도 repo 분리 완료** — prototype 단계 |
| 파생 ② | 미착수 | 설계 단계 |

### 5.2 분리 로드맵 (완료 이력)

| 단계 | 작업 | 일자 | 상태 |
|---|---|---|---|
| **[C]** 아키텍처 문서화 | 본 문서 작성 | 2026-05-13 | ✅ 완료 |
| **[A]** Sub-folder 격리 | `subproducts/rfp-to-proposal/` 로 코드·자산 격리 | 2026-05-13 | ✅ 완료 |
| **[B]** 별도 repo 분리 | `processware-rfp-to-proposal` repo spawn + 본 repo `subproducts/` 제거 | 2026-05-13 | ✅ 완료 |

### 5.3 중장기 로드맵

- 파생 ② 의 설계·구현 (2026 Q4 이후)
- 파생 ①/② 의 SaaS 제품화 (2027~)
- 코어 vault 의 표준 라이브러리 확충 (ISO 9001 / 27001 / 13485 / IATF 16949 / 개인정보보호법 / NIST CSF 등)

---

## 6. 본 메인 repo 의 본업 재확인

본 Processware 메인 repo 는 **코어 vault 구축**에 집중한다:

- ✅ 본 repo 의 input 카테고리(`inputs/01_표준원문/`, `inputs/02_법규/`, `inputs/03_해설서/`, `inputs/05_산업가이드/`)는 **표준·법규·가이드** 만 받는다.
- ✅ `inputs/04_AsIs/` 는 **기존 조직 내부 표준 자산**(현 품질매뉴얼·기존 절차서 등) 만 받는다.
- ❌ **RFP·발주문서·SoW·고객 입찰 명세 등은 본 repo 의 입력이 아니다** — 이들은 별도 repo [processware-rfp-to-proposal](https://github.com/Processware-AI/processware-rfp-to-proposal) (파생 ①) 영역.
- ❌ 본 repo 에서 `/process-plan "RFP기반-사업명"` 같은 호출은 부적합 — RFP 는 표준이 아니므로 vault 의 영속 자산이 될 수 없다.

본 경계가 흐려지면 vault 가 오염되고, 표준 자산의 재사용성이 떨어진다.

---

## 7. 관련 문서

- `vault/00_공통관리/01_문서체계.md` — 8종 문서 유형 (POL/PRO/WI/TMP/EX/REC/MAT/REF)
- `vault/00_공통관리/02_문서번호체계.md` — MAT 번호 할당 원칙
- `vault/00_공통관리/07_표준분류레지스트리.md` — 표준 분류 3축 (Layer/Structure/Integration)
- [processware-rfp-to-proposal/README.md](https://github.com/Processware-AI/processware-rfp-to-proposal/blob/main/README.md) — 파생 ① 현 상태 및 사용법 (별도 repo)
