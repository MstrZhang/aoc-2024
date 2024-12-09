from itertools import combinations

INPUT_FILE = 'day8.txt'


def read_input():
    with open(INPUT_FILE) as file:
        lines = [line.strip() for line in file]
        return lines


def find_nodes(nodes):
    node_map = {}

    for x, row in enumerate(nodes):
        for y, node in enumerate(row):
            if node != '.':
                if node not in node_map:
                    node_map[node] = []
                node_map[node].append((x, y))

    return node_map


def check_antinode(length, width, antinode):
    return antinode[0] >= 0 and antinode[0] < length and antinode[1] >= 0 and antinode[1] < width


def find_antinodes(nodes, part=1):
    length, width = len(nodes), len(nodes[0])
    node_map = find_nodes(nodes)
    antinodes = set()

    for _, positions in node_map.items():
        pos_combinations = list(combinations(positions, 2))

        for p1, p2 in pos_combinations:
            vector_x = p2[0] - p1[0]
            vector_y = p2[1] - p1[1]

            counter = 1
            while True:
                # we don't have to care about direction beecause we will get the other direction with the opposite permutation
                p3 = (p2[0] + counter * vector_x, p2[1] + counter * vector_y)
                p4 = (p1[0] - counter * vector_x, p1[1] - counter * vector_y)

                if part == 2:
                    if check_antinode(length, width, p1):
                        antinodes.add(p1)
                    if check_antinode(length, width, p2):
                        antinodes.add(p2)
                if check_antinode(length, width, p3):
                    antinodes.add(p3)
                if check_antinode(length, width, p4):
                    antinodes.add(p4)

                if part != 2 or (not check_antinode(length, width, p3) and not check_antinode(length, width, p4)):
                    break

                counter += 1

    return len(antinodes)


def part_one(nodes):
    return find_antinodes(nodes)


def part_two(nodes):
    return find_antinodes(nodes, 2)


if __name__ == '__main__':
    nodes = read_input()

    print(part_one(nodes))
    print(part_two(nodes))
