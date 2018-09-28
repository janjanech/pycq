import unittest
from collections import deque

from pycq.q import Q


class ToDeque(unittest.TestCase):
    def test_tuple(self):
        data = (1, 2, 3)
        ret = Q(data).to_deque()

        self.assertIsInstance(ret, deque)
        self.assertSequenceEqual(data, ret)

    def test_generator(self):
        data = (i for i in range(10))

        ret = Q(data).to_deque()

        self.assertIsInstance(ret, deque)
        self.assertSequenceEqual(list(range(10)), ret)

    def test_max_length(self):
        data = (i for i in range(100))

        ret = Q(data).to_deque(5)

        self.assertIsInstance(ret, deque)
        self.assertSequenceEqual([95, 96, 97, 98, 99], ret)
