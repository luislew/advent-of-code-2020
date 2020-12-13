import math
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        earliest_ts_str, bus_schedule = f.readlines()
        return int(earliest_ts_str), bus_schedule.split(",")


def time_til_next_departure(current_timestamp, bus_id):
    mod = current_timestamp % bus_id
    return bus_id - mod if mod else 0
