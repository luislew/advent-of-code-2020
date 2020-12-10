from collections import Counter

from day_10 import JOLTAGE_DIFFS


if __name__ == "__main__":
    joltage_diff_counts = Counter(JOLTAGE_DIFFS)
    print(joltage_diff_counts[1] * joltage_diff_counts[3])
