from day_21 import get_allergens_to_ingredient


if __name__ == "__main__":
    print(",".join(ingredient for _, ingredient in sorted(get_allergens_to_ingredient().items())))
