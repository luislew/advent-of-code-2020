from day_5 import get_data_from_input, get_seat_id_for_boarding_pass


def find_missing_seat_id_for_data(data):
    sorted_seat_ids = sorted(get_seat_id_for_boarding_pass(bp) for bp in data)
    # Look for consecutive seat IDs apart by 2
    previous_seat_id = sorted_seat_ids[0]
    for seat_id in sorted_seat_ids[1:]:
        if seat_id - previous_seat_id == 2:
            return seat_id - 1
        previous_seat_id = seat_id


if __name__ == "__main__":
    data = get_data_from_input()
    print(find_missing_seat_id_for_data(data))
