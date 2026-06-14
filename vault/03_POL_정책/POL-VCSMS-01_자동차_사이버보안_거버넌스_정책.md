---
type: POL
doc_id: "POL-VCSMS-01"
title: "자동차 사이버보안 거버넌스 정책"
version: "0.1"
owner: "Cybersecurity Manager (CSM)"
reviewer: "Process Control Board (PCB)"
approver: "Top Management (경영진)"
scope: "전사 도로차량 E/E 시스템 사이버보안 거버넌스 — 정책·문화·역량·도구·정보공유·지속활동·감사"
child_pro:
  - "[[PRO-VCSMS-01-01_조직_사이버보안_거버넌스_운영_절차]]"
  - "[[PRO-VCSMS-01-02_독립_조직_사이버보안_감사_절차]]"
  - "[[PRO-VCSMS-01-03_지속적_사이버보안_활동_및_취약점_관리_절차]]"
  - "[[PRO-VCSMS-01-04_사이버보안_사고_대응_절차]]"
standards: ["ISO/SAE 21434"]
area_code: VCSMS
module_display: ACSMS
layer: L2_engineering
integration_mode: interface_only
status: draft
created: 2026-06-14
updated: 2026-06-14
retention: "상시"
tags: [POL, VCSMS, ISO21434, cybersecurity, automotive, governance, interface_only]
---

# 자동차 사이버보안 거버넌스 정책 (POL-VCSMS-01)

> 상위 기준: [[표준프로세스_구성원칙]] · 문서체계: [[01_문서체계]] · 분류: [[07_표준분류레지스트리]]
> 통합방식: **interface_only** — VCSMS 전용 체계. HLS(L1) POL/PRO 에 병합하지 않으며 경계면은 "참조" 링크로만 연결.

## 1. 목적
본 정책은 당사가 개발·생산·운영·지원하는 도로차량 전기·전자(E/E) 시스템과 그 구성요소에 대해, **수명주기 전반의 사이버보안 리스크를 인지하고 관리하려는 경영진의 의지**를 천명하고, ISO/SAE 21434 가 요구하는 조직 차원의 사이버보안 거버넌스 방향을 정의한다. 정책·규칙·책임·자원·문화·역량·정보공유·지속활동·독립감사의 원칙을 제시한다.

## 2. 적용 범위
양산 도로차량의 E/E 시스템·item·component 의 사이버보안 엔지니어링을 수행·지원하는 전사 모든 조직에 적용한다. 조직 차원의 거버넌스(ISO/SAE 21434 Clause 5), 상시 수행되는 지속적 활동(Clause 8) 및 사고 대응(Clause 13.3)을 포괄한다. 프로젝트 차원의 엔지니어링 활동은 [[POL-VCSMS-02_차량_사이버보안_엔지니어링_정책]] 이 관장한다.

## 3. 정책 원칙
1. **경영 의지와 책임** — 경영진은 차량 사이버보안 리스크를 인지하고, 본 표준 이행에 필요한 책임·권한을 배정·전파하며 충분한 자원을 제공한다.
2. **규칙 기반 운영** — 사이버보안 활동을 가능케 하는 규칙·프로세스를 수립·유지하고, 인접 분야(기능안전·품질·정보보안)와 소통채널을 통해 통합한다.
3. **사이버보안 문화·역량** — 견고한 사이버보안 문화를 조성하고, 사이버보안 역할 담당자의 역량·인식을 보장한다. (역량 관리 경계면 → 상위 §7.2 참조)
4. **지속적 개선과 정보공유** — 지속적 개선 프로세스를 운영하고, 내·외부 사이버보안 정보공유의 요구·허용·금지 상황을 정의하여 정보보안을 정렬한다.
5. **독립 감사를 통한 검증** — 조직 프로세스가 본 표준 목적을 달성하는지 실행자와 독립된 주체가 정기적으로 감사한다.

## 4. 역할과 책임
| 역할 | 책임 |
|---|---|
| **Top Management (경영진)** | 정책 승인, 책임·권한 배정, 자원 제공 |
| **Cybersecurity Manager (CSM)** | 거버넌스 정책 유지·유효성 검토, 규칙·프로세스 수립, 지속활동·사고대응 총괄 |
| **Process Control Board (PCB)** | 정책 신규·개정 심의, 테일러링·예외 승인 |
| **사이버보안 감사인 (Auditor)** | 조직 프로세스 적합성 독립 감사 (실행자와 분리) |
| **사이버보안 역할 담당자** | 배정된 사이버보안 활동 수행, 역량·인식 유지 |

