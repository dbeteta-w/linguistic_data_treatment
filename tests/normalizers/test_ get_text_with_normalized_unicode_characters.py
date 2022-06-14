import unittest
import unicodedata

from processes.normalizers.get_text_with_normalized_unicode_characters import get_text_with_normalized_unicode_characters


class TestGetTextWithNormalizedUnicodeCharacters(unittest.TestCase):
    def test_normalizer(self):
        # # NFC form (Normalization Form Canonical Composition) => accented letters = 1 character
        test_golds = {
            unicodedata.normalize("NFC", "Hola, qué tal"): "Hola, que tal",
            unicodedata.normalize("NFC", "Hola, que tal te va mañana?"): "Hola, que tal te va manana?"
        }

        for test, gold in test_golds.items():
            text_with_normalized_unicode_characters = get_text_with_normalized_unicode_characters(test)
            self.assertEqual(text_with_normalized_unicode_characters, gold)


if __name__ == '__main__':
    unittest.main()
