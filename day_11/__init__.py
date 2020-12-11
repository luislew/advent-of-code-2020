import os
from itertools import chain

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

DIRECTION_STEPS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def get_initial_seat_configuration():
    return [list(line) for line in get_data_from_input()]


def is_valid_seat_index(index, row_size, col_size):
    row, col = index
    return 0 <= row < row_size and 0 <= col < col_size


def update_seat_configuration(seat_configuration, adjacent_seat_fn, max_occupied_count):
    indices_to_flip = []
    for row_idx, row in enumerate(seat_configuration):
        for col_idx, state in enumerate(row):
            seat_idx = (row_idx, col_idx)
            adjacent_states = adjacent_seat_fn(seat_configuration, seat_idx)
            occupied_count = adjacent_states.count("#")
            if (state == "L" and not occupied_count) or (state == "#" and occupied_count >= max_occupied_count):
                indices_to_flip.append(seat_idx)

    for row_idx, col_idx in indices_to_flip:
        state = seat_configuration[row_idx][col_idx]
        seat_configuration[row_idx][col_idx] = "#" if state == "L" else "L"
    return seat_configuration, not indices_to_flip


def get_stable_seat_configuration(adjacent_seat_fn, max_occupied_count):
    seat_configuration = get_initial_seat_configuration()
    stable = False
    while not stable:
        seat_configuration, stable = update_seat_configuration(seat_configuration, adjacent_seat_fn, max_occupied_count)
    return seat_configuration


def get_occupied_seat_count(seat_configuration):
    return sum(1 for state in chain.from_iterable(seat_configuration) if state == "#")
