"""algorithms
"""
import numpy as np
from tspdux.libtypes import EdgeList
import networkx as nx
from itertools import permutations

from tspdux.utils import create_edge_list, calc_total_distance

def lexigraphic_permutations(city_map: nx.Graph) -> EdgeList:
    """Computes the optimal path to traverse a list of 2D points
    Warning: This function does NOT scale well (O(n!))
    """
    city_permutations = list(permutations(list(city_map.nodes)))
    city_route_permutations = [create_edge_list(p, closed=True) for p in city_permutations]
    shortest_distance = np.inf
    shortest_route_idx = None
    for i, route in enumerate(city_route_permutations):
        dist = calc_total_distance(city_map, route)
        if dist < shortest_distance:
            shortest_distance = dist
            shortest_route_idx = i
    return city_route_permutations[shortest_route_idx]
