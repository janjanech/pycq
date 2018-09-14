import unittest
from itertools import zip_longest

from q import Q


class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = (1, 2, 3)
        ret = Q(data)
        self.assertTrue(all(a == b for a, b in zip_longest(data, ret)))
