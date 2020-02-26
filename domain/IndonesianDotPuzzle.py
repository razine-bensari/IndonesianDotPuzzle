import copy
from collections import defaultdict
import textwrap
from queue import PriorityQueue
import time


class IndonesianDotPuzzle:

    def __init__(self, textline):
        self.tree = defaultdict(list)
        self.textArray = textline.split()
        self.size = int(self.textArray[0])
        self.max_depth = int(self.textArray[1])
        self.max_length = int(self.textArray[2])
        self.numofchildren = int(self.size) * int(self.size)
        self.maxnodenumber = self.numofchildren ** int(self.max_depth)
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
        print("GENERATING TREE. . .")
        root = Node(0, 0, 0, 0, self.puzzle)
        self.rootnode = root
        currentnode = root

        nodecounter = 1
        counter = 0

        while nodecounter <= self.maxnodenumber:
            for i in range(self.numofchildren):
                childlist, nodecounter = self.generatechildrenfrompuzzlestate(currentnode.puzzlestate, nodecounter)
                self.tree[counter].extend(childlist)
                currentnode = self.tree[counter // self.numofchildren][i]
                counter += 1

    def calculateHofN(self, nodeList):
        for node in nodeList:
            counter = 0
            for i in node.puzzleState:
                for j in node.puzzleState[i]:
                    if node.puzzleState[i][j] == 1:
                        counter += 1
            node.hOfN = counter

    def generatechildrenfrompuzzlestate(self, parentpuzzlestate, nodecounter):
        childrenlist = []
        puzzlestate = parentpuzzlestate
        for y in range(int(self.size)):
            for x in range(int(self.size)):
                childrenlist.append(Node(int(nodecounter), 0, 0, 0, self.touch(y, x, puzzlestate)))
                self.calculateHofN(childrenlist)
                nodecounter += 1
        return childrenlist, nodecounter

    def BFS(self):
        start = time.time()

        if self.max_length == 0:
            print("the max length cannot be 0. Otherwise, BFS will take a long time to compute")
            stop = time.time()
            print("time to run BFS: " + str((stop - start)))
            return

        # Used as Priority Queue
        openlist = PriorityQueue()

        # Used as search path (excludes goal node)
        closedlist = []

        openlist.put((0, self.rootnode))

        goalstate = creategoalstate(self.size)

        counter = 0
        print("BFS. . . .")
        while openlist.qsize() != 0:
            node = openlist.get()
            if node.puzzlestate == goalstate:
                print("SUCCESS!! the node index is: " + str(node.index))
                stop = time.time()
                print("time to run BFS: " + str((stop - start)))
                start = time.time()
                # solution path here
                return
            else:
                children, counter = self.generatechildrenfrompuzzlestate(node.puzzlestate, counter)
                closedlist.append(node)
                for node in children:
                    if isNodeInOpenOrClosedList(node, openlist, closedlist):
                        children.remove(node)
                openlist = addChildrenToOpenList(children, openlist)
            counter += 1
        if len(closedlist) == self.max_length:
            print("No solution within cuttoff of max_length. Maximum length reach is  " + str(len(closedlist)))
            stop = time.time()
            print("time to run BFS: " + str((stop - start)))
            return
        else:
            print("NO SOLUTION")
            stop = time.time()
            print("time to run BFS: " + str((stop - start)))


def creategoalstate(size):
    goalstate = [[0] * size for _ in range(size)]
    return goalstate


def nodeToString(node, size):
    linetoprint = str(node.fOfN) + " " + str(node.gOfN) + " " + str(node.hOfN) + " " + puzzleStateToString(
        node.puzzlestate, size)
    return linetoprint


def puzzleStateToString(puzzlestate, size):
    statestring = ""
    for i, lst in enumerate(puzzlestate):
        for j in range(size):
            statestring = statestring + str(lst[j])
    statestring = statestring + "\n"
    return statestring


def isNodeInOpenOrClosedList(node, openlist, closedlist):
    for n in openlist:
        if n.index == node.index:
            return True
    for n in closedlist:
        if n.index == node.index:
            return True
    return False


def createSolutionIndex(nodeindex, stack, size):
    if nodeindex == 0:
        stack.append(nodeindex)
        return
    stack.append(nodeindex)
    for x in range(nodeindex):
        ceilingvalue = ((x * size * size) + 1)
        floorvalue = ((x * size * size) + (size * size) + 1)
        if ceilingvalue <= nodeindex <= floorvalue:
            parentindex = x
            createSolutionIndex(parentindex, stack, size)
            break


def addChildrenToOpenList(children, openlist):
    for node in children:
        openlist.put((node.hOfN, node))
    return openlist


def printTree(tree):
    # Printing node
    for key, childrenNodes in tree.items():
        for node in childrenNodes:
            print(key, " : ", node.index)


class Node:

    def __init__(self, index, costvalue, heuristicvalue, pathcostvalue, puzzlestate):
        self.index = index
        self.puzzlestate = puzzlestate
        self.fOfN = pathcostvalue
        self.gOfN = costvalue
        self.hOfN = heuristicvalue
        self.isvisited = False
