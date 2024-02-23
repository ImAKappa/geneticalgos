import networkx as nx
import matplotlib.pyplot as plt
from tspdux.algorithms import lexigraphic_permutations
from tspdux.utils import rand_city_map


cities = rand_city_map(n_cities=3)
print(lexigraphic_permutations(cities))