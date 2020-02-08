from collections import defaultdict
import textwrap


class IndonesianDotPuzzle:

    def __init__(self, textline):
        self.tree = defaultdict(list)
        self.textArray = textline.split()
        self.size = self.textArray[0]
        self.max_depth = self.textArray[1]
        self.max_length = self.textArray[2]
        self.puzzleArray = textwrap.wrap(self.textArray[3], self.size)
        self.puzzle = []

        for row in self.puzzleArray:
            self.puzzle.append(list(str(row)))
    
    def touch(self, y, x, puzzlestate):

        temp = puzzlestate

        # Always switch the touched value
        temp[y][x] = self.switch(temp[y][x])

        # Handling leftmost & rightmost columns
        if y == 0:
            temp[y + self.size][x] = self.switch(temp[y + self.size][x])
        
        if y == self.size - 1:
            temp[y - self.size][x] = self.switch(temp[y - self.size][x])
        
        if y != 0 and y != self.size - 1:
            temp[y + self.size][x] = self.switch(temp[y + self.size][x])
            temp[y - self.size][x] = self.switch(temp[y - self.size][x])
        
        if x == 0:
            temp[y][x + 1] = self.switch(temp[y][x + 1])
        
        if x == self.size - 1:
            temp[y][x - 1] = self.switch(temp[y][x - 1])
        
        if x != 0 and x != self.size - 1:
            temp[y][x + 1] = self.switch(temp[y][x + 1])
            temp[y][x - 1] = self.switch(temp[y][x - 1])
        
        return temp

    @staticmethod
    def switch(val):
        return 1 - val

    def generatetreeasadjacencylist(self):

        root = Node(0, 0, 0, self.puzzle)
        currentnode = root

        nodecounter = 1
        counter = 0

        numofchildren = self.size * self.size
        maxnodenumber = numofchildren^self.max_depth

        while nodecounter < maxnodenumber:
            for i in range(numofchildren):
                childlist, nodecounter = self.generatechildrenfromnode(currentnode, nodecounter)
                self.tree[counter].extend(childlist)
                currentnode = self.tree[counter//numofchildren][i]
                counter += 1

    def generatechildrenfromnode(self, parentnode, nodecounter):
        childrenlist = []
        for y in range(self.size):
            for x in range(self.size):
                childrenlist.append(Node(0, 0, 0, self.touch(y, x, parentnode.puzzleState)))
                nodecounter += 1
        return childrenlist, nodecounter


class Node:

    def __init__(self, costvalue, heuristicvalue,  pathcostvalue, puzzlestate):
        self.puzzleState = puzzlestate
        self.fOfN = pathcostvalue
        self.gOfN = costvalue
        self.hOfN = heuristicvalue
