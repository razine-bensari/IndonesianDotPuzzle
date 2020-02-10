# Implementation of DEPTH FIRST SEARCH (DFS) using a depth length called max_d.

# The implementation of this DFS algorithm will be done using what has been taught in class. It is possible to
# optimize this search using recursion or other means, however, for the purpose of this course, the preferred
# implementation is the one shown in class


def DFS(tree, max_d, size, rootNode):
    if max_d == 0:
        print("the max depth cannot be 0. Otherwise, DFS will take a long time to compute")
        return

    # Used as Stack
    openlist = []
    closedlist = []

    openlist.append(rootNode)

    goalstate = creategoalstate(size)

    while len(openlist) != 0:
        node = openlist.pop()
        if node.puzzlestate == goalstate:
            print("SUCCESS")
            return
            # backtrack using function
        else:
            children = tree[node.index]
            closedlist.append(node)

            for node in children:
                if isNodeInOpenOrClosedList(node, openlist, closedlist):
                    children.remove(node)
            openlist.extend(children)
    print("Did not find any node with goal state")


def creategoalstate(size):
    goalstate = [[0] * size for _ in range(size)]
    return goalstate


def isNodeInOpenOrClosedList(node, openlist, closedlist):
    for n in openlist:
        if n.index == node.index:
            return True
    for n in closedlist:
        if n.index == node.index:
            return True
    return False


def printTree(tree):
    # Printing node
    for key, childrenNodes in tree.items():
        for node in childrenNodes:
            print(key, " : ", node.index)
