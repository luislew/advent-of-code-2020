from day_9 import get_data_from_input


def find_contiguous_sequence_adding_to_total(data, total):
    for start_idx, candidate in enumerate(data):
        running_total = candidate
        for end_idx, number in enumerate(data[start_idx + 1:]):
            running_total += number
            if running_total == total:
                return start_idx, start_idx + end_idx + 2
            elif running_total > total:
                break


if __name__ == "__main__":
    desired_total = 104054607  # from part 1
    data = list(get_data_from_input())
    sequence_start, sequence_end = find_contiguous_sequence_adding_to_total(data, desired_total)
    sequence = data[sequence_start:sequence_end]
    assert sum(sequence) == desired_total
    print(min(sequence) + max(sequence))
