from day_3 import get_data_from_input, tree_collisions_from_top_to_bottom_for_slope


if __name__ == "__main__":
    data = get_data_from_input()
    print(tree_collisions_from_top_to_bottom_for_slope(data, right=3, down=1))
