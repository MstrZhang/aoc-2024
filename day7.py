import itertools

INPUT_FILE = 'day7.txt'


def read_input():
    with open(INPUT_FILE) as file:
        lines = [line.strip() for line in file]

        parsed_lines = []
        for line in lines:
            result, values = line.split(':')
            values = values.split(' ')[1:]
            parsed_lines.append((int(result), list(map(int, values))))

        return parsed_lines


def evaluate_equation(values, expected_result, part=1):
    total = 0

    allowed_ops = '+*'
    if part == 2:
        allowed_ops += '|'

    for ops in itertools.product(allowed_ops, repeat=len(values) - 1):
        result = values[0]
        for argument, op in zip(values[1:], ops):
            if op == '+':
                result += argument
            elif op == '*':
                result *= argument
            elif op == '|':
                result = int(f'{result}{argument}')

        if result == expected_result:
            total += expected_result
            break

    return total


def part_one(eqs):
    result = 0

    for eq in eqs:
        expected_result, values = eq
        result += evaluate_equation(values, expected_result)

    return result


def part_two(eqs):
    result = 0

    for eq in eqs:
        expected_result, values = eq
        result += evaluate_equation(values, expected_result, part=2)

    return result


if __name__ == '__main__':
    eqs = read_input()

    print(part_one(eqs))
    print(part_two(eqs))
