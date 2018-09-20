import unittest
from typing import cast, Iterable

from pycq.q import Q


class SelectMany(unittest.TestCase):
    def test_select_many(self):
        data = [1, 2, 3], [4, 5, 6]
        ret = Q(data).select_many(lambda x: cast(Iterable[int], x)).to_list()
        
        self.assertSequenceEqual(ret, [1, 2, 3, 4, 5, 6])

    def test_chain(self):
        data = [1, 2, 3], [4, 5, 6]
        ret = Q(data).chain().to_list()

        self.assertSequenceEqual(ret, [1, 2, 3, 4, 5, 6])
