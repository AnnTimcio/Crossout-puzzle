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

from word_dict import WordDict


class TestWordDict(TestCase):
    def test_get_words_n(self):
        wd = WordDict()
        words = wd.get_words(3)
        self.assertEqual(3, len(words))

    def test_get_words_different(self):
        wd = WordDict()
        words = wd.get_words(5)
        self.assertTrue(len(words) == len(set(words)))