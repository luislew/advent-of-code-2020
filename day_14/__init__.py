import math
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            instruction, value = line.strip().split(" = ")
            if instruction == "mask":
                yield instruction, value
            else:
                key = int(instruction[4:-1])
                yield key, int(value)


def bits_array_to_int(bits):
    return int("".join(bits), base=2)
