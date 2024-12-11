INPUT_FILE = 'day11.txt'
RULES = {
    'zero': lambda _: 1,
    'even': lambda x: (int(str(x)[:len(str(x))//2]), int(str(x)[len(str(x))//2:])),
    'default': lambda x: x * 2024
}


def read_input():
    with open(INPUT_FILE) as f:
        return list(map(int, f.read().split(' ')))


def loop(stone_map):
    next_stones = {}

    for stone, count in stone_map.items():
        if stone == 0:
            next_stones[RULES['zero'](stone)] = next_stones.get(
                RULES['zero'](stone), 0) + count
        elif len(str(stone)) % 2 == 0:
            left, right = RULES['even'](stone)
            next_stones[left] = next_stones.get(left, 0) + count
            next_stones[right] = next_stones.get(right, 0) + count
        else:
            next_stones[RULES['default'](stone)] = next_stones.get(
                RULES['default'](stone), 0) + count

    return next_stones


def part_one(values):
    stone_map = {value: 1 for value in values}

    for _ in range(25):
        stone_map = loop(stone_map)

    return sum(stone_map.values())


def part_two(values):
    stone_map = {value: 1 for value in values}

    for _ in range(75):
        stone_map = loop(stone_map)

    return sum(stone_map.values())


if __name__ == '__main__':
    values = read_input()

    print(part_one(values))
    print(part_two(values))
