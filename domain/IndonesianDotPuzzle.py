import copy
import textwrap
from queue import PriorityQueue
import time


class IndonesianDotPuzzle:

    def __init__(self, textline):
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

        self.rootnode = Node(0, 0, 0, 0, 0, 0, None, self.puzzle, "0")

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

    # Heuristic 1
    # Counts the number of ones in the puzzle state
    @staticmethod
    def calculateHofN_one(puzzlestate):
        hOfN = 0
        for row in puzzlestate:
            for j in row:
                if j == 1:
                    hOfN += 1
        return hOfN

    # Heuristic 2
    # Associate a heuristic value based on the current shape of the puzzle
    @staticmethod
    def calculateHofH_two(node):
        return None

    @staticmethod
    def calculateGofN(node):
        return node.depthLevel

    @staticmethod
    def calculateFofN(node):
        return node.gOfN + node.hOfN

    @staticmethod
    def calculateEarliestWhiteDot(puzzlestate):
        earliestWhiteDot = 0
        for row in puzzlestate:
            for j in row:
                if j == 0:
                    return earliestWhiteDot
                else:
                    earliestWhiteDot += earliestWhiteDot
        return earliestWhiteDot

    def generatechildrenfrompuzzlestate(self, node, nodecounter, depthLevel):
        childrenlist = []
        for y in range(int(self.size)):
            for x in range(int(self.size)):
                newPuzzleState = self.touch(y, x, node.puzzlestate)
                hOfN = self.calculateHofN_one(newPuzzleState)
                gOfN = self.calculateGofN(node)
                fOfN = self.calculateFofN(node)
                coord = getTouchedCoordinate(x, y)
                earliestWhiteDot = self.calculateEarliestWhiteDot(newPuzzleState)
                childrenlist.append(Node(int(nodecounter),
                                         gOfN,
                                         hOfN,
                                         fOfN,
                                         earliestWhiteDot,
                                         depthLevel,
                                         node,
                                         newPuzzleState,
                                         coord))
                nodecounter += 1
        return childrenlist, nodecounter

    def DFS(self):
        start = time.time()
        if self.max_depth == 0:
            print("the max depth cannot be 0. Otherwise, DFS will take a long time to compute")
            stop = time.time()
            print("time to run DFS: " + str((stop - start)))
            return

        # Used as Stack
        openlist = []
        closedlist = []

        openlist.append(self.rootnode)

        goalstate = creategoalstate(self.size)

        counter = 0
        print("DFS. . . .")
        while len(openlist) != 0:
            node = openlist.pop()
            if node.puzzlestate == goalstate:
                print("SUCCESS!! the node index is: " + str(node.index))
                stop = time.time()
                print("time to run DFS: " + str((stop - start)))
                outputSolutionPath(node, self.size)
                return
            else:
                children, counter = self.generatechildrenfrompuzzlestate(node, counter, node.depthLevel + 1)
                closedlist.append(node)
                for node in children:
                    if isNodeInOpenOrClosedList(node, openlist, closedlist):
                        children.remove(node)
                openlist = addChildrenToOpenList(children, openlist, "DFS")
            counter += 1
        if self.maxnodenumber == counter:
            print("No solution within cutoff. Maximum number of nodes for given depth is: " + str(self.maxnodenumber))
            stop = time.time()
            print("time to run DFS: " + str((stop - start)))
            return
        else:
            print("NO SOLUTION")
            stop = time.time()
            print("time to run DFS: " + str((stop - start)))

    def BFS(self):
        start = time.time()

        if self.max_length == 0:
            print("the max length cannot be 0. Otherwise, BFS will take a long time to compute")
            stop = time.time()
            print("time to run BFS: " + str((stop - start)))
            # print solution path to terminal
            return

        # Used as Priority Queue
        openlist = PriorityQueue()

        # Used as search path (excludes goal node)
        closedlist = []

        openlist.put(((0, 0), self.rootnode))

        goalstate = creategoalstate(self.size)

        counter = 1
        print("BFS. . . .")
        while openlist.qsize() != 0:
            hn, node = openlist.get()
            if node.puzzlestate == goalstate:
                print("SUCCESS!! the node index is: " + str(node.index))
                stop = time.time()
                print("time to run BFS: " + str((stop - start)))
                outputSolutionPath(node, self.size)
                return
            else:
                children, counter = self.generatechildrenfrompuzzlestate(node, counter, node.depthLevel + 1)
                closedlist.append(node)
                if counter % 10007 == 0:
                    print("Visited a thousand node: " + nodeToString(node, self.size))
                openlist = addChildrenToOpenList(children, openlist, "BFS")
            if len(closedlist) >= self.max_length:
                print("No solution within cutoff of max_length. Maximum length reach is  " + str(len(closedlist)))
                stop = time.time()
                print("time to run BFS: " + str((stop - start)))
                return
        else:
            print("NO SOLUTION")
            stop = time.time()
            print("time to run BFS: " + str((stop - start)))
            return

    def A_star(self):
        start = time.time()

        if self.max_length == 0:
            print("the max length cannot be 0. Otherwise, A* will take a long time to compute")
            stop = time.time()
            print("time to run A*: " + str((stop - start)))
            # print solution path to terminal
            return

        # Used as Priority Queue
        openlist = PriorityQueue()

        # Used as search path (excludes goal node)
        closedlist = []

        openlist.put(((0, 0), self.rootnode))

        goalstate = creategoalstate(self.size)

        counter = 1
        print("A*. . . .")
        while openlist.qsize() != 0:
            hn, node = openlist.get()
            if node.puzzlestate == goalstate:
                print("SUCCESS!! the node index is: " + str(node.index))
                stop = time.time()
                print("time to run A*: " + str((stop - start)))
                outputSolutionPath(node, self.size)
                return
            else:
                children, counter = self.generatechildrenfrompuzzlestate(node, counter, node.depthLevel + 1)
                closedlist.append(node)
                if counter % 10007 == 0:
                    print("Visited a thousand node: " + nodeToString(node, self.size))
                openlist = addChildrenToOpenList(children, openlist, "A*")
            if len(closedlist) >= self.max_length:
                print("No solution within cutoff of max_length. Maximum length reach is  " + str(len(closedlist)))
                stop = time.time()
                print("time to run A*: " + str((stop - start)))
                return
        else:
            print("NO SOLUTION")
            stop = time.time()
            print("time to run A*: " + str((stop - start)))
            return


