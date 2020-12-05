import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def get_number_for_spec(spec):
    min_number, max_number = 0, 2 ** len(spec) - 1
    for char in spec:
        half_distance = (max_number - min_number + 1) // 2
        if half_distance == 1:
            return min_number if char in ("F", "L") else max_number
        elif char in ("F", "L"):
            max_number -= half_distance
        else:
            min_number += half_distance


def get_row_and_col_for_boarding_pass(boarding_pass):
    return get_number_for_spec(boarding_pass[:7]), get_number_for_spec(boarding_pass[7:])


def get_seat_id_for_boarding_pass(boarding_pass):
    row_number, col_number = get_row_and_col_for_boarding_pass(boarding_pass)
    return 8 * row_number + col_number
