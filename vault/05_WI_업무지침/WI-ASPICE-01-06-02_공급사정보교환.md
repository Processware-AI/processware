---
doc_id: "WI-ASPICE-01-06-02"
title: "공급사 정보 교환 (ACQ.4)"
type: WI
version: "0.1"
status: draft
owner: "Supply Chain Engineer"
reviewer: "Project Manager / QA"
approver: "Procurement Manager"
scope: "계약 체결 후 → 정기 기술 회의 운영 → 산출물 교환 → 인터페이스 이슈 관리"
scope_type: project
scope_code: ASPICE
domain: ASPICE
parent_pro: "[[PRO-ASPICE-01-06_구매및공급망프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-06-02-01_공급사기술회의록]]"]
aspice_processes: ["ACQ.4"]
entry_gate: "WI-ASPICE-01-06-01.status == done"
standards: ["Automotive SPICE 4.0"]
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, ACQ.4, Supplier, Communication]
---

# WI-ASPICE-01-06-02 — 공급사 정보 교환 (ACQ.4)

## 1. 업무 목적
계약 체결된 공급사와의 기술적 정보 교환을 정기적·체계적으로 운영하여 인터페이스 이슈·산출물 교환·이슈 추적을 표준화한다. ASPICE 4.0 ACQ.4 활동 중 공급사 협업·산출물 교환·이슈 관리 부분을 충족한다.

## 2. 수행 주체
- **주 수행자**: Supply Chain Engineer
- **검토자**: Project Manager / QA
- **승인자**: Procurement Manager

## 3. 범위
- 대상: 계약 체결된 모든 1차 공급사(Tier-1) 와 핵심 2차 공급사
- 활동: 정기 기술 회의, 산출물 교환, ICD(Interface Control Document) 관리, 이슈 트래커 운영
- 제외: 계약 협상·체결(WI-ASPICE-01-06-01), 성과 모니터링(WI-ASPICE-01-06-03)

## 4. 입력 자료 / 산출물
**입력 자료**
- 공급사 계약서 / SOW
- 의사소통 계획(Communication Plan)
- ICD 베이스라인 (현행)
- 이전 회의록 / Action Item 목록

**산출물**
- 공급사 기술 회의록(TMP-ASPICE-01-06-02-01)
- 교환 산출물 목록 (방향·버전·승인 상태)
- ICD 변경 요청서
- Action Item 트래커 갱신

## 5. 수행 절차

### 5.1 사전 준비
1. 회의 의제 사전 합의 (양사 사전 회람 48h 전).
2. 교환 예정 산출물 사전 등록 및 사내 검토 완료.
3. 이전 회의 Action Item 진행률 확인.
4. 회의 기록 시스템(공유 폴더·트래커) 가용성 점검.

### 5.2 수행 단계
1. **회의 개최** (ACQ.4 BP1) — 정기 회의(주간/격주/월간) 를 의제 순서대로 진행한다.
2. **산출물 교환** (ACQ.4 BP2) — 의제별 산출물(ICD·시험 보고서·결함 데이터)을 양방향 전달하고 버전·체크섬을 기록한다.
3. **인터페이스 이슈 등록** (ACQ.4 BP3) — 발견된 ICD 충돌·기술적 차이를 이슈 트래커에 즉시 등록한다.
4. **Action Item 합의** — 담당자·마감일·완료 기준을 명확히 합의한다.
5. **회의록 발행** — 24h 이내 회의록 초안 회람 후 양사 서명/회신 확인.
6. **산출물 CM 등록** — 수신 산출물을 사내 CM 에 등록한다.
7. **이슈 후속 관리** — 마감일 도래 전 1주일 알림 발송.

### 5.3 완료 조건 체크리스트
- [ ] 회의 의제·참석자가 사전 합의되었다.
- [ ] 교환 산출물의 버전·방향·체크섬이 기록되었다.
- [ ] 인터페이스 이슈가 트래커에 등록되었다.
- [ ] Action Item 의 담당자·마감일이 합의되었다.
- [ ] 회의록이 24h 이내 회람되고 양사 확인을 받았다.
- [ ] 수신 산출물이 CM 에 등록되었다.
- [ ] [[MAT-001_문서관리대장]] 갱신 완료.

## 6. 인터페이스 부서
- 시스템 엔지니어링: ICD 검토 및 인터페이스 정합성
- HW/SW 팀: 기술 이슈 분석·대응
- QA: 회의 운영·산출물 품질 감사
- CM: 수신 산출물 베이스라인 관리
- 법무: 산출물 IP/라이선스 검토

## 7. 주의사항 / 예외 처리

### 7.1 공급사 산출물 지연
약속된 산출물이 마감일 초과 시 공식 알림 발송 후 7일 이내 시정조치(WI-ASPICE-01-06-04) 절차로 에스컬레이션한다.

### 7.2 ICD 충돌 발생
양사 ICD 해석 차이로 충돌이 발생하면 즉시 양측 시스템 엔지니어 합동 검토 회의를 소집하고 결정 사항을 ICD 변경 요청서로 발행한다.

### 7.3 보안 사고 의심
교환 채널·산출물에서 보안 사고(누설·악성코드 등)가 의심되면 즉시 채널을 차단하고 보안팀에 통보한다.

### 7.4 비공식 채널 사용
공식 채널 외 메신저·개인 이메일로 산출물 교환이 발견되면 해당 산출물을 비공식으로 분류하고 공식 채널 재전달 후 폐기한다.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-06-02-01_공급사기술회의록]]
- 작성예시: [[EX-ASPICE-01-06-02-01_공급사기술회의록_작성예시]]
- 상위 절차: [[PRO-ASPICE-01-06_구매및공급망프로세스]]
- 후속 단계: [[WI-ASPICE-01-06-03_공급사성과모니터링]]
- 추적성: [[MAT-007_요구사항추적매트릭스]]

## 9. 출처
```yaml
source_citation:
  - file: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    section: "ACQ.4 / ASPICE 4.0"
    accessed: "2026-05-06"
standards:
  - "Automotive SPICE 4.0 — ACQ.4 Supplier Monitoring"
```

## 10. 개정 이력
| 버전 | 일자 | 변경 내용 | 승인자 |
|------|------|-----------|--------|
| 0.1 | 2026-05-06 | 최초 작성 (Draft) | Procurement Manager |
