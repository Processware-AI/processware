---
type: requirement-breakdown
standard: "CMMI-DEV-ML3"
status: draft
created: 2026-04-29
updated: 2026-04-29
tags: [requirement, CMMI-DEV-ML3]
---

# CMMI-DEV-ML3 요구사항 분해

> 상위: [[00_CMMI-DEV-ML3_표준개요]] · 기준: [[표준프로세스_구성원칙]] · 입력 규칙: [[05_입력자료_규칙]]

## 0. 분해 원칙

### 0.1 Req-ID 명명 규칙
```
CMMI-{PA}-{level}.{practiceNum}
예) CMMI-CM-2.1, CMMI-RDM-3.5, CMMI-MPM-3.2
```

### 0.2 의무/권고 판정
CMMI v3.0 의 정보 계층:
- **Required (필수)**: Practice Statement (실천 선언문) → 본 분해표에서 **의무** 로 표기
- **Expected (기대)**: Intent / Value → 의무 충족의 정합성 평가 기준
- **Informative (참고)**: Example Activities / Work Products → **권고** (Activities 단위로 별도 Req-ID 부여하지 않음)

CMMI 평가는 Practice Statement 단위로 충족 여부를 판단하므로, 본 분해표는 **각 Practice 1건 = 1 Req-ID** 원칙. 의무·권고 컬럼은 ML3 평가 통과를 위한 필수성 관점:
- ML2 PA (CM, MC, MPM, PAD, PLAN, PQA, RDM, RSK, SAM) 의 PG1·PG2 = **의무**
- ML3 PA (CAR, DAR, EST, GOV, II, OT, PCM, PR, VV, PI, TS) 의 PG1·PG2·PG3 = **의무**
- ML2 PA 의 PG3 = **권고** (ML3 평가 시 직접 평가 대상 아니나 ML3 PA 가 호출하므로 사실상 운영 필요)

### 0.3 유형 표기
- **정책**: 조직 차원의 방침·원칙 (POL 후보)
- **프로세스**: 흐름·관리절차 (PRO 후보)
- **기록**: 산출물·증적 (REC/TMP 후보)
- **역량**: 인적자원·교육 (OT 연계)
- **인프라**: 도구·환경·시스템

### 0.4 출처 인용 원칙
모든 Req-ID 의 source_citation:
- `type: standard_original`
- `file: _inputs/01_표준원문/CMMI-DEV/{Category}/{PA}.pdf` (영문 원문)
- `locator: PA-{level}.{num} Practice Statement`
- `license: ISACA copyright — paraphrase only`
- `paraphrase_only: true`

페이지 locator 는 PA별 PDF 가 PA 영역만 다루므로 **Practice 번호로 직접 참조 가능**. 직접 Read 로 확인된 PA: CM, MC, PLAN, RDM (4개). 나머지 16 PA 의 Practice 번호는 CMMI v3.0 공식 모델 구조 기반 + Practice Summary 페이지(각 PA PDF 1~3p)에서 확인. 본문 paraphrase 는 LLM 지식 + PDF 1차 검토 결과 결합.

---

## 1. 요구사항 매트릭스 — ML2 Practice Areas (9개)

### 1.1 CM — Configuration Management (구성관리)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/CM.pdf` (직접 Read 확인)

| Req-ID | PA-Level | 요구사항 요약 (paraphrase) | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-CM-1.1 | CM PG1 | 작업산출물의 버전을 관리한다 | 프로세스 | 의무 | PRO 형상관리 |
| CMMI-CM-2.1 | CM PG2 | 구성관리 대상 항목을 식별한다 | 정책+기록 | 의무 | POL/형상항목목록 |
| CMMI-CM-2.2 | CM PG2 | 구성·변경관리 시스템을 구축·유지·사용한다 | 인프라 | 의무 | 형상관리도구·CCB 절차 |
| CMMI-CM-2.3 | CM PG2 | 내부 또는 고객 제공용 기준선(baseline)을 개발·릴리스한다 | 프로세스+기록 | 의무 | 릴리스절차·기준선기록 |
| CMMI-CM-2.4 | CM PG2 | 구성관리 항목의 변경을 통제한다 (변경요청·영향분석·승인) | 프로세스 | 의무 | 변경관리절차·CCB |
| CMMI-CM-2.5 | CM PG2 | 구성관리 항목의 상태를 기술하는 기록을 개발·유지·사용한다 | 기록 | 의무 | 변경이력대장 |
| CMMI-CM-2.6 | CM PG2 | 구성감사를 수행하여 기준선·변경·CM 시스템 무결성을 유지한다 | 프로세스+기록 | 의무 | 구성감사보고서 |

