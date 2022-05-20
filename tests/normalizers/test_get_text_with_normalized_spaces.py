import unittest

from processes.normalizers.get_text_with_normalized_spaces import get_text_with_normalized_spaces


class TestGetTextWithNormalizedSpaces(unittest.TestCase):
    def test_normalizer(self):
        test_golds = {
            "Hola que tal": "Hola que tal",
            "Hola    que tal": "Hola que tal",
            "Hola que\t tal": "Hola que tal",
            "Hola que tal\n": "Hola que tal",
            "Hola   ": "Hola",
            "   Hola": "Hola"
        }

        for test, gold in test_golds.items():
            text_with_normalized_spaces = get_text_with_normalized_spaces(test)
            self.assertEqual(text_with_normalized_spaces, gold)


if __name__ == '__main__':
    unittest.main()
