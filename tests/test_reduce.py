import unittest

from q import Q


class Reduce(unittest.TestCase):
    def test_with_initializer(self):
        data = (1, 2, 3)
        ret = Q(data).reduce([], lambda a, b: a + [b])

        self.assertSequenceEqual(data, ret)

    def test_without_initializer(self):
        data = (1, 2, 3)
        ret = Q(data).reduce(lambda a, b: a + b)

        self.assertEqual(6, ret)
