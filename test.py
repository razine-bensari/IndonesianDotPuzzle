from domain.IndonesianDotPuzzle import *
from StateSpaceSearchAlgorithm.DFS import *


def insertSolutionQuickToFind():
    # For testing purposes: incorporating a quick to find solution
    for i, lst in enumerate(puzzle1.tree[3][8].puzzlestate):
        for j in range(puzzle1.size):
            lst[j] = 0


# print("\n- - - - - - - - START OF PUZZLE 1 TEST - - - - - - - -\n")
# puzzle1 = IndonesianDotPuzzle("3 4 100 111001011")
# puzzle1.generatetreeasadjacencylist()

# For testing purposes: incorporating a quick to find solution
#insertSolutionQuickToFind()

# DFS(puzzle1.tree, puzzle1.max_depth, puzzle1.size, puzzle1.rootnode, puzzle1.maxnodenumber, 1)
# print("\n- - - - - - - - END OF PUZZLE 1 SEARCH TEST- - - - - - - -\n")

# print("\n- - - - - - - - START OF PUZZLE 0 TEST - - - - - - - -\n")
# puzzle0 = IndonesianDotPuzzle(testpuzzle0.rstrip('\n'))
# puzzle0.generatetreeasadjacencylist()
# DFS(puzzle0.tree, puzzle0.max_depth, puzzle0.size, puzzle0.rootnode, puzzle0.maxnodenumber, 0)
# print("\n- - - - - - - - END OF PUZZLE 0 SEARCH - - - - - - - -\n")

print("\n- - - - - - - - START OF PUZZLE 1 TEST - - - - - - - -\n")
puzzle1 = IndonesianDotPuzzle("3 4 100 111001011")
puzzle1.generatetreeasadjacencylist()
DFS(puzzle1.tree, puzzle1.max_depth, puzzle1.size, puzzle1.rootnode, puzzle1.maxnodenumber, 1)
print("\n- - - - - - - - END OF PUZZLE 1 SEARCH - - - - - - - -\n")
