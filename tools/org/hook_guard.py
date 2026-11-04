"""Claude Code PreToolUse 훅 — Write/Edit/MultiEdit/NotebookEdit 의 대상 경로를 격리 가드로 검사 (org-layer 단계 5).

stdin: Claude Code 훅 JSON ({"tool_name": ..., "tool_input": {"file_path": ...}})
exit 0  : 허용 (또는 판단 불가 — 조직 컨텍스트 없음 · 입력 파싱 실패)
exit 2  : 차단. stderr 의 메시지가 Claude 에게 전달된다

차단하는 경우 (활성 조직 컨텍스트가 있을 때만):
  - {ORG_ROOT}/vault 의 플랫폼 관리(managed) 파일에 쓰기
  - 플랫폼 repo 의 vault/ inputs/ sources/ .processware/ (단계 3 에서 제거된 위치) 에 쓰기
  - 조직 루트 · 플랫폼 둘 다 아닌 곳에 쓰기
플랫폼 자산(.claude/ tools/ docs/ core/)은 플랫폼 개발 작업이므로 차단하지 않는다.

설정: .claude/settings.json → hooks.PreToolUse (matcher Write|Edit|MultiEdit|NotebookEdit)
"""

from __future__ import annotations

import json
import os
import sys


def _target_path(data: dict):
    ti = data.get("tool_input") or {}
    for k in ("file_path", "notebook_path", "path"):
        v = ti.get(k)
        if isinstance(v, str) and v:
            return v
    return None


def main() -> int:
    # Windows 콘솔(cp949)에서도 훅 JSON(한글 경로)을 깨지지 않게 읽고 쓴다 — stdin 도 반드시 UTF-8
    for s in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            try:
                s.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass

    if not (os.environ.get("PROCESSWARE_ORG_ROOT") or os.environ.get("PROCESSWARE_ORG")):
        return 0  # 조직 컨텍스트 없음 — 플랫폼 개발 세션

    try:
        data = json.load(sys.stdin)
    except Exception as e:
        print(f"[org-guard] 훅 입력 파싱 실패, 가드 생략: {e}", file=sys.stderr)
        return 0
    path = _target_path(data)
    if not path:
        return 0

    try:
        from .context import OrgContextError, resolve
        from .guard import Guard
        ctx = resolve(strict=False)
    except Exception as e:  # 컨텍스트 해석 실패 — 차단하지 않고 경고만
        print(f"[org-guard] 조직 컨텍스트 해석 실패, 가드 생략: {e}", file=sys.stderr)
        return 0

    res = Guard(ctx).check(path, mode="write", allow_platform=True)
    if res.ok:
        return 0
    tool = data.get("tool_name", "Write")
    print(f"[org-guard] {tool} 차단: {res.path}\n  zone={res.zone} managed={res.managed}\n  {res.reason}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
