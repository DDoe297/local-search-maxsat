'''
Solve a given MaxSAT problem using 
1. Stochastic hill climbing
2. Simulated annealing 
3. Tabu search 
algorithms.
'''
import sys

from .simulated_annealing import SimulatedAnnealing
from .stochastic_hill_climbing import StochasticHillClimbing
from .tabu_search import TabuSearch

tabu_search: TabuSearch = TabuSearch(sys.argv[1])
tabu_search.solve(500)
print(f'Tabu Search: {tabu_search}')
stochastic_hill_climbing: StochasticHillClimbing = StochasticHillClimbing(sys.argv[1])
stochastic_hill_climbing.solve(100)
print(f'Stochastic Hill Climbing: {stochastic_hill_climbing}')
simulated_annealing: SimulatedAnnealing = SimulatedAnnealing(sys.argv[1])
simulated_annealing.solve(0.5)
print(f'Simulated Annealing: {simulated_annealing}')
