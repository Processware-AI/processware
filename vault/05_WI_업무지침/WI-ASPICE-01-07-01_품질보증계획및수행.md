---
type: WI
doc_id: "WI-ASPICE-01-07-01"
title: "품질보증 계획 및 수행 (SUP.1)"
version: "0.1"
owner: "QA Lead"
reviewer: "Process Quality Office"
approver: "CTO"
scope: "QA 계획 수립 → 산출물·프로세스 감사 → 부적합 추적 → 시정 폐쇄"
parent_pro: "[[PRO-ASPICE-01-07_품질보증및지원프로세스]]"
related_tmp: []
related_rec: []
standards: ["Automotive SPICE 4.0", "ISO 9001"]
aspice_processes: ["SUP.1"]
entry_gate: null
scope_type: "common"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, SUP.1, QA, Audit]
---

# 품질보증 계획 및 수행 업무지침 (WI-ASPICE-01-07-01)

> 상위 절차: [[PRO-ASPICE-01-07_품질보증및지원프로세스]]
> ASPICE 매핑: SUP.1 (Quality Assurance) — BP1~BP6

## 1. 업무 목적

프로젝트의 산출물과 프로세스가 정의된 표준·계획에 부합하는지 독립적으로 보증하고, 부적합 발견 시 시정조치를 추적·폐쇄한다.

## 2. 수행 주체
- **주 수행자**: QA Engineer
- **검토자**: Process Quality Office
- **승인자**: CTO (QA 독립성 원칙)

## 3. 범위
프로젝트 착수 시점부터 종료 시점까지 모든 산출물·프로세스에 적용한다.

## 4. 입력 자료 / 산출물
- **Input**: 프로젝트 계획, 표준 매뉴얼, 산출물·프로세스
- **Output**: QA Plan, 감사 보고서, 부적합(NCR) 보고서, 시정조치 추적 대장

## 5. 수행 절차

### 5.1 사전 준비
1. QA 인력의 독립성 확인 (개발 라인 비참여).
2. 감사 체크리스트 표준화 (산출물 유형별).

### 5.2 수행 단계

1. **QA 계획 수립** (SUP.1.BP1)
   - 감사 대상 산출물·프로세스·주기 정의.
   - QA 자원·일정 확정 + PM 합의.

2. **산출물 감사** (SUP.1.BP2)
   - 마일스톤별 산출물 vs 표준 비교.
   - 결함·부적합 식별 + NCR 발행.

3. **프로세스 감사** (SUP.1.BP3)
   - 프로세스 준수 여부 점검 (예: SwRS 베이스라인 절차).

4. **부적합(NCR) 추적** (SUP.1.BP4)
   - NCR 별 책임자·기한·시정조치 등록.
   - 폐쇄 효과성 검증.

5. **에스컬레이션** (SUP.1.BP5)
   - 폐쇄 지연 또는 반복 부적합 발생 시 PM·CTO 보고.

6. **QA 보고** (SUP.1.BP6)
   - 정기(월간) QA 보고서 작성 + 경영검토 입력.

### 5.3 완료 조건 체크리스트
- [ ] QA Plan 의 감사 일정 100% 실행
- [ ] 산출물 감사 결과 문서화 + 부적합 NCR 등록
- [ ] 프로세스 감사 체크리스트 100% 실행
- [ ] NCR 폐쇄율 ≥ 95% (분기)
- [ ] 반복 부적합 RCA 실행 + 프로세스 개선 회귀
- [ ] 월간 QA 보고서 발행
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **PM (MAN.3)**: 일정·자원·NCR 의사결정
- **Process Owner**: 프로세스 개선 회귀
- **Process Improvement (PIM.3)**: 반복 부적합 → 개선 항목

## 7. 주의사항 / 예외 처리

### 7.1 QA 독립성 위반
- QA Engineer 가 개발 활동에 참여 의심:
  - 즉시 분리 + CTO 통보.
  - 해당 기간 QA 결과 외부 감사로 재검증.

### 7.2 NCR 폐쇄 지연
- NCR 폐쇄 기한 초과:
  - 1차 알림 → 2차 PM 에스컬레이션 → 3차 CTO 보고.
  - 반복 시 책임자 인사 평가 반영.

### 7.3 반복 부적합 (Systemic Issue)
- 동일 유형 NCR 3건 이상 반복:
  - RCA 강제 + 프로세스 개선 PIM.3 회귀.
  - 개선 효과는 3개월 추적 후 종결.

### 7.4 외부 감사 (OEM/인증) 부적합
- 외부 심사에서 발견된 부적합:
  - 즉시 NCR 등록 + Critical 분류.
  - 외부 감사 종료일 기준 시정조치 일정 협의.

## 8. 연계 템플릿 / 기록
- 기록 폴더: `vault/08_REC_기록/SUP.1/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-SUP.1-PURPOSE-001 / VWAY-SUP.1-BP1~BP6"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — SUP.1 QA 계획·감사·NCR 추적 | (대기) |
