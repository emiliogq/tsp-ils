from ils import ILS
from pytest import approx, mark
from common import read_nodes_file

# BSK http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/STSP.html
best_known_solution = 2579
data = read_nodes_file("data/a280.tsp", 6, 286)

ils = ILS()

@mark.xfail
def test_a280_tsp_instance_with_default_ils():
    solution, elapsed_time = ils.run(data)
    assert solution.cost == approx(best_known_solution, rel=0.5)

@mark.xfail    
def test_a280_tsp_instance_with_10k_iterations():
    solution, elapsed_time = ils.run(data, iterations=10000)
    assert solution.cost == approx(best_known_solution, rel=0.3)
@mark.xfail
def test_a280_tsp_instance_with_best_parameter_values_found():
    solution, elapsed_time = ils.run(data, iterations=2584, threshold=2584)
    assert solution.cost == approx(best_known_solution, rel=0.1)