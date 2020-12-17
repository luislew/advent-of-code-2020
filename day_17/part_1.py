import dataclasses
from itertools import product
from typing import Dict

from day_17 import get_active_count_after_cycles


@dataclasses.dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int

    @property
    def neighbors(self):
        """Returns the 26 neighboring points"""
        x, y, z = self.x, self.y, self.z
        return [
            Point(x + x_diff, y + y_diff, z + z_diff)
            for x_diff, y_diff, z_diff in product((-1, 0, 1), repeat=3)
            if any((x_diff, y_diff, z_diff))
        ]


@dataclasses.dataclass
class CubeConfiguration:
    states_by_point: Dict[Point, str]

    @classmethod
    def from_input(cls, lines):
        cube_configuration = cls({})
        for y, line in enumerate(lines):
            for x, state in enumerate(line):
                cube_configuration.states_by_point[Point(x, -y, 0)] = state
        return cube_configuration


if __name__ == "__main__":
    print(get_active_count_after_cycles(CubeConfiguration, 6))
