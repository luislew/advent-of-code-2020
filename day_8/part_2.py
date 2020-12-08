from day_8 import calculate_value_at_infinite_loop_or_end, get_instructions_from_input


def swap_instruction_at_idx(instructions, idx) -> bool:
    """Swap jmp with nop; returns True if swapped, else False"""
    op, value = instructions[idx]
    if op == "acc":
        return False

    instructions[idx] = ("jmp" if op == "nop" else "nop", value)
    return True


def get_value_for_fixed_instructions(instructions, visited) -> int:
    """Modify visited instructions in place, one at a time, and look for execution without infinite loop"""
    for idx in visited:
        if swap_instruction_at_idx(instructions, idx):
            accumulated_value, _, infinite_loop = calculate_value_at_infinite_loop_or_end(instructions)
            # If swapping instruction breaks the infinite loop, return value; otherwise, swap back and continue
            if infinite_loop is False:
                return accumulated_value
            else:
                swap_instruction_at_idx(instructions, idx)

    raise AssertionError("No fix detected!")


if __name__ == "__main__":
    instructions = list(get_instructions_from_input())
    _, visited, infinite_loop = calculate_value_at_infinite_loop_or_end(instructions)
    assert infinite_loop is not False, "No infinite loop detected!"
    print(get_value_for_fixed_instructions(instructions, visited))
