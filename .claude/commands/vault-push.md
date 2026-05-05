---
description: vault → Redmine Process Library 단방향 동기화. final 상태 문서를 Library Module wiki/issue로 push.
---

vault를 Redmine Process Library에 단방향 Push하는 스킬입니다.

## 사용법

```
/vault-push [옵션]
```

| 명령 | 동작 |
|---|---|
| `/vault-push` | vault 전체 → Library 동기화 |
| `/vault-push --changed` | git diff 변경분만 |
| `/vault-push --setup` | Redmine Library 프로젝트 계층 자동 생성 |
| `/vault-push --setup --dry-run` | 생성 예정 프로젝트 미리보기 |
| `/vault-push WI-ISO27001-001-001-001` | 특정 문서 1건 |
| `/vault-push --type WI` | WI 전체 |
| `/vault-push --scope ISO27001` | 특정 표준 전체 |
| `/vault-push --dry-run` | 실제 전송 없이 미리보기 |
| `/vault-push --status` | 마지막 동기화 상태 |

## 실행 방법

아래 명령을 터미널에서 실행하거나, 이 스킬이 호출되면 자동으로 실행합니다.

```bash
cd integrations/redmine
python3 sync.py [옵션]
```

## 사전 조건

1. `integrations/redmine/config.yaml` 에 실제 Redmine URL과 API KEY 입력
2. 환경변수 설정: `export REDMINE_API_KEY=your_key`
3. 의존 패키지 설치: `pip3 install -r integrations/redmine/requirements.txt`
4. Redmine에 `lib-{scope_code}` 상위 프로젝트 수동 생성 (최초 1회)
5. `/vault-push --setup` 으로 Library Module 서브프로젝트 자동 생성

## 동기화 규칙

- `status: draft` 문서는 skip
- POL/PRO/WI/TMP/EX/MAT → Wiki 페이지
- REC/REC-NCR → Issue (Tracker: 프로세스기록/NCR)
- Obsidian `[[wikilink]]` → Redmine wiki 링크 자동 변환
- 모든 페이지에 자동생성 헤더 삽입 (직접 편집 금지 안내 포함)

## Workspace 생성

표준 프로세스를 특정 업무 프로젝트(Workspace)에 복사하려면:

```
/workspace-create --name "프로젝트명" --slug slug명 --modules PRO-XXX,PRO-YYY
```

## 이 스킬이 호출되면

다음 단계를 수행합니다:

1. `integrations/redmine/config.yaml` 설정 확인
2. `REDMINE_API_KEY` 환경변수 확인
3. 사용자 요청에 맞는 인수로 `python3 integrations/redmine/sync.py` 실행
4. 결과(생성/갱신/건너뜀/오류) 보고
