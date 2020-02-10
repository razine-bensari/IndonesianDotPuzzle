from domain.IndonesianDotPuzzle import *
from StateSpaceSearchAlgorithm.DFS import *


puzzle = IndonesianDotPuzzle("3 5 50 110100110")

puzzle.generatetreeasadjacencylist()

# making one solution inside
for i, lst in enumerate(puzzle.tree[3][0].puzzlestate):
        for j in range(puzzle.size):
            lst[j] = 0



DFS(puzzle.tree, puzzle.max_depth, puzzle.size, puzzle.rootnode)


print("end of main.py")