from day_8 import calculate_value_at_infinite_loop_or_end, get_instructions_from_input


if __name__ == "__main__":
    instructions = list(get_instructions_from_input())
    value, _, infinite_loop = calculate_value_at_infinite_loop_or_end(instructions)
    assert infinite_loop is not False, "No infinite loop detected!"
    print(value)
