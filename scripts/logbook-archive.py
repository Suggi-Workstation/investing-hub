#!/usr/bin/env python3
"""Archive log entries from active .log files when they exceed MAX_LINES.

Triggered by .github/workflows/logbook-archive.yml on push to main.
Skips commits tagged with [archive] to prevent infinite loops.
Cuts at complete entry boundaries (## [ENT-NNN]) -- never splits an entry.
Keeps the header comment intact. Appends archived entries to
logbook/archive/<name>-<quarter>.log.
"""
import os
import sys
from datetime import datetime, timezone

MAX_LINES = 500
TARGET_LINES = 400  # Cut enough to leave headroom for normal operation
LOGBOOK_DIR = "logbook"
ARCHIVE_DIR = "logbook/archive"

def date_label():
    """Return current date label like '2026-07-22'."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")

def find_entry_boundaries(lines):
    """Return list of (start_idx, end_idx) tuples for each entry block.
    An entry starts at a line matching '## [ENT-' and runs until the
    next entry or EOF. The header is everything before the first entry.
    """
    entry_starts = []
    for i, line in enumerate(lines):
        if line.startswith("## [ENT-"):
            entry_starts.append(i)

    if not entry_starts:
        return 0, [], 0  # No entries at all -- header_only

    header_end = entry_starts[0]
    boundaries = []
    for j, start in enumerate(entry_starts):
        end = entry_starts[j + 1] if j + 1 < len(entry_starts) else len(lines)
        boundaries.append((start, end))

    return header_end, boundaries, entry_starts[0]

def process_log(log_path):
    """Archive oldest entries from log_path if it exceeds MAX_LINES."""
    with open(log_path, "r", encoding="ascii", errors="replace") as f:
        lines = f.readlines()

    total = len(lines)
    if total <= MAX_LINES:
        print(f"  {log_path}: {total} lines -- OK (limit {MAX_LINES})")
        return False

    header_end, boundaries, first_entry_idx = find_entry_boundaries(lines)
    header_lines = lines[:header_end]
    header_count = len(header_lines)

    if header_count >= MAX_LINES:
        print(f"  {log_path}: header alone is {header_count} lines -- skipping (abnormal)")
        return False

    # Keep entries from the BOTTOM until we stay under MAX_LINES.
    # Work backwards through boundaries.
    kept_boundaries = []
    kept_count = header_count
    for start, end in reversed(boundaries):
        entry_len = end - start
        if kept_count + entry_len <= TARGET_LINES:
            kept_boundaries.insert(0, (start, end))
            kept_count += entry_len
        else:
            break  # This entry would push us over -- archive everything from here up

    archive_boundaries = [b for b in boundaries if b not in kept_boundaries]

    if not archive_boundaries:
        print(f"  {log_path}: {total} lines but cannot trim (single giant entry?) -- skipping")
        return False

    # Build archive content
    archive_lines = []
    for start, end in archive_boundaries:
        archive_lines.extend(lines[start:end])

    # Build trimmed file: header + kept entries
    trimmed = list(header_lines)
    for start, end in kept_boundaries:
        trimmed.extend(lines[start:end])

    # Determine archive filename
    base = os.path.basename(log_path).replace(".log", "")
    archive_name = f"{base}-{date_label()}.log"
    archive_path = os.path.join(ARCHIVE_DIR, archive_name)

    # Create archive dir if needed
    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    # Write archive (append if exists, create if not)
    mode = "a" if os.path.exists(archive_path) else "w"
    with open(archive_path, mode, encoding="ascii") as f:
        if mode == "w":
            # Extract ENT IDs from first archived and first kept entries
            first_archived_line = lines[archive_boundaries[0][0]]
            last_archived_line = lines[archive_boundaries[-1][0]]
            first_ent = first_archived_line.strip().split("[ENT-")[1].split("]")[0] if "[ENT-" in first_archived_line else "???"
            last_ent = last_archived_line.strip().split("[ENT-")[1].split("]")[0] if "[ENT-" in last_archived_line else "???"
            first_kept_line = lines[kept_boundaries[0][0]] if kept_boundaries else ""
            ent_match = first_kept_line.strip().split("[ENT-")[1].split("]")[0] if kept_boundaries and "[ENT-" in first_kept_line else "???"
            f.write(f"<!-- {base}.log archive -- ENT-{first_ent} to ENT-{last_ent}\n")
            f.write(f"     Moved from active log on {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")
            f.write(f"     Active log continues from ENT-{ent_match} onward.\n")
            f.write(f"     See logbook/protocol.md for full spec.\n")
            f.write("-->\n\n")
        else:
            first_archived_line = lines[archive_boundaries[0][0]]
            last_archived_line = lines[archive_boundaries[-1][0]]
            first_ent = first_archived_line.strip().split("[ENT-")[1].split("]")[0] if "[ENT-" in first_archived_line else "???"
            last_ent = last_archived_line.strip().split("[ENT-")[1].split("]")[0] if "[ENT-" in last_archived_line else "???"
            f.write(f"\n<!-- Appended {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} -- ENT-{first_ent} to ENT-{last_ent} -->\n\n")
        f.writelines(archive_lines)

    # Write trimmed active file
    with open(log_path, "w", encoding="ascii") as f:
        f.writelines(trimmed)

    print(f"  {log_path}: {total} -> {len(trimmed)} lines "
          f"(archived {len(archive_lines)} lines to {archive_name})")
    return True

def main():
    changed = False
    log_files = sorted([
        f for f in os.listdir(LOGBOOK_DIR)
        if f.endswith(".log") and os.path.isfile(os.path.join(LOGBOOK_DIR, f))
    ])

    if not log_files:
        print("No .log files found in logbook/")
        return 0

    for log_file in log_files:
        log_path = os.path.join(LOGBOOK_DIR, log_file)
        if process_log(log_path):
            changed = True

    if not changed:
        print("All log files within limits.")
    return 0

if __name__ == "__main__":
    sys.exit(main())