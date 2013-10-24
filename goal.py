# .   (period)    Empty goal


class Goal:

    ''' goal with coordinates '''

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = '.'
    def update(self, x, y):
        self.x = x
        self.y = y
