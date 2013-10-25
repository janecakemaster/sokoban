from spot import Spot


L = Spot(-1, 0)
R = Spot(1, 0)
U = Spot(0, -1)
D = Spot(0, 1)
directions = [U, D, L, R]


class Board:

    def __init__(self):
        self.walls = set()
        self.goals = set()
        self.boxes = set()
        self.player = None

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
            if self.player + d not in self.walls:
                if self.player + d in self.boxes:
                    if self.player + d.double() not in self.boxes.union(self.walls):
                        moves.append(d)
                else:
                    moves.append(d)
        return moves

    def move(self, direction):
        p = self.player + direction
        if p in self.boxes:
            self.boxes.remove(p)
            self.boxes.add(self.player)
        self.player = p

    def is_win(self):
        if self.goals.issubset(self.boxes):
            return True
        else:
            return False
