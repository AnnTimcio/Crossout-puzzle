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
import random

from crossout_table import CrossoutTable


class Engine:

    def __init__(self):
        self.table = CrossoutTable()
        self.TRIES = 20

    def _try_add(self, word):
        pos_dir = ['n','w','e','s','nw','ne','se','sw']
        x = random.randint(0, self.table.W)
        y = random.randint(0, self.table.H)
        dire = random.choice(pos_dir)
        i = self._can_add(x, y, word, dire)
        if i:
            self.table.add(x, y, word, dire)
        return i

    def add(self, word):
        for t in range(self.TRIES):
            if self._try_add(word):
                return True
        return False


    def _can_add(self, x, y, word, direction):
        if direction == 'nw' or direction == 'w' or direction == 'sw':
            if len(word) > x + 1:
                logging.debug('no room left')
                return False
        if direction == 'sw' or direction == 's' or direction == 'se':
            if len(word) + y > self.table.H:
                logging.debug('no room bottom')
                return False
        if direction == 'se' or direction == 'e' or direction == 'ne':
            if len(word) + x > self.table.W:
                logging.debug('no room right')
                return False
        if direction == 'ne' or direction == 'n' or direction == 'nw':
            if len(word) > y + 1:
                logging.debug('no room top')
                return False

        if direction == 'e':
            return self.table.can_add_e(x, y, word)

        if direction == 's':
            return self.table.can_add_s(x, y, word)

        if direction == 'w':
            return self.table.can_add_w(x, y, word)

        if direction == 'n':
            return self.table.can_add_n(x, y, word)

        if direction == 'sw':
            return self.table.can_add_sw(x, y, word)

        if direction == 'se':
            return self.table.can_add_se(x, y, word)

        if direction == 'ne':
            return self.table.can_add_ne(x, y, word)

        if direction == 'nw':
            return self.table.can_add_nw(x, y, word)

        return True

    def count_letters(self):
        l = 0
        for c in self.table.t:
            if c != ' ':
                l += 1
        return l