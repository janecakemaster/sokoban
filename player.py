# @   (at)        Player on floor
# +   (plus)      Player on goal


class Player:

    ''' player with coordinates and on floor/on goal state '''

    def __init__(self, x, y, b):
        self.x = x
        self.y = y
        self.floor = b
        if self.floor == True:
            self.char = '@'
        else:
            self.char = '+'
    def update(self, x, y):
        self.x = x
        self.y = y