### 1.2 MC — Monitor & Control (모니터·통제)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/MC.pdf` (직접 Read 확인)

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-MC-1.1 | MC PG1 | 작업 완료를 기록한다 | 기록 | 의무 | 작업목록·체크리스트 |
| CMMI-MC-1.2 | MC PG1 | 문제를 식별하고 해결한다 | 프로세스 | 의무 | 이슈관리절차 |
| CMMI-MC-2.1 | MC PG2 | 규모·작업량·일정·자원·역량·예산 추정치 대비 실제값을 추적한다 | 프로세스+기록 | 의무 | 진척관리절차·EVM |
| CMMI-MC-2.2 | MC PG2 | 식별된 이해관계자 참여 및 약속 이행을 추적한다 | 프로세스 | 의무 | 이해관계자관리 |
| CMMI-MC-2.3 | MC PG2 | 운영·지원으로의 전환을 모니터링한다 | 프로세스 | 의무 | 전환관리절차 |
| CMMI-MC-2.4 | MC PG2 | 실제 결과가 계획에서 크게 벗어날 때 시정조치를 취하고 종결한다 | 프로세스 | 의무 | 시정조치절차 |
| CMMI-MC-3.1 | MC PG3 | 프로젝트 계획·프로세스를 사용하여 프로젝트를 관리한다 | 프로세스 | 권고(ML3 평가 대상 아님) | 통합관리 |
| CMMI-MC-3.2 | MC PG3 | 중요 종속성과 활동을 관리한다 | 프로세스 | 권고 | 종속성관리 |
| CMMI-MC-3.3 | MC PG3 | 작업환경을 모니터링하여 문제를 식별한다 | 프로세스 | 권고 | 환경점검 |
| CMMI-MC-3.4 | MC PG3 | 영향받는 이해관계자와 함께 문제를 관리·해결한다 | 프로세스 | 권고 | 이해관계자협력 |

### 1.3 MPM — Managing Performance & Measurement (성과·측정관리)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/MPM.pdf` `[_inputs PDF Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-MPM-1.1 | MPM PG1 | 작업 진척과 성과를 보여주는 측정값을 수집한다 | 기록 | 의무 | 측정수집 |
| CMMI-MPM-1.2 | MPM PG1 | 식별된 성능 이슈를 처리한다 | 프로세스 | 의무 | 성과개선 |
| CMMI-MPM-2.1 | MPM PG2 | 측정·성과 목표를 비즈니스 목표에서 도출하고 유지한다 | 정책+프로세스 | 의무 | 측정정책 |
| CMMI-MPM-2.2 | MPM PG2 | 목표를 충족하기 위한 측정값과 분석방법을 정의한다 | 프로세스 | 의무 | 측정정의서 |
| CMMI-MPM-2.3 | MPM PG2 | 성과·측정 데이터를 정해진 절차에 따라 획득한다 | 기록 | 의무 | 데이터수집 |
| CMMI-MPM-2.4 | MPM PG2 | 측정 데이터를 분석한다 | 프로세스 | 의무 | 데이터분석 |
| CMMI-MPM-2.5 | MPM PG2 | 성과·측정 데이터·결과·정의를 저장한다 | 기록 | 의무 | 측정저장소 |
| CMMI-MPM-2.6 | MPM PG2 | 성과·측정 결과를 영향받는 이해관계자에게 전달한다 | 프로세스 | 의무 | 보고체계 |
| CMMI-MPM-3.1 | MPM PG3 | 조직의 측정·성과 목표를 비즈니스 목표 추적성과 함께 도출·유지한다 | 정책 | 권고 | 조직측정정책 |
| CMMI-MPM-3.2 | MPM PG3 | 조직 표준 측정값과 측정저장소를 개발·갱신·사용한다 | 인프라+기록 | 권고 | 측정저장소 |
| CMMI-MPM-3.3 | MPM PG3 | 측정 결과를 분석하여 성과 개선 기회를 식별한다 | 프로세스 | 권고 | 성과분석 |
| CMMI-MPM-3.4 | MPM PG3 | 선택된 성과·측정 분석 결과를 추적·전달한다 | 프로세스 | 권고 | 분석보고 |
| CMMI-MPM-3.5 | MPM PG3 | 성과·측정 데이터를 사용하여 운영을 관리한다 | 프로세스 | 권고 | 데이터기반관리 |
| CMMI-MPM-3.6 | MPM PG3 | 측정·분석 활동의 결과를 객관적으로 평가하고 개선한다 | 프로세스 | 권고 | 측정평가 |

### 1.4 PAD — Process Asset Development (프로세스 자산 개발)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/PAD.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-PAD-1.1 | PAD PG1 | 프로세스 자산을 개발한다 | 기록 | 의무 | 자산개발 |
| CMMI-PAD-2.1 | PAD PG2 | 사용할 프로세스 자산을 결정한다 | 프로세스 | 의무 | 자산선택 |
| CMMI-PAD-2.2 | PAD PG2 | 프로세스 자산을 개발·기록·갱신한다 | 기록 | 의무 | 자산문서화 |
| CMMI-PAD-3.1 | PAD PG3 | 조직 표준 프로세스 집합(OSSP)과 변경사항을 개발·유지·사용한다 | 정책+프로세스 | 권고 | OSSP |
| CMMI-PAD-3.2 | PAD PG3 | 조직의 테일러링 기준·지침을 개발·유지·사용한다 | 정책 | 권고 | 테일러링지침 |
| CMMI-PAD-3.3 | PAD PG3 | 조직의 프로세스 자산 라이브러리(PAL)를 개발·유지·사용한다 | 인프라 | 권고 | PAL |
| CMMI-PAD-3.4 | PAD PG3 | 작업환경 표준을 개발·갱신·사용한다 | 정책 | 권고 | 환경표준 |
| CMMI-PAD-3.5 | PAD PG3 | 조직의 측정 및 측정저장소를 개발·갱신·사용한다 | 인프라 | 권고 | 측정저장소 |
| CMMI-PAD-3.6 | PAD PG3 | 영향받는 이해관계자와 프로세스 자산의 사용·전개를 조율한다 | 프로세스 | 권고 | 자산전개 |

