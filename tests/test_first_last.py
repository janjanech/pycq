import unittest

from q import Q


class FirstLast(unittest.TestCase):
    def test_first(self):
        data = [1, 2, 3]
        ret = Q(data).first()

        self.assertEqual(1, ret)

    def test_first_or_default(self):
        data = [1, 2, 3]
        ret = Q(data).first_or_default(0)

        self.assertEqual(1, ret)

    def test_first_on_empty(self):
        data = []
        self.assertRaises(ValueError, lambda: Q(data).first())

    def test_first_or_default_on_empty(self):
        data = []
        ret = Q(data).first_or_default(0)

        self.assertEqual(0, ret)

    def test_last(self):
        data = [1, 2, 3]
        ret = Q(data).last()

        self.assertEqual(3, ret)

    def test_last_or_default(self):
        data = [1, 2, 3]
        ret = Q(data).last_or_default(0)

        self.assertEqual(3, ret)

    def test_last_on_empty(self):
        data = []
        self.assertRaises(ValueError, lambda: Q(data).last())

    def test_last_or_default_on_empty(self):
        data = []
        ret = Q(data).last_or_default(0)

        self.assertEqual(0, ret)
