---
type: PRO
doc_id: "PRO-MDCS-01-05"
title: "보안 문제해결 프로세스 절차"
version: "0.1"
owner: "보안책임자(PSO)"
reviewer: "보안운영위원회(PSGB)"
approver: "경영책임자(Top Management)"
scope: "취약점 접수·조사·분석·처리·공개 및 정기 검토 (Clause 9 + 4.1.7 공개)"
parent_policy: "[[POL-MDCS-01_헬스SW_제품_보안_거버넌스_방침_v0.1]]"
child_wi: []
standards: ["IEC 81001-5-1"]
tier: "C"
pro_type: core
scope_type: project
source_scenarios: []
follows: ["PRO-MDCS-01-03"]
precedes: []
interface_with: [IEC62304, "ISO/IEC 29147"]
covers_requirements: [4.1.7-REQ-001, 9.2-REQ-001, 9.2-REQ-002, 9.3-REQ-001, 9.4-REQ-001, 9.5-REQ-001, 9.5-REQ-002, 9.5-REQ-003, 9.5-REQ-004, 9.5-REQ-005, 9.5-REQ-006]
wi_sequence:
  - wi_id: WI-MDCS-01-05-01
    title: "취약점 접수 채널 및 출처별 접수·종결 추적"
    mandatory: true
    entry_condition: null
  - wi_id: WI-MDCS-01-05-02
    title: "취약점 조사(적용성·검증가능성·위협)"
    mandatory: true
    entry_condition: "WI-MDCS-01-05-01.status == done"
  - wi_id: WI-MDCS-01-05-03
    title: "취약점 분석(영향·근본원인·교차제품·안전유효성)"
    mandatory: true
    entry_condition: "WI-MDCS-01-05-02.status == done"
  - wi_id: WI-MDCS-01-05-04
    title: "보안 이슈 처리·변경영향 검토·교차통지"
    mandatory: true
    entry_condition: "WI-MDCS-01-05-03.status == done"
  - wi_id: WI-MDCS-01-05-05
    title: "취약점 공개(규제기관·사용자 통지)"
    mandatory: true
    entry_condition: "WI-MDCS-01-05-04.status == done"
  - wi_id: WI-MDCS-01-05-06
    title: "미해결 보안이슈 정기 검토(릴리스별)"
    mandatory: true
    entry_condition: null
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [PRO, MDCS, cybersecurity, vulnerability, disclosure, IEC81001-5-1]
---

# 보안 문제해결 프로세스 절차 (PRO-MDCS-01-05)

> 상위 정책: [[POL-MDCS-01_헬스SW_제품_보안_거버넌스_방침_v0.1]] · 기준: [[표준프로세스_구성원칙]]

## 1. 목적
내·외부 출처에서 보고된 헬스SW 취약점을 접수·조사·분석하고, 영향 평가와 수용 가능 잔여 리스크에 근거해 처리·공개를 결정하며, 미해결 이슈를 정기 검토하여 적시·추적 가능하게 종결한다.

## 2. 적용 범위
헬스SW 제품과 관련된 모든 보안 취약점·보안 이슈에 적용한다. 협력적 취약점 공개는 ISO/IEC 29147 을 따른다. *(향후 연계: [[IEC 62304 MDSW]] §9)* (9.1 Overview 는 서론으로 요구사항 없음 → 미커버.)

## 3. 역할과 책임 (RACI)
| 단계 | PSO | 취약점 분류자(triage) | 분석가 | 개발자 | 규제/대외 통지 | PSGB |
|---|---|---|---|---|---|---|
| 접수·추적 | C | **R** | I | I | I | I |
| 조사(적용성) | C | **R** | C | C | - | - |
| 분석(영향·근본원인) | C | C | **R** | C | - | I |
| 처리·변경영향 | **A** | C | C | **R** | - | C |
| 공개 결정·통지 | C | I | I | I | **R** | **A** |
| 정기 검토 | **R** | C | C | - | - | **A** |

