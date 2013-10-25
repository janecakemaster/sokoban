from board import Board
import bfs
import ucs
import dfs
import gbfs
import ass


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
                    elif char == '.':
                        b.add_goal(x, y)
                    elif char == '@':
                        b.set_player(x, y)
                    elif char == '+':
                        b.set_player(x, y)
                        b.add_goal(x, y)
                    elif char == '$':
                        b.add_box(x, y)
                    elif char == '*':
                        b.add_box(x, y)
                        b.add_goal(x, y)
                    x += 1
                y += 1
                x = 0
            if hasattr(b, 'player'):
                return b
            else:
                print "No player on board"
                return None
