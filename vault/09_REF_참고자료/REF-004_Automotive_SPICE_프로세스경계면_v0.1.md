---
type: REF
doc_id: REF-004
title: "Automotive SPICE (ASPICE) — 프로세스 성숙도 경계면 요약"
version: "0.1"
status: draft
created: 2026-06-14
updated: 2026-06-14
related_standard: VCSMS
area_code_ref: SPICE
interface_with: "ISO/SAE 21434 Clause 6/10 (관리·개발 프로세스)"
tags: [REF, VCSMS, SPICE, ASPICE, process-maturity]
---

# REF-004 Automotive SPICE — 프로세스 경계면

> 관련 모듈: [[적용요건|ACSMS 적용요건]] · 영역코드 SPICE(별도 빌드 대상) · 표준: ISO/SAE 21434 (interface_with)

## 1. 개요
Automotive SPICE(ASPICE)는 자동차 SW·시스템 개발 **프로세스 성숙도(capability) 평가 모델**이다. ISO/SAE 21434 의 엔지니어링 활동(계획·요구·설계·통합·검증)은 ASPICE 프로세스 위에서 수행되는 경우가 많아 프로세스 정의·관리 측면에서 경계면을 형성한다.

## 2. ISO/SAE 21434 와의 관계 (interface)
- ASPICE 는 *프로세스를 어떻게 정의·관리·개선하는가(capability)* 를, ISO/SAE 21434 는 *사이버보안 활동의 내용(what)* 을 규정 → 상호 보완.
- 변경관리(SUP.10), 형상관리(SUP.8), 문제해결(SUP.9), 품질보증(SUP.1) 등 지원 프로세스가 §5.4.4 QMS 경계면과 정합.
- 최근 ASPICE for Cybersecurity(PAM) 확장이 ISO/SAE 21434 활동을 직접 프로세스화.

## 3. ACSMS 매핑 메모
| ASPICE 프로세스군 | VCSMS 근거 | REQ |
|---|---|---|
| MAN.3 프로젝트관리 | Clause 6 (계획) | VCSMS-R-018~031 |
| SUP.8/10 형상·변경 | §5.4.4 | VCSMS-R-011, R-028~029 |
| SWE/SYS 개발 | Clause 9·10 | VCSMS-R-068~091 |
| ACQ 공급자관리 | Clause 7 | VCSMS-R-052~059 |

## source_citation
```yaml
source_citation:
  - type: industry
    file: "[inputs 미제공 — LLM 추정]"
    locator: "Automotive SPICE PAM (VDA QMC) + Cybersecurity extension"
    retrieved_at: "2026-06-14"
    license: "VDA QMC — 발행처 라이선스 확인 필요"
    paraphrase_only: true
    note: "ASPICE 원문 미인제스트. SPICE 영역 별도 빌드 시 상세화."
```
