import sys
from sokoban import Sokoban
from spot import Spot

L = Spot(-1, 0)
R = Spot(1, 0)
U = Spot(0, -1)
D = Spot(0, 1)

s = Sokoban()
b = s.new_board('puzzles/easy1.txt')
s.bfs(b)

# moves = b.moves_available()
# b.move(L)
# print 'PLAYER:',str(b.player)
# for x in b.boxes:
#     print 'BOX', str(x)
# b.move(L)
# print 'PLAYER:',str(b.player)
# for x in b.boxes:
#     print 'BOX', str(x)
# b.move(L)
# print 'PLAYER:',str(b.player)
# for x in b.boxes:
#     print 'BOX', str(x)
# for w in b.walls:
#     print w

# print b.player
# gets file from args and plays that puzzle
# if len(sys.argv) == 2:
#     sokoban.play(sys.argv[1])
# else:
    # sokoban.play('puzzles/easy3.txt')
    # sokoban.play('puzzles/easy4.txt')
