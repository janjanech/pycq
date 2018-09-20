import unittest

from pycq.q import Q


class Default(unittest.TestCase):
    def test_distinct(self):
        data = (1, 1, 2, 5, 1)
        ret = Q(data).distinct().to_set()

        self.assertSetEqual({1, 2, 5}, ret)

    def test_distinct_with_key_selector(self):
        data = (1, 1, 2, 5, 1)
        ret = Q(data).distinct(lambda x: x%2).to_set()

        self.assertSetEqual({1, 2}, ret)

    def test_ordered_distinct(self):
        data = (1, 1, 2, 5, 1)
        ret = Q(data).distinct_ordered().to_list()

        self.assertSequenceEqual([1, 2, 5, 1], ret)

    def test_ordered_distinct_with_key_selector(self):
        data = (1, 1, 2, 5, 1)
        ret = Q(data).distinct_ordered(lambda x: x%2).to_list()

        self.assertSequenceEqual([1, 2, 5], ret)