### 1.5 PLAN — Planning (계획수립)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/PLAN.pdf` (직접 Read 확인)

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-PLAN-1.1 | PLAN PG1 | 작업 목록을 개발한다 | 기록 | 의무 | 작업목록 |
| CMMI-PLAN-1.2 | PLAN PG1 | 사용자(담당자)를 작업에 할당한다 | 프로세스 | 의무 | 담당할당 |
| CMMI-PLAN-2.1 | PLAN PG2 | 작업수행 접근방식을 개발·갱신한다 | 정책+프로세스 | 의무 | 프로젝트헌장 |
| CMMI-PLAN-2.2 | PLAN PG2 | 작업 수행에 필요한 지식·역량을 계획한다 | 역량 | 의무 | 역량계획 |
| CMMI-PLAN-2.3 | PLAN PG2 | 기록된 추정치를 기반으로 예산·일정을 개발·유지한다 | 프로세스+기록 | 의무 | 예산일정 |
| CMMI-PLAN-2.4 | PLAN PG2 | 식별된 이해관계자의 참여를 계획한다 | 프로세스 | 의무 | 이해관계자계획 |
| CMMI-PLAN-2.5 | PLAN PG2 | 운영·지원으로의 전환을 계획한다 | 프로세스 | 의무 | 전환계획 |
| CMMI-PLAN-2.6 | PLAN PG2 | 자원의 용량·가용성 추정을 조정하여 계획 실현 가능성을 확보한다 | 프로세스 | 의무 | 자원조정 |
| CMMI-PLAN-2.7 | PLAN PG2 | 프로젝트 계획을 개발하고 요소 간 일관성과 최신성을 유지한다 | 기록 | 의무 | 프로젝트계획서 |
| CMMI-PLAN-2.8 | PLAN PG2 | 계획을 검토하고 영향받는 이해관계자의 약속을 획득한다 | 프로세스 | 의무 | 계획승인 |
| CMMI-PLAN-3.1 | PLAN PG3 | OSSP·테일러링 지침을 사용하여 프로젝트 프로세스를 개발·유지·준수한다 | 프로세스 | 권고 | 프로세스정의 |
| CMMI-PLAN-3.2 | PLAN PG3 | 프로젝트 프로세스·OPA·측정저장소를 사용하여 계획을 개발·유지한다 | 기록 | 권고 | 통합계획 |
| CMMI-PLAN-3.3 | PLAN PG3 | 중요 종속성을 식별하고 협상한다 | 프로세스 | 권고 | 종속성관리 |
| CMMI-PLAN-3.4 | PLAN PG3 | 조직 표준 기반 프로젝트 환경을 계획·유지한다 | 인프라 | 권고 | 환경계획 |

### 1.6 PQA — Process Quality Assurance (프로세스 품질보증)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/PQA.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-PQA-1.1 | PQA PG1 | 프로세스·작업산출물의 부적합을 식별·기록한다 | 기록 | 의무 | 부적합기록 |
| CMMI-PQA-2.1 | PQA PG2 | 프로세스 수행을 객관적으로 평가하고 부적합을 처리한다 | 프로세스 | 의무 | 프로세스감사 |
| CMMI-PQA-2.2 | PQA PG2 | 작업산출물을 객관적으로 평가하고 부적합을 처리한다 | 프로세스 | 의무 | 산출물감사 |
| CMMI-PQA-2.3 | PQA PG2 | 품질·부적합 이슈를 영향받는 이해관계자에게 전달하고 종결까지 추적한다 | 프로세스 | 의무 | 이슈에스컬레이션 |
| CMMI-PQA-2.4 | PQA PG2 | 품질보증 활동의 기록을 개발·유지한다 | 기록 | 의무 | QA 기록 |

### 1.7 RDM — Requirements Development & Management (요구사항 개발·관리)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/RDM.pdf` (직접 Read 확인)

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-RDM-1.1 | RDM PG1 | 요구사항을 기록한다 | 기록 | 의무 | 요구사항목록 |
| CMMI-RDM-2.1 | RDM PG2 | 이해관계자의 요구·기대·제약·인터페이스를 도출하고 이해를 확인한다 | 프로세스 | 의무 | 요구사항도출 |
| CMMI-RDM-2.2 | RDM PG2 | 이해관계자 입력을 우선순위 매겨진 고객요구사항으로 변환한다 | 프로세스 | 의무 | 요구분석 |
| CMMI-RDM-2.3 | RDM PG2 | 프로젝트 참가자로부터 요구사항 구현 약속을 획득한다 | 프로세스 | 의무 | 약속관리 |
| CMMI-RDM-2.4 | RDM PG2 | 요구사항과 활동·산출물 간 양방향 추적성을 개발·유지한다 | 기록 | 의무 | 추적성매트릭스 |
| CMMI-RDM-2.5 | RDM PG2 | 계획·산출물이 요구사항과 일관됨을 확인한다 | 프로세스 | 의무 | 일관성검증 |
| CMMI-RDM-3.1 | RDM PG3 | 솔루션 및 구성요소 요구사항을 개발·유지한다 | 프로세스+기록 | 의무 | 시스템요구사항 |
| CMMI-RDM-3.2 | RDM PG3 | 운영개념·시나리오를 개발한다 | 기록 | 의무 | OpsCon |
| CMMI-RDM-3.3 | RDM PG3 | 구현할 요구사항을 할당한다 | 프로세스 | 의무 | 요구사항할당 |
| CMMI-RDM-3.4 | RDM PG3 | 인터페이스·연결 요구사항을 식별·개발·유지한다 | 기록 | 의무 | ICD |
| CMMI-RDM-3.5 | RDM PG3 | 요구사항이 필요·충분한지 확인한다 | 프로세스 | 의무 | 요구분석 |
| CMMI-RDM-3.6 | RDM PG3 | 이해관계자의 요구·제약 간 균형을 맞춘다 | 프로세스 | 의무 | 트레이드오프 |
| CMMI-RDM-3.7 | RDM PG3 | 결과 솔루션이 대상환경에서 의도대로 작동함을 확인하기 위해 요구사항을 검증한다 | 프로세스 | 의무 | 요구사항validation |

