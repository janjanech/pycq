import unittest

from pycq.q import Q


class TakeSkipLastHaving(unittest.TestCase):
    def test_take_last_having(self):
        ret = Q.range(1, 9).take_last_having(lambda x: x % 2).to_list()

        self.assertSequenceEqual((9, ), ret)

    def test_skip_last_having(self):
        ret = Q.range(1, 9).skip_last_having(lambda x: x % 2).to_list()

        self.assertSequenceEqual((1, 2, 3, 4, 5, 6, 7, 8), ret)
