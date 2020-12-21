from itertools import chain
from operator import itemgetter

from day_21 import get_allergens_to_ingredient, INGREDIENTS_AND_ALLERGENS


if __name__ == "__main__":
    allergens_to_ingredient = get_allergens_to_ingredient()
    prohibited_ingredients = set(allergens_to_ingredient.values())
    all_ingredients = chain.from_iterable(map(itemgetter(0), INGREDIENTS_AND_ALLERGENS))
    print(len([ingredient for ingredient in all_ingredients if ingredient not in prohibited_ingredients]))
