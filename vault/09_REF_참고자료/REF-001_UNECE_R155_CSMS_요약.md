---
type: REF
doc_id: REF-001
title: "UNECE R155 (CSMS) — 차량형식승인 사이버보안 규제 요약"
version: "0.1"
status: draft
created: 2026-06-14
updated: 2026-06-14
related_standard: VCSMS
interface_with: "ISO/SAE 21434:2021 Clause 5-8"
tags: [REF, VCSMS, UNECE, R155, CSMS, regulation]
---

# REF-001 UNECE R155 — Cyber Security Management System

> 관련 모듈: [[적용요건|ACSMS 적용요건]] · 표준: ISO/SAE 21434 (interface_with)

## 1. 개요
UNECE Regulation No. 155 는 차량 형식승인(type approval) 단계에서 제조사가 **사이버보안 경영체계(CSMS)** 를 보유·운영할 것을 요구하는 국제 자동차 규제다. EU·일본·한국 등 WP.29 1958 협정 가입국에서 신차 형식승인 요건으로 적용된다.

## 2. ISO/SAE 21434 와의 관계 (interface)
- R155 는 *무엇을(what)* 요구하는 규제, ISO/SAE 21434 는 *어떻게(how)* 충족하는 엔지니어링 표준이다.
- R155 의 CSMS 적합성 입증에 ISO/SAE 21434 프로세스가 사실상의 표준 수단으로 인용된다.
- 경계면: 조직 거버넌스(Clause 5), 공급망(Clause 7), 지속적 모니터링·취약점·사고대응(Clause 8·13).

## 3. 핵심 요구 (paraphrase)
- 전 수명주기(개발·생산·사후)에 걸친 리스크 식별·평가·관리 프로세스 보유.
- 사이버보안 위협 모니터링·탐지·대응 및 인시던트 보고 능력.
- 공급망(공급자·하청) 사이버보안 리스크 관리.
- CSMS 의 적합성 인증서(Certificate of Compliance) 확보 및 차량형식별 적용 입증.

## 4. ACSMS 매핑 메모
| R155 영역 | VCSMS 근거 | REQ |
|---|---|---|
| 조직 거버넌스 | Clause 5 | VCSMS-R-001~017 |
| 모니터링·취약점 | Clause 8 | VCSMS-R-060~067 |
| 사고 대응 | Clause 13 | VCSMS-R-097~098 |
| 공급망 | Clause 7 | VCSMS-R-052~059 |

## source_citation
```yaml
source_citation:
  - type: industry
    file: "[inputs 미제공 — LLM 추정]"
    locator: "UNECE WP.29 R155 (Uniform provisions concerning the approval of vehicles with regard to cyber security and CSMS)"
    retrieved_at: "2026-06-14"
    license: "UNECE 공개 규제문서 (공공)"
    paraphrase_only: false
    note: "원문 미인제스트 — 본 REF 는 LLM 지식 기반 요약. design 단계 원문 확보 권고."
```
