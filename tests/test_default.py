import unittest

from pycq.q import Q


class Default(unittest.TestCase):
    def test_default_on_empty(self):
        data = ()
        ret = Q(data).default_if_empty("default").to_tuple()

        self.assertEqual(("default", ), ret)

    def test_default_on_non_empty(self):
        data = ("foo", "bar")
        ret = Q(data).default_if_empty("default").to_tuple()

        self.assertEqual(("foo", "bar"), ret)