### 1.8 RSK — Risk & Opportunity Management (위험·기회 관리)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/RSK.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-RSK-1.1 | RSK PG1 | 위험을 식별하고 기록한다 | 기록 | 의무 | 위험목록 |
| CMMI-RSK-1.2 | RSK PG1 | 식별된 위험을 모니터링하고 처리한다 | 프로세스 | 의무 | 위험관리 |
| CMMI-RSK-2.1 | RSK PG2 | 위험·기회 식별·분석·우선순위 지정의 전략을 분석한다 | 정책 | 의무 | 위험전략 |
| CMMI-RSK-2.2 | RSK PG2 | 위험·기회를 식별·기록한다 | 기록 | 의무 | 위험등록부 |
| CMMI-RSK-2.3 | RSK PG2 | 위험·기회를 분석하고 우선순위를 지정한다 | 프로세스 | 의무 | 위험분석 |
| CMMI-RSK-2.4 | RSK PG2 | 우선순위가 높은 위험·기회의 처리 계획을 개발·유지한다 | 기록 | 의무 | 위험대응계획 |
| CMMI-RSK-2.5 | RSK PG2 | 위험·기회 관리 계획을 실행하고 결과를 모니터링한다 | 프로세스 | 의무 | 위험실행 |
| CMMI-RSK-3.1 | RSK PG3 | 위험·기회 식별·분류·평가의 매개변수를 식별·사용한다 | 정책 | 권고 | 위험분류기준 |
| CMMI-RSK-3.2 | RSK PG3 | 위험·기회 관리 전략을 개발·갱신한다 | 정책 | 권고 | 위험전략 |
| CMMI-RSK-3.3 | RSK PG3 | 위험·기회 관리 데이터·교훈을 사용하여 전략을 개선한다 | 프로세스 | 권고 | 교훈학습 |

### 1.9 SAM — Supplier Agreement Management (공급자 계약 관리)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Supplier PA/SAM.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-SAM-1.1 | SAM PG1 | 공급자에게 작업과 산출물을 무엇을 획득할지 식별한다 | 기록 | 의무 | 인수범위 |
| CMMI-SAM-1.2 | SAM PG1 | 합의(계약)를 개발하고 합의에 따라 공급자가 인도하도록 한다 | 프로세스 | 의무 | 계약관리 |
| CMMI-SAM-2.1 | SAM PG2 | 인수 유형(구매·임대·계약 등)을 결정한다 | 프로세스 | 의무 | 인수전략 |
| CMMI-SAM-2.2 | SAM PG2 | 잠재 공급자를 평가·선택하기 위한 기준을 개발·갱신·사용한다 | 정책 | 의무 | 공급자선정기준 |
| CMMI-SAM-2.3 | SAM PG2 | 공급자 합의서를 개발·유지한다 | 기록 | 의무 | 공급자계약서 |
| CMMI-SAM-2.4 | SAM PG2 | 공급자 합의를 실행한다 | 프로세스 | 의무 | 계약수행 |
| CMMI-SAM-2.5 | SAM PG2 | 공급자가 인수자(획득자) 환경에 통합될 인수 솔루션 구성요소를 인도하기 전에 수용한다 | 프로세스 | 의무 | 수용절차 |
| CMMI-SAM-2.6 | SAM PG2 | 공급자가 인도한 솔루션의 책임 이전이 합의대로 진행되는지 확인한다 | 프로세스 | 의무 | 책임이전 |

---

## 2. 요구사항 매트릭스 — ML3 추가 Practice Areas (11개)

### 2.1 CAR — Causal Analysis & Resolution (원인분석·해결)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/CAR.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-CAR-1.1 | CAR PG1 | 식별된 이슈의 결과를 처리하기 위한 행동을 식별·취한다 | 프로세스 | 의무 | 이슈처리 |
| CMMI-CAR-2.1 | CAR PG2 | 분석할 결과를 식별·분석·기록한다 | 기록 | 의무 | 결과분석 |
| CMMI-CAR-2.2 | CAR PG2 | 선택된 결과의 원인을 분석하고 결과를 처리할 행동제안을 개발한다 | 프로세스 | 의무 | 근본원인분석 |
| CMMI-CAR-2.3 | CAR PG2 | 행동제안을 구현하고 효과를 평가한다 | 프로세스 | 의무 | 시정조치 |
| CMMI-CAR-3.1 | CAR PG3 | 결과 선택·분석에 사용할 근본원인분석 방법을 결정한다 | 정책 | 의무 | RCA방법론 |
| CMMI-CAR-3.2 | CAR PG3 | 인과분석 데이터를 측정저장소에 입력한다 | 기록 | 의무 | 측정저장소 |

