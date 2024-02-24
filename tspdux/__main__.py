import networkx as nx
import matplotlib.pyplot as plt
from tspdux.algorithms import brute_force_tsp
from tspdux.utils import rand_city_map, new_citymap, calc_city_distances
import numpy as np
from scipy.spatial.distance import pdist


# cities = rand_city_map(n_cities=3)
# print(cities.nodes[0]["pos"])
# print(brute_force_tsp(cities))

nodes = [
    [0, 0],
    [10, 10],
    [0, 1],
    [12, 3]
]

city_map = new_citymap(nodes)
print(calc_city_distances(city_map))