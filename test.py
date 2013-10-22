from glob import glob
import sokoban

# puzzles = glob('puzzles/*.txt')
# for p in puzzles:
#     print p
#     sokoban.play(p)
sokoban.play('puzzles/easy1.txt')
