import dataclasses
import os
from functools import reduce
from typing import Set

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


@dataclasses.dataclass(frozen=True)
class Rule:
    field_name: str
    lower_range_low: int
    lower_range_hi: int
    upper_range_low: int
    upper_range_hi: int
    allowed_values: Set[int]

    @classmethod
    def from_rule_definition(cls, rule_def):
        field_name, valid_range_str = rule_def.split(": ")
        lower_range_str, upper_range_str = valid_range_str.split(" or ")
        lower_range_low, lower_range_hi = parse_str_into_ints_array(lower_range_str, "-")
        upper_range_low, upper_range_hi = parse_str_into_ints_array(upper_range_str, "-")
        lower_range_values = set(range(lower_range_low, lower_range_hi + 1))
        upper_range_values = set(range(upper_range_low, upper_range_hi + 1))
        allowed_values = lower_range_values | upper_range_values
        return cls(field_name, lower_range_low, lower_range_hi, upper_range_low, upper_range_hi, allowed_values)

    def is_valid_value(self, value):
        return value in self.allowed_values


def get_data_from_input():
    your_ticket = None
    nearby_tickets = []
    rules = []
    current_section = None
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            line = line.strip()
            if "ticket" in line:
                current_section = line[:-1]
                continue
            elif not line:
                continue

            if current_section is None:  # Initial rules
                rules.append(Rule.from_rule_definition(line))
            elif current_section == "your ticket":
                your_ticket = parse_str_into_ints_array(line)
            elif current_section == "nearby tickets":
                nearby_tickets.append(parse_str_into_ints_array(line))

    return rules, your_ticket, nearby_tickets


def parse_str_into_ints_array(string, separator=","):
    return [int(i) for i in string.split(separator)]


def get_rule_validators(rules):
    rules_validators_by_field = {}
    for rule in rules:
        rules_validators_by_field[rule.field_name] = rule.is_valid_value
    return rules_validators_by_field


RULES, YOUR_TICKET, NEARBY_TICKETS = get_data_from_input()
RULE_VALIDATORS = get_rule_validators(RULES)
ALL_ALLOWED_VALUES = reduce(lambda s, t: s | t, (rule.allowed_values for rule in RULES))
FIELD_NAMES = set(RULE_VALIDATORS)
NUM_FIELDS = len(FIELD_NAMES)
