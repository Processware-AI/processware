---
doc_id: "WI-ASPICE-01-07-04"
title: "형상 항목 식별 (SUP.8)"
type: WI
version: "0.1"
status: draft
created: "2026-05-06"
updated: "2026-05-06"
owner: "CM Engineer"
reviewer: "Project Manager / QA"
approver: "CM Manager"
scope: "프로젝트 초기 → 형상 항목(CI) 식별·분류·명명 규칙 정의 → CM 도구 등록"
scope_code: "ASPICE"
scope_type: "process"
domain: "ASPICE"
parent_pol: "[[POL-ASPICE-01_ASPICE품질정책]]"
parent_pro: "[[PRO-ASPICE-01-07_품질보증및형상관리프로세스]]"
related_tmp: ["[[TMP-ASPICE-01-07-04-01_형상항목목록]]"]
aspice_processes: ["SUP.8"]
entry_gate: null
standards: ["Automotive SPICE 4.0"]
tags: [WI, ASPICE, SUP.8, CM, ConfigurationItem]
---

# WI-ASPICE-01-07-04 형상 항목 식별 (SUP.8)

## 1. 업무 목적
프로젝트 초기 단계에서 추적·통제 대상이 되는 모든 형상 항목(CI, Configuration Item)을
체계적으로 식별·분류·명명하여 CM 도구에 등록한다. ASPICE SUP.8 BP1(CM 전략 수립) ~ BP3(CI 식별)
및 BP4(CI 베이스라인) 의 식별 부분을 수행한다.

## 2. 수행 주체
- 주 수행자: CM Engineer
- 검토자: Project Manager, QA
- 승인자: CM Manager

## 3. 범위
- 대상: 프로젝트가 산출하거나 의존하는 모든 인공물 (SW 소스, HW 설계, 문서, 테스트, 빌드 도구, 외부 라이브러리)
- 시점: 프로젝트 킥오프 직후 ~ 첫 베이스라인 동결 전
- 제외: 일회성 작업 파일·개인 노트(임시 산출물)

## 4. 입력 자료 / 산출물
| 구분 | 항목 | 출처/위치 |
|---|---|---|
| 입력 | 프로젝트 계획서 | MAN.3 산출물 |
| 입력 | 시스템·SW 산출물 목록 | SYS.1, SWE.1 계획 |
| 입력 | CM 전략 (조직 표준) | POL-ASPICE-01 |
| 출력 | 형상 항목 목록 | TMP-ASPICE-01-07-04-01 |
| 출력 | CM 도구 등록 결과 (Git/Artifactory/Jira 링크) | CM 시스템 |

## 5. 수행 절차

### 5.1 사전 준비
1. 프로젝트 계획서에서 산출물 목록 추출.
2. 조직 CM 전략에서 분류 체계·명명 규칙 표준 확보.
3. CM 도구 접근 권한·리포지토리 생성 권한 확보.

### 5.2 수행 단계
1. **CI 분류 체계 정의** — SW 소스 / HW 설계 / 요구사항·설계 문서 / 테스트 자산 / 빌드·도구 / 릴리즈 패키지 (SUP.8 BP1).
2. **CI 후보 식별** — 각 분류별 인공물 후보 도출, 중복·누락 검토.
3. **CI ID 부여** — 명명 규칙에 따라 유일한 CI-ID 부여 (예: CI-{프로젝트}-{분류}-{시퀀스}).
4. **CI 메타데이터 정의** — 명칭·유형·저장소·버전 형식·담당자·접근 권한 (SUP.8 BP3).
5. **CM 도구 등록** — Git/Artifactory/Confluence/Jira 등 적합한 도구에 등록.
6. **형상 항목 목록 문서화** — TMP-ASPICE-01-07-04-01 작성.
7. **검토 및 승인** — PM·QA 검토 후 CM Manager 승인.
8. **공지** — 프로젝트 전 구성원에게 CI 목록·접근 방법 공지.

### 5.3 완료 조건 체크리스트
- [ ] CI 분류 체계가 정의됨
- [ ] 모든 CI 가 유일한 CI-ID 를 가짐
- [ ] CI 별 담당자가 지정됨
- [ ] CI 별 저장소(URL/경로) 가 지정됨
- [ ] 명명 규칙이 명문화됨
- [ ] CM 도구 등록이 완료됨
- [ ] 형상 항목 목록이 CM Manager 결재됨
- [ ] [[MAT-001_문서관리대장]] 갱신

## 6. 인터페이스 부서
- Project Management Office: 산출물 목록 제공
- SW/HW/Systems Engineering: CI 후보 식별·담당자 지정
- QA: 분류·명명 규칙 준수 검증
- IT Infrastructure: CM 도구·저장소 인프라 지원

## 7. 주의사항 / 예외 처리

### 7.1 외부 의존성(서드파티 라이브러리) 처리
오픈소스·상용 라이브러리도 CI 로 등록하되 라이선스 종류·버전·SBOM 링크를 메타데이터에 포함.
보안 패치 추적성을 위해 별도 분류 코드(CI-{프로젝트}-EXT-NN) 부여.

### 7.2 도구·환경의 형상 관리
빌드 도구·컴파일러·테스트 도구도 CI 로 식별. 버전 변경이 결과에 영향을 주므로 동결된 도구 버전을
CM 도구에 함께 등록하거나 Container Image 로 보존.

### 7.3 CI 추가·폐기 절차
프로젝트 진행 중 CI 추가/폐기는 변경 요청(SUP.10) 으로만 가능. 임의 추가·삭제 금지.

### 7.4 명명 규칙 충돌 시
타 프로젝트 또는 조직 표준과 충돌 시 조직 표준 우선. 프로젝트 고유 접두사로 충돌 회피.

## 8. 연계 템플릿 / 기록
- 양식: [[TMP-ASPICE-01-07-04-01_형상항목목록]]
- 작성예시: [[EX-ASPICE-01-07-04-01_형상항목목록_작성예시]]
- 후속 절차: [[WI-ASPICE-01-07-05_베이스라인및변경통제]]
- 연계 기록: CM 도구 등록 로그, 명명 규칙 표준서

## 9. 출처
```yaml
source_citation:
  - source: "inputs/01_표준원문/VWAY_Motors/requirements.yaml"
    standard: "Automotive SPICE 4.0"
    process: "SUP.8 — Configuration Management"
    base_practices: ["BP1", "BP2", "BP3"]
    work_products: ["08-04 Configuration management plan", "16-03 Configuration management system"]
```

## 10. 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-05-06 | 최초 작성 (draft) | CM Manager |
