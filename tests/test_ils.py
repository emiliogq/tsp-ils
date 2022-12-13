from ils import ILS
from common import *
from pytest import approx

ils = ILS()

def test_simple_ils():

    # Default iteration and threshold values : 1000, 50
    solution, elapsed_time = ils.run(berlin52)
    assert solution.cost == approx(berlin52_best_known_solution_cost, rel=0.5)

def test_simple_ils_with_10k_iterations():

    solution, elapsed_time = ils.run(berlin52, iterations=10000)
    assert solution.cost == approx(berlin52_best_known_solution_cost, rel=0.3)

def test_simple_ils_with_1k_iterations_and_threshold():
    solution, elapsed_time = ils.run(berlin52, iterations=1000, threshold=1000)
    assert solution.cost == approx(berlin52_best_known_solution_cost, rel=0.1)
