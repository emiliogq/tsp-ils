
from ils import ILS

import logging

def fibonacci(n, memory = {}):
    result = n if n < 2 else memory[str(n)] if str(n) in memory else (fibonacci(n-1, memory) + fibonacci(n-2, memory))
    memory[str(n)] = result
    return result

def find_best_parameters(data, iterations = 20, thresholds = 20):
    results = []
    ils = ILS()
    progress = 0.0
    iterations, thresholds = [fibonacci(i) for i in range(2, iterations)], [fibonacci(i) for i in range(2, thresholds)]
    iterations, thresholds = split_list(iterations), split_list(thresholds) 
    for i in iterations:        
        for j in thresholds:
            logging.info(f"\nILS run with {i} iterations and {j} threshold")
            logging.info("----------------------")
            solution, elapsed_time = ils.run(data, threshold=j, iterations=i)
            results.append((i, j, solution.cost(), elapsed_time))
            progress = progress + (1.0 / (len(iterations) * len(thresholds)))

            logging.info(f"\nProgress {progress*100:.2f}% \n")
    min_result = min(results, key=lambda result: (result[2],result[3]))
    return min_result


def split_list(list):
    size = len(list)
    low = list[:2]
    middle = int((size - 1 ) / 2)
    medium = list[middle:middle+2]
    high = list[size - 2 :]
    return low + medium + high

def read_nodes_file(filename:str, node_line_start:int, node_line_end:int):
    with open(filename) as file:
        lines = file.readlines()
        raw_nodes = lines[node_line_start:node_line_end]
        return [ create_node(raw_node) for raw_node in raw_nodes ]
        
def read_tour_file(filename:str, node_line_start, node_line_end):
    with open(filename) as file:
        lines = file.readlines()
        raw_nodes_indexes = lines[node_line_start:node_line_end]
        return [ int(index_line.strip()) for index_line in raw_nodes_indexes ]
        

def create_node(raw_node: str):
    node = raw_node.strip().split(" ")
    _, x, y = node
    return [float(x),float(y)]