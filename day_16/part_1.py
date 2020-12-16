from day_16 import ALL_ALLOWED_VALUES, NEARBY_TICKETS


def get_ticket_scanning_error_rate(tickets):
    return sum(value for ticket in tickets for value in ticket if value not in ALL_ALLOWED_VALUES)


if __name__ == "__main__":
    print(get_ticket_scanning_error_rate(NEARBY_TICKETS))
