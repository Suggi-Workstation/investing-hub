#!/usr/bin/env python3
"""Evaluate investing-index retrieval against curated gold queries."""

import json
import math
import re
import sys
from pathlib import Path, PurePosixPath

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
EVAL_K = 20

sys.path.insert(0, str(SCRIPT_DIR))
from query import (cfg, deduplicate_files, dense_search, load_index, rerank,
                   rrf_fusion, sparse_search)


def load_gold_queries():
    """Load gold queries from gold-queries.yaml."""
    with open(SCRIPT_DIR / "gold-queries.yaml") as handle:
        data = yaml.safe_load(handle) or {}
    return data.get("queries", [])


def gold_files(query: dict) -> list[str]:
    """Return a query's relevance set, accepting the legacy singular key."""
    if "gold_files" in query:
        files = query["gold_files"]
    elif "gold_file" in query:
        files = [query["gold_file"]]
    else:
        raise ValueError("missing gold_files")
    if not isinstance(files, list) or not files:
        raise ValueError("gold_files must be a non-empty list")
    if any(not isinstance(path, str) or not path.strip() for path in files):
        raise ValueError("gold_files entries must be non-empty strings")
    return files


def validate_gold_queries(queries: list, indexed_files: set[str] | None = None) -> list:
    """Validate schema, path confinement, existence, and index membership."""
    if not queries:
        raise ValueError("no gold queries found")

    errors = []
    seen_ids = set()
    seen_questions = set()
    normalized = []
    root = REPO_ROOT.resolve()

    for position, query in enumerate(queries, start=1):
        if not isinstance(query, dict):
            errors.append(f"entry {position}: expected a mapping")
            continue

        qid = query.get("qid")
        question = query.get("question")
        domain = query.get("domain")
        if not isinstance(qid, str) or not re.fullmatch(r"[a-z][a-z0-9-]*", qid):
            errors.append(f"entry {position}: invalid qid")
        elif qid in seen_ids:
            errors.append(f"{qid}: duplicate qid")
        else:
            seen_ids.add(qid)

        if not isinstance(question, str) or not question.strip():
            errors.append(f"{qid or position}: question is required")
        elif question in seen_questions:
            errors.append(f"{qid}: duplicate question")
        else:
            seen_questions.add(question)

        if not isinstance(domain, str) or not domain.strip():
            errors.append(f"{qid or position}: domain is required")

        try:
            files = gold_files(query)
        except ValueError as exc:
            errors.append(f"{qid or position}: {exc}")
            continue

        if len(files) != len(set(files)):
            errors.append(f"{qid or position}: duplicate gold file")

        for relative in files:
            pure = PurePosixPath(relative)
            if ("\x00" in relative or "\\" in relative or pure.is_absolute()
                    or ".." in pure.parts or str(pure) != relative):
                errors.append(f"{qid or position}: unsafe path {relative!r}")
                continue
            target = (REPO_ROOT / relative).resolve()
            try:
                target.relative_to(root)
            except ValueError:
                errors.append(f"{qid or position}: path escapes repository: {relative}")
                continue
            if not target.is_file():
                errors.append(f"{qid or position}: missing gold file: {relative}")
            elif target.stat().st_size == 0:
                errors.append(f"{qid or position}: empty gold file: {relative}")
            elif indexed_files is not None and relative not in indexed_files:
                errors.append(f"{qid or position}: gold file is not indexed: {relative}")

        item = dict(query)
        item.pop("gold_file", None)
        item["gold_files"] = files
        normalized.append(item)

    if errors:
        raise ValueError("Invalid gold queries:\n- " + "\n- ".join(errors))
    return normalized


def _relevant(gold: str | list[str]) -> set[str]:
    return {gold} if isinstance(gold, str) else set(gold)


def recall_at_k(gold: str | list[str], results: list, k: int = EVAL_K) -> float:
    """Return the fraction of relevant files found in the top-k results."""
    relevant = _relevant(gold)
    unique = deduplicate_files(results, top_k=k)
    found = {result["file"] for result in unique} & relevant
    return len(found) / len(relevant)


def reciprocal_rank(gold: str | list[str], results: list) -> float:
    """Return reciprocal rank of the first relevant result."""
    relevant = _relevant(gold)
    for rank, result in enumerate(deduplicate_files(results, len(results)), start=1):
        if result["file"] in relevant:
            return 1.0 / rank
    return 0.0


