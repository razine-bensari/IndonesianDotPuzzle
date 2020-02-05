from domain.Node import Node
from domain.Tree import Tree
from StateSpaceSearchAlgorithm.DFS import DFS



t = Tree()
root = Node(0, None, None)

# Add children to root node
t.addNode(root.index, Node(1, None, None))
t.addNode(root.index, Node(2, None, None))
t.addNode(root.index, Node(3, None, None))
t.addNode(root.index, Node(4, None, None))

# Add children to node 2
t.addNode(2, Node(5, None, None))
t.addNode(2, Node(6, None, None))
print("Executing DFS NOW: . . . .")
DFS(t, 1)