import unittest
from collections import deque

from pycq.q import Q


class ToList(unittest.TestCase):
    def test_tuple(self):
        data = (1, 2, 3)
        ret = Q(data).to_deque()

        self.assertIsInstance(ret, deque)
        self.assertSequenceEqual(ret, data)

    def test_generator(self):
        data = (i for i in range(10))

        ret = Q(data).to_deque()

        self.assertIsInstance(ret, deque)
        self.assertSequenceEqual(ret, list(range(10)))

    def test_max_length(self):
        data = (i for i in range(100))

        ret = Q(data).to_deque(5)

        self.assertIsInstance(ret, deque)
        self.assertSequenceEqual(ret, [95, 96, 97, 98, 99])
