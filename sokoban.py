from board import Board


def play(filename):
    ''' checks for valid file and plays the puzzle '''
    # try:
    b = Board(filename)
    print b
    print "Player position: (" + str(b.p.x) + ", " + str(b.p.y) + ")"
    # prompt = "Enter a nubmer: 1) Breadth first search \n2) Depth first search \n3) Uniform cost search \n4) Greedy best first search \n5) A* search"
    # s = int(raw_input(prompt))
    # if s == 1:
    #     bfs(b)
    # elif s == 2:
    #     dfs(b)
    # elif s == 3:
    #     ucs(b)
    # elif s == 4:
    #     gbfs(b)
    # elif s == 5:
    #     astar(b)
    # else:
    #     print "bad prompt"

    # bfs(b)

    # except:
    #     print "file doesn't exist, try again"


def bfs(problem):
    return
# function BREADTH-FIRST-SEARCH(problem) returns a solution, or failure
# node <- a node with STATE = problem.INITIAL-STATE, PATH-COST = 0 if problem.GOAL-TEST(node.STATE) then return SOLUTION(node) frontier <- a FIFO queue with node as the only element
# explored <- an empty set
# loop do
# if EMPTY?(frontier) then return failure
# node<-POP(frontier) /*choosestheshallowestnodeinfrontier */ add node.STATE to explored
# for each action in problem.ACTIONS(node.STATE) do
# child <-CHILD-NODE(problem,node,action)
# if child.STATE is not in explored or frontier then
# if problem.GOAL-TEST(child.STATE) then return SOLUTION(child) frontier
# <-INSERT(child,frontier)


def ucs(problem):
    return
# function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
# node <- a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
# frontier <- a priority queue ordered by PATH-COST, with node as the only element explored <- an empty set
# loop do
# if EMPTY?(frontier) then return failure
# node<-POP(frontier) /*choosesthelowest-costnodeinfrontier */ if problem.GOAL-TEST(node.STATE) then return SOLUTION(node) add node.STATE to explored
# for each action in problem.ACTIONS(node.STATE) do
# child <-CHILD-NODE(problem,node,action)
# if child.STATE is not in explored or frontier then
# frontier <-INSERT(child,frontier)
# else if child.STATE is in frontier with higher PATH-COST then
# replace that frontier node with child


def dfs(problem):
    return
# function DEPTH-LIMITED-SEARCH(problem,limit) returns a solution, or failure/cutoff return RECURSIVE-DLS(MAKE-NODE(problem.INITIAL-STATE),problem,limit)
# function RECURSIVE-DLS(node,problem,limit) returns a solution, or failure/cutoff if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
# else if limit = 0 then return cutoff
# else
# cutoff occurred?<-false
# for each action in problem.ACTIONS(node.STATE) do
# child <-CHILD-NODE(problem,node,action) result<-RECURSIVE-DLS(child,problem,limit -1) if result = cutoff then cutoff occurred ? <- true
# else if result != failure then return result
# if cutoff occurred? then return cutoff else return failure


def gbfs(problem):
    return


def astar(problem):
    return
