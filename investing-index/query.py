#!/usr/bin/env python3
"""
Query the investing-index. Returns ranked file paths with snippets.

Usage:
    python query.py "your question" --top-k 20
    python query.py "your question" --no-dense      # BM25 only
    python query.py "your question" --no-sparse     # vector only
    python query.py --check-freshness               # verify index is current
"""

import json
import hashlib
import math
import os
import sys
from datetime import datetime
from pathlib import Path
from collections import Counter

import yaml
import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

with open(SCRIPT_DIR / "config.yaml") as f:
    cfg = yaml.safe_load(f)

DATA_DIR = Path(os.path.expanduser(cfg["index"]["data_dir"]))
CHUNKS_PATH = DATA_DIR / "chunks.jsonl"
VECTORS_PATH = DATA_DIR / "vectors.npy"
META_PATH = DATA_DIR / "meta.json"
MANIFEST_PATH = DATA_DIR / "manifest.json"


def load_index():
    """Load chunks and vectors from disk."""
    if not CHUNKS_PATH.exists() or not VECTORS_PATH.exists():
        sys.exit("ERROR: No index found. Run 'python index.py --force' first.")

    chunks = []
    with open(CHUNKS_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                chunks.append(json.loads(line))

    vectors = np.load(str(VECTORS_PATH)).astype(np.float32)
    return chunks, vectors


def check_corpus_manifest(root: Path, manifest_path: Path,
                          exclude_dirs: set) -> tuple[bool, str]:
    """Compare all live indexable Markdown hashes with the saved manifest."""
    if not manifest_path.is_file():
        return False, "index manifest missing"
    with open(manifest_path) as f:
        manifest = json.load(f)

    current = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name not in exclude_dirs]
        for filename in sorted(filenames):
            if filename.startswith(".") or Path(filename).suffix.lower() != ".md":
                continue
            path = Path(dirpath) / filename
            relative = path.relative_to(root).as_posix()
            current[relative] = hashlib.md5(path.read_bytes()).hexdigest()

    expected = {
        relative: details.get("hash") if isinstance(details, dict) else None
        for relative, details in manifest.items()
    }
    new = set(current) - set(expected)
    deleted = set(expected) - set(current)
    changed = {path for path in current.keys() & expected.keys()
               if current[path] != expected[path]}
    if new or changed or deleted:
        return False, ("live corpus differs from manifest "
                       f"(new={len(new)}, changed={len(changed)}, "
                       f"deleted={len(deleted)})")
    return True, "live corpus matches manifest"


def load_embedder():
    """Lazy-load the embedding model (in-process fallback)."""
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(cfg["embedding"]["model"],
                                device=cfg["embedding"]["device"])
    return model


# --- Warm daemon integration ---
# The brain-embed daemon keeps the embedding model loaded (127.0.0.1:8099),
# so queries skip the ~11s cold model load. If the daemon is down, we fall
# back to in-process loading (same behavior as before). Indexing (index.py)
# uses the daemon too, with its own in-process fallback.
_EMBED_DAEMON_URL = "http://127.0.0.1:8099/embed"
_DAEMON_DEAD = False


