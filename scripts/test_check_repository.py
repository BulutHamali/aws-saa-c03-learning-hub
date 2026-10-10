"""Exercise checks with intentionally broken navigation, not just happy paths."""

import tempfile
import unittest
from pathlib import Path

from check_repository import anchors, check_attribution, check_links, check_plan


class RepositoryChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name, text):
        target = self.root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def test_missing_target(self):
        self.write("README.md", "[missing](missing.md)")
        self.assertIn("missing link target", check_links(self.root)[0])

    def test_missing_fragment(self):
        self.write("README.md", "# Existing\n[missing](#absent)")
        self.assertIn("missing heading anchor", check_links(self.root)[0])

    def test_valid_cross_file_encoded_path_and_fragment(self):
        self.write("README.md", "[ok](my%20guide.md#read--retry)")
        self.write("my guide.md", "## Read & Retry\n")
        self.assertEqual(check_links(self.root), [])

    def test_images_are_checked(self):
        self.write("README.md", "![diagram](missing.png)")
        self.assertIn("missing link target", check_links(self.root)[0])

    def test_escape_is_rejected(self):
        self.write("README.md", "[escape](../outside.md)")
        self.assertIn("escapes repository", check_links(self.root)[0])

    def test_external_and_fenced_examples_are_ignored(self):
        self.write("README.md", "[web](https://example.org/a#b)\n~~~md\n[example](missing.md)\n~~~\n")
        self.assertEqual(check_links(self.root), [])

    def test_duplicate_headings_and_code(self):
        self.assertEqual(anchors("## Hello\n## Hello\n```md\n## Fake\n```\n"), {"hello", "hello-1"})

    def test_plan_omission_is_detected(self):
        self.write("topic-guides/00-README.md", "# Index")
        self.write("topic-guides/01-IAM.md", "# IAM")
        self.write("learning-paths/4-week-plan.md", "# Plan")
        self.assertEqual(check_plan(self.root), ["Study plan omits topic guide: 01-IAM.md"])

    def test_plan_link_coverage(self):
        self.write("topic-guides/00-README.md", "# Index")
        self.write("topic-guides/01-IAM.md", "# IAM")
        self.write("learning-paths/4-week-plan.md", "[IAM](../topic-guides/01-IAM.md)")
        self.assertEqual(check_plan(self.root), [])

    def test_missing_attribution(self):
        self.write("README.md", "# Guide")
        self.assertEqual(len(check_attribution(self.root)), 3)


if __name__ == "__main__":
    unittest.main()
