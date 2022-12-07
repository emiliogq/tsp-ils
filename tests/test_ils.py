from ils import *
from common import *
from pytest import approx

def test_simple_ils():

    # Default iteration and threshold values : 1000, 50
    solution, cost, elapsed_time = iterated_local_search(berlin52)
    assert cost == approx(berlin52_best_known_solution_cost, rel=0.5)

    solution, cost, elapsed_time = iterated_local_search(berlin52, iterations=10000)
    assert cost == approx(berlin52_best_known_solution_cost, rel=0.3)

    solution, cost, elapsed_time = iterated_local_search(berlin52, iterations=1000, threshold=1000)
    assert cost == approx(berlin52_best_known_solution_cost, rel=0.1)
