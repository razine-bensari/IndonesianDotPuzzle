from collections import defaultdict
class IndonesianDotPuzzle:

    #Using adjacent list structure (dictionary of all nodes. All values of dic are list of children node related to parent node - Key)
    def __init__(self, textLine):
        # self.tree = defaultdict(list)
        textArray = textLine.split()
        self.size = textArray[0]
        self.max_depth = textArray[1]
        self.max_length = textArray[2]
        puzzleArray = textwrap.wrap(textArray[3], self.size)
        self.puzzle = []

        for row in puzzleArray:
            puzzle.append(list(str(row)))
    
    def touch(y, x):

        temp = self.puzzle

        # Always switch the touched value
        temp[y][x] = switch(temp[y][x])

        # Handeling leftmost & rightmost columns
        if y == 0:
            temp[y + self.size][x] = switch(temp[y + self.size][x])
        
        if y == self.size - 1:
            temp[y - self.size][x] = switch(temp[y - self.size][x])
        
        if y != 0 && y != self.size - 1:
            temp[y + self.size][x] = switch(temp[y + self.size][x])
            temp[y - self.size][x] = switch(temp[y - self.size][x])
        
        if x == 0:
            temp[y][x + 1] = switch(temp[y][x + 1])
        
        if x == self.size - 1:
            temp[y][x - 1] = switch(temp[y][x - 1])
        
        if x != 0 && x != self.size - 1:
            temp[y][x + 1] = switch(temp[y][x + 1])
            temp[y][x - 1] = switch(temp[y][x - 1])
        
        return temp



    def switch(val):
        return 1 - val
        

#Node class used for the graph data structure
class Node:
    def __init__(self, costValue, heuristicValue, puzzleState):
        self.puzzleState = puzzleState
        self.costValue = costValue
        self.heuristicValue = heuristicValue