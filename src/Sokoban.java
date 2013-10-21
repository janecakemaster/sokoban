public class Sokoban {

	// function BREADTH-FIRST-SEARCH(problem) returns a solution, or failure
	public void bfs() {

	}
	// node <- a node with STATE = problem.INITIAL-STATE, PATH-COST = 0 if
	// problem.GOAL-TEST(node.STATE) then return SOLUTION(node) frontier <- a
	// FIFO queue with node as the only element
	// explored <- an empty set
	// loop do
	// if EMPTY?(frontier) then return failure
	// node<-POP(frontier) /*choosestheshallowestnodeinfrontier */ add
	// node.STATE to explored
	// for each action in problem.ACTIONS(node.STATE) do
	// child <-CHILD-NODE(problem,node,action)
	// if child.STATE is not in explored or frontier then
	// if problem.GOAL-TEST(child.STATE) then return SOLUTION(child)
	// frontier <-INSERT(child,frontier)
}
