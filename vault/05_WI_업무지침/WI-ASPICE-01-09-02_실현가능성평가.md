---
type: WI
doc_id: "WI-ASPICE-01-09-02"
title: "실현 가능성 평가 (MAN.3)"
version: "0.1"
owner: "Project Manager"
reviewer: "Tech Lead / QA / PMO"
approver: "Program Director"
scope: "프로젝트 초기 → 기술·일정·자원 실현 가능성 분석 → 착수 승인 기준 충족 확인"
parent_pro: "[[PRO-ASPICE-01-09_프로젝트관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-09-02-01_실현가능성평가보고서]]"]
related_rec: []
aspice_processes: ["MAN.3"]
entry_gate: "WI-ASPICE-01-09-01.status == done"
standards: ["Automotive SPICE 4.0"]
status: draft
created: "2026-05-06"
updated: "2026-05-06"
tags: [WI, ASPICE, MAN.3, FeasibilityStudy, ProjectManagement]
---

# 실현 가능성 평가 (WI-ASPICE-01-09-02)

> 상위 절차: [[PRO-ASPICE-01-09_프로젝트관리프로세스]]

## 1. 업무 목적
RFQ/SOW 기반 프로젝트 착수 전, 기술·일정·자원·비용 측면의 실현 가능성을 정량 평가하여 착수 승인(Go/No-Go) 의사결정의 근거를 제공한다. ASPICE 4.0 MAN.3 BP1(프로젝트 범위 정의) 및 BP2(프로젝트 수명주기 정의)에 부합한다.

## 2. 수행 주체
- **주수행자**: Project Manager
- **검토자**: Tech Lead, QA Manager, PMO
- **승인자**: Program Director

## 3. 범위
신규 프로젝트 착수 전 단계 전반에 적용한다. 기존 양산 프로그램의 변경 요청(ECR) 중 기술 신규성·일정 영향이 큰 변경에도 본 지침을 준용한다.

## 4. 입력 자료 / 산출물
- **Input**: RFQ/SOW, 고객 기술 요구사항(고객 SRS 초안), 사내 표준 기술 카탈로그, 인력풀 현황, 과거 유사 프로젝트 실적
- **Output**: 실현 가능성 평가 보고서(TMP-ASPICE-01-09-02-01), Go/No-Go 의사결정 회의록

## 5. 수행 절차 (단계별)

### 5.1 사전 준비
1. RFQ/SOW 및 고객 기술 요구사항 사본 확보, 비밀유지(NDA) 범위 확인.
2. 사내 표준 기술 카탈로그(SoC·MCU·툴체인) 최신본 확인.
3. 평가에 참여할 도메인 전문가(SW/HW/ML/Safety) 일정 조율.

### 5.2 수행 단계 (ASPICE BP 참조)
1. **BP1 범위 정의** — RFQ/SOW로부터 기능 범위, 변종(variant), 하드웨어/소프트웨어 경계를 정의.
2. **기술 실현 가능성 분석** — 신규 SoC/MCU 도입 여부, ML 모델 탑재 여부, SW 복잡도(KLoC 추정), 표준 준수(ISO 26262 ASIL 등급) 가능성을 항목별 평가(High/Med/Low).
3. **일정 실현 가능성 분석** — 고객 요구 SOP(Start of Production) 대비 V-model 단계별 소요 추정, ASPICE 인증 일정(외부 심사 리드타임) 포함, 마일스톤 여유(buffer) 산출.
4. **자원 가용성 분석** — 역할별 필요 인원(SW/HW/ML/QA/Safety) 대비 투입 가능 인원, 핵심 장비(HIL/SIL/MIL bench) 가용성, 외주(supplier) 의존도.
5. **비용 추정** — 인건비·라이선스·툴·시제품·외주 비용 보수적/낙관적 시나리오로 산출.
6. **종합 판정** — 항목별 결과를 가중 합산하여 Go / No-Go / 조건부 Go 권고안 작성.
7. **Program Director 보고 및 승인** — 권고안과 핵심 리스크를 보고하고 착수 승인 또는 보류를 결재.

### 5.3 완료 조건 체크리스트
- [ ] 기술/일정/자원/비용 4개 영역 모두 평가 완료되었는가
- [ ] 핵심 리스크(High) 항목별 완화 전략 또는 조건이 명시되었는가
- [ ] Go/No-Go/조건부 Go 권고가 명확히 도출되었는가
- [ ] Program Director 결재가 기록되었는가
- [ ] 평가 보고서가 PLM/문서관리시스템에 등록되었는가
- [ ] [[MAT-001_문서관리대장]] 갱신이 완료되었는가

## 6. 인터페이스 부서
- 영업/사업개발팀(고객 요구 정합성 확인)
- HR(역량 매트릭스 데이터 제공)
- 구매팀(외주 단가 견적)
- Safety팀(ASIL 평가 협조)

## 7. 주의사항 / 예외 처리
1. **데이터 부재 시**: 과거 유사 프로젝트 실적이 없으면 보수적 추정값(+30% 버퍼)을 적용하고 그 사유를 명시한다.
2. **고객 일정 압박 시**: 일정 실현 가능성 Low인데 고객이 강행을 요구하면 "조건부 Go(외주 1팀 추가)"로 권고하고 추가 비용을 사전 합의한다.
3. **신규 SoC 채택 시**: 양산 검증 이력이 없는 SoC는 별도 PoC 단계를 평가 단계 전에 수행할 것을 권고한다.
4. **No-Go 판정 시**: 영업과 협의해 고객에게 대안 제시 또는 정중한 사양 협상 절차를 진행한다.

## 8. 연계 템플릿 / 기록
- 템플릿: [[TMP-ASPICE-01-09-02-01_실현가능성평가보고서]]
- 작성예시: [[EX-ASPICE-01-09-02-01_실현가능성평가보고서_작성예시]]
- 기록 폴더: `08_REC_기록/`

## 9. 출처 (source_citation)
- `inputs/01_표준원문/VWAY_Motors/requirements.yaml`
- Automotive SPICE 4.0 PAM, MAN.3 Project Management

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 작성 | Program Director |
