import unittest
import unicodedata

from processes.normalizers.get_text_with_normalized_accents import get_text_with_normalized_accents


class TestGetTextWithNormalizedAccents(unittest.TestCase):
    def test_normalizer(self):
        test_golds = {
            unicodedata.normalize("NFD", "Hola, qué tal"): "Hola, qué tal",
            unicodedata.normalize("NFD", "Hola, que tal te va mañana?"): "Hola, que tal te va mañana?"
        }

        for test, gold in test_golds.items():
            text_with_normalized_accents = get_text_with_normalized_accents(test)
            self.assertEqual(text_with_normalized_accents, gold)


if __name__ == '__main__':
    unittest.main()
