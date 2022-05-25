import unittest

from processes.normalizers.get_text_without_tags import get_text_without_tags


class TestGetTextWithoutTags(unittest.TestCase):
    def test_normalizer(self):
        test_golds = {
            "Hola que%d tal": "Hola que tal",
            "Hola que tal&9": "Hola que tal",
            "</head>Hola que tal</head>": "Hola que tal",
            "<map/>Hola que tal<map/>": "Hola que tal",
            "Hola {audio}que tal{audio}": "Hola que tal"
        }

        for test, gold in test_golds.items():
            text_without_tags = get_text_without_tags(test)
            self.assertEqual(text_without_tags, gold)


if __name__ == '__main__':
    unittest.main()
