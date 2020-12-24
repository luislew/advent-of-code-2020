from day_24 import get_data_from_input, TileFloor


if __name__ == "__main__":
    tile_floor = TileFloor()
    tile_floor.flip_tiles_for_lines(get_data_from_input())
    print(tile_floor.black_tiles_count)
