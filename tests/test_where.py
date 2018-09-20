import unittest

from pycq.q import Q


class Where(unittest.TestCase):
    def test_where(self):
        ret = Q.range(1, 10).where(lambda x: x > 5).to_list()
        self.assertSequenceEqual([6, 7, 8, 9, 10], ret)
