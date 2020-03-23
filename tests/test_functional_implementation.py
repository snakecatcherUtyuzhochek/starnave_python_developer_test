import pytest

from implementations.functional import get_path_to_treasure


def test_functional_success(treasure_map):
    path = get_path_to_treasure(treasure_map)

    assert path[-1] == 43
    assert path == [11, 55, 15, 21, 44, 32, 13, 25, 43]
