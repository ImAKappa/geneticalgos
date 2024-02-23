import pytest
from tspdux import utils
import networkx as nx

def test_new_city():
    N_CITIES = 7
    cities = utils.rand_city_map(N_CITIES)
    assert len(list(cities.nodes())) == N_CITIES

def test_city_position_attribute():
    N_CITIES = 5
    cities = utils.rand_city_map(n_cities=N_CITIES)
    positions = nx.get_node_attributes(cities, "pos")
    assert len(positions) == N_CITIES, "Each city should have a position attribute"
    assert len(positions[0]) == 2, "Each position should be a 2D coordinate"
    print(cities.edges(data=True))

def test_negative_number_of_cities():
    with pytest.raises(ValueError, match="`n_cities` must be >= 0"):
        utils.rand_city_map(n_cities=-1)

def test_decimal_number_of_cities():
    with pytest.raises(ValueError, match="`n_cities` must be an integer"):
        utils.rand_city_map(n_cities=3.14)

def test_calc_distance():
    g = nx.Graph()
    cities = {
        0: {"pos": [0, 0]},
        1: {"pos": [0, 3]},
        2: {"pos": [4, 0]},
    }
    g.add_nodes_from(cities.keys())
    nx.set_node_attributes(g, cities)
    assert utils.calc_distance(g, 0, 1) == 3
    assert utils.calc_distance(g, 1, 2) == 5

def test_calc_total_distance():
    g = nx.Graph()
    cities = {
        0: {"pos": [0, 0]},
        1: {"pos": [0, 3]},
        2: {"pos": [4, 0]},
    }
    g.add_nodes_from(cities.keys())
    nx.set_node_attributes(g, cities)
    assert utils.calc_total_distance(g, [(0, 1)]) == 3
    assert utils.calc_total_distance(g, [(1, 2)]) == 5
    assert utils.calc_total_distance(g, [(0, 1), (1, 2)]) == 8

def test_create_edgelist_from_nodes():
    assert utils.create_edge_list([1, 2, 3, 4]) == [(1, 2), (2, 3), (3, 4)]
    assert utils.create_edge_list([1, 2, 3, 4], closed=True) == [(1, 2), (2, 3), (3, 4), (4, 1)]
