INPUT_FILE = 'day2.txt'


def read_input():
    levels = []

    with open(INPUT_FILE) as file:
        while line := file.readline().split():
            levels.append([int(x) for x in line])

    return levels


def check_safe(level):
    if sorted(level) == level or sorted(level, reverse=True) == level:
        differences = [abs(j - i) for i, j in zip(level, level[1:])]
        if all(diff >= 1 and diff <= 3 for diff in differences):
            return True
    return False


def part_one(levels):
    safe = 0

    for level in levels:
        if check_safe(level):
            safe += 1

    return safe


def part_two(levels):
    safe = 0

    for level in levels:
        if check_safe(level):
            safe += 1
        else:
            # check if level is safe without this element
            for i in range(len(level)):
                if check_safe(level[:i] + level[i+1:]):
                    safe += 1
                    break

    return safe


if __name__ == '__main__':
    levels = read_input()

    print(part_one(levels))
    print(part_two(levels))
