#!/bin/sh
# QSTACK_SESSION_HOOK=off disables the routing mandate without uninstalling the plugin.
[ "${QSTACK_SESSION_HOOK:-on}" = "off" ] && exit 0
cat "$(dirname "$0")/session-start-context.md"
