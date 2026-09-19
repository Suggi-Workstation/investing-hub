"""Archive regressions use disposable logs, never a repository's live logbook."""

from contextlib import redirect_stdout
import importlib.util
import io
from pathlib import Path
import re
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "logbook-archive.py"


class LogbookArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="logbook-archive-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        spec = importlib.util.spec_from_file_location("archive_under_test", SCRIPT)
        assert spec is not None and spec.loader is not None
        self.archive = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.archive)
        setattr(self.archive, "ARCHIVE_DIR", str(self.root / "archive"))
        self.log = self.root / "activity.log"
        self.header = "<!-- Disposable log fixture. -->\n\n"

    @staticmethod
    def entry(number, lines):
        return f"## [ENT-{number:03d}] | fixture\n" + "Fixture body.\n" * (lines - 1)

    def process(self):
        with redirect_stdout(io.StringIO()):
            return self.archive.process_log(str(self.log))

    def test_oversized_newest_entry_remains_active_with_latest_counter(self):
        old = self.entry(588, self.archive.MAX_LINES)
        newest = self.entry(589, self.archive.TARGET_LINES + 1)
        self.log.write_text(self.header + old + newest, encoding="ascii")

        self.assertTrue(self.process())
        self.assertEqual(self.log.read_text(encoding="ascii"), self.header + newest)
        ids = re.findall(r"^## \[ENT-(\d+)\]", self.log.read_text(), re.M)
        self.assertEqual(ids, ["589"])
        archived = list((self.root / "archive").glob("*.log"))
        self.assertEqual(len(archived), 1)
        contents = archived[0].read_text(encoding="ascii")
        self.assertIn(old, contents)
        self.assertNotIn(newest, contents)
        before = archived[0].read_bytes()
        self.assertFalse(self.process())
        self.assertEqual(archived[0].read_bytes(), before)

    def test_single_oversized_entry_is_left_intact_without_an_archive(self):
        original = self.header + self.entry(589, self.archive.MAX_LINES + 1)
        self.log.write_text(original, encoding="ascii")

        self.assertFalse(self.process())
        self.assertEqual(self.log.read_text(encoding="ascii"), original)
        self.assertFalse((self.root / "archive").exists())

    def test_normal_trimming_preserves_complete_newest_entries(self):
        old = self.entry(587, self.archive.MAX_LINES)
        recent = self.entry(588, 20)
        newest = self.entry(589, 20)
        self.log.write_text(self.header + old + recent + newest, encoding="ascii")

        self.assertTrue(self.process())
        self.assertEqual(self.log.read_text(encoding="ascii"), self.header + recent + newest)
        archived = list((self.root / "archive").glob("*.log"))
        self.assertEqual(len(archived), 1)
        self.assertIn(old, archived[0].read_text(encoding="ascii"))
        self.assertFalse(self.process())


if __name__ == "__main__":
    unittest.main()
