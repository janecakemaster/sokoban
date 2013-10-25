import sys
from sokoban import Sokoban
from spot import Spot

L = Spot(-1, 0)
R = Spot(1, 0)
U = Spot(0, -1)
D = Spot(0, 1)

s = Sokoban()
b = s.new_board('puzzles/easy1.txt')
