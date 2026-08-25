---
name: investing-logbook-protocol
id: 20260825T191500Z
tier: protocol
author: Morpheus
approved_by: Suggi
links:
  - governance/system-constitution.md
  - logbook/protocol.md
---
# Investing Logbook Protocol -- Investing Event Log Spec

## What the Logbook Is

The investing logbook is an append-only event log for investing
activity in the investing-hub repo. It is the investing-hub analogue
of the agentic-brain logbook, scoped to investing work.

Entries are appended at the bottom, never edited or deleted. Agents
catch up by reading entries since their last-seen timestamp.

| Log file | Purpose |
|:--|:--|
| `investing.log` | Investing activity: company deep-dives, DCF models, portfolio analysis, screening results |
| `errors.log` | Bugs, scars, fixes, gate additions |

## Directory Structure

```
logbook/
  protocol.md          # this file -- the spec
  investing.log        # investing activity log (append-only)
  errors.log           # error/bug/scar log (append-only)
  archive/             # logs archived by CI when >500 lines
```

## Entry Format

Each entry is a single block appended to the bottom of the file. No
editing, no deletion. Most recent entries are at the bottom.

```
## [ENT-001] | 2026-08-25 19:15 UTC | Morpheus | investing | ref: companies/coca-cola.md | see: 20260825T191500Z
Completed DCF + EPV model for Coca-Cola. Intrinsic range $52-58.
DCF assumptions: 8% WACC, 3% terminal growth. EPV: no-growth value
$55. Margin of safety tight at current $63.
```

Entry bodies MUST use multiple short lines. Do NOT pack an entire
session summary onto one line. Break at logical boundaries: one
major point or workstream per line.

## Entry Schema

| Field | Required | Description |
|:--|:--|:--|
| `ENT-ID` | Yes | Sequential per-file (ENT-001, ENT-002...). Never reused. Derived from last entry in file + 1. |
| Timestamp | Yes | ISO 8601 date + HH:MM UTC. Append-only = always increasing. |
| Agent | Yes | Which agent wrote this (Morpheus, Neo, Investment-Runner, etc.) |
| Category | Yes | `investing` or `error` |
| ref: | Optional | Path to file this entry relates to (ref: `companies/coca-cola.md`). |
| see: | Optional | Cross-reference to another entry or artifact ID. |
| Body | Yes | What was done, what file was written/changed. Multiline. |

## Categories

| Category | Use for | File |
|:--|:--|:--|
| `investing` | Company deep-dives, DCF models, portfolio analysis, screening | investing.log |
| `error` | Bugs found, scars earned, gates added | errors.log |

## How to Write

1. Read the tail of the target log file to get the last ENT-ID counter.
2. Append a new entry at the bottom, incrementing the counter.
3. Commit and push. No waiting.

## How to Read (Catch-Up)

1. At session start, check log files for new entries since last-seen.
2. Read entries since last-seen timestamp.
3. Update last-seen to current UTC time.
4. No reply needed unless an entry contains an @mention.

## Archiving

When a .log file exceeds 500 lines, CI automatically archives the
oldest entries to keep reads fast and context lean.

The `logbook-archive.yml` workflow (`.github/workflows/`) fires on
every push to main. It:

1. Checks all `logbook/*.log` files for line count > 500.
2. Cuts the oldest complete entries (never mid-entry) from the active file.
3. Appends them to `logbook/archive/<name>-<YYYY-MM-DD>.log`.
4. Commits with `[archive]` tag so the workflow does not re-trigger.
5. The ENT-ID counter continues uninterrupted -- archived entries keep
   their original ENT-IDs for cross-reference integrity.

Agents do NOT need to archive manually. Push log entries as normal;
CI trims them when they exceed the threshold.

## Compliance

- **ASCII-only:** all .log entries and this protocol file are plain
  7-bit ASCII. CI enforces.
- **No self-modification:** this protocol file is authored by agents
  and approved by Suggi. Changes require a proposal.
- **No force-push:** append-only design precludes history rewriting.