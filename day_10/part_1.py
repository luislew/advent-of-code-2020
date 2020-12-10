from day_10 import SORTED_JOLTAGES_WITH_ENDS, find_joltage_diff_counts_for_joltages


if __name__ == "__main__":
    joltage_diff_counts = find_joltage_diff_counts_for_joltages(SORTED_JOLTAGES_WITH_ENDS)
    print(joltage_diff_counts[1] * joltage_diff_counts[3])
