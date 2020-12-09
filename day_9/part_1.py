from collections import deque
from itertools import combinations

from day_9 import get_data_from_input


def get_valid_sums_for_preamble(preamble):
    return {i + j for i, j in combinations(preamble, 2)}


def find_first_invalid_number(data, preamble_length=25):
    preamble = deque(data[:preamble_length], maxlen=preamble_length)
    valid_sums = get_valid_sums_for_preamble(preamble)

    for number in data[preamble_length:]:
        if number not in valid_sums:
            return number

        preamble.append(number)
        valid_sums = get_valid_sums_for_preamble(preamble)


if __name__ == "__main__":
    data = list(get_data_from_input())
    print(find_first_invalid_number(data))
