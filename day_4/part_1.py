from day_4 import EXPECTED_KEYS, get_data_from_input, valid_passports_count


def is_valid_passport(passport):
    return set(passport.keys()).issuperset(EXPECTED_KEYS)


if __name__ == "__main__":
    data = get_data_from_input()
    print(valid_passports_count(data, is_valid_passport))
