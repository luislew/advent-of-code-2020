import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def tree_collisions_from_top_to_bottom_for_slope(data, right, down):
    collisions = 0
    x_pos = 0
    for y_pos, line in enumerate(data):
        if y_pos % down:
            continue

        if line[x_pos % len(line)] == "#":
            collisions += 1
        x_pos += right
    return collisions