def outputSolutionPath(finalNode, size):
    currentNode = finalNode
    solutionlist = []

    while currentNode is not None:
        solutionlist.append(currentNode)
        currentNode = currentNode.parentNode

    # in place reverse
    solutionlist.reverse()

    print("\n\nSolution path: ")
    for node in solutionlist:
        statestring = puzzleStateToString(node.puzzlestate, size)
        print(node.coord + " " + statestring, end='')


def getTouchedCoordinate(y, x):
    return str(y) + str(x)


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


# def createSolutionIndex(nodeindex, stack, size):
#     if nodeindex == 0:
#         stack.append(nodeindex)
#         return
#     stack.append(nodeindex)
#     for x in range(nodeindex):
#         ceilingvalue = ((x * size * size) + 1)
#         floorvalue = ((x * size * size) + (size * size) + 1)
#         if ceilingvalue <= nodeindex <= floorvalue:
#             parentindex = x
#             createSolutionIndex(parentindex, stack, size)
#             break


def addChildrenToOpenList(children, openlist, distinguisher):
    if distinguisher == "BFS":
        for node in children:
            openlist.put(((node.hOfN, node.earliestWhiteDot), node))
        return openlist
    elif distinguisher == "A*":
        for node in children:
            openlist.put(((node.fOfN, node.earliestWhiteDot), node))
        return openlist
    elif distinguisher == "DFS":
        return openlist.extend(children)


def printTree(tree):
    # Printing node
    for key, childrenNodes in tree.items():
        for node in childrenNodes:
            print(key, " : ", node.index)


class Node:

    def __init__(self, index, costvalue, heuristicvalue, functionCostvalue, earliestWhiteDot, depthLevel, parentNode,
                 puzzlestate, coord):
        self.index = index
        self.puzzlestate = puzzlestate
        self.fOfN = functionCostvalue
        self.gOfN = costvalue
        self.hOfN = heuristicvalue
        self.earliestWhiteDot = earliestWhiteDot
        self.depthLevel = depthLevel
        self.parentNode = parentNode
        self.coord = coord

    # https://github.com/laurentluce/python-algorithms/issues/6
    def __lt__(self, other):
        return self.hOfN < other.hOfN
