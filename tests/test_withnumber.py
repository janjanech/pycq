import unittest

from q import Q


class WithNumber(unittest.TestCase):
    def test_with_number(self):
        ret = Q.repeat('A', 5).with_number().to_list()
        self.assertSequenceEqual([(0, 'A'), (1, 'A'), (2, 'A'), (3, 'A'), (4, 'A')], ret)
