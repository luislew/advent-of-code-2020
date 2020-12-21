import dataclasses
import os
from functools import reduce
from itertools import product, chain
from typing import List, Optional, Set

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


@dataclasses.dataclass
class SimpleRule:
    substrings: List[str]
    id: Optional[int] = None

    def check_message(self, message: str) -> bool:
        return message in self.substrings

    def __add__(self, other: "SimpleRule"):
        combinations = product(self.substrings, other.substrings)
        substrings = ["".join(combo) for combo in combinations]
        return SimpleRule(substrings)


@dataclasses.dataclass
class ReferenceRule:
    """Concatenation of simple rule instances"""
    rule_ids: List[int]
    id: Optional[int] = None

    def is_simplifiable(self, simple_rule_ids: Set[int]) -> bool:
        return simple_rule_ids.issuperset(set(self.rule_ids))

    def as_simple_rule(self, rules_by_id):
        return reduce(lambda x, y: x + y, (rules_by_id[rule_id] for rule_id in self.rule_ids))


@dataclasses.dataclass
class UnionRule:
    """Union of simple/composite rules"""
    rules: List[ReferenceRule]
    id: int

    def is_simplifiable(self, simple_rule_ids: Set[int]) -> bool:
        return all(rule.is_simplifiable(simple_rule_ids) for rule in self.rules)

    def as_simple_rule(self, rules_by_id):
        simplified_rules = [rule.as_simple_rule(rules_by_id) for rule in self.rules]
        substrings = list(chain.from_iterable(rule.substrings for rule in simplified_rules))
        return SimpleRule(substrings, self.id)


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def get_rules_and_messages():
    rules = []
    messages = []
    in_rules_section = True
    for line in get_data_from_input():
        if not line:
            in_rules_section = False
        elif in_rules_section:
            rules.append(line)
        else:
            messages.append(line)
    return rules, messages


def parse_rule(raw_rule):
    # example rules:
    # 54: "a"
    # 95: 97 54
    # 43: 104 54 | 53 117
    try:
        rule_id_str, rule_spec = raw_rule.split(": ")
    except ValueError:
        print(raw_rule)
        raise

    rule_id = int(rule_id_str)
    if '"' in rule_spec:
        # Simple rule
        substring = rule_spec.replace('"', "")
        return SimpleRule([substring], rule_id)
    elif "|" in rule_spec:
        # Union rule
        subrule_specs = rule_spec.split(" | ")
        rules = [ReferenceRule(rule_ids=[int(i) for i in rule_spec.split()]) for rule_spec in subrule_specs]
        return UnionRule(rules, rule_id)
    else:
        # Reference rule
        rule_ids = [int(i) for i in rule_spec.split()]
        return ReferenceRule(rule_ids, rule_id)


def simplify_rules(rules_by_id):
    simple_rules = [rule for rule in rules_by_id.values() if isinstance(rule, SimpleRule)]
    simple_rule_ids = set(rule.id for rule in simple_rules)
    simplifiable_rules = [
        rule for rule in rules_by_id.values()
        if isinstance(rule, (ReferenceRule, UnionRule)) and rule.is_simplifiable(simple_rule_ids)
    ]
    while simplifiable_rules:
        for rule in simplifiable_rules:
            rules_by_id[rule.id] = rule.as_simple_rule(rules_by_id)
        simple_rule_ids = set(rule_id for rule_id, rule in rules_by_id.items() if isinstance(rule, SimpleRule))
        simplifiable_rules = [
            rule for rule in rules_by_id.values()
            if isinstance(rule, (ReferenceRule, UnionRule)) and rule.is_simplifiable(simple_rule_ids)
        ]
    return rules_by_id


RAW_RULES, MESSAGES = get_rules_and_messages()
RULES_BY_ID = {}
for raw_rule in RAW_RULES:
    rule = parse_rule(raw_rule)
    RULES_BY_ID[rule.id] = rule
