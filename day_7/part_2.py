from day_7 import RULES_BY_BAG_TYPE


def find_all_contents_for_bag_type(container_bag_type, contents=None):
    if contents is None:
        contents = {}

    rules = RULES_BY_BAG_TYPE[container_bag_type]
    if not rules:
        return contents

    for rule in rules:
        contents[rule] = find_all_contents_for_bag_type(rule[1])
    return contents


def get_all_contents_bag_count(all_contents):
    total = 0
    for rule, subcontents in all_contents.items():
        bag_count = rule[0]
        total += bag_count
        total += bag_count * get_all_contents_bag_count(subcontents)
    return total


if __name__ == "__main__":
    print(get_all_contents_bag_count(find_all_contents_for_bag_type("shiny gold")))
