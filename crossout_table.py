class CrossoutTable:
    def __init__(self):
        self.t = [list('                    '), list('                    '), list('                    '),
                  list('                    '), list('                    '), list('                    '),
                  list('                    '),
                  list('                    '), list('                    '), list('                    ')]


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
            if x + z < 20:
                self.t[y][x + z] = c
            z += 1

    def add_n(self, x, y, word):
        z = 0
        for c in word:
            if x + z >= 0:
                self.t[y + z][x] = c
            z -= 1

    def add_ne(self, x, y, word):
        z = 0
        a = 0
        for c in word:
            if x + z < 20 and y + a >= 0:
                self.t[y + a][x + z] = c
            a -= 1
            z += 1

    def add_se(self, x, y, word):
        z = 0
        a = 0
        for c in word:
            if x + z < 20 and y + a < 10:
                self.t[y + a][x + z] = c
            z += 1
            a += 1

    def add_s(self, x, y, word):
        z = 0
        for c in word:
            if x + z < 20:
                self.t[y + z][x] = c
            z += 1

    def add_sw(self, x, y, word):
        z = 0
        a = 0
        for c in word:
            if x + z >= 0 and y + a < 10:
                self.t[y + a][x + z] = c
            z -= 1
            a += 1

    def add_w(self, x, y, word):
        z = 0
        for c in word:
            if x + z >= 0:
                self.t[y][x + z] = c
            z -= 1

    def add_nw(self, x, y, word):
        z = 0
        a = 0
        for c in word:
            if x + z >= 0 and a + y >= 0:
                self.t[y + a][x + z] = c
            z -= 1
            a -= 1

    def to_string(self):
        return ("**********************\n"
                f"*{''.join(self.t[0])}*\n"
                f"*{''.join(self.t[1])}*\n"
                f"*{''.join(self.t[2])}*\n"
                f"*{''.join(self.t[3])}*\n"
                f"*{''.join(self.t[4])}*\n"
                f"*{''.join(self.t[5])}*\n"
                f"*{''.join(self.t[6])}*\n"
                f"*{''.join(self.t[7])}*\n"
                f"*{''.join(self.t[8])}*\n"
                f"*{''.join(self.t[9])}*\n"
                "**********************")
