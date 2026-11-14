# investing-index -- Search investing-hub

Hybrid file retrieval over the `investing-hub` repository. It combines
semantic search (embedding model in `config.yaml`) with BM25 keyword search,
merges both rankings with Reciprocal Rank Fusion (RRF), and returns one best
chunk per file.

Gold questions measure the search results. They never influence live ranking.

## VPS Commands

Run from `/srv/investing/investing-hub`:

```bash
/opt/repo-tools/venv/bin/python investing-index/query.py --check-freshness
/opt/repo-tools/venv/bin/python investing-index/query.py "<question>" --top-k 20
/opt/repo-tools/venv/bin/python investing-index/index.py --check
/opt/repo-tools/venv/bin/python investing-index/eval.py --validate-only
/opt/repo-tools/venv/bin/python investing-index/eval.py --verbose
/opt/repo-tools/venv/bin/python investing-index/eval.py --baseline <earlier eval-results.json>
/opt/repo-tools/venv/bin/python investing-index/self-test.py
```

The watcher owns index builds on the VPS. Do not run `index.py --force` unless
recovering a diagnosed corrupt index or changing the embedding model.

## Files

- `index.py`: incremental/full index builder and freshness check.
- `query.py`: dense + BM25 + RRF retrieval. BM25 matches lowercase words;
  punctuation and Markdown marks separate words.
- `eval.py`: relevance-set validation; Top-1/3/5, Recall, MRR and nDCG;
  question-by-question comparison with an earlier run.
- `gold-queries.yaml`: curated questions and relevant repository files.
- `self-test.py`: package contract and regression tests.
- `config.yaml`: model, chunking, fusion, and data-path settings.

## Data and Evaluation

Index data lives in `~/.investing-index` (`/srv/investing/index` on the VPS),
outside git. Gold entries use `gold_files` because one question can have more
than one relevant file. Every target must exist, be nonempty, and appear in
the index.

Refresh relevance judgments when the corpus grows materially.

Agents open the top 3-5 files, so Top-1/3/5 and MRR decide a search change;
Recall@20 only guards against losing files. To test a change, keep the
`eval-results.json` of the old state and run `eval.py --baseline <that file>`
on the same gold set. It prints the MRR difference with its 95% interval:
`clear gain` and `clear loss` are real; `no clear difference` means this gold
set cannot tell the two states apart.