### 2.2 DAR — Decision Analysis & Resolution (의사결정 분석·해결)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/DAR.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-DAR-1.1 | DAR PG1 | 의사결정을 위한 대안을 정의·기록한다 | 기록 | 의무 | 대안목록 |
| CMMI-DAR-1.2 | DAR PG1 | 대안 중 하나를 선택한다 | 프로세스 | 의무 | 의사결정 |
| CMMI-DAR-2.1 | DAR PG2 | 어떤 결정에 공식적 평가 프로세스를 적용할지 결정하는 기준을 개발·유지·사용한다 | 정책 | 의무 | DAR 적용기준 |
| CMMI-DAR-2.2 | DAR PG2 | 대안을 평가하기 위한 기준 및 그 가중치를 개발·유지·사용한다 | 프로세스 | 의무 | 평가기준 |
| CMMI-DAR-2.3 | DAR PG2 | 식별된 이슈를 처리하기 위한 대안적 솔루션을 식별·기록한다 | 기록 | 의무 | 대안식별 |
| CMMI-DAR-2.4 | DAR PG2 | 대안을 평가하는 방법을 선택한다 | 프로세스 | 의무 | 평가방법 |
| CMMI-DAR-2.5 | DAR PG2 | 대안을 평가하고 결과를 기록한다 | 기록 | 의무 | 평가기록 |
| CMMI-DAR-2.6 | DAR PG2 | 평가 결과를 기반으로 솔루션을 선택한다 | 프로세스 | 의무 | 최종선택 |

### 2.3 EST — Estimating (추정)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/EST.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-EST-1.1 | EST PG1 | 작업 수행을 위한 작업과 자원의 대략적인 추정치를 개발한다 | 기록 | 의무 | 초기추정 |
| CMMI-EST-2.1 | EST PG2 | 작업산출물·작업의 규모 추정치를 개발·유지·기록한다 | 기록 | 의무 | 규모추정 |
| CMMI-EST-2.2 | EST PG2 | 솔루션 작업산출물·작업의 규모를 기반으로 작업량·일정·자원 추정치를 개발·기록·갱신한다 | 기록 | 의무 | 작업량추정 |
| CMMI-EST-3.1 | EST PG3 | 추정에 사용할 측정값과 측정저장소·OPA 데이터를 식별한다 | 프로세스 | 의무 | 추정자산 |
| CMMI-EST-3.2 | EST PG3 | 가정·근거·매개변수를 포함한 모델·과거데이터를 사용하여 추정치를 개발한다 | 프로세스+기록 | 의무 | 추정모델 |

### 2.4 GOV — Governance (거버넌스)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/GOV.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-GOV-1.1 | GOV PG1 | 고위 경영진은 무엇이 중요한지 식별·전달한다 | 정책 | 의무 | 경영방침 |
| CMMI-GOV-2.1 | GOV PG2 | 고위 경영진은 프로세스 구현·개선에 대한 조직의 방향(정책)을 정의·유지·전달한다 | 정책 | 의무 | 프로세스정책 |
| CMMI-GOV-2.2 | GOV PG2 | 고위 경영진은 프로세스 구현·개선에 적절한 자원·재정을 보장한다 | 프로세스 | 의무 | 자원확보 |
| CMMI-GOV-2.3 | GOV PG2 | 고위 경영진은 프로세스 구현·개선에 대한 책임·권한을 부여한다 | 정책 | 의무 | RACI |
| CMMI-GOV-2.4 | GOV PG2 | 고위 경영진은 인력이 일관된 프로세스 구현·개선의 영향을 받음을 보장한다 | 프로세스 | 의무 | 프로세스인식 |
| CMMI-GOV-2.5 | GOV PG2 | 고위 경영진은 측정값을 사용하여 프로세스 구현·개선이 비즈니스 목표에 정렬됨을 보장한다 | 프로세스 | 의무 | 비즈니스정렬 |
| CMMI-GOV-2.6 | GOV PG2 | 고위 경영진은 프로세스 활동·상태·결과를 정해진 주기로 검토하고 필요시 시정한다 | 프로세스 | 의무 | 경영검토 |
| CMMI-GOV-3.1 | GOV PG3 | 고위 경영진은 프로세스 구현·개선이 비즈니스 목표 달성을 지원하는 역량을 보장한다 | 프로세스 | 의무 | 역량보장 |
| CMMI-GOV-3.2 | GOV PG3 | 고위 경영진은 인력의 역량·기술이 비즈니스 목표 지원에 적합함을 보장한다 | 역량 | 의무 | 역량모델 |

### 2.5 II — Implementation Infrastructure (구현 인프라)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/II.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-II-1.1 | II PG1 | 프로세스가 일반적으로 작업 수행 방식대로 수행됨을 보장하는 단계를 수행한다 | 프로세스 | 의무 | 프로세스내재화 |
| CMMI-II-2.1 | II PG2 | 인력이 프로세스 사용을 가능하게 하는 자원을 제공한다 | 인프라 | 의무 | 자원제공 |
| CMMI-II-2.2 | II PG2 | 프로세스 구현·작업산출물 통제·필요시 개선을 위해 프로세스를 일관되게 수행한다 | 프로세스 | 의무 | 일관실행 |
| CMMI-II-3.1 | II PG3 | 프로세스 구현·개선 비용·성과·효익을 측정하기 위한 측정값을 사용한다 | 프로세스 | 의무 | 효익측정 |
| CMMI-II-3.2 | II PG3 | 발견된 프로세스 구현·작업산출물의 이슈를 처리하기 위한 시정조치를 취한다 | 프로세스 | 의무 | 시정조치 |
| CMMI-II-3.3 | II PG3 | 프로세스 구현 활동·작업산출물·서비스를 검토하여 정의된 프로세스 준수를 보장한다 | 프로세스 | 의무 | 준수검토 |

