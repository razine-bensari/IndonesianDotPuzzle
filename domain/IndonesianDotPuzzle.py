import copy
import textwrap
from queue import PriorityQueue
import time
import string


class IndonesianDotPuzzle:

    def __init__(self, textline, puzzleNumber):
        self.puzzleNumber = puzzleNumber
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

    def switch(self, val):
        return 1 - int(val)

    def getNumOfOnes(self, puzzlestate):
        # Get Number of 1s
        numOfOnes = 0
        value = 0
        for row in puzzlestate:
            for v in row:
                if v == 1:
                    numOfOnes += 1
        return numOfOnes

    # Heuristic 1
    # Counts the number of ones in the puzzle state
    def calculateHofN_one(self, puzzlestate):
        hOfN = 0
        for row in puzzlestate:
            for j in row:
                if j == 1:
                    hOfN += 1
        return hOfN

    def isCrossState(self, puzzlestate):
        for i, row in enumerate(puzzlestate):
            for j, v in enumerate(row):
                if v == 1 and i != 0 and i != self.size - 1 and j != 0 and j != self.size - 1 and \
                        puzzlestate[i-1][j] == 1 and puzzlestate[i+1][j] == 1 and puzzlestate[i][j+1] == 1 and puzzlestate[i+1][j-1]:
                    return True
        else:
            return False

    def isTshape(self, puzzlestate):
        for i, row in enumerate(puzzlestate):
            for j, v in enumerate(row):
                if v == 1:
                    # T shape is in top row
                    if i == 0 and j != 0 and j != self.size - 1 and puzzlestate[i + 1][j] == 1 and \
                            puzzlestate[i][j - 1] == 1 and puzzlestate[i][j + 1] == 1:
                        return True
                    # T shape is in bottom row
                    elif i == self.size - 1 and j != 0 and j != self.size - 1 and puzzlestate[i - 1][j] == 1 and \
                            puzzlestate[i][j - 1] == 1 and puzzlestate[i][j + 1] == 1:
                        return True
                    # T shape is in left side
                    elif j == 0 and i != 0 and i != self.size - 1 and puzzlestate[i][j + 1] == 1 and \
                            puzzlestate[i - 1][j] == 1 and puzzlestate[i + 1][j] == 1:
                        return True
                    # T shape is in the right
                    elif j == self.size - 1 and i != 0 and i != self.size - 1 and puzzlestate[i][j - 1] == 1 and \
                            puzzlestate[i - 1][j] == 1 and puzzlestate[i + 1][j] == 1:
                        return True
        else:
            return False

    def isLshape(self, puzzlestate):
        for i, row in enumerate(puzzlestate):
            for j, v in enumerate(row):
                if v == 1:
                    # Top left corner
                    if i == 0 and j == 0 and puzzlestate[i][j + 1] == 1 and puzzlestate[i + 1][j] == 1:
                        return True
                    # Top right corner
                    elif i == 0 and j == self.size - 1 and puzzlestate[i][j - 1] == 1 and puzzlestate[i + 1][
                        j] == 1:
                        return True
                    # bottom left corner
                    elif i == self.size - 1 and j == 0 and puzzlestate[i - 1][j] == 1 and puzzlestate[i][
                        j + 1] == 1:
                        return True
                    # bottom right corner
                    elif i == self.size - 1 and j == self.size - 1 and puzzlestate[i][j - 1] == 1 and \
                            puzzlestate[i - 1][j] == 1:
                        return True
        else:
            return False

    def isThereALoop(self, puzzlestate, node):
        if node.parentNode is None:
            return False
        if puzzleStateToString(puzzlestate, self.size) == puzzleStateToString(node.parentNode.puzzlestate, self.size):
            return True

    # Heuristic 2
    # Associate a heuristic value based on the current shape of the puzzle
    def calculateHofH_two(self, puzzlestate, node):
        # Get Number of 1s
        numOfOnes = self.getNumOfOnes(puzzlestate)

        if numOfOnes == 5 and self.isCrossState(puzzlestate):
            hOfN = 1
        elif numOfOnes == 3 and self.isLshape(puzzlestate):
            hOfN = 1
        elif numOfOnes == 4 and self.isTshape(puzzlestate):
            hOfN = 1
        elif numOfOnes == 0:
            hOfN = 0
        elif self.isThereALoop(puzzlestate, node):
            hOfN = 100000
        else:
            # check for loop (heavy computation <0.0>)
            hOfN = numOfOnes + 1
        return hOfN

    def calculateGofN(self, node):
        return node.depthLevel + self.size/3

    def calculateFofN(self, costValue, heuristicValue):
        return costValue + heuristicValue

    def calculateEarliestWhiteDot(self, puzzlestate):
        earliestWhiteDot = 0
        for row in puzzlestate:
            for j in row:
                if j == 0:
                    return earliestWhiteDot
                else:
                    earliestWhiteDot += earliestWhiteDot
        return earliestWhiteDot

    def generatechildrenfrompuzzlestate(self, node, nodecounter, depthLevel, typeOfSearch):
        if typeOfSearch == "DFS":
            childrenlist = []
            for y in range(int(self.size)):
                for x in range(int(self.size)):
                    newPuzzleState = self.touch(y, x, node.puzzlestate)
                    hOfN = 0
                    gOfN = 0
                    fOfN = 0
                    coord = 0
                    earliestWhiteDot = 0
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
        elif typeOfSearch == "BFS":
            childrenlist = []
            for y in range(int(self.size)):
                for x in range(int(self.size)):
                    newPuzzleState = self.touch(y, x, node.puzzlestate)
                    hOfN = self.calculateHofH_two(newPuzzleState, node)
                    gOfN = 0
                    fOfN = 0
                    coord = getTouchedCoordinate(y, x)
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
        else:
            childrenlist = []
            for y in range(int(self.size)):
                for x in range(int(self.size)):
                    newPuzzleState = self.touch(y, x, node.puzzlestate)
                    hOfN = self.calculateHofH_two(newPuzzleState, node)
                    gOfN = self.calculateGofN(node)
                    fOfN = self.calculateFofN(gOfN, hOfN)
                    coord = getTouchedCoordinate(y, x)
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
        fileNameSearch = str(self.puzzleNumber) + "_dfs_search.txt"
        fileNameSolution = str(self.puzzleNumber) + "_dfs_solution.txt"
        fSearch = open(fileNameSearch, "w")
        fSol = open(fileNameSolution, "w")
        start = time.time()

        if self.max_depth == 0:
            print("the max depth cannot be 0. Otherwise, DFS will take a long time to compute")
            stop = time.time()
            print("time to run DFS: " + str((stop - start)))
            fSearch.close()
            fSol.close()
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
                outputSolutionPath(node, self.size, fSol)
                fSol.close()
                fSearch.close()
                return
            else:
                children, counter = self.generatechildrenfrompuzzlestate(node, counter, node.depthLevel + 1, "DFS")
                fSearch.write(nodeToString(node, self.size))
                closedlist.append(node)
                for node in children:
                    if isNodeInOpenOrClosedList(node, openlist, closedlist):
                        children.remove(node)
                addChildrenToOpenList(children, openlist, "DFS")
            counter += 1
            if self.maxnodenumber == counter:
                print("No solution within cutoff. Maximum number of nodes for given depth is: " + str(self.maxnodenumber))
                stop = time.time()
                print("time to run DFS: " + str((stop - start)))
                fSol.write("no solution")
                fSearch.close()
                fSol.close()
                return
        else:
            print("NO SOLUTION")
            stop = time.time()
            print("time to run DFS: " + str((stop - start)))
            fSol.write("no solution")
            fSol.close()
            fSearch.close()
            return

    def BFS(self):
        fileNameSearch = str(self.puzzleNumber) + "_bfs_search.txt"
        fileNameSolution = str(self.puzzleNumber) + "_bfs_solution.txt"
        fSearch = open(fileNameSearch, "w")
        fSol = open(fileNameSolution, "w")
        start = time.time()

        if self.max_length == 0:
            print("the max length cannot be 0. Otherwise, BFS will take a long time to compute")
            stop = time.time()
            print("time to run BFS: " + str((stop - start)))
            fSearch.close()
            fSol.close()
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
                outputSolutionPath(node, self.size, fSol)
                print("Number of nodes in openlist: " + str(len(openlist.queue)))
                print("Number of nodes in closedlist: " + str(len(closedlist)))
                fSol.close()
                fSearch.close()
                return
            else:
                children, counter = self.generatechildrenfrompuzzlestate(node, counter, node.depthLevel + 1, "BFS")
                fSearch.write(nodeToString(node, self.size))
                closedlist.append(node)
                openlist = addChildrenToOpenList(children, openlist, "BFS")
            if len(closedlist) >= self.max_length:
                print("No solution within cutoff of max_length. Maximum length reach is  " + str(len(closedlist)))
                stop = time.time()
                print("Number of nodes in openlist: " + str(len(openlist.queue)))
                print("Number of nodes in closedlist: " + str(len(closedlist)))
                print("time to run BFS: " + str((stop - start)))
                fSol.write("no solution")
                fSearch.close()
                fSol.close()
                return
        else:
            print("NO SOLUTION")
            stop = time.time()
            print("Number of nodes in openlist: " + str(len(openlist.queue)))
            print("Number of nodes in closedlist: " + str(len(closedlist)))
            print("time to run BFS: " + str((stop - start)))
            fSol.write("no solution")
            fSol.close()
            fSearch.close()
            return

    def A_star(self):
        fileNameSearch = str(self.puzzleNumber) + "_astar_search.txt"
        fileNameSolution = str(self.puzzleNumber) + "_astar_solution.txt"
        fSearch = open(fileNameSearch, "w")
        fSol = open(fileNameSolution, "w")
        start = time.time()

        if self.max_length == 0:
            print("the max length cannot be 0. Otherwise, A* will take a long time to compute")
            stop = time.time()
            print("time to run A*: " + str((stop - start)))
            fSearch.close()
            fSol.close()
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
                outputSolutionPath(node, self.size, fSol)
                print("Number of nodes in openlist: " + str(len(openlist.queue)))
                print("Number of nodes in closedlist: " + str(len(closedlist)))
                fSol.close()
                fSearch.close()
                return
            else:
                children, counter = self.generatechildrenfrompuzzlestate(node, counter, node.depthLevel + 1, "A*")
                fSearch.write(nodeToString(node, self.size))
                closedlist.append(node)
                openlist = addChildrenToOpenList(children, openlist, "A*")
            if len(closedlist) >= self.max_length:
                print("No solution within cutoff of max_length. Maximum length reach is  " + str(len(closedlist)))
                stop = time.time()
                print("Number of nodes in openlist: " + str(len(openlist.queue)))
                print("Number of nodes in closedlist: " + str(len(closedlist)))
                print("time to run A*: " + str((stop - start)))
                fSol.write("no solution")
                fSearch.close()
                fSol.close()
                return
        else:
            print("NO SOLUTION")
            stop = time.time()
            print("Number of nodes in openlist: " + str(len(openlist.queue)))
            print("Number of nodes in closedlist: " + str(len(closedlist)))
            print("time to run A*: " + str((stop - start)))
            fSol.write("no solution")
            fSearch.close()
            fSol.close()
            return


def outputSolutionPath(finalNode, size, fSol):
    mapLetter = dict(zip(range(1, 27), string.ascii_lowercase))
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
        coordinate = getCartesianCoordinate(mapLetter, node.coord)
        print(coordinate + "    " + statestring, end='')
        fSol.write(coordinate + "    " + statestring)


def getCartesianCoordinate(dic, coord):
    if len(coord) == 1:
        return "0 "
    else:
        c1 = int(coord[0])
        c2 = int(coord[1])
        return str(dic.get(c1 + 1)).capitalize() + str(c2 + 1)


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


def addChildrenToOpenList(children, openlist, typeOfSearch):
    if typeOfSearch == "BFS":
        for node in children:
            openlist.put(((node.hOfN, node.earliestWhiteDot), node))
        return openlist
    elif typeOfSearch == "A*":
        for node in children:
            openlist.put(((node.fOfN, node.earliestWhiteDot), node))
        return openlist
    elif typeOfSearch == "DFS":
        openlist.extend(children)


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
