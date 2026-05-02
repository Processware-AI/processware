---
description: 프로세스 모듈 1건을 구성원칙과 8종 문서유형(POL/PRO/WI/TMP/EX/REC/MAT/REF)에 맞춰 Obsidian vault에 구축. 입력은 표준 코드·PA 그룹·자연어 요건 기술 모두 수용. 체크포인트/재개·자가수정 루프 지원. 사용: /build-process "프로젝트 계획·추정·리스크 관리"
argument-hint: "<모듈_또는_요건> [--restart] [--resume] [--from <phase>] [--skip-qa] [--cross] [--max-attempts N]"
---

# 프로세스 모듈 빌드 파이프라인 (Level 3: 체크포인트 + 자가수정)

빌드 대상: **$ARGUMENTS**

## 실행 원칙
- 기준 문서: `vault/01_구성원칙/표준프로세스_구성원칙.md`
- 문서체계: `vault/00_공통관리/01_문서체계.md` (8종 유형)
- 번호체계: `vault/00_공통관리/02_문서번호체계.md`
- 입력자료 규칙: `vault/00_공통관리/05_입력자료_규칙.md`
- **파이프라인 상태 규약**: `vault/00_공통관리/06_파이프라인_상태규약.md` (체크포인트/재개/자가수정)
- 모든 산출물: Obsidian 호환 MD(frontmatter + `[[wikilink]]`)

---

## Phase −2: Git Branch 격리 (state 결정 직전)

본 파이프라인은 **branch-per-standard** 정책을 따른다. main 은 harness 와 표준 등록 메타만 누적하고, 표준별 산출물은 격리된 feature branch 에 영구 보존한다.

### −2-1. 사전 등록 (main 작업)

표준 빌드 시작 전, 다음 두 파일에 **신규 표준 식별 정보**를 등록하고 main 에 직접 commit·push 한다:

- `vault/00_공통관리/02_문서번호체계.md` — 영역 코드 표 신규 행 + MAT 표준별 추적성 표 신규 행
- `vault/00_공통관리/07_표준분류레지스트리.md` — §2 해당 섹션에 row 추가 + §6 메타 모델 YAML block 추가

**진행 절차**:
```bash
git checkout main
git pull --ff-only
# (위 2개 파일 편집)
git add vault/00_공통관리/02_문서번호체계.md vault/00_공통관리/07_표준분류레지스트리.md
git commit -m "feat(registry): {표준코드} 영역코드 등록 + 표준분류레지스트리 등재"
git push origin main
```

**예외**: 사용자가 `--no-branch` 플래그로 비활성화하면 본 phase 전체를 skip (단일 main 작업 모드).

### −2-2. Feature branch 생성

main 의 등록 commit 위에서 분기:

```bash
git checkout -b feat/{모듈슬러그}-output
```

이후 모든 phase (preflight ~ qa, 자가수정) 는 이 branch 에서 작업.

**branch 명 컨벤션**:
- 형식: `feat/{모듈슬러그}-output`
- 모듈슬러그 결정 규칙:
  - 표준 코드 입력: 소문자 그대로. 예: `feat/iso9001-output`, `feat/cmmi-dev-ml3-output`
  - PA 그룹명 입력: 소문자·하이픈. 예: `feat/cmmi-prj-planning-output`
  - 자연어 입력: 핵심 키워드 추출 후 소문자·하이픈. 예: "프로젝트 계획·추정·리스크 관리" → `feat/prj-planning-est-risk-output`
  - 슬러그 결정 후 사용자에게 확인 후 진행
- 동일 모듈 재빌드 시: `feat/{모듈슬러그}-output-{YYYYMMDD}` 로 일자 suffix

### −2-3. 작업 도중 commit 정책

각 phase 종료 시 **선택적 중간 commit** (사용자 옵션 `--commit-per-phase` 시):
- analyze 종료: `feat({표준코드}): analyze 완료 — 요구사항 분해 N건`
- design 종료: `feat({표준코드}): design 완료 — POL N / PRO M`
- write 종료: `feat({표준코드}): write 완료 — WI/TMP/EX N×3`
- trace 종료: `chore({표준코드}): MAT 갱신 + MAT-{NNN} 신규`
- qa 종료: `chore({표준코드}): QA attempt N — Pass/Fail 통계`

