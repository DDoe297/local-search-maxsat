'''
MaxSAT problem solver using simulated annealing algorithm.
'''
from math import e
from random import random

from .base_solver import BaseSolver


class SimulatedAnnealing(BaseSolver):
    '''
    Solve MaxSAT problem using simulated annealing algorithm.
    '''

    def solve(self, stop: float) -> list[bool]:
        '''
        Solve the problem using simulated annealing algorithm.
        Input:
            stop: float -> The temperature at which the algorithm stops.
        Output:
            list[bool] -> The solution of the problem.
        '''
        T: float = 100
        while T >= stop:
            neighbour: list[bool] = self.generate_random_neighbour()
            neighbour_fitness: int = self.check_fitness(neighbour)
            if neighbour_fitness >= self.fitness:
                self.state = neighbour
                self.fitness = neighbour_fitness
            elif random() < e**((neighbour_fitness-self.fitness)/T):
                self.state = neighbour
                self.fitness = neighbour_fitness
            T = self.schedule(T)
            if self.fitness == len(self.clauses):
                break
        return self.state

    def schedule(self, T: float) -> float:
        '''
        Schedule the temperature of simulated annealing algorithm.
        Input:
            T: float -> The current temperature.
        Output:
            float -> The next temperature.
        '''
        return T*0.999
