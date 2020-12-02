from itertools import combinations

from day_1 import get_numbers_from_input


def find_combo_summing_to_2020(numbers):
    """
    Strategy:

    * Do one pass through numbers to find 2 smallest & 2 greatest
    * Create candidates generator which excludes numbers that either:
      * Add up to less than 2020 when combined with 2 greatest numbers, or
      * Add up to greater than 2020 when combined with 2 smallest numbers
    * Iterate combinations over combinations of candidates and return if sum(combo) is 2020
    """
    # Find mins and maxes
    greatest = second_greatest = least = second_least = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
        elif number > second_greatest:
            second_greatest = number
        elif number < least:
            least = number
        elif number < second_least:
            second_least = number

    # Find candidates
    candidates = (i for i in numbers if i + least + second_least <= 2020 <= i + greatest + second_greatest)

    # Combination search on candidates
    for combo in combinations(candidates, 3):
        if sum(combo) == 2020:
            print(f"Found combo: {combo}")
            return combo


if __name__ == "__main__":
    numbers = get_numbers_from_input()
    combo = find_combo_summing_to_2020(numbers)
    print(combo[0] * combo[1] * combo[2])
