---
type: WI
doc_id: "WI-SPICE-01-02-03"
title: "SW 상세설계 및 유닛 구현 (SWE.3)"
version: "0.1"
owner: "SW Engineer"
reviewer: "SW Architect / QA"
approver: "SW Lead"
scope: "SwAD → 상세설계(모듈/함수) → MISRA-C 코딩 → 정적분석 → 코드리뷰 → 커밋"
parent_pro: "[[PRO-SPICE-01-02_소프트웨어공학프로세스]]"
related_tmp:
  - "[[TMP-SPICE-01-02-03-01_SW상세설계서및구현이력]]"
related_rec: []
standards: ["Automotive SPICE 4.0", "MISRA-C:2012", "AUTOSAR", "ISO 26262"]
aspice_processes: ["SWE.3"]
entry_gate: "WI-SPICE-01-02-02.status == done"
scope_type: "project"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SWE.3, MISRA, CodeReview]
---

# SW 상세설계 및 유닛 구현 업무지침 (WI-SPICE-01-02-03)

> 상위 절차: [[PRO-SPICE-01-02_소프트웨어공학프로세스]] §5 단계 6~8
> ASPICE 매핑: SWE.3 (Software Detailed Design and Unit Construction) — BP1~BP6

## 1. 업무 목적

SwAD 의 각 SWC 를 모듈·함수 단위로 상세설계하고, MISRA-C:2012 코딩 표준을 준수하여 소스 코드를 작성하며, 정적분석·코드리뷰를 통과한 후 형상관리 시스템에 커밋한다.

## 2. 수행 주체

- **주 수행자**: SW Engineer
- **검토자**: SW Architect (설계), 동료(코드리뷰), QA
- **승인자**: SW Lead

## 3. 범위

WI-SPICE-01-02-02 의 SwAD v1.0 베이스라인 등록 후부터 모든 유닛 코드의 정적분석·리뷰 통과 + 형상관리 시스템 커밋까지 적용한다.

## 4. 입력 자료 / 산출물

- **Input**: SwAD v1.0, Coding Standard (MISRA-C:2012, AUTOSAR C++14 Guidelines)
- **Output**: 상세설계서(Detailed Design), Source Code, 정적분석 보고서, 코드리뷰 기록, Commit Log

## 5. 수행 절차

### 5.1 사전 준비
1. IDE/컴파일러(GHS, GCC, Tasking) 버전 + 라이선스 확인.
2. 정적분석 도구(Polyspace, Coverity, LDRA) 룰셋(MISRA-C:2012 Mandatory + Required) 확정.
3. Git 브랜치 정책(예: `feat/<SWR-ID>-<short>`) 합의.

### 5.2 수행 단계

1. **모듈 상세설계** (SWE.3.BP1)
   - SWC 를 모듈(.c/.h) + 함수 시그니처로 분해.
   - 함수 명세: 입력·출력·전제조건·사후조건·예외 처리·복잡도(Cyclomatic ≤ 15).
   - 결과: TMP-SPICE-01-02-03-01 §1 "상세설계".

2. **인터페이스 설계** (SWE.3.BP2)
   - 모듈 간 함수 호출·전역변수 정의 + Header 명세.
   - Singleton·전역상태 사용은 사유 기록 필수.

3. **유닛 코딩** (SWE.3.BP3)
   - MISRA-C:2012 Mandatory 규칙 위반 0건 목표.
   - 모든 함수에 Doxygen 주석 (@param, @return, @pre, @post).
   - Magic Number 금지 — `#define` 또는 `enum` 사용.
   - 결과: Source Code (Git commit).

4. **정적분석 실행** (SWE.3.BP4)
   - 정적분석 도구로 Mandatory + Required 룰 검증.
   - Mandatory 위반: 0건 → Pass.
   - Required 위반: 사유 기록 + Architect 승인 후 Deviation 등록.
   - 결과: 정적분석 보고서.

5. **동료 코드리뷰** (SWE.3.BP5)
   - 최소 1명 동료 + Architect 1명 리뷰.
   - 리뷰 코멘트 100% 종결 (또는 사유 기록).
   - 결과: TMP-SPICE-01-02-03-01 §3 "리뷰 기록".

6. **SwAD↔코드 추적성** (SWE.3.BP6)
   - 각 SwAD 컴포넌트 ↔ 모듈/함수 매핑.

7. **형상관리 커밋** (→ SUP.8)
   - Commit Message: `[SWR-ID] <짧은 변경 요지>`.
   - PR 생성 → 자동 빌드·정적분석 Pass → Merge.
   - 결과: Commit Log + Build Artifact.

### 5.3 완료 조건 체크리스트
- [ ] 모든 함수 상세설계 작성 (입출력·전제·사후·예외)
- [ ] 모든 함수 Cyclomatic Complexity ≤ 15 (또는 사유 기록)
- [ ] MISRA-C Mandatory 위반 0건
- [ ] MISRA-C Required 위반은 Deviation 등록
- [ ] 모든 함수 Doxygen 주석 작성
- [ ] 동료 + Architect 리뷰 코멘트 종결
- [ ] SwAD↔코드 추적성 ≥ 95%
- [ ] CI 빌드 + 정적분석 Pass 후 Merge
- [ ] [[MAT-001_문서관리대장]] 갱신 (모듈 베이스라인)

## 6. 인터페이스 부서
- **SW Architect**: 설계·리뷰
- **CM (SUP.8)**: Git 형상관리
- **QA (SUP.1)**: 품질 게이트
- **Build/CI 팀**: 빌드 파이프라인

## 7. 주의사항 / 예외 처리

### 7.1 MISRA-C Required 위반 불가피
- 컴파일러 인트린식·HW 레지스터 직접 접근 등 부득이한 위반:
  - Deviation 등록 (사유·범위·완화 방안 명시).
  - SW Architect + Safety Engineer 합동 승인.
  - 코드 내 `// PRQA S xxxx` 또는 `/*lint -e xxxx*/` 주석으로 마킹.

### 7.2 동료 리뷰 부재 (단독 개발자)
- 작은 모듈 또는 단독 개발 환경:
  - SW Architect 가 동료 역할 대리 + 외부 컨설턴트 분기 1회 검토.
  - 임시 조치이며 재발 방지 위해 인력 충원 요청.

### 7.3 Hot-fix 커밋
- 양산 ECU 의 긴급 결함 수정 시:
  - PR 우회 직접 커밋 절대 금지.
  - 긴급 PR 생성 + Reviewer 즉시 승인 + 자동 정적분석 Pass 후 Merge.
  - 사후 24시간 내 정식 리뷰 + RCA 실시 (SUP.9).

### 7.4 Magic Number 미제거
- 코드 내 Magic Number 발견 시:
  - 리뷰 단계에서 즉시 차단 — `#define` 또는 `enum` 으로 치환 후 Re-PR.
  - 단위·범위 주석 강제.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-SPICE-01-02-03-01_SW상세설계서및구현이력]]
- 작성예시: [[EX-SPICE-01-02-03-01_SW상세설계서및구현이력_작성예시]]
- 기록 폴더: `vault/08_REC_기록/SWE.3/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SWE.3-PURPOSE-001 / VWAY-SWE.3-BP1~BP6"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SWE.3 BP1~BP6 + MISRA-C Deviation | (대기) |
