from node import Node, Edge

class Solution:
    
    def __init__(self, nodes = []) -> None:
        self.nodes = nodes
        self.edges = [ self.create_edge(self.nodes[i], self.nodes[i+1]) for i in range(len(self.nodes)-1)]
        if len(self.nodes) > 1:
            self.edges.append(self.create_edge(self.nodes[-1], self.nodes[0]))
        
    def cost(self) -> float:
        return sum([edge.distance for edge in self.edges])
    
    def __eq__(self, solution:'Solution'):
        has_same_cost = solution.cost() == self.cost()
        has_same_node_len = len(self.nodes) == len(solution.nodes)
        return has_same_cost and has_same_node_len and all([ node in solution.nodes for node in self.nodes])
            
    def create_edge(self, node_a, node_b):
        xa,ya = node_a
        xb,yb = node_b
        return Edge(Node(xa,ya), Node(xb,yb))
    
    def add_node(self, node):
        x, y = node
        self.nodes.append(node)
        inserted_node = Node(x,y)
       
        if len(self.nodes) >= 2:
       
            x_origin, y_origin = self.nodes[0]
            origin = Node(x_origin, y_origin)
            end = origin
       
            if len(self.edges) > 0:
                last:Edge = self.edges.pop()
                origin, end = last.origin, last.end     
            
            self.edges.append(Edge(origin, inserted_node))
            self.edges.append(Edge(inserted_node, end))

        
    def remove_nodes(self):
        self.nodes.clear()
        self.remove_edges()
    
    def remove_edges(self):
        self.edges.clear()
    
    def __ge__(self, solution:'Solution'):
        
        return self.cost() >= solution.cost()
    
    def __le__(self, solution:'Solution'):
        return self.cost() <= solution.cost()

    def __gt__(self, solution:'Solution'):
        return self.cost() > solution.cost()
    
    def __lt__(self, solution:'Solution'):
        return self.cost() < solution.cost()    

    def __str__(self) -> str:
        return f"Cost = {self.cost()}"