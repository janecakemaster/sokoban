import sys
from sokoban import Sokoban


def runSearch(s, filename):
    b = s.new_board(filename)
    print '\nSolving ' + filename + '...'
    s.doSearches(b)

sok = Sokoban()

# gets file from args and plays that puzzle
if len(sys.argv) == 2:
    runSearch(sok, sys.argv[1])
else:
    runSearch(sok, 'puzzles/easy1.txt')
    runSearch(sok, 'puzzles/easy3.txt')
    runSearch(sok, 'puzzles/mod1.txt')
