import unittest

from pycq.q import Q


class Sorting(unittest.TestCase):
    def test_simple_sort(self):
        data = [1, 5, 3, 8, -5]
        ret = Q(data).sort_by(lambda x: x).to_list()

        self.assertSequenceEqual([-5, 1, 3, 5, 8], ret)

    def test_simple_sort_desc(self):
        data = [1, 5, 3, 8, -5]
        ret = Q(data).sort_by_desc(lambda x: x).to_list()

        self.assertSequenceEqual([8, 5, 3, 1, -5], ret)

    def sort_by_multiple(self):
        data = [1, 2, 5, 3, 8, -5]
        ret = Q(data)\
            .sort_by(lambda x: x%2)\
            .then_by(lambda x: x)\
            .to_list()

        self.assertSequenceEqual([2, 8, -5, 1, 3, 5], ret)

    def sort_by_multiple_with_different_orders(self):
        data = [1, 2, 5, 3, 8, -5]
        ret = Q(data)\
            .sort_by(lambda x: x%2)\
            .then_by_desc(lambda x: x)\
            .to_list()

        self.assertSequenceEqual([8, 2, 5, 3, 1, -5], ret)
