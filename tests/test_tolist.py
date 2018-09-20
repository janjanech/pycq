import unittest

from pycq.q import Q


class ToList(unittest.TestCase):
    def test_tuple(self):
        data = (1, 2, 3)
        ret = Q(data).to_list()

        self.assertIsInstance(ret, list)
        self.assertSequenceEqual(ret, data)

    def test_generator(self):
        data = (i for i in range(10))

        ret = Q(data).to_list()

        self.assertIsInstance(ret, list)
        self.assertSequenceEqual(ret, list(range(10)))
