import unittest

from pycq.q import Q


class TakeSkipLast(unittest.TestCase):
    def test_take_last(self):
        ret = Q.range(1, 10).take_last(5).to_list()

        self.assertSequenceEqual((6, 7, 8, 9, 10), ret)

    def test_skip_last(self):
        ret = Q.range(1, 10).skip_last(3).to_list()

        self.assertSequenceEqual((1, 2, 3, 4, 5, 6, 7), ret)
