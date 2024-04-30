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

import random
class WordDict:

    def __init__(self):
        self.WORDS = ['kot', 'pies', 'suwak', 'piłka', 'nietoperz', 'kubek',
                      'balon', 'lampa', 'firana', 'komputer', 'mysz', 'maj',
                      'drzwi', 'dzwon', 'sklep', 'pomidor', 'czekolada', 'cytryna',
                      'baterie', 'chusta', 'kapusta', 'woda', 'szklanka', 'makaron',
                      'cukier', 'gra', 'mucha', 'susza', 'ucho', 'pusto', 'drabina']

    def get_words(self, n):
        k = random.sample(self.WORDS, n)
        return k
