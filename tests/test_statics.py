import unittest

from pycq.q import Q


class Statics(unittest.TestCase):
    def test_empty(self):
        self.assertSequenceEqual(Q.empty().to_list(), [])

    def test_range(self):
        self.assertSequenceEqual(Q.range(1, 10).to_list(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_repeat_with_count(self):
        self.assertSequenceEqual(Q.repeat('A', 5).to_list(), ['A', 'A', 'A', 'A', 'A'])

    #TODO: test infinite Q.count and Q.repeat
