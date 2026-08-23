#!/usr/bin/env python3
"""Sanitize non-ASCII characters in text files to pure 7-bit ASCII.

Enforces the workspace ASCII-only rule (ascii-guard CI + pre-commit hook).
Maps common typographic characters to ASCII equivalents:

  em/en dash (U+2014/U+2013)  ->  -- / -
  curly quotes (U+2018-201D)  ->  ' "
  arrows (U+2190-2194)        ->  <-  ->  <->  v
  middle dot (U+00B7)         ->  -
  box drawing (U+2500-257F)   ->  - | + (diagram structure preserved)
  star emoji (U+2B50)         ->  [star]
  check emoji (U+2705)        ->  [OK]
  any other non-ASCII         ->  removed (or '?' if nothing maps)

Usage:
  python3 scripts/sanitize-ascii.py [FILE ...]
  python3 scripts/sanitize-ascii.py            # scan all tracked files

Exit code 0 = all files clean (nothing to fix, or all fixed).
Exit code 1 = a file could not be sanitized (binary/unreadable).
"""

import os
import subprocess
import sys

# Explicit character map: unicode codepoint -> ASCII replacement
CHAR_MAP = {
    0x2014: "--",   # em dash
    0x2013: "-",    # en dash
    0x2018: "'",    # left single quote
    0x2019: "'",    # right single quote
    0x201C: '"',    # left double quote
    0x201D: '"',    # right double quote
    0x2190: "<-",   # left arrow
    0x2192: "->",   # right arrow
    0x2194: "<->",  # left-right arrow
    0x2193: "v",    # down arrow
    0x00B7: "-",    # middle dot
    0x2500: "-",    # box horizontal
    0x2502: "|",    # box vertical
    0x250C: "+",    # box top-left
    0x2510: "+",    # box top-right
    0x2514: "+",    # box bottom-left
    0x2518: "+",    # box bottom-right
    0x251C: "+",    # box left tee
    0x2524: "+",    # box right tee
    0x252C: "+",    # box top tee
    0x2534: "+",    # box bottom tee
    0x253C: "+",    # box cross
    0x2B50: "[star]",  # star emoji
    0x2705: "[OK]",    # check emoji
}

def sanitize_text(text):
    """Replace non-ASCII chars per CHAR_MAP; strip unmapped ones."""
    out = []
    for ch in text:
        cp = ord(ch)
        if cp < 0x80:
            out.append(ch)
        elif cp in CHAR_MAP:
            out.append(CHAR_MAP[cp])
        else:
            # Unmapped non-ASCII: drop it (markdown safety)
            continue
    return "".join(out)

def get_tracked_files():
    """Return all git-tracked text files in the workspace."""
    r = subprocess.run(
        ["git", "ls-files", "-z"],
        capture_output=True, text=True, check=True,
    )
    return [f for f in r.stdout.split("\0") if f]

def is_binary(path):
    """Heuristic: contains NUL byte in first 8KB."""
    try:
        with open(path, "rb") as fh:
            return b"\0" in fh.read(8192)
    except OSError:
        return True

def main(argv):
    if argv:
        files = [f for f in argv if os.path.isfile(f)]
    else:
        files = get_tracked_files()

    changed = []
    errors = []

    for path in files:
        if is_binary(path):
            continue
        try:
            with open(path, "r", encoding="utf-8") as fh:
                text = fh.read()
        except (UnicodeDecodeError, OSError) as e:
            errors.append(f"{path}: {e}")
            continue

        cleaned = sanitize_text(text)
        if cleaned != text:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(cleaned)
            changed.append(path)

    if changed:
        print("Sanitized (non-ASCII -> ASCII):")
        for p in changed:
            print(f"  {p}")
    else:
        print("All files clean: no non-ASCII characters found.")

    if errors:
        print("ERRORS (could not sanitize):")
        for e in errors:
            print(f"  {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
