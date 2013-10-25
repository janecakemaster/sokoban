import sys
from sokoban import Sokoban


def runSearch(s, filename):
    b = s.new_board(filename)
    # TODO: uncomment for prod
    # print "Which algorithm?"
    # print "1) Breadth first search"
    # print "2) Depth first search"
    # print "3) Uniform cost search"
    # print "4) Greedy best first search"
    # print "5) A* search"
    # print "6) all"
    # p = raw_input("Type a number and press enter: ")
    # option = int(p)
    option = 3
    print '\nSolving ' + filename + '...'
    s.doSearches(b, option)

sok = Sokoban()

# gets file from args and plays that puzzle
if len(sys.argv) == 2:
    runSearch(sok, sys.argv[1])
else:
    runSearch(sok, 'puzzles/easy1.txt')
    runSearch(sok, 'puzzles/easy3.txt')
    runSearch(sok, 'puzzles/mod1.txt')
