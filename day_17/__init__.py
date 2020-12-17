import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class States:
    ACTIVE = "#"
    INACTIVE = "."


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def execute_cycle(cube_configuration):
    points_to_flip = []
    all_candidate_points = set()
    for point in cube_configuration.states_by_point:
        all_candidate_points.update(point.neighbors)

    for point in all_candidate_points:
        state = cube_configuration.states_by_point.setdefault(point, States.INACTIVE)
        neighbor_states = [
            cube_configuration.states_by_point.get(neighbor, States.INACTIVE)
            for neighbor in point.neighbors
        ]
        if state == States.ACTIVE and neighbor_states.count(States.ACTIVE) not in (2, 3):
            points_to_flip.append(point)
        elif state == States.INACTIVE and neighbor_states.count(States.ACTIVE) == 3:
            points_to_flip.append(point)

    for point in points_to_flip:
        current_state = cube_configuration.states_by_point[point]
        cube_configuration.states_by_point[point] = States.INACTIVE if current_state == States.ACTIVE else States.ACTIVE
    return cube_configuration


def get_active_count_after_cycles(cube_cls, number_of_cycles):
    cube_configuration = cube_cls.from_input(get_data_from_input())
    for _ in range(number_of_cycles):
        execute_cycle(cube_configuration)
    return sum(1 for state in cube_configuration.states_by_point.values() if state == States.ACTIVE)
