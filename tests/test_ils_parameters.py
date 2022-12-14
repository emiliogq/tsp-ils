from common import *
from pytest import approx


best_known_solution = 7542
data = read_nodes_file("data/berlin52.tsp", 6, 58)

def test_ils_parameters():
    
    min_result = find_best_parameters(data)
    
    min_cost = min_result[2]
    print(f"The result with minimum cost found is {min_result}")
    assert min_cost == approx(best_known_solution, rel=0.02)