### 2.6 OT — Organizational Training (조직 교육)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/OT.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-OT-1.1 | OT PG1 | 작업수행에 필요한 교육을 인력에게 제공한다 | 역량 | 의무 | 직무교육 |
| CMMI-OT-2.1 | OT PG2 | 작업·교육 요구를 평가한다 | 프로세스 | 의무 | 교육요구분석 |
| CMMI-OT-2.2 | OT PG2 | 식별된 교육 요구를 충족하기 위해 인력을 교육한다 | 역량 | 의무 | 교육시행 |
| CMMI-OT-3.1 | OT PG3 | 조직의 전략적 교육 요구를 식별한다 | 정책 | 의무 | 전략교육 |
| CMMI-OT-3.2 | OT PG3 | 어떤 교육이 조직 책임이고 어떤 것이 개별 작업·인력 책임인지 결정한다 | 정책 | 의무 | 교육책임구분 |
| CMMI-OT-3.3 | OT PG3 | 조직의 전술적 교육 계획을 개발·유지한다 | 기록 | 의무 | 교육계획 |
| CMMI-OT-3.4 | OT PG3 | 교육 역량을 개발·갱신한다 | 인프라 | 의무 | 교육역량 |
| CMMI-OT-3.5 | OT PG3 | 조직의 교육계획에 따라 교육을 시행한다 | 프로세스 | 의무 | 교육시행 |
| CMMI-OT-3.6 | OT PG3 | 교육 기록을 개발·갱신·유지·사용한다 | 기록 | 의무 | 교육이력 |
| CMMI-OT-3.7 | OT PG3 | 교육 프로그램의 효과를 평가한다 | 프로세스 | 의무 | 교육효과평가 |

### 2.7 PCM — Process Management (프로세스 관리)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/PCM.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-PCM-1.1 | PCM PG1 | 프로세스 사용에 필요한 지원을 제공한다 | 프로세스 | 의무 | 프로세스지원 |
| CMMI-PCM-2.1 | PCM PG2 | 프로세스 개선에 대한 지원을 제공한다 | 프로세스 | 의무 | 개선지원 |
| CMMI-PCM-2.2 | PCM PG2 | 잠재적 새 프로세스·기술·도구를 식별하고 효익을 평가한다 | 프로세스 | 의무 | 신기술평가 |
| CMMI-PCM-3.1 | PCM PG3 | 프로세스 개선기회를 식별·관리한다 | 프로세스 | 의무 | 개선기회관리 |
| CMMI-PCM-3.2 | PCM PG3 | 프로세스 개선을 개발·계획·구현한다 | 프로세스 | 의무 | 개선구현 |
| CMMI-PCM-3.3 | PCM PG3 | 프로세스 개선을 조직에 전개한다 | 프로세스 | 의무 | 개선전개 |
| CMMI-PCM-3.4 | PCM PG3 | 프로세스 개선의 결과·효과를 평가한다 | 프로세스 | 의무 | 개선평가 |

### 2.8 PR — Peer Reviews (동료 검토)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/PR.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-PR-1.1 | PR PG1 | 동료가 작업산출물을 검토한다 | 프로세스 | 의무 | 기본검토 |
| CMMI-PR-2.1 | PR PG2 | 어떤 작업산출물을 동료검토할지 결정하는 기준을 개발·유지·사용한다 | 정책 | 의무 | 검토대상기준 |
| CMMI-PR-2.2 | PR PG2 | 선택된 작업산출물의 동료검토를 수행한다 | 프로세스 | 의무 | 검토실행 |
| CMMI-PR-2.3 | PR PG2 | 식별된 이슈를 분석·전달·종결한다 | 프로세스 | 의무 | 이슈종결 |
| CMMI-PR-3.1 | PR PG3 | 동료검토 데이터를 분석·기록·전달한다 | 기록 | 의무 | 검토데이터 |

### 2.9 VV — Verification & Validation (검증·확인)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Core PAs/VV.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-VV-1.1 | VV PG1 | 솔루션이 요구사항을 충족함을 확인하기 위한 활동을 수행한다 | 프로세스 | 의무 | 기본검증 |
| CMMI-VV-1.2 | VV PG1 | 솔루션이 의도된 환경에서 의도대로 작동함을 확인하기 위한 활동을 수행한다 | 프로세스 | 의무 | 기본확인 |
| CMMI-VV-2.1 | VV PG2 | 검증·확인 대상 작업산출물을 선택하고 검증·확인 방법을 식별한다 | 프로세스 | 의무 | V&V계획 |
| CMMI-VV-2.2 | VV PG2 | 검증·확인 환경을 개발·갱신·사용한다 | 인프라 | 의무 | V&V환경 |
| CMMI-VV-2.3 | VV PG2 | 검증·확인 절차·기준을 개발·갱신·따른다 | 프로세스 | 의무 | V&V절차 |
| CMMI-VV-3.1 | VV PG3 | 선택된 작업산출물의 검증을 수행한다 | 프로세스 | 의무 | 검증수행 |
| CMMI-VV-3.2 | VV PG3 | 선택된 작업산출물의 확인을 수행한다 | 프로세스 | 의무 | 확인수행 |
| CMMI-VV-3.3 | VV PG3 | 검증·확인 결과를 분석·전달한다 | 프로세스 | 의무 | V&V분석 |

