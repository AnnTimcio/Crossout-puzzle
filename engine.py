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

from crossout_table import CrossoutTable


class Engine:

    def __init__(self):
        self.table = CrossoutTable()

    def add(self, word):
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

        return True
