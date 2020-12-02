from day_2 import get_data_from_input


def valid_passwords_count(data):
    return sum(
        1 for low, high, letter, password in data
        if (password[low - 1] == letter) != (password[high - 1] == letter)
    )


if __name__ == "__main__":
    data = get_data_from_input()
    print(valid_passwords_count(data))
