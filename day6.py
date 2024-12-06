INPUT_FILE = 'day6.txt'


def read_input():
    with open(INPUT_FILE) as file:
        lines = [line.strip() for line in file]
        return lines


def find_guard(map):
    for x, row in enumerate(map):
        if '^' in row:
            y = row.index('^')
            return (x, y)


def get_next_step(map, guard, direction, obstacle=None):
    x, y = guard

    if direction == 'up':
        try:
            if map[x - 1][y] == '#' or (x - 1, y) == obstacle:
                direction = 'right'
            else:
                x -= 1
        except:
            x -= 1
    elif direction == 'right':
        try:
            if map[x][y + 1] == '#' or (x, y + 1) == obstacle:
                direction = 'down'
            else:
                y += 1
        except:
            y += 1
    elif direction == 'down':
        try:
            if map[x + 1][y] == '#' or (x + 1, y) == obstacle:
                direction = 'left'
            else:
                x += 1
        except:
            x += 1
    elif direction == 'left':
        try:
            if map[x][y - 1] == '#' or (x, y - 1) == obstacle:
                direction = 'up'
            else:
                y -= 1
        except:
            y -= 1

    return (x, y), direction


def evaluate_path(map, initial_guard, initial_direction, obstacle=None):
    loop = False
    inside = True
    guard = initial_guard
    direction = initial_direction
    steps = set()
    seen = set()

    while inside and not loop:
        steps.add(guard)
        seen.add((guard, direction))
        guard, direction = get_next_step(map, guard, direction, obstacle)

        # if we have seen the guard and direction before, we have a loop
        loop = (guard, direction) in seen

        # if the guard is out of bounds, we have reached the end
        x, y = guard
        inside = x > 0 and y > 0 and x < len(map) and y < len(map[0])

    return steps, loop


def part_one(map, guard, direction):
    path, _ = evaluate_path(map, guard, direction)
    return len(path) + 1


def part_two(map, guard, direction):
    path, _ = evaluate_path(map, guard, direction)

    loops = 0
    for obstacle in path:
        _, loop = evaluate_path(map, guard, direction, obstacle)
        if loop:
            loops += 1

    return loops


if __name__ == '__main__':
    map = read_input()

    guard = find_guard(map)
    direction = 'up'

    print(part_one(map, guard, direction))
    print(part_two(map, guard, direction))
