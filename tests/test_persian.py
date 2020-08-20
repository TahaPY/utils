from unittest import TestCase

from utils import persian


class TestPersian(TestCase):
    def test_convert_digits(self):
        self.assertEqual(persian.convert_digits("0987654321"), "۰۹۸۷۶۵۴۳۲۱")
        self.assertEqual(persian.convert_digits("0987654321 abc"), "۰۹۸۷۶۵۴۳۲۱ abc")
        self.assertIsInstance(persian.convert_digits("0987654321 abc"), str)
