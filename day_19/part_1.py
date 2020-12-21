from day_19 import MESSAGES, RULES_BY_ID, simplify_rules


def solve_problem():
    rules_by_id = simplify_rules(RULES_BY_ID)
    rule = rules_by_id[0]
    return sum(1 for message in MESSAGES if rule.check_message(message))


if __name__ == "__main__":
    print(solve_problem())
