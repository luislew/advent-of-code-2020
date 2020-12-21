from day_21 import get_allergens_to_ingredient


if __name__ == "__main__":
    allergens_to_ingredient = get_allergens_to_ingredient()
    print(",".join(ingredient for _, ingredient in sorted(allergens_to_ingredient.items())))
