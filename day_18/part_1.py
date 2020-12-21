from day_18 import Expression, get_data_from_input


def solve_problem(data):
    return sum(Expression.from_line(line).evaluate() for line in data)


if __name__ == "__main__":
    print(solve_problem(get_data_from_input()))
