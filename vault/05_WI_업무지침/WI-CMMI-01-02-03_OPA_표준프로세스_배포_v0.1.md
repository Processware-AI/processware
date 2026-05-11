---
type: WI
doc_id: WI-CMMI-01-02-03
title: "OPA·표준프로세스 배포 (SG3: SP3.1~3.2)"
version: "0.1"
status: draft
owner: "EPG Lead"
reviewer: "Process Owner"
approver: "CEO/CTO"
scope: "조직 프로세스 자산(OPA) 및 OSSP의 프로젝트·신규 시작 프로젝트 대상 배포·교육"
scope_code: CMMI
parent_pro: "[[PRO-CMMI-01-02_조직_프로세스_개선_배포_절차]]"
parent_pol: "[[POL-CMMI-01_조직_프로세스_거버넌스_정책]]"
related_tmp:
  - "[[TMP-CMMI-01-02-03-01_OPA_배포_계획서]]"
  - "[[TMP-CMMI-01-02-03-02_표준프로세스_배포_가이드]]"
related_rec: []
standards: [CMMI-DEV-ML3-V1.3]
copyright_notice:
  holder: "Carnegie Mellon University / SEI"
  license: "internal_use_derivative_work"
pa_acronym: OPF
sg_sp_refs:
  - "CMMIDEV-OPF-SP3.1-REQ-001"
  - "CMMIDEV-OPF-SP3.2-REQ-001"
entry_gate: "WI-CMMI-01-02-02.status == done"
scope_type: organization
created: 2026-05-11
updated: 2026-05-11
tags: [WI, CMMI, OPF, ML3]
---

# OPA·표준프로세스 배포 (WI-CMMI-01-02-03)

> 상위 절차: [[PRO-CMMI-01-02_조직_프로세스_개선_배포_절차]]

## 1. 업무 목적
승인된 OPA(Organizational Process Assets) 와 OSSP 변경분을 조직 전체 프로젝트에 일관되게 배포하고, 신규 시작 프로젝트는 OSSP 를 의무 적용하도록 지원·교육한다.

## 2. 수행 주체
- **주 수행자**: EPG Lead
- **검토자**: Process Owner, CM, OT(Training Manager)
- **승인자**: CEO/CTO (배포 계획 승인)

## 3. 범위
PRO-CMMI-01-02 §5 의 **SP3.1(OPA 배포) ~ SP3.2(표준프로세스 배포)** 단계. 배포 후 모니터링은 [[WI-CMMI-01-02-04]] 참조.

## 4. 입력 자료 / 산출물
- **Input**
  - 액션 플랜 산출물 + 갱신된 OPA
  - 현 OSSP 베이스라인 ID
  - 활성 프로젝트 목록·신규 시작 예정 프로젝트
- **Output**
  - [[TMP-CMMI-01-02-03-01_OPA_배포_계획서]] 작성본 (승인)
  - [[TMP-CMMI-01-02-03-02_표준프로세스_배포_가이드]] 작성본
  - 교육자료·공지문·테일러링 기록부

## 5. 수행 절차

### 5.1 사전 준비
1. OPA·OSSP 갱신본 CM 베이스라인 확인.
2. 활성 프로젝트 목록·PM 명단 확보.
3. 변경 영향 분석: 어느 프로젝트가 영향을 받는지 매핑.

### 5.2 수행 단계
1. **배포 계획 수립** (SP3.1)
   - 배포 대상·범위·일정 정의 (전체/단계/그룹별).
   - 교육 필요성 평가 + OT 와 연계 ([[PRO-CMMI-01-03]] SP1.1 입력).
   - 위험·대안 분석.
   - [[TMP-CMMI-01-02-03-01]] 양식 작성.
2. **OPA 변경 문서화** (SP3.1)
   - 변경 항목 목록·이전/이후 비교표.
   - 변경 이유·기대 효과.
   - 적용 기한·전환기 정책.
