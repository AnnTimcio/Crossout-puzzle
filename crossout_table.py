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
import string


class CrossoutTable:
    def __init__(self, width=20, height=10):
        self.W = width
        self.H = height
        self.t = []
        for _ in range(self.H):
            row = [' '] * self.W
            self.t.append(row)

    def add(self, x, y, word, dir):
        if dir == 'nw':
            self.add_nw(x, y, word)

        elif dir == 'e':
            self.add_e(x, y, word)

        elif dir == 'n':
            self.add_n(x, y, word)

        elif dir == 'ne':
            self.add_ne(x, y, word)

        elif dir == 'se':
            self.add_se(x, y, word)

        elif dir == 's':
            self.add_s(x, y, word)

        elif dir == 'w':
            self.add_w(x, y, word)

        elif dir == 'sw':
            self.add_sw(x, y, word)

    def add_e(self, x, y, word):
        z = 0
        for c in word:
            if x + z < self.W:
                self.t[y][x + z] = c
            z += 1

    def can_add_e(self, x, y, word):
        z = 0
        for c in word:
            if x + z < self.W:
                if self.t[y][x + z] != ' ' and self.t[y][x + z] != c:
                    return False
            z += 1
        return True

    def add_n(self, x, y, word):
        z = 0
        for c in word:
            if y + z >= 0:
                self.t[y + z][x] = c
            z -= 1

    def can_add_n(self, x, y, word):
        z = 0
        for c in word:
            if y + z >= 0:
                if self.t[y + z][x] != ' ' and self.t[y + z][x] != c:
                    return False
            z -= 1
        return True

    def add_ne(self, x, y, word):
        z = 0
        a = 0
        for c in word:
            if x + z < self.W and y + a >= 0:
                self.t[y + a][x + z] = c
            a -= 1
            z += 1

    def can_add_ne(self, x, y, word):
        z = 0
        a = 0
        for c in word:
            if x + z < self.W and y + a >= 0:
                if self.t[y + a][x + z] != ' ' and self.t[y + a][x + z] != c:
                    return False
            a -= 1
            z += 1
        return True

    def add_se(self, x, y, word):
        z = 0
        a = 0
        for c in word:
            if x + z < self.W and y + a < self.H:
                self.t[y + a][x + z] = c
            z += 1
            a += 1

    def can_add_se(self, x, y, word):
        z = 0
        a = 0
        for c in word:
            if x + z < self.W and y + a < self.H:
                if self.t[y + a][x + z] != ' ' and self.t[y + a][x + z] != c:
                    return False
            z += 1
            a += 1
        return True

    def add_s(self, x, y, word):
        z = 0
        for c in word:
            if y + z <= self.H:
                self.t[y + z][x] = c
            z += 1

    def can_add_s(self, x, y, word):
        z = 0
        for c in word:
            if y + z <= self.H:
                if self.t[y + z][x] != ' ' and self.t[y + z][x] != c:
                    return False
            z += 1
        return True

    def add_sw(self, x, y, word):
        z = 0
        a = 0
        for c in word:
            if x + z >= 0 and y + a < self.H:
                self.t[y + a][x + z] = c
            z -= 1
            a += 1

    def can_add_sw(self, x, y, word):
        z = 0
        a = 0
        for c in word:
            if x + z >= 0 and y + a < self.H:
                if self.t[y + a][x + z] != ' ' and self.t[y + a][x + z] != c:
                    return False
            z -= 1
            a += 1
        return True

    def add_w(self, x, y, word):
        z = 0
        for c in word:
            if x + z >= 0:
                self.t[y][x + z] = c
            z -= 1

    def can_add_w(self, x, y, word):
        z = 0
        for c in word:
            if x + z >= 0:
                if self.t[y][x + z] != ' ' and self.t[y][x + z] != c:
                    return False
            z -= 1
        return True

    def add_nw(self, x, y, word):
        z = 0
        a = 0
        for c in word:
            if x + z >= 0 and a + y >= 0:
                self.t[y + a][x + z] = c
            z -= 1
            a -= 1

    def can_add_nw(self, x, y, word):
        z = 0
        a = 0
        for c in word:
            if x + z >= 0 and a + y >= 0:
                if self.t[y + a][x + z] != ' ' and self.t[y + a][x + z] != c:
                    return False
            z -= 1
            a -= 1
        return True

    def to_string(self):
        table = '**'
        for n in range(self.W):
            table += "*"
        table += "\n"
        for i in range(self.H):
            table += f"*{''.join(self.t[i])}*\n"
        for n in range(self.W):
            table += "*"
        table += "**"
        return table

    def is_full(self):
        for r in self.t:
            if any(element == ' ' for element in r):
                return False

        return True

    def fill_with_random(self):
        for r in self.t:
            if any(element == ' ' for element in r):
                for x in range(0, self.W):
                    if r[x] == ' ':
                        r[x] = random.choice(string.ascii_letters.lower())

    def count_letters(self):
        letters = 0
        for r in self.t:
            for c in r:
                if c != ' ':
                    letters += 1
        return letters


