---
type: guide
doc_id: MAN-07
title: "사용자 매뉴얼 — 07. FAQ (자주 묻는 질문)"
version: "1.0"
status: approved
created: 2026-05-03
updated: 2026-05-03
tags: [manual, faq, guide, troubleshooting]
---

# 07. FAQ — 자주 막히는 문제

---

## /process-plan 관련

### Q. 자연어 입력과 표준 코드 입력 중 어느 게 낫나?

**A.** 대부분의 경우 자연어가 더 낫다. 표준 코드를 입력하면 그 표준 전체를 빌드하려 하지만, 자연어를 입력하면 "내가 실제로 필요한 것"에 집중해서 빌드한다.

```bash
# 비권장: 표준 전체를 빌드 (필요 없는 것도 포함)
/process-plan iso9001

# 권장: 필요한 업무 체계를 설명
/process-plan "품질목표 수립·모니터링·불적합품 관리"
```

### Q. 입력자료(PDF 등)가 없어도 빌드가 되나?

**A.** 된다. LLM이 해당 표준에 대한 지식으로 추정해서 빌드한다. 다만 요구사항 커버리지가 낮거나 특수 요건을 놓칠 수 있다. 정확도가 중요하면 PDF를 `_inputs/01_표준원문/`에 배치하고 재실행 권장.

### Q. 빌드 중간에 실수로 Claude Code를 닫았다. 어떻게 하나?

**A.** `--resume` 플래그로 이어서 실행한다. 진행 상태는 `vault/02_표준/{모듈}/_state.yaml`에 저장되어 있다.

```bash
/process-plan "프로젝트 계획·추정·리스크 관리" --resume
```

### Q. QA가 계속 실패한다. 어떻게 해야 하나?

**A.** 자가수정이 3회(기본) 후에도 실패하면 `manual` 에스컬레이션이 발생한다. 이때:
1. QA 리포트 파일 열기: `vault/02_표준/{모듈}/99_QA리포트_*.md`
2. `assigned_to: manual` 항목 확인
3. 수동으로 해당 파일 수정
4. `--from qa` 로 QA만 재실행

```bash
/process-plan "모듈명" --from qa
```

### Q. CMMI를 전부 빌드하려면 어떻게 하나?

**A.** PA 그룹을 나눠서 순서대로 빌드하는 것을 강력히 권장한다. 한 번에 전체를 빌드하면 너무 크다.

```bash
# 조직 기반 (1회 구축)
/process-plan CMMI-ORG-FOUNDATION

# 프로젝트 계획·관리
/process-plan CMMI-PRJ-PLANNING

# 기술 개발
/process-plan CMMI-PRJ-ENGINEERING

# 프로젝트 지원
/process-plan CMMI-PRJ-SUPPORT
```

---

## /process-do 관련

### Q. WI 번호를 모른다. 어떻게 찾나?

**A.** 자연어로 입력하면 AI가 자동으로 매칭해준다.

```bash
/process-do "형상 항목 식별"
# → 자동 매칭: WI-CM-201-01_형상항목식별.md (신뢰도: 0.94)
```

또는 `vault/05_WI_업무지침/`을 Obsidian에서 검색.

### Q. HITL 승인 요청이 왔는데 무엇을 확인해야 하나?

**A.** `.claude/runs/{trace_id}/approval_request.md` 파일에 승인 요청 내용이 있다. 확인 사항:
- step 이름과 수집된 정보
- 승인의 의미 (다음에 무슨 일이 일어나는지)
- 반려 시 어떤 결과가 생기는지

```bash
/process-do --status run-a3f9c2b1     # 현재 상태 확인
```

### Q. 반려 후 수정해서 다시 실행할 수 있나?

**A.** 반려된 trace는 `status: rejected`로 마감된다. 수정 후 새로 실행하려면:

```bash
/process-do WI-PPR-101-01     # 새 trace_id로 새로 시작
```

### Q. dry-run으로 먼저 확인하고 싶다.

**A.** `--dry-run` 플래그를 사용한다. 대화는 진행되지만 REC와 MAT-005는 저장되지 않는다.

```bash
/process-do --dry-run WI-PPR-101-01
```

---

## /process-check 관련

### Q. "독립성 위반" 오류가 난다. 어떻게 해결하나?

**A.** ISO §9.2 독립성 원칙에 따라, 자신이 실행한 기록을 자신이 심사할 수 없다.

