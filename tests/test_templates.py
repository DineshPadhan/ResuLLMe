import os
import sys
import types
import unittest

fake_jinja2 = types.ModuleType("jinja2")
fake_jinja2.Environment = object
fake_jinja2.FileSystemLoader = object
sys.modules["jinja2"] = fake_jinja2

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from templates import get_final_section_ordering


class TemplateOrderingTests(unittest.TestCase):
    def test_basics_is_always_first(self):
        ordering = get_final_section_ordering(["skills", "work"])
        self.assertEqual(ordering[0], "basics")

    def test_no_duplicates_in_final_ordering(self):
        ordering = get_final_section_ordering(["skills", "skills", "education"])
        self.assertEqual(ordering.count("skills"), 1)
        self.assertEqual(ordering.count("education"), 1)


if __name__ == "__main__":
    unittest.main()
