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

    def test_to_string_1_word_e(self):
        ct = CrossoutTable()
        ct.add_e(2, 2, "kot")
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

    def test_to_string_word_cut_e(self):
        ct = CrossoutTable()
        ct.add_e(18, 2, "kotek")
        self.assertEqual("""\
**********************
*                    *
*                    *
*                  ko*
*                    *
*                    *
*                    *
*                    *
*                    *
*                    *
*                    *
**********************""", ct.to_string())

    def test_to_string_1_word_n(self):
        ct = CrossoutTable()
        ct.add_n(5, 2, "kot")
        self.assertEqual("""\
**********************
*     t              *
*     o              *
*     k              *
*                    *
*                    *
*                    *
*                    *
*                    *
*                    *
*                    *
**********************""", ct.to_string())

    def test_to_string_1_word_ne(self):
        ct = CrossoutTable()
        ct.add_ne(4, 9, "pieckaflowy")
        self.assertEqual("""\
**********************
*             w      *
*            o       *
*           l        *
*          f         *
*         a          *
*        k           *
*       c            *
*      e             *
*     i              *
*    p               *
**********************""", ct.to_string())

    def test_to_string_1_word_se(self):
        ct = CrossoutTable()
        ct.add_se(5, 2, "kot")
        self.assertEqual("""\
**********************
*                    *
*                    *
*     k              *
*      o             *
*       t            *
*                    *
*                    *
*                    *
*                    *
*                    *
**********************""", ct.to_string())

    def test_to_string_1_word_s(self):
        ct = CrossoutTable()
        ct.add_s(5, 2, "kot")
        self.assertEqual("""\
**********************
*                    *
*                    *
*     k              *
*     o              *
*     t              *
*                    *
*                    *
*                    *
*                    *
*                    *
**********************""", ct.to_string())

    def test_to_string_1_word_sw(self):
        ct = CrossoutTable()
        ct.add_sw(7, 2, "kot")
        self.assertEqual("""\
**********************
*                    *
*                    *
*       k            *
*      o             *
*     t              *
*                    *
*                    *
*                    *
*                    *
*                    *
**********************""", ct.to_string())

    def test_to_string_1_word_w(self):
        ct = CrossoutTable()
        ct.add_w(11, 2, "kot")
        self.assertEqual("""\
**********************
*                    *
*                    *
*         tok        *
*                    *
*                    *
*                    *
*                    *
*                    *
*                    *
*                    *
**********************""", ct.to_string())

    def test_to_string_1_word_nw(self):
        ct = CrossoutTable()
        ct.add_nw(9, 5, "kot")
        self.assertEqual("""\
**********************
*                    *
*                    *
*                    *
*       t            *
*        o           *
*         k          *
*                    *
*                    *
*                    *
*                    *
**********************""", ct.to_string())
