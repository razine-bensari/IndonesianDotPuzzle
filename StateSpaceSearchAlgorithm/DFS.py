# Implementation of DEPTH FIRST SEARCH (DFS) using a depth length called max_d.

# The implementation of this DFS algorithm will be done using what has been taught in class. It is possible to
# optimize this search using recursion or other means, however, for the purpose of this course, the preferred
# implementation is the one shown in class


def DFS(tree, max_d, size, rootNode, maxnodes, testnumber):
    if testnumber == 1:
        f = open("1_dfs_search.txt", "w")
    if testnumber == 0:
        f = open("0_dfs_search.txt", "w")
    if testnumber != 1 and testnumber != 0:
        print("Invalid test number")
        return

    if max_d == 0:
        print("the max depth cannot be 0. Otherwise, DFS will take a long time to compute")
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
            createSolutionIndex(int(node.index), listOfParentIndexes, size)
            outputSolutionPath(listOfParentIndexes, tree, size, testnumber)
            return
            # backtrack using function
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
        return
    else:
        print("NO SOLUTION")
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
        return
    stack.append(nodeindex)
    for x in range(nodeindex):
        if ((x * size * size) + 1) <= x <= ((x * size * size) + (size * size) + 1):
            parentindex = x
            createSolutionIndex(parentindex, stack, size)
            break


def outputSolutionPath(listOfParentIndexes, tree, size, testnumber):
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
    if testnumber != 1 and testnumber != 0:
        print("Invalid test number")
        return
    for node in listOfNodes:
        f.write(nodeToString(node, size))
    f.close()








def printTree(tree):
    # Printing node
    for key, childrenNodes in tree.items():
        for node in childrenNodes:
            print(key, " : ", node.index)
