import itertools

from day_14 import bits_array_to_int, get_data_from_input


def apply_bitmask_to_address(address, bitmask):
    """Returns all valid addresses after applying bitmask to address"""
    zero_padded_binary_address = f"{address:036b}"
    masked_bits = [
        orig if mask == "0" else mask
        for orig, mask in zip(zero_padded_binary_address, bitmask)
    ]
    floating_bits_indices = [idx for idx, bit in enumerate(masked_bits) if bit == "X"]
    if not floating_bits_indices:
        return [bits_array_to_int(masked_bits)]

    masked_addresses = []
    # Run through all combinations for floating bits
    for combo in itertools.product((0, 1), repeat=len(floating_bits_indices)):
        # We can modify the floating bits in place
        for idx, val in zip(floating_bits_indices, combo):
            masked_bits[idx] = str(val)
        masked_addresses.append(bits_array_to_int(masked_bits))
    return masked_addresses


def read_instructions_into_memory(data):
    bitmask = None
    memory = {}
    for instruction, value in data:
        if instruction == "mask":
            bitmask = value
        else:
            for address in apply_bitmask_to_address(instruction, bitmask):
                memory[address] = value
    return memory


if __name__ == "__main__":
    memory = read_instructions_into_memory(get_data_from_input())
    print(sum(memory.values()))