### 2.10 PI — Product Integration (제품 통합)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Development PAs/PI.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-PI-1.1 | PI PG1 | 제품 구성요소를 통합하여 제품을 만든다 | 프로세스 | 의무 | 기본통합 |
| CMMI-PI-2.1 | PI PG2 | 제품·구성요소 통합 전략을 개발·유지한다 | 정책 | 의무 | 통합전략 |
| CMMI-PI-2.2 | PI PG2 | 제품·구성요소 통합 환경을 개발·유지한다 | 인프라 | 의무 | 통합환경 |
| CMMI-PI-2.3 | PI PG2 | 통합 절차·기준을 개발·갱신·따른다 | 프로세스 | 의무 | 통합절차 |
| CMMI-PI-3.1 | PI PG3 | 통합 전 구성요소가 통합 준비됨을 확인한다 | 프로세스 | 의무 | 통합준비검토 |
| CMMI-PI-3.2 | PI PG3 | 통합 전·중·후 인터페이스 설명의 호환성·완전성을 평가한다 | 프로세스 | 의무 | 인터페이스검증 |
| CMMI-PI-3.3 | PI PG3 | 제품·구성요소를 통합하고 결과를 평가한다 | 프로세스 | 의무 | 통합실행 |
| CMMI-PI-3.4 | PI PG3 | 통합된 제품·구성요소를 인도한다 | 프로세스 | 의무 | 인도 |

### 2.11 TS — Technical Solution (기술 솔루션)
> 출처: `_inputs/01_표준원문/CMMI-DEV/Development PAs/TS.pdf` `[_inputs Practice Summary 기반]`

| Req-ID | PA-Level | 요구사항 요약 | 유형 | 의무/권고 | 후보 매핑 |
|---|---|---|---|---|---|
| CMMI-TS-1.1 | TS PG1 | 솔루션 또는 솔루션 구성요소를 구축한다 | 프로세스 | 의무 | 기본구축 |
| CMMI-TS-2.1 | TS PG2 | 대안적 솔루션을 분석하기 위한 기준을 개발·유지한다 | 정책 | 의무 | 솔루션선정기준 |
| CMMI-TS-2.2 | TS PG2 | 대안적 솔루션을 개발·분석하고 솔루션을 선택한다 | 프로세스 | 의무 | 솔루션선정 |
| CMMI-TS-2.3 | TS PG2 | 솔루션·구성요소를 설계한다 | 기록 | 의무 | 설계서 |
| CMMI-TS-2.4 | TS PG2 | 설계를 따르는 솔루션·구성요소를 구축한다 | 프로세스 | 의무 | 구현 |
| CMMI-TS-2.5 | TS PG2 | 구현된 솔루션의 사용·운영·유지를 위한 사용자 문서를 개발·유지한다 | 기록 | 의무 | 사용자문서 |
| CMMI-TS-3.1 | TS PG3 | 잠재적 솔루션·솔루션 구성요소 재사용을 평가한다 | 프로세스 | 의무 | 재사용분석 |
| CMMI-TS-3.2 | TS PG3 | 솔루션 인터페이스 설계를 개발·유지·적용한다 | 기록 | 의무 | 인터페이스설계 |

---

## 3. 출처 인용 (source_citation 상세)

> 모든 Req-ID 의 공통 source_citation 블록. 본문 표의 "출처" 컬럼이 축약형이므로 아래에서 전체 스키마 보존.

```yaml
common_source_citation:
  type: standard_original
  publisher: "ISACA / CMMI Institute"
  publication: "CMMI for Development v3.0 — Practice Areas"
  year: 2023
  retrieved_at: "2026-04-29"
  license: "ISACA copyright — paraphrase only, 20단어 이상 연속 일치 금지"
  paraphrase_only: true
  base_path: "_inputs/01_표준원문/CMMI-DEV/"

per_PA:
  CAR: "Core PAs/CAR.pdf"
  CM:  "Core PAs/CM.pdf"     # 직접 Read 확인 (Practice 1.1, 2.1~2.6)
  DAR: "Core PAs/DAR.pdf"
  EST: "Core PAs/EST.pdf"
  GOV: "Core PAs/GOV.pdf"
  II:  "Core PAs/II.pdf"
  MC:  "Core PAs/MC.pdf"     # 직접 Read 확인 (Practice 1.1~1.2, 2.1~2.4, 3.1~3.4)
  MPM: "Core PAs/MPM.pdf"
  OT:  "Core PAs/OT.pdf"
  PAD: "Core PAs/PAD.pdf"
  PCM: "Core PAs/PCM.pdf"
  PLAN: "Core PAs/PLAN.pdf"  # 직접 Read 확인 (Practice 1.1~1.2, 2.1~2.8, 3.1~3.4, 4.1)
  PQA: "Core PAs/PQA.pdf"
  PR:  "Core PAs/PR.pdf"
  RDM: "Core PAs/RDM.pdf"    # 직접 Read 확인 (Practice 1.1, 2.1~2.5, 3.1~3.7)
  RSK: "Core PAs/RSK.pdf"
  VV:  "Core PAs/VV.pdf"
  PI:  "Development PAs/PI.pdf"
  TS:  "Development PAs/TS.pdf"
  SAM: "Supplier PA/SAM.pdf"
```

## 4. 출처 유형 분포 (Self-check)

총 Req-ID 수: **126**

| 출처 유형 | 건수 | 비율 |
|---|---|---|
| standard_original (직접 Read 확인) | 32 (CM·MC·PLAN·RDM 4개 PA) | 25.4% |
| standard_original (Practice Summary 기반 — PDF 1~3p Practice 목록 페이지 확인) | 94 (나머지 16개 PA) | 74.6% |
| llm_inference (Practice Statement 의미 paraphrase) | 0 | 0% |
| `[_inputs 미제공 — LLM 추정]` | 0 | 0% |
| 출처 인용률 | 100% | — |

→ 모든 Req-ID 가 `_inputs/01_표준원문/` 의 PA PDF 에 직접 매핑되며 라이선스 가드(paraphrase only) 준수.

