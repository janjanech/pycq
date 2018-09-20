import unittest

from pycq.q import Q


class AnyAll(unittest.TestCase):
    def test_any_non_empty(self):
        data = ("one", "two", "three")
        ret = Q(data).any()

        self.assertTrue(ret)

    def test_any_empty(self):
        data = ()
        ret = Q(data).any()

        self.assertFalse(ret)

    def test_any_contains(self):
        data = ("one", "two", "three")
        ret = Q(data).any(lambda x: x.startswith("o"))

        self.assertTrue(ret)

    def test_any_not_contains(self):
        data = ("one", "two", "three")
        ret = Q(data).any(lambda x: x.startswith("f"))

        self.assertFalse(ret)

    def test_all_true(self):
        data = ("one", "two", "three")
        ret = Q(data).all(lambda x: len(x) > 0)

        self.assertTrue(ret)

    def test_all_false(self):
        data = ("one", "two", "three")
        ret = Q(data).all(lambda x: len(x) == 3)

        self.assertFalse(ret)
