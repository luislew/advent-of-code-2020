import math
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

DIRECTION_VECTORS = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0),
}


def get_steps_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            stripped = line.strip()
            yield stripped[0], int(stripped[1:])


def rotate_vector(vector, angle, direction):
    """Rotate (x, y) angle˚ around origin
    direction: L=counterclockwise, R=clockwise
    """
    x, y = vector
    if direction == "R":
        angle = 360 - angle
    angle_in_radians = math.radians(angle)
    sin = int(math.sin(angle_in_radians))
    cos = int(math.cos(angle_in_radians))
    return x * cos - y * sin, x * sin + y * cos


def translate_vector(vector, direction_vector, increment):
    x, y = vector
    x_delta, y_delta = direction_vector
    return x + x_delta * increment, y + y_delta * increment
