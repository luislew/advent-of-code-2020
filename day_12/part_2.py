from day_12 import DIRECTION_VECTORS, get_steps_from_input, rotate_vector, translate_vector


def get_position_for_steps(steps):
    position = (0, 0)
    waypoint = (10, 1)
    for instruction, value in steps:
        if instruction == "F":
            position = translate_vector(position, waypoint, value)
        elif instruction in ("L", "R"):
            waypoint = rotate_vector(waypoint, value, instruction)
        else:
            waypoint = translate_vector(waypoint, DIRECTION_VECTORS[instruction], value)
    return position


if __name__ == "__main__":
    steps = get_steps_from_input()
    print(sum(map(abs, get_position_for_steps(steps))))
