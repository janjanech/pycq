import unittest

from q import Q


class AppendPreped(unittest.TestCase):
    def test_prepend_all(self):
        data = (1, 2, 3)
        data2 = (1, 2, 3)
        ret = Q(data).prepend_all(data2).to_tuple()

        self.assertEqual(data2 + data, ret)

    def test_append_all(self):
        data = (1, 2, 3)
        data2 = (1, 2, 3)
        ret = Q(data).append_all(data2).to_tuple()

        self.assertEqual(data + data2, ret)

    def test_prepend_one(self):
        data = (1, 2, 3)
        ret = Q(data).prepend(5).to_tuple()

        self.assertEqual((5, ) + data, ret)


    def test_append_one(self):
        data = (1, 2, 3)
        ret = Q(data).append(5).to_tuple()

        self.assertEqual(data + (5, ), ret)
