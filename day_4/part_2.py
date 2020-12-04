import re

from day_4 import EXPECTED_KEYS, get_data_from_input, valid_passports_count

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#   * If cm, the number must be at least 150 and at most 193.
#   * If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
HAIR_COLOR_REGEX = re.compile(r"^#[0-9a-fA-F]{6}$")
VALID_EYE_COLORS = {'amb', 'blu', 'brn', 'grn', 'gry', 'hzl', 'oth'}
PASSPORT_ID_REGEX = re.compile(r"^[0-9]{9}$")


def validate_range(value, minimum, maximum):
    try:
        value_as_int = int(value)
    except ValueError:
        return False
    return minimum <= value_as_int <= maximum


def validate_height(value: str):
    if not value.endswith(("cm", "in")):
        return False

    height, unit = value[:-2], value[-2:]
    return validate_range(height, 150, 193) if unit == "cm" else validate_range(height, 59, 76)


def is_valid_passport(passport):
    if not set(passport.keys()).issuperset(EXPECTED_KEYS):
        return False

    return all([
        HAIR_COLOR_REGEX.match(passport["hcl"]),
        PASSPORT_ID_REGEX.match(passport["pid"]),
        passport["ecl"] in VALID_EYE_COLORS,
        validate_range(passport["byr"], 1920, 2002),
        validate_range(passport["iyr"], 2010, 2020),
        validate_range(passport["eyr"], 2020, 2030),
        validate_height(passport["hgt"]),
    ])


if __name__ == "__main__":
    data = get_data_from_input()
    print(valid_passports_count(data, is_valid_passport))
