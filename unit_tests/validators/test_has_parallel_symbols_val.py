import unittest

from validators.has_parallel_symbols_val import has_parallel_symbols_val


class TestHasParallelSymbolsVal(unittest.TestCase):
    def test_validator(self):
        test_golds = {
            tuple(["Hola", "Hello"]): True,
            tuple(["Hola...", "Hello..."]): True,
            tuple(["Hola @dbeteta-w", "Hello my friend @dbeteta-w"]): True,
            tuple(["Hola, mi nombre es Dani.", "Hello my name is Dani"]): True,
            tuple(["Hola...", "Hello"]): False,
        }

        for test, gold in test_golds.items():
            src, tgt = test
            x = has_parallel_symbols_val(src, tgt)
            self.assertEqual(has_parallel_symbols_val(src, tgt), gold)


if __name__ == '__main__':
    unittest.main()
