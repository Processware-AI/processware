---
type: EX
doc_id: EX-CMMI-03-02-03-01
title: "인터페이스 설계 명세서 (ICD) 작성예시"
version: "0.1"
owner: "Lead Architect"
parent_tmp: "[[TMP-CMMI-03-02-03-01_인터페이스_설계_명세서_ICD]]"
standards: [CMMI-DEV-ML3-V1.3]
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
status: draft
created: 2026-05-11
updated: 2026-05-11
tags: [EX, CMMI, TS, sample]
---

# 인터페이스 설계 명세서 (ICD) 작성예시 (EX-CMMI-03-02-03-01)

> 원본 양식: [[TMP-CMMI-03-02-03-01_인터페이스_설계_명세서_ICD]]

## 샘플 컨텍스트
"알파-MES v2" — ERP-MES 인터페이스 ICD.

## 1. 문서 정보 (샘플)
| 항목 | 예시값 |
|---|---|
| 문서번호 | ICD-2026-007 |
| 버전 | 1.0 |
| 프로젝트 | 알파-MES-v2 |
| 작성자 | 한OO (Architect) |
| 작성일 | 2026-07-10 |
| 검토자 | 박OO (PI Lead), 정OO (PM), C-06 Owner 김OO, ERP 측 이OO |
| 승인자 (PM) | 정OO |
| 입력 IR 정의서 | IR-SPEC-2026-007 v1.1 |

## 2. 적용 표준 (샘플)
| 표준 | 적용 항목 |
|---|---|
| 사내 REST 가이드 v4 | URL/HTTP 코드/오류 페이로드 |
| ASN.1·EDI X12 표준 | AS2 배치 메시지 |
| OpenAPI 3.1 | 모든 REST ICD 스키마 |
| OWASP ASVS L2 | 보안 통제 |

## 3. ICD 본 표 (샘플 일부)
| ICD-ID | IR-ID | From↔To | 스키마 | 프로토콜 | SLA | 에러/재시도 | 관측성 | 버전 정책 | 비표준 사유 |
|---|---|---|---|---|---|---|---|---|---|
| ICD-EXT-01 | IR-EXT-01 | ERP→C-06 | openapi/work-order.yaml v1.2 | REST/HTTPS | 99.9%, p95 ≤ 800ms | 5xx Retry-3 (지수 100→200→400ms), DLQ 적재 | Prometheus + Trace ID 전파 | URI v1, deprecated 6개월 전 통지 | - |
| ICD-EXT-02 | IR-EXT-02 | C-06→ERP | EDI X12 856 | AS2 1.1 | 99.5%, 1회/일 | 미수신시 12h 후 알림, 재전송 자동 | 송수신 로그·MIC 보존 | EDI 표준 버전 명시 | - |
| ICD-EXT-03 | IR-EXT-03 | C-01→Okta | OIDC ID Token | OIDC 1.0 | 99.95% | 401/403 시 토큰 갱신 | Audit 로그 | OIDC 1.0 + nonce 강제 | - |
| ICD-INT-01 | IR-INT-01 | C-02→C-03 | proto3 (workorder.proto) | Kafka 3.5 | end-to-end ≤ 3s | consumer lag 임계 알림, 멱등 키 | Kafka exporter | Schema Registry + backward compat | - |

## 4. 스키마 첨부 (샘플)
> `openapi/work-order.yaml v1.2`, `proto/workorder.proto`, `schemas/edi-856.x12` 외부 파일 첨부.

## 5. 검토 결과 (샘플)
| 항목 | 내용 |
|---|---|
| 검토 일자 | 2026-07-08 |
| 참여자 | PI Lead, C-06 Owner, ERP 측 Architect, Architect |
| 결함 수 | 5 (Major 1, Minor 4) |
| 해소 상태 | 전체 해소 (2026-07-10) |

## 6. PI 인계 (샘플)
| 항목 | 내용 |
|---|---|
| 인계 송부 ID | PI-HOI-2026-007 |
| 인계 일자 | 2026-07-11 |
| 수신자 | 박OO (PI Lead) |

## 7. 결재 (샘플)
| 검토 | 승인 | 일자 |
|---|---|---|
| 박OO (PI), 김OO (C-06) | 정OO (PM) | 2026-07-11 |

## 작성 시 유의사항
- 7요소(스키마·프로토콜·SLA·에러·재시도·관측·버전) 누락 시 ICD 미완료.
- 외부 합의 인터페이스는 양 측 검토자 참여 의무.
- 스키마는 본문에 통째로 붙이지 말고 외부 파일 ID 참조.

## 잘못된 작성 사례
> ❌ "ERP 와 REST 로 연동" — 7요소 거의 누락
> ✅ ICD-EXT-01 처럼 모든 요소 명시

> ❌ 외부 시스템 측 검토자 미참여
> ✅ ERP 측 Architect 합동 검토 필수
