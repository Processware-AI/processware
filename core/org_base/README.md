---
type: org-root-readme
title: Processware 조직 루트
updated: 2026-11-05
tags: [org-root, processware]
---

# Processware 조직 루트

이 디렉토리는 한 조직의 **표준 프로세스 자산 전체** 를 담는 조직 루트(`{ORG_ROOT}`)다.
플랫폼 repo(에이전트·커맨드·규칙·템플릿)와는 **별도 git repo** 로 관리한다 (NDA 격리).

설계: 플랫폼 repo `docs/architecture/org-layer.md`

## 구조

```
{ORG_ROOT}/
├── org.yaml                 ← 조직 설정 (org_id · 명칭 · 영역코드 · RBAC 배정 · Redmine)
├── sources/                 ← 원본 파일 투하 (표준 PDF · 법규 · AsIs DOCX …) — git 제외
├── inputs/                  ← /process-ingest 산출물 (YAML · MD) — 01_표준원문 ~ 06_목표흐름
├── vault/                   ← Obsidian vault — Open folder as vault
│   ├── 00_공통관리 · 01_구성원칙 · 99_템플릿   ← 플랫폼 관리 (sync-core 가 덮어씀, 직접 수정 금지)
│   ├── 00_MOC · 90_MAT_통합매핑               ← 플랫폼 시드 → 조직 소유 (sync-core 가 보존)
│   └── 02_적용요건 · 03_POL ~ 09_REF           ← 조직 산출물
└── .processware/
    ├── runs/                ← 실행 trace (감사 증적 — git 추적)
    ├── queues/process-act/  ← 차원 4 인계 큐
    ├── states/              ← 차원 1 체크포인트
    └── sync-core.yaml       ← 마지막 sync-core 기록
```

## 사용

플랫폼 repo 체크아웃에서, 이 루트를 활성 조직으로 지정해 커맨드를 실행한다.

```bash
export PROCESSWARE_ORG_ROOT=/path/to/this-dir      # 또는 레지스트리 등록 후 export PROCESSWARE_ORG=<org_id>
python3 -m tools.org context --format table         # 해석 확인
python3 -m tools.org sync-core                      # 플랫폼 갱신 반영 (managed 덮어쓰기 · seed 보존)
python3 -m tools.org sync-core --dry-run            # 변경 미리보기
```

## 규칙

- `vault/00_공통관리` · `01_구성원칙` · `99_템플릿` 과 각 폴더의 `README.md` 는 **플랫폼 관리** 파일이다. 수정하지 말고, 조직별 추가 사항은 별도 파일로 둔다 (예: `00_공통관리/03_용어집_조직추가.md`).
- `90_MAT_통합매핑/MAT-*.md` 와 `00_MOC/*.md` 는 최초 1회 시드된 뒤 **조직이 소유** 한다. sync-core 는 덮어쓰지 않는다 (`--force` 로 재시드 가능).
- `org.yaml` 의 `platform_version` 은 sync-core 가 자동 갱신한다. 플랫폼 커밋과의 정합성 확인용.
- 이 루트 밖(플랫폼 repo)에는 조직 데이터를 두지 않는다.

## Git

이 루트는 **자체 git repo** 다. 처음 한 번:

```bash
git -C <이 루트> init -b main
git -C <이 루트> add -A && git -C <이 루트> commit -m "chore(org): 조직 루트 초기화"
```

- `/process-plan` 은 **branch-per-standard** 로 동작한다: 기준 브랜치(main)에 `org.yaml scopes` · `00_MOC/MOC_추적성매트릭스.md` 등록 커밋 → `feat/{슬러그}-output` 브랜치에 산출물 · `.processware/states` · `.processware/runs` 커밋 → origin 이 있으면 push 후 PR 안내. 모든 git 명령은 `git -C <이 루트>` 로 실행되며 플랫폼 repo 에서는 실행되지 않는다.
- 플랫폼 관리 파일 변경(sync-core 결과)은 산출물 커밋과 섞지 않고 `chore(sync-core): platform <version>` 으로 기준 브랜치에 따로 커밋한다.
- 관리 폴더 안의 조직 추가 파일은 `*_조직추가.md` 로 이름 짓는다 (예: `00_공통관리/07_표준분류레지스트리_조직추가.md`) — 가드가 쓰기를 허용하고 sync-core 가 보존한다.
- `.github/workflows/vault-push.yml` 은 main push 시 Redmine Library 로 단방향 push 한다 (`org.yaml redmine.enabled: true` + 시크릿 설정 시).
