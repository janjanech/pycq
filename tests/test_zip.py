import unittest

from pycq.q import Q


class Zip(unittest.TestCase):
    def test_zip(self):
        ret = Q.range(1, 10).zip(Q.range(5, 5)).to_list()

        self.assertSequenceEqual([(1, 5), (2, 6), (3, 7), (4, 8), (5, 9)], ret)

    def test_zip_longest_no_fill(self):
        ret = Q.range(1, 10).zip_longest(Q.range(5, 5)).to_list()

        self.assertSequenceEqual(
            [(1, 5), (2, 6), (3, 7), (4, 8), (5, 9), (6, None), (7, None), (8, None), (9, None), (10, None)],
            ret
        )

    def test_zip_longest_fill_shorter(self):
        ret = Q.range(1, 10).zip_longest(Q.range(5, 5), fill=0).to_list()

        self.assertSequenceEqual(
            [(1, 5), (2, 6), (3, 7), (4, 8), (5, 9), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0)],
            ret
        )

    def test_zip_longest_fill_longer(self):
        ret = Q.range(1, 5).zip_longest(Q.range(5, 10), fill=0).to_list()

        self.assertSequenceEqual(
            [(1, 5), (2, 6), (3, 7), (4, 8), (5, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14)],
            ret
        )

    def test_zip_longest_fill_left_shorter(self):
        ret = Q.range(1, 10).zip_longest(Q.range(5, 5), fill_left=0).to_list()

        self.assertSequenceEqual(
            [(1, 5), (2, 6), (3, 7), (4, 8), (5, 9), (6, None), (7, None), (8, None), (9, None), (10, None)],
            ret
        )

    def test_zip_longest_fill_right_longer(self):
        ret = Q.range(1, 5).zip_longest(Q.range(5, 10), fill_right=0).to_list()

        self.assertSequenceEqual(
            [(1, 5), (2, 6), (3, 7), (4, 8), (5, 9), (None, 10), (None, 11), (None, 12), (None, 13), (None, 14)],
            ret
        )

    def test_zip_longest_right_shorter(self):
        ret = Q.range(1, 10).zip_longest(Q.range(5, 5), fill_right=0).to_list()

        self.assertSequenceEqual(
            [(1, 5), (2, 6), (3, 7), (4, 8), (5, 9), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0)],
            ret
        )
