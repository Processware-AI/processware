---
description: vault → 외부 시스템 Process Library 단방향 동기화. final 상태 문서를 Library Module로 push. --target으로 백엔드 선택 (기본값: publish/config.yaml의 default_target).
---

vault를 외부 시스템 Process Library에 단방향 Push하는 스킬입니다.

## 사용법

```
/vault-push [--target <backend>] [옵션]
```

| 명령 | 동작 |
|---|---|
| `/vault-push` | vault 전체 → Library 동기화 |
| `/vault-push --changed` | git diff 변경분만 |
| `/vault-push --setup` | Library 프로젝트 계층 자동 생성 |
| `/vault-push --setup --dry-run` | 생성 예정 프로젝트 미리보기 |
| `/vault-push WI-ISO27001-001-001-001` | 특정 문서 1건 |
| `/vault-push --type WI` | WI 전체 |
| `/vault-push --scope ISO27001` | 특정 표준 전체 |
| `/vault-push --dry-run` | 실제 전송 없이 미리보기 |
| `/vault-push --status` | 마지막 동기화 상태 |
| `/vault-push --target confluence` | Confluence 백엔드 사용 |

## 지원 백엔드

| backend | 어댑터 경로 | 상태 |
|---|---|---|
| `redmine` | `publish/redmine/adapter.py` | 구현 완료 |
| 기타 | `publish/{target}/adapter.py` | 어댑터 추가 시 자동 인식 |

기본값은 `publish/config.yaml`의 `default_target` 필드로 지정합니다.

## 실행 방법

```bash
python3 publish/dispatcher.py push [--target <backend>] [옵션]
```

예시:
```bash
python3 publish/dispatcher.py push --dry-run
python3 publish/dispatcher.py push --target redmine --changed
python3 publish/dispatcher.py push --setup
```

## 사전 조건

1. `publish/config.yaml` 에 `default_target` 설정 (또는 `--target` 명시)
2. `publish/{target}/config.yaml` 에 접속 정보 입력
3. 환경변수 설정: `export REDMINE_API_KEY=your_key` (Redmine 사용 시)
4. 의존 패키지 설치: `pip3 install -r publish/{target}/requirements.txt`
5. `/vault-push --setup` 으로 Library 구조 초기화 (최초 1회)

## 새 백엔드 추가 방법

1. `publish/{target}/` 폴더 생성
2. `publish/{target}/adapter.py` 에 `BaseAdapter` 상속 클래스 구현
3. `publish/{target}/config.yaml` 작성
4. `publish/config.yaml` 의 `default_target` 변경 (선택)

## 이 스킬이 호출되면

1. `publish/config.yaml` 에서 `default_target` 확인 (또는 `--target` 인수 우선)
2. `publish/{target}/adapter.py` 동적 로드
3. `publish/{target}/config.yaml` 설정 로드
4. 사용자 요청에 맞는 메서드 실행
5. 결과(생성/갱신/건너뜀/오류) 보고
