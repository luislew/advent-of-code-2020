from day_19 import MESSAGES, parse_rule, RULES_BY_ID, simplify_rules


def check_message(message, rule_42_substrings, rule_31_substrings):
    # Complex rules:
    # 0: 8 11
    # 8: 42 | 42 8 --> (42){1,}
    # 11: 42 31 | 42 11 31 --> (42)+(31)+ where 42 and 31 are repeated an equal # of times
    # --> 0: (42){2,}(31)+
    substring_length = len(rule_42_substrings[0])
    rule_42_matches = 0
    while message:
        if message.startswith(rule_42_substrings):
            message = message[substring_length:]
            rule_42_matches += 1
        else:
            break
    if rule_42_matches < 2:
        return False

    rule_31_matches = 0
    while message:
        if message.startswith(rule_31_substrings):
            message = message[substring_length:]
            rule_31_matches += 1
        else:
            return False

    return not message and 0 < rule_31_matches < rule_42_matches


def solve_problem():
    rules_by_id = RULES_BY_ID
    rules_by_id[8] = parse_rule("8: 42 | 42 8")
    rules_by_id[11] = parse_rule("11: 42 31 | 42 11 31")
    rules_by_id = simplify_rules(RULES_BY_ID)
    rule_42_substrings = tuple(rules_by_id[42].substrings)
    rule_31_substrings = tuple(rules_by_id[31].substrings)
    return sum(1 for message in MESSAGES if check_message(message, rule_42_substrings, rule_31_substrings))


if __name__ == "__main__":
    print(solve_problem())
