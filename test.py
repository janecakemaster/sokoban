import sys
# from glob import glob
import sokoban

# puzzles = glob('puzzles/*.txt')
# for p in puzzles:
#     print p
#     sokoban.play(p)

# gets file from args and plays that puzzle
if len(sys.argv) == 2:
    sokoban.play(sys.argv[1])
else:
    sokoban.play('puzzles/easy1.txt')
    sokoban.play('puzzles/easy3.txt')
    sokoban.play('puzzles/easy4.txt')