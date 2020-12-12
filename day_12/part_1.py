from day_12 import DIRECTION_VECTORS, get_steps_from_input, rotate_vector, translate_vector


def get_position_for_steps(steps):
    position = (0, 0)
    direction = DIRECTION_VECTORS["E"]  # Facing east to start
    for instruction, value in steps:
        if instruction in ("L", "R"):
            direction = rotate_vector(direction, value, instruction)
        else:
            position = translate_vector(position, DIRECTION_VECTORS.get(instruction, direction), value)
    return position


if __name__ == "__main__":
    steps = get_steps_from_input()
    print(sum(map(abs, get_position_for_steps(steps))))
