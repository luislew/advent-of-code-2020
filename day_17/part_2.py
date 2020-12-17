import dataclasses
from itertools import product
from typing import Dict

from day_17 import get_active_count_after_cycles


@dataclasses.dataclass(frozen=True)
class Point4D:
    x: int
    y: int
    z: int
    w: int

    @property
    def neighbors(self):
        """Returns the 80 neighboring points"""
        x, y, z, w = self.x, self.y, self.z, self.w
        return [
            Point4D(x + x_diff, y + y_diff, z + z_diff, w + w_diff)
            for x_diff, y_diff, z_diff, w_diff in product((-1, 0, 1), repeat=4)
            if any((x_diff, y_diff, z_diff, w_diff))
        ]


@dataclasses.dataclass
class HypercubeConfiguration:
    states_by_point: Dict[Point4D, str]

    @classmethod
    def from_input(cls, lines):
        cube_configuration = cls({})
        z = w = 0
        for y, line in enumerate(lines):
            for x, state in enumerate(line):
                cube_configuration.states_by_point[Point4D(x, -y, z, w)] = state
        return cube_configuration


if __name__ == "__main__":
    print(get_active_count_after_cycles(HypercubeConfiguration, 6))
