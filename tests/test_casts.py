import unittest

from pycq.q import Q


class Casts(unittest.TestCase):
    def test_cast(self):
        data = [1, 2, 3]
        ret = Q(data).cast(float).to_list()

        self.assertSequenceEqual(ret, [1.0, 2.0, 3.0])
        self.assertTrue(all(isinstance(i, float) for i in ret))

    def test_of_type(self):
        data = [1.0, 2, 3.0]
        ret = Q(data).of_type(float).to_list()

        self.assertSequenceEqual(ret, [1.0, 3.0])
        self.assertTrue(all(isinstance(i, float) for i in ret))
