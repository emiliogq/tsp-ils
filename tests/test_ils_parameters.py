from common import *
from pytest import approx

def test_ils_parameters():
    
    min_result = find_best_parameters(berlin52)
    
    min_cost = min_result[2]
    print(f"The result with minimum cost found is {min_result}")
    assert min_cost == approx(berlin52_best_known_solution_cost, rel=0.02)