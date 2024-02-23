"""utils

Utility functions
"""
import numpy as np
import networkx as nx
import math
from tspdux.libtypes import EdgeList

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
    return city_map

def calc_distance(city_map: nx.Graph, city_1: int, city_2: int) -> float:
    """Calculates the distance to travel between cities, based on their positions"""
    return math.dist(city_map.nodes[city_1]["pos"], city_map.nodes[city_2]["pos"])

def calc_total_distance(city_map: nx.Graph, routes: EdgeList) -> float:
    """Calculates the total distance to travel between cities, based on their position"""
    return sum(calc_distance(city_map, city_1=r[0], city_2=r[1]) for r in routes)

def create_edge_list(nodes: list[int], closed=False) -> EdgeList:
    edgelist = [(n1, n2) for n1, n2 in zip(nodes, nodes[1:])]
    if closed:
        edgelist.append((nodes[-1], nodes[0]))
    return edgelist