#!/usr/bin/env bash
set -euo pipefail

if ! command -v uv >/dev/null 2>&1; then
    printf 'uv is required. Run ./bot --setup after installing it from https://docs.astral.sh/uv/getting-started/installation/\n' >&2
    exit 1
fi

exec uv run python src/bot.py "$@"
