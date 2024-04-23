class CrossoutTable:
    def __init__(self):
        self.t = [list('                    '),list('                    '),list('                    '),
                  list('                    '),list('                    '),list('                    '),
                  list('                    '),
                  list('                    '),list('                    '),list('                    ')]

    def add(self, x, y, word):
        z=0
        for c in word:
            self.t[y][x+z] = c
            z+=1

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
