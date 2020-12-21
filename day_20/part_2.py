import math
from itertools import product

from day_20 import flip_squares_grid, Point, rotate_squares_grid, solve_puzzle

"""
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
SEA_MONSTER_POINTS = [
    Point(18, 0),
    Point(0, 1),
    Point(5, 1),
    Point(6, 1),
    Point(11, 1),
    Point(12, 1),
    Point(17, 1),
    Point(18, 1),
    Point(19, 1),
    Point(1, 2),
    Point(4, 2),
    Point(7, 2),
    Point(10, 2),
    Point(13, 2),
    Point(16, 2),
]


def get_subgrid_sea_monsters_hits(squares, subgrid_upper_left):
    x_offset, y_offset = subgrid_upper_left
    offset_points = [(point.x + x_offset, point.y + y_offset) for point in SEA_MONSTER_POINTS]
    if all(squares[point] == "#" for point in offset_points):
        return offset_points


def find_sea_monsters(squares):
    # Sea monster requires 20 x 3 subgrid
    # We can check horizontal subgrids (0, 0) to (19, 2) --> (76, 93) to (95, 95),
    grid_size = int(math.sqrt(len(squares)))
    sea_monster_hits = set()
    for x, y in product(range(grid_size - 19), range(grid_size - 2)):
        subgrid_hits = get_subgrid_sea_monsters_hits(squares, (x, y))
        if subgrid_hits:
            sea_monster_hits.update(subgrid_hits)
    return sea_monster_hits


def find_grid_orientation_with_sea_monsters(squares):
    rotations = [rotate_squares_grid(squares, angle) for angle in (0, 90, 180, 270)]
    reflections = (None, True, False)
    for rotation, reflection in product(rotations, reflections):
        orientation = flip_squares_grid(rotation, reflection) if reflection else rotation
        sea_monster_hits = find_sea_monsters(orientation)
        if sea_monster_hits:
            return sea_monster_hits


if __name__ == "__main__":
    tile_grid = solve_puzzle()
    tile_grid.populate_squares()
    squares = {(point.x, point.y): char for point, char in tile_grid.squares.items()}
    sea_monster_hits = find_grid_orientation_with_sea_monsters(squares)
    print(list(tile_grid.squares.values()).count("#") - len(sea_monster_hits))
