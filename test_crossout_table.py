from unittest import TestCase
from crossout_table import CrossoutTable


class TestCrossoutTable(TestCase):
    def test_to_string_innit(self):
        ct = CrossoutTable()
        self.assertEqual("""\
**********************
*                    *
*                    *
*                    *
*                    *
*                    *
*                    *
*                    *
*                    *
*                    *
*                    *
**********************""", ct.to_string())

    def test_to_string_1word(self):
        ct = CrossoutTable()
        ct.add(2, 2, "kot")
        self.assertEqual("""\
**********************
*                    *
*                    *
*  kot               *
*                    *
*                    *
*                    *
*                    *
*                    *
*                    *
*                    *
**********************""", ct.to_string())
