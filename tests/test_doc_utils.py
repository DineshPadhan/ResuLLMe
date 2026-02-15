import os
import sys
import types
import unittest

sys.modules.setdefault("pdfminer", types.ModuleType("pdfminer"))
pdfminer_high_level = types.ModuleType("pdfminer.high_level")
pdfminer_high_level.extract_text = lambda *_args, **_kwargs: ""
sys.modules["pdfminer.high_level"] = pdfminer_high_level

fake_docx2txt = types.ModuleType("docx2txt")
fake_docx2txt.process = lambda *_args, **_kwargs: ""
sys.modules["docx2txt"] = fake_docx2txt

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from doc_utils import escape_for_latex


class EscapeForLatexTests(unittest.TestCase):
    def test_escapes_special_characters(self):
        input_text = "A&B_#%$"
        escaped = escape_for_latex(input_text)
        self.assertEqual(escaped, r"A\&B\_\#\%\$")

    def test_escapes_nested_data(self):
        data = {
            "name": "John_Doe",
            "skills": ["C++", "R&D"],
        }
        escaped = escape_for_latex(data)

        self.assertEqual(escaped["name"], r"John\_Doe")
        self.assertEqual(escaped["skills"][1], r"R\&D")


if __name__ == "__main__":
    unittest.main()
