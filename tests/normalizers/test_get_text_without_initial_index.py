import unittest

from processes.normalizers.get_text_without_initial_index import get_text_without_initial_index


class TestGetTextWithoutInitialIndex(unittest.TestCase):
    def test_normalizer(self):
        test_golds = {
            "Hola que tal 22": "Hola que tal 22",
            "98Hola que tal": "Hola que tal",
            "98 Hola que tal": "Hola que tal",
            "98,Hola que tal": "Hola que tal",
            "98|Hola que tal": "Hola que tal",
            "98\tHola que tal": "Hola que tal",
        }

        for test, gold in test_golds.items():
            text_without_initial_index = get_text_without_initial_index(test)
            self.assertEqual(text_without_initial_index, gold)


if __name__ == '__main__':
    unittest.main()
