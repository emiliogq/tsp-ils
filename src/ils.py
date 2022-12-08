from time import time
from random import randrange
from math import sqrt
import logging

def construct_initial_solution(data):
    permutation = data.copy()
    size = len(permutation)
    for i in range(size):
        shuffle_index = randrange(i, size)
        permutation[shuffle_index], permutation[i] = permutation[i], permutation[shuffle_index]
    
    return permutation

def euclidean_distance(node_a, node_b):
    sum = 0.0
    for xa, xb in zip(node_a, node_b):
        sum += ((xa-xb)**2)
    return sqrt(sum)

def tour_cost(solution):
    distance = 0.0
    size = len(solution)
    for i in range(size-1):
        distance += euclidean_distance(solution[i], solution[i+1])
    distance += euclidean_distance(solution[-1],solution[0])
    return distance

def stochastic_two_opt(solution):
    result, size = solution.copy(), len(solution)
    
    p1, p2 = randrange(0, size), randrange(0, size)
    
    excluded_indexes = set([ size-1 if p1 == 0 else p1-1, p1, 0 if p1 == size-1 else p1+1])
   
    while p2 in excluded_indexes:
        p2 = randrange(0, size)

    if p2 < p1:
        p1, p2 = p2, p1

    result[p1:p2] = reversed(result[p1:p2])

    return result

def local_search(solution, cost, threshold):
    i = 0
    while( i < threshold):
        new_solution = stochastic_two_opt(solution)
        new_cost = tour_cost(new_solution)
        if (new_cost < cost):
            solution, cost = new_solution, new_cost
        i += 1
    return solution, cost

"""
The double-bridge move involves partitioning a solution into 4 pieces (a, b, c, d)
and randomly order them, e.g. (a,d,b,c).
This is equivalent to a 4 opt move perturbation. 
"""
def double_bridge_move(solution):
    slice_length = len(solution) / 4
    part_one = 1 + randrange(0, slice_length)
    part_two = part_one + 1 + randrange(0, slice_length)
    part_three = part_two + 1 + randrange(0, slice_length)
    return solution[0:part_one] + solution[part_three:] + solution[part_two:part_three] + solution[part_one:part_two]
    
def perturb(solution, history:list):
    new_solution = double_bridge_move(solution)
    new_cost = tour_cost(new_solution)
    history.append((new_solution, new_cost))
    return new_solution, new_cost

def iterated_local_search(data, threshold = 50, iterations: int = 1000, degradation_grace_period = -1):
    start_time = time()
    history = []
    grace_period = degradation_grace_period
    base_solution = construct_initial_solution(data)
    base_cost = tour_cost(base_solution)
    # Getting local optima
    best_solution, best_cost = base_solution, base_cost = local_search(base_solution, base_cost, threshold)
    i = 0
    while ( i < iterations):
        solution, cost = perturb(base_solution, history)
        solution, cost = local_search(solution, cost, threshold)        
        if (cost < best_cost):
            best_solution = solution
            best_cost = cost
            logging.info(f"The best cost {best_cost} is found at {i+1}th iteration with threshold {threshold}")
        if (cost <= base_cost):
            base_solution, base_cost = solution, cost
        elif len(history) > 0 and grace_period > -1:
            grace_period -= 1
            if grace_period == 0:
                solution, cost = history.pop()
                logging.info(f"Degraded base solution with cost {base_cost} to the solution with cost {cost}")
                base_solution, base_cost = solution, cost
                grace_period = degradation_grace_period
        i += 1
    
    end_time = time()
    elapsed_time = end_time - start_time
    logging.info(f"Cost = {best_cost}")
    logging.info(f"Elapsed time: {elapsed_time}")
    return best_solution, best_cost, elapsed_time