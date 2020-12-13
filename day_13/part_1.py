from day_13 import get_data_from_input, time_til_next_departure


def get_earliest_departure_info(earliest_timestamp, bus_ids):
    bus_ids = [int(bus_id) for bus_id in bus_ids if bus_id != "x"]
    return min((time_til_next_departure(earliest_timestamp, bus_id), bus_id) for bus_id in bus_ids)


if __name__ == "__main__":
    time_diff, bus_id = get_earliest_departure_info(*get_data_from_input())
    print(time_diff, bus_id)
    print(time_diff * bus_id)
