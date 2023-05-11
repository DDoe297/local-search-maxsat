from functools import reduce
from random import choice, randint


class BaseSolver:
    '''
    Base class for MaxSAT problem solvers.
    '''
    def __init__(self, file_name: str) -> None:
        '''
        Initialize the solver by reading the problem from file and generating a random state.
        Input:
            file_name: str -> The name of the file containing the problem.
        '''
        self.read_file(file_name)
        self.state: list[bool] = \
            [True] + [choice((True, False)) for _ in range(self.number_of_vars)]
        self.fitness: int = self.check_fitness(self.state)

    def generate_all_neighbours(self) -> list[list[bool]]:
        '''
        Generate all neighbours of current state.
        Output:
            list[list[bool]] -> The list of all neighbours.
        '''
        neighbours: list[list[bool]] = []
        for i in range(1, len(self.state)):
            neighbour: list[bool] = self.state[:]
            neighbour[i] = not neighbour[i]
            neighbours.append(neighbour)
        return neighbours

    def read_file(self, file_name: str) -> None:
        '''
        Read the problem from file.
        Input:
            file_name: str -> The name of the file containing the problem.
        '''
        self.clauses: list[list[int]] = []
        with open(file_name, encoding='utf-8') as file:
            self.number_of_vars: int = int(file.readline().split()[0])
            for line in file:
                self.clauses.append(list(map(int, line.split()))[:-1])

    def check_fitness(self, state: list[bool]) -> int:
        '''
        Check the fitness of a state by counting the number of satisfied clauses.
        Input:
            state: list[bool] -> The state to check.
        Output:
            int -> The number of satisfied clauses.
        '''
        def var_or_inverse(var: int) -> bool:
            '''
            Check if a variable or its inverse is satisfied.
            Input:
                var: int -> The variable to check.
            Output:
                bool -> True if the variable or its inverse is satisfied, False otherwise.
            '''
            return state[var] if var > 0 else not state[var]

        def is_clause_sat(clause: list[int]) -> bool:
            '''
            Check if a clause is satisfied.
            Input:
                clause: list[int] -> The clause to check.
            Output:
                bool -> True if the clause is satisfied, False otherwise.
            '''
            return any(map(var_or_inverse, clause))
        return reduce(lambda a, b: a+b, map(is_clause_sat, self.clauses))

    def generate_random_neighbour(self) -> list[bool]:
        '''
        Generate a random neighbour of current state.
        Output:
            list[bool] -> The random neighbour.
        '''
        flip_choice: int = randint(1, self.number_of_vars)
        state: list[bool] = self.state[:]
        state[flip_choice] = not state[flip_choice]
        return state

    def solve(self, stop:float) -> list[bool]:
        '''
        Solve the problem.
        Input:
            stop: float -> The number of iterations the algorithm runs.
        Output:
            list[bool] -> The solution of the problem.
        '''
        raise NotImplementedError()

    def __str__(self) -> str:
        return f'{self.state[1:]}, Number of satisfied clauses: {self.check_fitness(self.state)}'