## 4. 절차 흐름
```mermaid
flowchart TD
  A[취약점 접수<br/>내부/외부/연구자/29147<br/>WI-01] --> B[조사<br/>적용성·검증가능성·위협<br/>WI-02]
  B --> C[분석<br/>영향(CVSS)·근본원인·교차제품·안전유효성<br/>WI-03]
  C --> D{처리 방식}
  D -->|문제해결| E[보안 이슈 처리·변경영향 검토<br/>WI-04]
  D -->|환경명세 갱신| F[의도된 환경 명세 갱신]
  E --> G[교차 프로세스·제3자 통지]
  F --> G
  G --> H{공개<br/>대상?}
  H -->|예| I[규제기관·사용자 통지<br/>CVSS·영향버전·해결방안<br/>WI-05]
  H -->|아니오| J[종결 기록]
  I --> J
  J --> K[미해결 이슈 정기 검토<br/>릴리스별<br/>WI-06]
```

## 5. 단계별 상세
| # | 단계 | 설명 | 담당 | 입력 | 출력 |
|---|---|---|---|---|---|
| 1 | 접수 | 내부·외부·불만·연구자(29147)·광범위 출처별 보고 채널 운영·종결 추적 | 분류자 | 취약점 보고 | 접수·추적 기록 |
| 2 | 조사 | 적시 조사로 제품 적용성·검증가능성·관련 위협 판정 | 분류자 | 접수 건 | 조사 기록 |
| 3 | 분석 | 영향(보안맥락·방어심층화·CVSS)·교차제품·근본원인·안전유효성 영향 | 분석가 | 조사 결과 | 분석 보고서·근본원인 |
| 4 | 처리 | 문제해결 vs 환경명세 갱신 결정, 변경 안전·보안·유효성 영향 검토, 교차·제3자 통지 | 개발자 | 분석 결과 | 처리·통지 기록 |
| 5 | 공개 | 9.5 종결 시 규제기관·사용자에 취약점 기술·점수·영향버전·해결방안 적시 통지 | 규제/대외 | 처리 결과 | 보안권고·공개 기록 |
| 6 | 정기 검토 | 미해결 보안 이슈를 최소 각 릴리스 시 정기 검토 | PSO | 이슈 현황 | 정기 검토 기록 |

## 6. 연계 업무지침 (WI)
- [[WI-MDCS-01-05-01_취약점_접수_및_종결추적_v0.1]] — (9.2)
- [[WI-MDCS-01-05-02_취약점_조사_v0.1]] — (9.3)
- [[WI-MDCS-01-05-03_취약점_분석_v0.1]] — (9.4)
- [[WI-MDCS-01-05-04_보안이슈_처리_및_교차통지_v0.1]] — (9.5-REQ-001~005)
- [[WI-MDCS-01-05-05_취약점_공개_통지_v0.1]] — (4.1.7)
- [[WI-MDCS-01-05-06_미해결_보안이슈_정기검토_v0.1]] — (9.5-REQ-006)

## 7. 통제점 / KPI
| 통제점 | 지표 | 목표 | 주기 |
|---|---|---|---|
| 접수 응답 | 보고→조사 착수 시간 | ≤ 정책 SLA | 월 |
| 근본원인 분석 | 처리 건 RCA 수행률 | 100% | 분기 |
| 공개 적시성 | 종결→통지 리드타임 | ≤ 정책 SLA | 분기 |
| 미해결 이슈 검토 | 릴리스별 검토 수행률 | 100% | 릴리스 |

## 8. 표준 매핑 (Traceability)
| 표준 조항 | Req-ID | 반영 위치 |
|---|---|---|
| §9.2 | 9.2-REQ-001~002 | §5 단계1 |
| §9.3 | 9.3-REQ-001 | §5 단계2 |
| §9.4 | 9.4-REQ-001 | §5 단계3 |
| §9.5 | 9.5-REQ-001~005 | §5 단계4 |
| §9.5 | 9.5-REQ-006 | §5 단계6 |
| §4.1.7 | 4.1.7-REQ-001 | §5 단계5 |

> 경계면: §9.2-REQ-002(f) 는 **ISO/IEC 29147**(협력적 취약점 공개)를 직접 인용 — hard interface. IEC 62304 §9 문제해결과 연계(향후).

## 9. 출처 (source_citation)
```yaml
- type: standard_original
  file: "inputs/01_표준원문/IEC81001-5-1/requirements.yaml"
  locator: "§9.2–9.5, §4.1.7 (Software problem resolution + disclosure)"
  retrieved_at: "2026-06-18"
  license: "IEC copyright — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| v0.1 | 2026-06-18 | 최초 작성 — Clause 9 + 4.1.7 보안 문제해결·공개 프로세스 | (미승인 초안) |
