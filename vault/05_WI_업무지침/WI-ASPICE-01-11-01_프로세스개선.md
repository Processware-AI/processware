---
type: WI
doc_id: "WI-ASPICE-01-11-01"
title: "프로세스 개선 (PIM.3)"
version: "0.1"
owner: "SEPG (Software Engineering Process Group)"
reviewer: "Process Owner / QA"
approver: "PCB (Process Control Board)"
scope: "프로세스 평가 → 개선 항목 식별 → 개선 실행 → 효과 측정"
parent_pro: "[[PRO-ASPICE-01-11_프로세스개선프로세스]]"
related_tmp: []
related_rec: []
standards: ["Automotive SPICE 4.0", "ISO/IEC 33000"]
aspice_processes: ["PIM.3"]
entry_gate: null
scope_type: "common"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, PIM.3, SEPG, CMMI, Improvement]
---

# 프로세스 개선 업무지침 (WI-ASPICE-01-11-01)

> 상위 절차: [[PRO-ASPICE-01-11_프로세스개선프로세스]]
> ASPICE 매핑: PIM.3 (Process Improvement) — BP1~BP7

## 1. 업무 목적

조직 표준 프로세스의 성숙도와 효과성을 정기 평가하고, 개선 항목을 우선순위화하여 실행·검증함으로써 지속적인 품질·생산성 향상을 달성한다.

## 2. 수행 주체
- **주 수행자**: SEPG
- **검토자**: Process Owner, QA, 도메인 Lead
- **승인자**: PCB

## 3. 범위
조직 전체 표준 프로세스(POL/PRO/WI/TMP/EX) 에 적용한다.

## 4. 입력 자료 / 산출물
- **Input**: SUP.1 QA 보고서, KPI 데이터, 외부 심사 결과, Lessons Learned, 조직 전략
- **Output**: Process Assessment Report, 개선 계획, 개선 결과 보고서

## 5. 수행 절차

### 5.1 사전 준비
1. 평가 모델(ASPICE PAM, CMMI) + 평가팀 구성.
2. KPI 데이터 수집 채널 (MAN.6) 확인.

### 5.2 수행 단계

1. **현황 평가** (PIM.3.BP1)
   - 프로세스 영역별 성숙도 평가 (Capability Level).
   - GAP 분석.

2. **개선 항목 식별** (PIM.3.BP2)
   - QA NCR + KPI 미달 + Lessons Learned 통합.
   - Pareto 분석으로 우선순위.

3. **개선 계획 수립** (PIM.3.BP3)
   - 항목별 책임자·일정·자원·기대 효과 명시.
   - PCB 승인.

4. **개선 실행** (PIM.3.BP4)
   - 프로세스 산출물 (POL/PRO/WI) 개정.
   - 파일럿 적용 → 효과 측정 → 전사 확산.

5. **효과 측정·검증** (PIM.3.BP5)
   - 사전·사후 KPI 비교.
   - 개선 효과 정량화.

6. **표준화·전파** (PIM.3.BP6)
   - 결과를 조직 표준에 반영.
   - 교육·내재화.

7. **사후 모니터링** (PIM.3.BP7)
   - 개선 효과 6개월 추적.
   - 지속 효과 미달 시 재개선.

### 5.3 완료 조건 체크리스트
- [ ] 프로세스 평가 보고서 발행 (반기)
- [ ] 개선 항목 우선순위 + PCB 승인
- [ ] 개선 실행 + 파일럿 결과 문서화
- [ ] 사전·사후 KPI 비교 분석
- [ ] 조직 표준 반영 + 교육 실행
- [ ] 6개월 사후 효과 추적
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- **PCB**: 개선 계획 승인
- **Process Owner**: 개선 실행 책임
- **QA (SUP.1)**: 효과 검증
- **HR/Training**: 교육 실행
- **MAN.6 (Measurement)**: KPI 데이터

## 7. 주의사항 / 예외 처리

### 7.1 개선 효과 미달
- 사후 KPI 가 기대 미달:
  - RCA → 개선 방향 재조정.
  - 재개선 또는 항목 폐기 결정.

### 7.2 변경 저항 (Change Resistance)
- 현업의 새 프로세스 회피:
  - 교육 강화 + 인센티브 검토.
  - Process Owner + 라인 매니저 합동 코칭.

### 7.3 외부 심사 부적합 누락
- 외부 인증 심사 부적합이 개선 항목에 미포함:
  - 즉시 항목 추가 + Critical 분류.
  - 시정조치 일정 별도 추적.

### 7.4 다중 개선 항목 자원 충돌
- 동시 다수 개선으로 자원 부담:
  - PCB 가 우선순위 재조정 + 단계적 실행.
  - 조직 변화 수용 한계 고려.

## 8. 연계 템플릿 / 기록
- 기록 폴더: `vault/08_REC_기록/PIM.3/`

## 9. 출처
```yaml
- type: standard_original
  file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
  locator: "VWAY-PIM.3-PURPOSE-001 / VWAY-PIM.3-BP1~BP7"
  retrieved_at: "2026-05-06"
  license: "ASPICE 4.0 © VDA QMC — paraphrase only"
  paraphrase_only: true
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 초안 — PIM.3 BP1~BP7 + 사후 효과 추적 | (대기) |
