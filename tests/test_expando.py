import unittest

from pycq.expando import Expando


class ExpandoObject(unittest.TestCase):
    def test_creation(self):
        obj = Expando(attr1=5, attr2=8)

        self.assertEqual(5, obj.attr1)
        self.assertEqual(8, obj.attr2)

    def test_setting_attribute(self):
        obj = Expando(attr1=5, attr2=8)

        def foo():
            obj.attr3 = 20

        self.assertRaises(AttributeError, foo)

    def test_setting_existing_attribute(self):
        obj = Expando(attr1=5, attr2=8)

        def foo():
            obj.attr1 = 20

        self.assertRaises(AttributeError, foo)

    def test_deleting_attribute(self):
        obj = Expando(attr1=5, attr2=8)

        def foo():
            del obj.attr1

        self.assertRaises(AttributeError, foo)

    def test_with(self):
        obj = Expando(attr1=5).__with__(attr2=8)

        self.assertEqual(5, obj.attr1)
        self.assertEqual(8, obj.attr2)
