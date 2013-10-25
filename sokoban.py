from board import Board


class Sokoban:

    def new_board(self, filename):
        b = Board()
        with open(filename, 'r') as f:
            read_data = f.read()
            lines = read_data.split('\n')
            height = lines.pop(0)
            x = 0
            y = 0
            for line in lines:
                for char in line:
                    if char == '#':
                        b.add_wall(x, y)
                        # print "Wall added"
                    elif char == '.':
                        b.add_goal(x, y)
                        # print "Goal added"
                    elif char == '@':
                        b.set_player(x, y)
                        # print "Player located"
                    elif char == '+':
                        b.set_player(x, y)
                        b.add_goal(x, y)
                        # print "Player located"
                        # print "goal added"
                    elif char == '$':
                        b.add_box(x, y)
                        # print "box added"
                    elif char == '*':
                        b.add_box(x, y)
                        b.add_goal(x, y)
                        # print "box added"
                        # print "goal added"
                    x += 1
                y += 1
                x = 0
            if hasattr(b, 'player'):
                return b
            else:
                print "No player on board"
                return None
