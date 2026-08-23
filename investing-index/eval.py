#!/usr/bin/env python3
"""
Evaluate brain-index search quality against gold queries.

Metrics: recall@20, MRR (Mean Reciprocal Rank), nDCG@20.

Usage:
    python eval.py              # run eval
    python eval.py --verbose    # show per-query results
"""

import json
import math
import os
import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent

# --- Import query functions from query.py ---
sys.path.insert(0, str(SCRIPT_DIR))
from query import load_index, load_embedder, dense_search, sparse_search, rrf_fusion, rerank


def load_gold_queries():
    """Load gold queries from gold-queries.yaml."""
    path = SCRIPT_DIR / "gold-queries.yaml"
    with open(path) as f:
        data = yaml.safe_load(f)
    return data["queries"]


def recall_at_k(gold_file: str, results: list, k: int = 20) -> bool:
    """Check if gold_file appears in top-k results."""
    for r in results[:k]:
        if r["file"] == gold_file:
            return True
    return False


def reciprocal_rank(gold_file: str, results: list) -> float:
    """1 / rank of first gold hit, or 0 if not found."""
    for i, r in enumerate(results):
        if r["file"] == gold_file:
            return 1.0 / (i + 1)
    return 0.0


def ndcg_at_k(gold_file: str, results: list, k: int = 20) -> float:
    """Normalized DCG: 1 if gold at rank 1, decaying with rank."""
    for i, r in enumerate(results[:k]):
        if r["file"] == gold_file:
            # DCG = 1 / log2(rank+2), IDCG = 1, so nDCG = DCG
            return 1.0 / math.log2(i + 2)
    return 0.0


def run_eval(verbose: bool = False):
    """Run full eval against all gold queries."""
    queries = load_gold_queries()
    if not queries:
        print("No gold queries found. Add queries to gold-queries.yaml first.")
        sys.exit(1)

    chunks, vectors = load_index()
    # dense_search embeds via the warm daemon when available; the in-process
    # model is only needed as fallback, so we DON'T preload it here (saves
    # the ~11s cold load when the daemon is up).
    model = None

    recall_hits = 0
    mrr_sum = 0.0
    ndcg_sum = 0.0
    results_detail = []

    for i, q in enumerate(queries):
        try:
            dense = dense_search(q["question"], model, chunks, vectors, top_k=20)
        except Exception:
            dense = []
        try:
            sparse = sparse_search(q["question"], chunks, top_k=20)
        except Exception:
            sparse = []

        if dense and sparse:
            results = rrf_fusion(dense, sparse, k=60, top_k=20)
        elif dense:
            results = dense[:20]
        else:
            results = sparse[:20]

        # Stage 2: cross-encoder rerank (same path agents get in query.py)
        results = rerank(q["question"], results, top_k=20)

        hit = recall_at_k(q["gold_file"], results, 20)
        rr = reciprocal_rank(q["gold_file"], results)
        ndcg = ndcg_at_k(q["gold_file"], results, 20)

        recall_hits += 1 if hit else 0
        mrr_sum += rr
        ndcg_sum += ndcg

        rank_found = "NOT FOUND"
        if hit:
            for j, r in enumerate(results):
                if r["file"] == q["gold_file"]:
                    rank_found = f"rank {j + 1}"
                    break

        results_detail.append({
            "qid": q["qid"],
            "question": q["question"],
            "gold_file": q["gold_file"],
            "hit": hit,
            "rank": rank_found,
            "rr": round(rr, 4),
            "ndcg": round(ndcg, 4),
        })

        if verbose:
            status = "PASS" if hit else "MISS"
            print(f"{status} {q['qid']}: {rank_found} | "
                  f"RR={rr:.4f} nDCG={ndcg:.4f}")
            print(f"  Q: {q['question'][:80]}...")
            if hit:
                print(f"  -> {q['gold_file']}")
            print()

    n = len(queries)
    recall = recall_hits / n
    mrr = mrr_sum / n
    ndcg = ndcg_sum / n

    print(f"---")
    print(f"Queries: {n}")
    print(f"Recall@20: {recall_hits}/{n} = {recall:.1%}")
    print(f"MRR:       {mrr:.4f}")
    print(f"nDCG@20:   {ndcg:.4f}")
    print(f"PASS" if recall >= 0.80 else "WARN: recall below 80%")

    # Write detailed results
    out_path = SCRIPT_DIR / "eval-results.json"
    summary = {
        "queries": n,
        "recall_at_20": round(recall, 4),
        "mrr": round(mrr, 4),
        "ndcg_at_20": round(ndcg, 4),
        "results": results_detail,
    }
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nDetailed results: {out_path}")

    return recall


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", "-v", action="store_true",
                    help="Show per-query results")
    args = ap.parse_args()

    recall = run_eval(verbose=args.verbose)
    sys.exit(0 if recall >= 0.80 else 1)
