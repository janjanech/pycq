import unittest

from pycq.q import Q


class Tee(unittest.TestCase):
    def test_tee(self):
        data = iter(range(10))
        q = Q(data)
        ret1 = q.tee().where(lambda x: x < 5).to_list()
        ret2 = q.tee().where(lambda x: x % 2 == 0).to_list()

        self.assertSequenceEqual([0, 1, 2, 3, 4], ret1)
        self.assertSequenceEqual([0, 2, 4, 6, 8], ret2)
