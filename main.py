from domain.IndonesianDotPuzzle import *
from StateSpaceSearchAlgorithm.DFS import *


# testfilename = "test.txt"
#
# f = open(testfilename, "r")
#
# testpuzzle0 = f.readline()
# testpuzzle0 = testpuzzle0.rstrip()
# testpuzzle1 = f.readline()
# testpuzzle1 = testpuzzle1.rstrip()
# testpuzzle2 = f.readline()
# testpuzzle2 = testpuzzle2.rstrip()
# testpuzzle3 = f.readline()
# testpuzzle3 = testpuzzle3.rstrip()
# testpuzzle4 = f.readline()
# testpuzzle4 = testpuzzle4.rstrip()
# testpuzzle5 = f.readline()
# testpuzzle5 = testpuzzle5.rstrip()
# print(testpuzzle0)
# print(testpuzzle1)
# print(testpuzzle2)
# print(testpuzzle3)
# print(testpuzzle4)
# print(testpuzzle5)


# print("\n- - - - - - - - START OF PUZZLE 0 - - - - - - - -\n")
# puzzle0 = IndonesianDotPuzzle(testpuzzle0.rstrip('\n'))
# puzzle0.generatetreeasadjacencylist()
# DFS(puzzle0.tree, puzzle0.max_depth, puzzle0.size, puzzle0.rootnode, puzzle0.maxnodenumber, 0)
# print("\n- - - - - - - - END OF PUZZLE 0 SEARCH - - - - - - - -\n")
#
# # print("\n- - - - - - - - START OF PUZZLE 1 - - - - - - - -\n")
# # puzzle0 = IndonesianDotPuzzle(testpuzzle1.rstrip('\n'))
# # puzzle0.generatetreeasadjacencylist()
# # DFS(puzzle0.tree, puzzle0.max_depth, puzzle0.size, puzzle0.rootnode, puzzle0.maxnodenumber, 1)
# # print("\n- - - - - - - - END OF PUZZLE 1 SEARCH - - - - - - - -\n")
#
# print("\n- - - - - - - - START OF PUZZLE 2 - - - - - - - -\n")
# puzzle0 = IndonesianDotPuzzle(testpuzzle2.rstrip('\n'))
# puzzle0.generatetreeasadjacencylist()
# DFS(puzzle0.tree, puzzle0.max_depth, puzzle0.size, puzzle0.rootnode, puzzle0.maxnodenumber, 2)
# print("\n- - - - - - - - END OF PUZZLE 2 SEARCH - - - - - - - -\n")
#
# print("\n- - - - - - - - START OF PUZZLE 3 - - - - - - - -\n")
# puzzle0 = IndonesianDotPuzzle(testpuzzle3.rstrip('\n'))
# puzzle0.generatetreeasadjacencylist()
# DFS(puzzle0.tree, puzzle0.max_depth, puzzle0.size, puzzle0.rootnode, puzzle0.maxnodenumber, 3)
# print("\n- - - - - - - - END OF PUZZLE 3 SEARCH - - - - - - - -\n")
#
# # print("\n- - - - - - - - START OF PUZZLE 4 - - - - - - - -\n")
# # puzzle0 = IndonesianDotPuzzle(testpuzzle4.rstrip('\n'))
# # puzzle0.generatetreeasadjacencylist()
# # DFS(puzzle0.tree, puzzle0.max_depth, puzzle0.size, puzzle0.rootnode, puzzle0.maxnodenumber, 4)
# # print("\n- - - - - - - - END OF PUZZLE 4 SEARCH - - - - - - - -\n")
#
# print("\n- - - - - - - - START OF PUZZLE 5 - - - - - - - -\n")
# puzzle0 = IndonesianDotPuzzle(testpuzzle5.rstrip('\n'))
# puzzle0.generatetreeasadjacencylist()
# DFS(puzzle0.tree, puzzle0.max_depth, puzzle0.size, puzzle0.rootnode, puzzle0.maxnodenumber, 5)
# print("\n- - - - - - - - END OF PUZZLE 5 SEARCH - - - - - - - -\n")

#puzzle = IndonesianDotPuzzle("3 4 20000 010111010")
puzzle = IndonesianDotPuzzle("3 10 100000 111111111")
puzzle.BFS()

puzzle = IndonesianDotPuzzle("3 4 2000 110110111")
puzzle.BFS()

puzzle = IndonesianDotPuzzle("3 100 2000 011001100")
puzzle.A_star()

puzzle = IndonesianDotPuzzle("3 4 2000 110110111")
puzzle.A_star()


puzzle = IndonesianDotPuzzle("10 2 20000 0000000000000000000000000000000000000000000100000000111000000001000000000000000000000000000000000000")
puzzle.A_star()
