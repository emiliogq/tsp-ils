from abc import ABC
from math import sqrt

class Node(ABC):

    last_ID = -1

    def __init__(self, x, y):
        Node.last_ID += 1
        self.ID = Node.last_ID # node identifier (depot ID = 0)
        self.x = x # x-coordinate
        self.y = y # y-coordinate
  
    def euclidean_distance(self, node:'Node') -> float :
        return sqrt((self.x - node.x)**2 + (self.y - node.y)**2)

class Edge:
    def __init__(self, origin: Node, end: Node):
        self.origin = origin # origin node of the edge (arc)
        self.end = end # end node of the edge (arc)
        self.distance = origin.euclidean_distance(end)
        self.travel_time = 0

    def is_origin(self, node: Node):
        return self.origin == node
    
    def is_end(self, node: Node):
        return self.end == node

    def __str__(self) -> str:
        return f"({self.origin.ID} -> {self.end.ID})"