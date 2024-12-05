INPUT_FILE = 'day5.txt'


def read_input():
    with open(INPUT_FILE) as file:
        lines = [line.strip() for line in file]
        break_index = lines.index('')
        return lines[:break_index], lines[break_index + 1:]


def validate_order(target, after_nums, rule_group):
    target_index = rule_group.index(target)
    for num in after_nums:
        try:
            if rule_group.index(num) < target_index:
                return False
        except:
            pass
    return True


def fix_order(target, after_nums, rule_group):
    target_index = rule_group.index(target)
    for num in after_nums:
        try:
            if rule_group.index(num) < target_index:
                rule_group.remove(num)
                rule_group.insert(target_index, num)
        except:
            pass
    return rule_group


def part_one(rule_map, update_rules):
    valid_groups = []

    for rule in update_rules:
        rule_group = rule.split(',')
        group_is_valid = True

        for target in rule_group:
            after_nums = rule_map.get(target, [])
            if validate_order(target, after_nums, rule_group):
                continue
            else:
                group_is_valid = False
                break

        if group_is_valid:
            valid_groups.append(rule_group)

    result = sum([int(group[len(group) // 2]) for group in valid_groups])

    return result


def part_two(rule_map, update_rules):
    invalid_groups = []

    for rule in update_rules:
        rule_group = rule.split(',')

        for target in rule_group:
            after_nums = rule_map.get(target, [])
            if validate_order(target, after_nums, rule_group):
                continue
            else:
                invalid_groups.append(rule_group)
                break

    fixed_groups = []
    for group in invalid_groups:
        while not all([validate_order(target, rule_map.get(target, []), group) for target in group]):
            for target in group:
                after_nums = rule_map.get(target, [])
                group = fix_order(target, after_nums, group)
        fixed_groups.append(group)

    result = sum([int(group[len(group) // 2]) for group in fixed_groups])

    return result


if __name__ == '__main__':
    order_rules, update_rules = read_input()

    rule_map = {}
    for rule in order_rules:
        before, after = rule.split('|')
        rule_map[before.strip()] = rule_map.get(
            before.strip(), []) + after.split(',')

    print(part_one(rule_map, update_rules))
    print(part_two(rule_map, update_rules))
