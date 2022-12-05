from ils import *
from pytest import approx

berlin52 = [[565,575], [25,185], [345,750], [945,685], [845,655],
            [880,660], [25,230] , [525, 1000] , [580, 1175], [650, 1130] , [165,620],
            [122,580], [1465, 200] , [1530,5], [845,680], [725,370], [145,665],
            [415,635], [510,875] , [560,365] , [300,465] , [520,585] , [480,415],
            [835,625], [975,580], [1215, 245] , [1320,315] , [1250, 400] , [660, 180],
            [410,250], [420,555] , [575,665], [1150, 1160], [700,580] , [685,595],
            [685,610], [770,610], [795,645], [720,635] , [760,650], [475,960],
            [95,260], [875,920] , [700,500], [555,815], [830,485], [1170,65],
            [830,610], [605,625], [595,360] , [1340, 725], [1740, 245]]

def test_metaheuristic():

    best_known_solution = 7544.37

    # Default iteration and threshold values : 1000, 50
    solution, cost, elapsed_time = iterated_local_search(berlin52)
    assert cost == approx(best_known_solution, rel=0.5)

    solution, cost, elapsed_time = iterated_local_search(berlin52, iterations=10000)
    assert cost == approx(best_known_solution, rel=0.3)

    solution, cost, elapsed_time = iterated_local_search(berlin52, iterations=1000, threshold=1000)
    assert cost == approx(best_known_solution, rel=0.1)