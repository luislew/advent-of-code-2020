from day_18 import Expression, get_data_from_input, Op


def add_parens(items):
    # Find consecutive addends and wrap in parentheses
    in_sequence = False
    open_count = 0
    new_items = []
    subitems = []
    for idx, item in enumerate(items):
        if open_count:
            if item == Op.START:
                if open_count:
                    subitems.append(item)
                open_count += 1
            elif item == Op.END:
                open_count -= 1
                if not open_count:
                    new_items.extend(add_parens(subitems))
                    new_items.append(Op.END)
                    subitems = []
                else:
                    subitems.append(Op.END)
            else:
                subitems.append(item)
        else:
            if item == Op.START:
                open_count += 1
            elif item == Op.ADD:
                if not in_sequence:
                    in_sequence = True
                    if new_items[-1].isdigit():
                        new_items.insert(-1, Op.START)
                    elif new_items[-1] == Op.END:
                        # Find opening paren and insert before
                        close_count = 0
                        for rev_idx, rev_item in enumerate(reversed(new_items)):
                            if rev_item == Op.END:
                                close_count += 1
                            elif rev_item == Op.START:
                                close_count -= 1
                                if not close_count:
                                    break
                        new_items.insert(-rev_idx - 1, Op.START)
            new_items.append(item)
            if item == Op.MULT and in_sequence:
                in_sequence = False
                new_items.insert(-1, Op.END)
    if in_sequence:
        new_items.append(Op.END)
    return new_items


def solve_problem(data):
    total = 0
    for line in data:
        items = Expression.from_line(line).items
        items = add_parens(items)
        total += Expression(items).evaluate()
    return total


if __name__ == "__main__":
    print(solve_problem(get_data_from_input()))
