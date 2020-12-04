import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

EXPECTED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        record = {}
        for line in f:
            if not line.strip():  # Found a blank link marking end of record
                yield record
                record = {}
                continue

            kv_pairs = line.strip().split()
            for pair in kv_pairs:
                k, v = pair.split(":")
                record[k] = v
        yield record


def valid_passports_count(data, passport_validator):
    return sum(1 for passport in data if passport_validator(passport))
