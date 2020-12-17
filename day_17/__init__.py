import abc
import dataclasses
import os
from itertools import product
from typing import Dict, Union

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class States:
    ACTIVE = "#"
    INACTIVE = "."


@dataclasses.dataclass(frozen=True)
class Point3D:
    x: int = 0
    y: int = 0
    z: int = 0

    @property
    def neighbors(self):
        """Returns the 26 neighboring points"""
        x, y, z = self.x, self.y, self.z
        return [
            Point3D(x + x_diff, y + y_diff, z + z_diff)
            for x_diff, y_diff, z_diff in product((-1, 0, 1), repeat=3)
            if any((x_diff, y_diff, z_diff))
        ]


@dataclasses.dataclass(frozen=True)
class Point4D(Point3D):
    w: int = 0

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
class AbstractCubeConfiguration(abc.ABC):
    states_by_point: Dict[Union[Point3D, Point4D], str]

    @property
    @abc.abstractmethod
    def point_cls(self) -> Union[Point3D, Point4D]:
        pass

    @classmethod
    def from_input(cls, lines):
        cube_configuration = cls({})
        for y, line in enumerate(lines):
            for x, state in enumerate(line):
                point = cls.point_cls(x, y)
                cube_configuration.states_by_point[point] = state
        return cube_configuration

    def execute_cycle(self):
        points_to_flip = []
        all_candidate_points = set()
        for point in self.states_by_point:
            all_candidate_points.update(point.neighbors)

        for point in all_candidate_points:
            state = self.states_by_point.setdefault(point, States.INACTIVE)
            neighbor_states = [
                self.states_by_point.get(neighbor, States.INACTIVE)
                for neighbor in point.neighbors
            ]
            if state == States.ACTIVE and neighbor_states.count(States.ACTIVE) not in (2, 3):
                points_to_flip.append(point)
            elif state == States.INACTIVE and neighbor_states.count(States.ACTIVE) == 3:
                points_to_flip.append(point)

        for point in points_to_flip:
            current_state = self.states_by_point[point]
            self.states_by_point[point] = States.INACTIVE if current_state == States.ACTIVE else States.ACTIVE
        return self


@dataclasses.dataclass
class CubeConfiguration(AbstractCubeConfiguration):
    point_cls = Point3D


@dataclasses.dataclass
class HypercubeConfiguration(AbstractCubeConfiguration):
    point_cls = Point4D


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def get_active_count_after_cycles(cube_cls, number_of_cycles):
    cube_configuration = cube_cls.from_input(get_data_from_input())
    for _ in range(number_of_cycles):
        cube_configuration.execute_cycle()
    return sum(1 for state in cube_configuration.states_by_point.values() if state == States.ACTIVE)
