---
type: REF
doc_id: REF-002
title: "UNECE R156 (SUMS) — 소프트웨어 업데이트 관리체계 요약"
version: "0.1"
status: draft
created: 2026-06-14
updated: 2026-06-14
related_standard: VCSMS
interface_with: "ISO/SAE 21434:2021 §13.4 (Updates)"
tags: [REF, VCSMS, UNECE, R156, SUMS, OTA]
---

# REF-002 UNECE R156 — Software Update Management System

> 관련 모듈: [[적용요건|ACSMS 적용요건]] · 표준: ISO/SAE 21434 §13.4 (interface_with)

## 1. 개요
UNECE Regulation No. 156 은 차량 **소프트웨어 업데이트 관리체계(SUMS)** 와 무선(OTA) 업데이트의 안전·보안을 규제한다. R155(CSMS)와 짝을 이루는 규제로, 형식승인 단계에서 SUMS 인증을 요구한다.

## 2. ISO/SAE 21434 와의 관계 (interface)
- ISO/SAE 21434 §13.4(Updates) [RQ-13-03] 는 차량 내 업데이트·업데이트 역량을 본 표준에 따라 개발하도록 요구 → R156 SUMS 의 보안 측면과 직접 연계.
- R156 은 업데이트의 **무결성·진본성·롤백·기록·차량 식별** 등 형상/배포 관점을 추가로 규정.

## 3. 핵심 요구 (paraphrase)
- 각 차량형식의 SW 버전·하드웨어·형상 식별 및 업데이트 이력 추적.
- 업데이트가 차량 안전·법규 적합성에 미치는 영향 평가.
- 업데이트 패키지의 무결성·진본성 보호 및 실패 시 안전 상태 보장.
- OTA 업데이트의 사용자 통지·실행 조건 관리.

## 4. ACSMS 매핑 메모
| R156 영역 | VCSMS 근거 | REQ |
|---|---|---|
| 업데이트 개발·보안 | §13.4 | VCSMS-R-099 |
| 형상정보 가용성 | §5.4.4 | VCSMS-R-012 |
| 무단변경 방지(생산) | §12.4 | VCSMS-R-095 |

## source_citation
```yaml
source_citation:
  - type: industry
    file: "[inputs 미제공 — LLM 추정]"
    locator: "UNECE WP.29 R156 (Uniform provisions concerning the approval of vehicles with regard to software update and SUMS)"
    retrieved_at: "2026-06-14"
    license: "UNECE 공개 규제문서 (공공)"
    paraphrase_only: false
    note: "원문 미인제스트 — LLM 지식 기반 요약."
```
