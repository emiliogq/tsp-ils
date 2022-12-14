from common import *
from pytest import approx

best_known_solution = 7542
data = read_nodes_file("data/berlin52.tsp", 6, 58)

def test_ils_parameters():
    iterations = thresholds = [fibonacci(i) for i in range(2, 20)]
    split_thresholds = split_list(thresholds)
    split_iterations = split_list(iterations)
    
    min_result = find_best_parameters(data, split_iterations, split_thresholds)
    
    min_cost = min_result[2]
    print(f"The result with minimum cost found is {min_result}")
    assert min_cost == approx(best_known_solution, rel=0.02)