기본은 **종료 시 일괄 4개 분할 commit**:
1. `feat({표준코드}): 표준 산출물 + 입력자료 (POL/PRO/WI/TMP/EX/REF)`
2. `chore(MAT): MAT-001~006 갱신 + MAT-{NNN} 신규`
3. `docs(MOC): 전체표준·추적성매트릭스 인덱스 갱신`
4. (필요 시) `fix({표준코드}): self-heal 후속 보정`

### −2-4. 종료 시 push

`overall_status: done` 도달 시:
```bash
git push -u origin feat/{표준코드}-output
```

main 에 merge 는 사용자 결정 사항. PR 생성 안내만 출력 (`gh pr create` 명령 예시).

### −2-5. 안전 가드

- main 에 절대 force-push 하지 않는다.
- branch 에 force-push 가 필요하면 `--force-with-lease` 사용.
- 빌드 실패·중단 시 branch 는 그대로 보존 (다음 attempt 재개 가능).

---

## Phase −1: State 결정 (가장 먼저)

### −1-1. `_state.yaml` 탐색
경로: `vault/02_표준/{표준코드}/_state.yaml`

| 상황 | 기본 동작 | 플래그 override |
|---|---|---|
| 파일 없음 | **Fresh 시작** — 템플릿 `T14_파이프라인상태.yaml` 복사 | — |
| `overall_status: done` | 사용자에게 "이미 완료. 재실행?" 질문 | `--restart` 강제 |
| `overall_status: halted` | "중단됨. 이어서? 새로 시작?" 질문 | `--resume` 자동 이어서 / `--restart` 신규 |
| `overall_status: running` (전 세션 중단) | 현재 `current_phase` 부터 재개 제안 | `--resume` 자동 / `--from <phase>` 지정 |

### −1-2. `--restart` 처리
기존 `_state.yaml` 을 `_state_{YYYYMMDD_HHMM}.yaml` 으로 rename 보존 → 신규 상태 파일 생성.

### −1-3. 진행 결정 보고
사용자에게 현재 attempt·다음 실행 phase·생략될 phase 를 요약 보고 후 진행.

---

## Phase 0: 입력자료·골든샘플 Preflight

(Fresh 시작 또는 `--from preflight` 시에만 실행. 재개 시엔 state 에서 done 이면 생략.)

0-1. `vault/02_표준/{표준코드}/_inputs/` 존재 확인
   - 없으면 폴더 + `_inputs/README.md` 스텁 생성 후 사용자에게:
     ```
     [Preflight 경고] {표준코드}/_inputs/ 에 입력자료가 없습니다.
     옵션:
       A) 지금 입력자료를 배치하고 재실행 (권장)
       B) LLM 추정만으로 진행 (정확도·감사 방어력 낮음)
     ```
   - B 선택 시에만 다음 단계 진행.

0-2. `vault/_inputs_common/` 선택 스캔.

0-3. 입력물 인벤토리 요약 보고(파일 수·카테고리·라이선스 상태).

0-4. **골든샘플 3종 선행 로드** (`vault/99_템플릿/_골든샘플/`): GS-POL-QMS-002 / GS-PRO-QMS-102 / GS-WI-102-04.

0-5. `_state.yaml` 의 `phases.preflight` 를 `status: done` 으로 갱신, `current_phase: analyze`.

---

## 정상 파이프라인 (Attempt N, 첫 실행)

각 에이전트는 **Phase −1(자체 Prerequisite 확인)** 을 실행하고, 완료 시 **done-marker 갱신** 을 한다 (상태규약 §4).

1. **Analyze** — Agent `standard-analyzer`
   - 출력: `02_표준/{표준코드}/` 개요·요구사항분해·작업노트, `09_REF_참고자료/`, `90_MAT/MAT-002`
   - done-marker 로 `phases.analyze` 완료 기록

2. **Design** — Agent `process-designer`
   - 출력: `03_POL_정책/POL-*`, `04_PRO_절차/PRO-*`, `90_MAT/MAT-003`
   - done-marker: `phases.design`

3. **Write** — Agent `wi-tmp-writer`
   - 출력: `05_WI_업무지침/`, `06_TMP_템플릿/`, `07_EX_작성예시/`, `90_MAT/MAT-001`
   - done-marker: `phases.write`

4. **Trace** — Agent `traceability-mapper`
   - 출력: `90_MAT_통합매핑/MAT-{NNN}_{표준코드}_추적성_*` (NNN 은 MAT-011 부터 순차. 기존 번호 스캔 후 max+1), 공통 매트릭스(MAT-001·003·004·005·006) 최신화, 02_문서번호체계 표에 신규 행 append
   - done-marker: `phases.trace`

