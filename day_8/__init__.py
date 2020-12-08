import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_instructions_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for instruction in f:
            op, value_str = instruction.strip().split()
            yield op, int(value_str)


def calculate_value_at_infinite_loop_or_end(instructions: list) -> (int, list, bool):
    """Runs instructions, and either breaks on infinite loop detection or end of instructions"""
    current_idx = 0
    accumulated_value = 0
    infinite_loop = True
    visited = set()
    while current_idx not in visited:
        visited.add(current_idx)
        try:
            op, value = instructions[current_idx]
        except IndexError:
            infinite_loop = False
            break

        current_idx += value if op == "jmp" else 1
        if op == "acc":
            accumulated_value += value

    return accumulated_value, visited, infinite_loop
