import unittest

from processes.validators.has_properly_length_factor_val import has_properly_length_factor_val


class TestHasProperlyLengthFactorVal(unittest.TestCase):
    def test_validator(self):
        test_golds = {
            tuple(["Hola amigo", "Hello friend"]): True,
            tuple(["Hola", "Hello"]): True,
            tuple(["Hola", "Hello, how are you doing my friend?"]): False,
            tuple(["Hola, ¿cómo vas amigo mio?", "Hello"]): False,
        }

        for test, gold in test_golds.items():
            src, tgt = test
            self.assertEqual(has_properly_length_factor_val(src, tgt), gold)


if __name__ == '__main__':
    unittest.main()
