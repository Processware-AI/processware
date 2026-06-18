---
type: PRO
doc_id: "PRO-MDCS-01-04"
title: "보안 형상관리 프로세스 절차"
version: "0.1"
owner: "보안책임자(PSO)"
reviewer: "보안운영위원회(PSGB)"
approver: "경영책임자(Top Management)"
scope: "헬스SW 변경통제·변경이력·외부 컴포넌트 인벤토리(SBOM) 재현 능력 (Clause 8)"
parent_policy: "[[POL-MDCS-01_헬스SW_제품_보안_거버넌스_방침_v0.1]]"
child_wi: []
standards: ["IEC 81001-5-1"]
tier: "S"
pro_type: support
scope_type: project
source_scenarios: []
follows: ["PRO-MDCS-01-02"]
precedes: []
interface_with: [IEC62304, ISO13485]
covers_requirements: [8-REQ-001, 8-REQ-002]
wi_sequence:
  - wi_id: WI-MDCS-01-04-01
    title: "보안 변경통제 및 변경이력 관리"
    mandatory: true
    entry_condition: null
  - wi_id: WI-MDCS-01-04-02
    title: "외부 컴포넌트 인벤토리(SBOM) 구성·재현"
    mandatory: true
    entry_condition: null
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [PRO, MDCS, cybersecurity, configuration_management, SBOM, IEC81001-5-1]
---

# 보안 형상관리 프로세스 절차 (PRO-MDCS-01-04)

> 상위 정책: [[POL-MDCS-01_헬스SW_제품_보안_거버넌스_방침_v0.1]] · 기준: [[표준프로세스_구성원칙]]

## 1. 목적
헬스SW 의 개발·유지보수·지원 전반에 변경통제와 변경이력을 포함한 형상관리를 적용하고, 출시·시판 중인 헬스SW 의 보안 의무를 위해 취약해질 수 있는 **외부 컴포넌트 목록(SBOM)을 재현**할 수 있는 능력을 보장한다.

## 2. 적용 범위
보안 수명주기가 적용되는 헬스SW 의 모든 구성 항목 및 외부 컴포넌트에 적용한다. *(향후 연계: [[IEC 62304 MDSW]] §8 / [[ISO 13485 MDQMS]] §7.5)*

## 3. 역할과 책임 (RACI)
| 단계 | PSO | 형상관리 담당 | 개발자 | 변경통제위원회(CCB) |
|---|---|---|---|---|
| 변경통제·이력 | C | **R** | C | **A** |
| 외부 컴포넌트 인벤토리(SBOM) | **A** | **R** | C | I |

## 4. 절차 흐름
```mermaid
flowchart TD
  A[형상 항목 식별·기준선 설정] --> B[변경 요청 접수]
  B --> C[변경통제위원회 심의<br/>보안 영향 평가]
  C --> D{승인?}
  D -->|예| E[변경 반영·이력 기록<br/>WI-01]
  D -->|아니오| F[반려·기록]
  E --> G[외부 컴포넌트 인벤토리 갱신<br/>SBOM 재현 가능 유지<br/>WI-02]
  G --> H[형상 상태 보고]
```

## 5. 단계별 상세
| # | 단계 | 설명 | 담당 | 입력 | 출력 |
|---|---|---|---|---|---|
| 1 | 변경통제 | 변경 요청·심의(보안 영향)·승인·반영·이력 기록 | 형상관리 담당 | 변경 요청 | 변경통제 기록·변경 이력 |
| 2 | 컴포넌트 인벤토리 | 출시 SW 의 외부 컴포넌트 목록 작성·갱신, 취약점 추적 위한 SBOM 재현 능력 유지 | 형상관리 담당 | 빌드 산출물 | SBOM·구성관리 기록 |

## 6. 연계 업무지침 (WI)
- [[WI-MDCS-01-04-01_보안_변경통제_및_변경이력_v0.1]] — (8-REQ-001)
- [[WI-MDCS-01-04-02_외부_컴포넌트_인벤토리_SBOM_v0.1]] — (8-REQ-002)

## 7. 통제점 / KPI
| 통제점 | 지표 | 목표 | 주기 |
|---|---|---|---|
| 변경 이력 완전성 | 승인 변경 대비 이력 기록률 | 100% | 월 |
| SBOM 최신성 | 출시 SW 대비 SBOM 보유율 | 100% | 릴리스 |
| 컴포넌트 재현 | 과거 릴리스 구성 재현 가능률 | 100% | 분기 |

## 8. 표준 매핑 (Traceability)
| 표준 조항 | Req-ID | 반영 위치 |
|---|---|---|
| §8 | 8-REQ-001 | §5 단계1 |
| §8 | 8-REQ-002 | §5 단계2 |

> 출처 주의: source_map 상 Clause 8 의 페이지 미상(`page: 0`) — 조항은 확정, 페이지는 차후 보정 필요(적용요건 §5 플래그). 경계면: IEC 62304 §8 / ISO 13485 §7.5 (향후 연계).

## 9. 출처 (source_citation)
```yaml
- type: standard_original
  file: "inputs/01_표준원문/IEC81001-5-1/requirements.yaml"
  locator: "§8 (Software CONFIGURATION MANAGEMENT PROCESS) — page 미상"
  retrieved_at: "2026-06-18"
  license: "IEC copyright — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| v0.1 | 2026-06-18 | 최초 작성 — Clause 8 보안 형상관리 프로세스 | (미승인 초안) |
