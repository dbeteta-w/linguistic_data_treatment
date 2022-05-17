import unittest

from helpers.clean_to_be_compared import clean_to_be_compared


class TestCleanToBeCompared(unittest.TestCase):
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
            test_corrected = clean_to_be_compared(test)
            self.assertEqual(test_corrected, gold)


if __name__ == '__main__':
    unittest.main()
