# $   (dollar)    Box on floor
# *   (asterisk)  Box on goal


class Box:

    ''' box with coordinates and on goal/on floor state '''

    def __init__(self, x, y, b):
        self.x = x
        self.y = y
        self.placed = b
        if self.placed == True:
            self.char = '*'
        else:
            self.char = '$'
    def update(self, x, y):
        self.x = x
        self.y = y
