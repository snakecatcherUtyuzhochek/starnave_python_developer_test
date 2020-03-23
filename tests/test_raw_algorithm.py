import pytest


def test_algorithm(treasure_map):
    clue = (1, 1)
    while True:
        next_clue_str = str(treasure_map[clue[0] - 1][clue[1] - 1])
        next_clue = int(next_clue_str[0]), int(next_clue_str[1])
        if next_clue == clue:
            break
        clue = next_clue

    assert clue == (4, 3)
