import unittest

from pycq.q import Q


class SetOperations(unittest.TestCase):
    def test_union(self):
        data1 = [1, 2, 3, 4]
        data2 = [3, 4, 5, 6, 7]

        ret = Q(data1).union(data2).to_set()

        self.assertSetEqual({1, 2, 3, 4, 5, 6, 7}, ret)

    def test_intersection(self):
        data1 = [1, 2, 3, 4]
        data2 = [3, 4, 5, 6, 7]

        ret = Q(data1).intersect(data2).to_set()

        self.assertSetEqual({3, 4}, ret)

    def test_difference(self):
        data1 = [1, 2, 3, 4]
        data2 = [3,  4, 5, 6, 7]

        ret = Q(data1).except_(data2).to_set()

        self.assertSetEqual({1, 2}, ret)
