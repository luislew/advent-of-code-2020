from functools import reduce
from itertools import product

from day_20 import solve_puzzle


if __name__ == "__main__":
    tile_grid = solve_puzzle()
    corner_tiles = [tile_grid.get_tile(x, y) for x, y in product((0, 11), repeat=2)]
    print(reduce(lambda x, y: x * y, [tile.id for tile in corner_tiles]))
