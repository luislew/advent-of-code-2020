import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_data_from_input():
    """Yield low number, high number, letter, password tuples from input text file"""
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            # Sample line: "16-18 h: hhhhhhhhhhhhhhhhhh"
            number_spec, letter_spec, password = line.strip().split()
            low, high = [int(s) for s in number_spec.split("-")]
            letter = letter_spec[0]
            yield low, high, letter, password
