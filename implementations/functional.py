treasure_map = [
        [55, 14, 25, 52, 21],
        [44, 31, 11, 53, 43],
        [24, 13, 45, 12, 34],
        [42, 22, 43, 32, 41],
        [51, 23, 33, 54, 15]
    ]


START_CLUE = (1, 1)


def tuple_to_int(t, dimension=2):
    str_int = ''
    for i in range(dimension):
        str_int += str(t[i])

    return int(str_int)


def convert_tuples_list_to_int_list(l, dimension=2):
    return [tuple_to_int(t, dimension=dimension) for t in l]


def get_path_to_treasure(treasure_map, start_clue=(1, 1)):
    treasure_path = [start_clue]

    def try_next_clue(clue):
        next_clue_str = str(treasure_map[clue[0] - 1][clue[1] - 1])
        next_clue = int(next_clue_str[0]), int(next_clue_str[1])

        if next_clue == clue:
            return clue

        treasure_path.append(next_clue)
        try_next_clue(next_clue)

    try_next_clue(start_clue)

    return convert_tuples_list_to_int_list(treasure_path)


if __name__ == '__main__':
    dimension = int(input('Choose dimension of treasure map:\n'))
    treasure_map = []
    print('Write treasure map using single space as separator\n')
    for i in range(dimension):
        row = tuple(
            map(int, input(f'{i} row:\n').split(" "))
        )
        treasure_map.append(row)

    treasure_map = tuple(treasure_map)
    treasure_path = get_path_to_treasure(treasure_map)

    printable_treasure_path = ''
    for cell in treasure_path:
        printable_treasure_path += f'{cell} '

    print(printable_treasure_path)
