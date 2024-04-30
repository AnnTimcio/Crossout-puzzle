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
import logging
from unittest import TestCase

from engine import Engine


class TestEngine(TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)

    def test_can_add_1(self):
        eng = Engine()
        self.assertTrue(eng._can_add(0, 0, 'segregator', 'se'))

    def test_can_add_2(self):
        eng = Engine()
        self.assertFalse(eng._can_add(0, 0, 'oryginalny', 'w'))

    def test_can_add_3(self):
        eng = Engine()
        self.assertFalse(eng._can_add(4, 6, 'kotek', 's'))

    def test_can_add_4(self):
        eng = Engine()
        self.assertFalse(eng._can_add(8, 5, 'aliteracyjni', 'sw'))

    def test_can_add_5(self):
        eng = Engine()
        self.assertTrue(eng._can_add(5, 2, 'fotka', 'se'))

    def test_can_add_6(self):
        eng = Engine()
        self.assertTrue(eng._can_add(12, 3, 'matematyka', 'w'))

    def test_can_add_7(self):
        eng = Engine()
        self.assertTrue(eng._can_add(2, 8, 'winogrono', 'ne'))

    def test_can_add_8(self):
        eng = Engine()
        self.assertFalse(eng._can_add(17, 5, 'kwiaty', 'se'))

    def test_can_add_crossing_1(self):
        eng = Engine()
        eng.table.add(0, 0, 'window', 'e')
        self.assertTrue(eng._can_add(0, 0, 'wind', 's'))

    def test_can_add_crossing_2(self):
        eng = Engine()
        eng.table.add(0, 0, 'window', 'e')
        self.assertFalse(eng._can_add(0, 0, 'red', 's'))

    def test_add_possible(self):
        eng = Engine()
        self.assertTrue(eng.add('noga'))

    def test_add_correct(self):
        eng = Engine()
        eng.add('keel')
        print(eng.table.to_string())
        self.assertEqual(4, eng.table.count_letters())
