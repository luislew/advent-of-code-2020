from math import prod

from day_16 import ALL_ALLOWED_VALUES, FIELD_NAMES, NEARBY_TICKETS, NUM_FIELDS, RULE_VALIDATORS, YOUR_TICKET


def get_valid_tickets(tickets):
    return (ticket for ticket in tickets if all(value in ALL_ALLOWED_VALUES for value in ticket))


def get_allowed_fields_for_all_tickets(tickets):
    allowed_fields_for_all_tickets = [FIELD_NAMES.copy() for _ in range(NUM_FIELDS)]
    for ticket in tickets:
        for idx, value in enumerate(ticket):
            allowed_fields_for_all_tickets[idx] -= {
                field_name for field_name, validator in RULE_VALIDATORS.items() if not validator(value)
            }

    return allowed_fields_for_all_tickets


def get_ordered_field_names(allowed_fields_for_all_tickets):
    ordered_field_names = [None for _ in range(NUM_FIELDS)]
    while None in ordered_field_names:
        for idx, s in enumerate(allowed_fields_for_all_tickets):
            if len(s) == 1:
                field_name = s.pop()
                ordered_field_names[idx] = field_name
                allowed_fields_for_all_tickets = [s - {field_name} for s in allowed_fields_for_all_tickets]
    return ordered_field_names


if __name__ == "__main__":
    valid_tickets = get_valid_tickets(NEARBY_TICKETS)
    allowed_fields_for_all_tickets = get_allowed_fields_for_all_tickets(valid_tickets)
    ordered_field_names = get_ordered_field_names(allowed_fields_for_all_tickets)
    print(prod(v for k, v in zip(ordered_field_names, YOUR_TICKET) if k.startswith("departure")))
