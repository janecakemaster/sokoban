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
                        s = Space(x, y)
                        row.append(s)
                        self.spaces.append(s)
                        player_found = True
                    elif char == '+':
                        self.p = Player(x, y, False)
                        g = Goal(x, y)
                        row.append(g)
                        self.goals.append(g)
                        player_found = True
                    elif char == '$':
                        b = Box(x, y, False)
                        row.append(b)
                        self.boxes.append(b)
                    elif char == '*':
                        b = Box(x, y, True)
                        row.append(b)
                        self.boxes.append(b)
                        g = Goal(x, y)
                        self.goals.append(g)
                    else:
                        s = Space(x, y)
                        row.append(s)
                        self.spaces.append(s)
                    x += 1
                if len(row) > self.width:
                    self.width = len(row)
                self.rows.append(row)
                y += 1
                x = 0
            if player_found == False:
                self.rows = []
                print "no player found on this board"
            # self.move_player('u')

            # for row in self.rows:
            #     for item in row:
            #         print item.char

            # print self.rows

            # xp = 0
            # yp = 0
            # while yp < self.height:
            #     while xp < self.width:
            #         print self.at(xp, yp).y
            #         xp += 1
            #     xp = 0
            #     print '\n'
            #     yp += 1

    def at(self, x, y):
        return self.rows[y][x]

    def can_move(self, obj, direction):
        xold = self.p.x
        yold = self.p.y
        if direction == 'u':
            ynew = yold - 1
            obj.y = ynew
            to_move = self.at(xold, ynew)
            kind = type(to_move)
            if kind == Wall:
                return False
            if kind == Goal:
                return True
            if kind == Space:
                return True
            if kind == Box:
                return can_move(to_move, direction)
            # recursive call to find out if adjacent obj can be moved


    def move_player(self, direction):
        # switch position of player object with object in next position
        xold = self.p.x
        yold = self.p.y
        if direction == 'u':
            ynew = yold - 1
            self.p.y = ynew
            to_move = self.at(xold, ynew)
            kind = type(to_move)
            if kind == Box:
                # check if box can move
                move_box(to_move)
            if kind == Goal:
                self.p.floor = False
            if kind == Space:
                self.rows[ynew][xold] = self.p
                self.rows[yold][xold] = Space(xold, yold)

        #     self.p.y = ynew
        #     self.rows[ynew][xold] = self.p
        # print self

    def move_box(self, box, direction):
        xold = box.x
        yold = box.y
        if direction == 'u':
            ynew = yold - 1

            to_move = self.at(xold, ynew)
            kind = type(to_move)
            if kind ==
        return

    def moves_available(self, player):
        x = player.x
        y = player.y
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
