import copy
from collections import defaultdict
import textwrap


class IndonesianDotPuzzle:

    def __init__(self, textline):
        self.tree = defaultdict(list)
        self.textArray = textline.split()
        self.size = int(self.textArray[0])
        self.max_depth = int(self.textArray[1])
        self.max_length = int(self.textArray[2])
        self.puzzleArray = textwrap.wrap(self.textArray[3], int(self.size))
        self.puzzle = []

        for i, lst in enumerate(self.puzzleArray):
            lst = [int(i) for i in lst]
            self.puzzle.append(lst)

    def touch(self, y, x, puzzlestate):

        temp = copy.deepcopy(puzzlestate)

        # Always switch the touched value
        temp[y][x] = self.switch(temp[y][x])

        # Handling leftmost & rightmost columns
        if y == 0:
            temp[y + 1][x] = self.switch(temp[y + 1][x])
        
        if y == self.size - 1:
            temp[y - 1][x] = self.switch(temp[y - 1][x])
        
        if y != 0 and y != self.size - 1:
            temp[y + 1][x] = self.switch(temp[y + 1][x])
            temp[y - 1][x] = self.switch(temp[y - 1][x])
        
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
        return 1 - int(val)

    def generatetreeasadjacencylist(self):

        root = Node(0, 0, 0, 0, self.puzzle)
        self.rootnode = root
        currentnode = root

        nodecounter = 1
        counter = 0

        numofchildren = int(self.size) * int(self.size)
        maxnodenumber = numofchildren ** int(self.max_depth)

        while nodecounter <= maxnodenumber:
            for i in range(numofchildren):
                childlist, nodecounter = self.generatechildrenfrompuzzlestate(currentnode.puzzlestate, nodecounter)
                self.tree[counter].extend(childlist)
                currentnode = self.tree[counter//numofchildren][i]
                counter += 1

    def generatechildrenfrompuzzlestate(self, parentpuzzlestate, nodecounter):
        childrenlist = []
        puzzlestate = parentpuzzlestate
        for y in range(int(self.size)):
            for x in range(int(self.size)):
                childrenlist.append(Node(int(nodecounter), 0, 0, 0, self.touch(y, x, puzzlestate)))
                nodecounter += 1
        return childrenlist, nodecounter


class Node:

    def __init__(self, index, costvalue, heuristicvalue,  pathcostvalue, puzzlestate):
        self.index = index
        self.puzzlestate = puzzlestate
        self.fOfN = pathcostvalue
        self.gOfN = costvalue
        self.hOfN = heuristicvalue
        self.isvisited = False
