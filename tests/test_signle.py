import unittest

from pycq.q import Q


class Single(unittest.TestCase):
    def test_single(self):
        data = [1]
        ret = Q(data).single()

        self.assertEqual(1, ret)

    def test_single_or_default(self):
        data = [1]
        ret = Q(data).single_or_default(0)

        self.assertEqual(1, ret)

    def test_single_on_empty(self):
        data = []
        self.assertRaises(ValueError, lambda: Q(data).single())

    def test_single_or_default_on_empty(self):
        data = []
        ret = Q(data).single_or_default(0)

        self.assertEqual(0, ret)

    def test_single_on_multi(self):
        data = [1, 2, 3]
        self.assertRaises(ValueError, lambda: Q(data).single())

    def test_single_or_default_on_multi(self):
        data = [1, 2, 3]
        self.assertRaises(ValueError, lambda: Q(data).single_or_default(0))
