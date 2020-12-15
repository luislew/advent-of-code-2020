from day_15 import get_data_from_input, get_nth_number

TEST_CASES = [
    ([0,3,6], 436),
    ([1,3,2], 1),
    ([2,1,3], 10),
    ([1,2,3], 27),
    ([2,3,1], 78),
    ([3,2,1], 438),
    ([3,1,2], 1836),
]


if __name__ == "__main__":
    for starting_numbers, result in TEST_CASES:
        assert get_nth_number(starting_numbers, 2020) == result

    print(get_nth_number(get_data_from_input(), 2020))
