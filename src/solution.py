class Solution:
    
    def __init__(self, nodes = []) -> None:
        self.nodes = nodes
        self.cost = 0.0

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