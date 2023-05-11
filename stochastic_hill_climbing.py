'''
MaxSAT problem solver using stochastic hill climbing algorithm.
'''
from random import choices

from .base_solver import BaseSolver


class StochasticHillClimbing(BaseSolver):
    '''
    Solve MaxSAT problem using stochastic hill climbing algorithm.
    '''

    def solve(self, stop: float) -> list[bool]:
        '''
        Solve the problem using stochastic hill climbing algorithm.
        Input:
            stop: float -> The number of iterations the algorithm runs.
        Output:
            list[bool] -> The solution of the problem.
        '''
        for _ in range(int(stop)):
            neighbours: list[list[bool]] = self.generate_all_neighbours()
            weights: list[int] = list(map(lambda a: max(0, a-self.fitness),
                                          map(self.check_fitness, neighbours)))
            try:
                next_neighbour: list[bool] = choices(
                    neighbours, weights, k=1)[0]
            except IndexError:
                break
            self.state = next_neighbour
            self.fitness = self.check_fitness(self.state)
            if self.fitness == len(self.clauses):
                break
        return self.state