def _daemon_embed(texts, is_query):
    """Try the warm daemon; returns list of vectors or None on failure."""
    global _DAEMON_DEAD
    if _DAEMON_DEAD:
        return None
    try:
        import urllib.request

        payload = json.dumps({"texts": texts, "query": is_query}).encode("utf-8")
        req = urllib.request.Request(
            _EMBED_DAEMON_URL, data=payload,
            headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data["embeddings"]
    except Exception:
        # Daemon unreachable once -> don't hammer it every query
        _DAEMON_DEAD = True
        return None


def embed_query(query: str):
    """Embed a query via the warm daemon, falling back to in-process."""
    vecs = _daemon_embed([query], is_query=True)
    if vecs is not None:
        import numpy as _np
        v = _np.array(vecs[0], dtype=_np.float32)
        n = _np.linalg.norm(v)
        return v / n if n > 0 else v
    model = load_embedder()
    return model.encode_query(query, normalize_embeddings=True)


def dense_search(query: str, model, chunks: list, vectors: np.ndarray,
                 top_k: int) -> list:
    """Semantic (vector) search."""
    q_vec = embed_query(query)
    scores = np.dot(vectors, q_vec)
    top_idx = np.argsort(scores)[-top_k:][::-1]
    results = []
    for idx in top_idx:
        if scores[idx] > 0:
            results.append({
                "file": chunks[idx]["file"],
                "chunk_id": chunks[idx]["chunk_id"],
                "score": float(scores[idx]),
                "snippet": chunks[idx]["text"][:cfg["search"]["snippet_chars"]],
                "title": chunks[idx].get("title", ""),
                "domain": chunks[idx].get("domain", ""),
                "tags": chunks[idx].get("tags", []),
            })
    return results


# --- Inline BM25 implementation (no external deps) ---

def tokenize(text: str) -> list:
    """Simple whitespace tokenizer, lowercase."""
    return text.lower().split()


class BM25:
    """Minimal BM25 implementation. k1=1.5, b=0.75 default."""

    def __init__(self, corpus: list, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.n = len(corpus)
        self.doc_len = [len(doc) for doc in corpus]
        self.avgdl = sum(self.doc_len) / max(self.n, 1)
        self.df = Counter()
        self.tf = []
        for doc in corpus:
            counts = Counter(doc)
            self.tf.append(counts)
            for term in counts:
                self.df[term] += 1

    def _idf(self, term: str) -> float:
        df = self.df.get(term, 0)
        if df == 0:
            return 0.0
        return math.log((self.n - df + 0.5) / (df + 0.5) + 1.0)

    def score(self, query_tokens: list) -> np.ndarray:
        scores = np.zeros(self.n)
        for term in query_tokens:
            idf = self._idf(term)
            if idf == 0:
                continue
            for i in range(self.n):
                tf = self.tf[i].get(term, 0)
                if tf == 0:
                    continue
                doc_len_norm = 1.0 - self.b + self.b * (self.doc_len[i] / self.avgdl)
                scores[i] += idf * (tf * (self.k1 + 1)) / (tf + self.k1 * doc_len_norm)
        return scores


def sparse_search(query: str, chunks: list, top_k: int) -> list:
    """BM25 keyword search using inline implementation."""
    corpus = [tokenize(c["text"]) for c in chunks]
    bm25 = BM25(corpus, k1=cfg["bm25"]["k1"], b=cfg["bm25"]["b"])
    tokenized = tokenize(query)
    scores = bm25.score(tokenized)

    # Normalize to [0,1] for display
    if scores.max() > 0:
        scores = scores / scores.max()

    top_idx = np.argsort(scores)[-top_k:][::-1]
    results = []
    for idx in top_idx:
        if scores[idx] > 0:
            results.append({
                "file": chunks[idx]["file"],
                "chunk_id": chunks[idx]["chunk_id"],
                "score": float(scores[idx]),
                "snippet": chunks[idx]["text"][:cfg["search"]["snippet_chars"]],
                "title": chunks[idx].get("title", ""),
                "domain": chunks[idx].get("domain", ""),
                "tags": chunks[idx].get("tags", []),
            })
    return results


def deduplicate_files(results: list, top_k: int = 20) -> list:
    """Preserve rank order while returning at most one chunk per file."""
    unique = []
    seen = set()
    for result in results:
        path = result["file"]
        if path in seen:
            continue
        seen.add(path)
        unique.append(result)
        if len(unique) == top_k:
            break
    return unique


def rrf_fusion(dense_results: list, sparse_results: list,
               k: int = 60, top_k: int = 20) -> list:
    """Reciprocal Rank Fusion -- combine dense + sparse results."""
    scores = {}
    info = {}

    for rank, r in enumerate(dense_results):
        cid = r["chunk_id"]
        scores[cid] = scores.get(cid, 0) + 1.0 / (k + rank + 1)
        info[cid] = r

    for rank, r in enumerate(sparse_results):
        cid = r["chunk_id"]
        scores[cid] = scores.get(cid, 0) + 1.0 / (k + rank + 1)
        info[cid] = r

    ranked = []
    for cid in sorted(scores, key=lambda x: scores[x], reverse=True):
        result = dict(info[cid])
        result["rrf_score"] = round(scores[cid], 4)
        ranked.append(result)
    return deduplicate_files(ranked, top_k=top_k)



# Module-level cache: the cross-encoder loads ONCE per process, not per
# query. Loading a 278M/1.1GB model per call made eval (100 queries) take
# 13+ minutes; with the cache the model loads once and every query reuses it.
_RERANKER_CACHE = {}


def _get_reranker(rc: dict):
    """Load the cross-encoder once per process; return cached instance."""
    key = (rc["model"], rc.get("max_length", 512))
    if key not in _RERANKER_CACHE:
        from sentence_transformers import CrossEncoder

        _RERANKER_CACHE[key] = CrossEncoder(
            rc["model"], max_length=rc.get("max_length", 512)
        )
    return _RERANKER_CACHE[key]


def rerank(query: str, results: list, top_k: int = 20) -> list:
    """Cross-encoder rerank of fused candidates (stage 2, in-process)."""
    if not results or not cfg.get("reranker", {}).get("enabled", False):
        return results
    try:
        from sentence_transformers import CrossEncoder
    except Exception:
        print("reranker disabled: sentence-transformers unavailable")
        return results

    rc = cfg["reranker"]
    model = _get_reranker(rc)
    pairs = [(query, r["snippet"]) for r in results]
    scores = model.predict(pairs, batch_size=rc.get("batch_size", 16),
                           show_progress_bar=False)
    for r, s in zip(results, scores):
        r["rerank_score"] = float(s)
    reranked = sorted(results, key=lambda x: x["rerank_score"], reverse=True)
    return reranked[:top_k]

def _nonnegative_int(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _valid_timestamp(value) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _valid_git_sha(value) -> bool:
    return (isinstance(value, str) and len(value) == 40
            and all(char in "0123456789abcdef" for char in value.lower()))


def metadata_matches_config(meta: dict, config: dict) -> bool:
    """Return whether stored build-sensitive metadata matches config."""
    try:
        model_matches = meta["model"] == config["embedding"]["model"]
        dim_matches = meta["dim"] == config["embedding"]["dim"]
    except (KeyError, TypeError):
        return False
    if not model_matches or not dim_matches:
        return False
    return meta.get("chunking") == config.get("chunking", {})


def validate_index_state(root: Path, data_dir: Path, config: dict,
                         check_head: bool = True,
                         check_corpus: bool = True) -> tuple[bool, str]:
    """Validate artifacts, schemas, build config, corpus, and optional HEAD."""
    import subprocess

    heartbeat_path = data_dir / "heartbeat.json"
    chunks_path = data_dir / "chunks.jsonl"
    vectors_path = data_dir / "vectors.npy"
    meta_path = data_dir / "meta.json"
    manifest_path = data_dir / "manifest.json"
    if not heartbeat_path.is_file():
        return False, "NO INDEX -- run 'python index.py --force' first"

    required_paths = (chunks_path, vectors_path, meta_path, manifest_path)
    missing_data = [path.name for path in required_paths if not path.is_file()]
    if missing_data:
        return False, "STALE -- index data missing: " + ", ".join(missing_data)

    try:
        with open(heartbeat_path) as f:
            heartbeat = json.load(f)
        with open(meta_path) as f:
            meta = json.load(f)
        with open(manifest_path) as f:
            manifest = json.load(f)
    except (OSError, ValueError) as exc:
        return False, f"UNVERIFIED -- unreadable index metadata: {exc}"
    if not isinstance(heartbeat, dict) or not isinstance(meta, dict):
        return False, "UNVERIFIED -- index metadata must be JSON objects"
    if not isinstance(manifest, dict):
        return False, "UNVERIFIED -- index manifest must be a JSON object"

    heartbeat_fields = {
        "schema_version", "last_run_utc", "status", "built_at_head",
        "count", "files", "model",
    }
    missing = sorted(heartbeat_fields - heartbeat.keys())
    if missing:
        return False, "UNVERIFIED -- heartbeat missing: " + ", ".join(missing)
    heartbeat_types_ok = (
        _nonnegative_int(heartbeat["schema_version"])
        and heartbeat["schema_version"] == 1
        and heartbeat["status"] == "ok"
        and _valid_timestamp(heartbeat["last_run_utc"])
        and _valid_git_sha(heartbeat["built_at_head"])
        and _nonnegative_int(heartbeat["count"])
        and _nonnegative_int(heartbeat["files"])
        and isinstance(heartbeat["model"], str)
        and bool(heartbeat["model"])
    )
    if not heartbeat_types_ok:
        return False, "UNVERIFIED -- heartbeat schema, status, or types invalid"

    meta_fields = {
        "format_version", "model", "dim", "count", "files", "built_at",
        "mode", "chunking",
    }
    missing = sorted(meta_fields - meta.keys())
    if missing:
        return False, "UNVERIFIED -- index metadata missing: " + ", ".join(missing)
    meta_types_ok = (
        _nonnegative_int(meta["format_version"])
        and meta["format_version"] == 1
        and isinstance(meta["model"], str) and bool(meta["model"])
        and _nonnegative_int(meta["dim"]) and meta["dim"] > 0
        and _nonnegative_int(meta["count"])
        and _nonnegative_int(meta["files"])
        and _valid_timestamp(meta["built_at"])
        and meta["mode"] in {"full", "incremental"}
        and isinstance(meta["chunking"], dict)
    )
    if not meta_types_ok:
        return False, "UNVERIFIED -- index metadata schema or types invalid"
    if not metadata_matches_config(meta, config):
        return False, "STALE -- index metadata and build config disagree"
    if heartbeat["model"] != meta["model"]:
        return False, "STALE -- heartbeat and index model disagree"
    if (heartbeat["count"] != meta["count"]
            or heartbeat["files"] != meta["files"]):
        return False, "STALE -- heartbeat and index metadata disagree"
    if len(manifest) != meta["files"]:
        return False, "STALE -- manifest and index file count disagree"

    try:
        chunk_count = 0
        chunk_files = set()
        with open(chunks_path, encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                chunk = json.loads(line)
                chunk_count += 1
                chunk_files.add(chunk["file"])
        vectors = np.load(str(vectors_path), mmap_mode="r", allow_pickle=False)
    except (OSError, ValueError, KeyError) as exc:
        return False, f"UNVERIFIED -- unreadable index data: {exc}"
    if chunk_count != meta["count"]:
        return False, "STALE -- chunks and index metadata disagree"
    if not chunk_files.issubset(manifest):
        return False, "STALE -- chunk files are absent from manifest"
    if vectors.shape != (meta["count"], meta["dim"]):
        return False, "STALE -- vector shape and index metadata disagree"
    if vectors.dtype != np.dtype(np.float16):
        return False, "STALE -- vector dtype is not float16"

    if check_corpus:
        corpus_ok, corpus_message = check_corpus_manifest(
            root, manifest_path, set(config["index"]["exclude_dirs"]))
        if not corpus_ok:
            return False, "STALE -- " + corpus_message

    if check_head:
        try:
            head = subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=str(root), text=True
            ).strip()
        except Exception:
            return False, "UNVERIFIED -- git HEAD unavailable"
        if heartbeat["built_at_head"] != head:
            return False, (f"STALE -- index at {heartbeat['built_at_head'][:8]}, "
                           f"HEAD at {head[:8]}")

    return True, (f"OK -- {meta['count']} chunks, "
                  f"built {heartbeat['last_run_utc'][:19]}")


def check_freshness():
    """Return whether the complete index state matches the repository."""
    return validate_index_state(REPO_ROOT, DATA_DIR, cfg, check_head=True)


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?", help="Search query")
    ap.add_argument("--top-k", type=int, default=cfg["search"]["top_k"])
    ap.add_argument("--no-dense", action="store_true",
                    help="Disable semantic search (BM25 only)")
    ap.add_argument("--no-sparse", action="store_true",
                    help="Disable keyword search (vector only)")
    ap.add_argument("--check-freshness", action="store_true",
                    help="Check index freshness only")
    args = ap.parse_args()

    if args.check_freshness:
        ok, message = check_freshness()
        print(message)
        sys.exit(0 if ok else 1)

    if not args.query:
        ap.print_help()
        sys.exit(1)

    chunks, vectors = load_index()

    results_dense = []
    results_sparse = []

    if not args.no_dense:
        # dense_search embeds via the warm daemon; the in-process model is
        # only loaded lazily as fallback inside embed_query, so we do NOT
        # preload it here (avoids the ~11s cold load when the daemon is up).
        results_dense = dense_search(args.query, None, chunks, vectors,
                                     args.top_k)

    if not args.no_sparse:
        results_sparse = sparse_search(args.query, chunks, args.top_k)

    if results_dense and results_sparse:
        results = rrf_fusion(results_dense, results_sparse,
                             k=cfg["rrf"]["k"], top_k=args.top_k)
    elif results_dense:
        results = results_dense[:args.top_k]
    else:
        results = results_sparse[:args.top_k]

    results = deduplicate_files(results, top_k=args.top_k)

    if cfg.get("reranker", {}).get("enabled", False):
        results = rerank(args.query, results, top_k=args.top_k)

    if not results:
        print("No results found.")
        sys.exit(0)

    for i, r in enumerate(results):
        score = r.get("rrf_score", r.get("score", 0))
        domain_str = f" [{r['domain']}]" if r.get("domain") else ""
        title_str = f" -- {r['title']}" if r.get("title") else ""
        print(f"\n[{i + 1}] {r['file']}{domain_str}{title_str}")
        print(f"    score: {score:.4f}")
        print(f"    {r['snippet'][:200]}...")
