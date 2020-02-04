#Node class used for the graph data structure
class Node:
    def __init__(self, index, costValue, heuristicValue):
        self.index = index
        self.costValue = costValue
        self.heuristicValue = heuristicValue