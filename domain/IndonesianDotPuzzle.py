from collections import defaultdict
class IndonesianDotPuzzle:

    #Using adjacent list structure (dictionary of all nodes. All values of dic are list of children node related to parent node - Key)
    def __init__(self):
        self.tree = defaultdict(list)
    
    #Inserts a node given a parent node (parentNode is essentially the index in the adjacent list)
    def addNode(self, parentNode, nodeToInsert):
        self.tree[parentNode].append(nodeToInsert)

#Node class used for the graph data structure
class Node:
    def __init__(self, index, costValue, heuristicValue):
        self.index = index
        self.costValue = costValue
        self.heuristicValue = heuristicValue