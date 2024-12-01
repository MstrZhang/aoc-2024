INPUT_FILE = 'day1.txt'


def read_input():
    left = []
    right = []

    with open(INPUT_FILE) as file:
        while line := file.readline():
            l, r = line.split('   ')
            left.append(int(l.rstrip()))
            right.append(int(r.rstrip()))

    return left, right


def part_one(left, right):
    lsorted = sorted(left)
    rsorted = sorted(right)

    result = 0
    for i in range(len(lsorted)):
        diff = abs(lsorted[i] - rsorted[i])
        result += diff

    return result


def part_two(left, right):
    frequency_map = {}
    for num in right:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    result = 0
    for num in left:
        if num in frequency_map:
            result += frequency_map[num] * num
        else:
            result += 0

    return result


if __name__ == '__main__':
    left, right = read_input()

    print(part_one(left, right))
    print(part_two(left, right))
