import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        return [int(i) for i in f.read().strip().split(",")]


def get_nth_number(starting_numbers, n):
    spoken_numbers = {}  # map of numbers by last turn spoken
    current_turn = 1
    number = None
    last_spoken_turn = None
    for number in starting_numbers:
        last_spoken_turn = spoken_numbers.get(number)
        spoken_numbers[number] = current_turn
        current_turn += 1

    while current_turn <= n:
        number = current_turn - last_spoken_turn - 1 if last_spoken_turn is not None else 0
        last_spoken_turn = spoken_numbers.get(number)
        spoken_numbers[number] = current_turn
        current_turn += 1

    return number
