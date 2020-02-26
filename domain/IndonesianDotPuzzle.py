import copy
from collections import defaultdict
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

        self.rootnode = Node(0, 0, 0, 0, 0, self.puzzle)

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
    def calculateHofN(puzzlestate):
        hOfN = 0
        for row in puzzlestate:
            for j in row:
                if j == 1:
                    hOfN += 1
        return hOfN

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

    def generatechildrenfrompuzzlestate(self, parentpuzzlestate, nodecounter):
        childrenlist = []
        puzzlestate = parentpuzzlestate
        for y in range(int(self.size)):
            for x in range(int(self.size)):
                newPuzzleState = self.touch(y, x, puzzlestate)
                hOfN = self.calculateHofN(newPuzzleState)
                earliestWhiteDot = self.calculateEarliestWhiteDot(newPuzzleState)
                childrenlist.append(Node(int(nodecounter), 0, hOfN, 0, earliestWhiteDot, newPuzzleState))
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
        listOfParentIndexes = []

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
                # No need for solution path for dfs because we already demoed the code
                return
            else:
                children, counter = self.generatechildrenfrompuzzlestate(node.puzzlestate, counter)
                closedlist.append(node)
                for node in children:
                    if isNodeInOpenOrClosedList(node, openlist, closedlist):
                        children.remove(node)
                openlist.extend(children)
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
                start = time.time()
                # solution path here
                return
            else:
                children, counter = self.generatechildrenfrompuzzlestate(node.puzzlestate, counter)
                closedlist.append(node)
                if counter % 10007 == 0:
                    print("Visited a thousand node: " + nodeToString(node, self.size))
                # for node in children:
                #     if isNodeInOpenOrClosedList(node, openlist.queue, closedlist):
                #         children.remove(node)
                openlist = addChildrenToOpenList(children, openlist)
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


def creategoalstate(size):
    goalstate = [[0] * size for _ in range(size)]
    return goalstate

# This method returns the best not from the queue given a tie in HofN
# Implementation based on what has been asked from the project handout
# def getNextNodeFromQueue(openListQueue, nodeFromGet):
#     nodeToReturn = None
#     sameNodeList = []
#
#     # Get all nodes with the same heuristic value
#     while True:
#         hofn, n = openListQueue.get()
#         if nodeFromGet.hOfN != n.hOfN:
#             openListQueue.put(((hofn, n.), n))
#             break
#         else:
#             if nodeFromGet.hOfN == n.hOfN:
#                 sameNodeList.append(n)
#
#     #loop through all the similar nodes and return the one with
#     # the smallest earliestWhiteDot, put all other nodes back in the
#     for node in openList:
#         if node.hOfN == nodeFromGet.hOfN:



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
        openlist.put(((node.hOfN, node.earliestWhiteDot), node))
    return openlist


def printTree(tree):
    # Printing node
    for key, childrenNodes in tree.items():
        for node in childrenNodes:
            print(key, " : ", node.index)


def outputSolutionPath(listOfParentIndexes, tree, root, size, testnumber):
    listOfNodes = []
    for index in listOfParentIndexes:
        for key, nodelist in tree.items():
            for i, node in enumerate(nodelist):
                if index == node.index:
                    listOfNodes.append(node)
    if testnumber == 1:
        f = open("1_dfs_solution.txt", "w")
    if testnumber == 0:
        f = open("0_dfs_solution.txt", "w")
    if testnumber == 2:
        f = open("2_dfs_solution.txt", "w")
    if testnumber == 3:
        f = open("3_dfs_solution.txt", "w")
    if testnumber == 4:
        f = open("4_dfs_solution.txt", "w")
    if testnumber == 5:
        f = open("5_dfs_solution.txt", "w")
    if testnumber != 1 and testnumber != 0 and testnumber != 2 and testnumber != 3 and testnumber != 4 and testnumber != 5:
        print("Invalid test number")
        return
    listOfNodes.append(root)
    listOfNodes.reverse()
    for node in listOfNodes:
        f.write(nodeToString(node, size))
    f.close()


def getSolutionPath(nodeindex, listOfParentIndexes, tree, rootNode, size, testnumber):
    createSolutionIndex(int(nodeindex), listOfParentIndexes, size)
    outputSolutionPath(listOfParentIndexes, tree, rootNode, size, testnumber)


class Node:

    def __init__(self, index, costvalue, heuristicvalue, pathcostvalue, earliestWhiteDot, puzzlestate):
        self.index = index
        self.puzzlestate = puzzlestate
        self.fOfN = pathcostvalue
        self.gOfN = costvalue
        self.hOfN = heuristicvalue
        self.isvisited = False
        self.earliestWhiteDot = earliestWhiteDot

    # https://github.com/laurentluce/python-algorithms/issues/6
    def __lt__(self, other):
        return self.hOfN < other.hOfN