5. **QA** — Agent `qa-reviewer` (옵션 `--skip-qa` 시 생략)
   - 리포트: `02_표준/{표준코드}/99_QA리포트_{YYYYMMDD}_attempt{N}.md`
   - done-marker + `qa_failures[]` (Fail 있을 때)

---

## 자가수정 루프 (Self-Correction Loop)

```
Attempt N 종료 시점에 qa_failures 평가:
  ├─ 빈 배열 (ALL PASS)
  │     → overall_status: done · current_phase: done · MOC ✅ 갱신 · 종료
  │
  ├─ 비어있고 N >= max_attempts (기본 3)
  │     → overall_status: halted · 사용자 에스컬레이션
  │
  └─ 비어있고 N < max_attempts
        → 자가수정 모드로 Attempt N+1 개시
```

### 자가수정 실행 순서
R-1. `_state.yaml` 의 `attempts` +1, `history` 에 `event: self_heal_start` append.
R-2. `qa_failures[]` 를 `assigned_to` 로 그룹화.
R-3. **그룹 순서**: `standard-analyzer` → `process-designer` → `wi-tmp-writer` → `traceability-mapper` 순서(상류부터 하류로).
R-4. 각 그룹당 해당 에이전트를 **자가수정 모드**로 재호출. 프롬프트에 명시:
   ```
   [자가수정 모드]
   아래 qa_failures 이슈만 처리하시오. 다른 작업 금지.
   이슈 목록:
   - issue_id / severity / description / fix_scope
   ...
   처리 완료 시 _state.yaml 의 qa_failures 에서 해당 issue_id 제거.
   phases.{자기} status 는 done 유지, history 에 phase_rerun_for_fix 기록.
   ```
R-5. 모든 그룹 처리 후 **Agent `qa-reviewer` 재실행**.
R-6. QA 결과로 루프 재평가.

### `assigned_to: manual` 처리
- 자동 수정 불가 → 루프 중단하고 사용자에게 직접 보고·지시 요청.

### `--skip-qa` 플래그
- QA·자가수정 루프 생략. `overall_status: done` 으로 직접 이동 (프로덕션 비권장).

---

## Phase Final: 마무리
- `00_MOC/MOC_전체표준.md` 상태 ✅ 갱신
- `_state.yaml` 의 `overall_status: done` 확인
- 생성/수정 파일 요약, 잔여 Issue 보고

---

## 플래그 정리

| 플래그 | 효과 |
|---|---|
| (기본) | state 감지 자동 판단, QA·자가수정 포함 |
| `--restart` | 기존 state 아카이브 후 처음부터 |
| `--resume` | 질문 없이 현재 phase 부터 자동 재개 |
| `--from <phase>` | 강제 특정 phase 부터 시작 (preflight/analyze/design/write/trace/qa) |
| `--skip-qa` | QA·자가수정 루프 생략 |
| `--cross` | trace 단계에서 교차 표준 통합 분석 포함 |
| `--max-attempts N` | 자가수정 최대 횟수 변경 (기본 3) |
| `--no-branch` | Phase −2 (git branch 격리) skip — 단일 main 작업 모드 |
| `--commit-per-phase` | 각 phase 종료 시 중간 commit (기본은 종료 시 일괄 4분할) |

---

## 규칙
- 각 phase 는 **state.yaml 선행 확인** 후 진행
- 구성원칙·문서체계 위반 결정은 즉시 정지 후 질문
- REC(기록)은 본 파이프라인에서 **생성하지 않음** — 운영 단계에서만

---

## 최종 보고
- 🧭 state 요약 (attempts, 최종 overall_status, 각 phase 소요 시간)
- 📥 `_inputs/` 활용 요약
- 🔄 자가수정 루프 요약 (attempt 별 Pass/Fail, 수정 건수)
- ✅ 생성 파일 트리
- 📊 요구사항 커버리지
- 🔗 `source_citation` 누락 건수 (목표: 0)
- 📋 MAT 5종 갱신 요약
- 🚩 잔여 Issue (`manual` 에스컬레이션 + 미해결)
- 🌿 git branch 정보 (현재 branch / origin push 결과 / PR 생성 안내)
- ➡️ 다음 권장 빌드 (연관 모듈·갭 보완 제안)
