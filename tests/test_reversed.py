import unittest

from q import Q


class Reduce(unittest.TestCase):
    def test_only_reverse(self):
        data = [1, 2, 3]
        ret = Q(data).reverse().to_list()

        self.assertSequenceEqual((3, 2, 1), ret)

    def test_reverse_and_where(self):
        data = (1, 2, 3)
        ret = Q(data).where(lambda x: x > 1).reverse().to_list()

        self.assertSequenceEqual((3, 2), ret)
