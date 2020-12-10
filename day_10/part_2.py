from itertools import combinations
from math import prod

from day_10 import SORTED_JOLTAGES_WITH_ENDS, check_chain_validity, get_joltage_diffs_for_joltages


def get_subchains_for_chain(joltages):
    # Break the chain of adapters into subchains at 3 joltage diff boundaries
    # NOTE: Just like `get_joltage_diffs_for_data` this expected **sorted** data
    joltage_diffs = get_joltage_diffs_for_joltages(joltages)
    current_chain = [joltages[0]]
    for joltage, joltage_diff in zip(joltages[1:], joltage_diffs):
        if joltage_diff == 3:
            # Break off a new chain
            yield current_chain
            current_chain = []
        current_chain.append(joltage)
    yield current_chain


def get_valid_combinations_for_subchain(subchain):
    # Construct all possible subsubchains and count the valid ones
    if len(subchain) < 3:
        return 1

    count = 0
    start, center, end = subchain[0], subchain[1:-1], subchain[-1]
    for i in range(len(center) + 1):
        for possible_center in combinations(center, i):
            if check_chain_validity([start, *possible_center, end]):
                count += 1

    return count


if __name__ == "__main__":
    subchains = get_subchains_for_chain(SORTED_JOLTAGES_WITH_ENDS)
    print(prod(get_valid_combinations_for_subchain(subchain) for subchain in subchains))
