import unittest

from pycq.q import Q


class ToDict(unittest.TestCase):
    def test_without_value_selector(self):
        data = ("one", "two", "four")
        ret = Q(data).to_dict(lambda x: x[0])

        self.assertIsInstance(ret, dict)
        self.assertEqual({"o": "one", "t": "two", "f": "four"}, ret)

    def test_with_value_selector(self):
        data = ("one", "two", "four")
        ret = Q(data).to_dict(lambda x: x[0], lambda x: ord(x[1]))

        self.assertIsInstance(ret, dict)
        self.assertEqual({"o": 110, "t": 119, "f": 111}, ret)
