import unittest

from pycq.q import Q


class GroupBy(unittest.TestCase):
    def test_unordered(self):
        data = ("one", "two", "three", "opq")
        ret = Q(data)\
            .group_by(lambda x: x[0])\
            .select(lambda x: (x.key, x.items.to_tuple()))\
            .to_set()

        self.assertSetEqual({('o', ('one', 'opq')), ('t', ('two', 'three'))}, ret)

    def test_ordered(self):
        data = ("one", "two", "three", "opq")
        ret = Q(data)\
            .group_by_ordered(lambda x: x[0])\
            .select(lambda x: (x.key, x.items.to_tuple()))\
            .to_list()

        self.assertSequenceEqual([('o', ('one', )), ('t', ('two', 'three')), ('o', ('opq', ))], ret)
