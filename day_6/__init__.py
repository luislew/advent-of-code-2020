import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def get_groups_from_input():
    group = []
    for line in get_data_from_input():
        if not line:
            yield group
            group = []
        else:
            group.append(line)
    if group:
        yield group
