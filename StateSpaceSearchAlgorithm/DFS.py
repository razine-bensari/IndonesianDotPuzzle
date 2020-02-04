#Implementation of DEPTH FIRST SEARCH (DFS) using a depth length called max_d.

# The implementation of this DFS algorithm will be done using what has been taught in class.
# It is possible to optimize this search using recursion or other means, however, for the purpose of this course, the preferred implementation
# is the one shown in class

def DFS(tree, max_d):

    # Used as Stack
    openList = []

    closedList = []

    if max_d == 0:
        print("the max depth cannot be 0. Otherwise, DFS will take a long time to compute")
        return
    
    #Printing node TODO
    for parentNode, childrenNodes in tree.tree.items():
     for node in childrenNodes:
          print(parentNode.index," : ",node.index)