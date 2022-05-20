import unittest

from processes.validators.has_a_properly_amount_of_words import has_text_properly_amount_of_words


class TestHasAProperlyAmountOfWords(unittest.TestCase):
    def test_validator(self):
        test_golds = {
            "Hola que tal": True,
            "Hola": False,
            "Os recordamos que \n vuestras opiniones son imprescindibles para mejorar la movilidad sostenible de los "
            "campus de la UPV. Por este motivo, os invitamos a participar en una encuesta que nos ayudará a conocer "
            "el sistema de movilidad actual, su evolución y la percepción que de él tiene la comunidad "
            "universitaria.": False,
            "Hola     ": False,
            "     Hola": False,
            "": False
        }

        for test, gold in test_golds.items():
            self.assertEqual(has_text_properly_amount_of_words(test), gold)


if __name__ == '__main__':
    unittest.main()
