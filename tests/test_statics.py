import unittest

from pycq.q import Q


class Statics(unittest.TestCase):
    def test_empty(self):
        ret = Q.empty().to_list()
        self.assertSequenceEqual([], ret)

    def test_range(self):
        ret = Q.range(1, 10).to_list()
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ret)

    def test_repeat_with_count(self):
        ret = Q.repeat('A', 5).to_list()
        self.assertSequenceEqual(['A', 'A', 'A', 'A', 'A'], ret)

    def test_infinite_iterate(self):
        ret = Q.iterate(1, lambda x: x * 10).take_while(lambda x: x < 2000).to_list()
        self.assertSequenceEqual([1, 10, 100, 1000], ret)

    def test_infinite_count(self):
        ret = Q.count(1).take(5).to_list()
        self.assertSequenceEqual([1, 2, 3, 4, 5], ret)

    def test_infinite_repeat(self):
        ret = Q.repeat(1).take(5).to_list()
        self.assertSequenceEqual([1, 1, 1, 1, 1], ret)
