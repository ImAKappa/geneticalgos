"""algorithms
"""
import numpy as np
import networkx as nx
from itertools import permutations

from tspdux.utils import calc_total_distance

def brute_force_tsp(city_map: nx.Graph, closed=False, force=False) -> list[int]:
    """Computes the optimal path to traverse a list of 2D points
    Warning: This function does NOT scale well with the size of the graph (O(n!)) for n nodes
    For n >= 10 the function will raise an error unless you force it
    """
    if city_map.number_of_nodes() > 10 and not force:
        raise ValueError(f"n={len(city_map)} will take a lot of time. If you want to continue, pass `force=True`")
    city_permutations = permutations(list(city_map.nodes))
    shortest_distance = np.inf
    shortest_route = None
    for route in city_permutations:
        dist = calc_total_distance(city_map, route)
        if dist < shortest_distance:
            shortest_distance = dist
            shortest_route = route
    return list(shortest_route)
