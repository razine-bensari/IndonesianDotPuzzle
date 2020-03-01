from domain.IndonesianDotPuzzle import *

testfilename = "test.txt"

with open(testfilename) as f:
    puzzlestring = f.readlines()

numOfTest = len(puzzlestring)

for i in range(numOfTest):
    print("\n- - - - - - - - START OF PUZZLE " + str(i) + " SEARCH - - - - - - - -\n")
    puzzle = IndonesianDotPuzzle(puzzlestring[i].rstrip('\n'), i)
    puzzle.BFS()
    print("\n- - - - - - - - END OF PUZZLE " + str(i) + " SEARCH - - - - - - - -\n\n\n")

for i in range(numOfTest):
    print("\n- - - - - - - - START OF PUZZLE " + str(i) + " - - - - - - - -\n")
    puzzle = IndonesianDotPuzzle(puzzlestring[i].rstrip('\n'), i)
    puzzle.A_star()
    print("\n- - - - - - - - END OF PUZZLE " + str(i) + " SEARCH - - - - - - - -\n\n\n")

# puzzle = IndonesianDotPuzzle("3 4 100 111001011", 0)
# puzzle.DFS()
