import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def parse_rule(line):
    """Parse line into bag type, bag contents rules tuples, e.g.:
    ('vibrant white', [(1, 'plaid silver'), (5, 'bright cyan'), (2, 'light crimson'), (4, 'clear black')])
    """
    # Examples rules:
    # "plaid beige bags contain 3 drab magenta bags."
    # "dim silver bags contain 2 shiny chartreuse bags, 4 dull magenta bags."
    # "mirrored gold bags contain no other bags."
    # "vibrant white bags contain 1 plaid silver bag, 5 bright cyan bags, 2 light crimson bags, 4 clear black bags."
    # "plaid chartreuse bags contain 1 posh lavender bag, 3 dull orange bags."
    bag_type_spec, bag_contents = line[:-1].split(" contain ")
    bag_type = " ".join(bag_type_spec.split()[:-1])
    bag_contents_rules = []
    if bag_contents != "no other bags":
        bag_contents_specs = bag_contents.split(", ")
        # Example bag contents specs:
        # "1 plaid silver bag"
        # "4 clear black bags"
        for spec in bag_contents_specs:
            number, pattern, color, _ = spec.split()
            bag_contents_rules.append((int(number), f"{pattern} {color}"))
    return bag_type, bag_contents_rules


RULES_BY_BAG_TYPE = dict(parse_rule(line) for line in get_data_from_input())
