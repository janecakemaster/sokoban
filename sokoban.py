from board import Board
import bfs
import ucs


class Sokoban:

    '''
    Sokoban game class
    '''

    def new_board(self, filename):
        ''' Creates new board from file '''
        e = []  # empty solution list
        b = Board(e)
        with open(filename, 'r') as f:  # automatically closes file
            read_data = f.read()
            lines = read_data.split('\n')
            height = lines.pop(0)
            x = 0
            y = 0
            for line in lines:
                for char in line:
                    # adds Spots to board's sets by reading in char
                    if char == '#':
                        b.add_wall(x, y)
                    elif char == '.':
                        b.add_goal(x, y)
                    elif char == '@':
                        b.set_player(x, y)
                    elif char == '+':
                        # player gets its own Spot marker
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
            # check for a board with no player
            if hasattr(b, 'player'):
                return b
            else:
                print "No player on board"
                return None

    def doSearches(self, board, option):
        if option == 1:
            bfs.search(board)
        if option == 2:
            dfs.search(board)
        if option == 3:
            ucs.search(board)
        if option == 4:
            gbfs.search(board)
        if option == 5:
            ass.search(board)
        if option == 6:  # all get executed
            bfs.search(board)
            dfs.search(board)
            ucs.search(board)
            gbfs.search(board)
            ass.search(board)