해결 방법:
1. **다른 사람에게 심사 요청** (실운영)
2. **PoC·학습 목적**: `--override-independence` 플래그 사용

```bash
/process-check start PRO-PPR-101 --auditor "나" --override-independence
```

### Q. NCR이 너무 많다. 한꺼번에 처리할 방법이 있나?

**A.** 같은 원인의 NCR이 여러 개라면 `/process-act start --batch`로 일괄 처리한다.

```bash
/process-act start --batch queue-q001,queue-q002,queue-q003
```

### Q. KPI 측정값이 이상하다. 어디서 확인하나?

**A.** kpi-collector가 수집한 raw data는 `kpi_data.yaml`에 있다. trace 디렉터리에서 확인:

```bash
ls .claude/runs/run-k*/
# kpi_data.yaml 확인
```

측정 source가 잘못됐다면 `/process-check --kpi start ... --period` 로 기간을 조정해서 재실행.

---

## /process-act 관련

### Q. act queue가 자동으로 생성되지 않는다.

**A.** act queue는 `/process-check`의 `--confirm` 이후 critical finding 또는 critical KPI가 있을 때만 생성된다. 현황 확인:

```bash
/process-act --list --status pending
ls .claude/queues/process-act/
```

큐가 없다면 심사에서 critical 판정이 없었던 것이다.

### Q. PCB 승인 없이 빠르게 테스트하고 싶다.

**A.** `--auto-approve` 플래그를 사용한다. PoC·테스트 전용이며 실운영에서는 사용하지 않는다.

```bash
/process-act start queue-q001 --auto-approve
```

---

## Git·브랜치 관련

### Q. main과 feat 브랜치의 차이가 뭔가?

**A.**
- **main**: 플랫폼(도구)만 — AI 에이전트, 커맨드 4종, vault 구조 템플릿
- **feat/{모듈}-output**: 실제 프로세스 자산 — POL/PRO/WI/TMP/EX와 실행 기록(REC)

프로세스 문서를 보려면 feat 브랜치로 이동하거나 worktree를 사용한다.

### Q. 여러 표준 모듈을 동시에 Obsidian에서 보고 싶다.

**A.** `git worktree`로 각 브랜치를 별도 폴더에 마운트하면 된다.

```bash
git worktree add ../qa-view feat/sw-qa-cm-output
git worktree add ../planning-view feat/prj-planning-est-risk-output
```

각 폴더를 Obsidian의 별도 vault로 열거나, 상위 폴더를 열면 모든 vault가 보인다.

### Q. feat 브랜치를 main에 합쳐도 되나?

**A.** 기술적으로 가능하지만 **권장하지 않는다**. 브랜치를 분리하는 이유가 모듈 독립성이다. merge하면:
- main에 프로세스 자산이 섞임
- 여러 모듈의 파일 번호가 충돌할 가능성

대신 worktree로 열어서 사용하거나, 모듈별로 Obsidian vault를 분리해서 운영한다.

---

## Obsidian 관련

### Q. Obsidian 그래프 뷰에서 연결이 안 보인다.

**A.** `[[wikilink]]` 형식의 내부 링크가 제대로 생성됐는지 확인. Obsidian 설정에서 "Use [[Wikilinks]]" 활성화 필요.

### Q. frontmatter가 보기 불편하다.

**A.** Obsidian 설정 → Editor → "Show frontmatter" 비활성화하면 본문만 보인다.

---

## 일반

### Q. CMMI 인증을 받고 싶은데 어떻게 해야 하나?

**A.** 필요한 프로세스를 먼저 빌드하고 운영한 다음, 갭 분석으로 부족한 부분만 추가한다.

```bash
# 1단계: 필요한 프로세스 빌드·운영
/process-plan "프로젝트 계획·관리"
/process-plan "기술 개발 프로세스"

# 2단계: 몇 개월 운영 후 CMMI-ML3 대비 갭 분석
/process-check --against CMMI-ML3    # (예정 기능)

# 3단계: 갭만 추가 빌드
/process-plan "부족한 PA"
```

표준이 목적이 아니라 도구가 된다.

### Q. 새 표준(ISO 27001, ISO 9001 등)을 추가하려면?

**A.** 표준 코드를 레지스트리에 등록한 후 빌드한다. `/process-plan` 실행 시 Phase -2에서 자동으로 등록 안내를 한다.

```bash
/process-plan "정보보안 위험관리·접근통제"    # ISO 27001 기반
```

또는 표준 코드로 직접:
```bash
/process-plan iso27001-isms
```
