#!/bin/sh
# Routing is on unless QSTACK_SESSION_HOOK=off or the user settings file says `session hook: off`.
[ "${QSTACK_SESSION_HOOK:-on}" = "off" ] && exit 0
settings="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/qstack.md"
if [ -r "$settings" ] && grep -qiE '^[[:space:]]*session hook:[[:space:]]*off[[:space:]]*$' "$settings"; then
  exit 0
fi
cat "$(dirname "$0")/session-start-context.md"
