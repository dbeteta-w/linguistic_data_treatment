import unittest

from processes.normalizers.get_text_without_repeated_symbols import get_text_without_repeated_symbols


class TestGetTextWithoutRepeatedSymbols(unittest.TestCase):
    def test_normalizer(self):
        test_golds = {
            "": "",
            "Hola que tal": "Hola que tal",
            "Hola,, que tal": "Hola, que tal",
            "Hola que tal..": "Hola que tal.",
            "Hola que tal;.": "Hola que tal;",
            "Hola,:, que tal": "Hola, que tal",
            "Hola,, que tal??": "Hola, que tal?"
        }

        for test, gold in test_golds.items():
            test_without_repeated_symbols = get_text_without_repeated_symbols(test)
            self.assertEqual(test_without_repeated_symbols, gold)


if __name__ == '__main__':
    unittest.main()

