"""Check registry consistency and beginner-facing errors."""
import json
from pathlib import Path
import unittest
import academy


class AcademyTests(unittest.TestCase):
    def test_urls_match_catalog(self):
        catalog = json.loads(Path("catalog.json").read_text())
        for name, item in catalog.items():
            self.assertTrue(academy.get_data_url(name).endswith("/" + item["repositoryPath"]))

    def test_missing_empty_unknown_and_wrong_type(self):
        for name in (None, "", "  ", "tpis", "missing"):
            with self.assertRaisesRegex(ValueError, "Available names:.*tips"):
                academy.get_data_url(name)
        with self.assertRaisesRegex(ValueError, "Did you mean 'tips'"):
            academy.get_data_url("tpis")
        with self.assertRaisesRegex(TypeError, "must be a string"):
            academy.get_data_url(42)


if __name__ == "__main__":
    unittest.main()
