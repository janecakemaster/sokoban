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
