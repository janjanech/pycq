import unittest
from collections import Callable

from q import Q


class ToDict(unittest.TestCase):
    def test_without_value_selector(self):
        data = ("one", "two", "four")
        key_sel:  Callable[[str], str] = lambda x: x[0]
        ret = Q(data).to_dict(key_sel)

        self.assertIsInstance(ret, dict)
        self.assertEqual(ret, {"o": "one", "t": "two", "f": "four"})

    def test_with_value_selector(self):
        data = ("one", "two", "four")
        key_sel:  Callable[[str], str] = lambda x: x[0]
        ret = Q(data).to_dict(key_sel)
        value_sel:  Callable[[str], int] = lambda x: ord(x[1])
        ret = Q(data).to_dict(key_sel, value_sel)

        self.assertIsInstance(ret, dict)
        self.assertEqual(ret, {"o": 110, "t": 119, "f": 111})
