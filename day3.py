import re

INPUT_FILE = 'day3.txt'


def read_input():
    with open(INPUT_FILE) as file:
        return [line.strip() for line in file]


def part_one(memory):
    result = 0

    for line in memory:
        products = re.findall(r'mul\(\d*,\d*\)', line)

        for product in products:
            a, b = map(int, re.findall(r'\d+', product))
            result += a * b

    return result


def part_two(memory):
    result = 0
    ops = []

    for line in memory:
        products = re.compile(r'mul\((\d*),(\d*)\)')
        for m in products.finditer(line):
            a, b = map(int, re.findall(r'\d+', m.group()))
            product = a * b
            ops.append((m.start(), product))

        dos = re.compile(r'do\(\)')
        for m in dos.finditer(line):
            ops.append((m.start(), m.group()))

        donts = re.compile(r'don\'t\(\)')
        for m in donts.finditer(line):
            ops.append((m.start(), m.group()))

    ops.sort(key=lambda x: x[0])

    apply = True
    for op in ops:
        if op[1] == 'do()':
            apply = True
        elif op[1] == "don't()":
            apply = False
        elif apply:
            result += op[1]

    return result


if __name__ == '__main__':
    memory = read_input()

    print(part_one(memory))
    print(part_two(memory))
