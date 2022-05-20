import unittest

from helpers.get_text_without_punctuation import get_text_without_punctuation


class TestGetTextWithoutPunctuation(unittest.TestCase):
    def test_helper(self):
        test_golds = {
            "Hola que tal": "Hola que tal",
            "Hola, que tal": "Hola que tal",
            "Hola! que tal?": "Hola que tal",
            "¡Hola!, ¿que tal?": "Hola que tal"
        }

        for test, gold in test_golds.items():
            test_without_punctuation = get_text_without_punctuation(test)
            self.assertEqual(test_without_punctuation, gold)


if __name__ == '__main__':
    unittest.main()
