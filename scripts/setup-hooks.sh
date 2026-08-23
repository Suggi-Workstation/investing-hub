#!/bin/sh
# Run this ONCE per machine, standing inside the repo folder:
#   bash scripts/setup-hooks.sh
# It switches on the local ASCII guard for this repo on this machine.
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
echo "Done. This machine now refuses non-ASCII commits in this repo."
