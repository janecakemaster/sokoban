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
