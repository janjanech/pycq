import unittest

from q import Q


class Skip(unittest.TestCase):
    def test_skip_n(self):
        data = [1, 2, 3, 4, 5, 1, 2, 4, 8, 16, 32]
        ret = Q(data).skip(5).to_list()
        self.assertSequenceEqual((1, 2, 4, 8, 16, 32), ret)

    def test_skip_while(self):
        data = [1, 2, 3, 4, 5, 1, 2, 4, 8, 16, 32]
        ret = Q(data).skip_while(lambda x: x < 5).to_list()
        self.assertSequenceEqual((5, 1, 2, 4, 8, 16, 32), ret)
