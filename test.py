import sys
from sokoban import Sokoban

'''
Tests search algos
Handles command line and user input
'''


def runSearch(s, filename, option):
    ''' Runs the search based on filename and option selected '''
    b = s.new_board(filename)
    print '\nSolving ' + filename + '...'
    s.doSearches(b, option)

sok = Sokoban()

print "Which algorithm?"
print "1) Breadth first search"
# print "2) Depth first search"
print "3) Uniform cost search"
# print "4) Greedy best first search"
# print "5) A* search"
print "6) all"
p = raw_input("Type a number and press enter: ")
option = int(p)

# gets file from args and plays that puzzle
if len(sys.argv) == 2:
    runSearch(sok, sys.argv[1], option)
else:
    runSearch(sok, 'puzzles/easy1.txt', option)
    runSearch(sok, 'puzzles/easy3.txt', option)
    runSearch(sok, 'puzzles/mod1.txt', option)