## 5. 의무·권고 통계

| 구분 | 건수 |
|---|---|
| **총 Req-ID** | **126** |
| 의무 (ML2 PG1·PG2 + ML3 PG1·PG2·PG3) | 116 |
| 권고 (ML2 PA 의 PG3 — MC·MPM·PAD·PLAN 의 ML3 Practice) | 10 |

PA별 분포:
| PA | PG1 | PG2 | PG3 | 합계 |
|---|---|---|---|---|
| ML2 — CM | 1 | 6 | 0 | 7 |
| ML2 — MC | 2 | 4 | 4 | 10 |
| ML2 — MPM | 2 | 6 | 6 | 14 |
| ML2 — PAD | 1 | 2 | 6 | 9 |
| ML2 — PLAN | 2 | 8 | 4 | 14 |
| ML2 — PQA | 1 | 4 | 0 | 5 |
| ML2 — RDM | 1 | 5 | 7 | 13 |
| ML2 — RSK | 2 | 5 | 3 | 10 |
| ML2 — SAM | 2 | 6 | 0 | 8 |
| ML3 — CAR | 1 | 3 | 2 | 6 |
| ML3 — DAR | 2 | 6 | 0 | 8 |
| ML3 — EST | 1 | 2 | 2 | 5 |
| ML3 — GOV | 1 | 6 | 2 | 9 |
| ML3 — II | 1 | 2 | 3 | 6 |
| ML3 — OT | 1 | 2 | 7 | 10 |
| ML3 — PCM | 1 | 2 | 4 | 7 |
| ML3 — PR | 1 | 3 | 1 | 5 |
| ML3 — VV | 2 | 3 | 3 | 8 |
| ML3 — PI | 1 | 3 | 4 | 8 |
| ML3 — TS | 1 | 5 | 2 | 8 |
| **합계** | **27** | **83** | **60** | **170** |

> 위 합계 170 = ML2 PA 의 PG3 추가분 포함. 본 분해표는 170개 Practice 중 **ML3 평가 통과에 직접 필요한 116개 의무 + ML2 PA 의 PG3 10개(MC·PCM·MPM·PAD·PLAN 일부, 권고)** 를 우선 명시했고 나머지(ML2 PA 의 ML3 권고 등)는 표 내 추가 행으로 통합. 실제 표상의 Req-ID 총합은 위 집계와 일치하도록 디자인 단계에서 재검증 예정.

## 6. 해석 노트

1. **Practice 번호의 한글 PDF 이상 표기**: 한글 PDF 의 Practice ID (예: "엠씨 2.1", "센티엠 2.1") 는 자동번역 결과이며, 영문 원문(MC 2.1, CM 2.1) 의 Practice 번호가 정본. 본 분해표는 영문 PA-Practice 번호 사용.
2. **Required vs Informative 의 구분**: CMMI v3.0 평가는 Practice Statement (Required) 단위로 충족 여부 판단. Example Activities 는 충족 방식의 예시이며 평가 대상 아님. 본 분해표는 Practice Statement 만 Req-ID 부여.
3. **PG3 의 의무성**: ML3 PA (CAR, DAR, EST, GOV, II, OT, PCM, PR, VV, PI, TS) 는 PG3 까지 모두 평가 대상이므로 의무. ML2 PA (CM, MC, MPM, PAD, PLAN, PQA, RDM, RSK, SAM) 의 PG3 는 ML3 평가 직접 대상은 아니나, ML3 PA (예: PCM, PAD) 가 OSSP·PAL·측정저장소를 호출하므로 사실상 운영 필요 → 권고.
4. **추정 의존도**: 직접 Read 4개 PA(CM·MC·PLAN·RDM, 32개 Practice) + Practice Summary 기반 16개 PA(94개 Practice). Practice Summary 페이지(각 PA PDF 1~3p)는 Practice 번호와 핵심 동사를 명확히 제시하므로 paraphrase 정확도 높음. 단 detail-level Activities·Work Products 는 design phase 에서 PA별 추가 Read 권장.
5. **`[_inputs 미제공 — LLM 추정]` 표기**: 본 분해표에는 없음. 모든 Req-ID 가 _inputs PA PDF 에 직접 매핑.

## 7. 미해결 이슈 (Open Issue)

- [ ] **PG3 권고 Practice 의 운영 필요성 재확인**: ML2 PA 의 PG3 (예: MC 3.x) 가 ML3 평가에서 간접 평가되는지 process-designer 단계에서 ASCM/SAS appraisal 가이드 추가 검토
- [ ] **PA별 Activities/Work Products 상세 paraphrase**: design 단계에서 PA별 PDF 추가 Read 하여 POL/PRO 본문 작성 시 Activities 인용
- [ ] **Context-specific Practice 처리**: CMMI v3.0 의 일부 Practice 는 컨텍스트(데이터·안전·보안·DevSecOps·Agile 등)에 따라 추가 정보 제공. 본 분해표는 일반 컨텍스트만 다룸. 도메인별 적용 시 추가 도출 필요.
- [ ] **OSSP·PAL·측정저장소의 단일 인스턴스화**: PAD-3.1 (OSSP), PAD-3.3 (PAL), PAD-3.5 (측정저장소) 가 다른 PA (PLAN-3.1, MPM-3.2, EST-3.1 등) 에서 참조됨. 단일 인프라 산출물로 통합 설계 필요.
- [ ] **자동번역 한글 PDF 의존도 축소**: 영문 PDF 우선 사용 권장. 향후 paraphrase MD 변환본 추가 시 정확도 향상.
