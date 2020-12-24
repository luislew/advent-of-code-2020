from day_23 import CrabCups, get_data_from_input


if __name__ == "__main__":
    initial_cups = get_data_from_input()
    initial_cups += list(range(10, 1000001))
    crab_cups = CrabCups.from_input(initial_cups)

    for _ in range(10000000):
        crab_cups.move()

    # Rotate cups until head is 1
    neighbor = crab_cups.neighbors[1]
    next_neighbor = crab_cups.neighbors[neighbor]
    print(neighbor * next_neighbor)
