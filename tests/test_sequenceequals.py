import unittest

from q import Q


class SequenceEquals(unittest.TestCase):
    def test_same_sequence(self):
        data = [1, 2, 3]

        self.assertTrue(Q(data).sequence_equal((1, 2, 3)))

    def test_shorter_sequence(self):
        data = [1, 2, 3]

        self.assertFalse(Q(data).sequence_equal((1, 2)))

    def test_longer_sequence(self):
        data = [1, 2, 3]

        self.assertFalse(Q(data).sequence_equal((1, 2, 3, 4)))

    def test_different_sequence(self):
        data = [1, 2, 3]

        self.assertFalse(Q(data).sequence_equal((4, 5, 6)))
