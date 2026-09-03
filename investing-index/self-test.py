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

    def test_eval_rejects_an_empty_hybrid_modality(self):
        result = {"file": "a.md", "chunk_id": "a:0", "score": 1.0}
        with self.assertRaises(ValueError):
            eval_mod.fuse_hybrid([], [result])
        with self.assertRaises(ValueError):
            eval_mod.fuse_hybrid([result], [])

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


if __name__ == "__main__":
    unittest.main(verbosity=2)
