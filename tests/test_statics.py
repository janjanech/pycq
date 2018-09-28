import unittest

from pycq.q import Q


class Statics(unittest.TestCase):
    def test_empty(self):
        self.assertSequenceEqual(Q.empty().to_list(), [])

    def test_range(self):
        self.assertSequenceEqual(Q.range(1, 10).to_list(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_repeat_with_count(self):
        self.assertSequenceEqual(Q.repeat('A', 5).to_list(), ['A', 'A', 'A', 'A', 'A'])

    def test_infinite_iterate(self):
        self.assertSequenceEqual(
            [1, 10, 100, 1000],
            Q.iterate(1, lambda x: x*10).take_while(lambda x: x < 2000).to_list()
        )

    def test_infinite_count(self):
        self.assertSequenceEqual(
            [1, 2, 3, 4, 5],
            Q.count(1).take(5).to_list()
        )

    def test_infinite_repeat(self):
        self.assertSequenceEqual(
            [1, 1, 1, 1, 1],
            Q.repeat(1).take(5).to_list()
        )
