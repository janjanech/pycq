import unittest

from pycq.q import Q


class SplitJoin(unittest.TestCase):
    def test_split_words(self):
        data = "hello world"
        ret = Q.split(data, None).to_list()

        self.assertSequenceEqual(["hello", "world"], ret)

    def test_split_words_with_count(self):
        data = "hello my world"
        ret = Q.split(data, None, 1).to_list()

        self.assertSequenceEqual(["hello", "my world"], ret)

    def test_join(self):
        data = ["hello", "world"]
        ret = Q(data).join(" and ")

        self.assertEqual("hello and world", ret)
