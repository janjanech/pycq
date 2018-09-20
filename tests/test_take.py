import unittest

from pycq.q import Q


class Take(unittest.TestCase):
    def test_take_n(self):
        data = [1, 2, 3, 4, 5, 1, 2, 4, 8, 16, 32]
        ret = Q(data).take(5).to_list()
        self.assertSequenceEqual((1, 2, 3, 4, 5), ret)

    def test_take_while(self):
        data = [1, 2, 3, 4, 5, 1, 2, 4, 8, 16, 32]
        ret = Q(data).take_while(lambda x: x < 5).to_list()
        self.assertSequenceEqual((1, 2, 3, 4), ret)
