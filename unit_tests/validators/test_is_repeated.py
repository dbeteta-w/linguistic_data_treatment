import unittest

from validators.is_repeated import is_repeated


class TestIsRepeated(unittest.TestCase):
    def test_validator(self):
        test_set = {
            tuple(["holaquetal", "hihowareyou"])
        }

        test_golds = {
            tuple(["Hola que tal", "Hi how are you doing"]): False,
            tuple(["Hola que tal", "Hi how are you"]): True,
            tuple(["Hola, que tal?", "Hi, how are you?"]): True,
            tuple(["HOLA QUE TAL", "HI HOW ARE YOU"]): True,
            tuple([" Hola que     tal", " Hi how    are you"]): True
        }

        for test, gold in test_golds.items():
            src, tgt = test
            self.assertEqual(is_repeated(src, tgt, test_set), gold)


if __name__ == '__main__':
    unittest.main()
