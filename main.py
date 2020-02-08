from domain.IndonesianDotPuzzle import *
from StateSpaceSearchAlgorithm.DFS import *


puzzle = IndonesianDotPuzzle("3 5 50 110100110")

puzzle.generateTreeAsAdjacencyList()

fileName = "solutiontesting.txt"


f = open(fileName, "w")



f.close()