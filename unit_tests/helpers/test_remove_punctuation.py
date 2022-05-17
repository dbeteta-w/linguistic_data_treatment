import unittest

from helpers.remove_punctuation import remove_punctuation


class TestRemovePunctuation(unittest.TestCase):
    def test_helper(self):
        test_golds = {
            "Hola que tal": "Hola que tal",
            "Hola, que tal": "Hola que tal",
            "Hola! que tal?": "Hola que tal",
        }

        for test, gold in test_golds.items():
            test_corrected = remove_punctuation(test)
            self.assertEqual(test_corrected, gold)


if __name__ == '__main__':
    unittest.main()
