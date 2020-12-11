from day_11 import (
    DIRECTION_STEPS,
    get_occupied_seat_count,
    get_stable_seat_configuration,
    is_valid_seat_index,
)


def get_adjacent_seats_at_index(seat_configuration, index):
    row, col = index
    row_size = len(seat_configuration)
    col_size = len(seat_configuration[0])
    adjacent_seat_indices = [(row + row_diff, col + col_diff) for row_diff, col_diff in DIRECTION_STEPS]
    return [
        seat_configuration[seat_idx[0]][seat_idx[1]]
        for seat_idx in adjacent_seat_indices
        if is_valid_seat_index(seat_idx, row_size, col_size)
    ]


if __name__ == "__main__":
    stable_seat_configuration = get_stable_seat_configuration(get_adjacent_seats_at_index, 4)
    print(get_occupied_seat_count(stable_seat_configuration))
