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

    def generateTree():

        listOfNodes = []
        root = Node(0, 0, 0, self.puzzle)
        listOfNodes.append(root)

        nodeCounter = 0
        counter = 0

        maxNodeNumber = (self.size * self.size)^self.max_depth

        while nodeCounter < maxNodeNumber:
            childrenList, nodeCounter = generateChildrenFromNode(listOfNodes[counter], nodeCounter)
            listOfNodes.append(childrenList)
            self.tree[counter].append(childrenList)
            counter++

    


    def generateChildrenFromNode(parentNode, nodeCounter):
        
        listOfChildrenNode = []

        for i in range(self.size):
                for j in range(self.size):
                    nodeCounter++
                    listOfChildrenNode.append(Node(nodeCounter, 0, 0, touch(y, x, parentNode.puzzleState)))
        
        return (listOfChildrenNode, nodeCounter)
                    
            


#Node class used for the graph data structure
class Node:
    def __init__(self,index, costValue, heuristicValue, puzzleState, parentNode):
        self.parentNode = parent
        self.childrenList = []
        self.index = index
        self.puzzleState = puzzleState
        self.costValue = costValue
        self.heuristicValue = heuristicValue