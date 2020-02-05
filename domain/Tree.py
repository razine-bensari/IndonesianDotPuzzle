from collections import defaultdict

class Tree:

    #Using adjacent list structure (dictionary of all nodes. All values of dic are list of children node related to parent node - Key)
    def __init__(self):
        self.tree = defaultdict(list)
    
    #Inserts a node given a parent node (parentNode is essentially the index in the adjacent list)
    def addNode(self, parentNode, nodeToInsert):
        self.tree[parentNode].append(nodeToInsert)