def ndcg_at_k(gold: str | list[str], results: list, k: int = EVAL_K) -> float:
    """Return binary-relevance nDCG at k for one or more relevant files."""
    relevant = _relevant(gold)
    unique = deduplicate_files(results, top_k=k)
    dcg = sum(
        1.0 / math.log2(rank + 1)
        for rank, result in enumerate(unique, start=1)
        if result["file"] in relevant
    )
    ideal_count = min(len(relevant), k)
    idcg = sum(1.0 / math.log2(rank + 1) for rank in range(1, ideal_count + 1))
    return dcg / idcg if idcg else 0.0


def prepare_eval():
    """Load the index and fail closed on an invalid gold set."""
    chunks, vectors = load_index()
    indexed_files = {chunk["file"] for chunk in chunks}
    queries = validate_gold_queries(load_gold_queries(), indexed_files)
    return queries, chunks, vectors


def fuse_hybrid(dense: list, sparse: list) -> list:
    """Require both retrieval branches before scoring the hybrid pipeline."""
    if not dense:
        raise ValueError("dense retrieval returned no candidates")
    if not sparse:
        raise ValueError("BM25 retrieval returned no candidates")
    return rrf_fusion(dense, sparse, k=cfg["rrf"]["k"], top_k=EVAL_K)


def run_eval(verbose: bool = False):
    """Run the production retrieval path against all gold queries."""
    queries, chunks, vectors = prepare_eval()
    recall_sum = 0.0
    mrr_sum = 0.0
    ndcg_sum = 0.0
    complete = 0
    details = []

    for query in queries:
        dense = dense_search(query["question"], None, chunks, vectors, top_k=EVAL_K)
        sparse = sparse_search(query["question"], chunks, top_k=EVAL_K)
        results = fuse_hybrid(dense, sparse)
        results = deduplicate_files(results, top_k=EVAL_K)
        results = rerank(query["question"], results, top_k=EVAL_K)

        relevant = query["gold_files"]
        recall = recall_at_k(relevant, results)
        rr = reciprocal_rank(relevant, results)
        ndcg = ndcg_at_k(relevant, results)
        found = [result["file"] for result in deduplicate_files(results, EVAL_K)
                 if result["file"] in set(relevant)]
        complete += int(recall == 1.0)
        recall_sum += recall
        mrr_sum += rr
        ndcg_sum += ndcg
        details.append({
            "qid": query["qid"],
            "question": query["question"],
            "gold_files": relevant,
            "found": found,
            "recall": round(recall, 4),
            "rr": round(rr, 4),
            "ndcg": round(ndcg, 4),
        })

        if verbose:
            status = "PASS" if recall == 1.0 else "PARTIAL" if recall else "MISS"
            print(f"{status} {query['qid']}: recall={recall:.2f} "
                  f"RR={rr:.4f} nDCG={ndcg:.4f}")
            print(f"  Q: {query['question'][:80]}...")
            for path in found:
                print(f"  -> {path}")
            print()

    count = len(queries)
    recall = recall_sum / count
    mrr = mrr_sum / count
    ndcg = ndcg_sum / count
    print("---")
    print(f"Queries: {count}")
    print(f"Complete@{EVAL_K}: {complete}/{count}")
    print(f"Recall@{EVAL_K}: {recall:.1%}")
    print(f"MRR:       {mrr:.4f}")
    print(f"nDCG@{EVAL_K}:   {ndcg:.4f}")
    print("PASS" if recall >= 0.80 else "FAIL: recall below 80%")

    output = {
        "queries": count,
        "complete_at_20": complete,
        "recall_at_20": round(recall, 4),
        "mrr": round(mrr, 4),
        "ndcg_at_20": round(ndcg, 4),
        "results": details,
    }
    out_path = SCRIPT_DIR / "eval-results.json"
    with open(out_path, "w") as handle:
        json.dump(output, handle, indent=2)
    print(f"\nDetailed results: {out_path}")
    return recall


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    try:
        if args.validate_only:
            queries, _, _ = prepare_eval()
            print(f"GOLD SET PASS: {len(queries)} valid queries")
            sys.exit(0)
        score = run_eval(verbose=args.verbose)
    except (OSError, ValueError, KeyError) as exc:
        print(f"GOLD SET FAIL: {exc}")
        sys.exit(1)
    sys.exit(0 if score >= 0.80 else 1)