import networkx as nx
import matplotlib.pyplot as plt
from tspdux.algorithms import brute_force_tsp
from tspdux.utils import rand_city_map


cities = rand_city_map(n_cities=3)
print(cities.nodes[0]["pos"])
print(brute_force_tsp(cities))