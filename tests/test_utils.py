import pytest
from tspdux import utils
import networkx as nx
import math

def test_new_city_size():
    N_CITIES = 7
    cities = utils.rand_city_map(N_CITIES)
    assert len(list(cities.nodes())) == N_CITIES

def test_new_city_distance_attribute():
    nodes = [
        [0, 0],
        [0, 1],
        [1, 1]
    ]
    city_map = utils.new_citymap(nodes)
    distances = nx.get_edge_attributes(city_map, "dist")
    print(city_map.edges[(0, 1)])
    assert distances[(0, 1)] == 1
    assert distances[(0, 2)] == 1.4142135623730951
    assert distances[(1, 2)] == 1

def test_city_position_attribute():
    N_CITIES = 5
    cities = utils.rand_city_map(n_cities=N_CITIES)
    positions = nx.get_node_attributes(cities, "pos")
    assert len(positions) == N_CITIES, "Each city should have a position attribute"
    assert len(positions[0]) == 2, "Each position should be a 2D coordinate"

def test_negative_number_of_cities():
    with pytest.raises(ValueError, match="`n_cities` must be >= 0"):
        utils.rand_city_map(n_cities=-1)

def test_decimal_number_of_cities():
    with pytest.raises(ValueError, match="`n_cities` must be an integer"):
        utils.rand_city_map(n_cities=3.14)

def test_calc_city_distance():
    nodes = [
        [0, 0],
        [0, 1],
        [1, 1]
    ]
    expected = {
        (0, 1): {"dist": 1},
        (0, 2): {"dist": 1.4142135623730951},
        (1, 2): {"dist": 1},
    }
    actual = utils.calc_city_distances(utils.new_citymap(nodes))
    comparisons = (math.isclose(e["dist"], a["dist"]) for e, a in zip(expected.values(), actual.values()))
    assert all(comparisons)

# def test_calc_distance():
#     g = nx.Graph()
#     cities = {
#         0: {"pos": [0, 0]},
#         1: {"pos": [0, 3]},
#         2: {"pos": [4, 0]},
#     }
#     g.add_nodes_from(cities.keys())
#     nx.set_node_attributes(g, cities)
#     assert utils.calc_distance(g, 0, 1) == 3
#     assert utils.calc_distance(g, 1, 2) == 5

def test_calc_total_distance():
    nodes = [
        [0, 0],
        [0, 1],
        [1, 1]
    ]
    city_map = utils.new_citymap(nodes)
    assert utils.calc_total_distance(city_map, [0, 1]) == 1
    assert math.isclose(utils.calc_total_distance(city_map, [0, 2]), 1.4142135623730951)
    assert utils.calc_total_distance(city_map, [1, 2]) == 1
    assert utils.calc_total_distance(city_map, [0, 1, 2]) == 1 + 1
    assert math.isclose(utils.calc_total_distance(city_map, [0, 2, 1]), 1.4142135623730951 + 1)
