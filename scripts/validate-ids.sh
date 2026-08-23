#!/bin/bash
# validate-ids.sh -- check frontmatter IDs for manual rounding
#
# WHAT: scans markdown files with YAML frontmatter id: fields and flags
# timestamps that appear to be manually typed rather than generated from
# `date -u +'%Y%m%dT%H%M%SZ'`.
#
# RULES:
#   1. id: must end in valid UTC seconds (00-59), not suspicious 00.
#      A timestamp ending in ...0000Z is almost certainly human-rounded.
#      Soft-warn if seconds are 00.
#   2. id: must match ISO 8601 format YYYYMMDDTHHMMSSZ.
#   3. id: must not be a duplicate of another file's id.
#   4. id: must not be in the future (allow 5 min clock skew).
#
# USAGE: validate-ids.sh [file...]
#   No args: scan all tracked markdown files in current repo.
#   With args: scan only the given files (for pre-commit hook use).

set -euo pipefail

errors=0
warnings=0
files_with_ids=0

# Collect all ids for duplicate check
declare -A id_map

# If no args, scan all tracked markdown files
if [ $# -eq 0 ]; then
  mapfile -t FILES < <(git ls-files '*.md')
else
  FILES=("$@")
fi

NOW=$(date -u +%s)

for f in "${FILES[@]}"; do
  [ -f "$f" ] || continue

  # Extract id: value from YAML frontmatter (between --- markers)
  id=$(awk '/^---$/ {c++; next} c==1 && /^id: / {print $2; exit} c>=2 {exit}' "$f" 2>/dev/null || true)
  [ -z "$id" ] && continue

  files_with_ids=$((files_with_ids + 1))

  # Check 1: ISO 8601 format
  if ! echo "$id" | grep -qE '^[0-9]{8}T[0-9]{6}Z$'; then
    echo "INVALID FORMAT: $f -> id: $id (not YYYYMMDDTHHMMSSZ)"
    errors=$((errors + 1))
    continue
  fi

  # Check 2: Human-rounded seconds (ends in 00Z)
  if echo "$id" | grep -qE 'T[0-9]{4}00Z$'; then
    echo "SUSPECT ROUNDED: $f -> id: $id (seconds are 00 -- likely manually typed, not from date -u)"
    warnings=$((warnings + 1))
  fi

  # Check 3: Duplicates
  if [ -n "${id_map[$id]:-}" ]; then
    echo "DUPLICATE ID: $f shares id: $id with ${id_map[$id]}"
    errors=$((errors + 1))
  else
    id_map[$id]="$f"
  fi

  # Check 4: Future timestamp
  ts=$(echo "$id" | sed 's/T//;s/Z//')
  ts_epoch=$(date -u -d "${ts:0:4}-${ts:4:2}-${ts:6:2} ${ts:8:2}:${ts:10:2}:${ts:12:2}" +%s 2>/dev/null || echo 0)
  if [ "$ts_epoch" -gt $((NOW + 300)) ]; then
    echo "FUTURE TIMESTAMP: $f -> id: $id (timestamp is in the future)"
    errors=$((errors + 1))
  fi
done

echo ""
echo "Scanned $files_with_ids files with frontmatter IDs."
echo "Errors: $errors | Warnings: $warnings"

if [ "$errors" -gt 0 ]; then
  echo ""
  echo "ERRORS FOUND -- fix before committing."
  exit 1
fi

if [ "$warnings" -gt 0 ]; then
  echo ""
  echo "WARNINGS: run 'date -u +%Y%m%dT%H%M%SZ' and compare with above IDs."
  echo "If IDs were manually typed, regenerate them before the next commit."
  # Warning only -- does not block commit
fi

exit 0
