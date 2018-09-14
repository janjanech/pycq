import unittest

from q import Q


class Count(unittest.TestCase):
    def test_sized(self):
        data = ("one", "two", "three")
        ret = Q(data).count()

        self.assertEqual(3, ret)

    def test_unsized(self):
        data = (i for i in range(10))
        ret = Q(data).count()

        self.assertEqual(10, ret)
