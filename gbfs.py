from time import time
from copy import deepcopy
import heapq


def print_results(board, gen, rep, fri, expl, dur):
    print "\n4. Greedy best first search"
    print "Solution: " + board.getDirections()
    print "Nodes generated: " + str(gen)
    print "Nodes repeated: " + str(rep)
    print "Fringe nodes: " + str(fri)
    print "Explored nodes: " + str(expl)
    print 'Duration: ' + str(dur) + ' secs'


def gbfs(board):
    start = time()
    nodes_generated = 0
    nodes_repeated = 0
    if board.is_win():
        end = time()
        print_results(board, 1, 0, 0, 1, end - start)
        return board
    node = deepcopy(board)
    nodes_generated += 1
    frontier = []
    frontierSet = set()
    heapq.heappush(frontier, node)
    frontierSet.add(node)
    explored = set()
    keepLooking = True
    while keepLooking:
        if len(frontier) == 0:
            print "Solution not found"
            return
        else:
            currNode = heapq.heappop(frontier)
            frontierSet.remove(currNode)
            if currNode.is_win():
                end = time()
                print_results(currNode, nodes_generated, nodes_repeated, len(
                              frontier), len(explored), end - start)
                return currNode
            moves = currNode.moves_available()
            currNode.fboxes = frozenset(currNode.boxes)
            explored.add(currNode)
            for m in moves:
                child = deepcopy(currNode)
                nodes_generated += 1
                child.move(m)
                if child.is_win():
                    end = time()
                    print_results(child, nodes_generated, nodes_repeated, len(
                                  frontier), len(explored), end - start)
                    return child
                if child not in explored:
                    if child not in frontierSet:
                        heapq.heappush(frontier, child)
                        frontierSet.add(child)
                elif child in frontierSet:
                    count = frontier.count(child)
                    i = 0
                    while i <= count:
                        a = frontier.pop((frontier.index(child)))
                        if child.cost < a.cost:
                            heapq.heappush(frontier, child)
                            child = a
                            i = count + 1
                        else:
                            heapq.heappush(frontier, a)
                            i += 1
                    nodes_repeated += 1
