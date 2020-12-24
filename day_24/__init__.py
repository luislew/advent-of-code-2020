import dataclasses
import os
from typing import Iterable, Dict, Tuple, List

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

DIRECTION_VECTORS = {
    "ne": (0.5, 0.5),
    "e": (1.0, 0.0),
    "se": (0.5, -0.5),
    "sw": (-0.5, -0.5),
    "w": (-1.0, 0.0),
    "nw": (-0.5, 0.5),
}


def get_data_from_input() -> Iterable[str]:
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def parse_line(line) -> Iterable[str]:
    step = ""
    for char in line:
        step += char
        if char not in ("n", "s"):
            yield step
            step = ""


@dataclasses.dataclass
class TileFloor:
    # (x, y): `False` if unflipped (white), `True` if flipped (black)
    states: Dict[Tuple[float, float], bool] = dataclasses.field(default_factory=dict)

    @staticmethod
    def get_neighbors(x: float, y: float) -> List[Tuple[float, float]]:
        return [(x + x_diff, y + y_diff) for x_diff, y_diff in DIRECTION_VECTORS.values()]

    @property
    def black_tiles_count(self) -> int:
        return sum(self.states.values())

    def get_state(self, x: float, y: float) -> bool:
        return self.states.get((x, y), False)

    def get_neighbor_states(self, x: float, y: float) -> List[bool]:
        return [self.get_state(neighbor_x, neighbor_y) for neighbor_x, neighbor_y in self.get_neighbors(x, y)]

    def add_neighbors(self, x: float, y: float) -> None:
        for neighbor_x, neighbor_y in self.get_neighbors(x, y):
            self.states.setdefault((neighbor_x, neighbor_y), False)

    def set_state(self, x: float, y: float, state: bool) -> None:
        self.states[(x, y)] = state
        self.add_neighbors(x, y)

    def flip_tile_for_steps(self, steps: Iterable[str]) -> None:
        x, y = 0, 0
        for step in steps:
            x_diff, y_diff = DIRECTION_VECTORS[step]
            x += x_diff
            y += y_diff
        self.set_state(x, y, not self.get_state(x, y))

    def flip_tiles_for_lines(self, lines: Iterable[str]) -> None:
        for line in lines:
            self.flip_tile_for_steps(parse_line(line))

    def flip_tiles_for_day(self):
        # Find tiles to flip
        white_tiles_to_flip = []
        black_tiles_to_flip = []
        for (x, y), state in self.states.items():
            neighbor_states = self.get_neighbor_states(x, y)
            adjacent_black_tiles = sum(neighbor_states)
            if state and adjacent_black_tiles in (0, 3, 4, 5, 6):
                black_tiles_to_flip.append((x, y))
            elif not state and adjacent_black_tiles == 2:
                white_tiles_to_flip.append((x, y))

        for x, y in white_tiles_to_flip:
            self.set_state(x, y, True)
        for x, y in black_tiles_to_flip:
            self.set_state(x, y, False)

    def flip_tiles_for_days(self, days: int):
        for _ in range(days):
            self.flip_tiles_for_day()
