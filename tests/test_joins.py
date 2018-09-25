import unittest
from collections import namedtuple

from pycq.q import Q


TestObject = namedtuple('TestObject', ['a', 'b'])


class InnerGroupedJoin(unittest.TestCase):
    def test_inner_join(self):
        data = ['foo', 'bar', 'over', 'rack', 'kick']
        ret = Q(data)\
            .inner_join(data, lambda x: x[-1], lambda x: x[0])\
            .select(lambda x: (x.left, x.right))\
            .to_set()

        self.assertSetEqual(
            {('foo', 'over'), ('bar', 'rack'), ('over', 'rack'), ('rack', 'kick'), ('kick', 'kick')},
            ret
        )

    def test_group_join(self):
        data = ['foo', 'bar', 'over', 'rack', 'kick']
        ret = Q(data)\
            .group_join(data, lambda x: x[-1], lambda x: x[0])\
            .select(lambda x: (x.left_items.to_frozenset(), x.right_items.to_frozenset()))\
            .to_set()

        self.assertSetEqual(
            {
                (frozenset(('foo', )), frozenset(('over', ))),
                (frozenset(('bar', 'over')), frozenset(('rack', ))),
                (frozenset(('rack', 'kick')), frozenset(('kick', ))),
                (frozenset(), frozenset(('foo',))),
                (frozenset(), frozenset(('bar',))),
            },
            ret
        )
