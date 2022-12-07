
from ils import iterated_local_search

berlin52 = [[565,575], [25,185], [345,750], [945,685], [845,655],
            [880,660], [25,230] , [525, 1000] , [580, 1175], [650, 1130] , [165,620],
            [122,580], [1465, 200] , [1530,5], [845,680], [725,370], [145,665],
            [415,635], [510,875] , [560,365] , [300,465] , [520,585] , [480,415],
            [835,625], [975,580], [1215, 245] , [1320,315] , [1250, 400] , [660, 180],
            [410,250], [420,555] , [575,665], [1150, 1160], [700,580] , [685,595],
            [685,610], [770,610], [795,645], [720,635] , [760,650], [475,960],
            [95,260], [875,920] , [700,500], [555,815], [830,485], [1170,65],
            [830,610], [605,625], [595,360] , [1340, 725], [1740, 245]]

berlin52_best_known_solution_cost = 7544.37

def fibonacci(n, memory = {}):
    result = n if n < 2 else memory[str(n)] if str(n) in memory else (fibonacci(n-1, memory) + fibonacci(n-2, memory))
    memory[str(n)] = result
    return result

def find_best_parameters(iterations, thresholds):
    results = []
    progress = 0.0
    for i in iterations:        
        for j in thresholds:
            print(f"\nILS run with {i} iterations and {j} threshold")
            print("----------------------")
            _, cost, elapsed_time = iterated_local_search(berlin52, threshold=j, iterations=i)
            results.append((i, j, cost, elapsed_time))
            progress = progress + (1.0 / (len(iterations) * len(thresholds)))

            print(f"\nProgress {progress*100:.2f}% \n")
    min_result = min(results, key=lambda result: (result[2],result[3]))
    return min_result


def split_list(list):
    size = len(list)
    low = list[:2]
    middle = int((size - 1 ) / 2)
    medium = list[middle:middle+2]
    high = list[size - 2 :]
    return low + medium + high