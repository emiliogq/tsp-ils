from abc import ABC, abstractmethod
from time import time
from random import randrange
from math import sqrt
import logging

from solution import Solution


class ILS(ABC):
    def __init__(self) -> None:
        pass

    def init_solution_history(self):
        self.history = []

    def construct_initial_solution(self, data):
        permutation = data.copy()
        size = len(permutation)
        for i in range(size):
            shuffle_index = randrange(i, size)
            permutation[shuffle_index], permutation[i] = permutation[i], permutation[shuffle_index]
        
        return Solution(permutation)

    def tour_cost(self, nodes):
        distance = 0.0
        size = len(nodes)
        for i in range(size-1):
            distance += euclidean_distance(nodes[i], nodes[i+1])
        distance += euclidean_distance(nodes[-1],nodes[0])
        return distance

    def local_search(self, solution, threshold):
        i = 0
        while( i < threshold):
            new_solution = Solution(stochastic_two_opt(solution.nodes))
            new_solution.cost = self.tour_cost(new_solution.nodes)
            solution = new_solution if (new_solution < solution) else solution
            i += 1
        return solution


    def perturb(self,solution:Solution):
        new_solution = Solution(double_bridge_move(solution.nodes))
        new_solution.cost = self.tour_cost(new_solution.nodes)
        return new_solution


    def acceptance_criterion(self, base_solution:Solution, best_solution:Solution, solution:Solution, i:int, threshold:int, degradation_grace_period = -1):    
        grace_period = degradation_grace_period
        if (solution < best_solution):
            best_solution = solution
            logging.info(f"The best cost {best_solution.cost} is found at {i+1}th iteration with threshold {threshold}")
        if (solution <= base_solution):
            base_solution = solution
        elif len(self.history) > 0 and grace_period > -1:
            grace_period -= 1
            if grace_period == 0:
                solution = self.history.pop()
                logging.info(f"Degraded base solution with cost {base_solution.cost} to the solution with cost {solution.cost}")
                base_solution, solution
                grace_period = degradation_grace_period
        return base_solution, best_solution

    def register(self, solution:Solution):
        self.history.append(solution)

    def run(self, data, threshold = 50, iterations: int = 1000, degradation_grace_period = -1):
        start_time = time()
        self.init_solution_history()
        base_solution = self.construct_initial_solution(data)
        base_solution.cost = self.tour_cost(base_solution.nodes)
        # Getting local optima
        best_solution = base_solution = self.local_search(base_solution, threshold)
        i = 0
        while ( i < iterations):
            solution = self.perturb(base_solution)
            self.register(solution)
            solution = self.local_search(solution, threshold)        
            base_solution, best_solution = self.acceptance_criterion(base_solution, best_solution, solution, i, threshold, degradation_grace_period)
            i += 1
        
        end_time = time()
        elapsed_time = end_time - start_time
        logging.info(f"Solution = {solution}")
        logging.info(f"Elapsed time: {elapsed_time}")
        return best_solution, elapsed_time

def euclidean_distance(node_a, node_b):
    sum = 0.0
    for xa, xb in zip(node_a, node_b):
        sum += ((xa-xb)**2)
    return sqrt(sum)

def stochastic_two_opt(items):
    result, size = items.copy(), len(items)
    
    p1, p2 = randrange(0, size), randrange(0, size)
    
    excluded_indexes = set([ size-1 if p1 == 0 else p1-1, p1, 0 if p1 == size-1 else p1+1])

    while p2 in excluded_indexes:
        p2 = randrange(0, size)

    if p2 < p1:
        p1, p2 = p2, p1

    result[p1:p2] = reversed(result[p1:p2])

    return result

"""
The double-bridge move involves partitioning a solution into 4 pieces (a, b, c, d)
and randomly order them, e.g. (a,d,b,c).
This is equivalent to a 4 opt move perturbation. 
"""
def double_bridge_move(items):
    items = items
    slice_length = int(len(items) / 4)
    part_one = 1 + randrange(0, slice_length)
    part_two = part_one + 1 + randrange(0, slice_length)
    part_three = part_two + 1 + randrange(0, slice_length)
    items = items[0:part_one] + items[part_three:] + items[part_two:part_three] + items[part_one:part_two]
    return items
        