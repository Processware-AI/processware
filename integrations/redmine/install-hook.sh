#!/usr/bin/env bash
# vault 변경 시 Redmine 자동 동기화 git hook 설치 스크립트.
# 프로젝트 루트에서 실행: bash integrations/redmine/install-hook.sh

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOK_DST="$REPO_ROOT/.git/hooks/post-commit"
HOOK_SRC="$REPO_ROOT/integrations/redmine/post-commit.hook"

# 이미 다른 hook이 있으면 append, 없으면 새로 생성
if [[ -f "$HOOK_DST" ]]; then
    if grep -q "vault-redmine-sync" "$HOOK_DST" 2>/dev/null; then
        echo "✅ vault-redmine-sync hook 이미 설치되어 있습니다."
        exit 0
    fi
    echo "" >> "$HOOK_DST"
    cat "$HOOK_SRC" >> "$HOOK_DST"
    echo "✅ 기존 post-commit hook에 vault-redmine-sync 추가 완료."
else
    cp "$HOOK_SRC" "$HOOK_DST"
    chmod +x "$HOOK_DST"
    echo "✅ post-commit hook 설치 완료: $HOOK_DST"
fi

echo ""
echo "사전 조건:"
echo "  1. export REDMINE_API_KEY=your_api_key"
echo "  2. integrations/redmine/config.yaml 에 실제 URL 입력"
echo "  3. pip3 install -r integrations/redmine/requirements.txt"
