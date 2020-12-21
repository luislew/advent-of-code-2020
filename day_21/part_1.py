from day_21 import get_allergens_to_ingredient, INGREDIENTS_AND_ALLERGENS


if __name__ == "__main__":
    allergens_to_ingredient = get_allergens_to_ingredient()
    prohibited_ingredients = set(allergens_to_ingredient.values())
    count = 0
    for ingredients, _ in INGREDIENTS_AND_ALLERGENS:
        for ingredient in ingredients:
            if ingredient not in prohibited_ingredients:
                count += 1
    print(count)
