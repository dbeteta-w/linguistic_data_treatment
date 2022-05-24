import unittest

from processes.normalizers.get_text_with_normalized_quotes import get_text_with_normalized_quotes


class TestGetTextWithNormalizedQuotes(unittest.TestCase):
    def test_normalizer(self):
        test_golds = {
            "Hola que tal": "Hola que tal",
            'Él dijo: "hola, que tal"': 'Él dijo: “hola, que tal”',
            'Él dijo: "hola, que tal»': 'Él dijo: “hola, que tal”',
            'Él dijo: 《hola, que tal"': 'Él dijo: “hola, que tal”',
            'Él dijo: "hola, que tal': 'Él dijo: hola, que tal',
            'Él dijo: “hola, que tal” y luego respondió "yo estoy bien"':
                'Él dijo: “hola, que tal” y luego respondió “yo estoy bien”'
        }

        for test, gold in test_golds.items():
            test_without_punctuation = get_text_with_normalized_quotes(test, "es")
            self.assertEqual(test_without_punctuation, gold)


if __name__ == '__main__':
    unittest.main()

