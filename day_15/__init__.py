import os
from collections import defaultdict, deque
from functools import partial

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        return [int(i) for i in f.read().strip().split(",")]


def get_nth_number(starting_numbers, n):
    spoken_numbers = defaultdict(partial(deque, maxlen=2))  # map of numbers by last turn spoken
    current_turn = 1
    last_spoken = None
    last_spoken_new = False
    for number in starting_numbers:
        last_spoken_new = number not in spoken_numbers
        spoken_numbers[number].append(current_turn)
        current_turn += 1
        last_spoken = number

    while current_turn <= n:
        if last_spoken_new:
            number = 0
        else:
            earlier, later = spoken_numbers[last_spoken]
            number = later - earlier

        last_spoken_new = number not in spoken_numbers
        spoken_numbers[number].append(current_turn)
        current_turn += 1
        last_spoken = number

    return last_spoken
