from itertools import combinations

from day_1 import get_numbers_from_input


def find_combo_summing_to_2020(numbers):
    """
    Strategy:

    * Do one pass through numbers to find smallest & greatest
    * Create candidates generator which excludes numbers where either:
      * Sum of number and greatest number is less than 2020, or
      * Sum of number and smallest number is greater than 2020
    * Iterate combinations over combinations of candidates and return if sum(combo) is 2020
    """
    # Find min and max
    greatest = least = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
        if number < least:
            least = number

    # Find candidates
    candidates = (i for i in numbers if i + least <= 2020 <= i + greatest)

    # Combination search on candidates
    for combo in combinations(candidates, 2):
        if sum(combo) == 2020:
            print(f"Found combo: {combo}")
            return combo


if __name__ == "__main__":
    numbers = get_numbers_from_input()
    combo = find_combo_summing_to_2020(numbers)
    print(combo[0] * combo[1])
