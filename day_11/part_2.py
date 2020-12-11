from day_11 import (
    DIRECTION_STEPS,
    get_occupied_seat_count,
    get_stable_seat_configuration,
    is_valid_seat_index,
)


def get_visible_seats_at_index(seat_configuration, index):
    row, col = index
    row_size = len(seat_configuration)
    col_size = len(seat_configuration[0])
    states = []
    for row_diff, col_diff in DIRECTION_STEPS:
        search_row, search_col = row + row_diff, col + col_diff
        while is_valid_seat_index((search_row, search_col), row_size, col_size):
            state = seat_configuration[search_row][search_col]
            if state != ".":
                states.append(state)
                break
            search_row, search_col = search_row + row_diff, search_col + col_diff
    return states


if __name__ == "__main__":
    stable_seat_configuration = get_stable_seat_configuration(get_visible_seats_at_index, 5)
    print(get_occupied_seat_count(stable_seat_configuration))
