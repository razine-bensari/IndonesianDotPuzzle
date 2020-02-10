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
puzzle1 = IndonesianDotPuzzle("3 4 100 111001011")

puzzle1.generatetreeasadjacencylist()


# For testing purposes
# making one solution inside
for i, lst in enumerate(puzzle1.tree[3][8].puzzlestate):
    for j in range(puzzle1.size):
        lst[j] = 0

DFS(puzzle1.tree, puzzle1.max_depth, puzzle1.size, puzzle1.rootnode, puzzle1.maxnodenumber, 1)
print("\n- - - - - - - - END OF PUZZLE 1 SEARCH - - - - - - - -\n")