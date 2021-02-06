
from unittest import TestCase

from utils import lists


class TestPersian(TestCase):
    def test_convert_digits(self):
        self.assertEqual(list(lists.chunks([0, 1, 2, 3], 2)), [[0, 1], [2, 3]])
        self.assertEqual(list(lists.chunks([0], 2)), [[0]])
