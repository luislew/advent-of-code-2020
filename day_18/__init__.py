import dataclasses
import os
from typing import List

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Op:
    ADD = "+"
    MULT = "*"
    START = "("
    END = ")"


@dataclasses.dataclass
class Expression:
    items: List[str]

    @classmethod
    def from_line(cls, line):
        parts = line.split()
        items = []
        for part in parts:
            items.extend(part)
        return cls(items)

    def evaluate(self):
        op = None
        value = None
        open_count = 0
        subitems = []
        for idx, item in enumerate(self.items):
            if open_count:
                if item == Op.START:
                    open_count += 1
                    subitems.append(item)
                elif item == Op.END:
                    open_count -= 1
                    if not open_count:
                        subvalue = Expression(subitems).evaluate()
                        if value is None:
                            value = subvalue
                        elif op == Op.ADD:
                            value += subvalue
                        elif op == Op.MULT:
                            value *= subvalue
                        subitems = []
                    else:
                        subitems.append(item)
                else:
                    subitems.append(item)
            else:
                if item == Op.START:
                    open_count += 1
                elif item in (Op.ADD, Op.MULT):
                    op = item
                elif value is None:
                    value = int(item)
                elif op == Op.ADD:
                    value += int(item)
                elif op == Op.MULT:
                    value *= int(item)
        return value


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()
