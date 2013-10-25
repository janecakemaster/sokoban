Sokoban
=======
**Assignment 2**  
**Jane Kim**  
**jk3316**  

Sokoban game in Python for Artificial Intelligence class. See `assignment.txt` for specs.

#####Specs
OS: Mac OSX  
Language: Python 2.7.1
Editor: Sublime Text 3  


##Testing
* To run test suite and see output in `results.txt`:
```
python test.py > results.txt
```

* To run your own puzzle:
```
python test.py <puzzle filename>
```

##Notes on Implementation

* *Only BFS and UCS are implemented*. The algorithms mostly follow the pseudocode presented in the textbook.
* Please see `results.txt` for the output of the test runs
* I decided to use sets for the board components in order to check for equality very quickly and membership. 
* Explored nodes are also in a set in order to quickly check if a node was already explored; the comparison of board nodes is by the position of boxes and goals.
* I created a custom queue `MyQueue` with some useful overloaded methods for this project.
* Runtime is calculated by subtracting the time at the beginning of function execution to the end using the Python `time` module.
* `copy.deepcopy()` used to create new nodes. Every `deepcopy()` added to the `nodes_generated` counter.
* In general, in each search file, `search()` prints results and returns a board if the search is successful; otherwise, the function terminates.
* `m in moves` used to iterate thorugh moves available (calculated through `Board.moves_available()`)
* Puzzles written up by professor live in `puzzles/`
* For the possible ways to run the program, the optional filename is taken from command line arguments. The option to use different search algos is presented through a command line prompt.
* `heapq` module used in UCS for sorting capabilities and quick retrieval capabilities.
* 