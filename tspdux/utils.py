"""utils

Utility functions
"""
import numpy as np
import networkx as nx
import math
from scipy.spatial.distance import pdist

def rand_city_map(n_cities: int, density=0.2) -> nx.Graph:
    """Creates a graph of cities in 2D space
    
    The verticies have a 'position' attribute
    The edges have a 'distance' attribute that is calculated from the city positions
    """
    if n_cities < 0:
        raise ValueError("`n_cities` must be >= 0") 
    if not isinstance(n_cities, int):
        raise ValueError("`n_cities` must be an integer")
    city_map: nx.Graph = nx.random_geometric_graph(n=n_cities, radius=1/density, dim=2)
    nx.set_edge_attributes(city_map, calc_city_distances(city_map))
    return city_map

def new_citymap(nodes: list[list[int]]) -> nx.Graph:
    """Creates a new graph from a list of 2D node positions.
    Note that the nodes are 0-indexed
    """
    city_map = nx.Graph()
    for i, pos in enumerate(nodes):
        city_map.add_node(i, pos=pos)
    dist_map = calc_city_distances(city_map)
    city_map.add_edges_from(dist_map.keys())
    nx.set_edge_attributes(city_map, dist_map)
    return city_map

def calc_distance(city_map: nx.Graph, city_1: int, city_2: int) -> float:
    """Calculates the distance to travel between cities, based on their positions"""
    return math.dist(city_map.nodes[city_1]["pos"], city_map.nodes[city_2]["pos"])

def calc_city_distances(city_map: nx.Graph) -> dict[tuple[int, int], float]:
    """Creates a dictionary of the distances between every pair of nodes in a graph"""
    positions = np.array(list(nx.get_node_attributes(city_map, "pos").values()))
    dists = pdist(positions)
    dist_idx = 0
    dist_map = {}
    for i in range(len(positions)-1):
        for j in range(i+1, len(positions)):
            dist_map[(i, j)] = {"dist": dists[dist_idx]}
            dist_idx += 1
    return dist_map

def calc_total_distance(city_map: nx.Graph, route: list[int]) -> float:
    """Calculates the total distance to travel between cities, based on their position"""
    # return sum(calc_distance(city_map, city_1, city_2) for city_1, city_2 in zip(route, route[1:]))
    return nx.path_weight(city_map, path=route, weight="dist")