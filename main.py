from domain.IndonesianDotPuzzle import *
from StateSpaceSearchAlgorithm.DFS import *

tree = IndonesianDotPuzzle()
root = Node(0, None, None)

# Add children to root node
tree.addNode(root.index, Node(1, None, None))
tree.addNode(root.index, Node(2, None, None))
tree.addNode(root.index, Node(3, None, None))
tree.addNode(root.index, Node(4, None, None))

# Add children to node 2
tree.addNode(2, Node(5, None, None))
tree.addNode(2, Node(6, None, None))
print("Executing DFS NOW: . . . .")
DFS(tree, 1)
printTree(tree.tree)