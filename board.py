from spot import Spot
from direction import Direction

L = Direction(Spot(-1, 0), 'l')
R = Direction(Spot(1, 0), 'r')
U = Direction(Spot(0, -1), 'u')
D = Direction(Spot(0, 1), 'd')
directions = [U, D, L, R]


class Board:

    def __init__(self, dir_list):
        self.dir_list = dir_list
        self.walls = set()
        self.goals = set()
        self.boxes = set()
        self.fboxes = frozenset()
        self.player = None

    def __eq__(self, other):
        if self.boxes.issubset(other.boxes) and self.player == other.player:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.fboxes, self.player))

    def add_wall(self, x, y):
        self.walls.add(Spot(x, y))

    def add_goal(self, x, y):
        self.goals.add(Spot(x, y))

    def add_box(self, x, y):
        self.boxes.add(Spot(x, y))

    def set_player(self, x, y):
        self.player = Spot(x, y)

    def moves_available(self):
        moves = []
        for d in directions:
            if self.player + d.sp not in self.walls:
                if self.player + d.sp in self.boxes:
                    if self.player + d.sp.double() not in self.boxes.union(self.walls):
                        moves.append(d)
                else:
                    moves.append(d)
        return moves

    def move(self, direction):
        p = self.player + direction.sp
        if p in self.boxes:
            self.boxes.remove(p)
            self.boxes.add(p + direction.sp)
        self.player = p
        self.dir_list.append(direction)

    def is_win(self):
        if self.goals.issubset(self.boxes):
            return True
        else:
            return False

    def getDirections(self):
        chars = ''
        for d in self.dir_list:
            chars += d.char
            chars += ', '
        return chars
