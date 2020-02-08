from collections import defaultdict
import textwrap

class IndonesianDotPuzzle:

    #Using adjacent list structure (dictionary of all nodes. All values of dic are list of children node related to parent node - Key)
    def __init__(self, textLine):
        self.tree = defaultdict(list)
        self.textArray = textLine.split()
        self.size = self.textArray[0]
        self.max_depth = self.textArray[1]
        self.max_length = textArray[2]
        self.puzzleArray = textwrap.wrap(textArray[3], self.size)
        self.puzzle = []

        for row in puzzleArray:
            puzzle.append(list(str(row)))
    
    def touch(self, y, x, puzzleState):

        self.temp = puzzleState

        # Always switch the touched value
        self.temp[y][x] = self.switch(self.temp[y][x])

        # Handeling leftmost & rightmost columns
        if y == 0:
            self.temp[y + self.size][x] = self.switch(self.temp[y + self.size][x])
        
        if y == self.size - 1:
            self.temp[y - self.size][x] = self.switch(self.temp[y - self.size][x])
        
        if y != 0 && y != self.size - 1:
            self.temp[y + self.size][x] = self.switch(self.temp[y + self.size][x])
            self.temp[y - self.size][x] = self.switch(self.temp[y - self.size][x])
        
        if x == 0:
            self.temp[y][x + 1] = self.switch(self.temp[y][x + 1])
        
        if x == self.size - 1:
            self.temp[y][x - 1] = self.switch(self.temp[y][x - 1])
        
        if x != 0 && x != self.size - 1:
            self.temp[y][x + 1] = self.switch(self.temp[y][x + 1])
            self.temp[y][x - 1] = self.switch(self.temp[y][x - 1])
        
        return self.temp

    def switch(self, val):
        return 1 - val

    def generateTreeAsAdjacencyList(self):

        self.root = Node(0, 0, 0, self.puzzle)
        self.currentNode = self.root

        self.nodeCounter = 1
        self.counter = 0

        self.numOfChildren = self.size * self.size
        self.maxNodeNumber = (self.numOfChildren)^self.max_depth


        while self.nodeCounter < self.maxNodeNumber:
            #childrenListSpace, nodeCounter = generateChildrenFromNode(currentNode, nodeCounter)
            for i in range(self.numOfChildren):
                self.tempChildList, self.nodeCounter = self.generateChildrenFromNode(self, self.currentNode, self.nodeCounter)
                self.tree[self.counter].extend(self.tempChildList)
                self.currentNode = self.tree[self.counter//self.numOfChildren][i]
                self.counter++

    def generateChildrenFromNode(self, parentNode, nodeCounter):
        self.childrenList = []
        for i in range(self.size):
                for j in range(self.size):
                    self.childrenList.append(Node(0, 0, 0, touch(y, x, parentNode.puzzleState)))
                    self.nodeCounter++
        return self.childrenList, self.nodeCounter



#Node class used for the graph data structure
class Node:
    def __init__(self,costValue, heuristicValue,  pathCostValue, puzzleState):
        self.puzzleState = puzzleState
        self.fOfN = pathCostValue
        self.gOfN = costValue
        self.hOfN = heuristicValue