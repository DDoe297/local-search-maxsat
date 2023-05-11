'''
MaxSAT problem solver using tabu search algorithm.
'''
from .base_solver import BaseSolver


class TabuSearch(BaseSolver):
    '''
    Solve MaxSAT problem using tabu search algorithm.
    '''
    def __init__(self, file_name: str) -> None:
        super().__init__(file_name)
        self.tabu_tenure: list[int] = [0 for _ in range(self.number_of_vars+1)]

    def solve(self, stop: float) -> list[bool]:
        '''
        Solve the problem using tabu search algorithm.
        Input:
            stop: float -> The number of iterations the algorithm runs.
        Output:
            list[bool] -> The solution of the problem.
        '''
        for _ in range(int(stop)):
            neighbours: list[tuple[int, list[bool]]] = \
                self.generate_allowed_neighbours()
            i, self.state = \
                max(neighbours, key=lambda a: self.check_fitness(a[1]))
            self.fitness = self.check_fitness(self.state)
            self.tabu_tenure = \
                list(map(lambda a: max(0, a-1), self.tabu_tenure))
            self.tabu_tenure[i] = self.number_of_vars//2
            if self.fitness == len(self.clauses):
                break
        return self.state

    def generate_allowed_neighbours(self) -> list[tuple[int, list[bool]]]:
        '''
        Generate all allowed neighbours of current state (neighbours that are not in tabu list).
        Output:
            list[tuple[int, list[bool]]] -> The list of all allowed neighbours.
        '''
        allowed_states: list[int] = \
            [i for i in range(1, self.number_of_vars+1) if self.tabu_tenure[i] == 0]
        neighbours: list[tuple[int, list[bool]]] = []
        for i in allowed_states:
            neighbour: list[bool] = self.state[:]
            neighbour[i] = not neighbour[i]
            neighbours.append((i, neighbour))
        return neighbours
