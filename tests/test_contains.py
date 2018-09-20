import unittest

from pycq.q import Q


class Contains(unittest.TestCase):
    def test_simple_contains(self):
        data = [1, 2, 3]

        self.assertTrue(Q(data).contains(1))
        self.assertFalse(Q(data).contains(0))

    def test_contains_all(self):
        data = [1, 2, 3]

        self.assertTrue(Q(data).contains_all((1, 2)))
        self.assertFalse(Q(data).contains_all((2, 4)))
        self.assertFalse(Q(data).contains_all((5, 6)))

    def test_contains_any(self):
        data = [1, 2, 3]

        self.assertTrue(Q(data).contains_any((1, 2)))
        self.assertTrue(Q(data).contains_any((2, 4)))
        self.assertFalse(Q(data).contains_any((5, 6)))
