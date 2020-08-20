import unittest

from utils import strings


class TestStrings(unittest.TestCase):
    def test_is_null_or_empty(self):
        self.assertEqual(strings.is_null_or_empty(""), True)
        self.assertEqual(strings.is_null_or_empty(None), True)
        self.assertEqual(strings.is_null_or_empty("Hi"), False)
