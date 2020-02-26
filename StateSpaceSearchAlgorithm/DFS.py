import time
# Implementation of DEPTH FIRST SEARCH (DFS) using a depth length called max_d.

# The implementation of this DFS algorithm will be done using what has been taught in class. It is possible to
# optimize this search using recursion or other means, however, for the purpose of this course, the preferred
# implementation is the one shown in class (more precisely, the one shown in the slides of the second lecture)


def DFS(tree, max_d, size, rootNode, maxnodes, testnumber):
    start = time.time()
    if testnumber == 1:
        f = open("1_dfs_search.txt", "w")
    if testnumber == 0:
        f = open("0_dfs_search.txt", "w")
    if testnumber == 2:
        f = open("2_dfs_search.txt", "w")
    if testnumber == 3:
        f = open("3_dfs_search.txt", "w")
    if testnumber == 4:
        f = open("4_dfs_search.txt", "w")
    if testnumber == 5:
        f = open("5_dfs_search.txt", "w")
    if testnumber != 1 and testnumber != 0 and testnumber != 2 and testnumber != 3 and  testnumber != 4 and testnumber != 5:
        print("Invalid test number")
        return

    if max_d == 0:
        print("the max depth cannot be 0. Otherwise, DFS will take a long time to compute")
        stop = time.time()
        print("time to run DFS: " + str((stop - start)))
        return

    # Used as Stack
    openlist = []
    closedlist = []
    listOfParentIndexes = []

    openlist.append(rootNode)

    goalstate = creategoalstate(size)

    counter = 0
    print("DFS. . . .")
    while len(openlist) != 0:
        node = openlist.pop()
        f.write(nodeToString(node, size))
        if node.puzzlestate == goalstate:
            print("SUCCESS!! the node index is: " + str(node.index))
            f.close()
            stop = time.time()
            print("time to run DFS: " + str((stop - start)))
            start = time.time()
            getSolutionPath(int(node.index), listOfParentIndexes, tree, rootNode, size, testnumber)
            stop = time.time()
            print("time to backtrack to root node: " + str((stop - start)))
            return
        else:
            children = tree[node.index]
            closedlist.append(node)

            for node in children:
                if isNodeInOpenOrClosedList(node, openlist, closedlist):
                    children.remove(node)
            openlist.extend(children)
        counter += 1
    if maxnodes == counter:
        print("No solution within cuttoff. Maximum number of nodes for given depth is: " + str(maxnodes))
        f.close()
        stop = time.time()
        print("time to run DFS: " + str((stop - start)))
        return
    else:
        print("NO SOLUTION")
        stop = time.time()
        print("time to run DFS: " + str((stop - start)))
        f.close()


def creategoalstate(size):
    goalstate = [[0] * size for _ in range(size)]
    return goalstate


def nodeToString(node, size):
    linetoprint = str(node.fOfN) + " " + str(node.gOfN) + " " + str(node.hOfN) + " " + puzzleStateToString(node.puzzlestate, size)
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


def printTree(tree):
    # Printing node
    for key, childrenNodes in tree.items():
        for node in childrenNodes:
            print(key, " : ", node.index)
