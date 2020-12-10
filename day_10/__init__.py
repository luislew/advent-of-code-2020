import os
from collections import Counter

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield int(line.strip())


def get_joltage_diffs_for_joltages(joltages):
    # NOTE: This expects joltages to already be sorted
    last_joltage = joltages[0]
    for joltage in joltages[1:]:
        joltage_diff = joltage - last_joltage
        yield joltage_diff
        last_joltage = joltage


def find_joltage_diff_counts_for_joltages(joltages):
    return Counter(get_joltage_diffs_for_joltages(joltages))


def check_chain_validity(joltages):
    return not any(joltage_diff > 3 for joltage_diff in get_joltage_diffs_for_joltages(joltages))


SORTED_JOLTAGES = sorted(get_data_from_input())
SORTED_JOLTAGES_WITH_ENDS = [0, *SORTED_JOLTAGES, SORTED_JOLTAGES[-1] + 3]
