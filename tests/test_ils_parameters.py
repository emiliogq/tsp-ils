from common import *
from pytest import approx

def test_ils_parameters():
    iterations = thresholds = [fibonacci(i) for i in range(2, 20)]
    split_thresholds = split_list(thresholds)
    split_iterations = split_list(iterations)
    
    min_result = find_best_parameters(split_iterations, split_thresholds)
    
    min_cost = min_result[2]
    print(f"The result with minimum cost found is {min_result}")
    assert min_cost == approx(berlin52_best_known_solution_cost, rel=0.02)