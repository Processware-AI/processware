#!/usr/bin/env bash
# 조직 루트 repo 에 vault → Redmine 자동 동기화 post-commit hook 설치 (org-layer 단계 6)
#
# 사용 (플랫폼 체크아웃에서):
#   bash publish/redmine/install-hook.sh --org-root /work/acme
# 또는 조직 루트에서 PROCESSWARE_ORG_ROOT 를 설정하고:
#   bash <플랫폼>/publish/redmine/install-hook.sh

set -euo pipefail

PLATFORM_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
ORG_ROOT="${PROCESSWARE_ORG_ROOT:-}"
if [[ "${1:-}" == "--org-root" && -n "${2:-}" ]]; then
    ORG_ROOT="$2"
fi
if [[ -z "$ORG_ROOT" ]]; then
    echo "❌ 조직 루트가 필요합니다: --org-root <path> 또는 PROCESSWARE_ORG_ROOT" >&2
    exit 1
fi
if [[ ! -f "$ORG_ROOT/org.yaml" ]]; then
    echo "❌ 조직 루트가 아닙니다 (org.yaml 없음): $ORG_ROOT" >&2
    exit 1
fi
if ! git -C "$ORG_ROOT" rev-parse --git-dir >/dev/null 2>&1; then
    echo "❌ 조직 루트가 git repo 가 아닙니다: $ORG_ROOT  (git init 후 재실행)" >&2
    exit 1
fi

HOOK_DST="$(git -C "$ORG_ROOT" rev-parse --git-path hooks)/post-commit"
HOOK_SRC="$PLATFORM_ROOT/publish/redmine/post-commit.hook"

mkdir -p "$ORG_ROOT/.processware"
echo "$PLATFORM_ROOT" > "$ORG_ROOT/.processware/platform_root"

if [[ -f "$HOOK_DST" ]]; then
    if grep -q "vault-redmine-sync" "$HOOK_DST" 2>/dev/null; then
        echo "✅ vault-redmine-sync hook 이미 설치되어 있습니다: $HOOK_DST"
        exit 0
    fi
    { echo ""; cat "$HOOK_SRC"; } >> "$HOOK_DST"
    echo "✅ 기존 post-commit hook 에 vault-redmine-sync 추가: $HOOK_DST"
else
    cp "$HOOK_SRC" "$HOOK_DST"
    chmod +x "$HOOK_DST"
    echo "✅ post-commit hook 설치: $HOOK_DST"
fi

echo ""
echo "사전 조건:"
echo "  1. export REDMINE_API_KEY=your_api_key"
echo "  2. $ORG_ROOT/org.yaml → redmine.enabled: true"
echo "  3. $ORG_ROOT/publish/redmine/config.yaml 에 실제 URL 입력"
echo "  4. pip3 install -r $PLATFORM_ROOT/publish/redmine/requirements.txt"
