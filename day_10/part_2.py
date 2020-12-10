from itertools import combinations
from math import prod

from day_10 import JOLTAGE_DIFFS, SORTED_JOLTAGES_WITH_ENDS, check_chain_validity


def get_subchains():
    # Break the chain of adapters into subchains at 3 joltage diff boundaries
    current_chain = [SORTED_JOLTAGES_WITH_ENDS[0]]
    for joltage, joltage_diff in zip(SORTED_JOLTAGES_WITH_ENDS[1:], JOLTAGE_DIFFS):
        if joltage_diff == 3:
            # Break off a new chain
            yield current_chain
            current_chain = []
        current_chain.append(joltage)
    yield current_chain


def get_valid_combinations_for_subchain(subchain):
    """Construct all possible subsubchains and count the valid ones"""
    count = 1  # We start with a valid subchain
    if len(subchain) < 3:
        return count

    start, center, end = subchain[0], subchain[1:-1], subchain[-1]
    for i in range(len(center)):
        for possible_center in combinations(center, i):
            if check_chain_validity([start, *possible_center, end]):
                count += 1

    return count


if __name__ == "__main__":
    print(prod(get_valid_combinations_for_subchain(subchain) for subchain in get_subchains()))