3. **지원자료 준비** (SP3.1)
   - 교육 슬라이드·FAQ·체크리스트.
   - PAL 자산 갱신·접근 권한 확인.
4. **신규 시작 프로젝트 식별** (SP3.2)
   - 향후 6개월 내 시작 예정 프로젝트 식별.
   - 활성 프로젝트 중 OSSP 갱신본 적용 권장 대상 식별.
5. **신규 프로젝트 OSSP 적용 지원** (SP3.2)
   - PM 에게 [[TMP-CMMI-01-02-03-02]] 가이드 전달.
   - 테일러링 컨설팅 제공 (가이드 [[WI-CMMI-01-01-02]] 참조).
   - 테일러링 기록부 작성 지원.
6. **공지 및 발효** (SP3.1·SP3.2)
   - 사내 공지(이메일·인트라넷·PCB 회의).
   - 발효일 명시 + 미적용 시 PPQA 가 NCR 발행.
7. **컴플라이언스 감사 대상 등재** (SP3.2)
   - 테일러링 적용 프로젝트는 PPQA 컴플라이언스 감사 일정에 등재.

### 5.3 완료 조건
- [ ] 배포 계획서 작성·CEO/CTO 승인 완료
- [ ] OPA 변경 문서·이전·이후 비교표 작성
- [ ] 지원자료(교육·FAQ·체크리스트) 배포 완료
- [ ] 신규·활성 프로젝트 식별 + 적용 대상 명단 확정
- [ ] 표준프로세스 배포 가이드 전달 + 테일러링 컨설팅 제공
- [ ] 사내 공지 발신 + 발효일 명시
- [ ] PPQA 감사 대상 등재
- [ ] CM 베이스라인 + MAT-001 등록

## 6. 인터페이스 부서
- **선행 WI**: [[WI-CMMI-01-02-02]] 액션 결과 인수
- **후행 WI**: [[WI-CMMI-01-02-04]] 모니터링·환류
- **OT**: 교육 니즈 공급 (BPM-feeds-OT)
- **CM**: 배포 자산 베이스라인 통제
- **PPQA**: 컴플라이언스 감사 실행
- **PM/프로젝트**: 적용 대상

## 7. 주의사항 / 예외 처리

### 7.1 활성 프로젝트의 부분 적용 거부
- 활성 프로젝트가 일정·계약 사유로 OSSP 갱신본 적용 어려우면 waiver 신청.
- waiver 승인 시 다음 마일스톤·차기 프로젝트에서 적용 의무.

### 7.2 긴급 핫픽스 배포
- 보안·법규 사유 핫픽스: 즉시 발효 + 48시간 내 정식 승인 보완.
- 사후 PCB 보고.

### 7.3 배포 후 결함 발견
- 배포 후 OPA·OSSP 결함 발견 시: 즉시 회수 결정 → 임시 복귀 → 수정본 재배포.
- 영향 받은 프로젝트에 별도 공지.

## 8. 연계 템플릿 / 기록
- 템플릿:
  - [[TMP-CMMI-01-02-03-01_OPA_배포_계획서]]
  - [[TMP-CMMI-01-02-03-02_표준프로세스_배포_가이드]]
- 작성예시:
  - [[EX-CMMI-01-02-03-01_OPA_배포_계획서_작성예시]]
  - [[EX-CMMI-01-02-03-02_표준프로세스_배포_가이드_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. source_citation
```yaml
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-OPF-SP3.1-REQ-001 (p.210)"
  retrieved_at: "2026-05-11"
  license: "CMU/SEI internal_use_derivative_work"
  paraphrase_only: true
- type: standard_original
  file: "inputs/01_표준원문/CMMI-DEV/requirements.yaml"
  locator: "CMMIDEV-OPF-SP3.2-REQ-001 (p.211)"
  retrieved_at: "2026-05-11"
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-11 | 최초 초안 (wi-tmp-writer) | - |
