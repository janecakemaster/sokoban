from spot import Spot


class Direction:

    def __init__(self, sp, char):
        self.sp = sp
        self.char = char

    def __str__(self):
        return self.char
