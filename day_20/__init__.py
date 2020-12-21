import dataclasses
import math
import os
from collections import namedtuple
from itertools import product
from typing import Dict

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


Point = namedtuple("Point", ["x", "y"])


def rotate_vector(vector, angle):
    """Rotate (x, y) angle˚ clockwise around origin"""
    x, y = vector
    angle_in_radians = math.radians(angle)
    sin = int(math.sin(angle_in_radians))
    cos = int(math.cos(angle_in_radians))
    return x * cos - y * sin, x * sin + y * cos


def rotate_squares_grid(squares, angle):
    # Translate grid points to origin
    squares_size = int(math.sqrt(len(squares)))
    offset = (squares_size - 1) / 2
    centered_squares = {(x - offset, y - offset): char for (x, y), char in squares.items()}
    rotated_squares = {rotate_vector(point, angle): char for point, char in centered_squares.items()}
    return {Point(x + offset, y + offset): char for (x, y), char in rotated_squares.items()}


def flip_squares_grid(squares, x_axis=True):
    # Reflect grid points across x-axis or y-axis
    squares_size = int(math.sqrt(len(squares)))
    offset = (squares_size - 1) / 2
    centered_squares = {(x - offset, y - offset): char for (x, y), char in squares.items()}
    if x_axis:
        flipped_squares = {(x, -y): char for (x, y), char in centered_squares.items()}
    else:
        flipped_squares = {(-x, y): char for (x, y), char in centered_squares.items()}
    return {Point(x + offset, y + offset): char for (x, y), char in flipped_squares.items()}


@dataclasses.dataclass
class SquaresGrid:
    squares: Dict[Point, str]


@dataclasses.dataclass
class Tile:
    squares: Dict[Point, str]
    height: int
    width: int
    id: int

    def __hash__(self):
        return self.id

    @classmethod
    def from_input(cls, lines):
        """Generate tile from input lines. Example::

        Tile 3461:
        #.##.#....
        ...#......
        #..##.#...
        #...##.#..
        ..#.####.#
        .....#....
        ##..#....#
        #....#....
        ##.###.#..
        ..#.#.#.#.
        """
        title = lines[0]
        squares = []
        tile_id = int(title.split()[1][:-1])
        for y_idx, line in enumerate(lines[1:]):
            for x_idx, square in enumerate(line):
                squares.append((Point(x_idx, y_idx), square))
        return cls(dict(squares), y_idx + 1, x_idx + 1, tile_id)

    @property
    def top_border(self):
        return "".join(self.squares[Point(x, 0)] for x in range(self.width))

    @property
    def bottom_border(self):
        return "".join(self.squares[Point(x, self.height - 1)] for x in range(self.width))

    @property
    def left_border(self):
        return "".join(self.squares[Point(0, y)] for y in range(self.height))

    @property
    def right_border(self):
        return "".join(self.squares[Point(self.width - 1, y)] for y in range(self.height))

    @property
    def possible_borders(self):
        """Assumes tiles are 10 x 10"""
        borders = {self.top_border, self.right_border, self.bottom_border, self.left_border}
        reversed_borders = {border[-1::-1] for border in borders}
        return borders | reversed_borders

    def matching_borders(self, tile):
        return self.possible_borders & tile.possible_borders

    def find_matching_tiles(self, tiles):
        matches = {}
        for tile in tiles:
            if tile.id == self.id:
                continue

            matching_borders = self.matching_borders(tile)
            if matching_borders:
                matches[tile.id] = matching_borders
        return matches

    def transform_squares(self, rotation_angle, x_axis_reflection=None):
        if not rotation_angle and not x_axis_reflection:
            return

        squares = self.squares
        if rotation_angle:
            squares = rotate_squares_grid(squares, rotation_angle)
        if x_axis_reflection is not None:
            squares = flip_squares_grid(squares, x_axis_reflection)
        self.squares = squares

    def print(self):
        for y in range(10):
            print("".join(char for char in [self.squares[(x, y)] for x in range(10)]))


@dataclasses.dataclass
class TileGrid:
    tiles: Dict[Point, Tile] = dataclasses.field(default_factory=dict)
    squares: Dict[Point, str] = dataclasses.field(default_factory=dict)

    @property
    def tile_ids(self):
        return {tile.id for tile in self.tiles.values()}

    def get_tile(self, x, y):
        return self.tiles[Point(x, y)]

    def set_tile(self, tile, x, y):
        self.tiles[Point(x, y)] = tile

    def populate_squares(self):
        # Fill in squares from tiles, excluding tile borders
        # Assumes a 12 x 12 grid of 10 x 10 tiles
        for y in range(12):
            for x in range(12):
                tile = self.get_tile(x, y)
                for point, char in tile.squares.items():
                    if point.x in (0, 9) or point.y in (0, 9):
                        continue
                    # Translate tile point to tile grid point
                    tile_grid_x, tile_grid_y = (point.x - 1) + 8 * x, (point.y - 1) + 8 * y
                    self.squares[Point(tile_grid_x, tile_grid_y)] = char

    def print(self, with_borders=True):
        if not with_borders:
            # Print the inner squares only
            for y in range(96):
                print("".join(char for char in [self.squares[(x, y)] for x in range(96)]))
        else:
            # Print the whole tiles with spacing
            for y in range(120):
                tile_y, square_y = y // 10, y % 10
                if 0 < y < 119 and not square_y:
                    print(((10 * "=" + "+") * 12)[:-1])

                row = []
                for x in range(120):
                    tile_x, square_x = x // 10, x % 10
                    if 0 < x < 119 and not square_x:
                        row.append("‖")
                    row.append(self.get_tile(tile_x, tile_y).squares[(square_x, square_y)])
                print("".join(row))


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def get_tiles():
    lines = []
    for line in get_data_from_input():
        if not line:
            continue
        elif len(lines) == 11:
            yield Tile.from_input(lines)
            lines = []
        else:
            lines.append(line)


