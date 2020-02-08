from collections import defaultdict
import textwrap

class IndonesianDotPuzzle:

    #Using adjacent list structure (dictionary of all nodes. All values of dic are list of children node related to parent node - Key)
    def __init__(self, textLine):
        self.tree = defaultdict(list)
        textArray = textLine.split()
        self.size = textArray[0]
        self.max_depth = textArray[1]
        self.max_length = textArray[2]
        puzzleArray = textwrap.wrap(textArray[3], self.size)
        self.puzzle = []

        for row in puzzleArray:
            puzzle.append(list(str(row)))
    
    def touch(y, x, puzzleState):

        temp = puzzleState

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

    def generateTreeAsAdjacencyList():

        root = Node(0, 0, 0, self.puzzle)
        currentNode = root

        nodeCounter = 0
        counter = 0

        maxNodeNumber = (self.size * self.size)^self.max_depth

        while nodeCounter < maxNodeNumber:
            childrenListSpace, nodeCounter = generateChildrenFromNode(currentNode, nodeCounter)
            for i in range(16):
                tempChildList, nodeCounter = generateChildrenFromNode(childrenListSpace[i], nodeCounter)
                self.tree[counter].extend(tempChildList)
                counter++
            
            index = counter//16
            currentNode = self.tree[index][0]

    def generateChildrenFromNode(parentNode, nodeCounter):
        childrenList = []
        for i in range(self.size):
                for j in range(self.size):
                    nodeCounter++
                    childrenList.append(Node(0, 0, 0, touch(y, x, parentNode.puzzleState)))
        return childrenList, nodeCounter
            


#Node class used for the graph data structure
class Node:
    def __init__(self,costValue, heuristicValue,  pathCostValue, puzzleState):
        self.puzzleState = puzzleState
        self.fOfN = pathCostValue
        self.gOfN = costValue
        self.hOfN = heuristicValue