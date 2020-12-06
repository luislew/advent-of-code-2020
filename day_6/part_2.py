from functools import reduce

from day_6 import get_groups_from_input


def common_count_in_group(lines):
    return len(reduce(lambda a, b: a & b, (set(line) for line in lines)))


if __name__ == "__main__":
    print(sum(common_count_in_group(group) for group in get_groups_from_input()))