## 5. 준수 기준
- 모든 산출물은 `[유형]-[식별번호]_[이름]_v[버전].md` 규칙 준수 ([[02_문서번호체계]])
- 변경·문서·형상·요구사항 관리는 상위 품질경영시스템(QMS)을 **참조**한다 (interface — §5.4.4 [RQ-05-11]). 본 영역에서 중복 생성 금지.
- 작업산출물의 정보보안 관리는 상위 정보보안경영시스템(ISMS)을 **참조**한다 (interface — §5.4.6 [RC-05-16]).
- 사이버보안 역량 관리는 상위 인적자원/역량관리 프로세스를 **참조**한다 (interface — §7.2).
- 독립 감사의 독립성 원칙(auditor ≠ executor)은 상위 내부심사(§9.2)와 정합한다.

> **경계면(Interface) 표기** — 위 참조 항목은 MAT-07 Interface 테이블 등록 대상이다. 상위 L1(QMS/ISMS/HR/Audit) 과 통합하지 않고 링크로만 연결한다.

## 6. 관련 하위 절차 (PRO)
- [[PRO-VCSMS-01-01_조직_사이버보안_거버넌스_운영_절차]] — 정책·규칙·책임·문화·역량·도구·정보공유 (Clause 5)
- [[PRO-VCSMS-01-02_독립_조직_사이버보안_감사_절차]] — 조직 사이버보안 감사 (§5.4.7)
- [[PRO-VCSMS-01-03_지속적_사이버보안_활동_및_취약점_관리_절차]] — 모니터링·이벤트·취약점 (Clause 8)
- [[PRO-VCSMS-01-04_사이버보안_사고_대응_절차]] — 사고 대응 계획·이행·종료 (§13.3)

## 7. 표준 매핑 (Traceability)
| 표준 조항 | Req-ID (native) | 반영 |
|---|---|---|
| ISO/SAE 21434 §5.4.1 | VCSMS-R-001~005, 008, 009 ([RQ-05-01~05,08,09]) | §3 원칙 1·2·4 |
| ISO/SAE 21434 §5.4.2 | VCSMS-R-006, 007 ([RQ-05-06,07]) | §3 원칙 3 |
| ISO/SAE 21434 §5.4.3 | VCSMS-R-010 ([RC-05-10]) | §3 원칙 4 |
| ISO/SAE 21434 §5.4.4–5.4.6 | VCSMS-R-011~016 ([RQ/RC-05-11~16]) | §5 준수 기준 (경계면 참조) |
| ISO/SAE 21434 §5.4.7 | VCSMS-R-017 ([RQ-05-17]) | §3 원칙 5, §6 PRO-01-02 |
| ISO/SAE 21434 Clause 8 | VCSMS-R-060~067 ([RQ-08-01~08]) | §6 PRO-01-03 |
| ISO/SAE 21434 §13.3 | VCSMS-R-097, 098 ([RQ-13-01,02]) | §6 PRO-01-04 |

## 8. 출처 (source_citation)
```yaml
- type: standard_original
  file: "inputs/01_표준원문/AutoCyberSec/requirements.yaml"
  locator: "ISO/SAE 21434:2021 §5.4.1–5.4.7 (Clause 5), §8.3–8.6 (Clause 8), §13.3 (Clause 13)"
  retrieved_at: "2026-06-14"
  license: "ISO/SAE copyright"
  paraphrase_only: true
- type: standard_original
  file: "vault/02_적용요건/VCSMS_자동차사이버보안/적용요건.md"
  locator: "§3.1 Clause 5, §3.4 Clause 8, §3.9 Clause 13"
  retrieved_at: "2026-06-14"
  license: "ISO/SAE copyright"
  paraphrase_only: true
```

## 9. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-06-14 | 최초 초안 — ISO/SAE 21434 Clause 5/8/13.3 거버넌스 정책 (interface_only) | (미승인) |
