from functools import reduce

from day_3 import get_data_from_input, tree_collisions_from_top_to_bottom_for_slope


if __name__ == "__main__":
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    collision_counts = (
        tree_collisions_from_top_to_bottom_for_slope(get_data_from_input(), right, down)
        for right, down in slopes
    )
    print(reduce(lambda x, y: x * y, collision_counts))
