from wall import Wall
from box import Box
from goal import Goal
from player import Player
from space import Space


class Board:

    def __init__(self, filename):
        self.walls, self.boxes, self.goals, self.spaces, self.rows = (
            [] for i in range(5))
        with open(filename, 'r') as f:
            read_data = f.read()
            lines = read_data.split('\n')
            self.height = lines.pop(0)
            x = 0
            y = 0
            self.width = 0
            player_found = False
            for line in lines:
                row = []
                for char in line:
                    if char == '#':
                        w = Wall(x, y)
                        row.append(w)
                        self.walls.append(w)
                    elif char == '.':
                        g = Goal(x, y)
                        row.append(g)
                        self.goals.append(g)
                    elif char == '@':
                        self.p = Player(x, y, True)
                        row.append(self.p)
                        player_found = True
                    elif char == '+':
                        self.p = Player(x, y, False)
                        row.append(self.p)
                        player_found = True
                    elif char == '$':
                        b = Box(x, y, False)
                        row.append(b)
                        self.boxes.append(b)
                    elif char == '*':
                        b = Box(x, y, True)
                        row.append(b)
                        self.boxes.append(b)
                    else:
                        s = Space(x, y)
                        row.append(s)
                        self.spaces.append(s)
                    x += 1
                if len(row) > self.width:
                    self.width = len(row)
                self.rows.append(row)
                y += 1
            if player_found == False:
                self.rows = []
                print "no player found on this board"

    def at(self, x, y):
        return self.rows[x][y]

    def moves_available(self):

        return

    def moves(self):
        return

    def __str__(self):
        text = ''
        for row in self.rows:
            for item in row:
                text += item.char
            text += '\n'
        return text

