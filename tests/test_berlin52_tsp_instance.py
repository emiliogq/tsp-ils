from ils import *
from common import *
from pytest import approx

best_known_solution = 7542
data = read_nodes_file("data/berlin52.tsp", 6, 58)

def test_berlin52_tsp_instance_with_default_ils():

    # Default iteration and threshold values : 1000, 50
    solution, cost, elapsed_time = iterated_local_search(data)
    assert cost == approx(best_known_solution, rel=0.5)

def test_berlin52_tsp_instance_with_10k_iterations():

    solution, cost, elapsed_time = iterated_local_search(data, iterations=10000)
    assert cost == approx(best_known_solution, rel=0.3)

def test_berlin52_tsp_instance_with_best_parameter_values_found():

    solution, cost, elapsed_time = iterated_local_search(data, iterations=1000, threshold=1000)
    assert cost == approx(best_known_solution, rel=0.1)
