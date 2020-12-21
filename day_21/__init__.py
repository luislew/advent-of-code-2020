import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def get_ingredients_and_allergens():
    for line in get_data_from_input():
        ingredients_list, allergens_list = line[:-1].split(" (contains ")
        ingredients = ingredients_list.split()
        allergens = allergens_list.split(", ")
        yield ingredients, allergens


INGREDIENTS_AND_ALLERGENS = list(get_ingredients_and_allergens())


def get_allergens_to_ingredient():
    allergens_to_possible_ingredient = {}
    for ingredients, allergens in INGREDIENTS_AND_ALLERGENS:
        for allergen in allergens:
            if allergen not in allergens_to_possible_ingredient:
                allergens_to_possible_ingredient[allergen] = set(ingredients)
            else:
                allergens_to_possible_ingredient[allergen] &= set(ingredients)

    allergens_to_ingredient = {}
    while len(allergens_to_ingredient) < len(allergens_to_possible_ingredient):
        for allergen, possible_ingredients in allergens_to_possible_ingredient.items():
            if len(possible_ingredients) == 1:
                ingredient = possible_ingredients.pop()
                allergens_to_ingredient[allergen] = ingredient
                for possibles in allergens_to_possible_ingredient.values():
                    possibles -= {ingredient}

    return allergens_to_ingredient
