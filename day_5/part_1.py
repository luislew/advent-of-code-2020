from day_5 import get_data_from_input, get_seat_id_for_boarding_pass


if __name__ == "__main__":
    data = get_data_from_input()
    print(max(get_seat_id_for_boarding_pass(bp) for bp in data))
