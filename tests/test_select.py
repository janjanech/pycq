import unittest
from typing import cast

from pycq.q import Q


class Select(unittest.TestCase):
    def test_select(self):
        ret = Q.range(1, 5).select(lambda x: cast(int, x*2)).to_list()
        self.assertSequenceEqual([2, 4, 6, 8, 10], ret)
