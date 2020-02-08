from domain.IndonesianDotPuzzle import *
from StateSpaceSearchAlgorithm.DFS import *


puzzle = IndonesianDotPuzzle("3 5 50 110100110")

puzzle.generatetreeasadjacencylist()

fileName = "solutiontesting.txt"


f = open(fileName, "w")

for i in range(puzzle.tree):
    f.writelines(puzzle.tree[i])
    print(puzzle.tree[i])
    
f.close()
