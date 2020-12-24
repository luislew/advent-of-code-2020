import dataclasses
import os
from typing import List, Dict

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        return [int(i) for i in f.read().strip()]


@dataclasses.dataclass
class CrabCups:
    current_cup: int
    neighbors: Dict[int, int]
    size: int

    @classmethod
    def from_input(cls, cups: List[int]) -> "CrabCups":
        size = len(cups)
        neighbors = {}
        first_cup = last_cup = cups[0]
        for cup in cups[1:]:
            neighbors[last_cup] = cup
            last_cup = cup
        neighbors[last_cup] = first_cup
        return cls(first_cup, neighbors, size)

    def move(self):
        # Get the cups to move by their neighbors
        first_cup = self.neighbors[self.current_cup]
        second_cup = self.neighbors[first_cup]
        third_cup = self.neighbors[second_cup]
        next_cup = self.neighbors[third_cup]
        cups_to_move = [first_cup, second_cup, third_cup]
        # Get the destination cup, excluding any cups to move
        destination_cup = (self.current_cup - 1) % self.size or self.size
        while destination_cup in cups_to_move:
            destination_cup = (destination_cup - 1) % self.size or self.size
        # Move the cups
        self.neighbors[third_cup] = self.neighbors[destination_cup]
        self.neighbors[destination_cup] = first_cup
        self.neighbors[self.current_cup] = next_cup
        self.current_cup = next_cup
