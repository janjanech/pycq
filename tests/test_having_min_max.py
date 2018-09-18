import unittest
from collections import namedtuple

from q import Q


TestObject = namedtuple('TestObject', ['a', 'b'])


class HavingMinMax(unittest.TestCase):
    def test_having_min_one(self):
        data = [TestObject(a=5, b=20), TestObject(a=1, b=10), TestObject(a=1, b=20)]
        ret = Q(data).having_min(lambda x: x.b).to_list()

        self.assertSequenceEqual([data[1]], ret)

    def test_having_min_multiple(self):
        data = [TestObject(a=5, b=20), TestObject(a=1, b=10), TestObject(a=1, b=20)]
        ret = Q(data).having_min(lambda x: x.a).to_list()

        self.assertSequenceEqual([data[1], data[2]], ret)

    def test_having_max_one(self):
        data = [TestObject(a=5, b=20), TestObject(a=1, b=10), TestObject(a=1, b=20)]
        ret = Q(data).having_max(lambda x: x.a).to_list()

        self.assertSequenceEqual([data[0]], ret)

    def test_having_max_multiple(self):
        data = [TestObject(a=5, b=20), TestObject(a=1, b=10), TestObject(a=1, b=20)]
        ret = Q(data).having_max(lambda x: x.b).to_list()

        self.assertSequenceEqual([data[0], data[2]], ret)
