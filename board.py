from wall import Wall
from box import Box
from goal import Goal
from player import Player
from space import Space


class Board:

    def __init__(self, filename):
        self.rows = []
        with open(filename, 'r') as f:
            read_data = f.read()
        lines = read_data.split('\n')
        lines.pop(0)
        x = 0
        y = 0
        for line in lines:
            row = []
            for char in line:
                if char == '#':
                    row.append(Wall(x, y))
                elif char == '.':
                    row.append(Goal(x, y))
                elif char == '@':
                    row.append(Player(x, y, True))
                elif char == '+':
                    row.append(Player(x, y, False))
                elif char == '$':
                    row.append(Box(x, y, False))
                elif char == '*':
                    row.append(Box(x, y, True))
                else:
                    row.append(Space(x, y))
                x += 1
            self.rows.append(row)
            y += 1

    def __str__(self):
        text = ''
        for row in self.rows:
            for item in row:
                text += item.char
            text += '\n'
        return text
