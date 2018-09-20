import unittest

from pycq.q import Q


class ToSet(unittest.TestCase):
    def test_non_frozen(self):
        data = [1, 2, 3]
        ret = Q(data).to_set()

        self.assertIsInstance(ret, set)
        self.assertSetEqual(ret, set(data))

    def test_frozen(self):
        data = [1, 2, 3]
        ret = Q(data).to_frozenset()

        self.assertIsInstance(ret, frozenset)
        self.assertSetEqual(ret, set(data))
