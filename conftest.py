import pytest

from implementations.object_oriented import TreasureMap, BasicTreasureFindingStrategy


@pytest.fixture()
def treasure_map():
    return (
        (55, 14, 25, 52, 21),
        (44, 31, 11, 53, 43),
        (24, 13, 45, 12, 34),
        (42, 22, 43, 32, 41),
        (51, 23, 33, 54, 15)
    )


@pytest.fixture()
def treasure_map_object():
    return TreasureMap(
        (
            (55, 14, 25, 52, 21),
            (44, 31, 11, 53, 43),
            (24, 13, 45, 12, 34),
            (42, 22, 43, 32, 41),
            (51, 23, 33, 54, 15)
        )
    )


@pytest.fixture()
def basic_finding_strategy():
    return BasicTreasureFindingStrategy()
