class Solution:
    
    def __init__(self, nodes = []) -> None:
        self.nodes = nodes
        self.cost = 0.0
    
    def __eq__(self, solution:'Solution'):
        has_same_cost = solution.cost == self.cost
        has_same_node_len = len(self.nodes) == len(solution.nodes)
        return has_same_cost and has_same_node_len and all([ node in solution.nodes for node in self.nodes])

    def __ge__(self, solution:'Solution'):
        return self.cost >= solution.cost
    
    def __le__(self, solution:'Solution'):
        return self.cost <= solution.cost

    def __gt__(self, solution:'Solution'):
        return self.cost > solution.cost
    
    def __lt__(self, solution:'Solution'):
        return self.cost < solution.cost    

    def __str__(self) -> str:
        return f"Cost = {self.cost}"