import unittest

from validators.has_too_many_numbers import has_text_too_many_numbers


class TestHasTooManyNumbers(unittest.TestCase):
    def test_validator(self):
        test_golds = {
            "Hola que tal": False,
            "Hola que tal 23": False,
            "Ho2": True,
            "xyz 23": True,
            "12345": True,
        }

        for test, gold in test_golds.items():
            self.assertEqual(has_text_too_many_numbers(test), gold)


if __name__ == '__main__':
    unittest.main()
