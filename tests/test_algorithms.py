import pytest
import networkx as nx
import math

from tspdux.algorithms import brute_force_tsp
from tspdux.utils import new_citymap, rand_city_map

def test_brute_force():
    nodes = [
        [0, 0],
        [10, 10],
        [0, 1],
        [12, 3]
    ]
    assert brute_force_tsp(new_citymap(nodes)) == [0, 2, 3, 1]

def test_brute_force_raises_error_on_large_inputs():
    city_map = rand_city_map(20)
    with pytest.raises(ValueError, match="n=20 will take a lot of time. If you want to continue, pass `force=True`"):
        brute_force_tsp(city_map)
    