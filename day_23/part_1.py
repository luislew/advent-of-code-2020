from day_23 import CrabCups, get_data_from_input


if __name__ == "__main__":
    crab_cups = CrabCups.from_input(get_data_from_input())
    for _ in range(100):
        crab_cups.move()

    last_cup = 1
    result = ""
    for _ in range(crab_cups.size - 1):
        neighbor = crab_cups.neighbors[last_cup]
        result += str(neighbor)
        last_cup = neighbor
    print(result)
