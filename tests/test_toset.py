import unittest

from q import Q


class ToSet(unittest.TestCase):
    def test_list(self):
        data = [1, 2, 3]
        ret = Q(data).to_set()

        self.assertIsInstance(ret, set)
        self.assertSetEqual(ret, set(data))
