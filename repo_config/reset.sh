#!/usr/bin/env bash
set -euo pipefail

if [[ ! -d data ]]; then
    printf 'No generated runtime state found.\n'
    exit 0
fi

read -r -p 'Delete generated runtime state in ./data? [y/N] ' confirmation
if [[ "$confirmation" != "y" && "$confirmation" != "Y" ]]; then
    printf 'Reset cancelled.\n'
    exit 0
fi

rm -rf -- data
printf 'Generated runtime state removed.\n'
