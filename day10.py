INPUT_FILE = 'day10.txt'


def read_input(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f]


def find_starts(trail_map):
    starts = []
    for x, row in enumerate(trail_map):
        if '0' in row:
            starts += [(x, y) for y in range(len(row)) if row[y] == '0']
    return starts


def in_grid(trail_map, x, y):
    return x >= 0 and x < len(trail_map) and y >= 0 and y < len(trail_map[0])


def bfs(trail_map, start, distinct=False):
    score = 0
    queue = [start]
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        x, y = queue.pop(0)

        if (x, y) in visited:
            continue

        if not distinct:
            visited.add((x, y))

        elevation = trail_map[x][y]
        if elevation == '9':
            score += 1
            continue

        edges = [(x + dx, y + dy) for dx, dy in directions if in_grid(trail_map, x + dx, y + dy)
                 and trail_map[x + dx][y + dy] == str(int(elevation) + 1)]
        queue += edges

    return score


def part_one(trail_map):
    starts = find_starts(trail_map)
    return sum(bfs(trail_map, start) for start in starts)


def part_two(trail_map):
    starts = find_starts(trail_map)
    return sum(bfs(trail_map, start, distinct=True) for start in starts)


if __name__ == '__main__':
    trail_map = read_input(INPUT_FILE)

    print(part_one(trail_map))
    print(part_two(trail_map))
