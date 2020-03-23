class Clue:
    """
    Represents clue in different types
    """
    def __init__(self, tuple_representation):
        self.tuple_representation = tuple_representation

    @classmethod
    def from_int(cls, clue_int):
        """
        Returns Clue object using it`s int representation
        """
        s = str(clue_int)

        return cls(
            (int(s[0]), int(s[1]))
        )

    def get_tuple(self):
        return self.tuple_representation

    def get_int_str(self):
        tuple_representation = self.tuple_representation

        return f'{tuple_representation[0]}' + f'{tuple_representation[1]}'


class TreasureMap:
    """
    Represents treasure map and basic operations with it
    """
    def __init__(self, tuple_representation):
        self.tuple_representation = tuple_representation

    def get_next_clue(self, clue):
        """
        Returns item found on current map using given clue

        Args:
           clue (Clue):  The clue used to get next.

        Returns:
           Clue.  The next clue::
        """
        clue_tuple = clue.get_tuple()
        next_clue_int = self.tuple_representation[clue_tuple[0] - 1][clue_tuple[1] - 1]

        return Clue.from_int(next_clue_int)


class Path:
    """
    Represents full path to the clue
    """
    def __init__(self, start_clue=Clue((1, 1))):
        self.clues_list = [start_clue]

    def add_clue(self, clue):
        """
        Adds clue to the path

        Args:
           clue (Clue):  The clue used to get next.
        """
        self.clues_list.append(clue)

    def __repr__(self):
        printable_representation = ""
        for clue in self.clues_list:
            printable_representation += f'{clue.get_int_str()} '

        return printable_representation


class TreasureFinder:
    """
    Treasure finding context. Could use different strategies
    """
    def __init__(self, strategy):
        """
        Initiates finder object assigning strategy it will use

        Args:
           clue (Clue):  The clue used to get next.
        """
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, treasure_map):
        return self.strategy.get_treasure_path(treasure_map)


class AbstractTreasureFindingStrategy:
    """
    Represents strategy interface for treasure finding context
    """
    def get_treasure_path(self, treasure_map):
        raise NotImplementedError


class BasicTreasureFindingStrategy(AbstractTreasureFindingStrategy):
    """
    Basic implementation of TreasureFindingStrategy interface
    """
    def get_treasure_path(self, treasure_map, start_clue=Clue((1, 1))):
        path = Path()
        clue = start_clue
        while True:
            next_clue = treasure_map.get_next_clue(clue)
            if clue.get_int_str() == next_clue.get_int_str():
                break

            path.add_clue(next_clue)
            clue = next_clue

        return path
