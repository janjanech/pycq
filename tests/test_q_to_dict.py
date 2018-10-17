import unittest

from pycq.q import Q


class QToDict(unittest.TestCase):
    def test_q_to_dict(self):
        data = {'h': ['hi', 'hello'], 'f': ['foo']}
        ret = Q(data).to_dict(lambda x: x.key, lambda x: Q(x.value).count())

        self.assertDictEqual({'h': 2, 'f': 1}, ret)
