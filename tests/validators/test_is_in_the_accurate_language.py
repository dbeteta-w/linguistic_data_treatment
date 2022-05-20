import os
import unittest
import fasttext

from processes.validators.is_in_the_accurate_language import is_in_the_accurate_language


class TestIsInTheAccurateLanguage(unittest.TestCase):
    def test_validator(self):
        pretrained_model = "../../models/lid.176.bin"
        fasttext_model = fasttext.load_model(os.path.abspath(pretrained_model))

        test_golds = {
            tuple(["Hola amigo mio", "Hello my friend"]): True,
            tuple(["Hola amigo mio", "Hola amigo mio"]): False,
            tuple(["Hello my friend", "Hello my friend"]): False,
            tuple(["Hello my friend", "Hola amigo mio"]): False,
        }

        for test, gold in test_golds.items():
            src, tgt = test
            self.assertEqual(is_in_the_accurate_language(src, "es", tgt, "en", fasttext_model), gold)


if __name__ == '__main__':
    unittest.main()
