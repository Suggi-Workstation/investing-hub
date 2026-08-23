# brain-index -- Shared Knowledge-Base Search for All Agents

Search the agentic-brain with hybrid semantic + keyword retrieval.
No servers, no API keys, no external services. Works on any machine
with Python 3.10+.

## Quick Start

```bash
# 1. Clone the brain
git clone https://github.com/Suggi-Workstation/agentic-brain.git /tmp/brain
cd /tmp/brain/brain-index

# 2. Install dependencies (once)
pip install -r requirements.txt

# 3. Build the index (once, ~2 min for 125 files)
python index.py --force

# 4. Query
python query.py "antitrust risk in digital platforms" --top-k 20
```

## How It Works

Hybrid search combining two retrieval methods:

- **Semantic (dense):** `unsloth/embeddinggemma-300m`
  (768-dim, public mirror of google/embeddinggemma-300m) converts
  text to vectors. Finds conceptually similar content even when
  keywords differ.
- **Keyword (sparse):** BM25 ranks by term frequency. Finds exact
  matches for specific terms and phrases.

Results are fused with Reciprocal Rank Fusion (RRF, k=60) and
deduplicated by file (one result per file, highest scoring chunk).

## Commands

```bash
# Build or refresh the index
python index.py              # Incremental (only changed files)
python index.py --force      # Full rebuild
python index.py --check      # Check freshness only

# Query the index
python query.py "your question"              # Hybrid (default)
python query.py "your question" --top-k 10   # Custom result count
python query.py "your question" --no-dense   # BM25 only
python query.py "your question" --no-sparse  # Vector only

# Check freshness
python query.py --check-freshness

# Run evaluation
python eval.py              # Summary only
python eval.py --verbose    # Per-query results
```

## Files

```
brain-index/
  index.py            Build the search index from markdown files
  query.py            Query the index, return ranked results
  eval.py             Run eval against gold queries (recall@20, MRR, nDCG)
  config.yaml         Embedding model, chunk size, RRF weights
  gold-queries.yaml   Test queries with expected file hits
  heartbeat.json      Freshness metadata (auto-generated)
  requirements.txt    Python deps (sentence-transformers, pyyaml, numpy)
  README.md           This file
```

Index data is stored in `~/.brain-index/` (NOT in the repo). Each
machine builds its own index from the shared brain source.

## Eval Gate

The eval gate prevents silent search quality regression:

```bash
python eval.py --verbose
```

Current baseline (2026-07-20): **Recall@20: 100%** (20/20 gold queries),
MRR: 0.74, nDCG@20: 0.81 on 125 brain files.

Gold queries grow with the brain. Add queries to `gold-queries.yaml`
as new domains and topics are added.

## Freshness

Every index build records the git HEAD SHA in `heartbeat.json`.
Run `python query.py --check-freshness` to verify the index matches
the current brain state. A stale index warns the operator.

## Scope

Indexes all markdown files with frontmatter in the agentic-brain repo.
Excluded: `logbook/`, `scripts/`, `.github/`, `.git/`, and non-markdown
files (JSON, YAML, images, etc.).

## Dependencies

- Python 3.10+
- sentence-transformers (for unsloth/embeddinggemma-300m
  embeddings) + BAAI/bge-reranker-v2-m3 (cross-encoder rerank,
  in-process, public)
- pyyaml (config and gold query parsing)
- numpy (vector operations)

All dependencies are pure Python. No GPU required. No external APIs.

## Reference

See `research/insights/brain-search-system.md` for the full
finished-system blueprint with architecture diagrams.
