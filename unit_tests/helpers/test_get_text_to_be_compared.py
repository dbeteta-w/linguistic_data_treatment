import unittest

from helpers.get_text_to_be_compared import get_text_to_be_compared


class TestGetTextToBeCompared(unittest.TestCase):
    def test_helper(self):
        test_golds = {
            "Hola que tal": "holaquetal",
            "Hola, que tal": "holaquetal",
            "Hola\tque  tal": "holaquetal",
            "Hola, que tal?\n": "holaquetal",
            "HOLA QUE TAL": "holaquetal",
            "holaquetal": "holaquetal"
        }

        for test, gold in test_golds.items():
            test_to_be_compared = get_text_to_be_compared(test)
            self.assertEqual(test_to_be_compared, gold)


if __name__ == '__main__':
    unittest.main()
