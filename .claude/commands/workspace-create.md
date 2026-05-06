---
description: Process Library에서 PRO Module을 선택·복사하여 현업 업무 단위 Workspace를 생성하거나 관리한다. --target으로 백엔드 선택 (기본값: publish/config.yaml의 default_target).
---

현업 업무(프로젝트/스코프)를 위한 Workspace를 Process Library에서 복사·조합하여 생성합니다.

## 개념

```
Process Library (vault 관리, READ ONLY)
  lib-iso27001-p001-001   ← 표준 프로세스 원본
  lib-iso27001-p001-002

       ↓ /workspace-create (필요한 PRO 선택)

Workspace (팀 관리, 자율 편집)
  ws-product-alpha
  ├── ws-product-alpha-p001-001   ← Library 복사본
  └── ws-product-alpha-p001-002   ← Library 복사본
```

- Library Module: vault push로 관리, 직접 편집 금지
- Workspace Module: 생성 후 팀 소유, 자유 편집 가능
- 버전 업데이트 필요 시: `/workspace-create sync`

## 사용법

### Workspace 생성

```
/workspace-create create \
  --name "제품Alpha 개발" \
  --slug product-alpha \
  --modules PRO-ISO27001-001-001,PRO-ISO27001-001-002
  [--target confluence]
```

옵션:
- `--name`: 워크스페이스 표시 이름
- `--slug`: URL-safe 식별자
- `--modules`: 쉼표 구분 PRO doc_id 목록
- `--description`: 설명 (선택)
- `--dry-run`: 실제 생성 없이 미리보기
- `--target`: 백엔드 지정 (기본값: `publish/config.yaml` 의 `default_target`)

### Library Module 최신화

```
/workspace-create sync \
  --workspace ws-product-alpha \
  --module lib-iso27001-p001-001
```

### 목록 조회

```
/workspace-create list
```

### 특정 Workspace 상세

```
/workspace-create status --workspace ws-product-alpha
```

## 실행 방법

```bash
python3 publish/dispatcher.py workspace [--target <backend>] create --name "..." --slug "..." --modules "PRO-XXX,PRO-YYY"
python3 publish/dispatcher.py workspace sync   --workspace ws-{slug} --module lib-{scope}-{pro_slug}
python3 publish/dispatcher.py workspace list
python3 publish/dispatcher.py workspace status --workspace ws-{slug}
```

## 사전 조건

1. Process Library 구성 완료 (`/vault-push --setup` 실행)
2. `publish/{target}/config.yaml` 의 `by_pro` 섹션에 PRO → Library Module 매핑 등록
3. 접속 정보 및 API KEY 환경변수 설정

## 이 스킬이 호출되면

1. `publish/config.yaml` 에서 `default_target` 확인 (또는 `--target` 인수 우선)
2. `publish/{target}/adapter.py` 동적 로드
3. `by_pro` 매핑 확인
4. `--modules` 의 각 PRO doc_id → Library Module identifier 변환
5. 외부 시스템에 `ws-{slug}` 상위 프로젝트 생성
6. 각 PRO → `ws-{slug}-{pro_slug}` 서브프로젝트 생성
7. Library Module 문서 전체 복사 (워크스페이스 헤더로 변환)
8. workspace_map DB 등록
9. 결과 요약 출력
