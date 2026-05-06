---
doc_id: "EX-ASPICE-01-05-05-01"
title: "OEM 인도 확인서 작성예시"
type: EX
version: "0.1"
status: draft
parent_tmp: "[[TMP-ASPICE-01-05-05-01_OEM인도확인서]]"
scope_type: project
scope_code: ASPICE
domain: ASPICE
created: "2026-05-06"
updated: "2026-05-06"
tags: [EX, sample, ASPICE, SPL.2, OEM]
---

# OEM 인도 확인서 (작성예시)

> 본 문서는 작성예시입니다. 가공의 회사·프로젝트 정보를 사용합니다.

## 작성 정보
| 항목 | 내용 |
|------|------|
| 프로젝트명 | ABC Motors Co., Ltd. — ADAS Domain Controller 개발 |
| 인도 대상 OEM | Global Auto Inc. (Tier-1 OEM) |
| 문서 번호 | ABC-ADAS-2026-001-DEL-001 |
| 작성자 | 이매니저 (Project Manager) |
| 검토자 | 정품질 (QA), 박법무 (Legal), 한CM (CM) |
| 승인자 | 강프로그램 (Program Director) |
| 인도 일자 | 2026-05-06 |

## 1. 인도 항목 목록
| 파일명 | 버전 | SHA-256 체크섬 | 비고 |
|--------|------|------------------|------|
| ADAS_SW_v1.0.0.bin | v1.0.0 | abc1230f...a91b | ECU flash image |
| Release_Notes_v1.0.0.pdf | v1.0.0 | def4561a...c702 | 릴리즈 노트 |

## 2. 전달 방법 및 채널
| 항목 | 내용 |
|------|------|
| 전송 채널 | OEM Global Auto Inc. SFTP Portal |
| 채널 ID/링크 | sftp://delivery.global-auto.com/abc-motors/2026-05-06/ |
| 전송 시작 일시 | 2026-05-06 10:30:12 KST |
| 전송 완료 일시 | 2026-05-06 10:34:48 KST |
| 암호화 방식 | SFTP (SSH-2 / AES-256) + manifest RSA-PSS-3072 서명 |

## 3. 수출통제 검토 결과
| 항목 | 내용 |
|------|------|
| 분류 (EAR/ITAR/EAR99) | EAR99 |
| 검토자 | 박법무 (Legal Counsel) |
| 검토 일자 | 2026-05-05 |
| 결과 | 통제 대상 아님 — 인도 가능 |

## 4. OEM 수령 확인
| 항목 | 내용 |
|------|------|
| 수령 담당자 (성명/소속) | 김글로벌 (Global Auto Inc. Procurement) |
| 수령 확인 방법 (서명/이메일) | 회신 이메일 + 디지털 서명 PDF |
| 수령 확인 일시 | 2026-05-06 14:22:15 KST |
| 회신 메시지 ID/첨부 | <20260506-1422-globalauto@global-auto.com> + ReceiptConfirmation.pdf |

| 서명자 | 서명 | 일자 |
|--------|------|------|
| OEM 수령 담당자 (김글로벌) | (디지털 서명) | 2026-05-06 |

## 5. 인도 후 지원 약정
| 항목 | 내용 |
|------|------|
| 지원 기간 | 인도일로부터 3개월 (2026-05-06 ~ 2026-08-06) |
| 지원 채널 | 전용 Slack 채널 #abc-globalauto-support, 이메일 support@abc-motors.example |
| 응답 SLA | Critical 4시간, High 1영업일, Medium 3영업일 |
| 결함 보고 채널 | OEM JIRA Project: GA-ADAS-DEFECTS |

## 6. 인도 완료 선언 / 승인
| 역할 | 성명 | 서명 | 일자 |
|------|------|------|------|
| 작성자(PM) | 이매니저 | (서명) | 2026-05-06 |
| 검토자(QA) | 정품질 | (서명) | 2026-05-06 |
| 검토자(Legal) | 박법무 | (서명) | 2026-05-06 |
| 검토자(CM) | 한CM | (서명) | 2026-05-06 |
| 승인자(Program Director) | 강프로그램 | (서명) | 2026-05-06 |

## 작성 요령
- 전송 채널은 암호화 채널만 허용 (SFTP/HTTPS Portal). 이메일 첨부 금지.
- OEM 수령 확인은 이메일 회신 또는 서명 PDF 둘 중 하나 이상 보존.
- 수출통제 검토는 인도 전에 반드시 완료하고 결과를 명시한다.

## 잘못된 사례
- 평문 이메일로 바이너리 첨부 → 보안 정책 위반.
- 수령 확인을 구두로만 받음 → 계약 이행 입증 부실.
- 지원 SLA 공란 → 인도 후 분쟁 소지.
