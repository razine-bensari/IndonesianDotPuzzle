from domain.IndonesianDotPuzzle import *
from StateSpaceSearchAlgorithm.DFS import *


testfilename = "test.txt"

f = open(testfilename, "r")

testpuzzle0 = f.readline()
testpuzzle0 = testpuzzle0.rstrip()
testpuzzle1 = f.readline()
testpuzzle1 = testpuzzle1.rstrip()
print(testpuzzle0)
print(testpuzzle1)


# print("\n- - - - - - - - START OF PUZZLE 0 - - - - - - - -\n")
# puzzle0 = IndonesianDotPuzzle(testpuzzle0.rstrip('\n'))
# puzzle0.generatetreeasadjacencylist()
# DFS(puzzle0.tree, puzzle0.max_depth, puzzle0.size, puzzle0.rootnode, puzzle0.maxnodenumber, 0)
# print("\n- - - - - - - - END OF PUZZLE 0 SEARCH - - - - - - - -\n")

print("\n- - - - - - - - START OF PUZZLE 1 - - - - - - - -\n")
puzzle1 = IndonesianDotPuzzle(testpuzzle1.rstrip('\n'))
start = time.time()
puzzle1.generatetreeasadjacencylist()
stop = time.time()

print("Time to generate the tree as adjacency list: " + str((stop - start)))

DFS(puzzle1.tree, puzzle1.max_depth, puzzle1.size, puzzle1.rootnode, puzzle1.maxnodenumber, 1)
print("\n- - - - - - - - END OF PUZZLE 1 SEARCH - - - - - - - -\n")