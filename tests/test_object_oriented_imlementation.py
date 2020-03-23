import pytest

from implementations.object_oriented import (
    Clue, TreasureMap, Path, TreasureFinder, BasicTreasureFindingStrategy
)


def test_treasure_map(treasure_map_object):
    clue = treasure_map_object.get_next_clue(Clue((1, 1)))

    assert clue.get_int_str() == Clue((5, 5)).get_int_str()


def test_object_oriented_success(treasure_map_object, basic_finding_strategy):
    context = TreasureFinder(basic_finding_strategy)
    path = context.execute_strategy(treasure_map_object)

    assert len(path.clues_list) == 9
    assert path.__repr__() == "11 55 15 21 44 32 13 25 43 "
