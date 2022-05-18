import unittest

from validators.has_parallel_number_val import has_parallel_number_val


class TestHasParallelNumberVal(unittest.TestCase):
    def test_validator(self):
        test_golds = {
            tuple(["Hola 23", "Hello 23"]): True,
            tuple(["Hi veintitres", "Hello twenty three"]): True,
            tuple(["Hi veintitres", "Hello 23"]): True,
            tuple(["Hola 23", "Hello 123"]): False,
        }

        for test, gold in test_golds.items():
            src, tgt = test
            self.assertEqual(has_parallel_number_val(src, tgt, "es", "en"), gold)


if __name__ == '__main__':
    unittest.main()
