---
type: WI
doc_id: "WI-CMMI-01-02-02"
title: "OSSP 개발 및 유지"
version: "1.0"
owner: "SEPG Lead"
reviewer: "PCB"
approver: "CEO"
scope: "조직 표준 프로세스 세트(OSSP) 의 신규 개발·개정·폐기"
parent_pro: "[[PRO-CMMI-01-02_프로세스_자산_개발_절차_v1.0]]"
parent_pol: "[[POL-CMMI-01_거버넌스_및_프로세스자산_정책_v1.0]]"
related_tmp:
  - "[[TMP-CMMI-01-02-02-01_OSSP_개정요청서_v1.0]]"
related_ex:
  - "[[EX-CMMI-01-02-02-01_OSSP_개정요청서_작성예시_v1.0]]"
standards: ["CMMI-DEV-ML3"]
scope_code: "CMMI"
status: approved
created: 2026-04-29
updated: 2026-04-29
tags: [WI, CMMI, PAD]
---

# OSSP 개발 및 유지 (WI-CMMI-01-02-02)

> 상위 절차: [[PRO-CMMI-01-02_프로세스_자산_개발_절차_v1.0]]

## 1. 업무 목적
조직 표준 프로세스 세트(OSSP=POL+PRO+WI+TMP) 의 신규 개발·개정·폐기를 통제된 절차로 수행하여, 프로세스 자산이 항상 최신·정합 상태가 되도록 한다.

## 2. 수행 주체
- 주 수행자: 자산 작성자(Process Owner 또는 SEPG)
- 검토자: PCB·법무·QA
- 승인자: CEO(중대) / SEPG Lead(경미)

## 3. 범위
- vault/03~07 의 POL/PRO/WI/TMP/EX 전체

## 4. 입력 / 산출물
- Input: 식별표, 개정요청서, 외부 표준 변경
- Output: 신규/개정/폐기 자산, [[MAT-001_문서관리대장]] Row

## 5. 수행 절차

### 5.1 사전 준비
1. 변경 요지·영향 평가 작성.
2. 골든샘플·템플릿 확인.

### 5.2 수행 단계
1. **개발/개정 작성** — 골든샘플 기준선 충족.
2. **PCB 검토** — 비즈니스 정합·골든샘플 충족 검증.
3. **법무·QA 검토** — 라이선스·중립성·QA 가능성.
4. **승인** — 중대 변경 CEO, 경미 SEPG Lead.
5. **PAL 등재** — vault 디렉토리 + 인덱스 갱신.
6. **공지** — 사내 공지·교육 자료 갱신.

### 5.3 완료 조건
- [ ] 자산 승인본 PAL 등재
- [ ] [[MAT-001_문서관리대장]] Row
- [ ] 영향받는 프로젝트 통보

## 6. 인터페이스 부서
- PCB, 법무, QA, OT

## 7. 주의사항 / 예외 처리

### 7.1 긴급 개정
- 법규·보안 이슈 시 SEPG Lead 가 선반영, 48시간 내 정식 결재.

### 7.2 외부 표준 라이선스
- ISO/CMMI 등 원문 paraphrase 만 허용, 직접 인용 시 출처 + 라이선스 명기.

### 7.3 폐기
- `99_폐기_보관/` 이동, `superseded_by` 메타 갱신.

## 8. 연계 템플릿
- [[TMP-CMMI-01-02-02-01_OSSP_개정요청서_v1.0]]
- [[EX-CMMI-01-02-02-01_OSSP_개정요청서_작성예시_v1.0]]

## 9. KPI
| 지표 | 목표 | 주기 |
|---|---|---|
| 개정요청 처리 리드타임 | ≤ 30영업일 | 분기 |
| 자산 갱신 적시성 | ≥ 95% | 분기 |
| 라이선스 위반 부적합 | 0건 | 분기 |

## 10. 출처
```yaml
- type: standard_original
  file: "_inputs/01_표준원문/CMMI-DEV/Core PAs/PAD.pdf"
  locator: "PAD 2.2 — develop and maintain OSSP"
  license: "ISACA copyright — paraphrase only"
  paraphrase_only: true
```

## 11. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 1.0 | 2026-04-29 | 최초 승인 | CEO |
