INPUT_FILE = 'day9.txt'


def read_input():
    with open(INPUT_FILE) as file:
        line = [line.strip() for line in file][0]
        return line


def generate_input_stream(disk_map, part=1):
    result = []
    spaces = []
    files = []
    counter = 0

    for i, char in enumerate(disk_map):
        if i % 2 == 0:
            if part == 2:
                files.append((counter, len(result), int(char)))
            result += [counter for _ in range(int(char))]
            counter += 1
        else:
            if part == 2:
                spaces.append((len(result), int(char)))
            result += ['.' for _ in range(i, i + int(char))]

    return result, spaces, files


def part_one(disk_map):
    result, _, _ = generate_input_stream(disk_map)

    # brute force is very slow on python3 lol
    # much faster with pypy
    try:
        while '.' in result:
            result[result.index('.')] = result.pop()
    except:
        pass

    return sum([x * i for i, x in enumerate(result)])


def part_two(disk_map):
    result, spaces, files = generate_input_stream(disk_map, 2)

    while files:
        file_id, file_idx, file_count = files.pop()
        for i, space in enumerate(spaces):
            space_index, space_count = space

            if space_count >= file_count and space_index < file_idx:
                # move file to empty space
                result[space_index: space_index +
                       file_count] = [file_id] * file_count
                # replace file with empty space
                result[file_idx: file_idx + file_count] = ["."] * file_count
                # update old empty space's position and size
                spaces[i] = (space_index + file_count,
                             space_count - file_count)
                break

    return sum(i * int(x) for i, x in enumerate(result) if x != '.')


if __name__ == '__main__':
    disk_map = read_input()

    print(part_one(disk_map))
    print(part_two(disk_map))
