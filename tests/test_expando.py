import unittest

from pycq.expando import Expando


class ExpandoObject(unittest.TestCase):
    def test_creation(self):
        obj = Expando(attr1=5, attr2=8)

        self.assertEqual(5, obj.attr1)
        self.assertEqual(8, obj.attr2)