def solve_puzzle():
    tiles = list(get_tiles())
    tiles_by_id = {tile.id: tile for tile in tiles}
    matches_by_tile_id = {}
    corner_tile_matches = {}
    edge_tile_matches = {}
    for tile in tiles:
        matches = tile.find_matching_tiles(tiles)
        matches_by_tile_id[tile.id] = matches
        if len(matches) == 2:
            corner_tile_matches[tile.id] = matches
        elif len(matches) == 3:
            edge_tile_matches[tile.id] = matches

    tile_grid = TileGrid()

    # Solve the top row
    corner_tile_id, matches = next(iter(corner_tile_matches.items()))
    tile_grid.set_tile(tiles_by_id[corner_tile_id], 0, 0)
    corner_tile_matches.pop(corner_tile_id)
    matches_by_tile_id.pop(corner_tile_id)

    neighbor_tile_id = [tile_id for tile_id, matches in edge_tile_matches.items() if corner_tile_id in matches][0]
    tile_grid.set_tile(tiles_by_id[neighbor_tile_id], 1, 0)
    edge_tile_matches.pop(neighbor_tile_id)
    matches_by_tile_id.pop(neighbor_tile_id)
    for x_idx in range(2, 11):
        neighbor_tile_id = [
            tile_id for tile_id, matches in edge_tile_matches.items()
            if neighbor_tile_id in matches and tile_id not in tile_grid.tile_ids
        ][0]
        tile_grid.set_tile(tiles_by_id[neighbor_tile_id], x_idx, 0)
        edge_tile_matches.pop(neighbor_tile_id)
        matches_by_tile_id.pop(neighbor_tile_id)

    corner_tile_id = [tile_id for tile_id, matches in corner_tile_matches.items() if neighbor_tile_id in matches][0]
    tile_grid.set_tile(tiles_by_id[corner_tile_id], 11, 0)
    corner_tile_matches.pop(corner_tile_id)
    matches_by_tile_id.pop(corner_tile_id)

    # Solve the rest of the puzzle
    for y_idx in range(1, 12):
        for x_idx in range(12):
            above_tile = tile_grid.get_tile(x_idx, y_idx - 1)
            neighbor_tile_id = [
                tile_id for tile_id, matches in matches_by_tile_id.items()
                if above_tile.id in matches and tile_id not in tile_grid.tile_ids
            ][0]
            tile_grid.set_tile(tiles_by_id[neighbor_tile_id], x_idx, y_idx)
            matches_by_tile_id.pop(neighbor_tile_id)

    # Try all orientations of individual tiles until borders match, starting in top left corner
    last_tile = tile_grid.get_tile(0, 0)
    right_neighbor_tile = tile_grid.get_tile(1, 0)
    for last_angle, last_reflection, neighbor_angle, neighbor_reflection in product(
        (0, 90, 180, 270), (None, True, False), (0, 90, 180, 270), (None, True, False),
    ):
        last_tile.transform_squares(last_angle, last_reflection)
        right_neighbor_tile.transform_squares(neighbor_angle, neighbor_reflection)
        if last_tile.right_border == right_neighbor_tile.left_border:
            break

    last_tile = right_neighbor_tile
    for x_idx in range(2, 12):
        right_neighbor_tile = tile_grid.get_tile(x_idx, 0)
        for angle, reflection in product((0, 90, 180, 270), (None, True, False)):
            right_neighbor_tile.transform_squares(angle, reflection)
            if last_tile.right_border == right_neighbor_tile.left_border:
                break
        last_tile = right_neighbor_tile

    # Line up the rest of the tiles by matching against top neighbors
    for y_idx in range(1, 12):
        for x_idx in range(12):
            tile = tile_grid.get_tile(x_idx, y_idx)
            upper_neighbor_tile = tile_grid.get_tile(x_idx, y_idx - 1)
            for angle, reflection in product((0, 90, 180, 270), (None, True, False)):
                tile.transform_squares(angle, reflection)
                if tile.top_border == upper_neighbor_tile.bottom_border:
                    break

    return tile_grid
