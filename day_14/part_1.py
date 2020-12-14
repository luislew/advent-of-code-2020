from day_14 import bits_array_to_int, get_data_from_input


def apply_bitmask_to_value(value, bitmask):
    zero_padded_binary_value = f"{value:036b}"
    masked_bits = [
        orig if mask == "X" else mask
        for orig, mask in zip(zero_padded_binary_value, bitmask)
    ]
    return bits_array_to_int(masked_bits)


def read_instructions_into_memory(data):
    bitmask = None
    memory = {}
    for instruction, value in data:
        if instruction == "mask":
            bitmask = value
        else:
            memory[instruction] = apply_bitmask_to_value(value, bitmask)
    return memory


if __name__ == "__main__":
    memory = read_instructions_into_memory(get_data_from_input())
    print(sum(memory.values()))
