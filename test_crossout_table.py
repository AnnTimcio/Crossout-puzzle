#    Copyright 2024 AnnTimcio
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#  limitations under the License.

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

    def test_to_string_1_word_add1(self):
        ct = CrossoutTable()
        ct.add(9, 5, "kot", 'nw')
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

    def test_to_string_1_word_add2(self):
        ct = CrossoutTable()
        ct.add(1, 0, "1234567890", 's')
        self.assertEqual("""\
**********************
* 1                  *
* 2                  *
* 3                  *
* 4                  *
* 5                  *
* 6                  *
* 7                  *
* 8                  *
* 9                  *
* 0                  *
**********************""", ct.to_string())

    def test_to_string_3_word(self):
        ct = CrossoutTable()
        ct.add(9, 5, "kot", 'nw')
        ct.add(6, 4, "piesek", 'sw')
        ct.add(7, 3, "tamburyno", 'e')
        self.assertEqual("""\
**********************
*                    *
*                    *
*                    *
*       tamburyno    *
*      p o           *
*     i   k          *
*    e               *
*   s                *
*  e                 *
* k                  *
**********************""", ct.to_string())

    def test_to_string_changed_size(self):
        ct = CrossoutTable(3, 3)
        ct.add(2, 2, "kot", 'nw')
        ct.add(0, 0, "tamburyno", 'e')
        self.assertEqual("""\
*****
*tam*
* o *
*  k*
*****""", ct.to_string())

    def test_full(self):
        ct = CrossoutTable(3, 3)
        ct.add(0, 0, "kot", 's')
        ct.add(1, 0, "tok", 's')
        ct.add(2, 0, "kto", 's')
        self.assertEqual("""\
*****
*ktk*
*oot*
*tko*
*****""", ct.to_string())

    def test_is_full(self):
        ct = CrossoutTable(3, 3)
        ct.add(0, 0, "kot", 's')
        ct.add(1, 0, "tok", 's')
        ct.add(2, 0, "kto", 's')
        self.assertTrue(ct.is_full())

    def test_is_not_full(self):
        ct = CrossoutTable(3, 3)
        ct.add(0, 0, "kot", 's')
        ct.add(2, 0, "kto", 's')
        self.assertFalse(ct.is_full())

    def test_fill_with_random(self):
        ct = CrossoutTable(3, 3)
        ct.fill_with_random()
        self.assertTrue(ct.is_full())
