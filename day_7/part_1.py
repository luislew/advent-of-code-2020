from day_7 import RULES_BY_BAG_TYPE


def find_containers_for_bag_type(bag_type, already_checked):
    return {
        container_bag_type
        for container_bag_type, rules in RULES_BY_BAG_TYPE.items()
        if container_bag_type not in already_checked and bag_type in [rule[1] for rule in rules]
    }


def find_all_containers_for_bag_type(bag_type, already_checked=None):
    if already_checked is None:
        already_checked = set()
    else:
        already_checked.add(bag_type)

    container_bag_types = find_containers_for_bag_type(bag_type, already_checked=already_checked)
    for container_bag_type in container_bag_types:
        already_checked.update(find_all_containers_for_bag_type(container_bag_type, already_checked=already_checked))
    return already_checked


if __name__ == "__main__":
    print(len(find_all_containers_for_bag_type("shiny gold")))
