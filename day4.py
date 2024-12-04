INPUT_FILE = 'day4.txt'


def read_input():
    with open(INPUT_FILE) as file:
        return [line.strip() for line in file]


def find_right(ws, x, y):
    if x + 3 < len(ws[y]):
        if ws[y][x + 1] == 'M' and ws[y][x + 2] == 'A' and ws[y][x + 3] == 'S':
            return True


def find_left(ws, x, y):
    if x - 3 >= 0:
        if ws[y][x - 1] == 'M' and ws[y][x - 2] == 'A' and ws[y][x - 3] == 'S':
            return True


def find_down(ws, x, y):
    if y + 3 < len(ws):
        if ws[y + 1][x] == 'M' and ws[y + 2][x] == 'A' and ws[y + 3][x] == 'S':
            return True


def find_up(ws, x, y):
    if y - 3 >= 0:
        if ws[y - 1][x] == 'M' and ws[y - 2][x] == 'A' and ws[y - 3][x] == 'S':
            return True


def find_diagonal_right_down(ws, x, y):
    if x + 3 < len(ws[y]) and y + 3 < len(ws):
        if ws[y + 1][x + 1] == 'M' and ws[y + 2][x + 2] == 'A' and ws[y + 3][x + 3] == 'S':
            return True


def find_diagonal_left_down(ws, x, y):
    if x - 3 >= 0 and y + 3 < len(ws):
        if ws[y + 1][x - 1] == 'M' and ws[y + 2][x - 2] == 'A' and ws[y + 3][x - 3] == 'S':
            return True


def find_diagonal_right_up(ws, x, y):
    if x + 3 < len(ws[y]) and y - 3 >= 0:
        if ws[y - 1][x + 1] == 'M' and ws[y - 2][x + 2] == 'A' and ws[y - 3][x + 3] == 'S':
            return True


def find_diagonal_left_up(ws, x, y):
    if x - 3 >= 0 and y - 3 >= 0:
        if ws[y - 1][x - 1] == 'M' and ws[y - 2][x - 2] == 'A' and ws[y - 3][x - 3] == 'S':
            return True


def find_forward_mas(ws, x, y):
    if x + 2 < len(ws[y]) and y + 2 < len(ws):
        if ws[x][y] == 'M' and ws[x + 1][y + 1] == 'A' and ws[x + 2][y + 2] == 'S' and ws[x][y + 2] == 'M' and ws[x + 2][y + 2] == 'S':
            return True


def find_backward_mas(ws, x, y):
    if x + 2 < len(ws[y]) and y + 2 < len(ws):
        if ws[x][y] == 'S' and ws[x + 1][y + 1] == 'A' and ws[x + 2][y + 2] == 'M' and ws[x][y + 2] == 'S' and ws[x + 2][y + 2] == 'M':
            return True


def find_ff_mas(ws, x, y):
    if x + 2 < len(ws[y]) and y + 2 < len(ws):
        if ws[x][y] == 'M' and ws[x + 2][y] == 'S' and ws[x + 1][y + 1] == 'A' and ws[x][y + 2] == 'M' and ws[x + 2][y + 2] == 'S':
            return True


def find_bb_mas(ws, x, y):
    if x + 2 < len(ws[y]) and y + 2 < len(ws):
        if ws[x][y] == 'S' and ws[x + 2][y] == 'M' and ws[x + 1][y + 1] == 'A' and ws[x][y + 2] == 'S' and ws[x + 2][y + 2] == 'M':
            return True


def find_fb_mas(ws, x, y):
    if x + 2 < len(ws[y]) and y + 2 < len(ws):
        if ws[x][y] == 'M' and ws[x + 2][y] == 'M' and ws[x + 1][y + 1] == 'A' and ws[x][y + 2] == 'S' and ws[x + 2][y + 2] == 'S':
            return True


def find_bf_mas(ws, x, y):
    if x + 2 < len(ws[y]) and y + 2 < len(ws):
        if ws[x][y] == 'S' and ws[x + 2][y] == 'S' and ws[x + 1][y + 1] == 'A' and ws[x][y + 2] == 'M' and ws[x + 2][y + 2] == 'M':
            return True


def part_one(ws):
    result = 0

    for y in range(len(ws)):
        for x in range(len(ws[y])):
            if ws[y][x] == 'X':
                if find_right(ws, x, y):
                    result += 1
                if find_left(ws, x, y):
                    result += 1
                if find_down(ws, x, y):
                    result += 1
                if find_up(ws, x, y):
                    result += 1
                if find_diagonal_right_down(ws, x, y):
                    result += 1
                if find_diagonal_left_down(ws, x, y):
                    result += 1
                if find_diagonal_right_up(ws, x, y):
                    result += 1
                if find_diagonal_left_up(ws, x, y):
                    result += 1

    return result


def part_two(ws):
    result = 0

    for y in range(len(ws)):
        for x in range(len(ws[y])):
            if find_ff_mas(ws, x, y):
                result += 1
            if find_bb_mas(ws, x, y):
                result += 1
            if find_fb_mas(ws, x, y):
                result += 1
            if find_bf_mas(ws, x, y):
                result += 1

    return result


if __name__ == '__main__':
    ws = read_input()

    print(part_one(ws))
    print(part_two(ws))
