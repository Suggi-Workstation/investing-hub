#!/usr/bin/env python3
"""Regression tests shared by all three repository indexes."""

import importlib
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

INDEX_DIR = Path(__file__).resolve().parent
REPO_ROOT = INDEX_DIR.parent
sys.path.insert(0, str(INDEX_DIR))
index_mod = importlib.import_module("index")
query_mod = importlib.import_module("query")
eval_mod = importlib.import_module("eval")
np = query_mod.np

class IndexContractTests(unittest.TestCase):
    def test_package_uses_repo_neutral_root_name(self):
        source = (INDEX_DIR / "index.py").read_text(encoding="ascii")
        self.assertNotIn("BRAIN_ROOT", source)
        self.assertIn("REPO_ROOT = SCRIPT_DIR.parent", source)
        self.assertNotIn("allow_legacy_chunking=True", source)

    def test_package_identity_is_repo_specific(self):
        index_name = INDEX_DIR.name
        repo_name = REPO_ROOT.name
        self.assertIn(index_name, (INDEX_DIR / "index.py").read_text(encoding="ascii")[:200])
        self.assertIn(index_name, (INDEX_DIR / "query.py").read_text(encoding="ascii")[:200])
        self.assertIn(index_name, (INDEX_DIR / "eval.py").read_text(encoding="ascii")[:200])
        self.assertIn(index_name, (INDEX_DIR / "config.yaml").read_text(encoding="ascii").splitlines()[0])
        self.assertIn(index_name, (INDEX_DIR / ".gitignore").read_text(encoding="ascii").splitlines()[0])
        readme = (INDEX_DIR / "README.md").read_text(encoding="ascii")
        self.assertIn(index_name, readme.lower())
        self.assertIn(repo_name, readme.lower())

    def test_index_check_reads_the_live_data_directory(self):
        ok, message = index_mod.check_freshness()
        self.assertIsInstance(ok, bool)
        self.assertTrue(message.startswith(
            ("OK --", "STALE --", "UNVERIFIED --", "NO INDEX --")), message)

    def test_query_freshness_returns_a_status_tuple(self):
        result = query_mod.check_freshness()
        self.assertIsInstance(result, tuple)
        ok, message = result
        self.assertIsInstance(ok, bool)
        self.assertTrue(message.startswith(
            ("OK --", "STALE --", "UNVERIFIED --", "NO INDEX --")), message)

    def test_freshness_checks_report_the_same_heartbeat(self):
        index_ok, index_message = index_mod.check_freshness()
        query_ok, query_message = query_mod.check_freshness()
        self.assertEqual(index_ok, query_ok)
        if index_ok:
            self.assertEqual(
                index_message.split("built ", 1)[1],
                query_message.split("built ", 1)[1],
            )
        else:
            self.assertEqual(index_message, query_message)

    def test_query_freshness_cli_fails_without_an_index(self):
        with tempfile.TemporaryDirectory() as temp_home:
            env = dict(os.environ)
            env["HOME"] = temp_home
            result = subprocess.run(
                [sys.executable, str(INDEX_DIR / "query.py"), "--check-freshness"],
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("NO INDEX", result.stdout)

    def test_malformed_heartbeat_fails_closed(self):
        current_head = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True).strip()
        with tempfile.TemporaryDirectory() as temp_data:
            heartbeat = Path(temp_data) / "heartbeat.json"
            heartbeat.write_text(
                json.dumps({"built_at_head": current_head}), encoding="ascii")
            with mock.patch.object(query_mod, "DATA_DIR", Path(temp_data)):
                query_ok, query_message = query_mod.check_freshness()
                index_ok, index_message = index_mod.check_freshness()
        self.assertFalse(query_ok)
        self.assertFalse(index_ok)
        self.assertEqual(query_message, index_message)

    def test_corpus_manifest_detects_untracked_markdown(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            document = root / "new-topic.md"
            document.write_text("# New topic\n", encoding="ascii")
            manifest = root / "manifest.json"
            manifest.write_text("{}", encoding="ascii")
            ok, _ = query_mod.check_corpus_manifest(root, manifest, set())
            self.assertFalse(ok)
            digest = hashlib.md5(document.read_bytes()).hexdigest()
            manifest.write_text(json.dumps({
                "new-topic.md": {"hash": digest},
            }), encoding="ascii")
            ok, _ = query_mod.check_corpus_manifest(root, manifest, set())
            self.assertTrue(ok)

    def test_index_state_rejects_metadata_and_vector_mismatches(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "repo"
            data = Path(temp_dir) / "index"
            root.mkdir()
            data.mkdir()
            document = root / "topic.md"
            document.write_text("# Topic\n", encoding="ascii")
            digest = hashlib.md5(document.read_bytes()).hexdigest()
            (data / "manifest.json").write_text(json.dumps({
                "topic.md": {"hash": digest},
            }), encoding="ascii")
            (data / "chunks.jsonl").write_text(
                json.dumps({"file": "topic.md"}) + "\n", encoding="ascii")
            np.save(data / "vectors.npy", np.zeros((1, 2), dtype=np.float16))
            meta = {
                "format_version": 1, "model": "test-model", "dim": 2,
                "count": 1, "files": 1,
                "built_at": "2026-01-01T00:00:00+00:00", "mode": "full",
                "chunking": {},
            }
            heartbeat = {
                "schema_version": 1,
                "last_run_utc": "2026-01-01T00:00:00+00:00",
                "status": "ok", "built_at_head": "0" * 40,
                "count": 1, "files": 1, "model": "test-model",
            }
            (data / "meta.json").write_text(json.dumps(meta), encoding="ascii")
            (data / "heartbeat.json").write_text(
                json.dumps(heartbeat), encoding="ascii")
            config = {
                "embedding": {"model": "test-model", "dim": 2},
                "index": {"exclude_dirs": []},
                "chunking": {},
            }
            ok, _ = query_mod.validate_index_state(
                root, data, config, check_head=False)
            self.assertTrue(ok)
            np.save(data / "vectors.npy", np.zeros((2, 2), dtype=np.float16))
            ok, _ = query_mod.validate_index_state(
                root, data, config, check_head=False)
            self.assertFalse(ok)
            np.save(data / "vectors.npy", np.zeros((1, 2), dtype=np.float16))
            meta["dim"] = 3
            (data / "meta.json").write_text(json.dumps(meta), encoding="ascii")
            ok, _ = query_mod.validate_index_state(
                root, data, config, check_head=False)
            self.assertFalse(ok)
            meta["dim"] = 2
            heartbeat["model"] = None
            (data / "meta.json").write_text(json.dumps(meta), encoding="ascii")
            (data / "heartbeat.json").write_text(
                json.dumps(heartbeat), encoding="ascii")
            ok, _ = query_mod.validate_index_state(
                root, data, config, check_head=False)
            self.assertFalse(ok)

            heartbeat["model"] = "test-model"
            heartbeat["schema_version"] = True
            (data / "heartbeat.json").write_text(
                json.dumps(heartbeat), encoding="ascii")
            ok, _ = query_mod.validate_index_state(
                root, data, config, check_head=False)
            self.assertFalse(ok)

            heartbeat["schema_version"] = 1
            meta["format_version"] = True
            (data / "heartbeat.json").write_text(
                json.dumps(heartbeat), encoding="ascii")
            (data / "meta.json").write_text(json.dumps(meta), encoding="ascii")
            ok, _ = query_mod.validate_index_state(
                root, data, config, check_head=False)
            self.assertFalse(ok)

    def test_multi_file_relevance_metrics(self):
        results = [{"file": "a.md"}, {"file": "b.md"}, {"file": "x.md"}]
        self.assertEqual(eval_mod.recall_at_k(["a.md", "b.md"], results, 2), 1.0)
        self.assertEqual(eval_mod.reciprocal_rank(["a.md", "b.md"], results), 1.0)
        self.assertEqual(eval_mod.ndcg_at_k(["a.md", "b.md"], results, 2), 1.0)

    def test_file_deduplication_preserves_rank_order(self):
        results = [
            {"file": "a.md", "score": 3.0},
            {"file": "a.md", "score": 2.0},
            {"file": "b.md", "score": 1.0},
        ]
        unique = query_mod.deduplicate_files(results, top_k=2)
        self.assertEqual([result["file"] for result in unique], ["a.md", "b.md"])

    def test_metrics_ignore_duplicate_chunks(self):
        results = [
            {"file": "a.md", "score": 3.0},
            {"file": "a.md", "score": 2.0},
            {"file": "b.md", "score": 1.0},
        ]
        self.assertEqual(eval_mod.recall_at_k(["a.md", "b.md"], results, 2), 1.0)
        self.assertEqual(eval_mod.ndcg_at_k(["a.md", "b.md"], results, 2), 1.0)

    def test_success_at_k_needs_a_relevant_file_in_the_top_k(self):
        results = [{"file": "x.md"}, {"file": "x.md"}, {"file": "a.md"}]
        self.assertEqual(eval_mod.success_at_k(["a.md"], results, 1), 0.0)
        self.assertEqual(eval_mod.success_at_k(["a.md"], results, 2), 1.0)

    def test_paired_comparison_reports_difference_and_interval(self):
        baseline = [{"qid": "q1", "rr": 1.0}, {"qid": "q2", "rr": 0.5}, {"qid": "q3", "rr": 0.0}]
        current = [{"qid": "q3", "rr": 0.5}, {"qid": "q1", "rr": 1.0}, {"qid": "q2", "rr": 1.0}]
        result = eval_mod.compare_runs(current, baseline)
        self.assertEqual((result["queries"], result["better"], result["worse"]), (3, 2, 0))
        self.assertAlmostEqual(result["mrr_diff"], 1 / 3, places=4)
        low, high = result["interval"]
        self.assertLess(low, result["mrr_diff"])
        self.assertGreater(high, result["mrr_diff"])

    def test_paired_comparison_rejects_a_different_question_set(self):
        with self.assertRaises(ValueError):
            eval_mod.compare_runs([{"qid": "q1", "rr": 1.0}], [{"qid": "q2", "rr": 1.0}])

    def test_keyword_tokens_are_lowercase_words(self):
        self.assertEqual(
            query_mod.tokenize("**BM25** retrieval, Re-ranking (v2)!"),
            ["bm25", "retrieval", "re", "ranking", "v2"])

    def test_keyword_search_matches_words_next_to_punctuation(self):
        chunks = [
            {"file": "a.md", "chunk_id": "a:0", "text": "Use **BM25**, then fuse both lists."},
            {"file": "b.md", "chunk_id": "b:0", "text": "Soft-boiled eggs need six minutes."},
        ]
        results = query_mod.sparse_search("bm25 fusion", chunks, top_k=5)
        self.assertEqual([result["file"] for result in results], ["a.md"])

    def test_keyword_statistics_are_built_once_per_index(self):
        chunks = [
            {"file": "a.md", "chunk_id": "a:0", "text": "alpha beta"},
            {"file": "b.md", "chunk_id": "b:0", "text": "gamma delta"},
        ]
        with mock.patch.object(query_mod, "BM25", wraps=query_mod.BM25) as built:
            first = query_mod.sparse_search("alpha", chunks, top_k=5)
            second = query_mod.sparse_search("gamma", chunks, top_k=5)
            self.assertEqual(built.call_count, 1)
            query_mod.sparse_search("alpha", list(chunks), top_k=5)
            self.assertEqual(built.call_count, 2)
        self.assertEqual([result["file"] for result in first], ["a.md"])
        self.assertEqual([result["file"] for result in second], ["b.md"])

    @staticmethod
    def _candidates(*chunk_ids):
        chunks = [{"file": cid.split(":")[0] + ".md", "chunk_id": cid,
                   "text": f"full text of {cid}"} for cid in chunk_ids]
        ranked = [{"file": c["file"], "chunk_id": c["chunk_id"], "score": 1.0,
                   "snippet": c["text"][:4]} for c in chunks]
        return chunks, ranked

    def test_rerank_orders_the_first_candidates_by_reranker_score(self):
        chunks, ranked = self._candidates("a:0", "b:0", "c:0")
        sent = []

        def scores(question, texts):
            sent.extend(texts)
            return [0.1, 0.9]

        with mock.patch.dict(query_mod.cfg, {"reranker": {"enabled": True, "top_k": 2}}), \
                mock.patch.object(query_mod, "_daemon_rerank", scores):
            result = query_mod.rerank("q", ranked, chunks)
        self.assertEqual([r["file"] for r in result], ["b.md", "a.md", "c.md"])
        self.assertEqual(sent, ["full text of a:0", "full text of b:0"])
        self.assertEqual(result[0]["rerank_score"], 0.9)

    def test_rerank_keeps_the_order_without_a_reranker_answer(self):
        chunks, ranked = self._candidates("a:0", "b:0")
        with mock.patch.dict(query_mod.cfg, {"reranker": {"enabled": True, "top_k": 25}}), \
                mock.patch.object(query_mod, "_daemon_rerank", lambda question, texts: None):
            result = query_mod.rerank("q", ranked, chunks)
        self.assertEqual([r["file"] for r in result], ["a.md", "b.md"])

    def test_rerank_is_not_called_when_disabled(self):
        chunks, ranked = self._candidates("a:0", "b:0")
        with mock.patch.dict(query_mod.cfg, {"reranker": {"enabled": False, "top_k": 25}}), \
                mock.patch.object(query_mod, "_daemon_rerank") as called:
            result = query_mod.rerank("q", ranked, chunks)
        called.assert_not_called()
        self.assertEqual(result, ranked)

    def test_combine_returns_each_file_once_led_by_its_best_chunk(self):
        chunks, ranked = self._candidates("a:0", "a:1", "b:0")
        with mock.patch.dict(query_mod.cfg, {"reranker": {"enabled": True, "top_k": 25}}), \
                mock.patch.object(query_mod, "_daemon_rerank",
                                  lambda question, texts: [0.2, 0.9, 0.5]):
            result = query_mod.combine("q", ranked, ranked, chunks, top_k=20)
        self.assertEqual([r["chunk_id"] for r in result], ["a:1", "b:0"])

    def test_eval_rejects_a_reranker_run_without_scores(self):
        result = {"file": "a.md", "chunk_id": "a:0", "score": 1.0}
        with mock.patch.dict(query_mod.cfg, {"reranker": {"enabled": True, "top_k": 25}}):
            with self.assertRaises(ValueError):
                eval_mod.require_reranked([result])
            eval_mod.require_reranked([dict(result, rerank_score=0.5)])
        with mock.patch.dict(query_mod.cfg, {"reranker": {"enabled": False, "top_k": 25}}):
            eval_mod.require_reranked([result])

    def test_eval_rejects_an_empty_hybrid_modality(self):
        result = {"file": "a.md", "chunk_id": "a:0", "score": 1.0}
        with self.assertRaises(ValueError):
            eval_mod.require_hybrid([], [result])
        with self.assertRaises(ValueError):
            eval_mod.require_hybrid([result], [])

    def test_gold_set_is_complete_and_valid(self):
        queries = eval_mod.load_gold_queries()
        self.assertGreater(len(queries), 0)
        indexed_files = set()
        with (Path(index_mod.DATA_DIR) / "chunks.jsonl").open(encoding="utf-8") as handle:
            for line in handle:
                indexed_files.add(json.loads(line)["file"])
        normalized = eval_mod.validate_gold_queries(queries, indexed_files)
        self.assertEqual(len(normalized), len(queries))
        self.assertEqual(len({q["qid"] for q in normalized}), len(normalized))

    def test_invalid_gold_target_is_rejected(self):
        bad = [{
            "qid": "bad001",
            "question": "This target does not exist.",
            "gold_files": ["../outside.md"],
            "domain": "test",
        }]
        with self.assertRaises(ValueError):
            eval_mod.validate_gold_queries(bad, set())


# --- chunk reuse (2026-11-24): a subprocess build against a fake embed daemon ---
TOOL_DIR = INDEX_DIR
TOOL_SUBDIR = INDEX_DIR.name
DOCS_SUBDIR = "notes"
DOCS_PREFIX = "notes/"
CONFIG_UPDATE = lambda root: {"data_dir": str(root / "data")}
DATA_OF = lambda root, tool: root / "data"


class ChunkReuseTests(unittest.TestCase):
    """An edit re-embeds only the chunks whose text changed; the result equals a full rebuild."""

    def setUp(self):
        import http.server
        import shutil
        import threading
        import yaml
        temp = tempfile.TemporaryDirectory(prefix="index-reuse-")
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.seen = []
        seen, dim = self.seen, 1024

        class Fake(http.server.BaseHTTPRequestHandler):
            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                seen.extend(body["texts"])
                vecs = [np.random.default_rng(int(hashlib.sha256(t.encode()).hexdigest()[:12], 16))
                        .standard_normal(dim).tolist() for t in body["texts"]]
                out = json.dumps({"embeddings": vecs}).encode()
                self.send_response(200)
                self.send_header("Content-Length", str(len(out)))
                self.end_headers()
                self.wfile.write(out)

            def log_message(self, *args):
                pass

        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Fake)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.shutdown)
        self.url = "http://127.0.0.1:%d/embed" % server.server_address[1]
        self.tool = self.root / TOOL_SUBDIR
        self.tool.mkdir(parents=True)
        for name in ("index.py", "query.py"):
            shutil.copy2(TOOL_DIR / name, self.tool / name)
        cfg = yaml.safe_load((TOOL_DIR / "config.yaml").read_text())
        cfg["index"].update(CONFIG_UPDATE(self.root))
        (self.tool / "config.yaml").write_text(yaml.safe_dump(cfg))
        self.docs = self.root / DOCS_SUBDIR
        self.docs.mkdir(parents=True, exist_ok=True)
        self.data = DATA_OF(self.root, self.tool)

    def paragraphs(self, tag, n):
        return ["Paragraph %s %d. " % (tag, i) + " ".join("word%s%d" % (tag, k) for k in range(i * 90, i * 90 + 90))
                for i in range(n)]

    def build(self, *flags):
        del self.seen[:]
        env = dict(os.environ, BRAIN_EMBED_URL=self.url)
        run = subprocess.run([sys.executable, str(self.tool / "index.py"), *flags], cwd=self.root, env=env,
                             capture_output=True, text=True, timeout=300)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        return len(self.seen)

    def index(self):
        chunks = [json.loads(line) for line in (self.data / "chunks.jsonl").read_text().splitlines() if line.strip()]
        vectors = np.load(self.data / "vectors.npy")
        self.assertEqual(len(chunks), len(vectors))
        return {c["chunk_id"]: (c["text"], vectors[i].tobytes()) for i, c in enumerate(chunks)}

    def test_an_edit_reembeds_only_changed_chunks_and_equals_a_full_rebuild(self):
        long_doc = self.paragraphs("a", 8)
        (self.docs / "a.md").write_text("# A\n\n" + "\n\n".join(long_doc) + "\n")
        (self.docs / "b.md").write_text("# B\n\nA short note that fits one chunk.\n")
        first = self.build("--force")
        before = self.index()
        a_chunks = [k for k in before if k.startswith(DOCS_PREFIX + "a.md::")]
        self.assertGreaterEqual(len(a_chunks), 3)
        self.assertEqual(first, len(before))                       # a full build embeds every chunk

        long_doc[-1] = "Paragraph a changed. " + long_doc[-1]        # one edit near the end
        (self.docs / "a.md").write_text("# A\n\n" + "\n\n".join(long_doc) + "\n")
        embedded = self.build()
        after = self.index()
        self.assertGreaterEqual(embedded, 1)
        self.assertLess(embedded, len(a_chunks))                  # not the whole file again
        kept = [k for k in a_chunks if after.get(k, (None,))[0] == before[k][0]]
        self.assertTrue(kept)
        for k in kept:
            self.assertEqual(after[k][1], before[k][1])            # unchanged text keeps its vector

        (self.docs / "b.md").rename(self.docs / "c.md")             # same text under a new name
        twin = "# Twin\n\nThe same new note written into two files.\n"
        (self.docs / "x.md").write_text(twin)
        (self.docs / "y.md").write_text(twin)
        self.assertEqual(self.build(), 1)                         # the rename costs nothing, the twins one call
        incremental = self.index()

        distinct = len({text for text, _vector in incremental.values()})
        self.assertEqual(self.build("--force"), distinct)          # --force reuses nothing from the old index
        self.assertEqual(self.index(), incremental)               # and builds exactly the same index


if __name__ == "__main__":
    unittest.main(verbosity=2)
